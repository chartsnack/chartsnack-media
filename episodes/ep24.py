import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

BPM = 16  # breaths per minute at rest (normal adult range 12-20)
DAY = BPM * 60 * 24
YEAR = DAY * 365.25
LIFE = YEAR * 80

def lungs(d, cx, cy, s, col, a):
    for side in (-1, 1):
        x = cx + side * 95 * s
        d.ellipse([x - 80 * s, cy - 150 * s, x + 80 * s, cy + 150 * s], fill=mix(col, a))
    d.rectangle([cx - 14 * s, cy - 230 * s, cx + 14 * s, cy - 60 * s], fill=mix(col, a))

def s1(t, D):
    im, d = frame_base()
    s = 1 + 0.12 * math.sin(t * 2.4)
    lungs(d, 540, 640, 0.9 * s, Y3, 1.0)
    text(d, (540, 1000), "How many BREATHS", 86, WHITE, 1.0)
    text(d, (540, 1100), "do you take", 70, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1240), "IN YOUR LIFE?", font=F(int(110 * p)), fill=Y1, anchor="mm")
    return im

def count_scene(title, col, total, bars, reveal, reveal_sub):
    return bars_scene(title, col, f"~{BPM} breaths per minute", lambda p: fmt(total * p), bars, reveal, reveal_sub)

s2 = count_scene("IN ONE DAY", Y1, DAY, [("One minute", "16", 16 / DAY, DGREY, False), ("One day", fmt(DAY), 1.0, Y1, True)], "23,040 breaths.", "Every single day – even asleep.")
s3 = count_scene("IN ONE YEAR", Y2, YEAR, [("One day", fmt(DAY), DAY / YEAR, DGREY, False), ("One year", "8.4 million", 1.0, Y2, True)], "8.4 MILLION.", "Without thinking about it once.")
s4 = count_scene("IN 80 YEARS", Y3, LIFE, [("One year", "8.4 million", 1 / 80, DGREY, False), ("80 years", "673 million", 1.0, Y3, True)], "673 MILLION breaths.", "Two-thirds of a BILLION.")
s5 = recap("Your breaths:", [("PER DAY", "23,040", Y1), ("PER YEAR", "8.4 million", Y2), ("IN 80 YEARS", "673 million", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("Spend $1 MILLION a day"), 5.0)],
      [(0, 4.5, 0.15, "How many breaths do you take in your whole life?"),
       (4.5, 11, 0.5, "At rest, an adult breathes about sixteen times a minute. That's twenty three thousand breaths a day."),
       (15.5, 12, 0.5, "In one year: about eight point four million breaths. And you never think about a single one."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "Over eighty years, that adds up to around six hundred seventy million breaths. Two thirds of a billion."),
       (46, 9.5, 0.4, "Twenty three thousand today. Six hundred seventy million in a life."),
       (55.5, 5, 0.4, "Next: spending a million dollars a day.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "How many breaths in your life?"),
       (3, 5, 0.2, "One day: twenty three thousand."),
       (8, 6, 0.2, "One year: eight million."),
       (14, 6, 0.2, "Eighty years: six hundred seventy million."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep24", "chartsnack_ep24_breaths.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
