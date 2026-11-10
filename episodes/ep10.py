import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def val(day): return 0.01 * 2 ** (day - 1)
def money(v):
    if v < 10: return f"${v:,.2f}"
    return f"${v:,.0f}"

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 520), "Take", 70, GREY, 1.0, bold=False)
    text(d, (540, 640), "$1 MILLION", 130, Y1, 1.0)
    text(d, (540, 760), "right now…", 70, WHITE, 1.0)
    text(d, (540, 900), "OR", 80, GREY, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1060), "1 PENNY", font=F(int(130 * p)), fill=Y3, anchor="mm")
    text(d, (540, 1180), "doubled every day for 30 days?", 50, WHITE, 1.0)
    return im

def day_scene(d0, d1, top, col, reveal, reveal_sub, line=None):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        day = d0 + (d1 - d0) * p
        cur = int(round(day))
        text(d, (540, 420), f"DAY {cur}", 80, col, appear(t, 0))
        text(d, (540, 560), money(val(cur)), 110, WHITE, appear(t, 0.1))
        a = appear(t, 0.3)
        x0, x1, yb, yt = 90, 990, 1450, 760
        bw = (x1 - x0) / 30
        d.line([(x0, yb), (x1, yb)], fill=mix(GREY, a), width=3)
        if line:
            ly = yb - (yb - yt) * min(1.0, line[0] / top)
            for x in range(x0, x1, 28): d.line([(x, ly), (x + 14, ly)], fill=mix(WHITE, a * 0.8), width=3)
            text(d, (x0, ly - 30), line[1], 34, WHITE, a, anchor="lm")
        for k in range(1, cur + 1):
            h = (yb - yt) * min(1.0, val(k) / top)
            if h < 3: h = 3
            c = col if k == cur else DGREY
            d.rectangle([x0 + (k - 1) * bw + 3, yb - h, x0 + k * bw - 3, yb], fill=mix(c, a))
        text(d, (x0, yb + 40), "day 1", 30, GREY, a, bold=False, anchor="lm")
        text(d, (x1, yb + 40), "day 30", 30, GREY, a, bold=False, anchor="rm")
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = day_scene(1, 20, val(20), Y1, "Day 20: $5,243.", "Looks like a terrible deal.")
s3 = day_scene(20, 28, 1.5e6, Y2, "Day 28: $1.34 million.", "It just passed the million.", line=(1e6, "$1 MILLION"))
s4 = day_scene(28, 30, val(30), Y3, "Day 30: $5,368,709.", "Over 5 times the million.", line=(1e6, "$1 MILLION"))
s5 = recap("Your doubling penny:", [("DAY 10", "$5.12", Y1), ("DAY 20", "$5,243", Y2), ("DAY 30", "$5.37 million", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("Earth shrunk to a basketball"), 5.0)],
      [(0, 4.5, 0.15, "One million dollars right now, or one penny that doubles every day for thirty days?"),
       (4.5, 12, 0.5, "Day two, two cents. Day ten, five dollars. Even on day twenty, you only have about five thousand dollars. Bad deal, right?"),
       (16.5, 13, 0.5, "But keep doubling. Day twenty five, about a hundred seventy thousand. And on day twenty eight, it passes one million."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "Two more doublings. Day thirty: five point three seven million dollars. More than five times the million."),
       (46, 9, 0.4, "And half of it arrives on the very last day. That's how doubling works."),
       (55, 5, 0.4, "Next: Earth, shrunk to a basketball.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A million now, or a doubling penny?"),
       (3, 5, 0.2, "Day twenty: just five thousand."),
       (8, 6, 0.2, "Day twenty eight: over a million."),
       (14, 6, 0.2, "Day thirty: five point three seven million."),
       (20, 5, 0.2, "Doubling wins. Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0), (14.5, 18.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep10", "chartsnack_ep10_penny.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
