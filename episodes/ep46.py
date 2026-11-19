import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("46", "cent_per_second", dict(
    hook=[(480, "Earn just", 80, WHITE, True), (610, "1 CENT", 140, Y1, True), (730, "every second.", 80, WHITE, True),
          (920, "For your whole life.", 64, GREY, False), (1060, "Rich?", 120, Y3, True)], pulse=1,
    steps=[dict(title="ONE DAY", col=Y1, sub="86,400 seconds", big=lambda p: "$" + fmt(864 * p),
                bars=[("One hour", "$36", 36 / 864, DGREY, False), ("One day", "$864", 1.0, Y1, True)], reveal="$864 A DAY.", reveal_sub="Even while you sleep."),
           dict(title="ONE YEAR", col=Y2, sub="31.6 million seconds", big=lambda p: "$" + fmt(315576 * p),
                bars=[("One day", "$864", 864 / 315576, DGREY, False), ("One year", "$315,576", 1.0, Y2, True)], reveal="$315,576 A YEAR.", reveal_sub="From one cent."),
           dict(title="80 YEARS", col=Y3, sub="2.5 billion seconds", big=lambda p: f"${25.2 * p:.1f} million",
                bars=[("One year", "$315,576", 1 / 80, DGREY, False), ("80 years", "$25.2 million", 1.0, Y3, True)], reveal="$25 MILLION.", reveal_sub="One cent at a time.")],
    recap=("1 cent per second:", [("ONE DAY", "$864", Y1), ("ONE YEAR", "$315,576", Y2), ("80 YEARS", "$25.2 million", Y3)], 64),
    teaser="Everyone on Earth in one line",
    yt_vo=["One cent every second, your whole life. Are you rich?",
           "One cent sounds like nothing. But there are eighty six thousand seconds in a day. That's eight hundred sixty four dollars a day.",
           "In one year: over three hundred fifteen thousand dollars. From pennies.",
           "And over eighty years? About twenty five million dollars. All from one cent per second.",
           "Tiny amounts. Huge totals.",
           "Next: everyone on Earth, in one line."],
    tt_vo=["One cent, every second.", "One day: eight hundred sixty four dollars.", "One year: three hundred fifteen thousand.", "A lifetime: twenty five million."]))
