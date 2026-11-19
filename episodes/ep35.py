import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def total(n): return n * (n + 1) // 2

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 460), "Save $1 today.", 90, WHITE, 1.0)
    text(d, (540, 570), "$2 tomorrow. $3 the day after...", 52, GREY, 1.0, bold=False)
    for i in range(6):
        h = 40 + i * 45
        d.rounded_rectangle([210 + i * 115, 1000 - h, 290 + i * 115, 1000], radius=10, fill=[Y1, Y1, Y2, Y2, Y3, Y3][i])
    text(d, (540, 1150), "After 10 years?", 96, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1280), "GUESS!", font=F(int(110 * p)), fill=Y1, anchor="mm")
    return im

def save_scene(title, col, days, bars, reveal, reveal_sub):
    return bars_scene(title, col, f"{fmt(days)} days, $1 more each day", lambda p: "$" + fmt(total(int(days * p))), bars, reveal, reveal_sub)

s2 = save_scene("AFTER 1 YEAR", Y1, 365, [("Last deposit", "$365", 365 / 66795, DGREY, False), ("Saved", "$66,795", 1.0, Y1, True)],
                "$66,795.", "From just $1 on day one.")
s3 = save_scene("AFTER 5 YEARS", Y2, 1826, [("After 1 year", "$66,795", 66795 / 1668051, DGREY, False), ("After 5 years", "$1.67 million", 1.0, Y2, True)],
                "A MILLIONAIRE.", "$1.67 million – no interest.")
s4 = save_scene("AFTER 10 YEARS", Y3, 3652, [("After 5 years", "$1.67 million", 1668051 / 6670378, DGREY, False), ("After 10 years", "$6.67 million", 1.0, Y3, True)],
                "$6.67 MILLION.", "Last day's deposit: $3,652.")
s5 = recap("$1 more every day:", [("1 YEAR", "$66,795", Y1), ("5 YEARS", "$1.67 million", Y2), ("10 YEARS", "$6.67 million", Y3)], size=64)

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("Shake hands with everyone"), 5.0)],
      [(0, 4.5, 0.15, "Save one dollar more every day. After ten years?"),
       (4.5, 11, 0.5, "One dollar on day one, two on day two, and so on. After one year: sixty six thousand dollars."),
       (15.5, 12, 0.5, "After five years, you'd have one point six seven million. A millionaire, without any interest."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "After ten years: six point six seven million dollars. Though by then, the daily deposit is over three and a half thousand dollars."),
       (46, 9.5, 0.4, "Small steps add up. Fast."),
       (55.5, 5, 0.4, "Next: shaking hands with everyone on Earth.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Save one dollar more every day."),
       (3, 5, 0.2, "One year: sixty six thousand."),
       (8, 6, 0.2, "Five years: a millionaire."),
       (14, 6, 0.2, "Ten years: six point seven million."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep35", "chartsnack_ep35_save.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
