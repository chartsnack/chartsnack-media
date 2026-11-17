import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

L_DAY = 2.0
BLUE = (80, 160, 255)

def glass(d, cx, cy, s, frac, a):
    w, h = 120 * s, 200 * s
    d.polygon([(cx - w, cy - h), (cx + w, cy - h), (cx + 0.8 * w, cy + h), (cx - 0.8 * w, cy + h)], outline=mix(WHITE, a), width=6)
    top = cy + h - 2 * h * frac
    ww = 0.8 * w + 0.2 * w * (cy + h - top) / (2 * h)
    d.polygon([(cx - ww + 6, top), (cx + ww - 6, top), (cx + 0.8 * w - 6, cy + h - 4), (cx - 0.8 * w + 6, cy + h - 4)], fill=mix(BLUE, a))

def s1(t, D):
    im, d = frame_base()
    glass(d, 540, 640, 1.2, 0.5 + 0.35 * math.sin(t * 2), 1.0)
    text(d, (540, 1010), "2 liters of water a day.", 64, WHITE, 1.0)
    text(d, (540, 1120), "How much in", 84, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1250), "YOUR LIFE?", font=F(int(124 * p)), fill=BLUE, anchor="mm")
    return im

def water_scene(title, col, liters, bars, reveal, reveal_sub):
    return bars_scene(title, col, "at 2 liters per day", lambda p: f"{fmt(liters * p)} liters", bars, reveal, reveal_sub, big_size=96)

s2 = water_scene("IN ONE WEEK", Y1, 14, [("Big water bottle", "1.5 l", 1.5 / 14, DGREY, False), ("One week", "14 l", 1.0, Y1, True)],
                 "14 LITERS.", "A full bucket.")
s3 = water_scene("IN ONE YEAR", Y2, 730.5, [("Bathtub", "~150 l", 150 / 730.5, DGREY, False), ("One year", "730 l", 1.0, Y2, True)],
                 "730 LITERS.", "About 5 full bathtubs.")
s4 = water_scene("IN 80 YEARS", Y3, 58440, [("One year", "730 l", 730 / 58440, DGREY, False), ("80 years", "58,440 l", 1.0, Y3, True)],
                 "58,440 LITERS.", "About 390 full bathtubs.")
s5 = recap("Water you drink:", [("ONE WEEK", "14 liters", Y1), ("ONE YEAR", "5 bathtubs", Y2), ("80 YEARS", "~390 bathtubs", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("How many chess games exist?"), 5.0)],
      [(0, 4.5, 0.15, "Two liters of water a day. How much in your whole life?"),
       (4.5, 11, 0.5, "Say you drink about two liters a day. In one week, that's fourteen liters. A full bucket."),
       (15.5, 12, 0.5, "In one year: about seven hundred thirty liters. Roughly five full bathtubs."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And over eighty years? Around fifty eight thousand liters. About three hundred ninety bathtubs, or more than a big tanker truck."),
       (46, 9.5, 0.4, "Glass by glass, it adds up to almost four hundred bathtubs."),
       (55.5, 5, 0.4, "Next: how many chess games are possible?")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Two liters a day. For your whole life?"),
       (3, 5, 0.2, "One week: a full bucket."),
       (8, 6, 0.2, "One year: five bathtubs."),
       (14, 6, 0.2, "Eighty years: three hundred ninety bathtubs."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep31", "chartsnack_ep31_water.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
