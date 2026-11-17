import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

GEN = 25  # years per generation (rough average)

def person(d, x, y, s, col, a):
    d.ellipse([x - 9 * s, y - 30 * s, x + 9 * s, y - 12 * s], fill=mix(col, a))
    d.rounded_rectangle([x - 13 * s, y - 8 * s, x + 13 * s, y + 18 * s], radius=int(6 * s), fill=mix(col, a))

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 470), "The Great Pyramid", 84, WHITE, 1.0)
    d.polygon([(540, 560), (330, 860), (750, 860)], fill=Y2)
    d.polygon([(540, 560), (540, 860), (750, 860)], fill=(214, 130, 20))
    text(d, (540, 1000), "How many", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1120), "GENERATIONS", font=F(int(118 * p)), fill=Y3, anchor="mm")
    text(d, (540, 1240), "ago was it built?", 76, WHITE, 1.0)
    return im

def gen_scene(title, col, years, sub, reveal, reveal_sub, per_icon=1):
    gens = years / GEN
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 400), title, 76, col, appear(t, 0))
        text(d, (540, 480), sub, 38, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        g = gens * p
        text(d, (540, 620), f"{fmt(g)} generations", 84, WHITE, appear(t, 0.2))
        a = appear(t, 0.3)
        n = int(round(g / per_icon))
        for k in range(min(n, 200)):
            r, c = divmod(k, 20)
            person(d, 100 + c * 46, 780 + r * 52, 1.0, col, a)
        if per_icon > 1: text(d, (540, 1340), f"1 figure = {per_icon} generations", 36, GREY, a, bold=False)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = gen_scene("SINCE YEAR 1", Y1, 2026, "~25 years per generation", "About 81 generations.", "81 parents in a row.")
s3 = gen_scene("SINCE THE PYRAMID", Y2, 4580, "built around 2560 BC", "Only ~180 generations!", "Fits in one school hall.")
s4 = gen_scene("SINCE THE FIRST HUMANS", Y3, 300000, "Homo sapiens: ~300,000 years", "~12,000 generations.", "Still a small town.", per_icon=60)
s5 = recap("Generations ago:", [("YEAR 1", "~81", Y1), ("GREAT PYRAMID", "~180", Y2), ("FIRST HUMANS", "~12,000", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("The lily pad riddle"), 5.0)],
      [(0, 4.5, 0.15, "How many generations ago was the Great Pyramid built?"),
       (4.5, 11, 0.5, "Count about twenty five years per generation. Back to the year one, that's only around eighty one parents in a row."),
       (15.5, 12, 0.5, "The Great Pyramid, around twenty five sixty BC? Just about one hundred eighty generations. They'd all fit in one school hall."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And all the way back to the first modern humans, about three hundred thousand years ago: roughly twelve thousand generations. A small town of ancestors."),
       (46, 9.5, 0.4, "History feels endless. In generations, it's surprisingly short."),
       (55.5, 5, 0.4, "Next: the lily pad riddle.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Pyramids: how many generations ago?"),
       (3, 5, 0.2, "Year one: about eighty."),
       (8, 6, 0.2, "The pyramid: only one hundred eighty."),
       (14, 6, 0.2, "First humans: about twelve thousand."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep28", "chartsnack_ep28_generations.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
