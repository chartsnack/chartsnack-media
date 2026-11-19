import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
N = 8.2e9
def hs(n): return n * (n - 1) / 2
build_ep("36", "handshakes", dict(
    hook=[(480, "Everyone on Earth", 88, WHITE, True), (580, "shakes hands with", 70, WHITE, True), (700, "EVERYONE ELSE.", 110, Y3, True),
          (900, "1 handshake per second.", 56, GREY, False), (1050, "How long?", 120, Y1, True)], pulse=2,
    steps=[dict(title="A PARTY OF 100", col=Y1, sub="everyone shakes everyone's hand", big=lambda p: fmt(hs(100) * p) + " shakes",
                bars=[("10 people", "45", 45 / 4950, DGREY, False), ("100 people", "4,950", 1.0, Y1, True)], reveal="4,950 HANDSHAKES.", reveal_sub="Under 2 minutes each."),
           dict(title="A CITY OF 1 MILLION", col=Y2, sub="1 handshake per second, non-stop", big=lambda p: f"{11.6 * p:.1f} days",
                bars=[("Party of 100", "99 seconds", 99 / 1e6, DGREY, False), ("1 million people", "11.6 days", 1.0, Y2, True)], reveal="11.6 DAYS. Each.", reveal_sub="Without sleeping."),
           dict(title="ALL 8.2 BILLION", col=Y3, sub="your share: 8.2 billion handshakes", big=lambda p: f"{260 * p:.0f} years",
                bars=[("A city", "11.6 days", 0.0001, DGREY, False), ("The whole world", "260 years", 1.0, Y3, True)], reveal="260 YEARS.", reveal_sub="Each. Non-stop. 33.6 quintillion shakes in total.")],
    recap=("Shake everyone's hand:", [("100 PEOPLE", "99 seconds", Y1), ("1 MILLION", "11.6 days", Y2), ("8.2 BILLION", "260 years", Y3)], 64),
    teaser="A billion minutes",
    yt_vo=["Shake hands with everyone on Earth. How long would it take?",
           "Start with a party of one hundred people. Everyone shakes everyone's hand: four thousand nine hundred fifty handshakes. Ninety nine seconds each.",
           "A city of a million people? At one handshake per second, that's eleven and a half days, non stop, for every single person.",
           "And all eight point two billion people? Two hundred sixty years each, without a break. Thirty three quintillion handshakes in total.",
           "Ninety nine seconds. Eleven days. Two hundred sixty years.",
           "Next: how long is a billion minutes?"],
    tt_vo=["Shake hands with everyone on Earth.", "A party of a hundred: ninety nine seconds.", "A city of a million: eleven days.", "Everyone on Earth: two hundred sixty years."]))
