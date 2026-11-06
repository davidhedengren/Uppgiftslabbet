"""Ma1 faktorisering: äldre tvåfältsuppgifter blir ett svarsfält med formatet största_faktor (2026-11-06).

Användaren: "då kan vi väl göra om de gamla så det inte behövs två svarsfält? Det känns väl mer naturligt om de
ska svara med hela det faktoriserade uttrycket istället".

För de 35 uppgifterna med svarFormat ["förenklat_polynom", "förenklat_polynom"] och svarEtiketter
["utbruten faktor", "innehåll i parentesen"] görs följande:
  - rättSvar [faktor, parentes] blir "faktor(parentes)", svarstyp blir "uttryck" och svarFormat "största_faktor";
  - svarsstruktur, svarEtiketter och tolerans tas bort;
  - meningen om två fält i frågan tas bort;
  - facit skrivs om enligt FACITMALL med samma steg som i #1.1685–1.1704 (tools/bygg-ma1-faktorisering-2026-11-06.py).
    Steg: största gemensamma faktor, dividera varje term, skriv som produkt, kontroll och svarsrad.
    Byggaren kontrollerar med sympy att dess svar är exakt det gamla facit;
  - ID, ledtråd, nivå, poäng, familj och verktygsflaggor behålls.
1.261 lämnas orörd. Där ska den första termen i parentesen vara 2x, vilket största_faktor inte kontrollerar.
Logg: agent/MA1_FAKTORISERING_2026-11-06.md

  python tools/ma1-faktorisering-ett-falt-2026-11-06.py [--skriv]
"""
import importlib.util
import io
import contextlib
import json
import re
import sys
from pathlib import Path

HAR = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('fakt', HAR / 'bygg-ma1-faktorisering-2026-11-06.py')
FK = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(FK)
BANK = HAR.parent / 'uppgifterma1.js'
UNDANTAG = {'1.261'}
FALTMENING = re.compile(r'\s*Ange faktorn och (?:det förenklade )?innehållet i parentesen i varsitt fält\.')


def omvandla(u):
    fraga = re.search(r'\\\((.+?)\\\)', u['t']).group(1).replace('{', '').replace('}', '')
    x = FK.del_bryt_ut(fraga, u['traningsniva'])
    gammalt = f'{u["rättSvar"][0]}({u["rättSvar"][1]})'
    assert x['svar'] == gammalt, (u['id'], x['svar'], gammalt)
    t = FALTMENING.sub('', u['t'])
    assert t != u['t'] and 'fält' not in t, u['id']
    ny = {}
    for k, v in u.items():           # behåll fältens ordning
        if k in ('svarsstruktur', 'svarEtiketter', 'tolerans'):
            continue
        ny[k] = v
    ny.update(t=t, s=FK.K1.lista(x['steg'], f'\\({x["svartex"]}\\)'), svarstyp='uttryck', rättSvar=gammalt, svarFormat='största_faktor')
    return ny


def main():
    src = open(BANK, encoding='utf-8', newline='').read()
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    gamla = [u for u in data if u.get('omr') == 'faktorisering' and u.get('svarFormat') == ['förenklat_polynom', 'förenklat_polynom']
             and u.get('svarEtiketter') == ['utbruten faktor', 'innehåll i parentesen'] and u['id'] not in UNDANTAG]
    print(len(gamla), 'uppgifter att omvandla')
    nl = '\r\n' if '\r\n' in src else '\n'
    for u in gamla:
        ny = omvandla(u)
        m = re.search(r'\{\s*"id":\s*"' + re.escape(u['id']) + r'"', src)
        _, slut = json.JSONDecoder().raw_decode(src, m.start())
        src = src[:m.start()] + FK.K1.som_json(ny, nl) + src[slut:]
        if '--visa' in sys.argv:
            print(u['id'], ny['rättSvar'], re.sub('<[^>]+>', ' ', ny['t']))
    json.loads(src[src.index('['):src.rindex(']') + 1])
    if '--skriv' in sys.argv:
        open(BANK, 'w', encoding='utf-8', newline='').write(src)
        print('skrivet')


if __name__ == '__main__':
    main()
