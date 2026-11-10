# German TikTok cut: Lotto 6 aus 49 (new). Run: python3 de03.py de
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *
ODDS = 139838160  # C(49,6) * 10 (Superzahl)

def ticket(d, cx, cy, a, col=Y1, w=380, h=180):
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=18, fill=mix(col, a))
    for i in range(6):
        x = cx - w / 2 + 42 + i * 50
        d.ellipse([x - 20, cy - 20, x + 20, cy + 20], fill=mix(WHITE, a))
    x = cx + w / 2 - 36
    d.ellipse([x - 20, cy - 20, x + 20, cy + 20], fill=mix(Y3, a))

def s1(t, D):
    im, d = frame_base()
    ticket(d, 540, 540, 1.0)
    text(d, (540, 780), "Jede Woche Lotto.", 88, WHITE, 1.0)
    text(d, (540, 880), "6 aus 49 + Superzahl", 60, GREY, 1.0, bold=False)
    text(d, (540, 1040), "Wann knackst du", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1170), "den JACKPOT?", font=F(int(116 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "DEINE CHANCE", 70, Y1, appear(t, 0))
    text(d, (540, 495), "6 Richtige aus 49 + Superzahl", 36, GREY, appear(t, 0.1), bold=False)
    text(d, (540, 720), "1 zu", 70, GREY, appear(t, 0.2))
    text(d, (540, 850), fmt(ODDS * prog(t, D)), 120, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    for k in range(60):
        i, j = k % 12, k // 12
        c = Y3 if k == 37 else DGREY
        d.ellipse([110 + i * 75, 1020 + j * 75, 150 + i * 75, 1060 + j * 75], fill=mix(c, a * (1 if k == 37 else 0.6)))
    text(d, (540, 1600), "1 zu 140 Millionen.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "Reine Mathematik.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s3 = bars_scene("1 TIPP PRO WOCHE", Y2, "durchschnittliche Wartezeit", lambda p: f"{fmt(2.68e6 * p)} Jahre",
                [("PYRAMIDEN BIS HEUTE", "~4.500 J.", 4500 / 2.68e6, DGREY, False),
                 ("HOMO SAPIENS", "~300.000 J.", 3e5 / 2.68e6, DGREY, False),
                 ("DEINE WARTEZEIT", "2,7 Mio. J.", 1.0, Y2, True)],
                "2,7 Millionen Jahre.", "Im Durchschnitt.", big_size=96)

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "60 JAHRE LANG", 70, Y3, appear(t, 0))
    text(d, (540, 495), "jede Woche 1 Tipp = 3.120 Tipps", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 700), f"{0.0022 * p:.4f} %".replace(".", ","), 110, WHITE, appear(t, 0.2))
    text(d, (540, 800), "Chance auf den Jackpot", 40, GREY, appear(t, 0.2), bold=False)
    a = appear(t, 0.4)
    text(d, (90, 950), "DEINE CHANCE", 38, Y3, a, anchor="lm")
    bar(d, 90, 990, 900, 1060, 0.0, Y3, a, minw=6)
    text(d, (90, 1150), "KEIN JACKPOT", 38, GREY, a, anchor="lm")
    bar(d, 90, 1190, 900, 1260, p, DGREY, a)
    text(d, (540, 1600), "Etwa 1 zu 45.000.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "Für ein ganzes Lotto-Leben.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("Lotto-Mathe:", [("CHANCE", "1 zu 140 Mio.", Y1), ("1 TIPP/WOCHE", "2,7 Mio. Jahre", Y2), ("60 JAHRE", "~0,002 %", Y3)], size=64)

DECUT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
         [(0, 3, 0.05, "Wann knackst du den Jackpot?"),
          (3, 5, 0.2, "Chance: eins zu hundertvierzig Millionen."),
          (8, 6, 0.2, "Wartezeit: zwei Komma sieben Millionen Jahre."),
          (14, 6, 0.2, "Sechzig Jahre Lotto? Fast keine Chance."),
          (20, 5, 0.2, "Folge für mehr.")],
         [(3.5, 7.0), (8.5, 12.0)],
         [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/de03", "chartsnack_de03_lotto.mp4", None, None, None, None, DECUT, [0.0, 4.8, 5.8, 5.8, 4.8])
