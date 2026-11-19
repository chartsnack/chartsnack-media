import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("41", "salary", dict(
    hook=[(480, "You earn", 80, WHITE, True), (610, "$100,000", 130, Y1, True), (720, "a year. Spend nothing.", 64, WHITE, True),
          (920, "When are you a", 76, WHITE, True), (1040, "BILLIONAIRE?", 120, Y3, True)], pulse=4,
    steps=[dict(title="$1 MILLION", col=Y1, sub="$100,000 per year, saved", big=lambda p: f"{10 * p:.0f} years",
                bars=[("A career", "~40 years", 1.0, DGREY, False), ("$1 million", "10 years", 0.25, Y1, True)], reveal="10 YEARS.", reveal_sub="Doable in one career."),
           dict(title="$100 MILLION", col=Y2, sub="$100,000 per year, saved", big=lambda p: f"{fmt(1000 * p)} years",
                bars=[("$1 million", "10 years", 0.01, DGREY, False), ("$100 million", "1,000 years", 1.0, Y2, True)], reveal="1,000 YEARS.", reveal_sub="Start in the Middle Ages."),
           dict(title="$1 BILLION", col=Y3, sub="$100,000 per year, saved", big=lambda p: f"{fmt(10000 * p)} years",
                bars=[("$100 million", "1,000 years", 0.1, DGREY, False), ("$1 billion", "10,000 years", 1.0, Y3, True)], reveal="10,000 YEARS.", reveal_sub="Twice as long ago as the pyramids.")],
    recap=("At $100,000 a year:", [("$1 MILLION", "10 years", Y1), ("$100 MILLION", "1,000 years", Y2), ("$1 BILLION", "10,000 years", Y3)]),
    teaser="Your life on your phone",
    yt_vo=["Earn a hundred thousand a year. When are you a billionaire?",
           "Save every cent of a hundred thousand dollars a year. One million takes ten years. Doable.",
           "One hundred million? One thousand years. You'd have to start in the Middle Ages.",
           "And one billion dollars: ten thousand years of saving. That's twice as long ago as the Great Pyramid was built.",
           "Ten years. A thousand years. Ten thousand years.",
           "Next: how much of your life is spent on your phone?"],
    tt_vo=["A hundred thousand a year. When a billionaire?", "One million: ten years.", "A hundred million: a thousand years.", "A billion: ten thousand years."]))
