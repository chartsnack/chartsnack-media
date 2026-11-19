import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("43", "heartbeat_dollars", dict(
    hook=[(480, "Get $1", 110, WHITE, True), (600, "for every", 80, WHITE, True), (720, "HEARTBEAT.", 120, Y3, True),
          (920, "How rich are you?", 80, Y1, True)], pulse=2,
    steps=[dict(title="ONE DAY", col=Y1, sub="~70 beats per minute", big=lambda p: "$" + fmt(100800 * p),
                bars=[("One hour", "$4,200", 4200 / 100800, DGREY, False), ("One day", "$100,800", 1.0, Y1, True)], reveal="$100,800 A DAY.", reveal_sub="Even while you sleep."),
           dict(title="ONE YEAR", col=Y2, sub="~70 beats per minute", big=lambda p: f"${36.8 * p:.1f} million",
                bars=[("One day", "$100,800", 0.003, DGREY, False), ("One year", "$36.8 million", 1.0, Y2, True)], reveal="$36.8 MILLION.", reveal_sub="Every single year."),
           dict(title="80 YEARS", col=Y3, sub="~70 beats per minute", big=lambda p: f"${2.9 * p:.1f} billion",
                bars=[("One year", "$36.8 million", 1 / 80, DGREY, False), ("80 years", "$2.9 billion", 1.0, Y3, True)], reveal="$2.9 BILLION.", reveal_sub="A billionaire – three times over.")],
    recap=("$1 per heartbeat:", [("ONE DAY", "$100,800", Y1), ("ONE YEAR", "$36.8 million", Y2), ("80 YEARS", "$2.9 billion", Y3)], 64),
    teaser="$1 billion in briefcases",
    yt_vo=["One dollar for every heartbeat. How rich would you be?",
           "At about seventy beats a minute, that's over one hundred thousand dollars every single day.",
           "In one year: almost thirty seven million dollars. Just for staying alive.",
           "And over eighty years? Almost three billion dollars. A billionaire three times over, from your own heart.",
           "One heartbeat. One dollar. Three billion.",
           "Next: a billion dollars in briefcases."],
    tt_vo=["One dollar per heartbeat.", "One day: a hundred thousand.", "One year: thirty seven million.", "A lifetime: almost three billion."]))
