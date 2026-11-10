import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

ODDS = 292201338

def ticket(d, cx, cy, a, col=Y1, w=360, h=180):
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=18, fill=mix(col, a))
    for i in range(5):
        x = cx - w / 2 + 45 + i * 50
        d.ellipse([x - 22, cy - 22, x + 22, cy + 22], fill=mix(WHITE, a))
    x = cx + w / 2 - 50
    d.ellipse([x - 22, cy - 22, x + 22, cy + 22], fill=mix(Y3, a))

def s1(t, D):
    im, d = frame_base()
    ticket(d, 540, 540, 1.0)
    text(d, (540, 780), "1 lottery ticket", 90, WHITE, 1.0)
    text(d, (540, 880), "every single week.", 70, GREY, 1.0, bold=False)
    text(d, (540, 1040), "When do you", 84, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1170), "WIN?", font=F(int(150 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "JACKPOT ODDS", 70, Y1, appear(t, 0))
    text(d, (540, 495), "5 of 69 numbers + 1 of 26 (Powerball)", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 720), "1 in", 70, GREY, appear(t, 0.2))
    text(d, (540, 850), fmt(ODDS * p), 120, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    for k in range(60):  # one lit dot among many
        i, j = k % 12, k // 12
        c = Y3 if k == 37 else DGREY
        d.ellipse([110 + i * 75, 1020 + j * 75, 150 + i * 75, 1060 + j * 75], fill=mix(c, a * (1 if k == 37 else 0.6)))
    text(d, (540, 1600), "1 in 292 million.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "Pure math, no luck involved.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s3 = bars_scene("1 TICKET A WEEK", Y2, "average wait for one win", lambda p: f"{fmt(5.6e6 * p)} years",
                [("PYRAMIDS TO TODAY", "~4,500 yrs", 4500 / 5.6e6, DGREY, False),
                 ("HOMO SAPIENS EXISTS", "~300,000 yrs", 3e5 / 5.6e6, DGREY, False),
                 ("YOUR WAIT", "5.6 million yrs", 1.0, Y2, True)],
                "5.6 million years.", "On average. Per win.", big_size=96)

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "PLAY 60 YEARS", 70, Y3, appear(t, 0))
    text(d, (540, 495), "1 ticket every week = 3,120 tickets", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 700), f"{0.00107 * p:.5f} %", 110, WHITE, appear(t, 0.2))
    text(d, (540, 800), "chance of ever hitting the jackpot", 40, GREY, appear(t, 0.2), bold=False)
    a = appear(t, 0.4)
    text(d, (90, 950), "YOUR CHANCE", 38, Y3, a, anchor="lm")
    bar(d, 90, 990, 900, 1060, 0.0, Y3, a, minw=6)
    text(d, (90, 1150), "NOT WINNING", 38, GREY, a, anchor="lm")
    bar(d, 90, 1190, 900, 1260, 1.0 * p, DGREY, a)
    text(d, (900, 1300), "99.999 %", 34, GREY, a, bold=False, anchor="rm")
    text(d, (540, 1600), "About 1 in 94,000.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "For a whole lifetime of tickets.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("Jackpot math:", [("ODDS", "1 in 292M", Y1), ("1/WEEK, WAIT", "5.6M years", Y2), ("60 YEARS OF PLAY", "~0.001 %", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("All 8 billion people in one spot"), 5.0)],
      [(0, 4.5, 0.15, "You buy one lottery ticket every week. When do you win?"),
       (4.5, 12, 0.5, "Pick five of sixty nine numbers, plus one of twenty six. That's one chance in two hundred ninety two million."),
       (16.5, 13, 0.5, "At one ticket a week, the average wait is five point six million years. Humans have only existed for about three hundred thousand."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "Play every week for sixty years. That's over three thousand tickets, and your chance is still only about one in ninety four thousand."),
       (46, 9, 0.4, "One in two hundred ninety two million. The math always wins."),
       (55, 5, 0.4, "Next: all eight billion people, in one spot.")],
      [(5.0, 13.8), (17.0, 26.8)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "One ticket a week. When do you win?"),
       (3, 5, 0.2, "Odds: one in two hundred ninety two million."),
       (8, 6, 0.2, "Average wait: five point six million years."),
       (14, 6, 0.2, "Sixty years of tickets? About a thousandth of a percent."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep12", "chartsnack_ep12_lottery.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
