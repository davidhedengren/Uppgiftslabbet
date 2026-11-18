# Fy1 kap 6 och 7 genomläsning (2026-11-18).
# Regelmässigt: "Räkna med att …" heter "Antag att …" (eller "Bortse från …"), "Anta" heter "Antag",
# "enligt modellen"/"i denna modell" stryks i beräkningsfrågor och "I (en förenklad) modell …" i början
# av en mening stryks. Frågor om modellens begränsningar står kvar (det är fysikens metod, inte modellspråk).
# "En elev" får namn.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

FRASER = [
    ('Räkna med att ingen energi går till kärlet eller omgivningen.', 'Bortse från energi som går till kärlet och omgivningen.'),
    ('Räkna med samma tryckökning under båda kolvarna.', 'Tryckökningen är densamma under båda kolvarna.'),
    ('Räkna med hela lockets area.', 'Använd hela lockets area.'),
    ('Räkna med tunna väggar så att', 'Antag att väggarna är tunna, så att'),
    ('Räkna med konstant lyftkraft tills', 'Antag att lyftkraften är konstant tills'),
    ('Räkna med klotformade ballonger.', 'Antag att ballongerna är klotformade.'),
    ('Räkna med den konstanta luftdensiteten 0,80 kg/m³.', 'Antag att luftens densitet är 0,80 kg/m³ överallt.'),
    ('Bestäm modellens startacceleration.', 'Bestäm startaccelerationen.'),
    ('I denna förenklade modell räknas smältvattnet ha samma densitet som havsvattnet.', 'Antag att smältvattnet har samma densitet som havsvattnet.'),
    ('En pump kan sänka trycket ovanför en vätskepelare till noll i en förenklad modell.', 'Antag att en pump kan sänka trycket ovanför en vätskepelare till noll.'),
    ('Två förenklade modeller beskriver hur trycket ändras i vatten och luft.', ''),
    ('En modell av en ubåt har', 'En ubåt har'),
    ('Tänk dig en förenklad atmosfär där', 'Antag att'),
    ('Hur hög är atmosfären i modellen?', 'Hur hög är atmosfären?'),
    ('Beräkna modellens huvudtryck', 'Beräkna trycket vid huvudet'),
    ('Beräkna modellens övertryck', 'Beräkna övertrycket'),
    ('En första modell tar bara med tyngdkraft och lyftkraft.', 'Räkna först bara med tyngdkraft och lyftkraft.'),
    ('i den första modellen', 'i den första beräkningen'),
    ('I en förenklad modell är värmeförlusten per sekund', 'Antag att värmeförlusten per sekund är'),
    ('I en förenklad modell avger en kropp', 'Antag att en kropp'),
    ('I en förenklad modell får skillnaden', 'Antag att skillnaden'),
    ('I en modell är blodets tryck', 'Blodets tryck är'),
    ('I en modell når kraften på den en gräns vid 1,5 N.', 'Kraften på den får vara högst 1,5 N.'),
    ('det värde på isens specifika värmekapacitet som elevens modell ger', 'det värde på isens specifika värmekapacitet som Selmas beräkning ger'),
    ('det värde på isens smältvärme som modellen ger', 'det värde på isens smältvärme som beräkningen ger'),
    ('Föreslå hur försöket eller modellen kan förbättras.', 'Föreslå hur försöket eller beräkningen kan förbättras.'),
]
NAMN = {'6.29': ('En elev säger:', 'Alva säger:'), '6.33': ('En elev säger att', 'Elias säger att'),
        '6.48': ('En elev använder', 'Theo använder'), '6.79': ('En elev dividerar', 'Ella dividerar'),
        '6.80': ('En elev använder', 'Liam använder'), '6.103': ('En elev säger att', 'Moa säger att'),
        '6.108': ('En elev säger att', 'Vilma säger att'), '7.27': ('En elev säger:', 'Hugo säger:'),
        '7.63': ('En elev undersöker', 'Tilde undersöker'), '7.120': ('En elev antar', 'Selma antar'),
        '7.227': ('En elev säger att', 'Nils säger att')}
REGEX = [
    (r' (?:enligt modellen|i denna modell|i den angivna modellen|i modellen)(?=[?.])', ''),
    (r'(?<![\w])I modellen ([a-zåäö])', lambda m: m.group(1).upper()),
    (r'(?<![\w])Räkna med att ', 'Antag att '),
    (r'(?<![\w])Räkna med (?!att)', 'Antag '),
    (r'(?<![\w])Anta (?=[a-zåäöt])', 'Antag '),
]

b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') not in (6, 7):
        continue
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    e = []

    def lagg(a, c):
        global alla
        if a and a in alla and raw.count(a) == alla.count(a) and not any(a == x[0] for x in e):
            e.append((a, c)); alla = alla.replace(a, c)

    if u['id'] in NAMN:
        lagg(*NAMN[u['id']])
    for a, c in FRASER:
        lagg(a, c)
    for rx, ny in REGEX:
        for m in list(re.finditer(rx, alla)):
            if m.group(0) in alla:
                lagg(m.group(0), m.expand(ny) if isinstance(ny, str) else ny(m))
    if e:
        R[u['id']] = {'ers': e}
