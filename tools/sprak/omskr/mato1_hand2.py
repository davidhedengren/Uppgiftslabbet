# Ma3c: "digitalt verktyg", "Välj rätt", "Markera alla", "Ange svaret med …" och "En elev" (2026-11-19).
# Verktyget framgår av GeoGebra-taggen och skrivs inte i frågan (användarbeslut 2026-11-06).
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

REGEX = [
    (r'Använd ett digitalt verktyg för att (\w)', lambda m: m.group(1).upper()),
    (r'Använd ett digitalt verktyg och (\w)', lambda m: m.group(1).upper()),
    (r'(Bestäm|Beräkna) med digitalt verktyg ?', lambda m: m.group(1) + ' '),
    (r'utan att använda digitalt verktyg', lambda m: 'utan räknare'),
    (r'Ange svaret med (en|två|tre) decimal(er)?\.', lambda m: f'Avrunda till {m.group(1)} decimal{m.group(2) or ""}.'),
    (r'Välj rätt svar med motivering\.', lambda m: 'Motivera ditt svar.'),
]
KG_MENING = {
    ' (Markera alla riktiga alternativ.)': 'Välj alla alternativ som stämmer.',
    ' Markera alla alternativ som stämmer.': 'Välj alla alternativ som stämmer.',
    ' Skriv svaret numeriskt om det innehåller en rot.': 'Skriv svaret som ett decimaltal om det innehåller en rot.',
    'Skriv svaret numeriskt om det innehåller en rot.': 'Skriv svaret som ett decimaltal om det innehåller en rot.',
    ' Ange koefficienterna med tre decimaler och skriv endast ekvationen i svarsfältet.': 'Skriv bara ekvationen, med koefficienterna avrundade till tre decimaler.',
}
NAMN = {'4.194': ('En elev', 'Ture', 'elevens'), '4.233': ('en elev', 'Mira', None),
        '2.1129': ('en elev', 'Otto', None), '2.1149': ('en elev', 'Märta', None), '2.1207': ('en elev', 'Elsa', None)}

b = Bank('mato1')
R = {}
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    e, kg = [], []

    def lagg(a, c):
        global alla
        if a and a in alla and raw.count(a) == alla.count(a) and not any(a == x[0] for x in e):
            e.append((a, c)); alla = alla.replace(a, c)

    for rx, ny in REGEX:
        for m in list(re.finditer(rx, alla)):
            lagg(m.group(0), ny(m))
    for a, k in KG_MENING.items():
        if a in alla:
            lagg(a, ''); kg.append(k)
    if u['id'] in NAMN:
        gammal, namn, form = NAMN[u['id']]
        for m in sorted(set(re.findall(r'\b' + gammal + r' [a-zåäö]+', alla))):
            lagg(m, m.replace(gammal, namn))
        if form == 'eleven':
            lagg(' eleven ', ' ' + namn + ' ')
        if form == 'elevens':
            lagg(' elevens ', ' ' + namn + 's ')
    if e:
        R[u['id']] = {'ers': e}
        if kg:
            R[u['id']]['kg'] = ' '.join(dict.fromkeys(kg))
# 4.164: namnet i båda meningarna
R['4.164'] = {'ers': [('Första dagen läser en elev 20 sidor.', 'Första dagen läser Ronja 20 sidor.'), (' läser eleven ', ' läser Ronja ')]}
