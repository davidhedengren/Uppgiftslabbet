"""A* och girig bäst först: f(n), g(n) och h(n) i stället för f, g och h (användarbeslut 2026-11-24).

Användaren: ”i alla uppgifter om A* och girig bäst först, skriv f(n) och g(n) istället för bara f och g.”
h skrivs på samma sätt, så att formeln blir f(n) = g(n) + h(n).

- När en bestämd nod står direkt efter (”f för P”, ”g, h och f för C1”) skrivs nodens namn: f(P), g(C1) …
- Annars f(n), g(n), h(n). Sammansättningar följer med: ”f-värdet” → ”f(n)-värdet”.
- Uppgifter: kapitel 2 och övriga uppgifter som nämner A* eller girig bäst först.
- Fält: t, spelIntro, s, ledtrad, kgInstruktion, alternativens txt och kommentar, svarEtiketter, rättSvar (samma
  ändring som alternativen, så att svaren fortsätter att stämma) och delkortens motsvarande fält.
- Inte ändrat: SVG-figurer (nodetiketterna ”h = 2” hör till en utritad nod), HTML-taggar, h₁/h₂/h₃ i 2.106,
  listbokstaven ”f)”.

  python tools/sprak/ai_fgh_n.py [--skriv]
"""
import copy
import json
import os
import re
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402

FIL = os.path.abspath(os.path.join(HERE, '..', '..', 'uppgifterai.js'))
TEXTFALT = ('t', 'spelIntro', 's', 'ledtrad', 'kgInstruktion', 'fraga')
NOD = r'[A-Z][0-9]?'
# ”g, h och f för C1” / ”f för P” – men inte ”h för P, Q och R” (flera noder)
PER_NOD = re.compile(r'(?<![\w\\{/.])([fgh])((?:, [fgh])*(?: och [fgh])?) för (' + NOD + r')'
                     r'(?![\wÅÄÖåäö]|, ' + NOD + r'\b| och (?:för )?' + NOD + r'\b)')
TVA_NODER = re.compile(r'(?<![\w\\{/.])([fgh]) för (' + NOD + r') och för (' + NOD + r')\b')
ENSAM = re.compile(r'(?<![\w\\{/.])([fgh])(?![\w(₀-₉)])')


def byt_text(s):
    # gammalt fel i några svarsrader: ”f(f för B1) = 7” → ”f(B1) = 7”
    s = re.sub(r'\b([fgh])\(\1 för (' + NOD + r')\)', r'\1(\2)', s)
    s = TVA_NODER.sub(lambda m: f'{m.group(1)}({m.group(2)}) och {m.group(1)}({m.group(3)})', s)
    def per_nod(m):
        nod = m.group(3)
        bokst = [m.group(1)] + re.findall(r'(?:, | och )([fgh])\b', m.group(2) or '')
        delar = [f'{b}({nod})' for b in bokst]
        return delar[0] if len(delar) == 1 else ', '.join(delar[:-1]) + ' och ' + delar[-1]
    s = PER_NOD.sub(per_nod, s)
    return ENSAM.sub(lambda m: m.group(1) + '(n)', s)


def byt_html(h):
    """Byt bara i textnoder utanför <svg>."""
    if not isinstance(h, str):
        return h
    ut = []
    for i, bit in enumerate(re.split(r'(<svg[\s\S]*?</svg>)', h)):
        if i % 2:
            ut.append(bit)
            continue
        for j, b in enumerate(re.split(r'(<[^>]+>)', bit)):
            ut.append(b if j % 2 else byt_text(b))
    return ''.join(ut)


def byt_svar(v):
    if isinstance(v, list):
        return [byt_svar(x) for x in v]
    return byt_text(v) if isinstance(v, str) else v


def byt_obj(o):
    for k in TEXTFALT:
        if k in o:
            o[k] = byt_html(o[k])
    for a in o.get('alternativ') or []:
        for k in ('txt', 'kommentar'):
            if isinstance(a.get(k), str):
                a[k] = byt_text(a[k])
    if 'svarEtiketter' in o:
        et = o['svarEtiketter']
        # ”g”, ”h”, ”f” på ett kort som frågar efter g(B2), h(B2) och f(B2): etiketten får nodens namn
        noder = set(re.findall(r'\b[fgh]\((' + NOD + r')\)', re.sub(r'<[^>]+>', ' ', o.get('fraga') or '')))
        if isinstance(et, list) and len(noder) == 1 and all(e in ('f', 'g', 'h') for e in et):
            nod = noder.pop()
            o['svarEtiketter'] = [f'{e}({nod})' for e in et]
        else:
            o['svarEtiketter'] = byt_svar(et)
    if 'rättSvar' in o and o.get('svarstyp') in ('alternativ', 'flera_delar', 'kort_text'):
        o['rättSvar'] = byt_svar(o['rättSvar'])


def i_omfang(u):
    return u['kap'] == 2 or bool(re.search(r'A\*|[Gg]irig', json.dumps(u, ensure_ascii=False)))


def main():
    src, bank = B.las(FIL)
    nya = {}
    for u in bank:
        if not i_omfang(u):
            continue
        ny = copy.deepcopy(u)
        byt_obj(ny)
        for d in ny.get('spelDelar') or []:
            byt_obj(d)
        if ny != u:
            nya[u['id']] = ny
    # rätt alternativ måste fortsätta stämma med rättSvar
    for ny in nya.values():
        for o in [ny] + list(ny.get('spelDelar') or []):
            if o.get('svarstyp') == 'alternativ' and o.get('alternativ'):
                ratt = [a['txt'] for a in o['alternativ'] if a.get('ratt')]
                assert o['rättSvar'] in ratt or o['rättSvar'] == ratt, (ny['id'], o.get('etikett'))
    ny_src = B.ersatt(src, nya)
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    print(len(nya), 'uppgifter', '(skrivet)' if '--skriv' in sys.argv else '(torrkörning)')
    if '--ut' in sys.argv:
        json.dump({k: v for k, v in nya.items()}, open(sys.argv[sys.argv.index('--ut') + 1], 'w', encoding='utf-8'),
                  ensure_ascii=False)
    if '--skriv' in sys.argv:
        B.skriv(FIL, ny_src)


if __name__ == '__main__':
    main()
