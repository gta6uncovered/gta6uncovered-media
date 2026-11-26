# GTA 6: The Real Cost, Episode 1 - What would it cost to build Vice City in real life?
NAME = 'L01 What would it cost to build Vice City in real life'
SPEED = 1.08
SRC_RLB = 'RLB Quarterly Cost Report Q4 2025 (Miami)'
SRC_COT = 'Cotality 2026 Hurricane Risk Report'
SRC_CEN = 'US Census QuickFacts'
SRC_PA = 'Miami-Dade Property Appraiser'
SRC_FDOT = 'FDOT Cost Per Mile Models'
# Clean trailer windows (file, start, max seconds) checked on 1 fps contact sheets, 26 Nov 2026
CITY=('t1',13.0,1.9); PALMS=('t1',18.6,0.6); SWAMP=('t1',19.0,1.9); FLAMINGO=('t1',21.0,0.9); BEACH=('t1',22.0,0.9)
PORT=('t1',23.0,1.9); NCAR=('t1',25.0,1.9); STREET=('t1',27.0,1.9); NCITY=('t1',31.0,1.9); OCEAN=('t1',33.0,0.9); ODRIVE=('t2',126.0,0.9)
CAUSE=('t1',36.0,0.9); ROOF=('t1',37.0,2.5); MARINA=('t3',4.6,1.4); YACHT=('t3',9.0,1.9); SEAPL=('t3',14.0,0.9)
PLANEB=('t3',55.0,0.9); NIGHT3=('t3',69.0,0.9); KEYS=('t2',7.0,1.4); STILT=('t2',8.6,1.9); HWY=('t2',34.6,2.3)
JETSKI=('t2',140.0,1.9); NSTREET=('t2',144.0,1.9); DUSK=('t2',153.0,2.5)
def c(*shots): return dict(kind='clip', shots=list(shots))
def card(bg, els, src='', est=True): return dict(kind='card', bg=bg, els=els, src=src, est=est)
def chap(n, title, bg): return dict(kind='chapter', n=n, title=title, bg=bg)
BEATS = [
 # ---------- HOOK ----------
 ("What would it cost to build Vice City in real life?", c(CITY, NCITY)),
 ("Not in code. In concrete, steel and glass.", c(NCITY, NIGHT3)),
 ("I'm a quantity surveyor in Dubai. Pricing buildings before they exist is my actual job.", card(('t1', 38.0), [dict(t='title', s='THE REAL COST', y=380, size=120, col='y'), dict(t='sub', s='a quantity surveyor prices Vice City', y=520)], est=False)),
 ("So I priced Vice City. Real rates, real quantities, and every number on screen.", card(('t2', 154.0), [dict(t='formula', q='QUANTITY', r='RATE', c='COST', y=420)], est=False)),
 ("The answer is about six hundred and fifty billion dollars.", card(('t1', 13.6), [dict(t='counter', to=653, pre='$', suf='B', y=470, size=260, dur=2.4)])),
 ("Here is exactly how I got there, line by line, so you can check my maths.", c(OCEAN, ODRIVE)),
 ("And stay to the end, because the land number is the one that surprised me most.", c(JETSKI, DUSK)),
 # ---------- 1 RULES ----------
 ("Chapter one. The rules.", chap(1, 'THE RULES', ('t1', 18.7))),
 ("Rockstar based Vice City on Miami. So we price the real place.", c(BEACH, CITY)),
 ("Vice City squeezes the city, the beaches and the suburbs into one map, so I use all of Miami-Dade County.", card(('t1', 13.6), [dict(t='map', big=1899.9, small=36.0, bl='MIAMI-DADE COUNTY', sl='CITY OF MIAMI')], src=SRC_CEN, est=False)),
 ("For scale, the City of Miami itself is only thirty six square miles. The county is more than fifty times bigger.", card(('t1', 13.6), [dict(t='formula', q='1,900 sq mi', op='÷', r='36 sq mi', c='53x', y=420)], src=SRC_CEN, est=False)),
 ("That is one thousand nine hundred square miles, two point eight million people, and one point one million homes.", card(('t1', 22.3), [dict(t='stats', items=[('1,900', 'SQUARE MILES'), ('2.84M', 'PEOPLE'), ('1.10M', 'HOMES')], y=470)], src=SRC_CEN, est=False)),
 ("Rule one. We price the cost to build, not the price to buy. Land comes at the end.", card(('t3', 4.5), [dict(t='rule', n='1', s='BUILD COST, NOT MARKET PRICE', y=470)], est=False)),
 ("Rule two. Rates are late twenty twenty five Miami prices, from published cost reports.", card(('t3', 4.5), [dict(t='rule', n='2', s='MIAMI RATES, LATE 2025', y=470)], src=SRC_RLB, est=False)),
 ("Rule three. Where I make an assumption, I say so on screen.", card(('t3', 4.5), [dict(t='rule', n='3', s='EVERY ASSUMPTION ON SCREEN', y=470)], est=False)),
 ("And one more thing. This is an estimate, not a tender price. Real projects move with markets, contractors and luck.", card(('t3', 4.5), [dict(t='assume', s='ESTIMATE, NOT A QUOTE', y=470)], est=False)),
 # ---------- 2 HOMES ----------
 ("Chapter two. The homes.", chap(2, 'THE HOMES', ('t2', 8.5))),
 ("Homes are the biggest line in any city, so we start there.", c(KEYS, STILT)),
 ("A data firm called Cotality prices what it would cost to rebuild homes after a hurricane.", c(DUSK, KEYS)),
 ("For the Miami metro area, that is six hundred and sixteen billion dollars for two point zero four million homes.", card(('t2', 7.5), [dict(t='counter', to=616, pre='$', suf='B', y=420, size=220, dur=2.0), dict(t='sub', s='to rebuild 2.04 million homes (Miami metro)', y=590)], src=SRC_COT)),
 ("Divide one by the other, and the average home costs about three hundred and two thousand dollars to rebuild.", card(('t2', 7.5), [dict(t='formula', q='$616B', op='÷', r='2.04M homes', c='$302K', y=420)], src=SRC_COT)),
 ("That figure is what insurers use. It covers labour and materials to rebuild the house, not the land under it.", c(STILT, KEYS)),
 ("Miami-Dade has one point one zero million homes.", c(STREET, NCAR)),
 ("So, one point one zero million homes, times three hundred and two thousand dollars, equals three hundred and thirty four billion dollars.", card(('t1', 27.5), [dict(t='formula', q='1,104,711 homes', r='$302K', c='$334B', y=420)], src=SRC_COT + ' / ' + SRC_CEN)),
 ("Now a quantity surveyor never trusts one method. Let's check it a second way.", c(JETSKI, DUSK)),
 ("Assume the average home is twelve hundred square feet. That is my assumption.", card(('t1', 38.0), [dict(t='assume', s='AVERAGE HOME = 1,200 SQ FT', y=470)])),
 ("Rider Levett Bucknall puts Miami apartment buildings at one eighty five to two eighty five dollars per square foot, so I use two hundred and forty.", card(('t1', 38.0), [dict(t='range', lo=185, hi=285, pick=240, lab='MIAMI MULTIFAMILY $/SQ FT', y=430)], src=SRC_RLB)),
 ("One point three three billion square feet, times two hundred and forty dollars, is three hundred and eighteen billion.", card(('t1', 38.0), [dict(t='formula', q='1.33B sq ft', r='$240', c='$318B', y=420)], src=SRC_RLB)),
 ("Two methods, three thirty four and three eighteen. Within five percent. I'll carry the higher one.", card(('t2', 7.5), [dict(t='bars', items=[('COTALITY METHOD', 334, 'a', '$334B'), ('QS METHOD', 318, 'y', '$318B')], vmax=334, y=360)], src=SRC_COT + ' / ' + SRC_RLB)),
 ("When two independent methods land this close, an estimator starts to relax a little.", c(DUSK, KEYS)),
 # ---------- 3 SKYLINE ----------
 ("Chapter three. The skyline.", chap(3, 'THE SKYLINE', ('t1', 32.0))),
 ("Miami has sixty nine completed towers over one hundred and fifty metres tall.", card(('t1', 32.0), [dict(t='counter', to=69, y=430, size=260, dur=1.6), dict(t='sub', s='completed towers taller than 150 m', y=600)], src='Skyscraper Center definition, via Wikipedia', est=False)),
 ("Take one tower of about a million square feet. That's my assumption, roughly fifty floors.", c(PALMS, CITY)),
 ("As apartments, at the top of R L B's range, it costs two hundred and eighty five million dollars.", card(('t1', 18.7), [dict(t='formula', q='1M sq ft', r='$285', c='$285M', y=420)], src=SRC_RLB)),
 ("Spread over fifty floors, that's about five point seven million dollars for every single floor.", card(('t1', 18.7), [dict(t='formula', q='$285M', op='÷', r='50 floors', c='$5.7M', y=420)], src=SRC_RLB)),
 ("As class A offices, at up to four hundred and thirty five dollars a foot, four hundred and thirty five million.", card(('t1', 18.7), [dict(t='formula', q='1M sq ft', r='$435', c='$435M', y=420)], src=SRC_RLB)),
 ("And as a five star hotel, at up to six hundred and twenty dollars a foot, six hundred and twenty million.", card(('t1', 33.3), [dict(t='bars', items=[('APARTMENTS', 285, 'g', '$285M'), ('OFFICES', 435, 'y', '$435M'), ('5-STAR HOTEL', 620, 'a', '$620M')], vmax=620, y=320)], src=SRC_RLB)),
 ("Same size, same city, and the price more than doubles. What's inside the building drives the cost: kitchens, lifts, finishes and services.", c(OCEAN, ODRIVE)),
 ("Sixty nine towers at around three hundred and fifty million each is about twenty four billion dollars.", card(('t1', 32.0), [dict(t='formula', q='69 towers', r='~$350M', c='~$24B', y=420)], src=SRC_RLB)),
 ("But careful. Those towers are already inside our homes and our commercial lines. No double counting.", card(('t1', 32.0), [dict(t='assume', s='ALREADY COUNTED: NOT ADDED AGAIN', y=470)])),
 # ---------- 4 COMMERCIAL ----------
 ("Chapter four. Shops, offices and warehouses.", chap(4, 'SHOPS, OFFICES, WAREHOUSES', ('t1', 33.3))),
 ("The county's property appraiser values every commercial and industrial property.", c(OCEAN, ODRIVE)),
 ("Commercial is eighty seven point eight billion. Industrial is forty five point eight billion.", card(('t1', 33.3), [dict(t='bars', items=[('COMMERCIAL', 87.8, 'y', '$87.8B'), ('INDUSTRIAL', 45.8, 'a', '$45.8B')], vmax=87.8, y=360)], src=SRC_PA + ', 2025 roll')),
 ("I don't have their floor areas, so I use that value as the rebuild cost. One hundred and thirty three point six billion.", card(('t1', 33.3), [dict(t='assume', s='REBUILD = APPRAISED VALUE', y=400), dict(t='counter', to=133.6, pre='$', suf='B', fmt='d1', y=560, size=150, dur=1.6, delay=1.2)], src=SRC_PA)),
 ("That value includes land, so this line is on the high side. Flag it.", c(OCEAN, ODRIVE)),
 ("Why not use floor areas? Because nobody publishes the total floor area of every shop and warehouse in a county. When the data isn't there, you say so.", c(OCEAN, ODRIVE)),
 # ---------- 5 ROADS ----------
 ("Chapter five. Roads and bridges.", chap(5, 'ROADS AND BRIDGES', ('t2', 35.5))),
 ("Florida's transport department publishes what a mile of road costs.", c(HWY, CAUSE)),
 ("A new six lane urban interstate is twenty five point seven nine million dollars per mile. And that's before bridges or land.", card(('t1', 27.5), [dict(t='counter', to=25.79, pre='$', suf='M', fmt='d2', y=420, size=200, dur=1.8), dict(t='sub', s='per mile, 6-lane urban interstate', y=580)], src=SRC_FDOT)),
 ("A new urban arterial road is eleven point zero nine million per mile.", card(('t1', 27.5), [dict(t='counter', to=11.09, pre='$', suf='M', fmt='d2', y=420, size=200, dur=1.6), dict(t='sub', s='per mile, urban arterial road', y=580)], src=SRC_FDOT)),
 ("Split across six lanes, that's about four point three million dollars per lane, per mile.", card(('t1', 27.5), [dict(t='formula', q='$25.79M', op='÷', r='6 lanes', c='$4.3M', y=420)], src=SRC_FDOT)),
 ("Want to add just one extra lane to an urban interstate? One point four two million per mile.", card(('t1', 27.5), [dict(t='counter', to=1.42, pre='$', suf='M', fmt='d2', y=420, size=200, dur=1.4), dict(t='sub', s='per mile, one added interstate lane', y=580)], src=SRC_FDOT)),
 ("Miami-Dade County maintains about fifty five hundred miles of road.", c(STREET, NCAR)),
 ("I price every mile at the arterial rate. Fifty five hundred miles times eleven point zero nine million equals sixty one billion.", card(('t2', 35.5), [dict(t='formula', q='5,500 miles', r='$11.09M', c='$61.0B', y=420), dict(t='note', s='Assumption: all county roads at arterial rate (likely high)', y=640)], src=SRC_FDOT + ' / Miami-Dade Public Works')),
 ("And bridges are their own monster. The new I three ninety five Signature Bridge is now eight hundred and sixty six million dollars.", card(('t2', 7.5), [dict(t='counter', to=866, pre='$', suf='M', y=420, size=220, dur=1.8), dict(t='sub', s='one bridge project (I-395 Signature Bridge)', y=590)], src='Miami Today, Aug 2025')),
 # ---------- 6 AIRPORT PORT STADIUM ----------
 ("Chapter six. Airport, port and stadium.", chap(6, 'AIRPORT, PORT, STADIUM', ('t2', 35.5))),
 ("Vice City has an airport. Miami International's current modernisation plan alone is nine billion dollars.", card(('t2', 35.5), [dict(t='counter', to=9, pre='$', suf='B', y=440, size=240, dur=1.4), dict(t='sub', s='MIA modernization plan (10 years)', y=600)], src='Construction Dive, Mar 2026')),
 ("PortMiami's capital programme is three point seven five billion.", card(('t3', 4.5), [dict(t='counter', to=3.75, pre='$', suf='B', fmt='d2', y=440, size=240, dur=1.4), dict(t='sub', s='PortMiami capital program, all years', y=600)], src='Miami-Dade FY26-27 budget')),
 ("And a brand new N F L stadium, using Buffalo's new Highmark Stadium as the benchmark, is about two point one billion.", card(('t1', 23.5), [dict(t='counter', to=2.1, pre='$', suf='B', fmt='d1', y=440, size=240, dur=1.4), dict(t='sub', s='benchmark: new Highmark Stadium, Buffalo', y=600)], src='ESPN, Jun 2026')),
 ("These are floors, not full rebuilds. A whole new airport would cost far more. Flag that too.", card(('t2', 35.5), [dict(t='assume', s='LANDMARKS = MINIMUM VALUES', y=470)])),
 ("Chapter seven. The cost clock.", chap(7, 'THE COST CLOCK', ('t2', 154.0))),
 ("Here's the part nobody thinks about. Construction prices don't stand still.", c(NCAR, STREET)),
 ("R L B measured Miami construction costs rising about five percent in a year.", card(('t2', 154.0), [dict(t='counter', to=4.99, suf='%', fmt='d2', y=440, size=240, dur=1.4), dict(t='sub', s='Miami construction cost growth, 12 months', y=600)], src='RLB Construction Cost Report East, Q2 2026', est=False)),
 ("On a six hundred and fifty three billion dollar job, that's about thirty three billion dollars more for every year you wait.", card(('t2', 154.0), [dict(t='formula', q='$652.7B', r='4.99%', c='$32.6B', y=420), dict(t='note', s='Assumption: the same yearly rise continues', y=640)], src='RLB Q2 2026')),
 ("That's roughly ninety million dollars a day. Just for waiting.", card(('t2', 154.0), [dict(t='formula', q='$32.6B', op='÷', r='365 days', c='$89M', y=420)])),
 ("And a city this size would take decades to build. So the real final bill would be far bigger than today's price.", c(CAUSE, DUSK)),
 ("Chapter eight. What I left out.", chap(8, 'WHAT I LEFT OUT', ('t1', 19.5))),
 ("Every honest estimate has an exclusions list. Here's mine.", c(SWAMP, FLAMINGO)),
 ("Water, sewer and power networks. Schools, hospitals and government buildings. Parks, beaches and canals.", card(('t1', 19.5), [dict(t='chips', items=['WATER + SEWER', 'POWER GRID', 'SCHOOLS', 'HOSPITALS', 'GOV. BUILDINGS', 'PARKS', 'CANALS'], y=380)])),
 ("And the expressways, because I couldn't find a sourced mileage for them.", c(STREET, NCAR)),
 ("So the real number is higher. But the big lines, homes and commercial buildings, are in.", c(PALMS, CITY)),
 # ---------- 7 THE BILL ----------
 ("Chapter nine. The bill.", chap(9, 'THE BILL', ('t1', 13.6))),
 ("Let's add it up.", c(CITY, DUSK)),
 ("Homes, three hundred and thirty four billion. Shops, offices and warehouses, one thirty four. Roads, sixty one. Landmarks, about sixteen.", card(('t1', 13.6), [dict(t='table', rows=[('Homes', '$333.6B'), ('Commercial + industrial', '$133.6B'), ('Roads', '$61.0B'), ('Airport, port, stadium, bridge', '$15.7B')], step=1.6, y=250)], src=SRC_COT + ' / ' + SRC_PA + ' / ' + SRC_FDOT)),
 ("That's five hundred and forty four billion dollars of pure construction.", card(('t1', 13.6), [dict(t='counter', to=543.9, pre='$', suf='B', fmt='d1', y=470, size=220, dur=1.8), dict(t='sub', s='hard construction cost', y=630)])),
 ("But no project is only construction. Design, fees, permits and management add cost. I allow twenty percent. That's my assumption.", card(('t1', 13.6), [dict(t='formula', q='$543.9B', op='×', r='20%', c='$108.8B', y=420), dict(t='note', s='Assumption: 20% for design, fees and management', y=640)])),
 ("Total: six hundred and fifty three billion dollars, to build Vice City in real life.", card(('t1', 13.6), [dict(t='counter', to=652.7, pre='$', suf='B', fmt='d1', y=440, size=260, dur=2.4), dict(t='sub', s='estimated cost to build Vice City (Miami-Dade)', y=620)])),
 # ---------- 8 WHAT IT MEANS ----------
 ("Chapter ten. What that money means.", chap(10, 'WHAT IT MEANS', ('t1', 18.7))),
 ("At seventy nine ninety nine, that's eight point one six billion copies of GTA 6.", card(('t1', 33.3), [dict(t='counter', to=8.16, suf='B', fmt='d2', y=420, size=240, dur=1.8), dict(t='sub', s='copies of GTA 6 at $79.99', y=590)])),
 ("Or about two hundred and thirty thousand dollars for every single person who lives there.", card(('t1', 22.3), [dict(t='counter', to=229937, pre='$', y=430, size=200, dur=2.0), dict(t='sub', s='per Miami-Dade resident', y=590)], src=SRC_CEN)),
 ("That's roughly the cost of rebuilding one average home, for every man, woman and child.", c(KEYS, STILT)),
 ("And remember, that's only to build it. To buy it, you'd need the land.", c(JETSKI, DUSK)),
 ("The property appraiser values Miami-Dade, land included, at seven hundred and seventy three billion dollars.", card(('t1', 38.0), [dict(t='bars', items=[('OUR BUILD ESTIMATE', 652.7, 'y', '$653B'), ('MARKET VALUE INC. LAND', 773.4, 'a', '$773B')], vmax=773.4, y=360)], src=SRC_PA + ', 2026 preliminary roll')),
 ("A sanity check every quantity surveyor loves. Our build cost sits below market value, exactly where it should.", c(NCITY, NIGHT3)),
 ("If our estimate had come out above market value, I'd know I made a mistake somewhere.", c(NCITY, NIGHT3)),
 ("And land is the wild card. One Brickell site just sold for five hundred and twenty million dollars for four and a quarter acres.", card(('t1', 18.7), [dict(t='formula', q='$520M', op='÷', r='4.25 acres', c='$122M/acre', y=420)], src='Bisnow, Dec 2025')),
 ("So in Vice City, the dirt under the towers can cost more than the towers.", c(CITY, NCITY)),
 ("Here in Dubai we see the same thing on the best plots. Location is priced before a single block is laid.", c(CITY, DUSK)),
 ("Quick recap. Homes, three hundred and thirty four billion. Commercial, one thirty four. Roads, sixty one. Landmarks, sixteen. Plus twenty percent. Six hundred and fifty three billion.", card(('t1', 13.6), [dict(t='table', rows=[('Homes', '$333.6B'), ('Commercial + industrial', '$133.6B'), ('Roads', '$61.0B'), ('Landmarks', '$15.7B'), ('Fees + design (20%)', '$108.8B'), ('TOTAL', '$652.7B')], step=1.4, y=200)])),
 ("Next episode, I price the rest of Leonida.", c(SWAMP, FLAMINGO)),
 ("So tell me. Did you think it would cost more, or less? Comment COST, and I'll pin the full breakdown.", card(('t1', 32.0), [dict(t='title', s='MORE OR LESS?', y=400, size=130, col='y'), dict(t='sub', s='Comment COST for the full breakdown', y=540)], est=False)),
]
THUMB = dict(f='t1', s=13.6, l1='REAL VICE CITY', l2='$653B', tag='ESTIMATE')
