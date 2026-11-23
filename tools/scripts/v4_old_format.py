LINES = [
    ("hook", "This trailer got ninety million views in one day."),
    ("beast", "That beat Mister Beast's record for a non music YouTube video."),
    ("then", "But then Rockstar dropped trailer two."),
    ("big", "Four hundred and seventy five million views. In twenty four hours."),
    ("claim", "Rockstar called it the biggest video launch of all time."),
    ("ask", "Now the game is finally out. So, did it live up to the hype?"),
]
# shots per line: (file, start_seconds)
SHOTS = {
    "hook":  [("t1", 12.3), ("t1", 32.3)],
    "beast": [("t1", 20.3), ("t1", 64.3), ("t1", 28.3)],
    "then":  [("t2", 36.3), ("t2", 88.3)],
    "big":   [("t2", 116.0), ("t2", 140.3), ("t2", 148.3)],
    "claim": [("t2", 96.3), ("t2", 100.3)],
    "ask":   [("t2", 152.3), ("t1", 76.3)],
}
