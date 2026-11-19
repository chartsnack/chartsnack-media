import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

PENNY = 0.00152  # m, thickness of a US penny

def coin_stack(d, x, ground, h_px, a, col=(205, 127, 50)):
    dark = (150, 90, 35)
    if h_px < 2: return
    d.rectangle([x - 70, ground - h_px, x + 70, ground], fill=mix(col, a))
    for y in range(int(ground) - 10, int(ground - h_px), -10):
        d.line([(x - 70, y), (x + 70, y)], fill=mix(dark, a), width=2)
    d.ellipse([x - 70, ground - h_px - 14, x + 70, ground - h_px + 14], fill=mix((230, 160, 80), a))

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 470), "Stack $1 MILLION", 90, WHITE, 1.0)
    text(d, (540, 570), "in pennies.", 80, WHITE, 1.0)
    coin_stack(d, 540, 1150, 380 + 20 * math.sin(t * 3), 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1320), "HOW TALL?", font=F(int(130 * p)), fill=Y3, anchor="mm")
    return im

def stack_scene(title, col, coins, comp_lab, comp_m, reveal, reveal_sub):
    h = coins * PENNY
    mx = max(h, comp_m) * 1.1
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 400), title, 84, col, appear(t, 0))
        text(d, (540, 480), f"{fmt(coins)} pennies", 40, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        text(d, (540, 610), hfmt(h * p), 100, WHITE, appear(t, 0.2))
        a = appear(t, 0.3)
        ground, top = 1450, 760
        d.line([(120, ground), (960, ground)], fill=mix(GREY, a), width=4)
        coin_stack(d, 380, ground, (ground - top) * h * p / mx, a)
        ch = (ground - top) * comp_m / mx
        d.rectangle([660, ground - ch, 820, ground], fill=mix(DGREY, a))
        text(d, (740, ground - ch - 40), comp_lab, 34, GREY, a)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = stack_scene("$1", Y1, 100, "A pencil (19 cm)", 0.19, "15 CM.", "Shorter than a pencil.")
s3 = stack_scene("$1,000", Y2, 100000, "Great Pyramid (139 m)", 139, "152 METERS.", "Taller than the Great Pyramid.")
s4 = stack_scene("$1 MILLION", Y3, 1e8, "Space begins (100 km)", 100000, "152 KM.", "It reaches into space.")
s5 = recap("Pennies, stacked:", [("$1", "15 cm", Y1), ("$1,000", "152 m", Y2), ("$1 MILLION", "152 km", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("Save $1 more every day"), 5.0)],
      [(0, 4.5, 0.15, "A million dollars in pennies. How tall is the stack?"),
       (4.5, 11, 0.5, "A penny is one point five millimeters thick. One dollar, a hundred pennies: fifteen centimeters."),
       (15.5, 12, 0.5, "One thousand dollars: a hundred thousand pennies. One hundred fifty two meters. Taller than the Great Pyramid."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And one million dollars? A hundred million pennies, one hundred fifty two kilometers high. Past the line where space begins."),
       (46, 9.5, 0.4, "Fifteen centimeters. A pyramid. Space."),
       (55.5, 5, 0.4, "Next: saving one dollar more every day.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A million dollars in pennies. How tall?"),
       (3, 5, 0.2, "One dollar: fifteen centimeters."),
       (8, 6, 0.2, "A thousand: taller than the pyramid."),
       (14, 6, 0.2, "A million: into space."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep34", "chartsnack_ep34_pennies.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
