import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("58", "lego", dict(
    hook=[(460, "Six LEGO bricks.", 96, Y1, True), (580, "Classic 2x4, same color.", 62, GREY, False), (780, "How many ways", 90, WHITE, True),
          (900, "to build them?", 96, Y3, True)], pulse=0,
    steps=[dict(title="TWO BRICKS", col=Y1, sub="2x4, same color", big=lambda p: fmt(24 * p) + " ways",
                bars=[("2 bricks", "24 ways", 1.0, Y1, True)], reveal="24 WAYS.", reveal_sub="Easy to try them all."),
           dict(title="THREE BRICKS", col=Y2, sub="one more brick", big=lambda p: fmt(1060 * p) + " ways",
                bars=[("2 bricks", "24", 24 / 1060, DGREY, False), ("3 bricks", "1,060", 1.0, Y2, True)], reveal="1,060 WAYS.", reveal_sub="44 times more."),
           dict(title="SIX BRICKS", col=Y3, sub="just three more", big=lambda p: fmt(915103765 * p),
                bars=[("3 bricks", "1,060", 0.01, DGREY, False), ("6 bricks", "915,103,765", 1.0, Y3, True)], reveal="915 MILLION.", reveal_sub="1 build per second: 29 years.")],
    recap=("Ways to combine 2x4 bricks:", [("2 BRICKS", "24", Y1), ("3 BRICKS", "1,060", Y2), ("6 BRICKS", "915,103,765", Y3)], 64),
    teaser="How long light takes to reach us",
    yt_vo=["Six Lego bricks. How many ways can you build them?",
           "Take two classic two by four bricks. They fit together in twenty four different ways.",
           "Add a third brick: one thousand sixty ways.",
           "With just six bricks: nine hundred fifteen million combinations. Building one per second would take twenty nine years.",
           "Six bricks. Almost a billion builds.",
           "Next: how long does light take to reach us?"],
    tt_vo=["Six Lego bricks. How many ways?", "Two bricks: twenty four.", "Three bricks: over a thousand.", "Six bricks: nine hundred fifteen million."]))
