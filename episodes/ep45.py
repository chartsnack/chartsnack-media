import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("45", "seating", dict(
    hook=[(470, "Seat friends at dinner", 76, WHITE, True), (580, "in a NEW order", 96, Y3, True), (680, "every night.", 76, WHITE, True),
          (880, "With 10 people,", 76, WHITE, True), (990, "how long?", 120, Y1, True)], pulse=1,
    steps=[dict(title="5 PEOPLE", col=Y1, sub="5 x 4 x 3 x 2 x 1", big=lambda p: f"{120 * p:.0f} orders",
                bars=[("Nights needed", "120", 120 / 365, Y1, True), ("One year", "365", 1.0, DGREY, False)], reveal="120 NIGHTS.", reveal_sub="Done in 4 months."),
           dict(title="8 PEOPLE", col=Y2, sub="8 x 7 x 6 x ... x 1", big=lambda p: fmt(40320 * p) + " orders", big_size=92,
                bars=[("5 people", "120 nights", 0.003, DGREY, False), ("8 people", "110 years", 1.0, Y2, True)], reveal="110 YEARS.", reveal_sub="Longer than a lifetime."),
           dict(title="10 PEOPLE", col=Y3, sub="10 x 9 x 8 x ... x 1", big=lambda p: fmt(3628800 * p) + " orders", big_size=88,
                bars=[("8 people", "110 years", 0.011, DGREY, False), ("10 people", "9,935 years", 1.0, Y3, True)], reveal="9,935 YEARS.", reveal_sub="Start in the Stone Age.")],
    recap=("A new seating order every night:", [("5 PEOPLE", "4 months", Y1), ("8 PEOPLE", "110 years", Y2), ("10 PEOPLE", "9,935 years", Y3)], 64),
    teaser="1 cent every second",
    yt_vo=["A new seating order every night. With ten people, how long?",
           "Five friends can sit in one hundred twenty different orders. One per night: about four months.",
           "Eight friends? Forty thousand orders. That's one hundred ten years of dinners.",
           "And ten friends: three point six million orders. Nine thousand nine hundred thirty five years. You'd have to start in the Stone Age.",
           "Two more chairs. Ten thousand more years.",
           "Next: one cent, every single second."],
    tt_vo=["A new seating order every night.", "Five people: four months.", "Eight people: a hundred ten years.", "Ten people: ten thousand years."]))
