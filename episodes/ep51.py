import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("51", "million_or_daily", dict(
    hook=[(440, "$1 MILLION now", 96, Y1, True), (570, "or", 70, GREY, False), (700, "$1,000 a DAY", 110, Y3, True), (820, "for life?", 80, WHITE, True),
          (1000, "Pick one.", 90, WHITE, True)], pulse=4,
    steps=[dict(title="AFTER 1 YEAR", col=Y1, sub="365 days x $1,000", big=lambda p: "$" + fmt(365000 * p),
                bars=[("Lump sum", "$1,000,000", 1.0, DGREY, False), ("$1,000 a day", "$365,000", 0.365, Y1, True)], reveal="THE MILLION LEADS.", reveal_sub="For now."),
           dict(title="DAY 1,000", col=Y2, sub="2.7 years in", big=lambda p: "$" + fmt(1000000 * p),
                bars=[("Lump sum", "$1,000,000", 1.0, DGREY, False), ("$1,000 a day", "$1,000,000", 1.0, Y2, True)], reveal="IT'S A TIE.", reveal_sub="And the daily money keeps coming."),
           dict(title="AFTER 50 YEARS", col=Y3, sub="18,262 days x $1,000", big=lambda p: f"${18.26 * p:.2f} million",
                bars=[("Lump sum", "$1 million", 1 / 18.26, DGREY, False), ("$1,000 a day", "$18.26 million", 1.0, Y3, True)], reveal="18x MORE.", reveal_sub="Slow money wins.")],
    recap=("$1,000 a day vs $1 million:", [("1 YEAR", "$365,000", Y1), ("DAY 1,000", "tied", Y2), ("50 YEARS", "$18.26 million", Y3)], 64),
    teaser="A googol vs the universe",
    yt_vo=["One million dollars now, or a thousand dollars a day for life?",
           "After one year, the daily deal has paid three hundred sixty five thousand dollars. The million is still way ahead.",
           "But on day one thousand, less than three years in, it's a tie. And the daily money never stops.",
           "Keep it going for fifty years: about eighteen point two six million dollars. More than eighteen times the lump sum.",
           "Fast money versus slow money.",
           "Next: is a googol bigger than the universe?"],
    tt_vo=["A million now, or a thousand a day?", "One year: three hundred sixty five thousand.", "Day one thousand: it's a tie.", "Fifty years: eighteen million."]))
