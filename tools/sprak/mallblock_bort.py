"""Ta bort generiska mallrader ur facit (2026-11-20).

Användning:
  python tools/sprak/mallblock_bort.py <bank> --lista      lista etikettblock som förekommer i minst 3 uppgifter
  python tools/sprak/mallblock_bort.py <bank> [--skriv]    tillämpa reglerna i mallblock_regler.py

Raderna är maskinskrivna råd med etiketter som ”Tänk så här:”, ”Varför metoden fungerar:”, ”Kontroll och insikt:”
och ”Nyckelidé:”. De är inte skrivna för uppgiften och hör ibland till ett helt annat område (tallinje i
derivatauppgifter, ekvationssystem i kvotregeln). Varje rad är handklassad i mallblock_regler.py: BORT tas bort,
AV behåller texten men tar bort etiketten. Rader som inte är klassade rörs inte. En lista som blir tom tas bort.
"""
import json, os, re, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprakverktyg import Bank, lit
from mallblock_regler import BORT, AV

ETIKETT = re.compile(r'^(Tänk så här|Varför metoden fungerar|Kontroll och insikt|Nyckelidé|Metod|Kontroll|Kontrollera ditt resonemang|Kontrollpunkter|Formel från formelbladet|Formelbladet|Rimlighetskontroll|Enhetssteg|Insikt|Begrepp):')
ETIKETT_HTML = re.compile(r'<strong>(Tänk så här|Varför metoden fungerar|Kontroll och insikt|Nyckelidé):</strong>\s*')
LI = re.compile(r'<li>((?:(?!<li>)[\s\S])*?)</li>')
TOM_OL = re.compile(r'<ol class="facit-steglista"[^>]*>\s*</ol>')
TOM_ARBETE = re.compile(r'<div class="facit-arbete">\s*</div>')


def ren(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h)).strip()


def facit(u):
    if u.get('s'):
        yield u['s']
    for d in u.get('spelDelar') or []:
        if d.get('s'):
            yield d['s']


def rensa(s):
    n = [0, 0]

    def li(m):
        t = ren(m.group(0))
        if t in BORT:
            n[0] += 1
            return ''
        if t in AV:
            n[1] += 1
            inner = ETIKETT_HTML.sub('', m.group(1), count=1)
            inner = re.sub(r'^(\s*<p[^>]*>)\s*', r'\1', inner)
            return '<li>' + inner + '</li>'
        return m.group(0)

    ny = LI.sub(li, s)
    for _ in range(2):
        ny = TOM_OL.sub('', ny)
        ny = TOM_ARBETE.sub('', ny)
    return ny, n


def lista(b):
    forek = defaultdict(set)
    for u in b.arr:
        for s in facit(u):
            for m in LI.finditer(s):
                t = ren(m.group(0))
                if ETIKETT.match(t):
                    forek[t].add(u['id'])
    for t, ids in sorted(forek.items(), key=lambda x: -len(x[1])):
        if len(ids) >= 3:
            status = 'BORT' if t in BORT else 'AV' if t in AV else '-'
            print(f'{len(ids)}\t{status}\t{t[:160]}')


def main():
    kod = sys.argv[1]
    b = Bank(kod)
    if '--lista' in sys.argv:
        return lista(b)
    tot = [0, 0]
    antal = 0
    korta = []
    for u in b.arr:
        par = []
        for s in facit(u):
            ny, n = rensa(s)
            if ny != s:
                par.append((s, ny))
                tot[0] += n[0]
                tot[1] += n[1]
                if len(ren(ny)) < 80:
                    korta.append(u['id'])
        if not par:
            continue
        antal += 1
        t = b.byte.get(u['id'], b.text(u['id']))
        for gammal, ny in par:
            if lit(gammal) in t:
                t = t.replace(lit(gammal), lit(ny))
            else:
                assert lit(ny) in t, u['id']
        json.loads(t)
        b.byte[u['id']] = t
    print(f'{tot[0]} rader bort, {tot[1]} etiketter bort, i {antal} uppgifter; {len(set(korta))} facit kortare än 80 tecken')
    if '--skriv' in sys.argv:
        print(b.spara(), 'objekt skrivna')


main()
