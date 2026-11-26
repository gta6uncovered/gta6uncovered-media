NAME = '019 Real Cost one mile of Vice City highway'
SOURCE = 'FDOT Cost Per Mile Models (U09, U11)'
PROG = 2
TAG = 'REAL COST'
# Hooks: 1 "One mile of Vice City highway costs 25.8 million dollars." 2 "Every time you drive a mile in GTA 6..." 3 "322,000 copies of GTA 6 per mile" 4 "What it costs to build the road you crash on" 5 "Highways are the most expensive thing you ignore" -> kept 2+1 merged
LINES = [
    ("hook", "Every mile you drive in Vice City would cost twenty five point eight million to build."),
    ("src", "That's Florida's price for a six lane urban interstate, before bridges and land."),
    ("lane", "Split it six ways: four point three million per lane, per mile."),
    ("copies", "That's three hundred and twenty two thousand copies of GTA 6."),
    ("ask", "Next: one Ocean Drive hotel room. Guess the price."),
]
SHOTS = {"hook": [("t1", 25.0, 1.9), ("t2", 34.6, 2.3)], "src": [("t2", 34.6, 2.3), ("t1", 31.5, 1.4)], "lane": [("t1", 25.0, 1.9)],
         "copies": [("t2", 149.0, 1.9), ("t3", 18.0, 2.9)], "ask": [("t2", 126.0, 0.9), ("t1", 33.0, 0.9)]}
CARDS = {
    "hook": [dict(type='counter', to=25.79, pre='$', suf='M', fmt='d2', y=440, size=200, dur=1.8), dict(type='text', s='PER MILE', y=600, size=90, delay=1.0)],
    "src": [dict(type='chips', items=['6 LANES', 'URBAN', 'NO BRIDGES', 'NO LAND'], y=420, step=0.5)],
    "lane": [dict(type='formula', ql='PER MILE', q='$25.79M', rl='/ LANES', r='6', cl='= PER LANE-MILE', c='$4.3M', y=360)],
    "copies": [dict(type='counter', to=322415, y=450, size=170, dur=1.6), dict(type='text', s='COPIES OF GTA 6', y=600, size=80, col='y', delay=0.8)],
    "ask": [dict(type='text', s='ONE HOTEL ROOM?', y=440, size=110, col='y'), dict(type='text', s='GUESS...', y=580, size=120, delay=0.6)],
}
IMPACTS = [("hook", 1.8), ("copies", 1.6)]
TICKS = [("copies", 0.0, 1.6)]
DROP = "copies"
