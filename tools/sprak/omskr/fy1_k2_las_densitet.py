# Fy1 kap 2 genomläsning: densitet och enheter (2026-11-18).
# Ändrat: precisionskrav som inte är uppgiftens poäng ("Avrunda inte.", "(Ange svaret med tre värdesiffror.)"),
# formler i frågan (klotets och cylinderns volym), modellmeningar ("I en förenklad tidsmodell", "I modellen",
# "Räkna som om", "I beräkningen antar vi"), "En elev" och 2.55 b som förlorade sin målenhet.
# I enheter och mätnoggrannhet står avrundning kvar där den är själva uppgiften (grundpotensform, närmaste tusental).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

E = {
    '2.55': [('Ange samma densitet.', 'Ange samma densitet i kg/m³.')],
    '2.10': [('I en förenklad tidsmodell räknas ett år som exakt', 'Ett år är')],
    '2.40': [('<p>Cylinderns massa är 405 g.</p><p>Figuren visar en cylinder med diametern 4,0 cm och höjden 12 cm. Cylinderns volym ges av V = πr²h.',
              '<p>Figuren visar en cylinder med diametern 4,0 cm och höjden 12 cm. Cylinderns massa är 405 g.')],
    '2.79': [(' Volymen av ett klot är 4πr³/3.', '')],
    '2.90': [('I beräkningen antar vi att vätskornas volymer kan adderas.', 'Antag att vätskornas volymer kan adderas.'),
             ('Förklara varför modellen inte ger ett exakt recept i verkligheten.', 'Varför stämmer inte detta exakt i verkligheten?')],
    '2.86': [('I modellen är massan och den fasta materiens volym oförändrade.', 'Massan och den fasta materiens volym är oförändrade.')],
    '2.63': [('I beräkningen ökar pelarens maxkraft med dess area.', 'Pelarens maxkraft är proportionell mot dess area.')],
    '2.184': [('I en räkneuppgift antas guld kosta 340 000 kr/kg.', 'Antag att guld kostar 340 000 kr/kg.')],
    '2.195': [('Räkna jorden som ett klot', 'Antag att jorden är ett klot')],
    '2.363': [('Räkna som om varje korn är en kub', 'Antag att varje korn är en kub')],
    '2.68': [(' Avrunda endast om frågan anger det.', '')],
    '2.59': [(' Ange svaren med en decimal.', '')],
    '2.222': [(' Avrunda kvoten till två decimaler.', '')],
    '2.34': [('En elev skriver:', 'Arvid skriver:')],
    '2.41': [('En elev säger:', 'Maja säger:')],
    '2.65': [('En elev minns inte', 'Isak minns inte')],
    '2.80': [('En elev mäter', 'Filippa mäter')],
    '2.98': [('En elev säger:', 'Edvin säger:')],
    '2.99': [('En elev bestämmer densiteten', 'Alma bestämmer densiteten')],
    '2.114': [('Eleven beräknar densiteten', 'Sedan beräknas densiteten')],
    '2.193': [('En elev säger att', 'Oliver säger att')],
    '2.195_': [],
    '2.277': [('En elev beräknar medeldensiteten', 'Vera beräknar medeldensiteten')],
    '2.334': [('Då får eleven densiteten', 'Då blir den beräknade densiteten')],
}
KG = {'2.191': (' Ange en minskning med negativt tecken och en ökning med positivt tecken.', 'En minskning skrivs som ett negativt tal.')}
GENERELLT = [(' Avrunda inte.', ''), ('<br>(Ange svaret med tre värdesiffror.)', ''), (' (Ange svaren med tre värdesiffror.)', ''),
             ('Räkna med att luftens massa i hålrummet är så liten att den kan bortses från.', 'Bortse från luftens massa i hålrummet.')]
AVRUNDA_KG = [(' Avrunda till hela gram.', 'Avrunda till hela gram.'), (' Avrunda till hela kilogram.', 'Avrunda till hela kilogram.')]

b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') != 2:
        continue
    alla = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = [x for x in E.get(u['id'], []) if x[0] in alla]
    kg = None
    if u['id'] in KG and KG[u['id']][0] in alla:
        e.append((KG[u['id']][0], '')); kg = KG[u['id']][1]
    for a, c in GENERELLT:
        if a in alla:
            e.append((a, c))
    for a, k in AVRUNDA_KG:
        if a in alla:
            e.append((a, '')); kg = k
    if '2.195' == u['id']:
        for a, c in (('En elev säger att', 'Hugo säger att'),):
            if a in alla:
                e.append((a, c))
    if e or kg:
        R[u['id']] = {'ers': e}
        if kg:
            R[u['id']]['kg'] = kg
