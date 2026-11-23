NAME = '007 Lucia was in prison before GTA 6 starts'
SOURCE = "Rockstar's official Lucia page"
PROG = 2
LINES = [
    ("hook", "Lucia was in prison before GTA 6 even starts."),
    ("dad", "Her father taught her to fight."),
    ("why", "She ended up in Leonida Penitentiary after fighting for her family."),
    ("luck", "And Rockstar says she got out mostly by luck."),
    ("mom", "Her mom has dreamed of a better life ever since their days in Liberty City."),
    ("ask", "So who's the real main character? Lucia, or Jason?"),
]
SHOTS = {
    "hook": [("t2", 64.3), ("t2", 48.3), ("t1", 72.3)],
    "dad": [("t2", 92.3), ("t2", 93.6)],
    "why": [("t2", 48.3), ("t2", 64.3), ("t2", 66.0)],
    "luck": [("t2", 96.3), ("t1", 72.3)],
    "mom": [("t1", 32.3), ("t1", 12.3), ("t2", 124.3)],
    "ask": [("t2", 96.3), ("t1", 60.3)],
}
CARDS = {
    "hook": [dict(type='text', s='LUCIA', y=430, size=150, col='y'), dict(type='text', s='LOCKED UP', y=580, size=110, col='r', delay=0.6)],
    "dad": [dict(type='chips', items=['TRAINED BY HER DAD', 'FIGHTER'], y=470, size=50, step=0.6)],
    "why": [dict(type='text', s='LEONIDA', y=420, size=110), dict(type='text', s='PENITENTIARY', y=540, size=110, col='a', delay=0.3),
            dict(type='text', s='for fighting for her family', y=650, size=40, font='i', delay=1.2)],
    "luck": [dict(type='stamp', l1='RELEASED', l2='MOSTLY BY LUCK', y=480, col='g', delay=0.4),
             dict(type='text', s='according to Rockstar', y=680, size=38, font='i', delay=0.6)],
    "mom": [dict(type='text', s="MOM'S DREAM:", y=420, size=80), dict(type='text', s='A BETTER LIFE', y=530, size=100, col='y', delay=0.4),
            dict(type='chips', items=['SINCE LIBERTY CITY'], y=660, size=46, delay=2.0)],
    "ask": [dict(type='text', s='LUCIA', y=420, size=120, col='y'), dict(type='text', s='OR JASON?', y=550, size=110, delay=0.8)],
}
IMPACTS = [("hook", 0.6), ("luck", 0.4)]
TICKS = []
DROP = "luck"
