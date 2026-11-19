import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
P = 43252003274489856000
build_ep("40", "rubik", dict(
    hook=[(470, "A Rubik's Cube has", 80, WHITE, True), (600, "HOW MANY", 120, Y3, True), (720, "positions?", 90, WHITE, True),
          (920, "Try 1 per second.", 60, GREY, False), (1060, "How long?", 120, Y1, True)], pulse=1,
    steps=[dict(title="POSITIONS", col=Y1, sub="every way the cube can be mixed", big=lambda p: "43 quintillion", big_size=88,
                bars=[("43,252,003,274,489,856,000", "", 1.0, Y1, True)], reveal="43 QUINTILLION.", reveal_sub="A 43 with 18 zeros."),
           dict(title="1 PER SECOND", col=Y2, sub="non-stop, day and night", big=lambda p: f"{1.37 * p:.2f} trillion yrs", big_size=84,
                bars=[("Age of the universe", "13.8 billion yrs", 0.01, DGREY, False), ("Every cube position", "1.37 trillion yrs", 1.0, Y2, True)],
                reveal="1.37 TRILLION YEARS.", reveal_sub="100x the age of the universe."),
           dict(title="BUT…", col=Y3, sub="any position can be solved in", big=lambda p: "20 moves",
                bars=[("Maximum moves needed", "20", 1.0, Y3, True)], reveal="20 MOVES. ALWAYS.", reveal_sub="'God's number' (proved in 2010).")],
    recap=("The Rubik's Cube:", [("POSITIONS", "43 quintillion", Y1), ("1 PER SECOND", "1.37 trillion yrs", Y2), ("ALWAYS SOLVABLE IN", "20 moves", Y3)], 60),
    teaser="$100,000 a year until $1 billion",
    yt_vo=["How many positions does a Rubik's cube have?",
           "Every possible way to mix it: forty three quintillion. That's forty three with eighteen zeros.",
           "Look at one position per second, non stop, and you'd need one point three seven trillion years. About a hundred times the age of the universe.",
           "And yet: every single one of those positions can be solved in twenty moves or fewer. That was proven in twenty ten.",
           "Forty three quintillion positions. Never more than twenty moves.",
           "Next: earning a hundred thousand a year, until a billion."],
    tt_vo=["How many Rubik's cube positions?", "Forty three quintillion.", "One per second: a trillion years.", "But always solvable in twenty moves."]))
