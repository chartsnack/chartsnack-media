import sys, random; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

YR = 365.25 * 86400
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def keys(d, word, t, a, y=1020, size=96):
    """random letters flicker, target word underneath"""
    rnd = random.Random(int(t * 12))
    n = len(word); w = min(110, 900 // n)
    x0 = 540 - w * n / 2
    for i in range(n):
        x = x0 + i * w
        d.rounded_rectangle([x + 4, y - 60, x + w - 4, y + 60], radius=14, fill=mix(TRACK, a))
        d.text((x + w / 2, y), rnd.choice(ABC), font=F(int(size * w / 110)), fill=mix(WHITE, a), anchor="mm")
    text(d, (540, y + 120), f"target: {word}", 40, GREY, a, bold=False)

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 480), "A monkey hits", 84, WHITE, 1.0)
    text(d, (540, 580), "random keys.", 84, WHITE, 1.0)
    text(d, (540, 700), "When does it type", 60, GREY, 1.0, bold=False)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 830), "BANANA?", font=F(int(140 * p)), fill=Y1, anchor="mm")
    keys(d, "BANANA", t, 1.0, y=1160)
    return im

def word_scene(word, col, tries, dur_txt, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 400), word, 110, col, appear(t, 0))
        text(d, (540, 490), f"{len(word)} letters, 1 try per second", 38, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        text(d, (540, 650), fmt(tries * p), 96, WHITE, appear(t, 0.2))
        text(d, (540, 740), "tries needed (on average)", 40, GREY, appear(t, 0.2), bold=False)
        keys(d, word, t, appear(t, 0.3), y=1000)
        text(d, (540, 1330), dur_txt, 72, col, appear(t, D - 3.4))
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = word_scene("CAT", Y1, 26 ** 3, "≈ 5 hours", "CAT: one afternoon.", "26 x 26 x 26 = 17,576 tries")
s3 = word_scene("BANANA", Y2, 26 ** 6, "≈ 10 years", "BANANA: 10 YEARS.", "Non-stop, day and night.")
s4 = word_scene("CHARTSNACK", Y3, 26 ** 10, "≈ 4.5 million years", "4.5 MILLION years.", "Just 4 more letters.")
s5 = recap("Random typing, 1 try/sec:", [("CAT", "5 hours", Y1), ("BANANA", "10 years", Y2), ("CHARTSNACK", "4.5 million years", Y3)], size=60)

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("How many breaths in a life?"), 5.0)],
      [(0, 4.5, 0.15, "A monkey hits random keys. When does it type banana?"),
       (4.5, 11, 0.5, "One random try per second. A three letter word like cat: seventeen thousand tries. About five hours."),
       (15.5, 12, 0.5, "Banana has six letters. That's three hundred million tries. About ten years, non stop."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And chart snack? Ten letters. One hundred forty trillion tries. Four and a half million years. Every extra letter makes it twenty six times harder."),
       (46, 9.5, 0.4, "Five hours. Ten years. Four and a half million years."),
       (55.5, 5, 0.4, "Next: how many breaths do you take in a life?")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "When does a monkey type banana?"),
       (3, 5, 0.2, "Cat: about five hours."),
       (8, 6, 0.2, "Banana: about ten years."),
       (14, 6, 0.2, "Chart snack: four and a half million years."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep23", "chartsnack_ep23_monkey.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
