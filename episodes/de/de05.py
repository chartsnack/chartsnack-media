# German TikTok cut: Geheimnis verdoppelt sich (based on ep18). Run: python3 de05.py de
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
    text(d, (540, 740), "Erzähl 1 Person ein Geheimnis.", 64, WHITE, 1.0)
    text(d, (540, 830), "Alle 10 Minuten erzählt es jeder,", 46, GREY, 1.0, bold=False)
    text(d, (540, 890), "der es kennt, 1 neuen Person.", 46, GREY, 1.0, bold=False)
    text(d, (540, 1050), "Wann weiß es", 84, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1180), "die ganze WELT?", font=F(int(108 * p)), fill=Y3, anchor="mm")
    return im

def spread_scene(r0, r1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        r = int(round(r0 + (r1 - r0) * prog(t, D)))
        n = min(2 ** r, int(WORLD)); mins = r * 10
        text(d, (540, 420), f"NACH {mins // 60} STD. {mins % 60:02d} MIN.", 66, col, appear(t, 0))
        text(d, (540, 600), fmt(n), 120, WHITE, appear(t, 0.1))
        text(d, (540, 700), "Menschen wissen es", 44, GREY, appear(t, 0.1), bold=False)
        a = appear(t, 0.3)
        text(d, (90, 860), "ANTEIL DER WELT", 38, col, a, anchor="lm")
        frac = min(1.0, n / WORLD)
        bar(d, 90, 900, 900, 980, frac, col, a, minw=6)
        s = (f"{100 * frac:.4f} %" if frac < 0.01 else f"{100 * frac:.0f} %").replace(".", ",")
        text(d, (900, 1020), s, 34, GREY, a, bold=False, anchor="rm")
        for i in range(6):
            sz = 12 + i * 12; x = 150 + i * 150
            d.ellipse([x - sz, 1250 - sz, x + sz, 1250 + sz], fill=mix(col if i == 5 else DGREY, a))
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = spread_scene(0, 12, Y1, "2 Std.: 4.096 Menschen.", "Ein Dorf. Praktisch 0 % der Welt.")
s3 = spread_scene(12, 24, Y2, "4 Std.: 16,8 Millionen.", "Riesig – aber nur 0,2 %.")
s4 = spread_scene(24, 33, Y3, "5,5 Std.: ALLE.", "Alle 8,2 Milliarden Menschen.")
s5 = recap("Ein Geheimnis verdoppelt sich:", [("NACH 2 STD.", "4.096", Y1), ("NACH 4 STD.", "16,8 Mio.", Y2), ("NACH 5,5 STD.", "die ganze Welt", Y3)], size=64)

DECUT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
         [(0, 3, 0.05, "Ein Geheimnis verdoppelt sich alle zehn Minuten."),
          (3, 5, 0.2, "Nach zwei Stunden: viertausend Menschen."),
          (8, 6, 0.2, "Nach vier Stunden: siebzehn Millionen."),
          (14, 6, 0.2, "Nach fünfeinhalb Stunden: die ganze Welt."),
          (20, 5, 0.2, "Folge für mehr.")],
         [(3.5, 7.0), (8.5, 12.0), (14.5, 18.0)],
         [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/de05", "chartsnack_de05_geheimnis.mp4", None, None, None, None, DECUT, [0.0, 4.8, 5.8, 5.8, 4.8])
