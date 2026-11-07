import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

BPM = 70
def heart(d, cx, cy, s, col, a):
    # simple heart: two circles + triangle
    r = 0.30 * s
    d.ellipse([cx - 2 * r, cy - r, cx, cy + r], fill=mix(col, a))
    d.ellipse([cx, cy - r, cx + 2 * r, cy + r], fill=mix(col, a))
    d.polygon([(cx - 1.93 * r, cy + 0.35 * r), (cx + 1.93 * r, cy + 0.35 * r), (cx, cy + 2.3 * r)], fill=mix(col, a))

def beat(t):  # pulse 70 bpm
    ph = (t * BPM / 60) % 1
    return 1 + 0.12 * math.exp(-ph * 9)

def s1(t, D):
    im, d = frame_base()
    heart(d, 540, 520, 300 * beat(t), Y3, appear(t, -1))
    text(d, (540, 900), "How many times will", 76, WHITE, appear(t, -1))
    text(d, (540, 990), "your heart beat", 76, WHITE, appear(t, -1))
    text(d, (540, 1080), "in your life?", 76, WHITE, appear(t, -1))
    text(d, (540, 1260), "???", 150, Y3, appear(t, 2.4))
    return im

def counter_scene(t, title, col, total, unit_label, reveal, sub, dur=7.0, small=None):
    im, d = frame_base()
    text(d, (540, 420), title, 70, col, appear(t, 0))
    heart(d, 540, 600, 170 * beat(t), col, appear(t, 0.1))
    p = ease_io((t - 0.5) / dur)
    text(d, (540, 870), fmt(total * p), 120, WHITE, appear(t, 0.2))
    text(d, (540, 970), unit_label, 40, GREY, appear(t, 0.2), bold=False)
    text(d, (540, 1150), reveal, 64, col, appear(t, dur + 0.8))
    text(d, (540, 1240), sub, 44, GREY, appear(t, dur + 1.3), bold=False)
    return im

def s2(t, D): return counter_scene(t, "ONE DAY", Y1, BPM * 60 * 24, "beats", "Over 100,000", "Every single day.")
def s3(t, D): return counter_scene(t, "ONE YEAR", Y2, BPM * 60 * 24 * 365.25, "beats", "Almost 37 million", "Without a single break.")
def s4(t, D): return counter_scene(t, "A LIFETIME (80 YEARS)", Y3, BPM * 60 * 24 * 365.25 * 80, "beats", "About 3 BILLION", "Counting them would take 93 years.", dur=9.0)

def s5(t, D):
    im, d = frame_base()
    text(d, (540, 560), "And while you", 70, WHITE, appear(t, 0))
    text(d, (540, 650), "watched this video...", 70, WHITE, appear(t, 0.3))
    heart(d, 540, 900, 230 * beat(t), Y3, appear(t, 0.8))
    n = min(72, int(max(0, t - 1.0) * 10))
    text(d, (540, 1230), f"{n} beats", 110, Y3, appear(t, 1.0))
    text(d, (540, 1340), "at 70 beats per minute", 40, GREY, appear(t, 1.2), bold=False)
    return im

SCENES = [("s1", s1, 5.0), ("s2", s2, 12.0), ("s3", s3, 12.0), ("s4", s4, 16.0), ("s5", s5, 12.0), ("s6", outro, 5.0)]
LINES = [
    (0, 5, 0.15, "How many times will your heart beat in your whole life?"),
    (5, 12, 0.6, "At seventy beats a minute, that's a hundred thousand beats every single day."),
    (17, 12, 0.6, "In one year? Almost thirty-seven million. Without a single break."),
    (29, 16, 0.6, "And over an eighty year life... about three billion beats. Just counting them, one per second, would take ninety-three years."),
    (45, 12, 0.6, "And while you watched this video, your heart beat about seventy times."),
    (57, 5, 0.5, "Follow Chart Snack. A new one every day."),
]
TICKS = [(5.5, 12.5), (17.5, 24.5), (29.5, 38.5)]
DINGS = [0.3, 2.4, 13.3, 25.3, 39.3, 46.0, 57.6]

if __name__ == "__main__":
    out = "/home/claude/chartsnack/ep05/out"
    if sys.argv[1:] == ["stills"]:
        stills(out, SCENES, [0.0, 11, 11, 15, 11, 4])
    else:
        build(out, SCENES, LINES, TICKS, DINGS, "chartsnack_ep05_heart.mp4", only=sys.argv[1:] or None)
