import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def prob(n):
    p = 1.0
    for i in range(int(n)): p *= (365 - i) / 365
    return 1 - p

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 560), "How many people", 84, WHITE, 1.0)
    text(d, (540, 660), "in one room until two", 64, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 820), "SHARE A BIRTHDAY?", font=F(int(92 * p)), fill=Y3, anchor="mm")
    text(d, (540, 960), "(a 50 % chance)", 52, GREY, 1.0, bold=False)
    text(d, (540, 1150), "365 days. Guess!", 80, Y1, 1.0)
    return im

def room_scene(n0, n1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        n = int(round(n0 + (n1 - n0) * p))
        pr = prob(n)
        text(d, (540, 420), f"{n} PEOPLE", 84, col, appear(t, 0))
        a = appear(t, 0.2)
        # people grid: 10 per row
        for k in range(n):
            r, c = divmod(k, 10)
            x, y = 135 + c * 90, 560 + r * 72
            d.ellipse([x - 14, y - 24, x + 14, y + 4], fill=mix(col, a))
            d.rounded_rectangle([x - 22, y + 8, x + 22, y + 34], radius=11, fill=mix(col, a))
        text(d, (90, 1110), "CHANCE OF A SHARED BIRTHDAY", 36, GREY, a, anchor="lm")
        bar(d, 90, 1150, 900, 1240, pr, col, a, minw=8)
        pct = f"{100 * pr:.1f} %" if pr < 0.999 else "99.9 %"
        text(d, (540, 1340), pct, 110, WHITE, a)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = room_scene(2, 10, Y1, "10 people: 12 %.", "Already more than you'd think.")
s3 = room_scene(10, 23, Y2, "23 people: 50 %!", "A coin flip. Just one school class.")
s4 = room_scene(23, 70, Y3, "70 people: 99.9 %.", "Almost guaranteed.")
s5 = recap("Shared birthday chance:", [("10 PEOPLE", "12 %", Y1), ("23 PEOPLE", "50 %", Y2), ("70 PEOPLE", "99.9 %", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 15.0), ("s5", s5, 9.5),
       ("s6", outro_next("$1 billion in $1 bills"), 5.0)],
      [(0, 4.5, 0.15, "How many people until two share a birthday? Fifty fifty odds."),
       (4.5, 11, 0.5, "Most people guess around one hundred eighty. But with just ten people, the chance is already twelve percent."),
       (15.5, 13, 0.5, "At twenty three people, it's fifty percent. A coin flip. Because every person is compared with every other person: that's two hundred fifty three pairs."),
       (28.5, 2.5, 0.1, "Subscribe for more."),
       (31, 15, 0.5, "And at seventy people? Ninety nine point nine percent. A shared birthday is almost guaranteed."),
       (46, 9.5, 0.4, "Twenty three for a coin flip. Seventy for a near certainty."),
       (55.5, 5, 0.4, "Next: a billion dollar bills, laid end to end.")],
      [(5.0, 12.8), (16.0, 25.8), (31.5, 43.8)],
      [0.2, 13.0, 26.0, 28.7, 44.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "When do two people share a birthday?"),
       (3, 5, 0.2, "Ten people: twelve percent."),
       (8, 6, 0.2, "Twenty three people: fifty percent!"),
       (14, 6, 0.2, "Seventy people: almost certain."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep21", "chartsnack_ep21_birthday.mp4", YT, TT, [0.0, 10.5, 12.5, 1.3, 14.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
