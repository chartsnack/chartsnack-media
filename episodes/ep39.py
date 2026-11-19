import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("39", "earth_year", dict(
    hook=[(470, "Squeeze ALL of", 84, WHITE, True), (580, "Earth's history", 90, WHITE, True), (700, "into ONE YEAR.", 110, Y3, True),
          (900, "Jan 1: Earth forms.", 56, GREY, False), (1050, "When do humans show up?", 70, Y1, True)], pulse=2,
    steps=[dict(title="DINOSAURS DIE OUT", col=Y1, sub="66 million years ago", big=lambda p: "Dec 26",
                bars=[("Days before New Year", "5.3 days", 5.3 / 365, Y1, True)], reveal="DECEMBER 26.", reveal_sub="The dinosaurs barely made Christmas."),
           dict(title="FIRST MODERN HUMANS", col=Y2, sub="~300,000 years ago", big=lambda p: "Dec 31, 23:25",
                bars=[("Minutes before midnight", "35 min", 35 / 1440, Y2, True)], reveal="35 MINUTES LEFT.", reveal_sub="On New Year's Eve."),
           dict(title="THE GREAT PYRAMID", col=Y3, sub="~4,600 years ago", big=lambda p: "23:59:28",
                bars=[("Seconds before midnight", "32 s", 32 / 3600, Y3, True)], reveal="32 SECONDS LEFT.", reveal_sub="All of written history: under a minute.")],
    recap=("Earth's history as 1 year:", [("DINOSAURS END", "Dec 26", Y1), ("FIRST HUMANS", "Dec 31, 23:25", Y2), ("THE PYRAMIDS", "23:59:28", Y3)], 60),
    teaser="Every Rubik's cube position",
    yt_vo=["Squeeze Earth's whole history into one year. When do humans appear?",
           "Earth forms on January first. The dinosaurs die out on December twenty sixth, about five days before New Year.",
           "The first modern humans? December thirty first, at about twenty five past eleven at night. Thirty five minutes before midnight.",
           "And the Great Pyramid is built just thirty two seconds before midnight. All of written history fits into the last minute of the year.",
           "Four and a half billion years. We're the last half hour.",
           "Next: every possible Rubik's cube position."],
    tt_vo=["Earth's history in one year.", "Dinosaurs die: December twenty six.", "Humans: thirty five minutes before midnight.", "Pyramids: thirty two seconds left."]))
