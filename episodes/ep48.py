import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("48", "password", dict(
    hook=[(480, "1 guess per second.", 76, WHITE, True), (640, "How long to crack", 84, WHITE, True), (770, "your PASSWORD?", 100, Y3, True),
          (960, "PIN, letters, or both?", 60, GREY, False)], pulse=2,
    steps=[dict(title="4-DIGIT PIN", col=Y1, sub="10,000 combinations", big=lambda p: f"{2.8 * p:.1f} hours",
                bars=[("All PINs", "10,000", 1.0, Y1, True)], reveal="UNDER 3 HOURS.", reveal_sub="Every single PIN, tried."),
           dict(title="8 LOWERCASE LETTERS", col=Y2, sub="26^8 = 208.8 billion options", big=lambda p: f"{fmt(6617 * p)} years",
                bars=[("4-digit PIN", "2.8 hours", 0.01, DGREY, False), ("8 letters", "6,617 years", 1.0, Y2, True)], reveal="6,600 YEARS.", reveal_sub="Longer than recorded history."),
           dict(title="a-z + A-Z + 0-9", col=Y3, sub="62^8 = 218 trillion options", big=lambda p: f"{6.9 * p:.1f} million years",
                bars=[("8 letters", "6,617 years", 0.01, DGREY, False), ("Mixed, 8 characters", "6.9 million years", 1.0, Y3, True)], reveal="6.9 MILLION YEARS.", reveal_sub="Same length. Bigger alphabet.", big_size=92)],
    recap=("1 guess per second:", [("4-DIGIT PIN", "2.8 hours", Y1), ("8 LETTERS", "6,617 years", Y2), ("MIXED", "6.9 million years", Y3)], 60),
    teaser="Counting $1 million by hand",
    yt_vo=["One guess per second. How long to crack your password?",
           "A four digit PIN has ten thousand combinations. One guess per second, and you've tried them all in under three hours.",
           "Eight lowercase letters: over two hundred billion options. That takes about six thousand six hundred years.",
           "Now mix lowercase, uppercase and numbers. Eight characters, two hundred eighteen trillion options. Almost seven million years of guessing.",
           "Same length. Bigger alphabet. Wildly longer.",
           "Next: counting one million dollars by hand."],
    tt_vo=["How long to crack your password?", "A PIN: under three hours.", "Eight letters: six thousand years.", "Add caps and numbers: seven million years."]))
