import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("60", "cent_from_everyone", dict(
    hook=[(460, "Everyone on Earth", 84, WHITE, True), (580, "gives you", 76, WHITE, True), (720, "1 CENT.", 140, Y1, True),
          (920, "How rich are you?", 86, Y3, True)], pulse=2,
    steps=[dict(title="1 CENT EACH", col=Y1, sub="8.2 billion people", big=lambda p: f"${82 * p:.0f} million",
                bars=[("1 cent each", "$82 million", 1.0, Y1, True)], reveal="$82 MILLION.", reveal_sub="For one cent each."),
           dict(title="$1 EACH", col=Y2, sub="8.2 billion dollars", big=lambda p: f"${8.2 * p:.1f} billion",
                bars=[("1 cent each", "$82 million", 0.01, DGREY, False), ("$1 each", "$8.2 billion", 1.0, Y2, True)], reveal="$8.2 BILLION.", reveal_sub="A billionaire, 8 times over."),
           dict(title="$100 EACH", col=Y3, sub="everyone, one bill", big=lambda p: f"${820 * p:.0f} billion",
                bars=[("$1 each", "$8.2 billion", 0.01, DGREY, False), ("$100 each", "$820 billion", 1.0, Y3, True)], reveal="$820 BILLION.", reveal_sub="Almost a trillion.")],
    recap=("Everyone on Earth gives you:", [("1 CENT", "$82 million", Y1), ("$1", "$8.2 billion", Y2), ("$100", "$820 billion", Y3)], 64),
    teaser="How many atoms are in you?",
    yt_vo=["Everyone on Earth gives you one cent. How rich are you?",
           "Eight point two billion people, one cent each. That's eighty two million dollars.",
           "Make it one dollar each, and you have eight point two billion dollars. A billionaire eight times over.",
           "And if everyone gave you one hundred dollars: eight hundred twenty billion dollars. Almost a trillion.",
           "Tiny amounts. Huge crowd.",
           "Next: how many atoms are in your body?"],
    tt_vo=["Everyone on Earth gives you one cent.", "That's eighty two million dollars.", "One dollar each: eight billion.", "A hundred each: eight hundred twenty billion."]))
