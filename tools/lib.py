"""Chart Snack shared render kit: drawing helpers, scene renderer, music/SFX, voiceover, final mix."""
import subprocess, sys, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BG = (18, 20, 28)
WHITE = (255, 255, 255)
GREY = (150, 156, 175)
TRACK = (42, 46, 61)
Y1, Y2, Y3 = (255, 200, 61), (255, 159, 28), (255, 90, 54)
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
_fc = {}
def F(size, bold=True):
    k = (size, bold)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(FB if bold else FM, size)
    return _fc[k]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_io(x): x = clamp(x); return 3 * x * x - 2 * x * x * x
def mix(c, a): return tuple(int(BG[i] + (c[i] - BG[i]) * a) for i in range(3))
def appear(t, start, dur=0.35): return ease((t - start) / dur)
def fmt(n): return f"{int(round(n)):,}"

def text(d, xy, s, size, col, a=1.0, bold=True, anchor="mm"):
    if a <= 0: return
    x, y = xy
    d.text((x, y + (1 - a) * 40), s, font=F(size, bold), fill=mix(col, a), anchor=anchor)

def logo(d, x0, y0, s, a=1.0, grow=1.0, radius=3):
    for (bx, by, bw, bh, c) in [(180, 440, 120, 160, Y1), (340, 340, 120, 260, Y2), (500, 200, 120, 400, Y3)]:
        h = bh * s * grow
        if h > 1:
            d.rounded_rectangle([x0 + bx * s, y0 + (by + bh) * s - h, x0 + (bx + bw) * s, y0 + (by + bh) * s], radius=radius, fill=mix(c, a))

def frame_base():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    logo(d, 380, 210, 0.09)
    d.text((450, 246), "CHART SNACK", font=F(34), fill=GREY, anchor="lm")
    return im, d

def bar(d, x0, y0, x1, y1, frac, col, a=1.0, r=14, minw=0):
    d.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=mix(TRACK, a))
    w = (x1 - x0) * clamp(frac)
    if w > 1 or minw:
        w = max(w, minw)
        if w >= 2 * r:
            d.rounded_rectangle([x0, y0, x0 + w, y1], radius=r, fill=mix(col, a))
        else:
            d.rectangle([x0, y0, x0 + max(w, 3), y1], fill=mix(col, a))

def outro(t, D):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    s = 0.55
    logo(d, 540 - 400 * s, 560, s, appear(t, 0, 0.5), grow=ease((t - 0.1) / 0.6), radius=12)
    text(d, (540, 1000), "CHART SNACK", 96, WHITE, appear(t, 0.6))
    text(d, (540, 1100), "A new chart snack every day.", 46, GREY, appear(t, 1.0), bold=False)
    text(d, (540, 1300), "Follow for tomorrow's snack", 44, Y1, appear(t, 1.6))
    return im

FADE = 0.25
def render_scene(name, fn, dur, outdir, fade_in=True):
    n = int(round(dur * FPS))
    tmp = os.path.join(outdir, f"{name}.tmp.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", tmp]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    blank = Image.new("RGB", (W, H), BG)
    for i in range(n):
        t = i / FPS
        im = fn(t, dur)
        fa = min(1.0, (dur - t) / FADE, (t / FADE) if fade_in else 1.0)
        if fa < 1.0:
            im = Image.blend(blank, im, max(0.0, fa))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    if p.wait() != 0: sys.exit(f"ffmpeg failed on {name}")
    os.replace(tmp, os.path.join(outdir, f"{name}.mp4"))

# ---------------- audio ----------------
SR = 44100
def music(path, dur, scene_starts, ticks, dings, beat_from=5.0, seed=7, bpm=100):
    from scipy.io import wavfile
    from scipy.signal import butter, sosfilt
    N = int(SR * dur); out = np.zeros(N); rng = np.random.default_rng(seed)
    def add(sig, t0, g=1.0):
        i = int(t0 * SR)
        if i >= N or i < 0: return
        j = min(N, i + len(sig)); out[i:j] += sig[: j - i] * g
    lp = lambda x, f: sosfilt(butter(2, f, "low", fs=SR, output="sos"), x)
    hp = lambda x, f: sosfilt(butter(2, f, "high", fs=SR, output="sos"), x)
    bp = lambda x, lo, hi: sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)
    note = lambda m: 440 * 2 ** ((m - 69) / 12)
    def env(n, a, r):
        e = np.ones(n); ai, ri = int(a * SR), int(r * SR)
        e[:ai] = np.linspace(0, 1, ai); e[-ri:] *= np.linspace(1, 0, ri); return e
    chords = [[57, 60, 64], [53, 57, 60], [48, 55, 64], [55, 59, 62]]
    cl = 4.0; t = np.arange(int(cl * SR)) / SR
    for k in range(int(dur / cl) + 1):
        ch = chords[k % 4]; s = np.zeros_like(t)
        for m in ch + [ch[0] - 12]:
            for det in (-0.12, 0.12):
                f = note(m) * (1 + det / 100)
                s += (2 * ((f * t) % 1) - 1) * 0.5 + np.sin(2 * np.pi * f * t) * 0.5
        add(lp(s, 900) * env(len(t), 0.6, 0.8), k * cl, 0.018)
    beat = 60 / bpm; kt = np.arange(int(0.25 * SR)) / SR
    kick = np.sin(2 * np.pi * np.cumsum(50 + 90 * np.exp(-kt * 30)) / SR) * np.exp(-kt * 14)
    hl = int(0.05 * SR); hat = hp(rng.standard_normal(hl), 7000) * np.exp(-np.arange(hl) / SR * 80)
    b = beat_from
    while b < dur - 5:
        add(kick, b, 0.35); add(hat, b + beat / 2, 0.06); b += beat
    cl_ = int(0.012 * SR); click = np.sin(2 * np.pi * 2200 * np.arange(cl_) / SR) * np.exp(-np.arange(cl_) / SR * 400)
    for (s0, s1) in ticks:
        tt = s0
        while tt < s1:
            x = (tt - s0) / (s1 - s0); add(click, tt, 0.12); tt += 1 / (5 + 20 * np.sin(np.pi * x))
    wl = int(0.45 * SR)
    for ts in scene_starts[1:]:
        nz = rng.standard_normal(wl)
        sw = np.concatenate([bp(nz[i:i + 2205], 300 + 3000 * i / wl, 600 + 5000 * i / wl) for i in range(0, wl, 2205)])[:wl]
        add(sw * np.sin(np.linspace(0, np.pi, wl)) ** 2, ts - 0.3, 0.35)
    def ding(f, d=1.2):
        tt = np.arange(int(d * SR)) / SR
        return (np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(4 * np.pi * f * tt) + 0.15 * np.sin(6 * np.pi * f * tt)) * np.exp(-tt * 4)
    scale = [72, 76, 79, 83, 84, 88]
    for i, ts in enumerate(dings): add(ding(note(scale[i % len(scale)])), ts, 0.16)
    out[: int(0.05 * SR)] *= np.linspace(0, 1, int(0.05 * SR))
    out[-int(1.5 * SR):] *= np.linspace(1, 0, int(1.5 * SR))
    out = out / np.max(np.abs(out)) * 0.707
    wavfile.write(path, SR, (np.stack([out, out], 1) * 32767).astype(np.int16))

VOICE = "kokoro:am_michael"   # or "piper:de_DE-thorsten-high" (German, CC0) – see PLAYBOOK "Voices"
PIPER_DIR = "/home/claude/tts/piper"
_tts = {}

def _synth(txt, voice, speed):
    """returns (float32 mono array, sample_rate)"""
    eng, name = voice.split(":", 1)
    if eng == "kokoro":
        from kokoro_onnx import Kokoro
        if "k" not in _tts: _tts["k"] = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
        return _tts["k"].create(txt, voice=name, speed=speed, lang="en-gb" if name[0] == "b" else "en-us")
    if eng == "piper":
        import glob, io, wave
        from piper import PiperVoice, SynthesisConfig
        base, _, sid = name.partition("#")
        if base not in _tts: _tts[base] = PiperVoice.load(glob.glob(f"{PIPER_DIR}/vits-piper-{base}/*.onnx")[0])
        v = _tts[base]; buf = io.BytesIO()
        with wave.open(buf, "wb") as w:
            v.synthesize_wav(txt, w, syn_config=SynthesisConfig(speaker_id=int(sid) if sid else None, length_scale=1.0 / speed))
        buf.seek(0)
        with wave.open(buf) as w:
            a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
            return a, w.getframerate()
    raise ValueError(voice)

def voiceover(path, dur, lines, voice=None, speed=1.1):
    """lines: (scene_start, scene_len, offset, text). Prints fit report; returns False if any line is too long."""
    import soundfile as sf
    voice = voice or VOICE
    vsr = 24000; track = np.zeros(int(dur * vsr)); ok = True
    for st, ln, off, txt in lines:
        a, sr = _synth(txt, voice, speed)
        if sr != vsr:
            a = np.interp(np.arange(0, len(a), sr / vsr), np.arange(len(a)), a)
        dd = len(a) / vsr; room = ln - off - 0.2
        print(f"{st:>5}s  {dd:5.2f}s / {room:5.2f}s  {'OK' if dd <= room else 'TOO LONG'}")
        ok &= dd <= room
        i = int((st + off) * vsr); track[i:i + len(a)] += a[: len(track) - i]
    sf.write(path, track, vsr)
    return ok

# voice "mastering" (since 2026-11-10): remove rumble, tame peaks, add presence -> clearer on phone speakers
VO_FX = "highpass=f=90,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3500:t=q:w=1.2:g=3,acompressor=threshold=-20dB:ratio=3:attack=5:release=80:makeup=2"

def build(outdir, scenes, lines, ticks, dings, final_name, only=None):
    os.makedirs(outdir, exist_ok=True)
    starts, t = [], 0.0
    for _, _, d in scenes: starts.append(t); t += d
    dur = t
    for i, (name, fn, d) in enumerate(scenes):
        if only and name not in only: continue
        render_scene(name, fn, d, outdir, fade_in=(i > 0)); print("done", name, flush=True)
    with open(os.path.join(outdir, "list.txt"), "w") as f:
        for name, _, _ in scenes: f.write(f"file '{name}.mp4'\n")
    run = lambda *a: subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *a], check=True, cwd=outdir)
    run("-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "video.mp4")
    music(os.path.join(outdir, "music.wav"), dur, starts, ticks, dings)
    if not voiceover(os.path.join(outdir, "vo.wav"), dur, lines): print("WARNING: a voice line is too long")
    run("-i", "video.mp4", "-i", "music.wav", "-i", "vo.wav", "-filter_complex",
        "[1:a]volume=0.35[m];[2:a]aresample=44100,"+VO_FX+",pan=stereo|c0=c0|c1=c0,volume=1.6[v];[m][v]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", final_name)
    print("final", os.path.join(outdir, final_name), "starts", starts)

def stills(outdir, scenes, at):
    os.makedirs(outdir, exist_ok=True)
    ims = []
    for (name, fn, d), t in zip(scenes, at):
        ims.append(fn(t, d).resize((360, 640)))
    sheet = Image.new("RGB", (360 * len(ims), 640), BG)
    for i, im in enumerate(ims): sheet.paste(im, (360 * i, 0))
    sheet.save(os.path.join(outdir, "stills.png"))

# --- subscribe hook (since ep06) ---
RED = (255, 48, 64)
def sub_pill(d, t, start, y=1600, dur=2.2):
    """Animated SUBSCRIBE button: pops in at start, 'clicked' at start+0.9, gone after dur."""
    lt = t - start
    if lt < 0 or lt > dur: return
    a = ease(lt / 0.25) * (1 - ease((lt - dur + 0.3) / 0.3))
    clicked = lt > 0.9
    sc = 1 + 0.12 * math.sin(clamp((lt - 0.85) / 0.2) * math.pi)
    w, h = 470 * sc, 120 * sc
    col = (70, 74, 90) if clicked else RED
    d.rounded_rectangle([540 - w / 2, y - h / 2, 540 + w / 2, y + h / 2], radius=int(h / 2), fill=mix(col, a))
    d.text((540, y), "SUBSCRIBED" if clicked else "SUBSCRIBE", font=F(int(52 * sc)), fill=mix(WHITE, a), anchor="mm")
    if 0.6 < lt < 1.1:  # little cursor tap
        cx, cy = 540 + 150, y + 40
        r = 28 + 10 * (lt - 0.6)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=mix(WHITE, a), width=5)

def outro_next(teaser):
    def fn(t, D):
        im = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(im)
        s = 0.42
        logo(d, 540 - 400 * s, 470, s, appear(t, 0, 0.5), grow=ease((t - 0.1) / 0.6), radius=10)
        text(d, (540, 820), "NEXT SNACK:", 44, GREY, appear(t, 0.5))
        text(d, (540, 920), teaser, 58, Y1, appear(t, 0.8))
        text(d, (540, 1100), "New chart every day.", 46, WHITE, appear(t, 1.2), bold=False)
        sub_pill(d, t, 1.4, y=1320, dur=10)
        return im
    return fn

def sub_scene(line1="Quick:"):
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 760), line1, 80, WHITE, appear(t, 0))
        text(d, (540, 870), "new chart every day", 52, GREY, appear(t, 0.15), bold=False)
        sub_pill(d, t, 0.2, y=1080, dur=D)
        return im
    return fn

def hfmt(m):
    if m < 10: return f"{m:.2f} m"
    if m < 1000: return f"{fmt(m)} m"
    if m < 10000: return f"{m/1000:.2f} km"
    return f"{fmt(m/1000)} km"

def run(out, final, YT, TT, stills_at_yt, stills_at_tt, DE=None, stills_at_de=None):
    """argv: [yt|tt|de] [stills|<only>...]   de = German TikTok cut (piper voice)"""
    global VOICE
    mode = sys.argv[1] if len(sys.argv) > 1 else "yt"
    rest = sys.argv[2:]
    cfg = {"yt": YT, "tt": TT, "de": DE}[mode]
    o = out + {"yt": "/out", "tt": "/out_tt", "de": "/out_de"}[mode]
    if mode == "de": VOICE = "piper:de_DE-thorsten-high"
    if rest == ["stills"]:
        stills(o, cfg[0], {"yt": stills_at_yt, "tt": stills_at_tt, "de": stills_at_de or stills_at_tt}[mode])
    else:
        build(o, *cfg, final.replace(".mp4", {"yt": "", "tt": "_tt", "de": "_de"}[mode]) + ".mp4", only=rest or None)
