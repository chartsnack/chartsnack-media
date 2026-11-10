import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def tri(d, cx, cy, s, a, col=Y1):
    d.polygon([(cx - s, cy + s * 0.8), (cx + s, cy + s * 0.8), (cx, cy - s * 0.8)], fill=mix(col, a))

def s1(t, D):
    im, d = frame_base()
    tri(d, 330, 560, 110, 1.0)
    d.ellipse([650, 450, 870, 670], fill=(200, 200, 210))
    text(d, (540, 790), "Did Cleopatra live closer to", 62, WHITE, 1.0)
    text(d, (540, 900), "the PYRAMIDS", 92, Y1, 1.0)
    text(d, (540, 1000), "or", 60, GREY, 1.0, bold=False)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1110), "the MOON LANDING?", font=F(int(92 * p)), fill=Y3, anchor="mm")
    return im

def timeline_scene(title, col, sub, start, end, marks, gaps, reveal, reveal_sub, unit=""):
    """marks: (year, label, sublabel, color, above). gaps: (y0, y1, text, color). Years can be negative (BC)."""
    def fn(t, D):
        im, d = frame_base()
        text(d, (540, 420), title, 66, col, appear(t, 0))
        text(d, (540, 495), sub, 36, GREY, appear(t, 0.1), bold=False)
        p = prog(t, D)
        a = appear(t, 0.3)
        lx0, lx1, ly = 110, 970, 900
        X = lambda yr: lx0 + (lx1 - lx0) * (yr - start) / (end - start)
        d.rounded_rectangle([lx0, ly - 6, lx1, ly + 6], radius=6, fill=mix(TRACK, a))
        fx = lx0 + (lx1 - lx0) * p
        d.rounded_rectangle([lx0, ly - 6, max(lx0 + 12, fx), ly + 6], radius=6, fill=mix(col, a))
        for (yr, lab, sl, c, above) in marks:
            x = X(yr)
            ma = a * (1.0 if fx >= x - 1 else 0.0)
            if ma <= 0: continue
            d.ellipse([x - 13, ly - 13, x + 13, ly + 13], fill=mix(c, ma))
            yy = ly - 120 if above else ly + 60
            tx = min(900, max(180, x))
            text(d, (tx, yy), lab, 34, c, ma)
            text(d, (tx, yy + 40), sl, 28, GREY, ma, bold=False)
        y = 1150
        for i, (g0, g1, txt, c) in enumerate(gaps):
            ga = appear(t, 0.5 + (D - 4) * (i + 1) / (len(gaps) + 1))
            x0, x1 = X(g0), X(g1)
            d.line([(x0, y), (x1, y)], fill=mix(c, ga), width=8)
            d.line([(x0, y - 18), (x0, y + 18)], fill=mix(c, ga), width=6)
            d.line([(x1, y - 18), (x1, y + 18)], fill=mix(c, ga), width=6)
            text(d, ((x0 + x1) / 2, y + 50), txt, 38, c, ga)
            y += 150
        text(d, (540, 1600), reveal, 60, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = timeline_scene("PYRAMIDS, CLEOPATRA, MOON", Y1, "years, 2560 BC to 1969", -2560, 1969,
                    [(-2560, "Great Pyramid", "~2560 BC", WHITE, True), (-30, "Cleopatra", "69–30 BC", Y1, True), (1969, "Moon", "1969", Y3, False)],
                    [(-2560, -69, "~2,500 years", WHITE), (-30, 1969, "~2,000 years", Y3)],
                    "Closer to the Moon landing.", "By about 500 years.")
s3 = timeline_scene("OXFORD vs THE AZTECS", Y2, "years, 1000 to 1600", 1000, 1600,
                    [(1096, "Oxford", "teaching by 1096", Y2, True), (1325, "Aztec capital", "founded 1325", WHITE, False)],
                    [(1096, 1325, "~230 years", Y2)],
                    "Oxford is older.", "Than the Aztec capital Tenochtitlan.")
s4 = timeline_scene("DINOSAURS", Y3, "millions of years ago", -155, 0,
                    [(-150, "Stegosaurus", "~150 M yrs ago", WHITE, True), (-66, "T. rex", "~66 M yrs ago", Y3, True), (0, "You", "today", Y1, False)],
                    [(-150, -66, "~80+ M years", WHITE), (-66, 0, "66 M years", Y3)],
                    "T. rex is closer to YOU.", "Than to Stegosaurus.")
s5 = recap("Closer in time:", [("CLEOPATRA", "nearer the Moon", Y1), ("OXFORD", "older than Aztecs", Y2), ("T. REX", "nearer to you", Y3)], size=60)

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("Another big number"), 5.0)],
      [(0, 4.5, 0.15, "Did Cleopatra live closer to the pyramids, or to the Moon landing?"),
       (4.5, 12, 0.5, "The Great Pyramid was built around twenty five sixty BC. Cleopatra came about twenty five hundred years later. The Moon landing, about two thousand years after her."),
       (16.5, 13, 0.5, "Another one. Oxford University was already teaching around ten ninety six. The Aztec capital was founded in thirteen twenty five."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "And Stegosaurus lived around a hundred fifty million years ago. T. rex, sixty six. So T. rex lived closer to you than to Stegosaurus."),
       (46, 9, 0.4, "History is way longer than it feels. Cleopatra is closer to us than to the pyramids."),
       (55, 5, 0.4, "Follow for another big number.")],
      [(5.0, 13.8), (17.0, 26.8), (32.5, 43.6)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 48.1, 49.3, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Cleopatra: closer to the pyramids or the Moon?"),
       (3, 5, 0.2, "The Moon landing. By five centuries."),
       (8, 6, 0.2, "Oxford is older than the Aztec capital."),
       (14, 6, 0.2, "T. rex is closer to you than to Stegosaurus."),
       (20, 5, 0.2, "Follow for more.")],
      [],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep19", "chartsnack_ep19_history.mp4", YT, TT, [0.0, 11.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
