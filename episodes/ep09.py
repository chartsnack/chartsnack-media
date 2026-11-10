import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

FACT = "80658175170943878571660636856403766975289505440883277824000000000000"  # 52!, 68 digits

def card(d, x, y, a, col=WHITE, w=110, h=154):
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], radius=12, fill=mix(col, a))
    d.rounded_rectangle([x - w / 2 + 8, y - h / 2 + 8, x + w / 2 - 8, y + h / 2 - 8], radius=8, outline=mix(Y3, a), width=4)

def s1(t, D):
    im, d = frame_base()
    for i in range(5):
        ang = -24 + i * 12
        card(d, 540 + (i - 2) * 70, 520 + abs(i - 2) * 14, 1.0)
    text(d, (540, 800), "Shuffle a deck.", 96, WHITE, 1.0)
    text(d, (540, 940), "How many orders", 80, WHITE, 1.0)
    p = 1 + 0.05 * math.sin(t * 7)
    d.text((540, 1080), "are possible?", font=F(int(110 * p)), fill=Y3, anchor="mm")
    return im

def s2(t, D):
    im, d = frame_base()
    text(d, (540, 420), "52 × 51 × 50 × 49 × …", 64, Y1, appear(t, 0))
    text(d, (540, 495), "choices for card 1, card 2, card 3 …", 36, GREY, appear(t, 0.1), bold=False)
    p = prog(t, D)
    n = max(1, int(round(68 * p)))
    shown = FACT[:n]
    rows = wrap_digits(shown, 14)
    for i, r in enumerate(rows):
        text(d, (540, 640 + i * 95), r, 76, WHITE, appear(t, 0.2))
    text(d, (540, 1190), f"{n} digits", 60, Y1, appear(t, 0.4))
    text(d, (540, 1600), "A 68-digit number.", 64, Y1, appear(t, D - 2.4))
    text(d, (540, 1690), "Called 52 factorial: 52!", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s3 = bars_scene("HOW BIG IS THAT?", Y2, "count the digits", None,
                [("SECONDS SINCE BIG BANG", "18 digits", 18 / 68, DGREY, False),
                 ("ATOMS IN YOUR BODY", "28 digits", 28 / 68, DGREY, False),
                 ("ATOMS IN PLANET EARTH", "51 digits", 51 / 68, DGREY, False),
                 ("ORDERS OF A DECK", "68 digits", 1.0, Y2, True)],
                "More than Earth's atoms.", "Way, way more.")

def s4(t, D):
    im, d = frame_base()
    text(d, (540, 420), "EVERYONE ON EARTH", 66, Y3, appear(t, 0))
    text(d, (540, 495), "shuffling once a second since the Big Bang", 34, GREY, appear(t, 0.1), bold=False)
    a = appear(t, 0.4)
    for k in range(40):
        i, j = k % 8, k // 8
        st = 0.4 + k * 0.06
        card(d, 160 + i * 108, 640 + j * 120, appear(t, st, 0.2) * 0.9, WHITE, w=70, h=98)
    text(d, (90, 1290), "ORDERS EVER SEEN", 38, Y3, a, anchor="lm")
    bar(d, 90, 1330, 900, 1400, 0.0, Y3, a, minw=8)
    text(d, (900, 1440), "0.00000000000000000…%", 34, GREY, a, bold=False, anchor="rm")
    text(d, (540, 1600), "Still basically zero.", 64, Y3, appear(t, D - 2.4))
    text(d, (540, 1690), "38 zeros after the decimal point.", 40, GREY, appear(t, D - 2.0), bold=False)
    return im

s5 = statement([(560, "Your next good shuffle", 64, WHITE, True, 0.0),
                (660, "is almost certainly", 64, WHITE, True, 0.3),
                (840, "A FIRST", 170, Y3, True, 0.8),
                (1000, "in the history of the universe.", 48, GREY, False, 1.2)])

YT = ([("s1", s1, 4.5), ("s2", s2, 12.0), ("s3", s3, 13.0), ("sx", sub_scene(), 2.5), ("s4", s4, 14.0), ("s5", s5, 9.0),
       ("s6", outro_next("A penny doubled for 30 days"), 5.0)],
      [(0, 4.5, 0.15, "Shuffle a deck of cards. How many different orders are possible?"),
       (4.5, 12, 0.5, "Fifty two choices for the first card, fifty one for the next, and so on. Multiply it all, and you get a sixty eight digit number."),
       (16.5, 13, 0.5, "Seconds since the Big Bang: eighteen digits. Atoms in your body: twenty eight. Atoms in the whole Earth: fifty one. A deck of cards: sixty eight."),
       (29.5, 2.5, 0.1, "Subscribe for more."),
       (32, 14, 0.5, "Imagine every person on Earth shuffling once a second, since the Big Bang. They still would have seen basically none of the possible orders."),
       (46, 9, 0.4, "So your next good shuffle is almost certainly a first, in the history of the universe."),
       (55, 5, 0.4, "Next: a penny, doubled for thirty days.")],
      [(5.0, 13.8)],
      [0.2, 14.0, 27.0, 29.7, 43.6, 46.9, 55.4])
TT = ([("s1", s1, 3.0), ("s2", s2, 5.0), ("s3", s3, 6.0), ("s4", s4, 6.0), ("s5", s5, 5.0)],
      [(0, 3, 0.05, "How many ways can you shuffle a deck?"),
       (3, 5, 0.2, "A sixty eight digit number."),
       (8, 6, 0.2, "More than the atoms in planet Earth."),
       (14, 6, 0.2, "Shuffle since the Big Bang? Still basically zero."),
       (20, 5, 0.2, "Your shuffle is a first. Follow for more.")],
      [(3.5, 4.8)],
      [0.1, 5.6, 11.6, 17.6, 20.4])

if __name__ == "__main__":
    run("/home/claude/chartsnack/ep09", "chartsnack_ep09_cards.mp4", YT, TT, [0.0, 10.5, 12.5, 1.3, 13.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
