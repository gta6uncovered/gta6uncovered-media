NAME = '006 GTA 6 broke the streaming record'
SOURCE = 'StreamsCharts (preliminary) via GTA Boom'
PROG = 1
LINES = [
    ("hook", "Six point three eight million people watched GTA 6 streams at the same time."),
    ("old", "The old record was Valorant's closed beta in twenty twenty, at about one point seven four million."),
    ("then", "But GTA 6 didn't just beat it."),
    ("big", "It more than tripled it."),
    ("split", "YouTube had two point six six million. Twitch, two point five. Kick, one point three one."),
    ("ask", "Were you one of them? Watching, or playing?"),
]
SHOTS = {
    "hook": [("t1", 32.3), ("t1", 20.3), ("t2", 100.3)],
    "old": [("t1", 24.3), ("t2", 36.3), ("t1", 64.3)],
    "then": [("t2", 88.3)],
    "big": [("t2", 116.0), ("t2", 140.3)],
    "split": [("t2", 124.3), ("t1", 28.3), ("t2", 148.3)],
    "ask": [("t1", 60.3), ("t2", 152.3)],
}
CARDS = {
    "hook": [dict(type='counter', to=6.38, fmt='d2', suf='M', y=470, size=170, dur=1.8),
             dict(type='text', s='WATCHING AT ONCE', y=610, size=70, delay=0.3)],
    "old": [dict(type='text', s='PEAK LIVE VIEWERS', y=340, size=56),
            dict(type='bars', vmax=6.38, y=440, gap=1.4, items=[('VALORANT 2020', 1.74, 'gr', '1.74M'), ('GTA 6', 6.38, 'y', '6.38M')])],
    "then": [dict(type='text', s="DIDN'T JUST", y=450, size=110), dict(type='text', s='BEAT IT', y=580, size=130, col='y', delay=0.4)],
    "big": [dict(type='text', s='3X', y=500, size=300, col='y'), dict(type='text', s='MORE THAN TRIPLED', y=700, size=64, delay=0.3)],
    "split": [dict(type='bars', vmax=2.66, y=360, gap=1.5, items=[('YOUTUBE', 2.66, 'r', '2.66M'), ('TWITCH', 2.50, (145, 70, 255), '2.50M'), ('KICK', 1.31, 'g', '1.31M')])],
    "ask": [dict(type='text', s='WATCHING', y=440, size=110), dict(type='text', s='OR PLAYING?', y=570, size=110, col='y', delay=0.6)],
}
IMPACTS = [("hook", 1.8), ("then", 0.05), ("big", 0.1)]
TICKS = [("hook", 0, 1.8)]
DROP = "then"
