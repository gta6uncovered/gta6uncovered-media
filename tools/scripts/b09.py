NAME = '009 GTA 6 got delayed twice'
SOURCE = 'Rockstar via GamesRadar / Metacritic'
PROG = 1
LINES = [
    ("hook", "GTA 6 was supposed to come out in fall twenty twenty five."),
    ("d1", "Then it got pushed to May twenty sixth, twenty twenty six."),
    ("then", "But then it got delayed again."),
    ("final", "November nineteenth, twenty twenty six. Rockstar even said sorry."),
    ("score", "The result? A ninety nine on Metacritic."),
    ("ask", "So, was the wait worth it?"),
]
SHOTS = {
    "hook": [("t1", 12.3), ("t1", 32.3)],
    "d1": [("t1", 20.3), ("t1", 24.3), ("t2", 36.3)],
    "then": [("t2", 48.3)],
    "final": [("t2", 124.3), ("t2", 140.3), ("t2", 148.3)],
    "score": [("t2", 116.0), ("t2", 100.3)],
    "ask": [("t2", 152.3), ("t2", 96.3)],
}
CARDS = {
    "hook": [dict(type='strike', s='FALL 2025', y=470, size=140, at=1.6)],
    "d1": [dict(type='strike', s='MAY 26, 2026', y=470, size=120, at=2.2)],
    "then": [dict(type='text', s='DELAYED', y=450, size=140, col='r'), dict(type='text', s='AGAIN', y=590, size=120, delay=0.5)],
    "final": [dict(type='text', s='NOV 19, 2026', y=450, size=130, col='g'),
              dict(type='text', s='"sorry" — Rockstar', y=580, size=50, font='i', delay=1.8)],
    "score": [dict(type='counter', to=99, y=480, size=260, dur=1.2, delay=0.8, endcol='g'), dict(type='text', s='METACRITIC', y=660, size=64, delay=0.9)],
    "ask": [dict(type='text', s='WORTH', y=420, size=130), dict(type='text', s='THE WAIT?', y=560, size=130, col='y', delay=0.4)],
}
IMPACTS = [("then", 0.05), ("final", 0.1), ("score", 2.0)]
TICKS = [("score", 0.8, 1.2)]
DROP = "then"
