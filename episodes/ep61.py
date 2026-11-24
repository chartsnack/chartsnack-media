import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("61", "atoms_body", dict(
    hook=[(460, "How many ATOMS", 96, Y2, True), (580, "are in YOUR body?", 84, WHITE, True), (780, "Could you", 80, WHITE, True),
          (900, "COUNT them?", 120, Y3, True)], pulse=3,
    steps=[dict(title="YOUR BODY", col=Y1, sub="about 70 kg, estimate", big=lambda p: f"{7 * p:.1f} octillion",
                bars=[("Atoms", "about 7 x 10^27", 1.0, Y1, True)], reveal="7 OCTILLION.", reveal_sub="A 7 with 27 zeros."),
           dict(title="1 ATOM PER SECOND", col=Y2, sub="nonstop counting", big=lambda p: f"{220 * p:.0f} quintillion years", big_size=80,
                bars=[("One year", "31.6 million atoms", 0.01, DGREY, False), ("All of them", "220 quintillion years", 1.0, Y2, True)], reveal="220 QUINTILLION YEARS.", reveal_sub="Just to count you."),
           dict(title="VS THE UNIVERSE", col=Y3, sub="13.8 billion years old", big=lambda p: f"{16 * p:.0f} billion times",
                bars=[("Age of the universe", "13.8 billion years", 0.01, DGREY, False), ("Counting your atoms", "16 billion x longer", 1.0, Y3, True)], reveal="16 BILLION TIMES.", reveal_sub="The age of the universe.")],
    recap=("Atoms in you:", [("ATOMS", "~7 octillion", Y1), ("COUNTING", "220 quintillion y", Y2), ("VS UNIVERSE", "16 billion x", Y3)], 64),
    teaser="A new chart snack tomorrow",
    yt_vo=["How many atoms are in your body? Could you count them?",
           "A seventy kilo human is made of about seven octillion atoms. That's a seven with twenty seven zeros.",
           "Count one atom per second, nonstop. You'd need about two hundred twenty quintillion years.",
           "That's sixteen billion times the age of the universe. Just to count yourself.",
           "Tiny atoms. Unimaginable numbers.",
           "See you at the next chart snack."],
    tt_vo=["How many atoms are in your body?", "About seven octillion.", "Counting them: quintillions of years.", "Sixteen billion times the universe."]))
