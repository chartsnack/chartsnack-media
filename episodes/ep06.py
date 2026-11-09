import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

BILL = 0.00010922  # m, thickness of a $100 bill
GROUND, TOP = 1480, 520
X0, X1 = 330, 470

def stack_scene(t, D, title, col, height, axis, marks, reveal, sub):
    im, d = frame_base()
    text(d, (540, 400), title, 76, col, appear(t, 0))
    p = ease_io((t - 0.5) / max(1.0, D - 3.2))
    h = height * p
    text(d, (540, 490), hfmt(h), 64, WHITE, appear(t, 0.2))
    a = appear(t, 0.3)
    d.line([(150, GROUND), (930, GROUND)], fill=mix(GREY, a), width=4)
    for (m, lab, sublab) in marks:
        y = GROUND - (GROUND - TOP) * m / axis
        reached = h >= m
        c = WHITE if reached else GREY
        for x in range(500, 930, 24):
            d.line([(x, y), (x + 12, y)], fill=mix(c, a * 0.8), width=3)
        text(d, (930, y - 26), lab, 34, c, a, anchor="rm")
        if sublab: text(d, (930, y + 22), sublab, 26, GREY, a, bold=False, anchor="rm")
    top = GROUND - (GROUND - TOP) * min(h, axis) / axis
    if GROUND - top > 2:
        d.rectangle([X0, top, X1, GROUND], fill=mix(col, a))
        dark = tuple(int(c * 0.75) for c in col)
        for y in range(int(GROUND) - 14, int(top), -14):
            d.line([(X0, y), (X1, y)], fill=mix(dark, a), width=2)
    text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
    text(d, (540, 1690), sub, 40, GREY, appear(t, D - 2.0), bold=False)
    return im

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 640), "Stack", 96, WHITE, 1.0)
    pulse = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 790), "$1 BILLION", font=F(int(150 * pulse)), fill=Y3, anchor="mm")
    text(d, (540, 940), "in $100 bills.", 76, WHITE, 1.0)
    text(d, (540, 1120), "How tall?", 110, Y1, appear(t, 0.5))
    return im

def s2(t, D): return stack_scene(t, D, "$1 MILLION", Y1, 1e4 * BILL, 2.0,
                                 [(1.75, "Average man", "1.75 m")], "About hip high.", "10,000 bills")
def s3(t, D): return stack_scene(t, D, "$1 BILLION", Y2, 1e7 * BILL, 1150,
                                 [(330, "Eiffel Tower", "330 m"), (828, "Burj Khalifa", "828 m")], "Over 1 km tall.", "10 million bills")
def s4(t, D): return stack_scene(t, D, "$1 TRILLION", Y3, 1e10 * BILL, 1150e3,
                                 [(100e3, "Space begins", "100 km"), (408e3, "Space station", "~400 km")], "Over 1,000 km.", "Into space.")

def s5(t, D):
    im, d = frame_base()
    text(d, (540, 440), "In $100 bills:", 64, WHITE, appear(t, 0))
    y = 680
    for st, lab, val, c in [(0.4, "$1 MILLION", "1.09 m", Y1), (1.6, "$1 BILLION", "1.09 km", Y2), (2.8, "$1 TRILLION", "1,092 km", Y3)]:
        a = appear(t, st)
        text(d, (90, y), lab, 44, c, a, anchor="lm")
        text(d, (900, y + 75), val, 72, WHITE, a, anchor="rm")
        y += 250
    if D < 6: text(d, (540, 1500), "Follow for more", 48, Y1, appear(t, 3.4))
    return im

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 15.0), ("sx", sub_scene(), 2.5), ("s4", s4, 15.0), ("s5", s5, 9.0),
       ("s6", outro_next("$15/hour vs $1 BILLION"), 5.0)],
      [(0, 4.5, 0.15, "Stack one billion dollars in hundred dollar bills. How tall is it?"),
       (4.5, 11, 0.5, "One million first. That's ten thousand bills. A stack about hip high."),
       (15.5, 15, 0.5, "One billion is ten million bills. It passes the Eiffel Tower, then the Burj Khalifa, and keeps going. Over one kilometer tall."),
       (30.5, 2.5, 0.1, "Subscribe for more."),
       (33, 15, 0.5, "And one trillion? Over a thousand kilometers high. Past where space begins, and way past the space station."),
       (48, 9, 0.4, "A million fits under your desk. A trillion leaves the planet."),
       (57, 5, 0.4, "Next: fifteen dollars an hour, versus a billion.")],
      [(5.0, 12.8), (16.0, 27.8), (33.5, 45.3)],
      [0.2, 13.0, 28.2, 30.7, 45.6, 48.4, 49.6, 50.8, 57.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A billion dollars in hundreds. How tall?"),
       (3, 5, 0.2, "One million: about hip high."),
       (8, 6, 0.2, "One billion: taller than the Burj Khalifa."),
       (14, 6, 0.2, "One trillion: over a thousand kilometers. Into space."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 4.8), (8.5, 10.8), (14.5, 16.8)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep06", "chartsnack_ep06_stack.mp4", YT, TT, [3.5, 10.5, 14.5, 1.3, 14.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
