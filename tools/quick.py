"""Quick episode factory (2026-11-19): one spec -> YT (60.5 s) + TT (25 s) using scenes.bars_scene.
spec = dict(hook=[(y, text, size, color, bold)], pulse=idx, steps=[dict(title, col, sub, big=lambda p: str, bars=[...], reveal, reveal_sub, big_size)],
            recap=(title, rows, size), teaser, yt_vo=[7 lines], tt_vo=[5 lines])"""
import sys; sys.path.insert(0, "/home/claude/chartsnack")
from scenes import *

def build_ep(nn, slug, spec):
    s1 = hook(spec["hook"], spec.get("pulse"))
    st = [bars_scene(x["title"], x["col"], x.get("sub", ""), x["big"], x["bars"], x["reveal"], x.get("reveal_sub", ""), big_size=x.get("big_size", 104))
          for x in spec["steps"]]
    rt, rows = spec["recap"][:2]
    s5 = recap(rt, rows, size=spec["recap"][2] if len(spec["recap"]) > 2 else 72)
    v = spec["yt_vo"]; w = spec["tt_vo"]
    YT = ([("s1", s1, 4.5), ("s2", st[0], 11.0), ("s3", st[1], 12.0), ("sx", sub_scene(), 2.5), ("s4", st[2], 16.0), ("s5", s5, 9.5),
           ("s6", outro_next(spec["teaser"]), 5.0)],
          [(0, 4.5, 0.15, v[0]), (4.5, 11, 0.5, v[1]), (15.5, 12, 0.5, v[2]), (27.5, 2.5, 0.1, "Subscribe for more."),
           (30, 16, 0.5, v[3]), (46, 9.5, 0.4, v[4]), (55.5, 5, 0.4, v[5])],
          [(5.0, 12.8), (16.0, 24.8), (30.5, 42.8)],
          [0.2, 13.0, 25.0, 27.7, 43.0, 46.9, 48.1, 49.3, 55.9])
    TT = ([("s1", s1, 3.0), ("s2", st[0], 5.0), ("s3", st[1], 6.0), ("s4", st[2], 6.0), ("s5", s5, 5.0)],
          [(0, 3, 0.05, w[0]), (3, 5, 0.2, w[1]), (8, 6, 0.2, w[2]), (14, 6, 0.2, w[3]), (20, 5, 0.2, "Follow for more.")],
          [(3.5, 5.6), (8.5, 11.6), (14.5, 17.6)],
          [0.1, 5.6, 11.6, 17.6, 20.4])
    run(f"/home/claude/chartsnack/ep{nn}", f"chartsnack_ep{nn}_{slug}.mp4", YT, TT,
        [0.0, 10.5, 11.5, 1.3, 15.5, 8.5, 4.0], [0.0, 4.8, 5.8, 5.8, 4.8])
