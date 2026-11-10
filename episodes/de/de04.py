# German TikTok cut: Reis auf dem Schachbrett (based on ep15). Run: python3 de04.py de
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *
LIGHT, DARK = (70, 74, 92), (42, 46, 61)

def board(d, x0, y0, size, upto, a, hl=None):
    c = size / 8
    for k in range(64):
        r, f = k // 8, k % 8
        x, y = x0 + f * c, y0 + (7 - r) * c
        col = Y1 if k < upto else (LIGHT if (r + f) % 2 == 0 else DARK)
        if hl is not None and k == hl: col = Y3
        d.rectangle([x, y, x + c, y + c], fill=mix(col, a))

def s1(t, D):
    im, d = frame_base()
    board(d, 340, 330, 400, 1, 1.0)
    text(d, (540, 850), "1 Reiskorn.", 90, WHITE, 1.0)
    text(d, (540, 950), "Auf jedem Feld verdoppelt.", 58, GREY, 1.0, bold=False)
    text(d, (540, 1100), "Wie viel liegt auf", 76, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1230), "FELD 64?", font=F(int(130 * p)), fill=Y3, anchor="mm")
    return im

def sq_scene(k0, k1, col, reveal, reveal_sub):
    def fn(t, D):
        im, d = frame_base()
        k = int(round(k0 + (k1 - k0) * prog(t, D)))
        text(d, (540, 420), f"FELD {k}", 76, col, appear(t, 0))
        s = fmt(2 ** (k - 1))
        text(d, (540, 560), s, 100 if len(s) < 12 else (78 if len(s) < 20 else 60), WHITE, appear(t, 0.1))
        text(d, (540, 650), "Körner", 40, GREY, appear(t, 0.1), bold=False)
        board(d, 220, 760, 640, k, appear(t, 0.3), hl=k - 1)
        text(d, (540, 1600), reveal, 64, col, appear(t, D - 2.4))
        text(d, (540, 1690), reveal_sub, 40, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

s2 = sq_scene(1, 32, Y1, "Feld 32: 2,1 Milliarden.", "Allein dieses Feld: ~54 Tonnen.")
s3 = sq_scene(32, 64, Y2, "Feld 64: 9,2 Trillionen.", "Ein einziges Feld.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "DAS GANZE BRETT", 70, Y3, appear(t, 0))
    text(d, (540, 495), "18,4 Trillionen Körner à ~25 mg", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    text(d, (540, 680), f"{fmt(460 * p)} Mrd. Tonnen", 80, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    for i in range(60):
        x, y = 140 + (i % 10) * 82, 820 + (i // 10) * 82
        d.rounded_rectangle([x, y, x + 64, y + 64], radius=10, fill=mix(Y3 if i < 60 * p else TRACK, a))
    text(d, (540, 1350), "1 Kästchen = 10 Jahre Welt-Reisernte", 34, GREY, a, bold=False)
    text(d, (540, 1600), "600+ Jahre Ernte.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "Alle Reisfelder der Welt.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = recap("Verdoppelter Reis:", [("FELD 32", "2,1 Mrd.", Y1), ("FELD 64", "9,2 Trillionen", Y2), ("GANZES BRETT", "600+ J. Ernte", Y3)], size=64)

DECUT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
         [(0, 3, 0.05, "Ein Reiskorn, vierundsechzigmal verdoppelt."),
          (3, 5, 0.2, "Feld zweiunddreißig: zwei Milliarden."),
          (8, 6, 0.2, "Feld vierundsechzig: neun Trillionen."),
          (14, 6, 0.2, "Über sechshundert Jahre Welt-Reisernte."),
          (20, 5, 0.2, "Folge für mehr.")],
         [(3.5, 7.0), (8.5, 12.0)],
         [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/de04", "chartsnack_de04_reis.mp4", None, None, None, None, DECUT, [0.0, 4.8, 5.8, 5.8, 4.8])
