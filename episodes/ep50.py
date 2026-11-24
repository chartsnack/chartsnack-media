import sys; sys.path.insert(0, "/home/claude/chartsnack")
from quick import *
build_ep("50", "sudoku", dict(
    hook=[(480, "How many", 90, WHITE, True), (610, "SUDOKUS", 140, Y2, True), (740, "are possible?", 90, WHITE, True),
          (930, "Will we ever run out?", 62, GREY, False)], pulse=1,
    steps=[dict(title="TIC-TAC-TOE", col=Y1, sub="every possible game", big=lambda p: fmt(255168 * p),
                bars=[("Games", "255,168", 1.0, Y1, True)], reveal="255,168 GAMES.", reveal_sub="1 per second: about 3 days."),
           dict(title="CONNECT FOUR", col=Y2, sub="every possible position", big=lambda p: f"{4.53 * p:.2f} trillion",
                bars=[("Tic-tac-toe", "255,168", 0.01, DGREY, False), ("Connect Four", "4.5 trillion", 1.0, Y2, True)], reveal="4.5 TRILLION.", reveal_sub="Positions on a 7x6 board."),
           dict(title="SUDOKU", col=Y3, sub="every valid 9x9 grid", big=lambda p: f"{6.67 * p:.2f} sextillion",
                bars=[("Connect Four", "4.5 trillion", 0.01, DGREY, False), ("Sudoku grids", "6.67 sextillion", 1.0, Y3, True)], reveal="6.67 SEXTILLION.", reveal_sub="1 per second: 211 trillion years.", big_size=92)],
    recap=("How many are possible?", [("TIC-TAC-TOE", "255,168", Y1), ("CONNECT FOUR", "4.5 trillion", Y2), ("SUDOKU", "6.67 sextillion", Y3)], 64),
    teaser="$1 million now or $1,000 a day?",
    yt_vo=["How many Sudokus are possible? Will we ever run out?",
           "Start small. Tic tac toe has two hundred fifty five thousand possible games. One per second, you'd play them all in three days.",
           "Connect Four: about four and a half trillion possible positions.",
           "And Sudoku: six point six seven sextillion valid grids. Solving one per second would take two hundred eleven trillion years.",
           "Simple rules. Endless puzzles.",
           "Next: a million dollars now, or a thousand a day?"],
    tt_vo=["How many Sudokus are possible?", "Tic tac toe: two hundred fifty thousand games.", "Connect Four: four and a half trillion.", "Sudoku: six sextillion grids."]))
