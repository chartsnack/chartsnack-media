import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("52", "googol", dict(
    hook=[(460, "A GOOGOL =", 110, Y2, True), (600, "1 and 100 zeros.", 76, WHITE, True), (800, "Bigger than", 80, WHITE, True),
          (920, "the UNIVERSE?", 110, Y3, True)], pulse=0,
    steps=[dict(title="COUNTING ZEROS", col=Y1, sub="million, billion, trillion", big=lambda p: f"{int(12 * p)} zeros",
                bars=[("Million", "6 zeros", 0.06, DGREY, False), ("Trillion", "12 zeros", 0.12, Y1, True), ("Googol", "100 zeros", 1.0, Y2, False)], reveal="A TRILLION: JUST 12.", reveal_sub="A googol has 100."),
           dict(title="ATOMS IN EARTH", col=Y2, sub="the whole planet, roughly", big=lambda p: f"10^{int(50 * p)}",
                bars=[("Atoms in Earth", "50 zeros", 0.5, Y2, True), ("Googol", "100 zeros", 1.0, DGREY, False)], reveal="ONLY HALFWAY.", reveal_sub="In zeros, at least."),
           dict(title="ATOMS IN THE UNIVERSE", col=Y3, sub="observable universe, estimate", big=lambda p: f"10^{int(80 * p)}",
                bars=[("Universe", "80 zeros", 0.8, Y3, True), ("Googol", "100 zeros", 1.0, DGREY, False)], reveal="GOOGOL WINS.", reveal_sub="100 quintillion times bigger.")],
    recap=("Number of zeros:", [("TRILLION", "12", Y1), ("ATOMS IN EARTH", "~50", Y2), ("ATOMS IN UNIVERSE", "~80", Y3)], 72),
    teaser="Hours you work in a lifetime",
    yt_vo=["A googol: a one with a hundred zeros. Bigger than the universe?",
           "A million has six zeros. A billion, nine. A trillion, just twelve. A googol has one hundred.",
           "Every atom in planet Earth? Roughly ten to the fifty. Fifty zeros. Only halfway there.",
           "Every atom in the entire observable universe: about ten to the eighty. A googol is still a hundred quintillion times bigger.",
           "A number bigger than everything that exists.",
           "Next: how many hours will you work in your life?"],
    tt_vo=["A googol: one and a hundred zeros.", "A trillion has just twelve.", "Atoms in Earth: about fifty.", "The whole universe: only eighty."]))
