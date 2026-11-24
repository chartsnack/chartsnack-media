import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("59", "light_travel", dict(
    hook=[(460, "Light is the", 80, WHITE, True), (580, "FASTEST thing.", 110, Y1, True), (720, "300,000 km per second.", 60, GREY, False),
          (920, "How long to reach us?", 80, Y3, True)], pulse=1,
    steps=[dict(title="FROM THE MOON", col=Y1, sub="384,400 km away", big=lambda p: f"{1.3 * p:.1f} seconds",
                bars=[("Moonlight", "1.3 s", 1.0, Y1, True)], reveal="1.3 SECONDS.", reveal_sub="Almost instant."),
           dict(title="FROM THE SUN", col=Y2, sub="150 million km away", big=lambda p: f"{int(500 * p) // 60} min {int(500 * p) % 60} s",
                bars=[("Moon", "1.3 s", 0.01, DGREY, False), ("Sun", "8 min 20 s", 1.0, Y2, True)], reveal="8 MINUTES 20 SECONDS.", reveal_sub="You see the Sun 8 minutes late."),
           dict(title="NEAREST STAR", col=Y3, sub="Proxima Centauri", big=lambda p: f"{4.24 * p:.2f} years",
                bars=[("Sun", "8 min 20 s", 0.01, DGREY, False), ("Proxima Centauri", "4.24 years", 1.0, Y3, True)], reveal="4.24 YEARS.", reveal_sub="And that's the closest one.")],
    recap=("Light travel time:", [("MOON", "1.3 seconds", Y1), ("SUN", "8 min 20 s", Y2), ("NEAREST STAR", "4.24 years", Y3)], 64),
    teaser="1 cent from everyone on Earth",
    yt_vo=["Light is the fastest thing. How long until it reaches us?",
           "Light from the Moon travels three hundred eighty four thousand kilometers. It arrives in just one point three seconds.",
           "Sunlight needs eight minutes and twenty seconds. You always see the Sun as it was eight minutes ago.",
           "And the nearest star, Proxima Centauri: four point two four years. That's the closest one we have.",
           "Even light needs time.",
           "Next: one cent from everyone on Earth."],
    tt_vo=["How long does light take to reach us?", "From the Moon: one second.", "From the Sun: eight minutes.", "Nearest star: four years."]))
