import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

GREEN = (90, 200, 120)

def bills(d, cx, cy, n, a, col=GREEN):
    for i in range(n):
        y = cy - i * 14
        d.rounded_rectangle([cx - 150, y - 34, cx + 150, y + 34], radius=8, fill=mix(col, a), outline=mix((30, 90, 50), a), width=3)
        d.ellipse([cx - 26, y - 22, cx + 26, y + 22], outline=mix((30, 90, 50), a), width=3)

def s1(t, D):
    im, d = frame_base()
    bills(d, 540, 640, 6, 1.0)
    text(d, (540, 820), "How heavy is", 90, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 960), "$1 TRILLION", font=F(int(130 * p)), fill=Y3, anchor="mm")
    text(d, (540, 1090), "in cash?", 84, WHITE, 1.0)
    return im

def weight_scene(title, col, sub, kg, bars, reveal, reveal_sub):
    def big(p):
        v = kg * p
        return f"{fmt(v)} kg" if kg < 1000 else f"{fmt(v / 1000)} tonnes"
    return bars_scene(title, col, sub, big, bars, reveal, reveal_sub)

s2 = weight_scene("$1 MILLION", Y1, "one $100 bill weighs about 1 gram", 10,
                  [("IN $100 BILLS", "10 kg", 0.01, Y1, True),
                   ("IN $1 BILLS", "1 tonne", 1.0, DGREY, False)],
                  "10 kg in hundreds.", "In $1 bills: about a small car.")
s3 = weight_scene("$1 BILLION", Y2, "in $100 bills", 10000,
                  [("AFRICAN ELEPHANT", "~6 tonnes", 0.6, DGREY, False),
                   ("$1 BILLION", "10 tonnes", 1.0, Y2, True)],
                  "Heavier than an elephant.", "10 million bills.")
s4 = weight_scene("$1 TRILLION", Y3, "in $100 bills", 1.0e7,
                  [("$1 BILLION", "10 tonnes", 0.001, DGREY, False),
                   ("EIFFEL TOWER", "~10,100 tonnes", 1.0, DGREY, False),
                   ("$1 TRILLION", "10,000 tonnes", 0.99, Y3, True)],
                  "As heavy as the Eiffel Tower.", "The entire tower.")
s5 = recap("Cash in $100 bills:", [("$1 MILLION", "10 kg", Y1), ("$1 BILLION", "10 tonnes", Y2), ("$1 TRILLION", "10,000 tonnes", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("Rice on a chessboard"), 5.0)],
      [(0, 4.5, 0.15, "How heavy is one trillion dollars, in cash?"),
       (4.5, 12, 0.5, "A hundred dollar bill weighs about one gram. So one million dollars is just ten kilograms. In one dollar bills, though, a whole tonne."),
       (16.5, 13, 0.5, "One billion dollars in hundreds: ten tonnes. Heavier than an African elephant."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "And one trillion? Ten thousand tonnes. About as heavy as the entire Eiffel Tower."),
       (46, 9, 0.4, "A million fits in a backpack. A trillion weighs as much as the Eiffel Tower."),
       (55, 5, 0.4, "Next: rice, on a chessboard.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "How heavy is a trillion dollars?"),
       (3, 5, 0.2, "One million: ten kilos."),
       (8, 6, 0.2, "One billion: heavier than an elephant."),
       (14, 6, 0.2, "One trillion: as heavy as the Eiffel Tower."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0), (14.5, 18.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep14", "chartsnack_ep14_weight.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
