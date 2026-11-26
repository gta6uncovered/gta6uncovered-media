NAME = '016 Real Cost Vice City 653 billion'
SOURCE = 'Cotality 2026 / Miami-Dade PA / FDOT / RLB Q4 2025'
PROG = 2
TAG = 'REAL COST · ESTIMATE'
# Hooks: 1 "Building Vice City in real life would cost 653 billion dollars." 2 "I priced Vice City like a real project" 3 "8 billion copies of GTA 6" 4 "What would Vice City cost? More than you think" 5 "Vice City in concrete: the bill" -> kept 1 (title promise + number)
LINES = [
    ("hook", "Building Vice City in real life would cost about six hundred and fifty three billion dollars."),
    ("homes", "Homes, three thirty four billion. Shops and offices, one thirty four."),
    ("roads", "Roads, sixty one. Landmarks, sixteen. Plus twenty percent fees."),
    ("copies", "That's eight billion copies of GTA 6."),
    ("ask", "Every number and source is in the full video. Higher or lower than you guessed?"),
]
SHOTS = {"hook": [("t1", 13.0, 1.9), ("t1", 31.0, 1.9)], "homes": [("t2", 149.0, 1.9), ("t2", 140.0, 1.9)], "roads": [("t2", 34.6, 2.3), ("t3", 4.6, 1.4)],
         "copies": [("t3", 69.0, 0.9)], "ask": [("t2", 153.0, 2.5), ("t1", 13.0, 1.9)]}
CARDS = {
    "hook": [dict(type='counter', to=653, pre='$', suf='B', y=460, size=220, dur=2.2)],
    "homes": [dict(type='chips', items=['HOMES $334B', 'COMMERCIAL $134B'], y=420, step=1.6, size=52)],
    "roads": [dict(type='chips', items=['ROADS $61B', 'LANDMARKS $16B', 'FEES +20%'], y=420, step=1.1, size=52)],
    "copies": [dict(type='counter', to=8.16, suf='B COPIES', fmt='d2', y=460, size=150, dur=1.2)],
    "ask": [dict(type='text', s='HIGHER', y=420, size=130, col='g'), dict(type='text', s='OR LOWER?', y=560, size=130, col='y', delay=0.6)],
}
IMPACTS = [("hook", 2.2), ("copies", 0.1)]
TICKS = [("hook", 0.0, 2.2)]
DROP = "copies"
