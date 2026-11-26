NAME = '014 Real Cost Part 2 the land'
SOURCE = 'Bisnow Dec 2025 (Brickell sale) / RLB Q4 2025'
PROG = 0
TAG = 'REAL COST · PART 2'
# Hooks: 1 "In Vice City, the dirt costs more than the tower." 2 "Part 2: the 215 million answer" 3 "One acre of Vice City: 122 million" 4 "The most expensive thing in GTA 6 isn't a car" 5 "Developers don't get rich from the building" -> kept 1 (surprise contradiction)
LINES = [
    ("hook", "In Vice City, the dirt can cost more than the tower."),
    ("land", "A Brickell site sold for five twenty million, for four and a quarter acres. A hundred and twenty two million an acre."),
    ("fees", "Add twenty percent fees: twenty three million."),
    ("sum", "Total cost, two fifty nine. Sales, three twenty nine."),
    ("ask", "Seventy million profit. Would you risk it? Comment COST."),
]
SHOTS = {"hook": [("t1", 31.0, 1.9), ("t1", 13.0, 1.9)], "land": [("t2", 140.0, 1.9), ("t3", 69.0, 0.9), ("t2", 153.0, 2.5)], "fees": [("t2", 32.0, 1.9)],
         "sum": [("t1", 13.0, 1.9), ("t3", 4.6, 1.4)], "ask": [("t1", 31.0, 1.9), ("t2", 140.0, 1.9)]}
CARDS = {
    "hook": [dict(type='text', s='THE DIRT', y=420, size=150, col='y'), dict(type='text', s='> THE TOWER', y=570, size=130, delay=1.0)],
    "land": [dict(type='formula', ql='BRICKELL SALE', q='$520M', rl='/ ACRES', r='4.25', cl='= PER ACRE', c='$122M', y=360, step=1.2)],
    "fees": [dict(type='formula', ql='BUILD', q='$114M', rl='x FEES (ASSUMED)', r='20%', cl='= FEES', c='$23M', y=360)],
    "sum": [dict(type='bars', vmax=329, y=380, gap=1.4, items=[('COST', 259, 'r', '$259M'), ('SALES', 329, 'g', '$329M')])],
    "ask": [dict(type='counter', to=70, pre='+$', suf='M', y=440, size=200, dur=1.2, col='g'), dict(type='text', s='COMMENT "COST"', y=600, size=100, col='y', delay=1.4)],
}
IMPACTS = [("hook", 1.0), ("sum", 0.1)]
TICKS = [("ask", 0.0, 1.2)]
DROP = "sum"
