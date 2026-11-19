import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("37", "minutes", dict(
    hook=[(500, "How long is", 90, WHITE, True), (640, "1 BILLION", 140, Y3, True), (780, "MINUTES?", 120, WHITE, True),
          (980, "Guess before the end.", 56, GREY, False)], pulse=1,
    steps=[dict(title="1 MILLION MINUTES", col=Y1, sub="1,000,000 minutes", big=lambda p: f"{694 * p:.0f} days",
                bars=[("1 year", "365 days", 365 / 694, DGREY, False), ("1 million minutes", "694 days", 1.0, Y1, True)], reveal="1.9 YEARS.", reveal_sub="Less than 2 years."),
           dict(title="100 MILLION MINUTES", col=Y2, sub="100,000,000 minutes", big=lambda p: f"{190 * p:.0f} years",
                bars=[("1 million minutes", "1.9 years", 0.01, DGREY, False), ("100 million minutes", "190 years", 1.0, Y2, True)], reveal="190 YEARS.", reveal_sub="Longer than any human has ever lived."),
           dict(title="1 BILLION MINUTES", col=Y3, sub="1,000,000,000 minutes", big=lambda p: f"{fmt(1901 * p)} years",
                bars=[("100 million minutes", "190 years", 0.1, DGREY, False), ("1 billion minutes", "1,901 years", 1.0, Y3, True)], reveal="1,901 YEARS.", reveal_sub="Back to the Roman Empire.")],
    recap=("How long is…", [("1 MILLION MIN", "1.9 years", Y1), ("100 MILLION MIN", "190 years", Y2), ("1 BILLION MIN", "1,901 years", Y3)], 64),
    teaser="Buying every lottery ticket",
    yt_vo=["How long is one billion minutes? Make a guess.",
           "One million minutes is about six hundred ninety four days. Less than two years.",
           "A hundred million minutes: about one hundred ninety years. Longer than any person has ever lived.",
           "And one billion minutes? One thousand nine hundred and one years. Count back that far, and you're in the Roman Empire.",
           "Two years. Two lifetimes. Two thousand years.",
           "Next: buying every single lottery ticket."],
    tt_vo=["How long is a billion minutes?", "A million minutes: under two years.", "A hundred million: one hundred ninety years.", "A billion: nineteen hundred years."]))
