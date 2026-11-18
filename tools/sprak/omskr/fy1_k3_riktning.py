# Fy1 kap 3: riktningar, tecken och precision, 2026-11-18 (körs efter fy1_kap3.py).
# Lärarens prov skriver aldrig "positiv riktning" eller "med tecken". Riktningsval flyttas till kgInstruktion
# (huvuduppgift och alla delkort), teckenuppmaningar och precisionskrav tas bort. Meningar där
# riktningen beskriver själva situationen skrivs om utan "positiv riktning" (EXTRA).
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare, fran_platshallare

EXTRA = {
    '3.244': [('Ett nytt koordinatsystem har samma positiva riktning men nollpunkten 5 m längre fram.', 'Ett nytt koordinatsystem pekar åt samma håll men har nollpunkten 5 m längre fram.')],
    '3.56': [('Låt s beteckna läge, med rörelsen från start mot 6 m som positiv riktning.', 'Läget s mäts från starten i riktning mot 6 m.')],
    '3.112': [('och kör i positiv riktning.', 'och kör åt samma håll.')],
    '3.141': [('Bilen kör hela tiden längs samma raka linje i positiv riktning.', 'Bilen kör hela tiden framåt längs samma raka väg.')],
    '3.385': [('B ligger 40,0 m i positiv riktning från A.', 'B ligger 40,0 m framför A.')],
    '3.41': [('Rörelsen sker i positiv riktning under hela förloppet.', 'Cyklisten rör sig hela tiden framåt.')],
    '3.226': [('accelererar A med +2,0 m/s² och B med −4,0 m/s², med öster som positiv riktning.', 'accelererar A med 2,0 m/s² österut och B med 4,0 m/s² västerut.')],
    '3.426': [('Läget x = 0 är vid bryggan och positiv riktning är bort från den.', 'Läget x = 0 är vid bryggan och x ökar bort från den.')],
    '3.427': [('Läget mäts längs rampen, med positiv riktning uppåt.', 'Läget mäts längs rampen och ökar uppåt.')],
    '3.444': [(' Diagrammet visar hastigheten med tecken.', '')],
}
KG_EXTRA = {'3.226': 'Öster räknas som positiv riktning.'}
SITUATION = [(r'(En vagn rör sig åt höger), som är positiv riktning\.', r'\1.', 'Höger räknas som positiv riktning.'),
             (r'(En cyklist rör sig framåt), som är positiv riktning\.', r'\1.', 'Framåt räknas som positiv riktning.')]

RIKT = [  # (regex, gruppnummer för riktningen) — hela meningen tas bort
    (r' ?(?<![\w])Välj ([^.<>]{2,50}?) som positiv(?: riktning|t)? och (bortse från [^.<>]+)\.', 1),
    (r' ?(?<![\w])Välj ([^.<>]{2,50}?) som positiv(?: riktning|t)?\.', 1),
    (r' ?(?<![\w])Räkna ([^.<>]{2,40}?) som positiv(?: riktning|t)?\.', 1),
    (r' ?(?<![\w])([A-ZÅÄÖ][a-zåäö]+(?: [a-zåäö]+){0,3}) (?:är|räknas som) positiv(?: riktning|t)?\.', 1),
]
I_FRAGA = r',? med ((?:den |det )?[a-zåäö]+(?: [a-zåäö]+){0,2}?) (?:som )?positiv(?:t| riktning)?(?=[.?,])'
BORT = [r' ?\((?:Svara|Ange)[^()]*?(?:tecken|tecknet|decimal|värdesiffr|avrunda)[^()]*\)',
        r' ?\(Svara i (?:s|m|m/s|s och m|s från starten|s från t = 0)\.\)',
        r' ?Ange med tecken\.', r',? med tecken och två decimaler', r',? med tecken(?=[.?])']
SAMMAN = [('Bestäm sammanlagda sträckan.', 'Bestäm hela sträckan.'), ('den sammanlagda körsträckan', 'den totala körsträckan'),
          ('mellan sammanlagda sträckan', 'mellan den totala sträckan')]
ENHET = [(r'(Bestäm [^.?]{3,60}?) i (?:m/s²|m/s|m)(?=[.?])', r'\1')]  # SI-enhet efter frågan, när tecknet togs bort


def kg_text(x):
    x = x.strip()
    if x.endswith(('riktningen', 'riktning')):
        return x[0].upper() + x[1:] + ' räknas som positiv.'
    return x[0].upper() + x[1:] + ' räknas som positiv riktning.'


b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') != 3:
        continue
    id_ = u['id']
    falt = [u.get('t'), u.get('spelIntro')] + [x for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    alla = ' '.join(till_platshallare(x)[0] for x in falt if x)
    ers, kg = [], []

    def lagg(a, c):
        global alla
        if a and a in alla and not any(a == e[0] for e in ers):
            ers.append((a, c))
            alla = alla.replace(a, c)

    for a, c in EXTRA.get(id_, []):
        lagg(a, c)
    if id_ in KG_EXTRA:
        kg.append(KG_EXTRA[id_])
    for rx, ny, k in SITUATION:
        m = re.search(rx, alla)
        if m:
            lagg(m.group(0), m.expand(ny)); kg.append(k)
    for rx, g in RIKT:
        for m in list(re.finditer(rx, alla)):
            if m.group(0) not in alla:
                continue
            ny = ''
            if m.re.groups >= 2:  # "Välj X som positiv riktning och bortse från …"
                ny = ' ' + m.group(2)[0].upper() + m.group(2)[1:] + '.'
            kg.append(kg_text(m.group(g)))
            lagg(m.group(0), ny)
    for m in list(re.finditer(I_FRAGA, alla)):
        if m.group(0) in alla:
            kg.append(kg_text(m.group(1)))
            lagg(m.group(0), '')
    for rx in BORT:
        for m in list(re.finditer(rx, alla)):
            lagg(m.group(0), '')
    for a, c in SAMMAN:
        lagg(a, c)
    for rx, ny in ENHET:
        for m in list(re.finditer(rx, alla)):
            if any(e[0].startswith(',') or 'tecken' in e[0] for e in ers):
                lagg(m.group(0), m.expand(ny))
    if not ers and not kg:
        continue
    # byt på platshållartexten så att figurer inte ändras
    def byt(x):
        t = till_platshallare(x)[0]
        for a, c in ers:
            t = t.replace(a, c)
        return t
    post = {}
    if u.get('t') and byt(u['t']) != till_platshallare(u['t'])[0]:
        post['t'] = byt(u['t'])
    if u.get('spelIntro') is not None and byt(u['spelIntro']) != till_platshallare(u['spelIntro'])[0]:
        post['intro'] = byt(u['spelIntro'])
    k = ' '.join(dict.fromkeys(kg)) if kg else None
    dd = {}
    for i, d in enumerate(u.get('spelDelar') or []):
        et = d.get('etikett') or chr(97 + i)
        q = {}
        if d.get('t') and byt(d['t']) != till_platshallare(d['t'])[0]:
            q['t'] = byt(d['t'])
        if d.get('fraga') and byt(d['fraga']) != till_platshallare(d['fraga'])[0]:
            q['f'] = fran_platshallare(byt(d['fraga']), till_platshallare(d['fraga'])[1], id_)
            if d.get('t') and 't' not in q:
                q['t'] = till_platshallare(d['t'])[0]
        if k:
            q['kg'] = k
        if q:
            dd[et] = q
    if dd:
        post['d'] = dd
    if k:
        post['kg'] = k
    if post:
        R[id_] = post
