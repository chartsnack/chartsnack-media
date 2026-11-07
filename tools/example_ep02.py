import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 620), "Spend $1,000", 104, WHITE, appear(t, 0.0))
    text(d, (540, 740), "every single day.", 72, GREY, appear(t, 0.4), bold=False)
    text(d, (540, 980), "How long until", 72, WHITE, appear(t, 2.0))
    a = appear(t, 2.6); pulse = 1 + 0.05 * math.sin(max(0, t - 2.6) * 7)
    if a > 0:
        d.text((540, 1120 + (1 - a) * 40), "$1 BILLION", font=F(int(150 * pulse)), fill=mix(Y3, a), anchor="mm")
    text(d, (540, 1260), "is gone?", 72, WHITE, appear(t, 2.9))
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "$1 MILLION", 76, Y1, appear(t, 0))
    p = ease_io((t - 0.6) / 8.0)
    text(d, (540, 560), "$" + fmt(1e6 * (1 - p)), 104, WHITE, appear(t, 0.2))
    text(d, (540, 650), "left", 40, GREY, appear(t, 0.2), bold=False)
    a = appear(t, 0.4)
    bar(d, 90, 760, 900, 860, 1 - p, Y1, a, r=20)
    text(d, (540, 990), f"Day {fmt(1000 * p)}", 96, WHITE, appear(t, 0.5))
    text(d, (540, 1180), "Gone in 1,000 days", 70, Y1, appear(t, 8.8))
    text(d, (540, 1280), "≈ 2 years, 9 months", 52, GREY, appear(t, 9.4), bold=False)
    return im

def s3(t, D):
    im, d = frame_base()
    text(d, (540, 420), "$1 BILLION", 76, Y2, appear(t, 0))
    p = ease_io((t - 0.6) / 9.0)
    yrs = 2738 * p
    text(d, (540, 570), f"{fmt(yrs)} years", 110, WHITE, appear(t, 0.2))
    text(d, (540, 670), "of spending $1,000 a day", 40, GREY, appear(t, 0.2), bold=False)
    lx0, lx1, ly = 90, 880, 1000
    a = appear(t, 0.5)
    d.rounded_rectangle([lx0, ly - 7, lx1, ly + 7], radius=7, fill=mix(TRACK, a))
    fx = lx0 + (lx1 - lx0) * p
    if fx - lx0 > 2: d.rounded_rectangle([lx0, ly - 7, fx, ly + 7], radius=7, fill=mix(Y2, a))
    yr_now = -712 + yrs
    def mark(year, label, sub, above, col=WHITE):
        x = lx0 + (lx1 - lx0) * (year + 712) / 2738
        ma = a * (1.0 if yr_now >= year else 0.0)
        if ma <= 0: return
        d.ellipse([x - 11, ly - 11, x + 11, ly + 11], fill=mix(col, ma))
        yy = ly - 95 if above else ly + 60
        text(d, (x, yy), label, 32, col, ma)
        text(d, (x, yy + 38), sub, 28, GREY, ma, bold=False)
    mark(-712, "START", "~700 BC", False, Y2)
    mark(-44, "Caesar", "44 BC", True)
    mark(476, "Rome falls", "476", False)
    mark(1492, "Columbus", "1492", True)
    mark(2026, "TODAY", "money gone", False, WHITE)
    text(d, (540, 1300), "Start around 700 BC,", 56, WHITE, appear(t, 10.0))
    text(d, (540, 1380), "run out today.", 56, Y2, appear(t, 10.5))
    return im

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "$100 BILLION", 76, Y3, appear(t, 0))
    text(d, (540, 500), "what today's richest people have", 38, GREY, appear(t, 0.2), bold=False)
    p = ease_io((t - 0.6) / 9.0)
    text(d, (540, 640), f"{fmt(273785 * p)} years", 104, WHITE, appear(t, 0.3))
    a = appear(t, 0.6)
    text(d, (90, 830), "SPENDING $100B", 38, Y3, a, anchor="lm")
    bar(d, 90, 870, 900, 940, 0.9126 * p, Y3, a)
    text(d, (90, 1030), "HUMANS HAVE EXISTED", 38, GREY, a, anchor="lm")
    bar(d, 90, 1070, 900, 1140, 1.0, (110, 116, 135), a)
    text(d, (900, 1180), "~300,000 years", 34, GREY, a, bold=False, anchor="rm")
    text(d, (540, 1330), "Almost as long as", 56, WHITE, appear(t, 10.2))
    text(d, (540, 1410), "our species has existed.", 56, Y3, appear(t, 10.7))
    return im

def s5(t, D):
    im, d = frame_base()
    text(d, (540, 440), "At $1,000 a day:", 64, WHITE, appear(t, 0))
    y = 680
    for st, lab, val, c in [(0.5, "$1 MILLION", "2.7 years", Y1), (2.2, "$1 BILLION", "2,738 years", Y2), (4.2, "$100 BILLION", "273,785 years", Y3)]:
        a = appear(t, st)
        text(d, (90, y), lab, 44, c, a, anchor="lm")
        text(d, (900, y + 75), val, 72, WHITE, a, anchor="rm")
        y += 250
    return im

SCENES = [("s1", s1, 5.0), ("s2", s2, 12.0), ("s3", s3, 17.0), ("s4", s4, 15.0), ("s5", s5, 10.0), ("s6", outro, 5.0)]
LINES = [
    (0, 5, 0.15, "Spend a thousand dollars a day. How long until a billion is gone?"),
    (5, 12, 0.8, "Start with one million. A thousand a day... and it's gone in under three years."),
    (17, 17, 0.6, "Now one billion. To run out today, you'd have had to start around seven hundred BC, when Rome was still a tiny kingdom. Through Caesar, Columbus, everything."),
    (34, 15, 0.6, "Some of today's richest people have over one hundred billion. Spending that takes two hundred seventy-three thousand years. Almost as long as humans have existed."),
    (49, 10, 0.4, "A million is a lot of money. A billion? That's a different universe."),
    (59, 5, 0.5, "Follow Chart Snack. A new one every day."),
]
TICKS = [(5.6, 13.6), (17.6, 26.6), (34.6, 43.6)]
DINGS = [0.55, 2.6, 13.8, 27.0, 44.2, 49.5, 51.2, 53.2, 59.6]

if __name__ == "__main__":
    out = "/home/claude/chartsnack/ep02/out"
    if sys.argv[1:] == ["stills"]:
        stills(out, SCENES, [4.5, 11, 16, 14, 9, 4])
    else:
        build(out, SCENES, LINES, TICKS, DINGS, "chartsnack_ep02_billion.mp4", only=sys.argv[1:] or None)
