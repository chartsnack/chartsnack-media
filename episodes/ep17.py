import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

GREEN = (90, 200, 120)

def coin(d, cx, cy, r, a, col=Y1):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(col, a))
    d.ellipse([cx - r * 0.72, cy - r * 0.72, cx + r * 0.72, cy + r * 0.72], outline=mix(Y2, a), width=max(2, int(r / 10)))

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 560), "Split", 80, GREY, 1.0, bold=False)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 690), "$1 BILLION", font=F(int(140 * p)), fill=Y1, anchor="mm")
    text(d, (540, 830), "between all 8.2 billion", 70, WHITE, 1.0)
    text(d, (540, 920), "people on Earth.", 70, WHITE, 1.0)
    text(d, (540, 1110), "How much", 90, WHITE, 1.0)
    text(d, (540, 1230), "do you get?", 110, Y3, 1.0)
    return im

def share_scene(title, col, total_txt, each, reveal, reveal_sub, coin_r):
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 420), title, 70, col, appear(t, 0))
        text(d, (540, 495), total_txt, 36, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        v = each * p
        s = f"${v:,.2f}" if each < 10 else f"${v:,.0f}"
        text(d, (540, 680), s, 150, WHITE, appear(t, 0.2))
        text(d, (540, 800), "per person", 44, GREY, appear(t, 0.2), bold=False)
        a = appear(t, 0.4)
        coin(d, 540, 1150, coin_r * (0.3 + 0.7 * p), a)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = share_scene("$1 BILLION", Y1, "÷ 8.2 billion people", 0.122, "12 cents each.", "Not even a candy bar.", 60)
s3 = share_scene("$1 TRILLION", Y2, "÷ 8.2 billion people", 122, "$122 each.", "A thousand times more – still just a nice dinner.", 180)

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "MAKE EVERYONE A", 64, Y3, appear(t, 0))
    text(d, (540, 500), "MILLIONAIRE?", 80, Y3, appear(t, 0.1))
    p = prog(t, D)
    text(d, (540, 660), f"${8.2 * p:.1f} quadrillion", 92, WHITE, appear(t, 0.2))
    text(d, (540, 760), "= 8,200 × one trillion dollars", 40, GREY, appear(t, 0.2), bold=False)
    a = appear(t, 0.4)
    n = int(400 * p)
    for k in range(400):
        i, j = k % 20, k // 20
        x, y = 140 + i * 40, 860 + j * 32
        d.rectangle([x, y, x + 30, y + 22], fill=mix(Y3 if k < n else TRACK, a))
    text(d, (540, 1540), "each block ≈ 20 trillion dollars", 32, GREY, a, bold=False)
    text(d, (540, 1620), "8.2 QUADRILLION.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1700), "A 16-digit number.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("Split with everyone:", [("$1 BILLION", "12 cents", Y1), ("$1 TRILLION", "$122", Y2), ("$1M EACH NEEDS", "$8.2 quadrillion", Y3)], size=64)

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("A rumor that doubles"), 5.0)],
      [(0, 4.5, 0.15, "Split one billion dollars between everyone on Earth. How much do you get?"),
       (4.5, 12, 0.5, "One billion divided by eight point two billion people. That's about twelve cents each. Not even a candy bar."),
       (16.5, 13, 0.5, "Okay, one trillion dollars then. A thousand times more. That's about a hundred twenty two dollars each."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "And to make every single person a millionaire? You'd need eight point two quadrillion dollars. Eight thousand two hundred trillions."),
       (46, 9, 0.4, "A billion sounds huge, until you split it eight billion ways."),
       (55, 5, 0.4, "Next: how fast a rumor reaches everyone.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "A billion dollars for everyone?"),
       (3, 5, 0.2, "Twelve cents each."),
       (8, 6, 0.2, "A trillion? A hundred twenty two dollars."),
       (14, 6, 0.2, "Everyone a millionaire? Eight point two quadrillion."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 7.0), (8.5, 12.0), (14.5, 18.0)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep17", "chartsnack_ep17_split.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
