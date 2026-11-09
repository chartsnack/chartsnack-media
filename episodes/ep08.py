import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

def person(d, cx, cy, s, col, a):
    d.ellipse([cx - 22 * s, cy - 70 * s, cx + 22 * s, cy - 26 * s], fill=mix(col, a))
    d.rounded_rectangle([cx - 34 * s, cy - 18 * s, cx + 34 * s, cy + 60 * s], radius=int(24 * s), fill=mix(col, a))

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 600), "8 billion people", 96, WHITE, 1.0)
    text(d, (540, 700), "are alive today.", 70, GREY, 1.0, bold=False)
    text(d, (540, 900), "How many have", 90, WHITE, 1.0)
    pulse = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1040), "EVER lived?", font=F(int(130 * pulse)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "HUMANS EVER BORN", 70, Y1, appear(t, 0))
    text(d, (540, 495), "estimate, since ~200,000 years ago", 36, GREY, appear(t, 0.1), bold=False)
    p = ease_io((t - 0.5) / max(1.0, D - 3.2))
    text(d, (540, 700), fmt(117e9 * p), 104, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    for i in range(10):  # crowd filling up
        for j in range(5):
            k = i * 5 + j
            on = 1.0 if k < 50 * p else 0.25
            person(d, 135 + i * 90, 900 + j * 120, 0.7, Y1 if on == 1.0 else GREY, a * on)
    text(d, (540, 1600), "About 117 BILLION", 64, Y1, appear(t, D - 2.4))
    return im

def s3(t, D):
    im, d = frame_base()
    text(d, (540, 420), "ALIVE vs EVER LIVED", 70, Y2, appear(t, 0))
    p = ease_io((t - 0.5) / max(1.0, D - 3.4))
    a = appear(t, 0.3)
    text(d, (90, 700), "EVER BORN", 40, GREY, a, anchor="lm")
    text(d, (900, 700), "117 billion", 40, WHITE, a, anchor="rm")
    bar(d, 90, 740, 900, 820, 1.0, (110, 116, 135), a)
    text(d, (90, 950), "ALIVE TODAY", 40, Y2, a, anchor="lm")
    text(d, (900, 950), "8.3 billion", 40, WHITE, a, anchor="rm")
    bar(d, 90, 990, 900, 1070, 0.071 * p, Y2, a, minw=8)
    text(d, (540, 1300), "Only about 7%", 72, Y2, appear(t, D - 2.4))
    text(d, (540, 1390), "of all humans ever are alive now.", 44, GREY, appear(t, D - 2.0), bold=False)
    return im

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "FOR EVERY PERSON ALIVE", 64, Y3, appear(t, 0))
    for k in range(14):
        i, j = k % 7, k // 7
        st = 0.4 + k * (max(1.0, D - 3.6) / 14)
        on = appear(t, st, 0.2)
        col = Y3 if k == 0 else (110, 116, 135)
        person(d, 150 + i * 130, 750 + j * 260, 1.3, col, on)
    text(d, (540, 1320), "about 13 have died.", 72, WHITE, appear(t, D - 2.4))
    text(d, (540, 1410), "1 in 14 humans ever is alive right now.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

def s5(t, D):
    im, d = frame_base()
    text(d, (540, 600), "Right now, you share", 70, WHITE, appear(t, 0))
    text(d, (540, 690), "the planet with", 70, WHITE, appear(t, 0.3))
    text(d, (540, 860), "7%", 220, Y3, appear(t, 0.8))
    text(d, (540, 1040), "of everyone who ever lived.", 52, GREY, appear(t, 1.2), bold=False)
    if D < 6: text(d, (540, 1300), "Follow for more", 48, Y1, appear(t, 2.6))
    return im

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("An even bigger number"), 5.0)],
      [(0, 4.5, 0.15, "Eight billion people are alive today. How many have ever lived?"),
       (4.5, 12, 0.5, "Researchers estimate that since our species began, about one hundred seventeen billion humans have been born."),
       (16.5, 13, 0.5, "So everyone alive right now, all eight billion of us, is only about seven percent of that."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "Put another way: for every person alive today, about thirteen people have already lived and died."),
       (46, 9, 0.4, "Right now, you share the planet with seven percent of everyone who ever lived."),
       (55, 5, 0.4, "Follow for an even bigger number.")],
      [(5.0, 13.8), (17.0, 26.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "How many humans have ever lived?"),
       (3, 5, 0.2, "About a hundred seventeen billion."),
       (8, 6, 0.2, "Only seven percent are alive today."),
       (14, 6, 0.2, "For every one of us, thirteen have died."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 4.8), (8.5, 10.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep08", "chartsnack_ep08_humans.mp4", YT, TT, [3.5, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
