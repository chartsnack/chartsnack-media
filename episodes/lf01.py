"""Long-form #1: How big is a TRILLION? 7 ways to finally feel it.  Run: python3 lf01.py [stills|build]"""
import sys, math
sys.path.insert(0, "/home/claude/chartsnack-media/tools"); sys.path.insert(0, "/home/claude/chartsnack")
from lf import *

CH = ["Intro", "Time", "Height", "Weight", "Work", "Spending", "Sharing", "Rice", "Recap"]
COLS = [Y1, Y2, Y3]
NAMES = ["MILLION", "BILLION", "TRILLION"]

# ---------- reusable visuals ----------
def three_up(title, vals, subs, active, note="", unit_fmt=None, icon=None):
    """three cards Million/Billion/Trillion; cards up to `active` are revealed, active one counts up"""
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        text(d, (W / 2, 165), title, 64, WHITE, appear(t, 0))
        p = ease_io((t - 0.4) / max(1.0, D * 0.55))
        for k in range(3):
            x = 360 + k * 600; a = appear(t, 0.2 + 0.15 * k)
            on = k <= active
            col = COLS[k] if on else DGREY
            d.rounded_rectangle([x - 260, 270, x + 260, 830], radius=36, fill=mixc((30, 34, 46), a), outline=mixc(col, a * (1 if k == active else 0.5)), width=5 if k == active else 2)
            text(d, (x, 330), "1 " + NAMES[k], 48, col, a)
            if k < active or (k == active):
                v = vals[k] if k < active else vals[k] * p
                s = unit_fmt(v) if unit_fmt else fmtn(v)
                text(d, (x, 520), s, 86 if len(s) < 11 else (70 if len(s) < 15 else 56), WHITE, a)
                if subs[k] and (k < active or t > D * 0.6):
                    text(d, (x, 640), subs[k], 36, GREY, appear(t, D * 0.6) if k == active else a, bold=False)
            else:
                text(d, (x, 520), "?", 120, DGREY, a)
            if icon: icon(d, x, 760, k, a, on)
        if note: text(d, (W / 2, 930), note, 46, COLS[active], appear(t, D - 2.2))
        return im
    return fn

def title_card(num, name, sub):
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        w = ease(t / 0.6) * W
        d.rectangle([0, 470, w, 610], fill=(30, 34, 46))
        text(d, (W / 2, 420), f"PART {num}", 40, GREY, appear(t, 0.2))
        text(d, (W / 2, 540), name, 110, Y1, appear(t, 0.35))
        text(d, (W / 2, 680), sub, 44, WHITE, appear(t, 0.6), bold=False)
        return im
    return fn

def timeline(span_years, marks, fill_years, col, label, sub=""):
    """horizontal timeline ending TODAY at the right; zooms out from 100 years to span_years (log zoom)"""
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        p = ease_io((t - 0.3) / max(1.0, D * 0.6))
        span = 10 ** (2 + (math.log10(span_years) - 2) * p)
        x0, x1, y = 120, W - 140, 600
        X = lambda ago: x1 - (x1 - x0) * ago / span
        d.rounded_rectangle([x0, y - 6, x1, y + 6], radius=6, fill=TRACK)
        fx = X(min(fill_years, span))
        d.rounded_rectangle([max(x0, fx), y - 10, x1, y + 10], radius=10, fill=col)
        # ticks
        step = 10 ** math.floor(math.log10(span / 2))
        k = 0
        while k * step <= span:
            xx = X(k * step); d.line([(xx, y + 18), (xx, y + 34)], fill=GREY, width=2)
            if k % 2 == 0: d.text((xx, y + 60), f"{fmtn(k * step)} y", font=F(24, False), fill=GREY, anchor="mm")
            k += 1
        for i, (ago, lab, up) in enumerate(marks):
            if ago > span * 1.0001: continue
            xx = X(ago); a = 1.0
            d.ellipse([xx - 10, y - 10, xx + 10, y + 10], fill=WHITE)
            yy = y - 120 - (i % 2) * 70 if up else y + 120 + (i % 2) * 60
            d.line([(xx, y - 12 if up else y + 12), (xx, yy + (30 if up else -30))], fill=DGREY, width=2)
            text(d, (min(W - 200, max(200, xx)), yy), lab, 34, WHITE, a)
        text(d, (x1, y - 50), "TODAY", 30, Y1, 1.0, anchor="rm")
        text(d, (W / 2, 220), label, 72, col, appear(t, 0))
        if sub: text(d, (W / 2, 300), sub, 40, GREY, appear(t, 0.3), bold=False)
        return im
    return fn

LANDMARKS = [(1.75, "a person"), (10, "a house"), (330, "Eiffel Tower"), (828, "Burj Khalifa"),
             (10e3, "airliners"), (100e3, "edge of space"), (408e3, "space station")]
def stack_climb(height, label, col, sub):
    """bill stack grows; log-scale camera rises with it; landmark lines pass by"""
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        p = ease_io((t - 0.3) / max(1.0, D * 0.6))
        h = max(0.01, height ** p if height > 1 else height * p)
        h = 0.05 * (height / 0.05) ** p
        top_view = h * 2.2
        L = lambda m: 980 - 820 * (math.log10(max(m, 0.01)) - math.log10(0.02)) / (math.log10(top_view) - math.log10(0.02))
        # landmarks
        for (m, lab) in LANDMARKS:
            yy = L(m)
            if 100 < yy < 990:
                passed = h >= m
                c = WHITE if passed else DGREY
                for x in range(960, 1780, 30): d.line([(x, yy), (x + 15, yy)], fill=c, width=2)
                d.text((1780, yy - 22), lab, font=F(30), fill=c, anchor="rm")
                d.text((1780, yy + 20), (f"{m:,.0f} m" if m < 1e4 else f"{m/1000:,.0f} km"), font=F(24, False), fill=GREY, anchor="rm")
        # the stack (log column)
        ytop = L(h)
        d.rectangle([760, ytop, 920, 990], fill=col)
        for yy in range(990, int(ytop), -16): d.line([(760, yy), (920, yy)], fill=tuple(int(c * 0.78) for c in col), width=2)
        d.line([(80, 990), (1840, 990)], fill=GREY, width=3)
        val = (f"{h:,.2f} m" if h < 10 else (f"{h:,.0f} m" if h < 1e4 else f"{h/1000:,.0f} km"))
        text(d, (370, 300), label, 60, col, appear(t, 0))
        text(d, (370, 400), val, 84, WHITE, appear(t, 0.2))
        text(d, (370, 480), "of $100 bills", 34, GREY, appear(t, 0.2), bold=False)
        if sub: text(d, (370, 620), sub, 40, col, appear(t, D - 2.0))
        d.text((90, 1010), "log scale", font=F(22, False), fill=GREY, anchor="lm")
        return im
    return fn

def compare_bars(title, rows, note, col, sub=""):
    """rows: (label, value_text, frac, color, animate)"""
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        text(d, (W / 2, 180), title, 64, col, appear(t, 0))
        if sub: text(d, (W / 2, 255), sub, 36, GREY, appear(t, 0.15), bold=False)
        p = ease_io((t - 0.5) / max(1.0, D * 0.5))
        y = 360
        for i, (lab, vt, frac, c, anim) in enumerate(rows):
            a = appear(t, 0.3 + 0.25 * i)
            text(d, (200, y), lab, 40, c if anim else GREY, a, anchor="lm")
            text(d, (1720, y), vt, 40, WHITE, a, anchor="rm")
            hbar(d, 200, y + 35, 1720, y + 95, frac * (p if anim else 1.0), c, a)
            y += 170
        text(d, (W / 2, 950), note, 50, col, appear(t, D - 2.2))
        return im
    return fn

def statement(lines):
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        for (y, s, size, col, st) in lines: text(d, (W / 2, y), s, size, col, appear(t, st), bold=size >= 50)
        return im
    return fn

def people_grid(per_person, label, col, sub):
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        text(d, (W / 2, 190), label, 64, col, appear(t, 0))
        text(d, (W / 2, 265), "÷ 8.2 billion people", 38, GREY, appear(t, 0.15), bold=False)
        p = ease_io((t - 0.4) / max(1.0, D * 0.5))
        for k in range(120):
            i, j = k % 20, k // 20
            x, y = 330 + i * 64, 380 + j * 70
            on = k < 120 * p
            c = col if on else DGREY
            d.ellipse([x - 9, y - 26, x + 9, y - 8], fill=c); d.rounded_rectangle([x - 14, y - 4, x + 14, y + 26], radius=8, fill=c)
        text(d, (W / 2, 880), per_person, 90, WHITE, appear(t, D * 0.55))
        text(d, (W / 2, 975), sub, 40, GREY, appear(t, D * 0.6), bold=False)
        return im
    return fn

def recap(t, D, ctx):
    im, d = background(t); chrome(d, ctx, t)
    rows = [("TIME (seconds)", "11.6 days", "31.7 years", "31,710 years"),
            ("HEIGHT ($100 bills)", "1.1 m", "1.1 km", "1,092 km"),
            ("WEIGHT ($100 bills)", "10 kg", "10 t", "10,000 t"),
            ("WORK ($15/hour)", "32 years", "32,051 yrs", "32 million yrs"),
            ("SPEND ($1,000/day)", "2.7 years", "2,738 years", "2.7 million yrs"),
            ("SHARE (8.2 bn people)", "$0.0001", "12 cents", "$122"),
            ("RICE (25 mg grains)", "25 kg", "25 t", "25,000 t")]
    text(d, (W / 2, 150), "A MILLION vs A BILLION vs A TRILLION", 52, WHITE, appear(t, 0))
    for k, (nm, c) in enumerate(zip(NAMES, COLS)): text(d, (880 + k * 360, 240), nm, 36, c, appear(t, 0.2))
    for i, r in enumerate(rows):
        a = appear(t, 0.5 + i * 0.6); y = 320 + i * 92
        d.rounded_rectangle([100, y - 38, 1820, y + 38], radius=14, fill=mixc((30, 34, 46), a))
        text(d, (130, y), r[0], 34, GREY, a, anchor="lm")
        for k in range(3): text(d, (880 + k * 360, y), r[k + 1], 40, COLS[k] if k == 2 else WHITE, a)
    return im

def outro(t, D, ctx):
    im, d = background(t)
    logo(d, W / 2 - 400 * 0.5, 250, 0.5, appear(t, 0, 0.5), grow=ease((t - 0.1) / 0.6), radius=12)
    text(d, (W / 2, 620), "CHART SNACK", 96, WHITE, appear(t, 0.6))
    text(d, (W / 2, 710), "Numbers you can finally feel.", 46, GREY, appear(t, 1.0), bold=False)
    lt = t - 1.6
    if lt > 0:
        clicked = lt > 1.0; col = (70, 74, 90) if clicked else (255, 48, 64)
        d.rounded_rectangle([W / 2 - 240, 800, W / 2 + 240, 900], radius=50, fill=col)
        d.text((W / 2, 850), "SUBSCRIBED" if clicked else "SUBSCRIBE", font=F(48), fill=WHITE, anchor="mm")
    return im

def hook(t, D, ctx):
    im, d = background(t); chrome(d, ctx, t)
    for k, (s, c) in enumerate(zip(["1,000,000", "1,000,000,000", "1,000,000,000,000"], COLS)):
        a = appear(t, 0.1 + k * 0.9)
        text(d, (W / 2, 330 + k * 190), s, 110 + k * 10, c, a)
        text(d, (W / 2, 330 + k * 190 + 75), "one " + NAMES[k].lower(), 30, GREY, a, bold=False)
    text(d, (W / 2, 950), "How big is a trillion, really?", 56, WHITE, appear(t, D - 2.5))
    return im

def zeros(t, D, ctx):
    im, d = background(t); chrome(d, ctx, t)
    text(d, (W / 2, 200), "Each step is 1,000× bigger", 64, WHITE, appear(t, 0))
    for k in range(3):
        a = appear(t, 0.5 + k * 0.8); y = 400 + k * 180
        text(d, (200, y), NAMES[k], 44, COLS[k], a, anchor="lm")
        w = [6, 9, 12][k]
        for z in range(w):
            zz = appear(t, 0.6 + k * 0.8 + z * 0.06)
            d.ellipse([520 + z * 88, y - 34, 584 + z * 88, y + 34], outline=mixc(COLS[k], zz), width=8)
        text(d, (1840, y), f"{w} zeros", 36, GREY, a, anchor="rm", bold=False)
    text(d, (W / 2, 950), "Your brain hears three similar words.", 46, Y3, appear(t, D - 2.2))
    return im

def calendar(n_days, label, col, sub):
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        text(d, (W / 2, 190), label, 64, col, appear(t, 0))
        p = ease_io((t - 0.4) / max(1.0, D * 0.55))
        for k in range(14):
            x, y = 330 + (k % 7) * 185, 330 + (k // 7) * 200
            on = k < n_days * p
            d.rounded_rectangle([x, y, x + 160, y + 170], radius=18, fill=col if on else TRACK)
            d.text((x + 80, y + 85), str(k + 1), font=F(56), fill=BG if on else GREY, anchor="mm")
        text(d, (W / 2, 820), f"{n_days * p:.1f} days", 90, WHITE, appear(t, 0.3))
        text(d, (W / 2, 940), sub, 44, GREY, appear(t, D - 2.0), bold=False)
        return im
    return fn

def lifebar(years, label, col, sub):
    def fn(t, D, ctx):
        im, d = background(t); chrome(d, ctx, t)
        text(d, (W / 2, 190), label, 64, col, appear(t, 0))
        p = ease_io((t - 0.4) / max(1.0, D * 0.55))
        for k in range(80):
            x, y = 200 + (k % 20) * 77, 330 + (k // 20) * 90
            d.rounded_rectangle([x, y, x + 64, y + 72], radius=10, fill=col if k < years * p else TRACK)
        text(d, (W / 2, 760), "each block = 1 year of an 80-year life", 32, GREY, appear(t, 0.3), bold=False)
        text(d, (W / 2, 870), f"{years * p:.1f} years", 90, WHITE, appear(t, 0.3))
        text(d, (W / 2, 975), sub, 44, col, appear(t, D - 2.0))
        return im
    return fn

def icon_weight(d, x, y, k, a, on):
    c = mixc(COLS[k] if on else DGREY, a)
    s = [30, 46, 62][k]
    d.polygon([(x - s, y + s * 0.6), (x + s, y + s * 0.6), (x + s * 0.6, y - s * 0.5), (x - s * 0.6, y - s * 0.5)], fill=c)
    d.ellipse([x - 12, y - s * 0.5 - 22, x + 12, y - s * 0.5 + 2], outline=c, width=5)

def wfmt(v):
    return f"{fmtn(v)} kg" if v < 1000 else f"{fmtn(v / 1000)} t"

# ---------- the script ----------
B = []
def add(fn, vo, md=3.0, ch=None): B.append(Beat(fn, vo, md, chapter=ch))

add(hook, "A million. A billion. A trillion. We say them like they're next door neighbors. They're not even on the same planet.", 7, ch=0)
add(zeros, "Each step is a thousand times bigger than the one before. But to your brain, they're just three words that sound almost the same. So today, let's look at a trillion in seven different ways. Time, height, weight, work, money, and even rice. By the end, you'll actually feel it.", 10)

add(title_card(1, "TIME", "Count one second at a time"), "Part one. Time. Let's count seconds.", 3.5, ch=1)
add(calendar(11.57, "1 MILLION SECONDS", Y1, "Less than two weeks."), "One million seconds is eleven and a half days. Start counting today, and you're done in less than two weeks.", 6)
add(lifebar(31.7, "1 BILLION SECONDS", Y2, "A huge part of a human life."), "One billion seconds? That's thirty one point seven years. If you started counting at birth, you'd finish somewhere in your early thirties.", 7)
add(timeline(31710, [(4586, "Pyramids", True), (20000, "Ice Age peak", False), (11700, "Ice Age ends", True), (31700, "cave paintings", False)], 31710, Y3, "1 TRILLION SECONDS", "31,710 years"),
    "And one trillion seconds is thirty one thousand, seven hundred years. To count that far, you'd have to start when humans were painting animals on cave walls, long before the Ice Age ended, and long before anyone built a pyramid.", 12)
add(statement([(380, "Million: 11 days.", 70, Y1, 0.2), (500, "Billion: 32 years.", 70, Y2, 0.8), (620, "Trillion: 31,710 years.", 70, Y3, 1.4), (800, "Same pattern, every time: × 1,000.", 44, GREY, 2.2)]),
    "Eleven days. Thirty two years. Thirty two thousand years. That's what a factor of a thousand looks like.", 6)

add(title_card(2, "HEIGHT", "Stack it in $100 bills"), "Part two. Height. Let's stack hundred dollar bills.", 3.5, ch=2)
add(stack_climb(1.0922, "$1 MILLION", Y1, "About as tall as a kid."), "A hundred dollar bill is about a tenth of a millimetre thick. One million dollars is ten thousand bills. Stacked up, that's about one point one metres. Roughly as tall as a small kid.", 8)
add(stack_climb(1092.2, "$1 BILLION", Y2, "Taller than the Burj Khalifa."), "One billion dollars is ten million bills. The stack shoots past the Eiffel Tower, past the Burj Khalifa, the tallest building on Earth, and keeps going to over a kilometre.", 10)
add(stack_climb(1092200, "$1 TRILLION", Y3, "Past the space station."), "And one trillion? The stack climbs past airliners, past the edge of space at one hundred kilometres, past the space station, and ends almost eleven hundred kilometres up.", 11)

add(title_card(3, "WEIGHT", "A $100 bill weighs about 1 gram"), "Part three. Weight. A hundred dollar bill weighs about one gram.", 4, ch=3)
add(three_up("Cash in $100 bills", [10, 10000, 1e7], ["fits in a backpack", "heavier than an elephant", "≈ the whole Eiffel Tower"], 0, "10 kilograms.", unit_fmt=wfmt, icon=icon_weight),
    "So a million dollars in hundreds weighs just ten kilograms. You could carry it in a backpack.", 6)
add(three_up("Cash in $100 bills", [10, 10000, 1e7], ["fits in a backpack", "heavier than an elephant", "≈ the whole Eiffel Tower"], 1, "10 tonnes.", unit_fmt=wfmt, icon=icon_weight),
    "A billion weighs ten tonnes. That's heavier than an adult elephant. You'd need a truck.", 6)
add(three_up("Cash in $100 bills", [10, 10000, 1e7], ["fits in a backpack", "heavier than an elephant", "≈ the whole Eiffel Tower"], 2, "10,000 tonnes.", unit_fmt=wfmt, icon=icon_weight),
    "And a trillion weighs ten thousand tonnes. About as much as the entire Eiffel Tower.", 7)

add(title_card(4, "WORK", "Earn $15 an hour, spend nothing"), "Part four. Work. Say you earn fifteen dollars an hour, full time, and never spend a cent.", 5, ch=4)
add(compare_bars("Earning $1 MILLION at $15/hour", [("Time needed", "32 years", 32 / 45, Y1, True), ("A whole career", "~45 years", 1.0, DGREY, False)], "32 years. Most of a working life.", Y1, "$31,200 per year"),
    "That's thirty one thousand two hundred dollars a year. To reach one million, you'd need thirty two years. Most of a career.", 7)
add(timeline(32051, [(4586, "Pyramids", True), (11700, "Ice Age ends", False), (20000, "Ice Age peak", True)], 32051, Y2, "Earning $1 BILLION: 32,051 years", "you'd have started in the Stone Age"),
    "One billion takes thirty two thousand years. You'd have to start working in the Stone Age to be done today.", 9)
add(compare_bars("Earning $1 TRILLION at $15/hour", [("Time needed", "32 million years", 32.05 / 66, Y3, True), ("Since the dinosaurs died", "66 million years", 1.0, DGREY, False)], "Half the time since the dinosaurs.", Y3),
    "And one trillion? Thirty two million years. That's about half the time since the dinosaurs went extinct.", 8)

add(title_card(5, "SPENDING", "Spend $1,000 every single day"), "Part five. Spending. Now flip it around. You spend a thousand dollars, every single day.", 5, ch=5)
add(compare_bars("Spending $1,000 per day", [("$1 MILLION is gone after", "2.7 years", 2.74 / 2738, Y1, True), ("$1 BILLION is gone after", "2,738 years", 1.0, Y2, True)], "A billion lasts since ancient Rome.", Y2),
    "A million dollars lasts two point seven years. A billion lasts two thousand seven hundred years. If you'd started when Rome was a small village, you'd still be spending today.", 10)
add(statement([(360, "$1 TRILLION at $1,000 a day:", 56, WHITE, 0.2), (520, "2.7 MILLION years", 110, Y3, 0.8), (680, "Longer than our species has existed.", 46, GREY, 1.8)]),
    "And a trillion? Two point seven million years. Longer than our own species, Homo sapiens, has even existed.", 7)

add(title_card(6, "SHARING", "Split it with everyone on Earth"), "Part six. Sharing. What if we split the money between all eight point two billion people on Earth?", 5, ch=6)
add(people_grid("12 cents each", "$1 BILLION", Y2, "Not even a candy bar."), "One billion dollars, shared with everyone, is about twelve cents per person. Not even a candy bar.", 7)
add(people_grid("$122 each", "$1 TRILLION", Y3, "A nice dinner. That's it."), "A trillion is a hundred twenty two dollars each. Nice, but nobody's quitting their job. Huge numbers shrink fast when you divide by eight billion.", 8)

add(title_card(7, "RICE", "One grain ≈ 25 milligrams"), "Part seven. Rice. One grain weighs about twenty five milligrams.", 4, ch=7)
add(three_up("Grains of rice", [25, 25000, 2.5e7], ["one big bag", "a full truckload", "a whole cargo ship"], 0, "25 kg. One bag.", unit_fmt=wfmt),
    "A million grains is twenty five kilograms. One big bag.", 5)
add(three_up("Grains of rice", [25, 25000, 2.5e7], ["one big bag", "a full truckload", "a whole cargo ship"], 1, "25 tonnes. A full truck.", unit_fmt=wfmt),
    "A billion grains, twenty five tonnes. A completely full truck.", 5)
add(three_up("Grains of rice", [25, 25000, 2.5e7], ["one big bag", "a full truckload", "a whole cargo ship"], 2, "25,000 tonnes. A cargo ship.", unit_fmt=wfmt),
    "And a trillion grains? Twenty five thousand tonnes. You'd need a cargo ship.", 6)

add(recap, "So here's everything side by side. Eleven days, thirty two years, thirty two thousand years. A backpack, a truck, the Eiffel Tower. Every row tells the same story. A billion is not a bit more than a million. And a trillion is a different universe.", 14, ch=8)
add(statement([(420, "A trillion isn't “a lot”.", 80, WHITE, 0.2), (560, "It's a thousand billions.", 80, Y3, 1.0), (740, "Next time you hear it in the news, picture the stack.", 44, GREY, 2.0)]),
    "So next time you hear the word trillion in the news, don't let it slide by. Picture a stack of cash reaching past the space station.", 8)
add(outro, "If this made numbers feel real for once, subscribe to Chart Snack. New charts every day.", 6)

if __name__ == "__main__":
    out = "/home/claude/chartsnack/lf01"
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    if mode == "stills":
        stills(B, out, CH, [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else list(range(0, len(B), 3)))
    else:
        lib.VOICE_SPEED = 1.0
        build(B, out, "chartsnack_lf01_trillion.mp4", CH)
