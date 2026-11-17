import sys, random; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

GREEN = (88, 190, 110)
WATER = (40, 70, 110)
PADS = []
_r = random.Random(3)
for _ in range(900):
    PADS.append((_r.uniform(-1, 1), _r.uniform(-1, 1), _r.random()))
PADS = [p for p in PADS if p[0] ** 2 + p[1] ** 2 < 0.92][:600]
PADS.sort(key=lambda p: p[2])

def pond(d, cx, cy, R, frac, a):
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=mix(WATER, a))
    r = max(6, R * math.sqrt(min(1.0, frac)))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(GREEN, a))
    dark = (60, 150, 85)
    for (x, y, _) in PADS[:200]:
        if (x * R) ** 2 + (y * R) ** 2 < (r - 20) ** 2:
            px, py = cx + x * R, cy + y * R
            d.arc([px - 18, py - 18, px + 18, py + 18], 20, 340, fill=mix(dark, a), width=3)

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 430), "Lily pads DOUBLE every day.", 62, WHITE, 1.0)
    text(d, (540, 520), "On day 30 the pond is full.", 56, GREY, 1.0, bold=False)
    pond(d, 540, 870, 290, 1.0, 1.0)
    text(d, (540, 1270), "When is it", 84, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1390), "HALF FULL?", font=F(int(120 * p)), fill=Y1, anchor="mm")
    return im

def day_scene(d0, d1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        day = d0 + (d1 - d0) * p
        frac = 2 ** (int(day + 1e-6) - 30)
        text(d, (540, 400), f"DAY {int(day)}", 100, col, appear(t, 0))
        pct = 100 * frac
        s = f"{pct:.0f} % covered" if pct >= 10 else (f"{pct:.1f} % covered" if pct >= 0.1 else f"{pct:.4f} % covered")
        text(d, (540, 510), s, 56, WHITE, appear(t, 0.1))
        pond(d, 540, 930, 330, frac, appear(t, 0.2))
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = day_scene(1, 20, Y1, "Day 20: 0.1 %.", "After 2 weeks: almost nothing.")
s3 = day_scene(20, 28, Y2, "Day 28: only 25 %.", "Still mostly water...")
s4 = day_scene(28, 29, Y3, "Day 29: HALF FULL.", "One day before the end.")
s5 = recap("Doubling lily pads:", [("DAY 20", "0.1 %", Y1), ("DAY 28", "25 %", Y2), ("DAY 29", "50 %", Y3)])

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("$100 million, $10,000 a day"), 5.0)],
      [(0, 4.5, 0.15, "Lily pads double daily. Full on day thirty. When half full?"),
       (4.5, 11, 0.5, "Day one: a single pad. Twenty days later, the pond is still only about zero point one percent covered."),
       (15.5, 12, 0.5, "Day twenty eight: just a quarter of the pond. Most of it is still open water."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And then it explodes. Day twenty nine: half full. Day thirty: completely covered. Half the pond fills in the very last day."),
       (46, 9.5, 0.4, "That's doubling. Nothing, nothing, nothing, then everything."),
       (55.5, 5, 0.4, "Next: one hundred million, ten thousand a day.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Full on day thirty. When half full?"),
       (3, 5, 0.2, "Day twenty: almost nothing."),
       (8, 6, 0.2, "Day twenty eight: only a quarter."),
       (14, 6, 0.2, "Day twenty nine: half full!"),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep29", "chartsnack_ep29_lilypads.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 12.0, 8.5, 4.0], [0.0, 4.8, 5.8, 4.0, 4.8])
