"""Chart Snack LONG-FORM kit (16:9, 1920x1080). Since 2026-11-13.
A video is a list of BEATS: Beat(fn, vo_text, min_dur). The voiceover is synthesized FIRST, and every
beat lasts max(min_dur, vo_length + pad) -> picture and voice can never drift apart.
fn(t, D, ctx) draws one frame (t = seconds into the beat, D = beat length)."""
import os, sys, math, subprocess
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, "/home/claude/chartsnack")
import lib
from lib import F, clamp, ease, ease_io, Y1, Y2, Y3, WHITE, GREY, TRACK, BG, logo

W, H, FPS = 1920, 1080, 30
BLUE = (80, 160, 255)
GREEN = (90, 200, 120)
DGREY = (110, 116, 135)

def mixc(c, a, base=BG): return tuple(int(base[i] + (c[i] - base[i]) * a) for i in range(3))
def appear(t, s, d=0.4): return ease((t - s) / d)
def fmtn(n): return f"{int(round(n)):,}"

class Beat:
    def __init__(self, fn, vo, min_dur=3.0, pad=0.8, chapter=None):
        self.fn, self.vo, self.min_dur, self.pad, self.chapter = fn, vo, min_dur, pad, chapter

# ---------------- drawing helpers ----------------
_bg = {}
def background(t):
    """dark vertical gradient + slowly drifting dot grid (subtle motion = 'alive' frame)"""
    if "g" not in _bg:
        g = np.zeros((H, W, 3), np.uint8)
        for i, c in enumerate(BG):
            g[:, :, i] = np.linspace(c + 6, max(0, c - 6), H)[:, None]
        _bg["g"] = g
    im = Image.fromarray(_bg["g"].copy())
    d = ImageDraw.Draw(im)
    off = (t * 6) % 60
    for y in range(-60, H + 60, 60):
        for x in range(-60, W + 60, 60):
            d.point((x + off, y + off * 0.5), fill=(40, 44, 58))
    return im, d

def text(d, xy, s, size, col, a=1.0, bold=True, anchor="mm", dy=30):
    if a <= 0: return
    x, y = xy
    d.text((x, y + (1 - a) * dy), s, font=F(size, bold), fill=mixc(col, a), anchor=anchor)

def chrome(d, ctx, t):
    """brand top-left, chapter name top-right, chapter progress bar at the bottom"""
    logo(d, 40, 30, 0.08)
    d.text((105, 62), "CHART SNACK", font=F(26), fill=GREY, anchor="lm")
    if ctx.get("chapter"):
        d.text((W - 40, 62), ctx["chapter"].upper(), font=F(26), fill=GREY, anchor="rm")
    n = ctx.get("nchap", 1); i = ctx.get("ichap", 0)
    seg = (W - 80) / n
    for k in range(n):
        x0 = 40 + k * seg + 4; x1 = 40 + (k + 1) * seg - 4
        col = Y2 if k < i else ((Y1) if k == i else TRACK)
        d.rounded_rectangle([x0, H - 22, x1, H - 14], radius=4, fill=col)
        if k == i:
            fx = x0 + (x1 - x0) * clamp(ctx.get("chap_p", 0))
            d.rounded_rectangle([x0, H - 22, max(x0 + 8, fx), H - 14], radius=4, fill=Y3)

def hbar(d, x0, y0, x1, y1, frac, col, a=1.0, r=14):
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=mixc(TRACK, a))
    w = (x1 - x0) * clamp(frac)
    if w >= 2 * r: d.rounded_rectangle([x0, y0, x0 + w, y1], radius=r, fill=mixc(col, a))
    elif w > 0.5: d.rectangle([x0, y0, x0 + max(w, 4), y1], fill=mixc(col, a))

def glow_circle(d, cx, cy, r, col, a=1.0):
    for k in range(6, 0, -1):
        rr = r * (1 + k * 0.12)
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=mixc(col, a * 0.08))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mixc(col, a))

# ---------------- build ----------------
def render_beat(path, fn, D, ctx):
    n = int(round(D * FPS))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", "-pix_fmt", "yuv420p", path + ".tmp.mp4"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        c = dict(ctx); c["chap_p"] = (ctx["chap_t0"] + t) / ctx["chap_len"]
        im = fn(t, D, c)
        fa = min(1.0, (D - t) / 0.2, t / 0.2 if ctx.get("fade_in", True) else 1.0)
        if fa < 1.0: im = Image.blend(Image.new("RGB", (W, H), BG), im, max(0.0, fa))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    if p.wait() != 0: sys.exit("ffmpeg failed")
    os.replace(path + ".tmp.mp4", path)

def plan(beats, outdir):
    """synthesize every VO line once (cached on disk) and compute beat durations"""
    import soundfile as sf
    os.makedirs(outdir + "/vo", exist_ok=True)
    durs = []
    for i, b in enumerate(beats):
        f = f"{outdir}/vo/{i:03d}.wav"
        key = f + ".txt"
        if b.vo and not (os.path.exists(f) and open(key).read() == b.vo):
            a, sr = lib._synth(b.vo, lib.VOICE, lib.VOICE_SPEED)
            sf.write(f, a, sr); open(key, "w").write(b.vo)
        vlen = sf.info(f).duration if b.vo else 0.0
        durs.append(round(max(b.min_dur, vlen + b.pad + 0.3), 2))
    return durs

def build(beats, outdir, final, chapters, only=None, workers=2):
    """chapters: list of chapter names; Beat.chapter = index into it"""
    import soundfile as sf
    durs = plan(beats, outdir)
    starts = list(np.cumsum([0] + durs[:-1]))
    total = sum(durs)
    # chapter bookkeeping
    chap_of = []; cur = 0
    for b in beats:
        if b.chapter is not None: cur = b.chapter
        chap_of.append(cur)
    chap_start = {}; chap_len = {}
    for i, c in enumerate(chap_of):
        chap_start.setdefault(c, starts[i]); chap_len[c] = chap_len.get(c, 0) + durs[i]
    jobs = []
    for i, b in enumerate(beats):
        c = chap_of[i]
        ctx = dict(chapter=chapters[c], ichap=c, nchap=len(chapters), chap_t0=starts[i] - chap_start[c], chap_len=chap_len[c], fade_in=i > 0)
        jobs.append((i, b, durs[i], ctx))
    todo = [j for j in jobs if (only is None or j[0] in only) and not (only is None and os.path.exists(f"{outdir}/b{j[0]:03d}.mp4"))]
    # render in parallel (fork)
    import multiprocessing as mp
    global _BEATS; _BEATS = beats
    with mp.get_context("fork").Pool(workers) as pool:
        pool.starmap(_rb, [(outdir, i, D, ctx) for (i, b, D, ctx) in todo])
    with open(f"{outdir}/list.txt", "w") as f:
        for i in range(len(beats)): f.write(f"file 'b{i:03d}.mp4'\n")
    run = lambda *a: subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *a], check=True, cwd=outdir)
    run("-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "video.mp4")
    # voice track
    vsr = 24000; track = np.zeros(int(total * vsr) + vsr)
    for i, b in enumerate(beats):
        if not b.vo: continue
        a, sr = sf.read(f"{outdir}/vo/{i:03d}.wav", dtype="float32")
        if sr != vsr: a = np.interp(np.arange(0, len(a), sr / vsr), np.arange(len(a)), a)
        k = int((starts[i] + 0.3) * vsr); track[k:k + len(a)] += a[: len(track) - k]
    sf.write(f"{outdir}/vo.wav", track, vsr)
    ticks = []; dings = [s + 0.1 for s, b in zip(starts, beats) if b.chapter is not None]
    lib.music(f"{outdir}/music.wav", total, starts, ticks, dings, beat_from=4.0, bpm=92)
    run("-i", "video.mp4", "-i", "music.wav", "-i", "vo.wav", "-filter_complex",
        "[1:a]volume=0.22[m];[2:a]aresample=44100," + lib.VO_FX + ",pan=stereo|c0=c0|c1=c0,volume=1.6[v];[m][v]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", final)
    # chapter timestamps for the description
    marks = []
    for c in range(len(chapters)):
        m, s = divmod(int(chap_start[c]), 60); marks.append(f"{m}:{s:02d} {chapters[c]}")
    print("final", f"{outdir}/{final}", "length", round(total, 1)); print("\n".join(marks))
    open(f"{outdir}/chapters.txt", "w").write("\n".join(marks))
    return durs

_BEATS = []
def _rb(outdir, i, D, ctx):
    render_beat(f"{outdir}/b{i:03d}.mp4", _BEATS[i].fn, D, ctx); print("beat", i, D, flush=True)

def stills(beats, outdir, chapters, idx, at=0.85):
    """contact sheet of selected beats at fraction `at` of a nominal 6 s beat"""
    os.makedirs(outdir, exist_ok=True)
    ims = []
    for i in idx:
        b = beats[i]; D = max(b.min_dur, 6.0)
        c = next((beats[j].chapter for j in range(i, -1, -1) if beats[j].chapter is not None), 0)
        ctx = dict(chapter=chapters[c], ichap=c, nchap=len(chapters), chap_t0=0, chap_len=1, chap_p=0.5)
        ims.append(b.fn(D * at, D, ctx).resize((640, 360)))
    cols = 3; rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (640 * cols, 360 * rows), BG)
    for k, im in enumerate(ims): sheet.paste(im, (640 * (k % cols), 360 * (k // cols)))
    sheet.save(f"{outdir}/stills.png")
