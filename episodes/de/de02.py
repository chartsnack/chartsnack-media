# German TikTok cut: Kartenmischen 52! (based on ep09). Run: python3 de02.py de
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *
FACT = "80658175170943878571660636856403766975289505440883277824000000000000"

def card(d, x, y, a, col=WHITE, w=110, h=154):
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], radius=12, fill=mix(col, a))
    d.rounded_rectangle([x - w / 2 + 8, y - h / 2 + 8, x + w / 2 - 8, y + h / 2 - 8], radius=8, outline=mix(Y3, a), width=4)

def s1(t, D):
    im, d = frame_base()
    for i in range(5): card(d, 540 + (i - 2) * 70, 520 + abs(i - 2) * 14, 1.0)
    text(d, (540, 800), "Mische ein Kartenspiel.", 76, WHITE, 1.0)
    text(d, (540, 940), "Wie viele Reihenfolgen", 72, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1080), "gibt es?", font=F(int(120 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "52 × 51 × 50 × 49 × …", 64, Y1, appear(t, 0))
    text(d, (540, 495), "Möglichkeiten für Karte 1, 2, 3 …", 36, GREY, appear(t, 0.1), bold=False)
    n = max(1, int(round(68 * prog(t, D))))
    for i, r in enumerate(wrap_digits(FACT[:n], 14)): text(d, (540, 640 + i * 95), r, 76, WHITE, appear(t, 0.2))
    text(d, (540, 1190), f"{n} Stellen", 60, Y1, appear(t, 0.4))
    text(d, (540, 1600), "Eine 68-stellige Zahl.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "52 Fakultät: 52!", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s3 = bars_scene("WIE GROSS IST DAS?", Y2, "Anzahl der Stellen", None,
                [("SEKUNDEN SEIT URKNALL", "18 Stellen", 18 / 68, DGREY, False),
                 ("ATOME IN DEINEM KÖRPER", "28 Stellen", 28 / 68, DGREY, False),
                 ("ATOME DER ERDE", "51 Stellen", 51 / 68, DGREY, False),
                 ("KARTEN-REIHENFOLGEN", "68 Stellen", 1.0, Y2, True)],
                "Mehr als Atome der Erde.", "Viel, viel mehr.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "ALLE MENSCHEN", 66, Y3, appear(t, 0))
    text(d, (540, 495), "mischen seit dem Urknall jede Sekunde", 34, GREY, appear(t, 0.1), bold=False)
    a = appear(t, 0.4)
    for k in range(40):
        i, j = k % 8, k // 8
        card(d, 160 + i * 108, 640 + j * 120, appear(t, 0.4 + k * 0.06, 0.2) * 0.9, WHITE, w=70, h=98)
    text(d, (90, 1290), "SCHON GESEHEN", 38, Y3, a, anchor="lm")
    bar(d, 90, 1330, 900, 1400, 0.0, Y3, a, minw=8)
    text(d, (900, 1440), "0,0000000000000000…%", 34, GREY, a, bold=False, anchor="rm")
    text(d, (540, 1600), "Praktisch null.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "38 Nullen nach dem Komma.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = statement([(560, "Deine nächste Mischung", 64, WHITE, True, 0.0),
                (660, "ist fast sicher", 64, WHITE, True, 0.3),
                (840, "EINMALIG", 150, Y3, True, 0.8),
                (1000, "in der Geschichte des Universums.", 46, GREY, False, 1.2)])

DECUT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
         [(0, 3, 0.05, "Wie oft kann man Karten mischen?"),
          (3, 5, 0.2, "Eine achtundsechzigstellige Zahl."),
          (8, 6, 0.2, "Mehr als alle Atome der Erde."),
          (14, 6, 0.2, "Seit dem Urknall gemischt? Fast nichts."),
          (20, 5, 0.2, "Deine Mischung ist einmalig.")],
         [(3.5, 4.8)],
         [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/de02", "chartsnack_de02_karten.mp4", None, None, None, None, DECUT, [0.0, 4.8, 5.8, 5.8, 4.8])
