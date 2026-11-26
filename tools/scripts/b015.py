NAME = '015 Fake GTA 6 PC port warning'
SOURCE = 'XDA 25 Nov 2026 / GamesRadar 24 Nov 2026'
PROG = 1
CAP_Y = 1380
# Hooks: 1 "GTA 6 on PC already? Don't download it." 2 "This GTA 6 PC port runs at 5 FPS" 3 "Rockstar never released GTA 6 on PC" 4 "A $1,000 PC runs GTA 6 at 7 FPS" 5 "The GTA 6 PC download is a trap" -> kept 1 (warning + you)
LINES = [
    ("hook", "GTA 6 on PC already? Don't download it."),
    ("fps", "The leading fan port boots the game at five to seven frames a second, on a top end PC."),
    ("leak", "It runs on a leaked build. That's how people get scammed and hacked."),
    ("dead", "A rival port already vanished overnight."),
    ("ask", "Rockstar hasn't announced PC at all. Would you wait, or buy a console?"),
]
SHOTS = {"hook": [("t1", 69.0, 0.9), ("t2", 117.5, 1.4)], "fps": [("t1", 25.0, 1.9), ("t3", 18.0, 2.9)], "leak": [("t1", 77.0, 1.9)],
         "dead": [("t2", 117.5, 1.4)], "ask": [("t2", 149.0, 1.9), ("t3", 26.0, 0.9)]}
CARDS = {
    "hook": [dict(type='stamp', l1='GTA 6 "PC PORT"', l2="DON'T DOWNLOAD", y=480, col='r')],
    "fps": [dict(type='counter', to=7, suf=' FPS', y=440, size=220, dur=0.8, col='r'), dict(type='text', s='RX 9070 XT + 9800X3D', y=600, size=64, delay=0.6)],
    "leak": [dict(type='chips', items=['LEAKED BUILD', 'MALWARE RISK', 'SCAMS'], y=440, step=0.5)],
    "dead": [dict(type='strike', s='RIVAL PORT', y=480, size=130, at=0.8)],
    "ask": [dict(type='text', s='WAIT FOR PC', y=420, size=120), dict(type='text', s='OR CONSOLE?', y=560, size=120, col='y', delay=0.6)],
}
IMPACTS = [("hook", 0.2), ("dead", 0.8)]
TICKS = [("fps", 0.0, 0.8)]
DROP = "dead"
