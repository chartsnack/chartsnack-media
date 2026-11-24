import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("54", "paid_to_sleep", dict(
    hook=[(460, "Get $1 for every", 80, WHITE, True), (590, "SECOND you sleep.", 100, Y1, True), (730, "8 hours a night.", 66, GREY, False),
          (930, "How rich?", 130, Y3, True)], pulse=3,
    steps=[dict(title="ONE NIGHT", col=Y1, sub="8 hours = 28,800 seconds", big=lambda p: "$" + fmt(28800 * p),
                bars=[("One hour", "$3,600", 1 / 8, DGREY, False), ("One night", "$28,800", 1.0, Y1, True)], reveal="$28,800 A NIGHT.", reveal_sub="Just for sleeping."),
           dict(title="ONE YEAR", col=Y2, sub="365 nights", big=lambda p: f"${10.5 * p:.1f} million",
                bars=[("One night", "$28,800", 0.01, DGREY, False), ("One year", "$10.5 million", 1.0, Y2, True)], reveal="$10.5 MILLION.", reveal_sub="A millionaire after 35 nights."),
           dict(title="80 YEARS", col=Y3, sub="a lifetime of sleep", big=lambda p: f"${841 * p:.0f} million",
                bars=[("One year", "$10.5 million", 1 / 80, DGREY, False), ("80 years", "$841 million", 1.0, Y3, True)], reveal="$841 MILLION.", reveal_sub="Almost a billionaire. Asleep.")],
    recap=("$1 per second of sleep:", [("ONE NIGHT", "$28,800", Y1), ("ONE YEAR", "$10.5 million", Y2), ("80 YEARS", "$841 million", Y3)], 64),
    teaser="The odds of a royal flush",
    yt_vo=["Get one dollar for every second you sleep. How rich are you?",
           "Eight hours a night is twenty eight thousand eight hundred seconds. So, twenty eight thousand eight hundred dollars, every night.",
           "After one year: ten and a half million dollars. You'd be a millionaire after just thirty five nights.",
           "Sleep like that for eighty years: about eight hundred forty one million dollars. Almost a billionaire, without ever waking up.",
           "Best paid job in the world.",
           "Next: how long until you get a royal flush?"],
    tt_vo=["One dollar for every second you sleep.", "One night: twenty eight thousand.", "One year: ten million.", "A lifetime: eight hundred forty million."]))
