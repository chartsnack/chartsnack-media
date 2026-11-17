import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

LIGHT, DARK = (232, 214, 180), (150, 110, 80)

def board(d, cx, cy, size, a, hi=0):
    s = size / 8
    x0, y0 = cx - size / 2, cy - size / 2
    for r in range(8):
        for c in range(8):
            col = LIGHT if (r + c) % 2 == 0 else DARK
            d.rectangle([x0 + c * s, y0 + r * s, x0 + (c + 1) * s, y0 + (r + 1) * s], fill=mix(col, a))
    for i in range(hi):
        r, c = divmod((i * 37) % 64, 8)
        d.ellipse([x0 + c * s + s * 0.3, y0 + r * s + s * 0.3, x0 + c * s + s * 0.7, y0 + r * s + s * 0.7], fill=mix(Y3, a))

def s1(t, D):
    im, d = frame_base()
    board(d, 540, 700, 520, 1.0)
    text(d, (540, 1080), "How many different", 76, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1200), "CHESS GAMES", font=F(int(120 * p)), fill=Y1, anchor="mm")
    text(d, (540, 1320), "are possible?", 76, WHITE, 1.0)
    return im

def chess_scene(title, col, n, sub, reveal, reveal_sub, big=None):
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 400), title, 76, col, appear(t, 0))
        text(d, (540, 480), sub, 38, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        text(d, (540, 610), big if big else fmt(n * p), 100, WHITE, appear(t, 0.2))
        text(d, (540, 700), "possible games so far", 40, GREY, appear(t, 0.2), bold=False)
        board(d, 540, 1080, 440, appear(t, 0.3), hi=int(12 * p))
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = chess_scene("1 MOVE EACH", Y1, 400, "white 20 options x black 20", "400 GAMES.", "After just one move each.")
s3 = chess_scene("3 MOVES EACH", Y2, 119060324, "6 moves in total", "119 MILLION.", "After only 3 moves each!")
s4 = chess_scene("A FULL GAME", Y3, 0, "estimate (Shannon number)", "~10^120 GAMES.", "Atoms in the universe: only ~10^80.", big="10^120")
s5 = recap("Possible chess games:", [("1 MOVE EACH", "400", Y1), ("3 MOVES EACH", "119 million", Y2), ("WHOLE GAME", "~10^120", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("Win 20 coin flips in a row"), 5.0)],
      [(0, 4.5, 0.15, "How many different chess games are possible?"),
       (4.5, 11, 0.5, "White has twenty possible first moves. Black has twenty answers. That's already four hundred games."),
       (15.5, 12, 0.5, "After just three moves each, there are over one hundred nineteen million different games."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "For a whole game, a famous estimate is ten to the power of one hundred twenty. There are only about ten to the eighty atoms in the observable universe."),
       (46, 9.5, 0.4, "More chess games than atoms in the universe."),
       (55.5, 5, 0.4, "Next: winning twenty coin flips in a row.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "How many chess games are possible?"),
       (3, 5, 0.2, "One move each: four hundred."),
       (8, 6, 0.2, "Three moves each: a hundred nineteen million."),
       (14, 6, 0.2, "Whole game: more than atoms in the universe."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep32", "chartsnack_ep32_chess.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
