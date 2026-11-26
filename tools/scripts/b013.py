NAME = '013 Real Cost Part 1 one Vice City tower'
SOURCE = 'RLB Q4 2025 Miami rates / Elliman Miami Beach Q4 2025'
PROG = 2
TAG = 'REAL COST · PART 1'
# Hooks: 1 "One Vice City tower costs 114 million to build. It sells for 329." 2 "I'm a quantity surveyor. Here's what one Vice City tower really costs" 3 "Where does 215 million dollars go?" 4 "Building this tower: 114M. Selling it: 329M." 5 "Real-life price of a Vice City condo tower" -> kept 1 (two numbers + gap = open loop)
LINES = [
    ("hook", "One Vice City tower: a hundred and fourteen million to build. Three twenty nine to sell."),
    ("qty", "Forty floors, ten thousand square feet each."),
    ("rate", "At Miami's top apartment rate, two eighty five a foot: one fourteen million."),
    ("sale", "Sell eighty percent at Miami Beach prices, ten twenty seven a foot: three twenty nine million."),
    ("gap", "So where do two hundred and fifteen million go? Part two."),
]
SHOTS = {"hook": [("t1", 13.0, 1.9), ("t1", 31.0, 1.9)], "qty": [("t2", 140.0, 1.9), ("t3", 69.0, 0.9)], "rate": [("t1", 13.0, 1.9), ("t1", 22.0, 0.9)],
         "sale": [("t2", 140.0, 1.9), ("t2", 126.0, 0.9)], "gap": [("t1", 31.0, 1.9), ("t1", 13.0, 1.9)]}
CARDS = {
    "hook": [dict(type='text', s='BUILD $114M', y=400, size=120), dict(type='text', s='SELL $329M', y=540, size=130, col='y', delay=1.8)],
    "qty": [dict(type='formula', ql='FLOORS', q='40', rl='x SQ FT / FLOOR', r='10,000', cl='= AREA', c='400,000 SF', y=360)],
    "rate": [dict(type='formula', ql='AREA', q='400,000 SF', rl='x RATE (RLB)', r='$285/SF', cl='= BUILD COST', c='$114M', y=360)],
    "sale": [dict(type='formula', ql='SELLABLE (80%)', q='320,000 SF', rl='x MIAMI BEACH', r='$1,027/SF', cl='= SALES', c='$329M', y=360)],
    "gap": [dict(type='counter', to=215, pre='$', suf='M', y=450, size=200, dur=1.4), dict(type='text', s='WHERE DOES IT GO?', y=600, size=90, col='y', delay=1.0), dict(type='text', s='PART 2 TOMORROW', y=720, size=70, delay=1.8)],
}
IMPACTS = [("hook", 1.8), ("gap", 1.4)]
TICKS = [("gap", 0.0, 1.4)]
DROP = "gap"
