import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

LIGHT, DARK = (70, 74, 92), (42, 46, 61)

def board(d, x0, y0, size, upto, a, hl=None):
    c = size / 8
    for k in range(64):
        r, f = k // 8, k % 8
        x, y = x0 + f * c, y0 + (7 - r) * c
        base = LIGHT if (r + f) % 2 == 0 else DARK
        col = Y1 if k < upto else base
        if hl is not None and k == hl: col = Y3
        d.rectangle([x, y, x + c, y + c], fill=mix(col, a))

def big_num(n):
    return f"{n:,}"

def s1(t, D):
    im, d = frame_base()
    board(d, 340, 330, 400, 1, 1.0)
    text(d, (540, 850), "1 grain of rice.", 90, WHITE, 1.0)
    text(d, (540, 950), "Double it on every square.", 58, GREY, 1.0, bold=False)
    text(d, (540, 1100), "How much on", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1230), "SQUARE 64?", font=F(int(130 * p)), fill=Y3, anchor="mm")
    return im

def sq_scene(k0, k1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        k = int(round(k0 + (k1 - k0) * p))
        text(d, (540, 420), f"SQUARE {k}", 76, col, appear(t, 0))
        s = big_num(2 ** (k - 1))
        size = 100 if len(s) < 12 else (78 if len(s) < 20 else 60)
        text(d, (540, 560), s, size, WHITE, appear(t, 0.1))
        text(d, (540, 650), "grains", 40, GREY, appear(t, 0.1), bold=False)
        board(d, 220, 760, 640, k, appear(t, 0.3), hl=k - 1)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = sq_scene(1, 32, Y1, "Square 32: 2.1 billion.", "Halfway – that square alone: ~54 tonnes.")
s3 = sq_scene(32, 64, Y2, "Square 64: 9.2 quintillion.", "One single square.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "THE WHOLE BOARD", 70, Y3, appear(t, 0))
    text(d, (540, 495), "18.4 quintillion grains, ~25 mg each", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 680), f"{fmt(460 * p)} billion tonnes", 80, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    yrs = int(600 * p)
    for i in range(60):
        x, y = 140 + (i % 10) * 82, 820 + (i // 10) * 82
        on = i < yrs / 10
        d.rounded_rectangle([x, y, x + 64, y + 64], radius=10, fill=mix(Y3 if on else TRACK, a))
    text(d, (540, 1350), "1 square = 10 years of world rice harvest", 34, GREY, a, bold=False)
    text(d, (540, 1600), "600+ years of harvest.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "Every rice field on Earth.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("Doubling rice:", [("SQUARE 32", "2.1 billion", Y1), ("SQUARE 64", "9.2 quintillion", Y2), ("WHOLE BOARD", "600+ yrs of rice", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("How many years you sleep"), 5.0)],
      [(0, 4.5, 0.15, "One rice grain, doubled every square. How much on the last one?"),
       (4.5, 12, 0.5, "Square two: two grains. Square ten: five hundred twelve. By square thirty two, the middle of the board, two point one billion grains."),
       (16.5, 13, 0.5, "And it keeps doubling. Square sixty four alone holds nine point two quintillion grains."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "The whole board weighs around four hundred sixty billion tonnes. That's more than six hundred years of the entire world's rice harvest."),
       (46, 9, 0.4, "One grain on square one. Six centuries of rice on square sixty four."),
       (55, 5, 0.4, "Next: how many years of your life you sleep.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Double a rice grain sixty four times."),
       (3, 5, 0.2, "Square thirty two: two billion grains."),
       (8, 6, 0.2, "Square sixty four: nine quintillion."),
       (14, 6, 0.2, "Six hundred years of world rice harvest."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep15", "chartsnack_ep15_rice.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
