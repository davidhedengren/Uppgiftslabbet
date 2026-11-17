# Fy1 kap 4 (utom Newtons andra lag, se fy1_k4_newton2.py): handgranskning 2026-11-17. Körs EFTER fy1_kap4.py.
# Ändrat: "modell" och "modelleras som sfäriskt symmetrisk", "Bara tyngdkraft och normalkraft verkar",
# riktnings- och vinkelkonventioner (-> kgInstruktion), precisionskrav, "En elev" (namn), "Räkna med".
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

E = {
    # gravitation
    '4.9': [('En modellplanet har massan', 'En planet har massan')],
    '4.364': [('En sfäriskt symmetrisk modellplanet har radien', 'En planet har radien')],
    '4.367': [('En sfäriskt symmetrisk modellplanet har massan', 'En planet har massan')],
    '4.370': [('Två sfäriskt symmetriska modellplaneter jämförs.', 'Två planeter jämförs.')],
    '4.186': [('I denna modell går rymdstationen ISS på 420 km höjd.', 'Rymdstationen ISS går på 420 km höjd.')],
    '4.188': [('Beräkna gravitationskraften mellan fartygen enligt modellen.', 'Beräkna gravitationskraften mellan fartygen.')],
    '4.374': [(' (Svara i m/s² och avrunda till två decimaler.)', '')],
    '4.375': [(' (Svara i m/s² och avrunda till två decimaler.)', '')],
    '4.378': [(' (Svara i km och avrunda till två decimaler.)', '')],
    '4.379': [(' (Svara i km och avrunda till två decimaler.)', '')],
    '4.369': [('c) En elev säger:', 'c) Amir säger:')],
    '4.381': [('En elev vill bestämma', 'Lova vill bestämma')],
    '4.216': [('En elev säger:', 'Sixten säger:')],
    # fjädrar
    '4.18': [('En elev mäter', 'Alva mäter')],
    '4.267': [('En elev skriver:', 'Theo skriver:')],
    '4.270': [('c) En elev säger:', 'c) Ebba säger:')],
    '4.42': [('En bil modelleras med fyra vertikala ideala fjädrar, var och en med k = 25 kN/m.', 'En bil vilar på fyra vertikala fjädrar med k = 25 kN/m vardera.')],
    '4.274': [('Bestäm modellens fjäderkonstant.', 'Bestäm fjäderkonstanten.')],
    # normalkraft
    '4.21': [('En elev säger:', 'Ines säger:')],
    '4.477': [('En elev drar rakt uppåt', 'Kevin drar rakt uppåt')],
    '4.484': [('En elev med massan 65 kg tar med', 'Moa, som väger 65 kg, tar med')],
    '4.479': [(' Bara tyngdkraften och normalkraften verkar på lådan.', '')],
    '4.545': [(' Bara tyngdkraften och normalkraften verkar.', '')],
    '4.625': [(' Bara tyngdkraft och normalkraft verkar.', ' Bortse från friktion och luftmotstånd.')],
    '4.583': [(' Bara tyngdkraft, normalkraft, glidfriktion och en kraft längs planet verkar.', ''),
              (' Bara tyngdkraft, normalkraft och glidfriktion verkar.', '')],
    '4.629': [(' Bara tyngdkraft, normalkraft och vajerkraft verkar.', ' Bortse från motståndskrafter.'),
              ('Hur stor är normalkraften från vägen i N?', 'Hur stor är normalkraften från vägen?')],
    # lutande plan
    '4.26': [('I en andra modell är det vilofriktionstalet 0,10.', 'Vilofriktionstalet är i stället 0,10.')],
    '4.58': [('a) Beräkna vilket vilofriktionstal vinkeln motsvarar i den modellen.', 'a) Vilket vilofriktionstal motsvarar vinkeln?'),
             ('c) Varför kan en sådan låda inte beskriva sandkornens rörelse helt? Ge ett exempel.', 'c) Varför stämmer jämförelsen med en låda inte helt för sandkorn? Ge ett exempel.')],
    '4.104': [(' (Svara i m/s med tre värdesiffror.)', '')],
    '4.395': [('En elev säger:', 'Elias säger:')],
    '4.399': [('b) En elev anger', 'b) Tuva anger')],
    '4.617': [('Den bromsande motståndskraften modelleras som μN, där N är normalkraften.', 'Den bromsande kraften är μN, där N är normalkraften.')],
    # friktion
    '4.30': [('I en förenklad modell är glidfriktionstalen', 'Glidfriktionstalen är')],
    '4.57': [('I modellen kan hela normalkraften utnyttjas för drivning.', 'Antag att hela normalkraften kan utnyttjas för drivning.')],
    '4.450': [('En elev skriver N = mg', 'Hanna skriver N = mg')],
    '4.540': [('I modellen är den bromsande kraften i sanden konstant och lika med 0,70mg.', 'Antag att den bromsande kraften i sanden är konstant och lika med 0,70mg.')],
    '4.547': [('Motståndskraften modelleras som f = μN, där μ är oförändrat även när farten ökar.', 'Motståndskraften är f = μN, där μ inte ändras med farten.')],
    '4.554': [('En elev håller en bok', 'Malte håller en bok')],
    '4.526': [(' (Svara i hela kg.)', '')],
    '4.531': [(' (Svara i hela meter.)', '')],
    '4.535': [(' (Svara i hela sekunder.)', ''), (' (Svara i hela meter.)', '')],
    # moment
    '4.79': [(' i denna förenklade modell', '')],
    '4.191': [(' i denna modell', '')],
    '4.130': [('Var ska hantverkaren stå för att stödkrafterna ska vara lika? (Svara i m från vänstra stödet. Svara med tre värdesiffror.)',
               'Hur långt från vänstra stödet ska hantverkaren stå för att stödkrafterna ska vara lika?'),
              ('den resulterande kraften från stöden', 'den totala kraften från stöden')],
    '4.251': [(' (Svara i ton.)', '')],
    '4.453': [('c) En elev säger:', 'c) Leia säger:')],
    '4.454': [('c) En elev hävdar', 'c) Selma hävdar')],
    '4.512': [('på sammanlagt 600 kg', 'som tillsammans väger 600 kg')],
    '4.817': [('den sammanlagda normalkraften', 'den totala normalkraften')],
    # newton 1 och 3, blandat
    '4.87': [('En elev ritar en kraft framåt', 'Lukas ritar en kraft framåt')],
    '4.414': [('Räkna med att framdrivningen och motståndet är horisontella krafter.', 'Antag att framdrivningen och motståndet är horisontella.')],
    '4.500': [(' (Svara i N med en decimal.)', '')],
    '4.671': [(' (Svara i N med högst två decimaler.)', '')],
    '4.672': [(' (Svara i N med högst två decimaler.)', '')],
    '4.145': [('En elev säger att', 'Julia säger att')],
    '4.892': [('Räkna med att friktion och luftmotstånd på vagnarna är försumbara.', 'Bortse från friktion och luftmotstånd.')],
    '4.277': [('Massan är konstant i modellen.', 'Massan är konstant.')],
    '4.445': [('En elev säger att', 'Ali säger att'), ('Stämmer det i modellen?', 'Stämmer det?')],
    '4.439': [('En elev säger att', 'Noah säger att')],
}
# Riktning som rättningen behöver: (fras att ta bort, kgInstruktion)
KG = {
    '4.329': (', med höger som positiv riktning.', '.', 'Höger räknas som positiv riktning.'),
    '4.645': (' (positiv uppåt)', '', 'Uppåt räknas som positiv riktning.'),
    '4.47': (' med nedför planet som positiv riktning', '', 'Nedför planet räknas som positiv riktning.'),
    '4.392': (' Nedför är positiv riktning.', '', 'Nedför planet räknas som positiv riktning.'),
    '4.393': (' med uppför planet som positiv riktning', '', 'Uppför planet räknas som positiv riktning.'),
    '4.121': (' med nedför som positiv riktning', '', 'Nedför planet räknas som positiv riktning.'),
    '4.318': (' med nedför som positiv riktning', '', 'Nedför planet räknas som positiv riktning.'),
    '4.398': (' Räkna framåt som positivt.', '', 'Framåt räknas som positiv riktning.'),
    '4.131': (' Räkna moturs som positivt.', '', 'Moturs räknas som positiv riktning.'),
    '4.301': (' Räkna moturs som positivt.', '', 'Moturs räknas som positiv riktning.'),
    '4.453': (', med moturs som positiv riktning', '', 'Moturs räknas som positiv riktning.'),
    '4.219': (' Räkna höger som positivt och vänster som negativt.', '', 'Höger räknas som positiv riktning.'),
    '4.425': (' Räkna höger som positiv riktning.', '', 'Höger räknas som positiv riktning.'),
    '4.158': (' Räkna färdriktningen som positiv.', '', 'Färdriktningen räknas som positiv.'),
    '4.166': (' Räkna rörelseriktningen som positiv.', '', 'Rörelseriktningen räknas som positiv.'),
}
# Hela kapitlet: konventioner i kraftvektorer och "i m/s²" efter frågan.
GENERELLT_KG = [
    (' Höger och uppåt räknas som positiva riktningar.', 'Höger och uppåt räknas som positiva riktningar.'),
    (' Räkna åt höger som positiv riktning.', 'Höger räknas som positiv riktning.'),
    (r' Ange riktningen som vinkeln \(v\) från positiva x-axeln, räknad moturs (mellan 0° och 360°).',
     'Ange riktningen som vinkeln moturs från positiva x-axeln, mellan 0° och 360°.'),
    (' Ange riktningen som vinkeln från positiva x-axeln, räknad moturs (mellan 0° och 360°).',
     'Ange riktningen som vinkeln moturs från positiva x-axeln, mellan 0° och 360°.'),
]
GENERELLT_BORT = [' (Ange med tecken. Svara i kN.)', ' (Ange med tecken.)', ' (Svara med tecken.)', ' Ange med tecken.']
AXLAR = 'Axlarnas riktningar i figuren räknas som positiva.'

b = Bank('fy1')


def texter(u):
    yield u.get('t') or ''
    yield u.get('spelIntro') or ''
    for d in u.get('spelDelar') or []:
        yield d.get('t') or ''
        yield d.get('fraga') or ''


R = {}
for u in b.arr:
    if u.get('kap') != 4 and u.get('omr') != 'kraftvektorer':
        continue
    id_ = u['id']
    alla = ' '.join(texter(u))
    ers = [e for e in E.get(id_, []) if e[0] in alla]
    kg = []
    if id_ in KG:
        a, c, k = KG[id_]
        if a in alla:
            ers.append((a, c))
            kg.append(k)
    for a, k in GENERELLT_KG:
        if a in alla:
            ers.append((a, ''))
            kg.append(k)
    tecken = False
    for a in GENERELLT_BORT:
        if a in alla:
            ers.append((a, ''))
            tecken = True
    if tecken and not any('positiv' in k for k in kg):
        kg.append(AXLAR)
    if re.search(r'Bestäm accelerationen i m/s²\.', alla):
        ers.append(('Bestäm accelerationen i m/s².', 'Bestäm accelerationen.'))
    if ers or kg:
        R[id_] = {'ers': ers}
        if kg:
            k = ' '.join(dict.fromkeys(kg))
            R[id_]['kg'] = k
            dd = {(d.get('etikett') or chr(97 + i)): {'kg': k} for i, d in enumerate(u.get('spelDelar') or [])}
            if dd:
                R[id_]['d'] = dd
