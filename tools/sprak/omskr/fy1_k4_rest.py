# Fy1 kap 4: sista omgången 2026-11-17 (körs efter fy1_kap4.py, fy1_k4_newton2.py och fy1_k4_hand.py).
# Regelmässiga byten för det som återstod: obestämd form "en vikt på 3,0 kg" (bestämd form som "lådan på
# 20 kg" står kvar, den pekar ut ett föremål), "Bara … verkar", "modelleras som", "sammanlagd", "Räkna på",
# "Bortse från andra horisontella/bromsande krafter" och metatext ("I sista delen ska du …").
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

FRASER = [
    (' Jorden modelleras som sfäriskt symmetrisk.', ''),
    (' Himlakroppen modelleras som sfäriskt symmetrisk.', ''),
    (' I sista delen ska du förklara varför jämförelsen av enbart de två kraftbeloppen inte avgör månens rörelse relativt jorden.', ''),
    (' I sista delen ska du bestämma fjäderns kraft på den här kroppen.', ''),
    (' Bara tyngdkraft, normalkraft och vilofriktion verkar på klossen.', ''),
    (' Bara tyngdkraft, normalkraft och vilofriktion verkar.', ''),
    (' Bara tyngdkraft, normalkraft och glidfriktion verkar.', ' Bortse från luftmotstånd.'),
    (' Bara tyngdkraft, normalkraft och friktion verkar.', ' Bortse från luftmotstånd.'),
    (' Bara tyngdkraft och krafter från vägen verkar.', ' Bortse från luftmotstånd.'),
    (' Bara tyngdkraften verkar.', ' Bortse från luftmotstånd.'),
    (' Bara tyngdkraften och kraften från linan verkar.', ''),
    (' Bara linans dragkraft och tyngdkraften verkar vertikalt. Linan är sträckt.', ''),
    (' Endast fjäderkraften och tyngdkraften verkar.', ''),
    (' Endast snörets spännkraft och tyngdkraften verkar.', ''),
    ('Bortse från andra horisontella krafter.', 'Bortse från friktion och luftmotstånd.'),
    ('Bortse från andra bromsande krafter.', 'Bortse från luftmotstånd.'),
    ('Bortse från andra motståndskrafter.', 'Bortse från luftmotstånd.'),
    ('Bortse från andra krafter och massförlust.', 'Bortse från luftmotstånd och från att massan minskar.'),
    (' Räkna på rörelsen längs en rak, horisontell bana.', ' Planet rör sig längs en rak, horisontell bana.'),
    (' Räkna på de raka delarna av grafen.', ''),
    (' Räkna på läget när brädan är horisontell.', ' Brädan är horisontell.'),
    ('ett tåg på 2,0 · 10⁵ kg', 'ett tåg med massan 2,0 · 10⁵ kg'),
    ('Kunden lägger vikter på 3,0 kg i viktskålen.', 'Kunden lägger vikter som väger totalt 3,0 kg i viktskålen.'),
    ('ett på 35 kg vid högra', 'ett som väger 35 kg vid högra'),
    ('Ett tredje barn på 25 kg', 'Ett tredje barn som väger 25 kg'),
    ('först en på 300 kg, sedan en på 200 kg', 'först en med massan 300 kg, sedan en med massan 200 kg'),
    ('En säck potatis på 2,5 kg', 'En säck potatis som väger 2,5 kg'),
    ('En extra massa på 0,30 kg', 'En extra vikt med massan 0,30 kg'),
    ('En extra last på 300 kg', 'En extra last med massan 300 kg'),
    ('det sammanlagda momentet', 'det resulterande momentet'),
    ('Bestäm bromskraftens sammanlagda storlek i kN.', 'Bestäm den totala bromskraften.'),
    ('hur stor sammanlagd kraft som drar', 'hur stor kraft som totalt drar'),
    ('Vilken sammanlagd fjäderkonstant', 'Vilken total fjäderkonstant'),
    ('oförändrad sammanlagd massa', 'oförändrad total massa'),
    ('sammanlagda', 'totala'),
]
REGEX = [
    (r'\b([Ee]n) (hängande (?:vikt|hink|kula)|liten vikt) på (\d[\d ,]*\s?(?:kg|g))\b', r'\1 \2 med massan \3'),
    (r'\b(lång (?:planka|stege|plattform|bro|bräda|balk|stång)) på (\d[\d ,]*\s?(?:kg|g))\b', r'\1 med massan \2'),
    (r'\b(en|En) stilla massa på (\d[\d ,]*\s?(?:kg|g))\b', r'\1 vikt med massan \2'),
]

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
    raw = ' '.join(texter(u))
    alla = ' '.join(till_platshallare(x)[0] for x in texter(u))
    ers, tmp = [], alla
    for a, c in FRASER:
        if a in tmp and raw.count(a) == tmp.count(a):
            ers.append((a, c))
            tmp = tmp.replace(a, c)
    for rx, ny in REGEX:
        for m in re.finditer(rx, tmp):
            a = m.group(0)
            c = m.expand(ny)
            if raw.count(a) == alla.count(a) and not any(a == x[0] for x in ers):
                ers.append((a, c))
    if ers:
        R[u['id']] = {'ers': ers}
