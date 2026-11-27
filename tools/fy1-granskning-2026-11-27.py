"""Manuell granskning av Fy1 (densitet, rörelse, krafter), 2026-11-27.

Ändringar som föreslogs i en tidigare chatt men aldrig nådde GitHub (pushen misslyckades där), gjorda om och
kontrollerade här:

Densitet: delfrågan efter ”Bestäm densiteten i g/cm³” löd bara ”Bestäm densiteten.”, fast facit begär enhetsbytet
till kg/m³. Enheten är det som prövas och står därför i frågan (undantag i beslutet om rena uppgifter 2026-11-23).
- 2.17 c: 288/240 = 1,2 g/cm³ = 1 200 kg/m³ → ”Ange rätblockets densitet i kg/m³.”
- 2.26 d: 1 050/125 = 8,4 g/cm³ = 8 400 kg/m³ → ”Ange kubens densitet i kg/m³.”
- 2.161 b: 5 600/5 000 = 1,12 g/cm³ = 1 120 kg/m³ → ”Ange glykolens densitet i kg/m³.”
- 2.379: ”vågrätt” → ”horisontellt” (stilguiden; språktestet sprak-2026-11-17 föll på detta).

Rörelse:
- 3.14: ”Sedan har den den konstanta accelerationen 3,0 m/s² i 4,0 sekunder.” → ”Den accelererar sedan konstant med
  3,0 m/s² i 4,0 s.”
- 3.158: ”Därefter håller den den farten.” → ”Därefter fortsätter bilen med samma fart.”
- 3.64, 3.120, 3.124, 3.155: facit räknar med konstant acceleration (tidlösa formeln, medelfart gånger tid), men frågan
  sa det inte; utan villkoret går bara en medelacceleration att bestämma. Nu: ”Räkna med att accelerationen är
  konstant (under inbromsningen).” Tomma <p></p> och inledande mellanslag i de redigerade styckena tas bort.

Krafter:
- 4.368: ”En satellit är 400 km över ytan.” → ”En satellit kretsar runt jorden på 400 km höjd.” Då går det att förklara
  både varför avståndet till jordens centrum ska användas och varför satelliten är i fritt fall (g ≈ 8,7 m/s² där).

Svar, facit och rättning är oförändrade.

  python tools/fy1-granskning-2026-11-27.py [--skriv]
"""
import json
import os
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

# id -> [(gammalt, nytt, fält)], fält 'text' = t, spelIntro och delkortens t/fraga; 'alla' = alla strängfält
BYTEN = {
    '2.17': [('Bestäm densiteten.', 'Ange rätblockets densitet i kg/m³.', 'text')],
    '2.26': [('Bestäm densiteten.', 'Ange kubens densitet i kg/m³.', 'text')],
    '2.161': [('Bestäm densiteten.', 'Ange glykolens densitet i kg/m³.', 'text')],
    '2.379': [('flyter vågrätt', 'flyter horisontellt', 'alla'), ('ligger vågrätt', 'ligger horisontellt', 'alla')],
    '3.14': [('Sedan har den den konstanta accelerationen 3,0 m/s² i 4,0 sekunder.',
              'Den accelererar sedan konstant med 3,0 m/s² i 4,0 s.', 'text')],
    '3.158': [('Därefter håller den den farten.', 'Därefter fortsätter bilen med samma fart.', 'text')],
    '3.64': [('bromsar sedan till stillastående på 4,0 meter.</p><p></p>',
              'bromsar sedan till stillastående på 4,0 m. Räkna med att accelerationen är konstant under '
              'inbromsningen.</p>', 'text')],
    '3.120': [('På 3,0 sekunder bromsas farten ned till 6,0 m/s.</p>',
               'Under 3,0 s bromsas farten ned till 6,0 m/s. Räkna med att accelerationen är konstant under '
               'inbromsningen.</p>', 'text'),
              ('</span><p></p>', '</span>', 'text')],
    '3.124': [('har farten 23 m/s efter 68 m.</p>',
               'har farten 23 m/s efter 68 m. Räkna med att accelerationen är konstant.</p>', 'text')],
    '3.155': [('på 7,5 s.</p>', 'på 7,5 s. Räkna med att accelerationen är konstant.</p>', 'text'),
              ('<li> Bestäm', '<li>Bestäm', 'text'), ('<p> Bestäm', '<p>Bestäm', 'text')],
    '4.368': [('En satellit är 400 km över ytan.', 'En satellit kretsar runt jorden på 400 km höjd.', 'text')],
}


def byt_i(v, gl, ny):
    if isinstance(v, str):
        return v.replace(gl, ny), v.count(gl)
    if isinstance(v, list):
        ut, n = [], 0
        for x in v:
            y, k = byt_i(x, gl, ny)
            ut.append(y)
            n += k
        return ut, n
    if isinstance(v, dict):
        ut, n = {}, 0
        for k, x in v.items():
            y, c = byt_i(x, gl, ny)
            ut[k] = y
            n += c
        return ut, n
    return v, 0


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    idx = {q['id']: q for q in bank}
    nya = {}
    for uid, byten in BYTEN.items():
        q = json.loads(json.dumps(idx[uid]))
        for gl, ny, falt in byten:
            n = 0
            if falt == 'alla':
                q, n = byt_i(q, gl, ny)
            else:
                for k in ('t', 'spelIntro'):
                    if isinstance(q.get(k), str):
                        n += q[k].count(gl)
                        q[k] = q[k].replace(gl, ny)
                for d in q.get('spelDelar') or []:
                    for k in ('t', 'fraga'):
                        if isinstance(d.get(k), str):
                            n += d[k].count(gl)
                            d[k] = d[k].replace(gl, ny)
            assert n >= 1, (uid, gl)
        nya[uid] = q
    # skriv tillbaka fält för fält (strängfält ersätts som JSON-literaler inom filen)
    ny_src = src
    for uid, q in nya.items():
        gq = idx[uid]
        for k in q:
            if q[k] == gq[k]:
                continue
            a = json.dumps(gq[k], ensure_ascii=False)
            b = json.dumps(q[k], ensure_ascii=False)
            if isinstance(gq[k], str):
                assert ny_src.count(a) == 1, (uid, k, ny_src.count(a))
                ny_src = ny_src.replace(a, b)
            else:
                start = ny_src.index('"id": ' + json.dumps(uid))
                slut = ny_src.index('\n}', start)
                dec = json.JSONDecoder()
                nyckel = json.dumps(k, ensure_ascii=False) + ': '
                i = ny_src.index(nyckel, start) + len(nyckel)
                assert i < slut
                _, j = dec.raw_decode(ny_src, i)
                assert json.loads(ny_src[i:j]) == gq[k]
                rad = ny_src.rfind('\n', 0, i) + 1
                ind = ny_src[rad:i - len(nyckel)]
                txt = ny_src[i:j]
                nytt = json.dumps(q[k], ensure_ascii=False, indent=2).replace('\n', '\n' + ind) if '\n' in txt else b
                ny_src = ny_src[:i] + nytt + ny_src[j:]
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = {x['id']: sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k)) for x, y in zip(efter, bank) if x != y}
    assert set(andr) == set(BYTEN), set(andr) ^ set(BYTEN)
    for x in efter:
        if x['id'] in nya:
            assert x == nya[x['id']], x['id']
            assert 'rättSvar' not in andr[x['id']]
            if x['id'] != '2.379':
                assert 's' not in andr[x['id']], x['id']
            assert '<p></p>' not in json.dumps(x, ensure_ascii=False) or x['id'] not in ('3.64', '3.120'), x['id']
    for uid in sorted(andr, key=lambda u: [float(p) for p in u.split('.')]):
        print(uid, andr[uid])
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)


if __name__ == '__main__':
    main()
