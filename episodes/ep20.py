import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

YR = 365.25 * 86400
ERAS = [("Moon landing", 1969, 2026 - 1969), ("Columbus", 1492, 2026 - 1492), ("Year 1", 1, 2026), ("Pyramids", -2560, 2026 + 2560)]
MAXY = ERAS[-1][2]

def money(v):
    if v >= 99.95e9: return f"${v / 1e9:.0f} billion"
    if v >= 1e9: return f"${v / 1e9:.1f} billion"
    return "$" + fmt(v)

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 560), "Earn $1", 110, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 700), "EVERY SECOND", font=F(int(112 * p)), fill=Y3, anchor="mm")
    text(d, (540, 830), "since the pyramids were built.", 52, GREY, 1.0, bold=False)
    text(d, (540, 1040), "Are you a", 80, WHITE, 1.0)
    text(d, (540, 1150), "BILLIONAIRE?", 104, Y1, 1.0)
    return im

def era_scene(i, col, reveal, reveal_sub):
    name, yr, years = ERAS[i]
    since = f"{yr} AD" if yr > 0 else f"~{-yr} BC"
    bars = []
    for j, (n2, y2, ys2) in enumerate(ERAS[: i + 1]):
        if i == 3 and j == 2: continue
        bars.append((f"Since {n2}", f"{fmt(ys2)} yrs", ys2 / MAXY, col if j == i else DGREY, j == i))
    return bars_scene(f"SINCE {name.upper()}", col, since, lambda p: money(years * YR * p), bars,
                      reveal, reveal_sub, big_size=92)

s2 = era_scene(0, Y1, "$1.8 BILLION.", "Already a billionaire.")
s3 = era_scene(1, Y2, "$16.9 BILLION.", "534 years of seconds.")
s4 = era_scene(3, Y3, "$145 BILLION.", "Since Year 1: only $64 billion.")
s5 = recap("$1 every second, since…", [("MOON LANDING", "$1.8 billion", Y1), ("COLUMBUS", "$16.9 billion", Y2), ("THE PYRAMIDS", "$145 billion", Y3)], size=64)

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 12.0), ("sx", sub_scene(), 2.5), ("s4", s4, 16.0), ("s5", s5, 9.5),
       ("s6", outro_next("23 people, same birthday?"), 5.0)],
      [(0, 4.5, 0.15, "One dollar every second, since the pyramids. Are you a billionaire?"),
       (4.5, 11, 0.5, "Start small. One dollar a second since the Moon landing, fifty seven years ago. That's already one point eight billion dollars."),
       (15.5, 12, 0.5, "Since Columbus sailed in fourteen ninety two? Almost seventeen billion. Every single second adds up."),
       (27.5, 2.5, 0.1, "Subscribe for more."),
       (30, 16, 0.5, "Since the Great Pyramid, about forty six centuries ago: around one hundred forty five billion dollars. Rich. But still not the richest person alive today."),
       (46, 9.5, 0.4, "One dollar a second, for four and a half thousand years. Wild, right?"),
       (55.5, 5, 0.4, "Next: twenty three people, and one birthday.")],
      [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
      [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "One dollar a second, since the pyramids."),
       (3, 5, 0.2, "Since the Moon landing: a billionaire."),
       (8, 6, 0.2, "Since Columbus: seventeen billion."),
       (14, 6, 0.2, "Since the pyramids: one hundred forty five billion."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep20", "chartsnack_ep20_pyramids.mp4", YT, TT, [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
