# Fy2 genomläsning (2026-11-18): modellspråk, "Anta", "Räkna med" och "En elev".
# Bohrs modell och kosmologiska modeller som fysikbegrepp står kvar; "alltså" som förklaring står kvar.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

FRASER = [
    ('Hubblekonstanten i modellen är', 'Hubblekonstanten är'),
    ('Anta Hubbles konstant', 'Använd Hubblekonstanten'),
    ('I modellen kan målvakten', 'Målvakten kan'),
    ('Anta i stället att ljudhastigheten kan approximeras med', 'Antag i stället att ljudhastigheten ges av'),
    ('Anta sfärisk spridning.', 'Antag att ljudet sprids lika mycket åt alla håll.'),
    ('Anta ljudhastigheten 1540 m/s i vävnaden.', 'Ljudhastigheten i vävnaden är 1540 m/s.'),
    ('Anta som en enkel tumregel att våglängden bör vara högst 0,50 mm.', 'Som tumregel bör våglängden vara högst 0,50 mm.'),
    ('Räkna med att ledningen är mycket lång och rak.', 'Ledningen är lång och rak.'),
    ('Använd en förenklad modell med ett homogent fält mellan två parallella metallplattor', 'Antag att fältet är homogent, som mellan två parallella metallplattor'),
    ('Anta jämn ljusstyrka', 'Antag jämn ljusstyrka'),
    ('I en förenklad modell antas en avlägsen galax följa med', 'Antag att en avlägsen galax följer med'),
    ('I en modell expanderar universum', 'Antag att universum expanderar'),
    ('Anta i en förenklad modell att avståndet', 'Antag att avståndet'),
    ('Räkna bara med den effekt som farten ger', 'Ta bara hänsyn till den effekt som farten ger'),
    ('Räkna med vinklar i radianer.', 'Räkna i radianer.'),
    ('En elev använder standardvärdet', 'Wilma använder standardvärdet'),
    ('En elev för en liten mikrofon', 'Oskar för en liten mikrofon'),
    ('En elev lägger in en platta', 'Sara lägger in en platta'),
    ('En elev undersöker inducerad spänning', 'Adam undersöker inducerad spänning'),
]

b = Bank('fy2')
R = {}
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    e = [(a, c) for a, c in FRASER if a in alla and raw.count(a) == alla.count(a)]
    if e:
        R[u['id']] = {'ers': e}
