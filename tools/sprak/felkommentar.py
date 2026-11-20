"""Lägg in felkommentarer på flervalsalternativ (2026-11-20).

Användning: python tools/sprak/felkommentar.py <bank> <skript.py> [--skriv]
Skriptet definierar K = {id: [kommentar för alternativ 0, 1, 2, …]} i huvuduppgiftens alternativordning,
där det rätta alternativet får None (eller en egen förklaring om den saknas). Samma kommentar läggs på
delkortens alternativ med samma txt. Befintliga kommentarer skrivs aldrig över.
Infogningen görs i objektets text, så att formatet (kompakt eller indraget) bevaras.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprakverktyg import Bank, lit


def lagg_in(txt_obj, alt_txt, ratt, kommentar):
    """Infoga kommentar efter "ratt": <bool> för alla alternativ med denna txt som saknar kommentar."""
    rb = 'true' if ratt else 'false'
    rx = re.compile(r'("txt"\s*:\s*' + re.escape(lit(alt_txt)) + r'\s*,(\s*)"ratt"\s*:\s*' + rb + r')(?!\s*,\s*"kommentar")')
    n = 0

    def ers(m):
        nonlocal n
        n += 1
        mellan = m.group(2)
        sep = ',' + mellan if '\n' in mellan else ', '
        return m.group(1) + sep + '"kommentar": ' + lit(kommentar)
    return rx.sub(ers, txt_obj), n


def main():
    kod, skript = sys.argv[1], sys.argv[2]
    ns = {}
    exec(open(skript, encoding='utf-8').read(), ns)
    K = ns['K']
    b = Bank(kod)
    fel = []
    antal = 0
    for id_, kommentarer in K.items():
        u = b.obj(id_)
        alt = u.get('alternativ') or next((d.get('alternativ') for d in u.get('spelDelar') or [] if d.get('alternativ')), None)
        if not alt:
            fel.append(f'{id_}: inga alternativ')
            continue
        if len(kommentarer) != len(alt):
            fel.append(f'{id_}: {len(kommentarer)} kommentarer men {len(alt)} alternativ')
            continue
        t = b.byte.get(id_, b.text(id_))
        for a, k in zip(alt, kommentarer):
            if a.get('ratt') and k:
                # Skydd (2026-11-20): None på fel plats i listan förskjuter alla kommentarer.
                fel.append(f'{id_}: kommentar på det rätta alternativet {a["txt"][:40]} (står None på rätt plats?)')
                continue
            if not k or (a.get('kommentar') or '').strip():
                continue
            t, n = lagg_in(t, a['txt'], bool(a.get('ratt')), k)
            if n == 0:
                fel.append(f'{id_}: hittade inte alternativet {a["txt"][:40]}')
            antal += n
        json.loads(t)
        b.byte[id_] = t
    for f in fel:
        print('FEL', f)
    print(antal, 'kommentarer i', len(K), 'uppgifter')
    if fel:
        sys.exit(1)
    if '--skriv' in sys.argv:
        print(b.spara(), 'objekt skrivna')


main()
