NAME = "008 Jason's backstory in 20 seconds"
SOURCE = "Rockstar's official Jason page"
PROG = 0
LINES = [
    ("hook", "Before GTA 6, Jason was a soldier."),
    ("kid", "He grew up around grifters and crooks."),
    ("army", "Then he joined the Army, trying to get away from all that."),
    ("keys", "But after the Army, he ended up working for drug runners in the Keys."),
    ("now", "Now he's teamed up with Lucia."),
    ("ask", "Soldier to criminal. Who's the better character, Jason or Lucia?"),
]
SHOTS = {
    "hook": [("t1", 60.3), ("t2", 28.3)],
    "kid": [("t1", 24.3), ("t2", 88.3)],
    "army": [("t2", 12.3), ("t2", 16.3), ("t1", 60.3)],
    "keys": [("t2", 80.3), ("t1", 64.3), ("t2", 82.0)],
    "now": [("t2", 96.3), ("t2", 148.3)],
    "ask": [("t1", 76.3), ("t2", 152.3)],
}
CARDS = {
    "hook": [dict(type='text', s='JASON', y=430, size=150, col='y'), dict(type='text', s='EX-SOLDIER', y=580, size=110, delay=0.9)],
    "kid": [dict(type='chips', items=['GRIFTERS', 'CROOKS'], y=470, size=58, step=0.6)],
    "army": [dict(type='text', s='THE ARMY', y=480, size=140, col='g')],
    "keys": [dict(type='strike', s='SOLDIER', y=420, size=120, at=0.7),
             dict(type='text', s='DRUG RUNNERS', y=560, size=100, col='r', delay=1.6),
             dict(type='text', s='in the Leonida Keys', y=670, size=40, font='i', delay=2.2)],
    "now": [dict(type='chips', items=['JASON', '+', 'LUCIA'], y=480, size=70, step=0.4)],
    "ask": [dict(type='text', s='JASON', y=420, size=120, col='y'), dict(type='text', s='OR LUCIA?', y=550, size=110, delay=1.2)],
}
IMPACTS = [("hook", 0.9), ("keys", 1.6)]
TICKS = []
DROP = "keys"
