"""Manuell granskning av Fy1 rörelse (omgång 2), 2026-11-27: medelhastighet.

Alla uppgifter i området är lästa och kontrollräknade (se agent/FY1_GRANSKNING_2026-11-27.md). Ändringar:

- Konstanter och tabellvärden ur uppgiftstexten till kgInstruktion (beslut 2026-10-25 och 2026-11-27):
  3.103 ljudets och ljusets fart, 3.127 och 2.308 b ljusets fart, 3.101 jordens radie.
- Avrundnings- och svarsinstruktioner till kgInstruktion eller bort: 3.101 a (närmaste hundratal km), 2.308 b
  (”Ange antalet varv.”), 3.21 b (”i m”, underförstådd enhet).
- Lösningsanvisningar och metatext bort: 3.103 (”Börja med att anta …”), 3.104 (”Antag att s > 0 och v > 0.”),
  3.229 (”Antag att alla sträckor och farter är positiva …” → ”Bilen gör inga stopp.”), 3.127 (”Antag att signalen
  går rakt …”), samt metodanvisningen ”Ställ upp ett uttryck …/en ekvation …” i 2.297, 2.303, 2.310, 2.315, 2.316,
  2.319.
- 2.295, 2.299: pappersbladets b upprepade situationen med nya ord (och 2.295 sa både ”åker” och ”cyklar”). Ny
  gemensam inledning; delkorten byggs som inledning + fråga (kedjan), med behövt mellanresultat i 2.299 b.
- 3.96: ”Antag” → ”Anta”.

Svar och facit är oförändrade.

  python tools/fy1-granskning-rorelse-2026-11-27.py [--skriv]
"""
import json
import os
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

LJUS = 'Ljusets fart är 3,00·10⁸ m/s.'

# id -> lista av operationer
#   ('byt', gammalt, nytt)            i t, spelIntro och delkortens t/fraga
#   ('kg', [meningar], vem)           vem = 'alla' (uppgift + delkort) eller en etikett eller 'uppgift'
#   ('falt', namn, värde)             sätt ett fält på uppgiften
#   ('del', etikett, {fält: värde})   sätt fält på ett delkort
OPS = {
    '3.21': [('byt', 'Hur stort är djupet i m?', 'Hur stort är djupet?')],
    '3.96': [('byt', 'Antag att snigeln fortsätter', 'Anta att snigeln fortsätter')],
    '3.101': [('byt', ' Jordens radie är 6371 km.', ''),
              ('byt', 'Bestäm banans omkrets i km, avrundad till närmaste hundratal km.', 'Bestäm banans omkrets i km.'),
              ('kg', ['Jordens radie är 6 371 km.'], 'alla'),
              ('kg', ['Avrunda omkretsen till närmaste hundratal km.'], 'a'),
              ('kg', ['Avrunda omkretsen till närmaste hundratal km.'], 'uppgift')],
    '3.103': [('byt', ' Ljudet går 340 m/s och ljusets fart är 3,00 · 10⁸ m/s.', ''),
              ('byt', '<p>Börja med att anta att ljuset inte tar någon tid på sig. Kontrollera sedan om det antagandet är rimligt.</p>', ''),
              ('kg', ['Ljudets fart är 340 m/s.', LJUS], 'alla')],
    '3.104': [('byt', '<p>Antag att s > 0 och v > 0.</p>', '')],
    '3.127': [('byt', ' Signalen går med ljusets fart, 3,00·10⁸ m/s.', ' Signalen går med ljusets fart.'),
              ('byt', '<p>Antag att signalen går rakt från satelliten till mottagaren med konstant fart. Bortse från övriga felkällor.</p>',
               '<p>Bortse från övriga felkällor.</p>'),
              ('kg', [LJUS], 'alla')],
    '3.229': [('byt', '<p>Antag att alla sträckor och farter är positiva och att inga stopp görs.</p>', '<p>Bilen gör inga stopp.</p>')],
    '2.297': [('byt', '<p>Ställ upp ett uttryck för var och ens läge eller tid och sätt dem lika.</p>', '')],
    '2.310': [('byt', '<p>Ställ upp ett uttryck för var och ens läge eller tid och sätt dem lika.</p>', '')],
    '2.319': [('byt', '<p>Ställ upp ett uttryck för var och ens läge eller tid och sätt dem lika.</p>', '')],
    '2.303': [('byt', '<p>Ställ upp en ekvation för tur och retur.</p>', '')],
    '2.315': [('byt', '<p>Ställ upp en ekvation.</p>', '')],
    '2.316': [('byt', '<p>Ställ upp en ekvation.</p>', '')],
    '2.308': [('byt', ' rör sig med i praktiken ljusets fart, \\(3{,}00\\cdot10^8\\) m/s. Hur många varv hinner de på 1,00 s? Ange antalet varv.',
               ' rör sig i praktiken med ljusets fart. Hur många varv hinner de på 1,00 s?'),
              ('kg', [LJUS], 'b'), ('kg', [LJUS], 'uppgift')],
}

INTRO_2295 = ('<p>Anna och Stina cyklar samma sträcka på 10 km. Anna cyklar med farten 18 km/h. Stina startar '
              '2,0 minuter efter Anna och kommer fram 3,0 minuter före henne.</p>')
F_2295 = ['Hur många minuter tar Annas cykeltur?', 'Vilken medelfart har Stina?']
INTRO_2299 = ('<p>En skidåkare åker åt samma håll med 6,7 m/s i 15 minuter och sedan med 8,2 m/s i 12 minuter. '
              'Därefter åker skidåkaren samma väg tillbaka till starten på 35 minuter.</p>')
F_2299 = ['Hur långt åker skidåkaren under de första 27 minuterna?',
          'Vilken medelfart har skidåkaren på vägen tillbaka?']
F_2299_KORT_B = 'Skidåkaren har åkt 11 934 m innan vändningen. Vilken medelfart har skidåkaren på vägen tillbaka?'


def kedja(q, intro, fragor, kortfragor=None):
    q['spelIntro'] = intro
    q['t'] = intro + '<ol type="a">' + ''.join(f'<li>{f}</li>' for f in fragor) + '</ol>'
    kortfragor = kortfragor or fragor
    assert len(q['spelDelar']) == len(fragor)
    for d, f in zip(q['spelDelar'], kortfragor):
        d['fraga'] = f
        d['t'] = intro + f'<p>{f}</p>'


def kg_med(kg, meningar):
    kg = (kg or '').strip()
    for m in meningar:
        if m not in kg:
            kg = (kg + ' ' + m).strip()
    return kg


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    idx = {q['id']: q for q in bank}
    nya = {}
    for uid, ops in OPS.items():
        q = json.loads(json.dumps(idx[uid]))
        for op in ops:
            if op[0] == 'byt':
                _, gl, ny = op
                n = 0
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
            elif op[0] == 'kg':
                _, meningar, vem = op
                if vem in ('alla', 'uppgift'):
                    q['kgInstruktion'] = kg_med(q.get('kgInstruktion'), meningar)
                for d in q.get('spelDelar') or []:
                    if vem == 'alla' or vem == d['etikett']:
                        d['kgInstruktion'] = kg_med(d.get('kgInstruktion'), meningar)
        nya[uid] = q
    q = json.loads(json.dumps(idx['2.295']))
    kedja(q, INTRO_2295, F_2295)
    nya['2.295'] = q
    q = json.loads(json.dumps(idx['2.299']))
    kedja(q, INTRO_2299, F_2299, [F_2299[0], F_2299_KORT_B])
    nya['2.299'] = q
    ny_src = src
    for uid, q in nya.items():
        start = ny_src.index('"id": ' + json.dumps(uid))
        a = ny_src.rfind('\n  {', 0, start) + 3
        slut = ny_src.index('\n  }', start) + 4
        assert json.loads(ny_src[a:slut]) == idx[uid], uid
        ny_src = ny_src[:a] + json.dumps(q, ensure_ascii=False, indent=2).replace('\n', '\n  ') + ny_src[slut:]
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = {x['id']: sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k)) for x, y in zip(efter, bank) if x != y}
    assert set(andr) == set(nya), set(andr) ^ set(nya)
    for uid, k in andr.items():
        assert not ({'s', 'rättSvar', 'svarEnhet'} & set(k)), (uid, k)
        x = next(e for e in efter if e['id'] == uid)
        assert '<p></p>' not in x['t'], uid
        print(uid, k)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)


if __name__ == '__main__':
    main()
