NAME = '021 GTA 6 Online still has no date'
SOURCE = 'Rockstar (no date given) / Kalshi News 19 Nov 2026 (betting market)'
PROG = 1
CAP_Y = 1380
# Hooks: 1 "Waiting for GTA 6 Online? Rockstar hasn't given a date." 2 "Bettors say 70%" 3 "GTA 6 Online could be a year away" 4 "When does GTA 6 Online come out?" 5 "Rockstar is silent on GTA 6 Online" -> kept 1 (you + answer)
LINES = [
    ("hook", "Waiting for GTA 6 Online? Rockstar still hasn't given a date."),
    ("bet", "On the betting site Kalshi, traders give it about seventy percent odds of arriving before July twenty twenty seven."),
    ("note", "That's a market guess, not Rockstar."),
    ("story", "Until then, it's story mode only."),
    ("ask", "Would you play Online on day one, or stay in story mode?"),
]
SHOTS = {"hook": [("t1", 27.0, 1.9), ("t3", 46.0, 1.9)], "bet": [("t1", 70.0, 1.9), ("t2", 96.0, 1.9), ("t3", 48.0, 1.9)], "note": [("t2", 82.0, 2.5)],
         "story": [("t3", 26.0, 0.9)], "ask": [("t1", 31.0, 1.9), ("t2", 140.0, 1.9)]}
CARDS = {
    "hook": [dict(type='text', s='GTA 6 ONLINE', y=400, size=120), dict(type='text', s='NO DATE', y=550, size=170, col='r', delay=1.2)],
    "bet": [dict(type='counter', to=70, suf='%', y=440, size=220, dur=1.4), dict(type='text', s='BEFORE JULY 2027?', y=600, size=80, col='y', delay=0.8)],
    "note": [dict(type='stamp', l1='SOURCE', l2='BETTING MARKET', y=480, col='a')],
    "story": [dict(type='text', s='STORY MODE', y=440, size=140, col='y'), dict(type='text', s='ONLY', y=580, size=140, delay=0.4)],
    "ask": [dict(type='text', s='ONLINE DAY ONE', y=420, size=110, col='y'), dict(type='text', s='OR STORY?', y=560, size=130, delay=0.5)],
}
IMPACTS = [("hook", 1.2), ("note", 0.1)]
TICKS = [("bet", 0.0, 1.4)]
DROP = "note"
