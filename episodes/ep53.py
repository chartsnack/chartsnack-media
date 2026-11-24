import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("53", "work_hours", dict(
    hook=[(460, "40 hours a week.", 84, WHITE, True), (580, "Your whole career.", 72, GREY, False), (780, "How many YEARS", 96, Y2, True),
          (900, "of your life?", 90, WHITE, True)], pulse=2,
    steps=[dict(title="ONE YEAR", col=Y1, sub="48 weeks x 40 hours", big=lambda p: f"{fmt(1920 * p)} hours",
                bars=[("One week", "40 h", 40 / 1920, DGREY, False), ("One year", "1,920 h", 1.0, Y1, True)], reveal="1,920 HOURS.", reveal_sub="That's 80 full days."),
           dict(title="A 45-YEAR CAREER", col=Y2, sub="age 20 to 65", big=lambda p: f"{fmt(86400 * p)} hours",
                bars=[("One year", "1,920 h", 1 / 45, DGREY, False), ("Career", "86,400 h", 1.0, Y2, True)], reveal="86,400 HOURS.", reveal_sub="Same as the seconds in a day."),
           dict(title="ALL IN ONE BLOCK", col=Y3, sub="24 hours a day, no weekends", big=lambda p: f"{9.9 * p:.1f} years",
                bars=[("A life of 80 years", "80 years", 1.0, DGREY, False), ("Working nonstop", "9.9 years", 9.9 / 80, Y3, True)], reveal="9.9 YEARS.", reveal_sub="1 of every 8 years of your life.")],
    recap=("40 hours a week:", [("ONE YEAR", "1,920 hours", Y1), ("CAREER", "86,400 hours", Y2), ("NONSTOP", "9.9 years", Y3)], 64),
    teaser="$1 for every second you sleep",
    yt_vo=["Forty hours a week, your whole career. How many years is that?",
           "Forty hours a week, forty eight weeks a year: one thousand nine hundred twenty hours. Eighty full days, every year.",
           "From age twenty to sixty five: eighty six thousand four hundred hours. The same number as seconds in a day.",
           "Put it all in one block, twenty four hours a day, no weekends: almost ten years of nonstop work. One in every eight years of your life.",
           "Ten years. Make them count.",
           "Next: get paid one dollar for every second you sleep."],
    tt_vo=["Forty hours a week. How many years?", "One year: nineteen hundred hours.", "A career: eighty six thousand hours.", "Nonstop: almost ten years."]))
