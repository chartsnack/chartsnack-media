import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

# driving nonstop at 100 km/h; planets at closest approach to Earth
def s1(t, D):
    im, d = frame_base()
    text(d, (540, 600), "Drive to the Moon", 96, WHITE, appear(t, -1))
    text(d, (540, 710), "at 100 km/h. Nonstop.", 64, GREY, appear(t, -1), bold=False)
    text(d, (540, 960), "How long", 84, WHITE, appear(t, 1.6))
    text(d, (540, 1070), "would it take?", 84, WHITE, appear(t, 1.9))
    a = appear(t, 2.6); pulse = 1 + 0.05 * math.sin(max(0, t - 2.6) * 7)
    if a > 0:
        d.text((540, 1240 + (1 - a) * 40), "???", font=F(int(170 * pulse)), fill=mix(Y3, a), anchor="mm")
    return im

def trip(t, title, col, km_label, days_total, unit, final, sub):
    im, d = frame_base()
    text(d, (540, 420), title, 76, col, appear(t, 0))
    text(d, (540, 500), km_label, 40, GREY, appear(t, 0.2), bold=False)
    p = ease_io((t - 0.6) / 7.0)
    a = appear(t, 0.4)
    # road with car
    y = 760; x0, x1 = 110, 900
    d.rounded_rectangle([x0, y - 6, x1, y + 6], radius=6, fill=mix(TRACK, a))
    if p > 0: d.rounded_rectangle([x0, y - 6, x0 + (x1 - x0) * p, y + 6], radius=6, fill=mix(col, a))
    cx = x0 + (x1 - x0) * p
    d.rounded_rectangle([cx - 34, y - 46, cx + 34, y - 14], radius=10, fill=mix(WHITE, a))
    d.ellipse([cx - 26, y - 20, cx - 10, y - 4], fill=mix(GREY, a)); d.ellipse([cx + 10, y - 20, cx + 26, y - 4], fill=mix(GREY, a))
    d.ellipse([x0 - 16, y - 16, x0 + 16, y + 16], fill=mix(Y1, a))
    d.ellipse([x1 - 22, y - 22, x1 + 22, y + 22], fill=mix(col, a))
    text(d, (x0, y + 60), "EARTH", 30, GREY, a)
    val = days_total * p
    shown = f"{val:,.0f} {unit}" if unit == "days" else f"{val/365.25:,.0f} years"
    text(d, (540, 980), shown, 110, WHITE, appear(t, 0.5))
    text(d, (540, 1180), final, 66, col, appear(t, 7.9))
    text(d, (540, 1270), sub, 44, GREY, appear(t, 8.5), bold=False)
    return im

def s2(t, D): return trip(t, "THE MOON", Y1, "384,400 km away", 160.2, "days", "\u2248 5 months", "No breaks. No sleep.")
def s3(t, D): return trip(t, "THE SUN", Y2, "150 million km away", 62333, "years", "\u2248 2 lifetimes", "Your great-great-grandkids arrive.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "THE PLANETS", 76, Y3, appear(t, 0))
    text(d, (540, 500), "even at their closest to Earth", 40, GREY, appear(t, 0.2), bold=False)
    rows = [(1.0, "Mars", 62, Y1), (4.0, "Jupiter", 671, Y2), (7.0, "Saturn", 1369, Y2), (10.0, "Neptune", 4905, Y3)]
    y = 650
    for st, name, yrs, c in rows:
        a = appear(t, st)
        p = ease_io((t - st) / 2.2)
        text(d, (90, y), name, 46, WHITE, a, anchor="lm")
        text(d, (900, y), f"{fmt(yrs * p)} years", 46, c, a, anchor="rm")
        bar(d, 90, y + 40, 900, y + 90, yrs / 4905 * p, c, a, r=12)
        y += 190
    return im

def s5(t, D):
    im, d = frame_base()
    text(d, (540, 520), "Neptune: 4,905 years.", 70, WHITE, appear(t, 0))
    text(d, (540, 720), "Leave before the", 60, GREY, appear(t, 1.0), bold=False)
    text(d, (540, 800), "pyramids were built...", 60, GREY, appear(t, 1.3), bold=False)
    text(d, (540, 1000), "...and you'd only", 72, Y3, appear(t, 3.0))
    text(d, (540, 1090), "just be arriving.", 72, Y3, appear(t, 3.3))
    text(d, (540, 1300), "Light makes it in 4 hours.", 46, GREY, appear(t, 5.5), bold=False)
    return im

SCENES = [("s1", s1, 5.0), ("s2", s2, 12.0), ("s3", s3, 11.0), ("s4", s4, 18.0), ("s5", s5, 11.0), ("s6", outro, 5.0)]
LINES = [
    (0, 5, 0.15, "Drive to the Moon at a hundred k-m-h, nonstop. How long would it take?"),
    (5, 12, 0.5, "The Moon is three hundred eighty-four thousand kilometers away. That's a hundred and sixty days of driving."),
    (17, 11, 0.5, "The Sun? A hundred and seventy-one years. Your great-great-grandkids would be the ones arriving."),
    (28, 18, 1.0, "And the planets, even at their closest. Mars, sixty-two years. Jupiter, six hundred seventy. Saturn, almost fourteen hundred. And Neptune..."),
    (46, 11, 0.5, "Four thousand nine hundred years. Leave before the pyramids were built, and you'd only just be arriving."),
    (57, 5, 0.5, "Follow Chart Snack. A new one every day."),
]
TICKS = [(5.6, 12.6), (17.6, 24.6)]
DINGS = [0.3, 2.6, 13.0, 25.0, 29.0, 32.0, 35.0, 38.0, 49.0, 57.6]

if __name__ == "__main__":
    out = "/home/claude/chartsnack/ep03/out"
    if sys.argv[1:] == ["stills"]:
        stills(out, SCENES, [0.0, 10, 10, 14, 8, 4])
    else:
        build(out, SCENES, LINES, TICKS, DINGS, "chartsnack_ep03_drive.mp4", only=sys.argv[1:] or None)
