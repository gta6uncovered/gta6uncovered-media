NAME = '018 Series S runs GTA 6 at 720p'
SOURCE = 'Digital Foundry via GTA BOOM, 19 Nov 2026'
PROG = 1
CAP_Y = 1380
# Hooks: 1 "Playing GTA 6 on Series S? You're seeing 720p." 2 "Series S gets half the pixels of PS5" 3 "GTA 6 drops to 20 FPS on this console" 4 "The worst way to play GTA 6" 5 "Is Series S dead?" -> kept 1 (you + number)
LINES = [
    ("hook", "Playing GTA 6 on Series S? You're looking at seven twenty p."),
    ("vs", "PS5 and Series X render at fourteen forty p. That's four times the pixels."),
    ("fps", "And Digital Foundry saw Series S drop to around twenty frames in heavy action."),
    ("still", "But it runs, it's cheap, and it's the whole game."),
    ("ask", "Series S owners, upgrade or keep playing?"),
]
SHOTS = {"hook": [("t3", 18.0, 2.9), ("t1", 70.0, 1.9)], "vs": [("t1", 13.0, 1.9), ("t1", 33.0, 0.9)], "fps": [("t2", 117.5, 1.4), ("t1", 25.0, 1.9)],
         "still": [("t3", 48.0, 1.9)], "ask": [("t2", 144.0, 1.9), ("t3", 26.0, 0.9)]}
CARDS = {
    "hook": [dict(type='text', s='SERIES S', y=400, size=120), dict(type='text', s='720p', y=560, size=200, col='r', delay=1.0)],
    "vs": [dict(type='bars', vmax=4, y=400, gap=1.2, items=[('SERIES S 720p', 1, 'r', '1x'), ('PS5 / SERIES X 1440p', 4, 'g', '4x')])],
    "fps": [dict(type='counter', frm=30, to=20, suf=' FPS', y=470, size=200, dur=1.2, col='r')],
    "still": [dict(type='chips', items=['IT RUNS', 'CHEAP', 'FULL GAME'], y=440, step=0.5, bg='g')],
    "ask": [dict(type='text', s='UPGRADE', y=420, size=140, col='y'), dict(type='text', s='OR KEEP?', y=560, size=130, delay=0.5)],
}
IMPACTS = [("hook", 1.0), ("fps", 1.2)]
TICKS = [("fps", 0.0, 1.2)]
DROP = "fps"
