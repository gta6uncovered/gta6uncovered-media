NAME = '012 Even PS5 Pro is stuck at 30 FPS'
SOURCE = 'Digital Foundry via GTA BOOM / Kotaku via 80.lv, 19 Nov 2026'
PROG = 1
CAP_Y = 1380
# Hooks: 1 "You paid for a PS5 Pro. GTA 6 still runs at 30." 2 "No console can run GTA 6 at 60 FPS" 3 "Rockstar says the PS5 Pro isn't powerful enough" 4 "30 FPS: dealbreaker or fine?" 5 "Why GTA 6 will never be 60 FPS on PS5" -> kept 1 (you + stakes + number)
LINES = [
    ("hook", "You paid for a PS5 Pro. GTA 6 still runs at thirty."),
    ("df", "Digital Foundry: PS5, PS5 Pro and Series X all run fourteen forty p, thirty frames."),
    ("why", "Rockstar says the Pro's CPU isn't powerful enough for the game's simulation."),
    ("pro", "The Pro looks a bit better. It does not run faster."),
    ("ask", "So, thirty FPS. Dealbreaker, or doesn't matter?"),
]
SHOTS = {"hook": [("t1", 25.0, 1.9), ("t3", 18.0, 2.9)], "df": [("t1", 70.0, 1.9), ("t2", 117.5, 1.4), ("t1", 60.0, 2.0)], "why": [("t1", 22.0, 0.9), ("t2", 126.0, 0.9)],
         "pro": [("t3", 48.0, 1.9)], "ask": [("t2", 149.0, 1.9), ("t3", 69.0, 0.9)]}
CARDS = {
    "hook": [dict(type='counter', to=30, suf=' FPS', y=470, size=220, dur=1.0, delay=0.9, col='r')],
    "df": [dict(type='chips', items=['PS5', 'PS5 PRO', 'SERIES X'], y=380, step=0.4), dict(type='text', s='1440p · 30 FPS', y=560, size=110, col='y', delay=1.6)],
    "why": [dict(type='stamp', l1='ROCKSTAR ON PS5 PRO CPU', l2='"NOT POWERFUL ENOUGH"', y=480)],
    "pro": [dict(type='text', s="BETTER", y=420, size=130, col='g'), dict(type='strike', s='FASTER', y=580, size=130, at=0.9, delay=0.6)],
    "ask": [dict(type='text', s='DEALBREAKER', y=420, size=120, col='r'), dict(type='text', s='OR FINE?', y=560, size=130, col='y', delay=0.6)],
}
IMPACTS = [("hook", 0.9), ("why", 0.1)]
TICKS = [("hook", 0.9, 1.0)]
DROP = "why"
