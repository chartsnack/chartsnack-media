# German TikTok cut: Jahre im Schlaf (based on ep16). Run: python3 de06.py de
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *
NIGHT = (110, 120, 255)

def moon(d, cx, cy, r, a):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(Y1, a))
    d.ellipse([cx - r + r * 0.55, cy - r - r * 0.2, cx + r + r * 0.55, cy + r - r * 0.2], fill=BG)

def s1(t, D):
    im, d = frame_base()
    moon(d, 540, 540, 110, 1.0)
    text(d, (540, 780), "Du schläfst 8 Stunden", 84, WHITE, 1.0)
    text(d, (540, 880), "jede Nacht.", 70, GREY, 1.0, bold=False)
    text(d, (540, 1040), "Wie viele JAHRE", 88, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1170), "sind das?", font=F(int(130 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "EIN TAG", 70, Y1, appear(t, 0))
    text(d, (540, 495), "24 Stunden", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D); a = appear(t, 0.3)
    cx, cy, r = 540, 1060, 280
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mix(TRACK, a))
    if p > 0.01: d.pieslice([cx - r, cy - r, cx + r, cy + r], -90, -90 + 120 * p, fill=mix(NIGHT, a))
    text(d, (540, 660), f"{8 * p:.1f}".replace(".", ",") + " Std. Schlaf", 70, WHITE, appear(t, 0.2))
    text(d, (540, 1600), "Ein Drittel jedes Tages.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "Jede einzelne Nacht.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

def s3(t, D):
    im, d = frame_base()
    text(d, (540, 420), "80 JAHRE LEBEN", 70, Y2, appear(t, 0))
    text(d, (540, 495), "1 Kästchen = 1 Jahr", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 640), f"{26.7 * p:.1f}".replace(".", ",") + " Jahre Schlaf", 84, WHITE, appear(t, 0.2))
    a = appear(t, 0.3)
    for k in range(80):
        x, y = 150 + (k % 10) * 80, 760 + (k // 10) * 80
        d.rounded_rectangle([x, y, x + 64, y + 64], radius=10, fill=mix(NIGHT if k < 26.7 * p else TRACK, a))
    text(d, (540, 1600), "26,7 Jahre. Im Schlaf.", 64, Y2, appear(t, D - 2.4))
    text(d, (540, 1690), "Jedes dritte Jahr deines Lebens.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s4 = bars_scene("ZU DEINEM GEBURTSTAG", Y3, "geschlafene Jahre bei 8 Std. pro Nacht", None,
                [("MIT 18", "6 Jahre", 6 / 26.7, NIGHT, True),
                 ("MIT 30", "10 Jahre", 10 / 26.7, NIGHT, True),
                 ("MIT 50", "16,7 Jahre", 16.7 / 26.7, NIGHT, True),
                 ("MIT 80", "26,7 Jahre", 1.0, Y3, True)],
                "Über 230.000 Stunden.", "Etwa 9.740 ganze Tage.")
s5 = recap("8 Std. Schlaf pro Nacht:", [("PRO JAHR", "~122 Tage", Y1), ("BIS 30", "10 Jahre", Y2), ("80 JAHRE", "26,7 Jahre", Y3)])

DECUT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
         [(0, 3, 0.05, "Wie viele Jahre verschläfst du?"),
          (3, 5, 0.2, "Ein Drittel jedes Tages."),
          (8, 6, 0.2, "In achtzig Jahren: fast siebenundzwanzig."),
          (14, 6, 0.2, "Mit dreißig hast du zehn Jahre geschlafen."),
          (20, 5, 0.2, "Folge für mehr.")],
         [(3.5, 7.0), (8.5, 12.0)],
         [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/de06", "chartsnack_de06_schlaf.mp4", None, None, None, None, DECUT, [0.0, 4.8, 5.8, 5.8, 4.8])
