import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("49", "count_million", dict(
    hook=[(480, "Count $1 MILLION", 90, WHITE, True), (600, "in $1 bills.", 80, WHITE, True), (760, "1 bill per second.", 70, GREY, False),
          (950, "How long?", 130, Y1, True)], pulse=3,
    steps=[dict(title="$1 MILLION", col=Y1, sub="1,000,000 bills, nonstop", big=lambda p: f"{11.6 * p:.1f} days",
                bars=[("Counting", "11.6 days", 1.0, Y1, True)], reveal="11.6 DAYS.", reveal_sub="No sleep. No breaks."),
           dict(title="$1 BILLION", col=Y2, sub="1,000,000,000 bills", big=lambda p: f"{31.7 * p:.1f} years",
                bars=[("$1 million", "11.6 days", 0.01, DGREY, False), ("$1 billion", "31.7 years", 1.0, Y2, True)], reveal="31.7 YEARS.", reveal_sub="Start at 20, done at 51."),
           dict(title="$1 TRILLION", col=Y3, sub="1,000,000,000,000 bills", big=lambda p: f"{fmt(31688 * p)} years",
                bars=[("$1 billion", "31.7 years", 0.01, DGREY, False), ("$1 trillion", "31,688 years", 1.0, Y3, True)], reveal="31,688 YEARS.", reveal_sub="6x all of recorded history.")],
    recap=("Counting $1 per second:", [("$1 MILLION", "11.6 days", Y1), ("$1 BILLION", "31.7 years", Y2), ("$1 TRILLION", "31,688 years", Y3)], 64),
    teaser="Every possible Sudoku",
    yt_vo=["Count one million dollars in one dollar bills. How long?",
           "One bill per second, nonstop, no sleep. One million dollars takes eleven and a half days.",
           "One billion dollars? Thirty one point seven years of counting. Start at twenty, finish at fifty one.",
           "And one trillion dollars: thirty one thousand six hundred eighty eight years. Six times longer than all of recorded history.",
           "Millions are days. Billions are lifetimes.",
           "Next: how many Sudoku puzzles exist?"],
    tt_vo=["Count a million dollars, one bill a second.", "A million: eleven days.", "A billion: thirty one years.", "A trillion: thirty one thousand years."]))
