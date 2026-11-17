import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

DAYS = 80 * 365.25

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 500), "You get", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 630), "$1 BILLION", font=F(int(140 * p)), fill=Y3, anchor="mm")
    text(d, (540, 780), "and 80 years to spend it all.", 56, GREY, 1.0, bold=False)
    text(d, (540, 980), "How much", 90, WHITE, 1.0)
    text(d, (540, 1090), "PER DAY?", 110, Y1, 1.0)
    return im

def day_scene(title, col, total, bars, reveal, reveal_sub):
    per = total / DAYS
    return bars_scene(title, col, "spent evenly over 80 years", lambda p: "$" + fmt(per * p) + " / day", bars, reveal, reveal_sub, big_size=88)

s2 = day_scene("$1 MILLION", Y1, 1e6, [("A nice dinner", "$100", 100 / 34.2 / 3, DGREY, False), ("$1 million", "$34 / day", 1 / 3, Y1, True)],
               "$34 A DAY.", "A million isn't THAT much.")
s3 = day_scene("$1 BILLION", Y2, 1e9, [("$1 million", "$34 / day", 0.001, DGREY, False), ("$1 billion", "$34,223 / day", 1.0, Y2, True)],
               "$34,223 A DAY.", "A new car. Every single day.")
s4 = day_scene("$1 TRILLION", Y3, 1e12, [("$1 billion", "$34,223 / day", 0.001, DGREY, False), ("$1 trillion", "$34 million / day", 1.0, Y3, True)],
               "$34 MILLION A DAY.", "A private jet every day. For 80 years.")
s5 = recap("Spend it all in 80 years:", [("$1 MILLION", "$34 / day", Y1), ("$1 BILLION", "$34,223 / day", Y2), ("$1 TRILLION", "$34.2M / day", Y3)], size=64)

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("Generations since the pyramids"), 5.0)],
      [(0, 4.5, 0.15, "A billion dollars, eighty years to spend it. How much per day?"),
       (4.5, 11, 0.5, "First, a million. Spread over eighty years, that's just thirty four dollars a day. Not exactly rich."),
       (15.5, 12, 0.5, "One billion? Thirty four thousand dollars, every single day. Like buying a new car. Daily."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And one trillion: thirty four million dollars a day. A private jet every morning, for eighty years straight. And you'd still have to keep going."),
       (46, 9.5, 0.4, "Thirty four dollars. Thirty four thousand. Thirty four million."),
       (55.5, 5, 0.4, "Next: how many generations since the pyramids?")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Spend a billion in eighty years."),
       (3, 5, 0.2, "A million: thirty four dollars a day."),
       (8, 6, 0.2, "A billion: thirty four thousand a day."),
       (14, 6, 0.2, "A trillion: thirty four million a day."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep27", "chartsnack_ep27_per_day.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
