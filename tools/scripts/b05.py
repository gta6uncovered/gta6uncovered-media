NAME = '005 GTA 6 sold 32.5 million before launch'
SOURCE = 'Take-Two via Push Square, 20 Nov 2026'
PROG = 0
LINES = [
    ("hook", "GTA 6 sold thirty two and a half million copies before it even launched."),
    ("then", "Then, on day one, it made three point seven nine billion dollars."),
    ("claim", "Take-Two calls it the biggest entertainment launch in history."),
    ("ctx", "And that's with no early access, at seventy nine ninety nine."),
    ("ask", "So, did you buy it on day one? Yes, or no?"),
]
SHOTS = {
    "hook": [("t1", 32.3), ("t2", 124.3), ("t1", 12.3)],
    "then": [("t1", 68.3), ("t2", 116.0), ("t1", 76.3)],
    "claim": [("t2", 140.3), ("t2", 100.3), ("t1", 28.3)],
    "ctx": [("t2", 148.3), ("t1", 36.3)],
    "ask": [("t2", 96.3), ("t2", 152.3)],
}
CARDS = {
    "hook": [dict(type='counter', to=32.5, fmt='d1', suf='M', y=470, size=170, dur=1.8, endcol='y'),
             dict(type='text', s='COPIES SOLD', y=610, size=70, delay=0.25),
             dict(type='text', s='BEFORE LAUNCH', y=700, size=70, col='y', delay=1.9)],
    "then": [dict(type='text', s='DAY ONE', y=360, size=80, delay=0.1),
             dict(type='counter', pre='$', to=3.79, fmt='d2', suf='B', y=500, size=170, dur=2.0, endcol='g', delay=0.6)],
    "claim": [dict(type='stamp', l1='BIGGEST ENTERTAINMENT', l2='LAUNCH IN HISTORY', y=480, delay=0.2),
              dict(type='text', s='according to Take-Two', y=680, size=38, font='i', delay=0.4)],
    "ctx": [dict(type='chips', items=['NO EARLY ACCESS', '$79.99'], y=470, size=54, step=0.9, delay=0.2)],
    "ask": [dict(type='text', s='DAY ONE?', y=440, size=120),
            dict(type='text', s='YES OR NO?', y=570, size=96, col='y', delay=0.6)],
}
IMPACTS = [("hook", 1.8), ("then", 2.6), ("claim", 0.25)]
TICKS = [("hook", 0, 1.8), ("then", 0.6, 2.0)]
DROP = "then"
