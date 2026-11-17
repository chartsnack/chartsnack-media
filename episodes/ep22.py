import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

BILL = 0.156  # m, length of a US $1 bill (6.14 in)

def km(v):
    if v >= 1e6: return f"{v / 1e6:.0f} million km"
    return f"{fmt(v)} km"

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 520), "Lay $1 BILLION", 96, WHITE, 1.0)
    text(d, (540, 630), "in $1 bills, end to end.", 64, WHITE, 1.0)
    # row of bills
    for i in range(6):
        x = 120 + i * 145
        d.rounded_rectangle([x, 760, x + 130, 820], radius=6, fill=(88, 140, 90))
        d.ellipse([x + 50, 775, x + 80, 805], outline=(200, 230, 200), width=3)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1000), "HOW FAR?", font=F(int(140 * p)), fill=Y3, anchor="mm")
    return im

def dist_scene(title, col, sub, total_km, comps, reveal, reveal_sub):
    mx = max([total_km] + [c[1] for c in comps])
    bars = [(lab, km(v), v / mx, DGREY, False) for lab, v in comps] + [(title, km(total_km), total_km / mx, col, True)]
    return bars_scene(title.upper(), col, sub, lambda p: km(total_km * p), bars, reveal, reveal_sub, big_size=96)

s2 = dist_scene("$1 million", Y1, "1 million bills", 156, [("Marathon", 42.2)], "156 km.", "Almost 4 marathons.")
s3 = dist_scene("$1 billion", Y2, "1 billion bills", 156000, [("Around Earth", 40075)], "156,000 km.", "Nearly 4x around the Earth.")
s4 = dist_scene("$1 trillion", Y3, "1 trillion bills", 156e6, [("Earth to Moon", 384400), ("Earth to Sun", 149.6e6)], "156 million km.", "Past the Sun!")
s5 = recap("$1 bills, end to end:", [("$1 MILLION", "156 km", Y1), ("$1 BILLION", "4x around Earth", Y2), ("$1 TRILLION", "past the Sun", Y3)], size=60)

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("A monkey typing BANANA"), 5.0)],
      [(0, 4.5, 0.15, "One billion dollar bills, end to end. How far?"),
       (4.5, 11, 0.5, "A dollar bill is fifteen and a half centimeters long. One million of them: one hundred fifty six kilometers."),
       (15.5, 12, 0.5, "One billion bills: one hundred fifty six thousand kilometers. Almost four times around the Earth."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "And one trillion? One hundred fifty six million kilometers. Past the Moon, and even further than the Sun."),
       (46, 9.5, 0.4, "A trillion dollar bills would reach the Sun. With room to spare."),
       (55.5, 5, 0.4, "Next: a monkey, a keyboard, and the word banana.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A billion dollar bills, end to end."),
       (3, 5, 0.2, "A million: one hundred fifty six kilometers."),
       (8, 6, 0.2, "A billion: four times around Earth."),
       (14, 6, 0.2, "A trillion: past the Sun."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep22", "chartsnack_ep22_bills.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
