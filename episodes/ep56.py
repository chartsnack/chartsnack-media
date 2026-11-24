import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("56", "trex_stego", dict(
    hook=[(460, "Is T. REX", 120, Y3, True), (590, "closer in time to", 76, WHITE, True), (720, "YOU", 130, Y1, True), (850, "or to Stegosaurus?", 80, WHITE, True)], pulse=2,
    steps=[dict(title="STEGOSAURUS", col=Y1, sub="Late Jurassic", big=lambda p: f"{int(150 * p)} million years ago", big_size=80,
                bars=[("Stegosaurus", "~150 million years ago", 1.0, Y1, True)], reveal="150 MILLION YEARS AGO.", reveal_sub="Long before T. rex."),
           dict(title="T. REX", col=Y2, sub="end of the Cretaceous", big=lambda p: f"{int(66 * p)} million years ago", big_size=80,
                bars=[("Stegosaurus", "150 million", 1.0, DGREY, False), ("T. rex", "66 million", 0.44, Y2, True)], reveal="66 MILLION YEARS AGO.", reveal_sub="One of the very last dinosaurs."),
           dict(title="THE GAPS", col=Y3, sub="who is closer to whom?", big=lambda p: f"{int(80 * p)}+ million years", big_size=88,
                bars=[("Stegosaurus to T. rex", "80+ million years", 1.0, Y3, True), ("T. rex to you", "66 million years", 66 / 82, DGREY, False)], reveal="T. REX IS CLOSER TO YOU.", reveal_sub="Than to Stegosaurus.")],
    recap=("Dinosaur time:", [("STEGOSAURUS", "150 My ago", Y1), ("T. REX", "66 My ago", Y2), ("CLOSER TO T. REX", "YOU", Y3)], 64),
    teaser="$5 a day for a whole lifetime",
    yt_vo=["Is T rex closer in time to you, or to Stegosaurus?",
           "Stegosaurus walked the Earth around one hundred fifty million years ago, back in the Jurassic.",
           "T rex came much later. It lived right at the end, about sixty six million years ago.",
           "So from Stegosaurus to T rex: more than eighty million years. From T rex to you: about sixty six million. T rex lived closer to us.",
           "Dinosaur time is deep time.",
           "Next: five dollars a day, for a whole lifetime."],
    tt_vo=["T rex: closer to you, or to Stegosaurus?", "Stegosaurus: a hundred fifty million years ago.", "T rex: sixty six million.", "T rex is closer to us."]))
