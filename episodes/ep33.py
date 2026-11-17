import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def coin(d, cx, cy, r, t, a, col=Y1):
    w = abs(math.cos(t * 6)) * r
    d.ellipse([cx - max(w, 6), cy - r, cx + max(w, 6), cy + r], fill=mix(col, a))
    if w > r * 0.4: d.text((cx, cy), "$", font=F(int(r * 1.1)), fill=mix(BG, a), anchor="mm")

def s1(t, D):
    im, d = frame_base()
    coin(d, 540, 560, 150, t, 1.0)
    text(d, (540, 820), "Bet $1 on a coin flip.", 70, WHITE, 1.0)
    text(d, (540, 910), "Every win DOUBLES it.", 70, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1080), "30 WINS IN A ROW?", font=F(int(92 * p)), fill=Y3, anchor="mm")
    text(d, (540, 1200), "How rich? What are the odds?", 50, GREY, 1.0, bold=False)
    return im

def flip_scene(n0, n1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        n = int(round(n0 + (n1 - n0) * p))
        text(d, (540, 400), f"{n} WINS IN A ROW", 76, col, appear(t, 0))
        text(d, (540, 560), "$" + fmt(2 ** n), 104, WHITE, appear(t, 0.1))
        text(d, (540, 660), "you have", 40, GREY, appear(t, 0.1), bold=False)
        a = appear(t, 0.2)
        for k in range(n):
            r, c = divmod(k, 10)
            x, y = 135 + c * 90, 820 + r * 100
            d.ellipse([x - 34, y - 34, x + 34, y + 34], fill=mix(col, a))
            d.text((x, y), "W", font=F(34), fill=mix(BG, a), anchor="mm")
        text(d, (540, 1250), f"Chance: 1 in {fmt(2 ** n)}", 60, col, a)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = flip_scene(1, 10, Y1, "10 wins: $1,024.", "Odds: 1 in 1,024.")
s3 = flip_scene(10, 20, Y2, "20 wins: $1 MILLION.", "Odds: about 1 in a million.")
s4 = flip_scene(20, 30, Y3, "30 wins: $1 BILLION.", "Odds: 1 in 1.07 billion.")
s5 = recap("$1, doubled every win:", [("10 WINS", "$1,024", Y1), ("20 WINS", "$1 million", Y2), ("30 WINS", "$1 billion", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("A new chart snack tomorrow"), 5.0)],
      [(0, 4.5, 0.15, "Bet one dollar. Double it on every coin flip. Thirty in a row?"),
       (4.5, 11, 0.5, "Ten wins in a row turns one dollar into one thousand twenty four. The chance: one in a thousand."),
       (15.5, 12, 0.5, "Twenty wins: over a million dollars. But the odds are about one in a million."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "Thirty wins in a row: over one billion dollars. The chance? One in one point oh seven billion. If everyone on Earth tried, only about eight people would make it."),
       (46, 9.5, 0.4, "Every flip doubles the money, and halves your chances."),
       (55.5, 5, 0.4, "See you at the next chart snack.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Double a dollar, thirty flips in a row."),
       (3, 5, 0.2, "Ten wins: a thousand dollars."),
       (8, 6, 0.2, "Twenty wins: a million."),
       (14, 6, 0.2, "Thirty wins: a billion. One in a billion odds."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep33", "chartsnack_ep33_coinflips.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
