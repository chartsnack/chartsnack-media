import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("42", "phone", dict(
    hook=[(480, "4 hours a day", 96, WHITE, True), (590, "on your phone.", 90, WHITE, True), (780, "How many YEARS", 104, Y3, True),
          (890, "of your life is that?", 70, WHITE, True), (1060, "Guess!", 110, Y1, True)], pulse=2,
    steps=[dict(title="ONE WEEK", col=Y1, sub="4 hours every day", big=lambda p: f"{28 * p:.0f} hours",
                bars=[("A full-time work week", "40 hours", 1.0, DGREY, False), ("Phone time", "28 hours", 0.7, Y1, True)], reveal="28 HOURS.", reveal_sub="More than a full day."),
           dict(title="ONE YEAR", col=Y2, sub="4 hours every day", big=lambda p: f"{61 * p:.0f} days",
                bars=[("Summer holidays", "~42 days", 42 / 61, DGREY, False), ("Phone time", "61 days", 1.0, Y2, True)], reveal="61 DAYS.", reveal_sub="Two full months, non-stop."),
           dict(title="AGE 10 TO 80", col=Y3, sub="4 hours every day for 70 years", big=lambda p: f"{11.7 * p:.1f} years",
                bars=[("School (age 6-18)", "12 years", 12 / 12, DGREY, False), ("Phone time", "11.7 years", 11.7 / 12, Y3, True)], reveal="11.7 YEARS.", reveal_sub="Awake, staring at a screen.")],
    recap=("4 hours a day on your phone:", [("ONE WEEK", "28 hours", Y1), ("ONE YEAR", "61 days", Y2), ("A LIFETIME", "11.7 years", Y3)], 64),
    teaser="$1 for every heartbeat",
    yt_vo=["Four hours a day on your phone. How many years is that?",
           "Four hours a day adds up to twenty eight hours a week. More than a full day and night.",
           "In one year: sixty one full days. Two months, around the clock.",
           "From age ten to eighty, that's almost twelve years. As long as you spent in school, but on your phone.",
           "Twenty eight hours. Two months. Twelve years.",
           "Next: one dollar for every heartbeat."],
    tt_vo=["Four hours a day on your phone.", "One week: twenty eight hours.", "One year: two full months.", "A lifetime: almost twelve years."]))
