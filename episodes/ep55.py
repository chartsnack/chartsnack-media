import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("55", "royal_flush", dict(
    hook=[(460, "1 poker hand", 90, WHITE, True), (580, "every MINUTE.", 90, Y1, True), (780, "When do you get", 76, WHITE, True),
          (900, "a ROYAL FLUSH?", 104, Y3, True)], pulse=3,
    steps=[dict(title="ALL 5-CARD HANDS", col=Y1, sub="from one 52-card deck", big=lambda p: fmt(2598960 * p),
                bars=[("Possible hands", "2,598,960", 1.0, Y1, True)], reveal="2.6 MILLION HANDS.", reveal_sub="Only 4 are royal flushes."),
           dict(title="THE ODDS", col=Y2, sub="per hand dealt", big=lambda p: "1 in " + fmt(649740 * p),
                bars=[("Royal flushes", "4", 0.01, DGREY, False), ("Odds", "1 in 649,740", 1.0, Y2, True)], reveal="1 IN 649,740.", reveal_sub="Every single hand."),
           dict(title="1 HAND PER MINUTE", col=Y3, sub="nonstop, day and night", big=lambda p: f"{fmt(451 * p)} days",
                bars=[("One day", "1,440 hands", 0.01, DGREY, False), ("Average wait", "451 days", 1.0, Y3, True)], reveal="451 DAYS.", reveal_sub="On average. No sleep.")],
    recap=("Waiting for a royal flush:", [("HANDS", "2,598,960", Y1), ("ODDS", "1 in 649,740", Y2), ("AVERAGE WAIT", "451 days", Y3)], 64),
    teaser="T. rex vs Stegosaurus",
    yt_vo=["One poker hand every minute. When do you get a royal flush?",
           "A single deck can make almost two point six million different five card hands. Only four of them are royal flushes.",
           "So your odds are one in six hundred forty nine thousand seven hundred forty. Every hand.",
           "Deal one hand per minute, day and night, no breaks. On average you'd wait four hundred fifty one days. More than a year of poker.",
           "Rarest hand. Longest wait.",
           "Next: is T rex closer to you, or to Stegosaurus?"],
    tt_vo=["A poker hand every minute.", "Two point six million hands.", "Royal flush: one in six hundred fifty thousand.", "Average wait: four hundred fifty days."]))
