import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 520), "You win", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 650), "$100 MILLION", font=F(int(124 * p)), fill=Y3, anchor="mm")
    text(d, (540, 800), "and spend", 70, WHITE, 1.0)
    text(d, (540, 900), "$10,000 every day.", 80, Y1, 1.0)
    text(d, (540, 1100), "When is it gone?", 90, WHITE, 1.0)
    return im

def spend_scene(title, col, big, bars, reveal, reveal_sub):
    return bars_scene(title, col, "$10,000 spent every day", big, bars, reveal, reveal_sub)

s2 = spend_scene("$1 MILLION", Y1, lambda p: f"{fmt(100 * p)} days",
                 [("1 year", "365 days", 1.0, DGREY, False), ("$1 million", "100 days", 100 / 365, Y1, True)],
                 "100 DAYS.", "Barely three months.")
s3 = spend_scene("$10 MILLION", Y2, lambda p: f"{fmt(1000 * p)} days",
                 [("$1 million", "100 days", 0.1, DGREY, False), ("$10 million", "1,000 days", 1.0, Y2, True)],
                 "2.7 YEARS.", "A fancy life – but short.")
s4 = spend_scene("$100 MILLION", Y3, lambda p: f"{27.4 * p:.1f} years",
                 [("$10 million", "2.7 years", 0.1, DGREY, False), ("$100 million", "27.4 years", 1.0, Y3, True)],
                 "27 YEARS.", "$10,000 a day – for 27 years.")
s5 = recap("At $10,000 a day:", [("$1 MILLION", "100 days", Y1), ("$10 MILLION", "2.7 years", Y2), ("$100 MILLION", "27.4 years", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("Water you drink in a lifetime"), 5.0)],
      [(0, 4.5, 0.15, "You win a hundred million. Spend ten thousand a day. When is it gone?"),
       (4.5, 11, 0.5, "Ten thousand dollars, every single day. One million lasts just one hundred days."),
       (15.5, 12, 0.5, "Ten million? One thousand days. That's under three years of the high life."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And one hundred million: ten thousand days. Twenty seven years of spending ten grand, every single day."),
       (46, 9.5, 0.4, "One hundred days. Under three years. Twenty seven years."),
       (55.5, 5, 0.4, "Next: how much water you drink in a life.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A hundred million. Ten grand a day."),
       (3, 5, 0.2, "One million: one hundred days."),
       (8, 6, 0.2, "Ten million: under three years."),
       (14, 6, 0.2, "A hundred million: twenty seven years."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep30", "chartsnack_ep30_ten_k.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
