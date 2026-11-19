import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
C = 292201338
build_ep("38", "powerball", dict(
    hook=[(480, "Buy EVERY", 100, WHITE, True), (600, "Powerball ticket.", 90, WHITE, True), (760, "Guaranteed jackpot.", 70, Y3, True),
          (960, "But how much –", 70, WHITE, True), (1060, "and how long?", 100, Y1, True)], pulse=2,
    steps=[dict(title="ALL COMBINATIONS", col=Y1, sub="5 of 69 numbers + 1 of 26", big=lambda p: fmt(C * p),
                bars=[("Your odds per ticket", "1 in 292 million", 1.0, Y1, True)], reveal="292 MILLION TICKETS.", reveal_sub="Every possible combination."),
           dict(title="THE COST", col=Y2, sub="$2 per ticket", big=lambda p: "$" + fmt(2 * C * p),
                bars=[("Cost", "$584 million", 1.0, Y2, True)], reveal="$584 MILLION.", reveal_sub="Before you win anything."),
           dict(title="FILLING THEM OUT", col=Y3, sub="1 ticket per second, non-stop", big=lambda p: f"{9.3 * p:.1f} years",
                bars=[("Powerball draws: 3 per week", "", 1.0, Y3, True)], reveal="9.3 YEARS.", reveal_sub="Non-stop. Day and night.")],
    recap=("Buying every ticket:", [("TICKETS", "292 million", Y1), ("COST", "$584 million", Y2), ("TIME", "9.3 years", Y3)]),
    teaser="Earth's history in one year",
    yt_vo=["Buy every Powerball ticket. How much, and how long?",
           "Five numbers out of sixty nine, plus one out of twenty six. That's two hundred ninety two million different tickets.",
           "At two dollars each, buying them all costs five hundred eighty four million dollars.",
           "And just filling them out, one ticket per second, non stop? Over nine years. The draw would be long gone.",
           "Two hundred ninety two million tickets. One jackpot.",
           "Next: the history of Earth, squeezed into one year."],
    tt_vo=["Buy every Powerball ticket?", "Two hundred ninety two million tickets.", "Cost: five hundred eighty four million.", "One per second: over nine years."]))
