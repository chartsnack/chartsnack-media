import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

def thick(n):
    mm = 0.1 * 2 ** n
    if mm < 10: return f"{mm:.1f} mm"
    if mm < 1000: return f"{mm/10:,.0f} cm"
    m = mm / 1000
    if m < 1000: return f"{m:,.0f} m"
    return f"{m/1000:,.0f} km"

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 600), "Fold a sheet of paper", 80, WHITE, appear(t, -1))
    a = appear(t, -1); pulse = 1 + 0.04 * math.sin(max(0, t) * 6)
    d.text((540, 760), "42 times.", font=F(int(150 * pulse)), fill=mix(Y3, a), anchor="mm")
    text(d, (540, 1000), "How thick", 84, WHITE, appear(t, 1.8))
    text(d, (540, 1100), "would it be?", 84, WHITE, appear(t, 2.1))
    return im

def fold_scene(t, n0, n1, col, landmark, sub, dur_count=6.0):
    im, d = frame_base()
    p = ease_io((t - 0.4) / dur_count)
    n = n0 + (n1 - n0) * p
    ni = int(round(n))
    text(d, (540, 430), f"FOLD #{ni}", 72, col, appear(t, 0))
    text(d, (540, 620), thick(n), 128, WHITE, appear(t, 0.1))
    # log progress bar 0..51 folds with marker
    a = appear(t, 0.2)
    bar(d, 90, 800, 900, 850, n / 51, col, a, r=14)
    for k, lab in [(0, "0"), (17, "17"), (34, "34"), (51, "51")]:
        x = 90 + 810 * k / 51
        text(d, (x, 890), lab, 28, GREY, a, bold=False)
    text(d, (540, 1080), landmark, 66, col, appear(t, dur_count + 0.8))
    text(d, (540, 1170), sub, 44, GREY, appear(t, dur_count + 1.3), bold=False)
    return im

def s2(t, D): return fold_scene(t, 0, 23, Y1, "Taller than the", "Burj Khalifa (828 m)", 7.5)
def s3(t, D): return fold_scene(t, 23, 30, Y2, "You're in space.", "Space starts at about 100 km.", 5.0)
def s4(t, D): return fold_scene(t, 30, 42, Y3, "Past the Moon.", "The Moon is 384,400 km away.", 5.0)
def s5(t, D): return fold_scene(t, 42, 51, Y3, "Past the Sun.", "Just 9 more folds.", 4.0)

def s6(t, D):
    im, d = frame_base()
    text(d, (540, 600), "The catch?", 90, WHITE, appear(t, 0))
    text(d, (540, 800), "The real world record", 60, GREY, appear(t, 1.2), bold=False)
    text(d, (540, 880), "is just", 60, GREY, appear(t, 1.5), bold=False)
    a = appear(t, 2.3)
    d.text((540, 1080 + (1 - a) * 40), "12 folds.", font=F(150), fill=mix(Y1, a), anchor="mm")
    return im

SCENES = [("s1", s1, 5.0), ("s2", s2, 14.0), ("s3", s3, 10.0), ("s4", s4, 11.0), ("s5", s5, 10.0), ("s6", s6, 9.0), ("s7", outro, 5.0)]
LINES = [
    (0, 5, 0.15, "Fold a sheet of paper forty-two times. How thick would it be?"),
    (5, 14, 0.5, "Every fold doubles it. Seven folds, about a centimeter. Seventeen, a four-story building. Twenty-three folds... taller than the Burj Khalifa."),
    (19, 10, 0.4, "Thirty folds, a hundred kilometers. You've left the atmosphere."),
    (29, 11, 0.4, "And at forty-two folds, four hundred thousand kilometers. That's past the Moon."),
    (40, 10, 0.4, "Nine more folds, and your paper reaches past the Sun."),
    (50, 9, 0.4, "The catch? The real world record is just twelve folds."),
    (59, 5, 0.5, "Follow Chart Snack. A new one every day."),
]
TICKS = [(5.4, 12.9), (19.4, 24.4), (29.4, 34.4), (40.4, 44.4)]
DINGS = [0.3, 2.0, 13.8, 25.3, 35.3, 45.3, 52.4, 59.6]

if __name__ == "__main__":
    out = "/home/claude/chartsnack/ep04/out"
    if sys.argv[1:] == ["stills"]:
        stills(out, SCENES, [0.0, 13, 9, 10, 9, 8, 4])
    else:
        build(out, SCENES, LINES, TICKS, DINGS, "chartsnack_ep04_paper.mp4", only=sys.argv[1:] or None)
