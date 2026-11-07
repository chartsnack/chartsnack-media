import subprocess, sys, os, math
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
def mix(c, a):  # fade colour toward bg
    return tuple(int(BG[i] + (c[i] - BG[i]) * a) for i in range(3))
def appear(t, start, dur=0.35): return ease((t - start) / dur)

def text(d, xy, s, size, col, a=1.0, bold=True, anchor="mm", dy=0):
    if a <= 0: return
    x, y = xy
    d.text((x, y + (1 - a) * 40 + dy), s, font=F(size, bold), fill=mix(col, a), anchor=anchor)

def fmt(n): return f"{int(round(n)):,}"

def brand(d):
    # small logo + wordmark (inside top safe area)
    x0, y0, s = 380, 210, 0.09
    for (bx, by, bw, bh, c) in [(180, 440, 120, 160, Y1), (340, 340, 120, 260, Y2), (500, 200, 120, 400, Y3)]:
        d.rounded_rectangle([x0 + bx * s, y0 + by * s, x0 + (bx + bw) * s, y0 + (by + bh) * s], radius=3, fill=c)
    d.text((x0 + 70, y0 + 36), "CHART SNACK", font=F(34), fill=GREY, anchor="lm")

def frame_base():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    brand(d)
    return im, d

# ---------------- scenes ----------------
def s1(t, D):  # hook 5s
    im, d = frame_base()
    text(d, (540, 640), "1,000,000 seconds", 92, WHITE, appear(t, 0.0))
    text(d, (540, 770), "= 11.6 days", 120, Y1, appear(t, 0.5))
    text(d, (540, 1010), "1,000,000,000 seconds", 82, WHITE, appear(t, 2.0))
    a = appear(t, 2.6)
    pulse = 1 + 0.06 * math.sin(max(0, t - 2.6) * 7)
    if a > 0:
        d.text((540, 1170 + (1 - a) * 40), "= ???", font=F(int(170 * pulse)), fill=mix(Y3, a), anchor="mm")
    text(d, (540, 1420), "Guess before the end", 46, GREY, appear(t, 3.4), bold=False)
    return im

def s2(t, D):  # million 13s
    im, d = frame_base()
    text(d, (540, 420), "1 MILLION SECONDS", 70, Y1, appear(t, 0))
    p = ease_io((t - 0.6) / 8.5)
    secs = 1e6 * p
    text(d, (540, 560), fmt(secs), 104, WHITE, appear(t, 0.2))
    text(d, (540, 650), "seconds", 40, GREY, appear(t, 0.2), bold=False)
    days = secs / 86400.0
    sq, gap, cols = 150, 24, 4
    x0 = (W - (cols * sq + (cols - 1) * gap)) // 2
    y0 = 760
    ga = appear(t, 0.4)
    for i in range(12):
        r, c = divmod(i, cols)
        x, y = x0 + c * (sq + gap), y0 + r * (sq + gap)
        d.rounded_rectangle([x, y, x + sq, y + sq], radius=18, fill=mix(TRACK, ga))
        fill = clamp(days - i)
        if fill > 0:
            h = sq * fill
            d.rounded_rectangle([x, y + sq - h, x + sq, y + sq], radius=18, fill=mix(Y1, ga))
        d.text((x + sq / 2, y + sq / 2), f"Day {i+1}", font=F(30), fill=mix(BG if fill > 0.55 else GREY, ga), anchor="mm")
    text(d, (540, 1340), "≈ 11 days, 14 hours", 78, Y1, appear(t, 9.4))
    text(d, (540, 1440), "Less than two weeks.", 44, GREY, appear(t, 10.2), bold=False)
    return im

def s3(t, D):  # billion 15s
    im, d = frame_base()
    text(d, (540, 420), "1 BILLION SECONDS", 70, Y2, appear(t, 0))
    p = ease_io((t - 0.6) / 9.5)
    secs = 1e9 * p
    text(d, (540, 560), fmt(secs), 96, WHITE, appear(t, 0.2))
    text(d, (540, 650), "seconds", 40, GREY, appear(t, 0.2), bold=False)
    years = secs / 31557600.0
    bx0, bx1 = 90, 900
    a = appear(t, 0.5)
    # million row
    text(d, (bx0, 790), "1 MILLION", 40, Y1, a, anchor="lm")
    d.rounded_rectangle([bx0, 830, bx1, 890], radius=14, fill=mix(TRACK, a))
    d.rectangle([bx0, 830, bx0 + 6, 890], fill=mix(Y1, a))
    text(d, (bx0 + 24, 860), "11.6 days (that tiny sliver)", 34, GREY, a, bold=False, anchor="lm")
    # billion row
    text(d, (bx0, 990), "1 BILLION", 40, Y2, a, anchor="lm")
    d.rounded_rectangle([bx0, 1030, bx1, 1090], radius=14, fill=mix(TRACK, a))
    w = (bx1 - bx0) * p
    if w > 2:
        d.rounded_rectangle([bx0, 1030, bx0 + max(w, 28), 1090], radius=14, fill=mix(Y2, a))
    text(d, (540, 1230), f"{years:.1f} years", 110, WHITE, appear(t, 0.8))
    text(d, (540, 1380), "≈ 31 years, 8 months", 60, Y2, appear(t, 10.4))
    text(d, (540, 1470), "Born on second one? You'd be 31.", 42, GREY, appear(t, 11.4), bold=False)
    return im

def s4(t, D):  # trillion 17s
    im, d = frame_base()
    text(d, (540, 420), "1 TRILLION SECONDS", 70, Y3, appear(t, 0))
    p = ease_io((t - 0.6) / 9.0)
    secs = 1e12 * p
    text(d, (540, 560), fmt(secs), 84, WHITE, appear(t, 0.2))
    text(d, (540, 650), "seconds", 40, GREY, appear(t, 0.2), bold=False)
    years = secs / 31557600.0
    text(d, (540, 790), f"{fmt(years)} years", 100, WHITE, appear(t, 0.8))
    # timeline: left = 31,700 years ago, right = today
    lx0, lx1, ly = 90, 880, 1080
    a = appear(t, 0.6)
    d.rounded_rectangle([lx0, ly - 6, lx1, ly + 6], radius=6, fill=mix(TRACK, a))
    span = 31700.0
    fx = lx1 - (lx1 - lx0) * min(years, span) / span
    if lx1 - fx > 2:
        d.rounded_rectangle([fx, ly - 6, lx1, ly + 6], radius=6, fill=mix(Y3, a))
    d.ellipse([lx1 - 14, ly - 14, lx1 + 14, ly + 14], fill=mix(WHITE, a))
    text(d, (lx1, ly + 50), "TODAY", 34, WHITE, a, anchor="rm")
    # pyramids marker (~4,580 years ago)
    px = lx1 - (lx1 - lx0) * 4580 / span
    pa = appear(t, 0.6 + 9.0 * 0.32) * a if years > 4580 else 0
    if pa > 0:
        d.ellipse([px - 11, ly - 11, px + 11, ly + 11], fill=mix(Y1, pa))
        text(d, (px + 20, ly - 70), "Great Pyramid", 34, Y1, pa, anchor="rm")
        text(d, (px + 20, ly - 32), "built", 30, GREY, pa, bold=False, anchor="rm")
    ma = appear(t, 9.8)
    if ma > 0:
        d.ellipse([lx0 - 14, ly - 14, lx0 + 14, ly + 14], fill=mix(Y3, ma))
        text(d, (lx0, ly + 52), "31,688 years ago", 34, Y3, ma, anchor="lm")
    text(d, (540, 1300), "1 trillion seconds ago,", 52, WHITE, appear(t, 10.6))
    text(d, (540, 1375), "woolly mammoths still", 52, Y3, appear(t, 11.1))
    text(d, (540, 1450), "roamed Europe.", 52, Y3, appear(t, 11.4))
    return im

def s5(t, D):  # scale 10s
    im, d = frame_base()
    text(d, (540, 430), "Make it physical:", 64, WHITE, appear(t, 0))
    text(d, (540, 515), "1 million seconds = 1 cm", 48, GREY, appear(t, 0.4), bold=False)
    rows = [(0.9, "1 MILLION", "1 cm", "a fingertip", Y1),
            (2.6, "1 BILLION", "10 m", "a 3-story building", Y2),
            (4.6, "1 TRILLION", "10 km", "taller than Mount Everest", Y3)]
    y = 720
    for st, lab, val, sub, c in rows:
        a = appear(t, st)
        text(d, (90, y), lab, 44, c, a, anchor="lm")
        text(d, (900, y), val, 76, WHITE, a, anchor="rm")
        text(d, (90, y + 70), sub, 40, GREY, a, bold=False, anchor="lm")
        y += 260
    return im

def s6(t, D):  # outro 5s
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    a = appear(t, 0, 0.5)
    s, x0, y0 = 0.55, 540 - 400 * 0.55, 560
    for (bx, by, bw, bh, c) in [(180, 440, 120, 160, Y1), (340, 340, 120, 260, Y2), (500, 200, 120, 400, Y3)]:
        h = bh * s * ease((t - 0.1 - bx / 2000) / 0.6)
        if h > 1:
            d.rounded_rectangle([x0 + bx * s, y0 + (by + bh) * s - h, x0 + (bx + bw) * s, y0 + (by + bh) * s], radius=12, fill=mix(c, a))
    text(d, (540, 1000), "CHART SNACK", 96, WHITE, appear(t, 0.6))
    text(d, (540, 1100), "A new chart snack every day.", 46, GREY, appear(t, 1.0), bold=False)
    text(d, (540, 1300), "Follow for tomorrow's snack", 44, Y1, appear(t, 1.6))
    return im

SCENES = [("s1", s1, 5.0), ("s2", s2, 13.0), ("s3", s3, 15.0), ("s4", s4, 17.0), ("s5", s5, 10.0), ("s6", s6, 5.0)]
FADE = 0.25

def render_scene(name, fn, dur, outdir):
    n = int(round(dur * FPS))
    tmp = os.path.join(outdir, f"{name}.tmp.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", tmp]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        im = fn(t, dur)
        fa = min(1.0, t / FADE, (dur - t) / FADE) if name != "s1" else min(1.0, (dur - t) / FADE)
        if fa < 1.0:
            im = Image.blend(Image.new("RGB", (W, H), BG), im, max(0.0, fa))
        p.stdin.write(im.tobytes())
    p.stdin.close()
    if p.wait() == 0:
        os.replace(tmp, os.path.join(outdir, f"{name}.mp4"))
    else:
        sys.exit(f"ffmpeg failed on {name}")

if __name__ == "__main__":
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    if len(sys.argv) > 2 and sys.argv[2] == "stills":
        # preview the busiest moments
        for name, fn, dur, t in [("s1", s1, 5, 4.5), ("s2", s2, 13, 12), ("s3", s3, 15, 14), ("s4", s4, 17, 16), ("s5", s5, 10, 9), ("s6", s6, 5, 4)]:
            fn(t, dur).save(os.path.join(outdir, f"still_{name}.png"))
    else:
        only = sys.argv[2:] or [s[0] for s in SCENES]
        for name, fn, dur in SCENES:
            if name in only:
                render_scene(name, fn, dur, outdir)
                print("done", name, flush=True)
