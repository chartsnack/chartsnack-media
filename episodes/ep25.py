import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 520), "You have", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 650), "$1 TRILLION", font=F(int(130 * p)), fill=Y3, anchor="mm")
    text(d, (540, 800), "and spend", 70, WHITE, 1.0)
    text(d, (540, 900), "$1 MILLION a day.", 84, Y1, 1.0)
    text(d, (540, 1100), "When is it gone?", 90, WHITE, 1.0)
    return im

def spend_scene(title, col, days, big, bars, reveal, reveal_sub):
    return bars_scene(title, col, "$1 million spent every day", big, bars, reveal, reveal_sub)

s2 = spend_scene("$1 BILLION", Y1, 1000, lambda p: f"{fmt(1000 * p)} days",
                 [("1 year", "365 days", 365 / 1000, DGREY, False), ("$1 billion", "1,000 days", 1.0, Y1, True)],
                 "2.7 YEARS.", "A billion is gone fast.")
s3 = spend_scene("$100 BILLION", Y2, 1e5, lambda p: f"{fmt(1e5 * p / 365.25)} years",
                 [("$1 billion", "2.7 years", 1 / 100, DGREY, False), ("$100 billion", "274 years", 1.0, Y2, True)],
                 "274 YEARS.", "Start in 1752 – done today.")
s4 = spend_scene("$1 TRILLION", Y3, 1e6, lambda p: f"{fmt(1e6 * p / 365.25)} years",
                 [("$100 billion", "274 years", 0.1, DGREY, False), ("$1 trillion", "2,738 years", 1.0, Y3, True)],
                 "2,738 YEARS.", "Start in Ancient Rome. Still spending.")
s5 = recap("At $1 million a day:", [("$1 BILLION", "2.7 years", Y1), ("$100 BILLION", "274 years", Y2), ("$1 TRILLION", "2,738 years", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("The Tower of Hanoi"), 5.0)],
      [(0, 4.5, 0.15, "One trillion dollars. You spend a million a day. When is it gone?"),
       (4.5, 11, 0.5, "First, one billion. At a million a day, that's one thousand days. Under three years."),
       (15.5, 12, 0.5, "One hundred billion? Two hundred seventy four years. Start in seventeen fifty two, and you'd finish today."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And one trillion: one million days. That's two thousand seven hundred thirty eight years. Start in ancient Rome, and you'd still be spending."),
       (46, 9.5, 0.4, "A million a day sounds like a lot. A trillion doesn't care."),
       (55.5, 5, 0.4, "Next: the puzzle that outlasts the universe.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Spend a million a day. From a trillion."),
       (3, 5, 0.2, "One billion: under three years."),
       (8, 6, 0.2, "A hundred billion: two hundred seventy four years."),
       (14, 6, 0.2, "One trillion: two thousand seven hundred years."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep25", "chartsnack_ep25_million_a_day.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
