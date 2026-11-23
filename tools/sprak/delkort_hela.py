"""Delkort som bara var fragment blir hela frågor (2026-11-23).

I Kunskapsgymmet visas ett delkort som inledning + fråga. När inledningen slutade mitt i en mening (”För
y = tan(2x), bestäm”) och frågan var ett fragment (”perioden i radianer”), blev kortet svårläst. Samma typ av fel
rättades i felrapporten för Ma4 1.59. Här skrivs inledningen som en hel mening och varje delkort som en hel fråga.
Papperstexten `t` byggs av samma delar (inledning + a), b) … med stor bokstav och punkt) i bankens befintliga format.
Svar, facit och allt annat är oförändrat.

Skriptfilen har R = {id: {'intro': ny inledning (HTML-fri text), 'd': {etikett: ny fråga}, 'ol': True/False}}.
Delkort med eget `t` (inledning + fråga) får `t` = inledning + fråga.

  python tools/sprak/delkort_hela.py <bank> <skript.py> [--skriv]
"""
import copy
import importlib.util
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import bankobjekt as B  # noqa: E402
from sprakverktyg import FIL  # noqa: E402

SPACER = '<br><span aria-hidden="true" style="display:block;height:7px"></span>'


def ladda(fil):
    spec = importlib.util.spec_from_file_location('omskr', fil)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.R


def main():
    kod, skript = sys.argv[1], sys.argv[2]
    fil = os.path.join(HERE, '..', '..', FIL[kod])
    R = ladda(skript)
    src, bank = B.las(fil)
    Q = {u['id']: u for u in bank}
    nya = {}
    for id_, r in R.items():
        u = Q[id_]
        assert '<svg' not in u['t'] and '<img' not in u['t'], id_
        ny = copy.deepcopy(u)
        etiketter = [d['etikett'] for d in ny['spelDelar']]
        assert set(r['d']) == set(etiketter), (id_, etiketter)
        intro = r['intro']
        ny['spelIntro'] = f'<p>{intro}</p>'
        for d in ny['spelDelar']:
            f = r['d'][d['etikett']]
            d['fraga'] = f'<p>{f}</p>' if d['fraga'].startswith('<p>') else f
            if d.get('t'):
                d['t'] = f'{intro} {f}' if not d['t'].startswith('<') else f'<p>{intro}</p><p>{f}</p>'
        if r.get('ol'):
            ny['t'] = f'<p>{intro}</p><ol type="a">' + ''.join(f'<li>{r["d"][e]}</li>' for e in etiketter) + '</ol>'
        else:
            ny['t'] = f'<p>{intro}</p><p>' + SPACER.join(f'{e}) {r["d"][e]}' for e in etiketter) + '</p>'
        for k in u:
            if k not in ('t', 'spelIntro', 'spelDelar'):
                assert ny[k] == u[k], (id_, k)
        for d0, d1 in zip(u['spelDelar'], ny['spelDelar']):
            assert {k: v for k, v in d0.items() if k not in ('t', 'fraga')} == \
                   {k: v for k, v in d1.items() if k not in ('t', 'fraga')}, id_
        nya[id_] = ny
    ny_src = B.ersatt(src, nya)
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    for id_ in list(nya)[:3]:
        print(id_, nya[id_]['t'][:300])
    print(len(nya), 'uppgifter', '(skrivet)' if '--skriv' in sys.argv else '(torrkörning)')
    if '--skriv' in sys.argv:
        B.skriv(fil, ny_src)


if __name__ == '__main__':
    main()
