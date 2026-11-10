import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

ORANGE = (232, 120, 40)
BLUE = (70, 150, 255)

def ball(d, cx, cy, r, a=1.0, col=ORANGE):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(col, a))
    if r > 30:
        line = mix((40, 25, 15), a); w = max(2, int(r / 30))
        d.line([(cx - r, cy), (cx + r, cy)], fill=line, width=w)
        d.line([(cx, cy - r), (cx, cy + r)], fill=line, width=w)
        d.arc([cx - r * 1.6, cy - r, cx - r * 0.4, cy + r], -60, 60, fill=line, width=w)
        d.arc([cx + r * 0.4, cy - r, cx + r * 1.6, cy + r], 120, 240, fill=line, width=w)

def s1(t, D):
    im, d = frame_base()
    ball(d, 540, 560, 150)
    text(d, (540, 820), "Shrink Earth", 96, WHITE, 1.0)
    text(d, (540, 920), "to a basketball.", 76, GREY, 1.0, bold=False)
    text(d, (540, 1080), "How tall is", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1210), "EVEREST?", font=F(int(140 * p)), fill=Y3, anchor="mm")
    return im

s2 = bars_scene("ON A 24 cm BALL", Y1, "Earth: 12,742 km wide", lambda p: f"{0.17 * p:.2f} mm",
                [("MOUNT EVEREST", "0.17 mm", 0.17 / 0.25, Y1, True),
                 ("DEEPEST OCEAN", "0.21 mm", 0.21 / 0.25, BLUE, True),
                 ("A SHEET OF PAPER", "~0.1 mm", 0.1 / 0.25, DGREY, False)],
                "Less than 2 sheets of paper.", "Smoother than it looks.")

s3 = bars_scene("GOING UP", Y2, "same scale", lambda p: f"{7.7 * p:.1f} mm",
                [("EDGE OF SPACE (100 km)", "1.9 mm", 1.9 / 8, Y2, True),
                 ("SPACE STATION (400 km)", "7.7 mm", 7.7 / 8, Y2, True),
                 ("MOUNT EVEREST", "0.17 mm", 0.17 / 8, DGREY, False)],
                "Space starts 2 mm up.", "The ISS: less than 1 cm above the ball.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "AND THE MOON?", 70, Y3, appear(t, 0))
    text(d, (540, 495), "a 6.5 cm ball – about a tennis ball", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    a = appear(t, 0.3)
    ball(d, 170, 900, 90, a)
    mx = 300 + (850 - 300) * p
    ball(d, mx, 900, 25, a, col=(200, 200, 210))
    y = 1060
    d.line([(170, y), (mx, y)], fill=mix(WHITE, a), width=4)
    d.line([(170, y - 15), (170, y + 15)], fill=mix(WHITE, a), width=4)
    d.line([(mx, y - 15), (mx, y + 15)], fill=mix(WHITE, a), width=4)
    text(d, (540, 700), f"{7.2 * p:.1f} metres away", 80, WHITE, appear(t, 0.2))
    text(d, (540, 1600), "7 metres away.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "Across a whole room.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("Earth as a basketball:", [("EVEREST", "0.17 mm", Y1), ("SPACE", "1.9 mm up", Y2), ("THE MOON", "7 m away", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("Your real lottery odds"), 5.0)],
      [(0, 4.5, 0.15, "Shrink Earth to a basketball. How tall is Mount Everest?"),
       (4.5, 12, 0.5, "Zero point one seven millimetres. The deepest ocean trench: zero point two one. Less than two sheets of paper."),
       (16.5, 13, 0.5, "Now go up. Space begins just two millimetres above the ball. The space station orbits less than one centimetre up."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "And the Moon? A ball the size of a tennis ball, about seven metres away. Across a whole room."),
       (46, 9, 0.4, "Mountains, oceans, the space station. All within one centimetre of the ball."),
       (55, 5, 0.4, "Next: your real lottery odds.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Earth is a basketball. How tall is Everest?"),
       (3, 5, 0.2, "Zero point one seven millimetres."),
       (8, 6, 0.2, "Space starts just two millimetres up."),
       (14, 6, 0.2, "The Moon: a tennis ball, seven metres away."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 4.8), (8.5, 10.8), (14.5, 18.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep11", "chartsnack_ep11_basketball.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
