import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

YR = 365.25 * 86400

def towers(d, n, a, y=1150, col=Y2, moved=0.0):
    """3 pegs, n discs (max 10 drawn), a fraction 'moved' shown on the right peg"""
    for px in (220, 540, 860):
        d.rounded_rectangle([px - 8, y - 330, px + 8, y], radius=6, fill=mix(GREY, a))
    d.rounded_rectangle([90, y, 990, y + 18], radius=8, fill=mix(GREY, a))
    k = min(n, 10)
    right = int(round(k * moved))
    for i in range(k):
        w = 125 - i * 9
        on_right = i < right
        px = 860 if on_right else 220
        lvl = i if on_right else i - right
        yy = y - 28 - lvl * 30
        cc = Y3 if on_right else col
        d.rounded_rectangle([px - w, yy - 12, px + w, yy + 12], radius=10, fill=mix(cc, a))

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 430), "Move a tower of", 76, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 550), "64 DISCS", font=F(int(130 * p)), fill=Y3, anchor="mm")
    text(d, (540, 660), "1 move per second. Never a big", 40, GREY, 1.0, bold=False)
    text(d, (540, 710), "disc on a small one.", 40, GREY, 1.0, bold=False)
    towers(d, 10, 1.0, y=1150, moved=0.0)
    text(d, (540, 1330), "How long?", 110, Y1, 1.0)
    return im

def hanoi_scene(n, col, dur_label, reveal, reveal_sub):
    moves = 2 ** n - 1
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 400), f"{n} DISCS", 96, col, appear(t, 0))
        p = prog(t, D)
        text(d, (540, 560), f"{moves:,}" if p >= 1 else fmt(moves * p), 88 if n < 40 else 64, WHITE, appear(t, 0.2))
        text(d, (540, 650), "moves (2 to the power of n, minus 1)", 36, GREY, appear(t, 0.2), bold=False)
        towers(d, n, appear(t, 0.3), y=1150, col=col, moved=p)
        text(d, (540, 1330), dur_label, 72, col, appear(t, D - 3.4))
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = hanoi_scene(10, Y1, "≈ 17 minutes", "10 discs: 17 MINUTES.", "1,023 moves. Easy.")
s3 = hanoi_scene(20, Y2, "≈ 12 days", "20 discs: 12 DAYS.", "Over a million moves. Non-stop.")
s4 = hanoi_scene(64, Y3, "≈ 585 billion years", "585 BILLION YEARS.", "42x the age of the universe.")
s5 = recap("Tower of Hanoi, 1 move/sec:", [("10 DISCS", "17 minutes", Y1), ("20 DISCS", "12 days", Y2), ("64 DISCS", "585 billion years", Y3)], size=60)

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("$1 BILLION, 80 years to spend"), 5.0)],
      [(0, 4.5, 0.15, "Sixty four discs. One move per second. How long?"),
       (4.5, 11, 0.5, "The rule: one disc at a time, never a big one on a small one. Ten discs take one thousand twenty three moves. Seventeen minutes."),
       (15.5, 12, 0.5, "Every extra disc doubles the work. Twenty discs: over a million moves. Twelve days, non stop."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And sixty four discs? Eighteen quintillion moves. Five hundred eighty five billion years. About forty two times the age of the universe."),
       (46, 9.5, 0.4, "Seventeen minutes. Twelve days. Forever, basically."),
       (55.5, 5, 0.4, "Next: a billion dollars, and eighty years to spend it.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Sixty four discs. One move a second."),
       (3, 5, 0.2, "Ten discs: seventeen minutes."),
       (8, 6, 0.2, "Twenty discs: twelve days."),
       (14, 6, 0.2, "Sixty four: five hundred eighty five billion years."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep26", "chartsnack_ep26_hanoi.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
