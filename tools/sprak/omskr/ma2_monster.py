# Ma2: språkmönster i hela banken (2026-11-18), efter ma2_alla.py.
# - "Funktionen är f(x) = …" heter "Funktionen f ges av f(x) = …" (stilguiden).
# - "Anta" heter "Antag", "sammanlagd(a)" heter "total(a)".
# - "En elev säger/skriver …" får ett namn; "eleven/elevens" i samma uppgift byts mot namnet.
# - "digitalt verktyg": verktyget framgår av GeoGebra-taggen och skrivs inte i frågan
#   (användarbeslut 2026-11-06); "utan digitalt verktyg" heter "utan räknare".
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

NAMN = ['Alva', 'Elias', 'Maja', 'Hugo', 'Saga', 'Noah', 'Wilma', 'Leo', 'Ella', 'Oscar', 'Alice', 'Liam', 'Ebba',
        'Ali', 'Nora', 'Omar', 'Siri', 'Arvid', 'Leila', 'Viktor', 'Tilde', 'Adam', 'Freja', 'Isak', 'Juni', 'Melvin',
        'Selma', 'Theo', 'Nova', 'Malte', 'Elin', 'Sixten', 'Hanna', 'Edvin', 'Lova', 'Sami', 'Agnes', 'Vincent']
REGEX = [
    (r'Funktionen är \\\((\w)\((\w)\)=', lambda m: f'Funktionen \\({m.group(1)}\\) ges av \\({m.group(1)}({m.group(2)})='),
    (r'(?<![\w])Anta (?=[a-zåäö\\])', lambda m: 'Antag '),
    (r'(?<![\w])sammanlagda(?![\w])', lambda m: 'totala'),
    (r'(?<![\w])sammanlagd(?![\w])', lambda m: 'total'),
    (r' med (?:hjälp av )?(?:ett )?digitalt verktyg(?=[.?,])', lambda m: ''),
    (r'(?<![\w])utan digitalt verktyg', lambda m: 'utan räknare'),
    (r'<p>Använd ett digitalt verktyg\.</p>', lambda m: ''),
    (r' Använd ett digitalt verktyg\.', lambda m: ''),
]
ELEV = re.compile(r'(?:(?<=[>.?)\]] )|(?<=<p>)|(?<=\\\] ))En elev (?=[a-zåäö]+r\b)')

b = Bank('ma2')
R = {}
ni = 0
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    raw = ' '.join(falt)
    alla = ' '.join(till_platshallare(x)[0] for x in falt)
    e = []

    def lagg(a, c):
        global alla
        if a and a in alla and raw.count(a) == alla.count(a) and not any(a == x[0] for x in e):
            e.append((a, c)); alla = alla.replace(a, c)

    for rx, ny in REGEX:
        for m in list(re.finditer(rx, alla)):
            lagg(m.group(0), ny(m))
    if ELEV.search(alla):
        namn = NAMN[ni % len(NAMN)]; ni += 1
        for m in list(ELEV.finditer(alla)):
            pass
        # byt hela meningsstarten "En elev " mot namnet i alla fält
        for m in sorted(set(re.findall(r'(?:<p>|[.?)\]] )En elev [a-zåäö]+r\b', alla)), key=len, reverse=True):
            lagg(m, m.replace('En elev ', namn + ' '))
        for a, c in [('Elevens ', namn + 's '), (' elevens ', ' ' + namn + 's '), ('Eleven ', namn + ' '), (' eleven ', ' ' + namn + ' '),
                     (' eleven.', ' ' + namn + '.'), (' eleven,', ' ' + namn + ',')]:
            lagg(a, c)
    if e:
        R[u['id']] = {'ers': e}
