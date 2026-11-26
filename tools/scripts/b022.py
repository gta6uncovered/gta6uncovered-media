NAME = '022 Real Cost one Ocean Drive hotel room'
SOURCE = 'RLB Quarterly Cost Report Q4 2025, Miami 5-star hotel'
PROG = 2
TAG = 'REAL COST · ESTIMATE'
# Hooks: 1 "One room in a Vice City luxury hotel costs up to 620,000 dollars to build." 2 "Ocean Drive hotel room: the real price" 3 "Why hotels cost twice as much as apartments" 4 "Your GTA 6 hotel room is worth a house" 5 "200 rooms, 124 million" -> kept 1
LINES = [
    ("hook", "One Vice City luxury hotel room: up to six hundred and twenty thousand dollars to build."),
    ("rate", "Miami five star hotels: four sixty to six twenty a square foot."),
    ("qty", "Two hundred rooms, a thousand square feet each, lobbies included. My assumption."),
    ("cost", "Ninety two to a hundred and twenty four million."),
    ("ask", "Double an apartment block. Would you build it? Comment COST."),
]
SHOTS = {"hook": [("t2", 126.0, 0.9), ("t1", 33.0, 0.9)], "rate": [("t2", 140.0, 1.9), ("t1", 33.0, 0.9)], "qty": [("t2", 126.0, 0.9), ("t3", 52.0, 1.9)],
         "cost": [("t1", 13.0, 1.9), ("t3", 69.0, 0.9)], "ask": [("t1", 33.0, 0.9), ("t2", 126.0, 0.9)]}
CARDS = {
    "hook": [dict(type='counter', to=620000, pre='$', y=440, size=180, dur=2.0), dict(type='text', s='PER ROOM', y=600, size=90, col='y', delay=1.2)],
    "rate": [dict(type='bars', vmax=620, y=400, gap=1.2, items=[('LOW', 460, 'y', '$460/SF'), ('HIGH', 620, 'a', '$620/SF')])],
    "qty": [dict(type='formula', ql='ROOMS', q='200', rl='x SF PER ROOM (ASSUMED)', r='1,000', cl='= AREA', c='200,000 SF', y=360)],
    "cost": [dict(type='formula', ql='AREA', q='200,000 SF', rl='x RATE', r='$460-620', cl='= BUILD COST', c='$92-124M', y=360)],
    "ask": [dict(type='text', s='2x AN APARTMENT', y=420, size=110, col='y'), dict(type='text', s='COMMENT "COST"', y=560, size=110, delay=0.6)],
}
IMPACTS = [("hook", 2.0), ("cost", 1.2)]
TICKS = [("hook", 0.0, 2.0)]
DROP = "cost"
