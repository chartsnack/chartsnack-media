import sys; sys.path.insert(0, "/home/claude/chartsnack")
from lib import *

PER_YEAR = 15 * 40 * 52  # $31,200

def s1(t, D):
    im, d = frame_base()
    text(d, (540, 600), "Earn $15", 110, WHITE, 1.0)
    text(d, (540, 710), "an hour.", 76, GREY, 1.0, bold=False)
    text(d, (540, 900), "How long to make", 76, WHITE, 1.0)
    pulse = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1040), "$1 BILLION?", font=F(int(140 * pulse)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "$1 MILLION", 76, Y1, appear(t, 0))
    text(d, (540, 495), "$15/h · full-time · spend nothing", 36, GREY, appear(t, 0.1), bold=False)
    p = ease_io((t - 0.5) / max(1.0, D - 3.2))
    text(d, (540, 650), f"{32.05 * p:.1f} years", 120, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    text(d, (90, 850), "EARNING $1M", 38, Y1, a, anchor="lm")
    bar(d, 90, 890, 900, 960, 32.05 / 45 * p, Y1, a)
    text(d, (90, 1050), "A WHOLE CAREER (45 YEARS)", 38, GREY, a, anchor="lm")
    bar(d, 90, 1090, 900, 1160, 1.0, (110, 116, 135), a)
    text(d, (540, 1350), "32 years.", 72, Y1, appear(t, D - 2.4))
    text(d, (540, 1440), "Most of a working life.", 44, GREY, appear(t, D - 2.0), bold=False)
    return im

def s3(t, D):
    im, d = frame_base()
    text(d, (540, 420), "$1 BILLION", 76, Y2, appear(t, 0))
    p = ease_io((t - 0.5) / max(1.0, D - 3.4))
    yrs = 32051 * p
    text(d, (540, 570), f"{fmt(yrs)} years", 110, WHITE, appear(t, 0.2))
    text(d, (540, 670), "of working full-time", 40, GREY, appear(t, 0.2), bold=False)
    lx0, lx1, ly = 90, 880, 1000
    a = appear(t, 0.4)
    d.rounded_rectangle([lx0, ly - 7, lx1, ly + 7], radius=7, fill=mix(TRACK, a))
    fx = lx0 + (lx1 - lx0) * p
    if fx - lx0 > 2: d.rounded_rectangle([lx0, ly - 7, fx, ly + 7], radius=7, fill=mix(Y2, a))
    ago_now = 32051 * (1 - p)  # years before today
    def mark(ago, label, sub, above, col=WHITE):
        x = lx0 + (lx1 - lx0) * (32051 - ago) / 32051
        ma = a * (1.0 if ago_now <= ago else 0.0)
        if ma <= 0: return
        d.ellipse([x - 11, ly - 11, x + 11, ly + 11], fill=mix(col, ma))
        yy = ly - 95 if above else ly + 60
        text(d, (x, yy), label, 32, col, ma)
        text(d, (x, yy + 38), sub, 28, GREY, ma, bold=False)
    mark(32051, "START", "30,000 BC", False, Y2)
    mark(20000, "Ice Age peak", "~20,000 yrs ago", True)
    mark(4580, "Pyramids", "2560 BC", False)
    mark(0, "TODAY", "$1 billion", True, WHITE)
    text(d, (540, 1300), "Start when humans", 56, WHITE, appear(t, D - 2.6))
    text(d, (540, 1380), "were painting caves.", 56, Y2, appear(t, D - 2.2))
    return im

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "$1 TRILLION", 76, Y3, appear(t, 0))
    p = ease_io((t - 0.5) / max(1.0, D - 3.2))
    text(d, (540, 600), f"{fmt(32.05e6 * p)} years", 96, WHITE, appear(t, 0.2))
    a = appear(t, 0.4)
    text(d, (90, 820), "EARNING $1 TRILLION", 38, Y3, a, anchor="lm")
    bar(d, 90, 860, 900, 930, 32.05 / 66 * p, Y3, a)
    text(d, (90, 1020), "SINCE THE DINOSAURS DIED", 38, GREY, a, anchor="lm")
    bar(d, 90, 1060, 900, 1130, 1.0, (110, 116, 135), a)
    text(d, (900, 1170), "~66 million years", 34, GREY, a, bold=False, anchor="rm")
    text(d, (540, 1330), "Half the time since", 56, WHITE, appear(t, D - 2.4))
    text(d, (540, 1410), "the dinosaurs.", 56, Y3, appear(t, D - 2.0))
    return im

def s5(t, D):
    im, d = frame_base()
    text(d, (540, 440), "At $15 an hour:", 64, WHITE, appear(t, 0))
    y = 680
    for st, lab, val, c in [(0.4, "$1 MILLION", "32 years", Y1), (1.6, "$1 BILLION", "32,051 years", Y2), (2.8, "$1 TRILLION", "32 million years", Y3)]:
        a = appear(t, st)
        text(d, (90, y), lab, 44, c, a, anchor="lm")
        text(d, (900, y + 75), val, 72, WHITE, a, anchor="rm")
        y += 250
    if D < 6: text(d, (540, 1500), "Follow for more", 48, Y1, appear(t, 3.4))
    return im

YT = ([("s1", s1, 4.5), ("s2", s2, 11.0), ("s3", s3, 15.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("How many humans EVER lived?"), 5.0)],
      [(0, 4.5, 0.15, "Earn fifteen dollars an hour. How long until you make a billion?"),
       (4.5, 11, 0.5, "Work full-time and never spend a cent. One million takes thirty-two years. Most of a career."),
       (15.5, 15, 0.5, "One billion? Thirty-two thousand years. To finish today, you'd have started when humans were still painting caves."),
       (30.5, 2.5, 0.1, "Subscribe for more."),
       (33, 14, 0.5, "And one trillion takes thirty-two million years. Half the time since the dinosaurs died."),
       (47, 9, 0.4, "A billion isn't earned by the hour. Not even close."),
       (56, 5, 0.4, "Next: how many humans have ever lived?")],
      [(5.0, 12.8), (16.0, 27.6), (33.5, 44.3)],
      [0.2, 13.0, 28.0, 30.7, 44.6, 47.4, 48.6, 49.8, 56.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "Fifteen an hour. Your first billion?"),
       (3, 5, 0.2, "One million: thirty-two years."),
       (8, 6, 0.2, "One billion: thirty-two thousand years."),
       (14, 6, 0.2, "A trillion: thirty-two million years."),
       (20, 5, 0.2, "Follow for more.")],
      [(3.5, 4.8), (8.5, 10.6), (14.5, 16.8)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep07", "chartsnack_ep07_wage.mp4", YT, TT, [3.5, 10.5, 14.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
