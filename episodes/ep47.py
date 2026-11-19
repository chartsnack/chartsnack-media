import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("47", "one_line", dict(
    hook=[(480, "All 8.2 billion people", 76, WHITE, True), (590, "in ONE LINE.", 110, Y3, True), (720, "Shoulder to shoulder.", 66, GREY, False),
          (920, "How long", 90, WHITE, True), (1030, "is the line?", 100, Y1, True)], pulse=1,
    steps=[dict(title="THE LINE", col=Y1, sub="about 0.5 m per person", big=lambda p: f"{fmt(4.1e6 * p)} km", big_size=96,
                bars=[("Length", "4.1 million km", 1.0, Y1, True)], reveal="4.1 MILLION KM.", reveal_sub="Now let's wrap it around things."),
           dict(title="AROUND THE EARTH", col=Y2, sub="Equator: 40,075 km", big=lambda p: f"{102 * p:.0f} times",
                bars=[("1 lap", "40,075 km", 0.01, DGREY, False), ("The line", "102 laps", 1.0, Y2, True)], reveal="102 TIMES AROUND.", reveal_sub="The whole planet, 102 times."),
           dict(title="TO THE MOON", col=Y3, sub="384,400 km away", big=lambda p: f"{10.7 * p:.1f} times",
                bars=[("Earth to Moon", "384,400 km", 384400 / 4.1e6, DGREY, False), ("The line", "4.1 million km", 1.0, Y3, True)], reveal="10 TIMES TO THE MOON.", reveal_sub="Or 5 round trips.")],
    recap=("Everyone in one line:", [("LENGTH", "4.1 million km", Y1), ("AROUND EARTH", "102 times", Y2), ("TO THE MOON", "10.7 times", Y3)], 60),
    teaser="A new chart snack tomorrow",
    yt_vo=["Everyone on Earth in one line. How long is it?",
           "Give every person about half a meter. Eight point two billion people make a line four point one million kilometers long.",
           "That wraps around the equator one hundred two times.",
           "Or stretch it into space: it reaches the Moon more than ten times. Five full round trips.",
           "One line. The whole planet. Five trips to the Moon.",
           "See you at the next chart snack."],
    tt_vo=["Everyone on Earth in one line.", "Four million kilometers long.", "A hundred times around Earth.", "Ten times to the Moon."]))
