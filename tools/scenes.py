"""Reusable Chart Snack scene builders (since ep09). Import after lib: `from scenes import *`.
Each builder returns fn(t, D) -> PIL image. Keep the first scene fully visible at t=0 (hook())."""
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *
import lib

# --- language switch: `python3 epNN.py de` builds the German TikTok cut ---
DE = len(sys.argv) > 1 and sys.argv[1] == "de"
def T(en, de):
    return de if DE else en
if DE:
    def fmt(n): return f"{int(round(n)):,}".replace(",", ".")
    lib.fmt = fmt

DGREY = (110, 116, 135)

def hook(lines, pulse_idx=None):
    """lines: (y, text, size, color, bold). Everything visible at t=0; line pulse_idx pulses."""
    def fn(t, D):
        im, d = frame_base()
        for i, (y, s, size, col, bold) in enumerate(lines):
            if i == pulse_idx:
                p = 1 + 0.05 * math.sin(t * 7)
                d.text((540, y), s, font=F(int(size * p), bold), fill=col, anchor="mm")
            else:
                text(d, (540, y), s, size, col, 1.0, bold=bold)
        return im
    return fn

def prog(t, D, start=0.5, tail=3.2):
    return ease_io((t - start) / max(1.0, D - tail))

def bars_scene(title, col, sub, big, bars, reveal, reveal_sub="", big_size=104, extra=None):
    """big(p)->str animated headline number. bars: (label, right_label, frac, color, animated)."""
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 420), title, 70, col, appear(t, 0))
        if sub: text(d, (540, 495), sub, 36, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        if big: text(d, (540, 660), big(p), big_size, WHITE, appear(t, 0.2))
        a = appear(t, 0.4)
        y = 850 if big else 640
        for (lab, rl, frac, c, anim) in bars:
            text(d, (90, y), lab, 38, c if anim else GREY, a, anchor="lm")
            if rl: text(d, (900, y), rl, 38, WHITE, a, anchor="rm")
            bar(d, 90, y + 40, 900, y + 110, frac * (p if anim else 1.0), c, a, minw=8)
            y += 200
        if extra: extra(d, t, D, p)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        if reveal_sub: text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

def recap(title, rows, follow_y=1500, size=72):
    """rows: (label, value, color). Shows 'Follow for more' only in the short (TikTok) cut."""
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 440), title, 64, WHITE, appear(t, 0))
        y = 680
        for i, (lab, val, c) in enumerate(rows):
            a = appear(t, 0.4 + 1.2 * i)
            text(d, (90, y), lab, 44, c, a, anchor="lm")
            text(d, (900, y + 75), val, size, WHITE, a, anchor="rm")
            y += 250
        if D < 6: text(d, (540, follow_y), T("Follow for more", "Folge für mehr"), 48, Y1, appear(t, min(3.4, D - 1.6)))
        return im
    return fn

def statement(lines, follow_y=1350):
    """lines: (y, text, size, color, bold, start). Final punchline scene."""
    def fn(t, D):
        im, d = frame_base()
        for (y, s, size, col, bold, st) in lines:
            text(d, (540, y), s, size, col, appear(t, st), bold=bold)
        if D < 6: text(d, (540, follow_y), T("Follow for more", "Folge für mehr"), 48, Y1, appear(t, min(2.6, D - 1.6)))
        return im
    return fn

def wrap_digits(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]
