# German TikTok cut: Cent verdoppeln (based on ep10). Run: python3 de01.py de
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def val(day): return 0.01 * 2 ** (day - 1)
def euro(v):
    if v < 10: return f"{v:.2f} €".replace(".", ",")
    return f"{fmt(v)} €"

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 640), "1 MILLION €", 120, Y1, 1.0)
    text(d, (540, 760), "sofort…", 70, WHITE, 1.0)
    text(d, (540, 900), "ODER", 80, GREY, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1060), "1 CENT", font=F(int(130 * p)), fill=Y3, anchor="mm")
    text(d, (540, 1180), "30 Tage lang täglich verdoppelt?", 50, WHITE, 1.0)
    return im

def day_scene(d0, d1, top, col, reveal, reveal_sub, line=None):
    def fn(t, D):
        im, d = frame_base()
        p = prog(t, D)
        cur = int(round(d0 + (d1 - d0) * p))
        text(d, (540, 420), f"TAG {cur}", 80, col, appear(t, 0))
        text(d, (540, 560), euro(val(cur)), 110, WHITE, appear(t, 0.1))
        a = appear(t, 0.3)
        x0, x1, yb, yt = 90, 990, 1450, 760
        bw = (x1 - x0) / 30
        d.line([(x0, yb), (x1, yb)], fill=mix(GREY, a), width=3)
        if line:
            ly = yb - (yb - yt) * min(1.0, line[0] / top)
            for x in range(x0, x1, 28): d.line([(x, ly), (x + 14, ly)], fill=mix(WHITE, a * 0.8), width=3)
            text(d, (x0, ly - 30), line[1], 34, WHITE, a, anchor="lm")
        for k in range(1, cur + 1):
            h = max(3, (yb - yt) * min(1.0, val(k) / top))
            d.rectangle([x0 + (k - 1) * bw + 3, yb - h, x0 + k * bw - 3, yb], fill=mix(col if k == cur else DGREY, a))
        text(d, (x0, yb + 40), "Tag 1", 30, GREY, a, bold=False, anchor="lm")
        text(d, (x1, yb + 40), "Tag 30", 30, GREY, a, bold=False, anchor="rm")
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = day_scene(1, 20, val(20), Y1, "Tag 20: 5.243 €.", "Sieht nach einem miesen Deal aus.")
s3 = day_scene(20, 28, 1.5e6, Y2, "Tag 28: 1,34 Millionen.", "Die Million ist geknackt.", line=(1e6, "1 MILLION €"))
s4 = day_scene(28, 30, val(30), Y3, "Tag 30: 5.368.709 €.", "Über 5-mal die Million.", line=(1e6, "1 MILLION €"))
s5 = recap("Dein verdoppelter Cent:", [("TAG 10", "5,12 €", Y1), ("TAG 20", "5.243 €", Y2), ("TAG 30", "5,37 Mio. €", Y3)])

DECUT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
         [(0, 3, 0.05, "Eine Million oder ein Cent, der sich verdoppelt?"),
          (3, 5, 0.2, "Tag zwanzig: nur fünftausend Euro."),
          (8, 6, 0.2, "Tag achtundzwanzig: über eine Million."),
          (14, 6, 0.2, "Tag dreißig: fünf Komma vier Millionen."),
          (20, 5, 0.2, "Folge für mehr.")],
         [(3.5, 7.0), (8.5, 12.0), (14.5, 18.0)],
         [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/de01", "chartsnack_de01_cent.mp4", None, None, None, None, DECUT, [0.0, 4.8, 5.8, 5.8, 4.8])
