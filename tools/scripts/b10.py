NAME = '010 There is no disc in the GTA 6 box'
SOURCE = 'Windows Central / Complex'
PROG = 2
LINES = [
    ("hook", "Bought GTA 6 on disc? There's no disc in the box."),
    ("code", "The physical edition is just a download code."),
    ("size", "So you still download about two hundred and ten gigabytes on PS5."),
    ("price", "Standard is seventy nine ninety nine. Ultimate is ninety nine ninety nine."),
    ("ea", "And neither one got early access."),
    ("ask", "So, disc or digital? Which one did you get?"),
]
SHOTS = {
    "hook": [("t2", 88.3), ("t2", 92.3), ("t1", 28.3)],
    "code": [("t1", 36.3), ("t2", 100.3)],
    "size": [("t2", 28.3), ("t1", 24.3), ("t2", 140.3)],
    "price": [("t1", 68.3), ("t2", 148.3), ("t1", 32.3)],
    "ea": [("t2", 116.0)],
    "ask": [("t2", 96.3), ("t2", 152.3)],
}
CARDS = {
    "hook": [dict(type='text', s='NO DISC', y=470, size=170, col='r', delay=1.3)],
    "code": [dict(type='text', s='JUST A', y=400, size=90), dict(type='text', s='CODE IN A BOX', y=520, size=110, col='y', delay=0.4)],
    "size": [dict(type='counter', to=210, suf=' GB', y=480, size=190, dur=2.0, delay=0.6), dict(type='text', s='PS5 DOWNLOAD', y=640, size=64, delay=0.6)],
    "price": [dict(type='bars', vmax=99.99, y=420, gap=1.8, items=[('STANDARD', 79.99, 'y', '$79.99'), ('ULTIMATE', 99.99, 'a', '$99.99')])],
    "ea": [dict(type='text', s='NO EARLY', y=440, size=140, col='r'), dict(type='text', s='ACCESS', y=580, size=140, delay=0.3)],
    "ask": [dict(type='text', s='DISC', y=420, size=130), dict(type='text', s='OR DIGITAL?', y=560, size=120, col='y', delay=0.5)],
}
IMPACTS = [("hook", 1.3), ("ea", 0.05)]
TICKS = [("size", 0.6, 2.0)]
DROP = "ea"
