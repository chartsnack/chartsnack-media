import sys; sys.path.insert(0, "/home/claude/chartsnack"); sys.path.insert(0, "/home/claude/chartsnack/ep04")
from lib import *
import ep04 as E

def s1(t, D):
    im, d = frame_base()
    a = 1.0; pulse = 1 + 0.05 * math.sin(t * 8)
    text(d, (540, 560), "Fold paper", 110, WHITE, a)
    d.text((540, 760), "42 times", font=F(int(170 * pulse)), fill=Y3, anchor="mm")
    text(d, (540, 960), "= how thick?", 100, WHITE, a)
    return im

def s2(t, D): return E.fold_scene(t, 0, 23, Y1, "Taller than the", "Burj Khalifa (828 m)", 3.6)
def s3(t, D): return E.fold_scene(t, 23, 42, Y2, "Past the Moon.", "The Moon is 384,400 km away.", 3.6)
def s4(t, D): return E.fold_scene(t, 42, 51, Y3, "Past the Sun.", "Just 9 more folds.", 2.6)
def s5(t, D):
    im, d = frame_base()
    text(d, (540, 620), "The catch?", 96, WHITE, appear(t, 0))
    text(d, (540, 800), "Real world record:", 60, GREY, appear(t, 0.5), bold=False)
    text(d, (540, 980), "12 folds.", 150, Y1, appear(t, 1.0))
    text(d, (540, 1250), "Follow for more", 48, Y3, appear(t, 2.2))
    return im

SCENES = [("s1", s1, 3.0), ("s2", s2, 6.0), ("s3", s3, 6.0), ("s4", s4, 5.0), ("s5", s5, 5.0)]
LINES = [
    (0, 3, 0.05, "Fold paper forty-two times. How thick?"),
    (3, 6, 0.2, "Twenty-three folds: taller than the Burj Khalifa."),
    (9, 6, 0.2, "Forty-two folds: past the Moon."),
    (15, 5, 0.2, "Nine more, and you pass the Sun."),
    (20, 5, 0.2, "The catch? The record is twelve folds."),
]
TICKS = [(3.2, 6.8), (9.2, 12.8), (15.2, 17.8)]
DINGS = [0.1, 7.6, 13.6, 18.6, 21.0]

if __name__ == "__main__":
    out = "/home/claude/chartsnack/tt/out04"
    if sys.argv[1:] == ["stills"]:
        stills(out, SCENES, [0.0, 5.5, 5.5, 4.5, 4.5])
    else:
        build(out, SCENES, LINES, TICKS, DINGS, "chartsnack_tt04_paper.mp4", only=sys.argv[1:] or None)
