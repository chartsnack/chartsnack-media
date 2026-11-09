import sys; sys.path.insert(0, "/home/claude/chartsnack"); sys.path.insert(0, "/home/claude/chartsnack/ep05")
from lib import *
import ep05 as E

def s1(t, D):
    im, d = frame_base()
    E.heart(d, 540, 520, 300 * E.beat(t), Y3, 1.0)
    text(d, (540, 900), "Your heart beats", 90, WHITE, 1.0)
    text(d, (540, 1010), "how many times", 90, WHITE, 1.0)
    text(d, (540, 1120), "in your life?", 90, Y3, 1.0)
    return im

def s2(t, D): return E.counter_scene(t, "ONE DAY", Y1, 70 * 60 * 24, "beats", "Over 100,000", "Every single day.", dur=3.0)
def s3(t, D): return E.counter_scene(t, "ONE YEAR", Y2, 70 * 60 * 24 * 365.25, "beats", "Almost 37 million", "No breaks.", dur=3.0)
def s4(t, D): return E.counter_scene(t, "80 YEARS", Y3, 70 * 60 * 24 * 365.25 * 80, "beats", "About 3 BILLION", "Counting them takes 93 years.", dur=3.5)
def s5(t, D):
    im, d = frame_base()
    text(d, (540, 600), "During this video:", 80, WHITE, appear(t, 0))
    E.heart(d, 540, 860, 230 * E.beat(t), Y3, 1.0)
    text(d, (540, 1180), "about 30 beats", 100, Y3, appear(t, 0.6))
    text(d, (540, 1300), "Follow for more", 48, Y1, appear(t, 2.0))
    return im

SCENES = [("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 5.0), ("s4", s4, 7.0), ("s5", s5, 5.0)]
LINES = [
    (0, 3, 0.05, "How many times will your heart beat?"),
    (3, 5, 0.2, "One day: over a hundred thousand."),
    (8, 5, 0.2, "One year: almost thirty-seven million."),
    (13, 7, 0.2, "A whole life: about three billion beats."),
    (20, 5, 0.2, "And during this video, about thirty."),
]
TICKS = [(3.5, 6.5), (8.5, 11.5), (13.5, 17.0)]
DINGS = [0.1, 7.0, 12.0, 17.5, 20.8]

if __name__ == "__main__":
    out = "/home/claude/chartsnack/tt/out05"
    if sys.argv[1:] == ["stills"]:
        stills(out, SCENES, [0.0, 4.5, 4.5, 6.5, 4.5])
    else:
        build(out, SCENES, LINES, TICKS, DINGS, "chartsnack_tt05_heart.mp4", only=sys.argv[1:] or None)
