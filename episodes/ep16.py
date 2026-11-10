import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

NIGHT = (110, 120, 255)

def moon(d, cx, cy, r, a):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(Y1, a))
    d.ellipse([cx - r + r * 0.55, cy - r - r * 0.2, cx + r + r * 0.55, cy + r - r * 0.2], fill=BG)

def s1(t, D):
    im, d = frame_base()
    moon(d, 540, 540, 110, 1.0)
    text(d, (540, 780), "You sleep 8 hours", 90, WHITE, 1.0)
    text(d, (540, 880), "every night.", 70, GREY, 1.0, bold=False)
    text(d, (540, 1040), "How many YEARS", 88, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1170), "is that?", font=F(int(130 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "ONE DAY", 70, Y1, appear(t, 0))
    text(d, (540, 495), "24 hours", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    a = appear(t, 0.3)
    cx, cy, r = 540, 1060, 280
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(TRACK, a))
    if p > 0.01:
        d.pieslice([cx - r, cy - r, cx + r, cy + r], -90, -90 + 120 * p, fill=mix(NIGHT, a))
    text(d, (540, 660), f"{8 * p:.1f} h asleep", 70, WHITE, appear(t, 0.2))
    text(d, (540, 1600), "One third of every day.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "Gone, every single night.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

def s3(t, D):
    im, d = frame_base()
    text(d, (540, 420), "AN 80-YEAR LIFE", 70, Y2, appear(t, 0))
    text(d, (540, 495), "each block = 1 year", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 640), f"{26.7 * p:.1f} years asleep", 84, WHITE, appear(t, 0.2))
    a = appear(t, 0.3)
    for k in range(80):
        i, j = k % 10, k // 10
        x, y = 150 + i * 80, 760 + j * 80
        on = k < 26.7 * p
        d.rounded_rectangle([x, y, x + 64, y + 64], radius=10, fill=mix(NIGHT if on else TRACK, a))
    text(d, (540, 1600), "26.7 years. Asleep.", 64, Y2, appear(t, D - 2.4))
    text(d, (540, 1690), "Every third year of your life.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s4 = bars_scene("BY YOUR BIRTHDAY", Y3, "years slept, at 8 hours a night", None,
                [("AGE 18", "6 years", 6 / 26.7, NIGHT, True),
                 ("AGE 30", "10 years", 10 / 26.7, NIGHT, True),
                 ("AGE 50", "16.7 years", 16.7 / 26.7, NIGHT, True),
                 ("AGE 80", "26.7 years", 1.0, Y3, True)],
                "Over 230,000 hours.", "About 9,740 full days.")

s5 = recap("Sleeping 8 h a night:", [("PER YEAR", "~122 days", Y1), ("BY AGE 30", "10 years", Y2), ("80-YEAR LIFE", "26.7 years", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("$1 BILLION, shared by all"), 5.0)],
      [(0, 4.5, 0.15, "You sleep eight hours every night. How many years is that?"),
       (4.5, 12, 0.5, "Eight out of twenty four hours. That's one third of every single day."),
       (16.5, 13, 0.5, "Over an eighty year life, that adds up to twenty six point seven years. Asleep."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "By eighteen, you've slept six years. By thirty, ten years. In total, over two hundred thirty thousand hours."),
       (46, 9, 0.4, "About a hundred twenty two days every year. One third of your whole life."),
       (55, 5, 0.4, "Next: a billion dollars, split between everyone.")],
      [(5.0, 13.8), (17.0, 26.8)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "How many years do you sleep?"),
       (3, 5, 0.2, "One third of every day."),
       (8, 6, 0.2, "Over eighty years: almost twenty seven."),
       (14, 6, 0.2, "By thirty, you've slept ten years."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep16", "chartsnack_ep16_sleep.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
