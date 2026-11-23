"""Hitta uppgifter som kan vara konstiga (2026-11-23). Bara en lista att läsa för hand, ändrar inget.

Flaggar: hänvisning till figur/tabell som saknas, kvarglömda platshållare, text utan fråga eller uppmaning,
mycket lång text, upprepad mening, dubbelord, numeriskt svar som inte står i facits svarsrad (5 %, tiopotenser
tolkas), delkort som hänvisar bakåt, negativt svar på ”Hur stor …”.

  python tools/sprak/konstigt.py fy2 [omr ...] > ut.txt
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprakverktyg import Bank  # noqa: E402

SMALA = '    '
UPPMANING = (r'\?|\b(Beräkna|Bestäm|Ange|Visa|Förklara|Rita|Lös|Skriv|Motivera|Beskriv|Uppskatta|Ta fram|Avgör|'
             r'Jämför|Undersök|Härled|Skissa|Teckna|Förenkla|Derivera|Integrera|Faktorisera|Fyll|Markera|Para|Ordna|'
             r'Ge|Gör|Använd|Välj|Pröva|Kontrollera|Utveckla|Dividera|Multiplicera|Konstruera|Tolka|Diskutera|'
             r'Resonera|Placera|Sortera|Formulera|Uttryck|Bevisa|Hitta|Läs|Räkna)\b')


def syn(h):
    h = re.sub(r'<svg.*?</svg>|<table.*?</table>', ' [FIG] ', h or '', flags=re.S)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()


def tal(s):
    s = s.replace('{,}', ',').replace('\\,', '').replace('−', '-')
    for c in SMALA:
        s = s.replace(c, '')
    s = re.sub(r'(\d+(?:,\d+)?)(?:\\cdot|·)10\^\{?(-?\d+)\}?',
               lambda m: m.group(1).replace(',', '.') + 'e' + m.group(2), s)
    return [float(x.replace(',', '.')) for x in re.findall(r'-?\d+(?:[.,]\d+)?(?:e-?\d+)?', s)]


def svarsrad(s):
    m = re.search(r'class="facit-svar"[^>]*>(.*?)</p>', s or '', re.S)
    return syn(m.group(1)) if m else ''


def nara(v, lista, rel=0.05):
    for x in lista:
        if v == 0 and abs(x) < 1e-9:
            return True
        if v != 0 and abs(x - v) <= rel * abs(v) + 1e-12:
            return True
        for e in (-9, -6, -3, -2, 2, 3, 6, 9):  # enhetsbyte i svarsraden (km, mm, kN …)
            if v != 0 and abs(x * 10 ** e - v) <= rel * abs(v):
                return True
    return False


def kolla(u):
    fynd = []
    t = u.get('t') or ''
    vt = syn(t)
    delar = u.get('spelDelar') or []
    harfig = bool(re.search(r'<svg|<img|<table', t + (u.get('spelIntro') or '')))
    if re.search(r'\b(figuren|bilden|tabellen|diagrammet|grafen)\b', vt, re.I) and not harfig:
        fynd.append('hänvisar till figur/tabell som saknas')
    utan_matte = re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', '', vt)
    for m in re.finditer(r'\b(?:undefined|None|NaN|nan|TODO|XXX)\b|[{}]|\[F\d\]|\?\?', utan_matte):
        fynd.append(f'platshållare {m.group(0)!r}')
    if not re.search(UPPMANING, vt):
        fynd.append('ingen fråga eller uppmaning')
    if len(vt) > 900:
        fynd.append(f'lång text ({len(vt)} tecken)')
    meningar = [m.strip() for m in re.split(r'(?<=[.?!])\s', vt) if len(m.strip()) > 25]
    dubb = {m for m in meningar if meningar.count(m) > 1}
    if dubb and not delar:
        fynd.append('upprepad mening: ' + next(iter(dubb))[:80])
    m = re.search(r'\b(\w{3,}) \1\b', vt)
    if m:
        fynd.append('dubbelord: ' + m.group(0))
    if u.get('svarstyp') == 'numeriskt' and isinstance(u.get('rättSvar'), (int, float)) and not delar:
        sr = svarsrad(u.get('s'))
        if sr and not nara(float(u['rättSvar']), tal(sr)):
            fynd.append(f'svar {u["rättSvar"]} saknas i facits svarsrad: {sr[:80]}')
    for d in delar:
        if d.get('svarstyp') == 'numeriskt' and isinstance(d.get('rättSvar'), (int, float)):
            sr = svarsrad(d.get('s'))
            if sr and not nara(float(d['rättSvar']), tal(sr)):
                fynd.append(f'delkort {d.get("etikett")}: svar {d["rättSvar"]} saknas i svarsraden: {sr[:70]}')
        f = syn((d.get('t') or '') + ' ' + (d.get('fraga') or ''))
        m = re.search(r'\b(se ovan|i föregående uppgift|från uppgift [a-e]\)|i [a-e]\))', f)
        if m:
            fynd.append(f'delkort {d.get("etikett")} hänvisar bakåt: {m.group(0)}')
    sista = vt.split('[FIG]')[-1].strip()
    if isinstance(u.get('rättSvar'), (int, float)) and u['rättSvar'] < 0 and \
            re.search(r'\bHur (stor|lång|många|mycket|långt|hög)', sista):
        fynd.append(f'negativt svar {u["rättSvar"]} på ”Hur stor/lång …”')
    return fynd


def main():
    b = Bank(sys.argv[1])
    omr = set(sys.argv[2:])
    n = 0
    for u in b.arr:
        if omr and u.get('omr') not in omr:
            continue
        f = kolla(u)
        if f:
            n += 1
            print(f'{u["id"]} [{u.get("omr")}] ' + ' | '.join(f))
            print('    ' + syn(u.get('t'))[:300])
    print('flaggade', n)


if __name__ == '__main__':
    main()
