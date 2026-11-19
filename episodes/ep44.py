import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("44", "briefcases", dict(
    hook=[(480, "One briefcase holds", 80, WHITE, True), (600, "$1 MILLION", 130, Y1, True), (710, "in $100 bills.", 70, WHITE, True),
          (900, "How many for", 80, WHITE, True), (1010, "$1 TRILLION?", 120, Y3, True)], pulse=4,
    steps=[dict(title="$1 MILLION", col=Y1, sub="10,000 bills of $100", big=lambda p: f"{10 * p:.0f} kg",
                bars=[("Briefcases", "1", 1.0, Y1, True)], reveal="1 BRIEFCASE.", reveal_sub="About 10 kg. You can carry it."),
           dict(title="$1 BILLION", col=Y2, sub="10 million bills", big=lambda p: f"{fmt(1000 * p)} briefcases",
                bars=[("Weight", "10 tonnes", 1.0, Y2, True)], reveal="1,000 BRIEFCASES.", reveal_sub="10 tonnes. A full truck.", big_size=88),
           dict(title="$1 TRILLION", col=Y3, sub="10 billion bills", big=lambda p: f"{fmt(1e6 * p)} briefcases",
                bars=[("$1 billion", "1,000 cases", 0.001, DGREY, False), ("$1 trillion", "1 million cases", 1.0, Y3, True)], reveal="1 MILLION BRIEFCASES.", reveal_sub="10,000 tonnes of cash.", big_size=80)],
    recap=("$100 bills in briefcases:", [("$1 MILLION", "1 case", Y1), ("$1 BILLION", "1,000 cases", Y2), ("$1 TRILLION", "1,000,000 cases", Y3)], 60),
    teaser="Seating 10 people at dinner",
    yt_vo=["A briefcase holds a million dollars. How many for a trillion?",
           "Ten thousand hundred dollar bills fit in one briefcase. About ten kilos. Easy to carry.",
           "One billion dollars needs a thousand briefcases. Ten tonnes of cash. That's a whole truck.",
           "And one trillion? One million briefcases. Ten thousand tonnes of hundred dollar bills.",
           "One case. One truck. A mountain of cash.",
           "Next: how many ways to seat ten people at dinner?"],
    tt_vo=["One briefcase: a million dollars.", "A million: one case, ten kilos.", "A billion: a thousand cases.", "A trillion: one million briefcases."]))
