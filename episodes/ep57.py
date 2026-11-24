import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("57", "coffee", dict(
    hook=[(460, "A $5 coffee.", 100, WHITE, True), (590, "EVERY day.", 110, Y1, True), (790, "What does it cost", 76, WHITE, True),
          (910, "over a LIFETIME?", 96, Y3, True)], pulse=1,
    steps=[dict(title="ONE YEAR", col=Y1, sub="365 coffees", big=lambda p: "$" + fmt(1825 * p),
                bars=[("One week", "$35", 35 / 1825, DGREY, False), ("One year", "$1,825", 1.0, Y1, True)], reveal="$1,825 A YEAR.", reveal_sub="One cup at a time."),
           dict(title="10 YEARS", col=Y2, sub="3,652 coffees", big=lambda p: "$" + fmt(18262 * p),
                bars=[("One year", "$1,825", 0.1, DGREY, False), ("10 years", "$18,262", 1.0, Y2, True)], reveal="$18,262.", reveal_sub="That's a car."),
           dict(title="50 YEARS", col=Y3, sub="18,262 coffees", big=lambda p: "$" + fmt(91312 * p),
                bars=[("10 years", "$18,262", 0.2, DGREY, False), ("50 years", "$91,312", 1.0, Y3, True)], reveal="$91,312.", reveal_sub="Before any price increases.")],
    recap=("$5 coffee, every day:", [("ONE YEAR", "$1,825", Y1), ("10 YEARS", "$18,262", Y2), ("50 YEARS", "$91,312", Y3)], 72),
    teaser="6 LEGO bricks, how many builds?",
    yt_vo=["A five dollar coffee, every day. What's the lifetime cost?",
           "Five dollars a day is one thousand eight hundred twenty five dollars a year. One cup at a time.",
           "Over ten years: more than eighteen thousand dollars. That's a car.",
           "Fifty years of daily coffee: about ninety one thousand dollars. And that's before prices go up.",
           "Small habits. Big numbers.",
           "Next: how many ways can six Lego bricks fit together?"],
    tt_vo=["A five dollar coffee, every day.", "One year: eighteen hundred dollars.", "Ten years: eighteen thousand.", "Fifty years: ninety one thousand."]))
