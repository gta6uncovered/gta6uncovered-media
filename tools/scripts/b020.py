NAME = '020 PC players found a 60 FPS GTA 6 trick'
SOURCE = 'XDA 25 Nov 2026 / Gizmodo 25 Nov 2026'
PROG = 0
# Hooks: 1 "No GTA 6 on PC? Some players found a workaround." 2 "PC gamers are playing GTA 6 at 60 FPS. Here's the catch." 3 "Rockstar still hasn't said PC" 4 "60 FPS GTA 6 without a PC port" 5 "The only legal way to play GTA 6 on PC" -> kept 2 (number + catch = open loop)
LINES = [
    ("hook", "PC players are getting GTA 6 to sixty FPS. Here's the catch."),
    ("how", "They stream it from a PS5 with Remote Play, then add frame generation on the PC."),
    ("catch", "So you still need the PS5. And the extra frames are generated, not real."),
    ("pc", "Rockstar still hasn't announced a PC version."),
    ("ask", "Would you play it like that, or wait for the real thing?"),
]
SHOTS = {"hook": [("t1", 25.0, 1.9), ("t3", 18.0, 2.9)], "how": [("t2", 32.0, 1.9), ("t1", 60.0, 2.0)], "catch": [("t3", 48.0, 1.9), ("t2", 149.0, 1.9)],
         "pc": [("t3", 38.0, 1.9)], "ask": [("t3", 26.0, 0.9), ("t2", 144.0, 1.9)]}
CARDS = {
    "hook": [dict(type='counter', to=60, suf=' FPS', y=460, size=220, dur=1.2, col='g'), dict(type='text', s='THE CATCH?', y=620, size=90, col='y', delay=1.5)],
    "how": [dict(type='chips', items=['PS5', 'REMOTE PLAY', 'PC', 'FRAME GEN'], y=440, step=0.6)],
    "catch": [dict(type='text', s='STILL NEED A PS5', y=400, size=100, col='r'), dict(type='text', s='"FAKE" FRAMES', y=540, size=110, delay=1.2)],
    "pc": [dict(type='stamp', l1='OFFICIAL PC VERSION', l2='NOT ANNOUNCED', y=480)],
    "ask": [dict(type='text', s='STREAM IT', y=420, size=130), dict(type='text', s='OR WAIT?', y=560, size=130, col='y', delay=0.5)],
}
IMPACTS = [("hook", 1.2), ("pc", 0.1)]
TICKS = [("hook", 0.0, 1.2)]
DROP = "pc"
