import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

WORLD = 8.2e9

def bubble(d, cx, cy, a):
    d.rounded_rectangle([cx - 120, cy - 70, cx + 120, cy + 50], radius=36, fill=mix(WHITE, a))
    d.polygon([(cx - 40, cy + 48), (cx - 80, cy + 100), (cx - 5, cy + 48)], fill=mix(WHITE, a))
    for i in range(3):
        x = cx - 50 + i * 50
        d.ellipse([x - 13, cy - 23, x + 13, cy + 3], fill=mix(BG, a))

def s1(t, D):
    im, d = frame_base()
    bubble(d, 540, 520, 1.0)
    text(d, (540, 740), "Tell 1 person a secret.", 76, WHITE, 1.0)
    text(d, (540, 830), "Every 10 min, everyone who knows", 46, GREY, 1.0, bold=False)
    text(d, (540, 890), "tells 1 new person.", 46, GREY, 1.0, bold=False)
    text(d, (540, 1050), "When does the", 84, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1180), "WORLD know?", font=F(int(116 * p)), fill=Y3, anchor="mm")
    return im

def spread_scene(r0, r1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        r = int(round(r0 + (r1 - r0) * p))
        n = min(2 ** r, int(WORLD))
        mins = r * 10
        text(d, (540, 420), f"AFTER {mins // 60} h {mins % 60:02d} min", 70, col, appear(t, 0))
        text(d, (540, 600), fmt(n), 120, WHITE, appear(t, 0.1))
        text(d, (540, 700), "people know", 44, GREY, appear(t, 0.1), bold=False)
        a = appear(t, 0.3)
        text(d, (90, 860), "SHARE OF THE WORLD", 38, col, a, anchor="lm")
        frac = min(1.0, n / WORLD)
        bar(d, 90, 900, 900, 980, frac, col, a, minw=6)
        text(d, (900, 1020), f"{100 * frac:.4f} %" if frac < 0.01 else f"{100 * frac:.0f} %", 34, GREY, a, bold=False, anchor="rm")
        # doubling dots: last 6 rounds as growing circles
        for i in range(6):
            rr = max(0, r - 5 + i)
            on = rr >= 0
            s = 12 + i * 12
            x = 150 + i * 150
            d.ellipse([x - s, 1250 - s, x + s, 1250 + s], fill=mix(col if i == 5 else DGREY, a))
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = spread_scene(0, 12, Y1, "2 hours: 4,096 people.", "A small town. Basically 0 % of the world.")
s3 = spread_scene(12, 24, Y2, "4 hours: 16.8 million.", "A huge city – but only 0.2 %.")
s4 = spread_scene(24, 33, Y3, "5.5 hours: EVERYONE.", "All 8.2 billion people.")
s5 = recap("A doubling secret:", [("AFTER 2 HOURS", "4,096", Y1), ("AFTER 4 HOURS", "16.8 million", Y2), ("AFTER 5.5 HOURS", "the whole world", Y3)], size=64)

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("Cleopatra vs the Moon landing"), 5.0)],
      [(0, 4.5, 0.15, "A secret that doubles every ten minutes. When does the whole world know?"),
       (4.5, 12, 0.5, "Every ten minutes, everyone who knows tells one new person. After two hours, four thousand ninety six people. A small town."),
       (16.5, 13, 0.5, "After four hours, almost seventeen million. And yet that's still only about zero point two percent of the world."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "But just ninety minutes later, at five and a half hours, the doubling covers all eight point two billion people."),
       (46, 9, 0.4, "Thirty three doublings. That's all it takes to reach everyone."),
       (55, 5, 0.4, "Next: Cleopatra, the pyramids, and the Moon.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A secret doubles every ten minutes."),
       (3, 5, 0.2, "Two hours: four thousand people."),
       (8, 6, 0.2, "Four hours: seventeen million."),
       (14, 6, 0.2, "Five and a half hours: the whole world."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0), (14.5, 18.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep18", "chartsnack_ep18_rumor.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
