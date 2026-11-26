NAME = '017 GTA 6 still crashing PS5s'
SOURCE = 'Gizmodo 25 Nov 2026 / Beebom patch tracker 23 Nov 2026'
PROG = 0
# Hooks: 1 "Is GTA 6 crashing your PS5? You're not alone." 2 "Error CE-108255-1" 3 "The GTA 6 patch didn't fix this" 4 "Update GTA 6 now or lose your save" (too strong) 5 "GTA 6's biggest bug is still here" -> kept 1 (you + relief + stakes)
LINES = [
    ("hook", "Is GTA 6 crashing your PS5? You're not alone."),
    ("code", "Players still report error C E one oh eight two five five one, even after the patch."),
    ("patch", "Patch one point oh two point oh two fixed crashes, failed autosaves, and wanted levels you couldn't lose."),
    ("size", "It's six hundred and four megabytes on PS5. So check you're on it."),
    ("ask", "Has yours crashed yet? How many times?"),
]
SHOTS = {"hook": [("t2", 117.5, 1.4), ("t1", 25.0, 1.9)], "code": [("t3", 34.0, 1.9), ("t2", 117.5, 1.4)], "patch": [("t2", 32.0, 1.9), ("t1", 60.0, 2.0)],
         "size": [("t3", 18.0, 2.9)], "ask": [("t2", 90.0, 2.0), ("t3", 26.0, 0.9)]}
CARDS = {
    "hook": [dict(type='text', s='CRASHING?', y=470, size=170, col='r', delay=0.4)],
    "code": [dict(type='stamp', l1='STILL REPORTED AFTER PATCH', l2='CE-108255-1', y=480, col='r')],
    "patch": [dict(type='text', s='PATCH 01.002.002', y=360, size=90, col='y'), dict(type='chips', items=['CRASHES', 'AUTOSAVES', 'STUCK WANTED LEVELS'], y=500, step=0.6, bg='g')],
    "size": [dict(type='counter', to=603.8, suf=' MB', fmt='d1', y=470, size=170, dur=1.2), dict(type='text', s='ON PS5', y=620, size=70, delay=0.6)],
    "ask": [dict(type='text', s='HOW MANY', y=420, size=130), dict(type='text', s='CRASHES?', y=560, size=140, col='r', delay=0.5)],
}
IMPACTS = [("hook", 0.4), ("code", 0.1)]
TICKS = [("size", 0.0, 1.2)]
DROP = "code"
