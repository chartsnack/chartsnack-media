import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def person(d, cx, cy, s, col, a):
    d.ellipse([cx - 22 * s, cy - 70 * s, cx + 22 * s, cy - 26 * s], fill=mix(col, a))
    d.rounded_rectangle([cx - 34 * s, cy - 18 * s, cx + 34 * s, cy + 60 * s], radius=int(24 * s), fill=mix(col, a))

def s1(t, D):
    im, d = frame_base()
    for k in range(9):
        person(d, 220 + k * 80, 560, 0.8, Y1 if k == 4 else DGREY, 1.0)
    text(d, (540, 760), "8 billion people.", 96, WHITE, 1.0)
    text(d, (540, 860), "Squeeze them all together.", 56, GREY, 1.0, bold=False)
    text(d, (540, 1020), "How much space", 84, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1150), "do we need?", font=F(int(116 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "4 PEOPLE PER m²", 70, Y1, appear(t, 0))
    text(d, (540, 495), "shoulder to shoulder, like a packed concert", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    side = 45.3 * p
    text(d, (540, 660), f"{side:.1f} km × {side:.1f} km", 84, WHITE, appear(t, 0.2))
    a = appear(t, 0.3)
    full = 700
    sq = max(6, full * p)
    x0, y0 = 540 - sq / 2, 1150 - sq / 2
    d.rectangle([x0, y0, x0 + sq, y0 + sq], fill=mix(Y1, a * 0.85))
    d.rectangle([540 - full / 2, 800, 540 + full / 2, 1500], outline=mix(DGREY, a), width=3)
    text(d, (540, 1600), "A square 45 km wide.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "About 2,050 km² in total.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s3 = bars_scene("HOW BIG IS THAT?", Y2, "area in km²", None,
                [("LOS ANGELES (CITY)", "1,302 km²", 1302 / 2050, DGREY, False),
                 ("GREATER LONDON", "1,572 km²", 1572 / 2050, DGREY, False),
                 ("ALL 8.2 BILLION OF US", "2,050 km²", 1.0, Y2, True)],
                "About 1.3 Londons.", "Every human on Earth.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "EARTH'S LAND", 70, Y3, appear(t, 0))
    text(d, (540, 495), "about 149 million km²", 36, GREY, appear(t, 0.1), bold=False)
    a = appear(t, 0.3)
    d.rectangle([140, 620, 940, 1420], fill=mix((60, 120, 80), a))
    p = prog(t, D)
    s = 3 + 4 * (1 - p)
    d.ellipse([540 - s, 1020 - s, 540 + s, 1020 + s], fill=mix(Y3, a))
    r = 60 * (1 - p) + 22
    d.ellipse([540 - r, 1020 - r, 540 + r, 1020 + r], outline=mix(WHITE, a), width=4)
    text(d, (540, 1600), "0.0014 % of the land.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "The rest of the land stays empty.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("All of humanity:", [("PEOPLE", "8.2 billion", Y1), ("PACKED AREA", "2,050 km²", Y2), ("SHARE OF LAND", "0.0014 %", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("How heavy is $1 TRILLION?"), 5.0)],
      [(0, 4.5, 0.15, "Eight billion people. Squeeze everyone together. How much space do we need?"),
       (4.5, 12, 0.5, "Pack four people into every square metre, like a crowded concert. Everyone fits in a square about forty five kilometres wide."),
       (16.5, 13, 0.5, "That's about two thousand square kilometres. Bigger than Los Angeles, about one point three times London."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "And compared to all the land on Earth? Just zero point zero zero one four percent. A tiny dot."),
       (46, 9, 0.4, "Every human alive, in one spot. And the rest of the planet, empty."),
       (55, 5, 0.4, "Next: how heavy is a trillion dollars?")],
      [(5.0, 13.8), (17.0, 26.8)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Squeeze all eight billion of us together."),
       (3, 5, 0.2, "A square just forty five kilometres wide."),
       (8, 6, 0.2, "About one point three Londons."),
       (14, 6, 0.2, "A tiny dot on Earth's land."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep13", "chartsnack_ep13_crowd.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
