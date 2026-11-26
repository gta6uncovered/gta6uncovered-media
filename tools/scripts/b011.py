NAME = '011 No Black Friday deal on GTA 6'
SOURCE = 'Beebom 25 Nov / GameRant 25 Nov 2026'
PROG = 0
# Hooks considered: 1 "Waiting for a GTA 6 Black Friday deal? Bad news." 2 "GTA 6 is NOT on sale this Black Friday" 3 "Don't wait for a GTA 6 discount" 4 "Every store skipped GTA 6 this Black Friday... almost" 5 "The only GTA 6 deal this Black Friday is in the UK" -> kept 1 (viewer + stakes)
LINES = [
    ("hook", "Waiting for a GTA 6 Black Friday deal? Bad news."),
    ("us", "In the US, there's no price cut at all."),
    ("price", "Standard is still seventy nine ninety nine. Ultimate, ninety nine ninety nine."),
    ("uk", "The one real deal is in the UK. Twenty percent off the Xbox digital code."),
    ("ask", "So did you pay full price, or are you still waiting?"),
]
SHOTS = {"hook": [("t3", 4.6, 1.4), ("t1", 33.0, 0.9)], "us": [("t2", 126.0, 0.9), ("t1", 31.5, 1.4)], "price": [("t2", 140.0, 1.9), ("t3", 18.0, 2.9)],
         "uk": [("t2", 7.0, 1.4), ("t1", 27.0, 1.9)], "ask": [("t3", 26.0, 0.9), ("t2", 144.0, 1.9)]}
CARDS = {
    "hook": [dict(type='text', s='BLACK FRIDAY?', y=430, size=130, col='y'), dict(type='text', s='BAD NEWS', y=570, size=150, col='r', delay=1.2)],
    "us": [dict(type='stamp', l1='US PRICE CUT', l2='$0.00', y=500, col='r')],
    "price": [dict(type='bars', vmax=99.99, y=400, gap=1.6, items=[('STANDARD', 79.99, 'y', '$79.99'), ('ULTIMATE', 99.99, 'a', '$99.99')])],
    "uk": [dict(type='strike', s='£69.99', y=420, size=130, at=0.7), dict(type='counter', frm=69.99, to=55.85, pre='£', fmt='d2', y=600, size=150, dur=1.4, delay=1.0, endcol='g'), dict(type='text', s='UK · XBOX DIGITAL · 20% OFF', y=730, size=50, delay=1.2)],
    "ask": [dict(type='text', s='FULL PRICE', y=420, size=120), dict(type='text', s='OR WAITING?', y=560, size=120, col='y', delay=0.5)],
}
IMPACTS = [("hook", 1.2), ("us", 0.1)]
TICKS = [("uk", 1.0, 1.4)]
DROP = "us"
