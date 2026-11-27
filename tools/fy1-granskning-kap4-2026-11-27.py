"""Manuell granskning av Fy1 kap 4 Krafter (omgång 2), 2026-11-27.

Alla uppgifter i tyngdkraft, newton1, normalkraft, newton3, fjädrar, friktion, gravitation, blandat_kraft,
lutande_plan, moment, kraftvektorer och newton2 är lästa och kontrollräknade (svar som bara kan läsas av i en figur
är inte omräknade). Alla beräknade svar stämmer. Ändringar (se agent/FY1_GRANSKNING_2026-11-27.md):

- Sakfel: 4.207 c och 4.749 b saknade data i huvudtexten (fjäderkonstanten 25 N/m, stenen 1,0 m över marken), som
  bara fanns i delkortet. 4.102 b:s delkort hade 82 N i stället för huvudtextens 75 N (nu en kedja). 4.206 c:s delkort
  sa samma sak två gånger. 4.635:s delkort skrev ”backen” om två olika backar. 4.149 sa både ”ger glidfriktion” och
  ”bortse från friktionen” (menat: i trissan).
- Tabellvärden och konstanter ur texten till kgInstruktion (beslut 2026-10-25, 2026-11-23, 2026-11-27): jordens
  radie och massa, g på månen och Mars, himlakropparnas data i 4.22, protonens och elektronens massa (4.736, 4.689),
  densiteter i 4.523 och 4.524. Där tabellvärdet saknades i kgInstruktion läggs det till (4.24 Venus, 4.273 och 4.812
  månen, 4.899 vattnets densitet).
- Modelljargong och metatext bort: ”Himlakroppen modelleras som sfäriskt symmetrisk.” och liknande (behåller ”Bortse
  från … rotation”), ”Samma jordmodell gäller i alla delar.”, ”De behåller sin form.”, ”Bortse från luftens
  lyftkraft.”, ”Bortse från variationen i g med höjden.”, metodtipset ”Skriv krafterna på vektorform …” (kraftvektorer),
  allmänna villkor (4.297) och ”Bestäm värdena på grafens raka delar.” (4.157).
- Underförstådda enheter bort (”i N”, ”i m/s²”), ”föremålet” → det namngivna föremålet i ritövningarna, ”elevens”
  → namnet (4.21), ”Antag” → ”Anta”.

Svar och facit är oförändrade.

  python tools/fy1-granskning-kap4-2026-11-27.py [--skriv]
"""
import json
import os
import re
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

MANEN = 'Tyngdaccelerationen är 1,62 m/s² på månen.'
MARS = 'Tyngdaccelerationen är 3,71 m/s² på Mars.'
R6370 = 'Jordens radie är 6 370 km.'
HIMLA = '<p>Himlakroppen modelleras som sfäriskt symmetrisk. Bortse från rotation.</p>'
HIMLA_BR = '<p>Himlakroppen modelleras som sfäriskt symmetrisk. Bortse från rotation.<br></p>'
JORD_ROT = '<p>Bortse från jordens rotation.</p>'
VEKTORTIPS = ' Skriv krafterna på vektorform och addera dem. Tänk på tecknen.'

# id -> lista av operationer
#   ('byt', gammalt, nytt)            i t, spelIntro och delkortens t/fraga
#   ('tbyt', gammalt, nytt)           bara i pappersbladets t
#   ('delbyt', etikett, gammalt, nytt) bara i ett delkorts t/fraga
#   ('kg', [meningar], vem)           vem = 'alla' (uppgift + delkort), 'uppgift' eller en etikett
#   ('delfraga', etikett, fraga)      delkortet blir spelIntro + fråga (kedjan)
OPS = {
    # tyngdkraft
    '4.883': [('byt', ' Tyngdaccelerationen på månen är 1,62 N/kg.', ''), ('kg', [MANEN], 'alla')],
    '4.885': [('byt', ', där \\(g=1{,}62\\) m/s².', '.'), ('kg', [MANEN], 'alla')],
    '4.886': [('byt', ', där \\(g=1{,}62\\) m/s²?', '?'), ('kg', [MANEN], 'alla')],
    '4.888': [('byt', ' Tyngdaccelerationen är 9,82 m/s² på jorden och 1,62 m/s² på månen.', ''),
              ('kg', [MANEN], 'alla')],
    '4.890': [('byt', ' På Mars är \\(g=3{,}71\\) m/s².', ''), ('kg', [MARS], 'alla')],
    '4.882': [('byt', ' Jordens radie är ungefär 6 400 km.', ''), ('kg', ['Jordens radie är ungefär 6 400 km.'], 'alla')],
    '4.24': [('kg', ['Tyngdaccelerationen är 8,87 m/s² på Venus.'], 'alla')],
    '4.899': [('kg', ['Vattnets densitet är 1,00 kg/dm³.'], 'alla')],
    # newton1
    '4.400': [('byt', 'krafterna på föremålet', 'krafterna på boken')],
    '4.401': [('byt', 'krafterna på föremålet', 'krafterna på lampan')],
    '4.404': [('byt', 'alla krafter på föremålet', 'alla krafter på bilen')],
    '4.408': [('byt', 'alla krafter på föremålet', 'alla krafter på skylten')],
    '4.421': [('byt', 'krafterna på föremålet', 'krafterna på kulan')],
    '4.135': [('byt', '<p>Bortse från luftens lyftkraft.</p>', '')],
    # normalkraft
    '4.207': [('tbyt', '<li>Bestäm fjäderns förlängning.</li></ol>',
               '<li>Dynamometerns fjäder har fjäderkonstanten 25 N/m. Bestäm fjäderns förlängning när vikten hänger '
               'fritt.</li></ol>')],
    '4.21': [('byt', ' Bortse från variationen i g med höjden.', ''),
             ('byt', 'Bedöm elevens påstående.', 'Bedöm Ines påstående.')],
    '4.406': [('byt', 'alla krafter på föremålet', 'alla krafter på personen'),
              ('byt', '<p>Visa bara krafterna på personen, som inte rör vid hissens väggar.</p>',
               '<p>Personen rör inte hissens väggar.</p>')],
    '4.812': [('kg', [MANEN], 'alla')],
    # fjädrar
    '4.273': [('kg', [MANEN], 'alla')],
    # friktion
    '4.523': [('byt', ' och densiteten är 2,70 g/cm³. Vilken', '. Vilken')],
    '4.524': [('byt', ' Densiteten är 8,96 g/cm³.', '')],
    # gravitation
    '4.362': [('byt', '<p>Jordens radie är 6370 km. Bortse från rotation.</p>', JORD_ROT), ('kg', [R6370], 'alla')],
    '4.374': [('byt', '<p>Jordens radie är 6370 km. Bestäm', '<p>Bestäm'), ('kg', [R6370], 'alla')],
    '4.378': [('byt', ' Jordens radie är 6370 km.</p>', '</p>'), ('kg', [R6370], 'alla')],
    '4.740': [('byt', '<p>Jordens massa är \\(5{,}97\\cdot10^{24}\\) kg och radie 6 370 km. Hur stor', '<p>Hur stor'),
              ('byt', HIMLA, JORD_ROT),
              ('kg', ['Jordens massa är 5,97·10²⁴ kg och jordens radie är 6 370 km.'], 'alla')],
    '4.741': [('byt', ' Jordens radie är 6 370 km.</p>' + HIMLA_BR, '</p>' + JORD_ROT), ('kg', [R6370], 'alla')],
    '4.742': [('byt', HIMLA, '<p>Bortse från himlakropparnas rotation.</p>')],
    '4.743': [('byt', ' Jordens massa är \\(5{,}977\\cdot10^{24}\\) kg och radie 6 380 km.</p>', '</p>'),
              ('byt', HIMLA, JORD_ROT),
              ('kg', ['Jordens massa är 5,977·10²⁴ kg och jordens radie är 6 380 km.'], 'alla')],
    '4.748': [('byt', ' Jordens radie är 6 370 km.</p>' + HIMLA_BR, '</p>' + JORD_ROT), ('kg', [R6370], 'alla')],
    '4.751': [('byt', HIMLA, '<p>Bortse från planeternas rotation.</p>')],
    '4.752': [('byt', HIMLA, '<p>Bortse från planeternas rotation.</p>')],
    '4.739': [('byt', '<p>Jordens massa är \\(5{,}977\\cdot10^{24}\\) kg. Jordradien', '<p>Jordradien'),
              ('byt', HIMLA_BR, JORD_ROT), ('kg', ['Jordens massa är 5,977·10²⁴ kg.'], 'alla')],
    '4.74': [('byt', ' Massan är M = 5,97 · 10²⁴ kg och radien R = 6371 km. Bortse från rotation. Samma jordmodell '
              'gäller i alla delar.', ' Bortse från jordens rotation.'),
             ('byt', '<p>Jordens radie är 6371 km. En satellit', '<p>En satellit'),
             ('kg', ['Jordens massa är 5,97·10²⁴ kg och jordens radie är 6 371 km.'], 'alla')],
    '4.186': [('byt', '<p>Jordens radie är 6371 km. Tyngdaccelerationen', '<p>Tyngdaccelerationen'),
              ('byt', '<p>Jorden modelleras som sfäriskt symmetrisk. Bortse från rotation.</p>', JORD_ROT),
              ('kg', ['Jordens radie är 6 371 km.'], 'alla')],
    '4.9': [('byt', ' Behandla planeten som sfäriskt symmetrisk och bortse från rotation.',
             ' Bortse från planetens rotation.')],
    '4.22': [('byt', '<p>Månens massa är 7,35·10²² kg. Avståndet till jorden (5,97·10²⁴ kg) är 3,84·10⁸ m och avståndet '
              'till solen (1,989·10³⁰ kg) är 1,496·10¹¹ m.</p>', '<p>Både jorden och solen drar i månen.</p>'),
             ('byt', '<p>De angivna avstånden är centrumavstånd. Bortse från andra himlakroppar.</p>',
              '<p>Bortse från andra himlakroppar.</p>'),
             ('kg', ['Månens massa är 7,35·10²² kg, jordens massa 5,97·10²⁴ kg och solens massa 1,989·10³⁰ kg. '
                     'Avståndet mellan jordens och månens centrum är 3,84·10⁸ m och mellan solens och månens centrum '
                     '1,496·10¹¹ m.'], 'alla')],
    '4.840': [('byt', ' Där är tyngdaccelerationen 1,62 N/kg.', ''), ('kg', [MANEN], 'alla')],
    '4.736': [('byt', 'mellan protonen (\\(1{,}67\\cdot10^{-27}\\) kg) och elektronen (\\(9{,}11\\cdot10^{-31}\\) kg) i '
               'en väteatom', 'mellan protonen och elektronen i en väteatom'),
              ('kg', ['Protonens massa är 1,67·10⁻²⁷ kg och elektronens massa är 9,11·10⁻³¹ kg.'], 'b'),
              ('kg', ['Protonens massa är 1,67·10⁻²⁷ kg och elektronens massa är 9,11·10⁻³¹ kg.'], 'uppgift')],
    '4.738': [('byt', 'Anta att bollarna är klot med jämnt fördelad massa. De behåller sin form.',
               'Anta att bollarna är klot med jämnt fördelad massa.')],
    '4.745': [('byt', 'Anta att bollarna är klot med jämnt fördelad massa. De behåller sin form.',
               'Anta att bollarna är klot med jämnt fördelad massa.')],
    '4.749': [('tbyt', '<li>Hur lång tid tar fallet?</li><li>Hur lång tid tar samma fall på asteroiden? Bortse från '
               'luftmotstånd. Tyngdaccelerationen är konstant under fallet.</li></ol>',
               '<li>En sten släpps 1,0 m över marken på jorden. Hur lång tid tar fallet?</li><li>Hur lång tid tar '
               'samma fall på asteroiden?</li></ol><p>Bortse från luftmotstånd.</p>')],
    # blandat_kraft
    '4.281': [('byt', 'Bestäm accelerationen i m/s² med samma kraftsumma.', 'Bestäm accelerationen med samma kraftsumma.')],
    '4.157': [('byt', ' Bestäm värdena på grafens raka delar.', '')],
    '4.282': [('byt', ' Räkna från det att paketet har lagts ned, utan vertikal acceleration.',
               ' Räkna tiden från det att paketet läggs ned.')],
    # lutande_plan
    '4.578': [('byt', 'Hur stor är normalkraften i N?', 'Hur stor är normalkraften?')],
    '4.579': [('byt', 'Hur stor är normalkraften i N?', 'Hur stor är normalkraften?')],
    '4.580': [('byt', 'Hur stor kraft måste Greger skjuta med i N?', 'Hur stor kraft måste Greger skjuta med?')],
    '4.585': [('byt', 'Bestäm accelerationen i m/s² om', 'Bestäm accelerationen om')],
    '4.594': [('byt', 'Vilken acceleration får hon då i m/s²?', 'Vilken acceleration får hon då?')],
    '4.635': [('delfraga', 'a', 'Vilken vinkel har den första backen mot marken?'),
              ('delfraga', 'b', 'Hur långt glider Johan uppför backen som lutar 20°?')],
    # moment
    '4.245': [('byt', 'Hur stor blir den övre kraften i N?', 'Hur stor blir den övre kraften?')],
    '4.297': [('byt', ' I det allmänna uttrycket är L > 0 och d ≥ 0.', '')],
    # newton2
    '4.402': [('byt', 'krafterna på föremålet', 'krafterna på bollen')],
    '4.149': [('byt', 'och från friktionen.</p>', 'och från friktionen i trissan.</p>')],
    '4.206': [('delbyt', 'c', 'Personen hänger nu stilla i en hand. ', '')],
    '4.700': [('byt', 'Anta att bromsaccelerationen är konstant och har storleken \\(30g\\). En förare',
               'Anta att bromsaccelerationen är konstant. En förare')],
    '4.689': [('delbyt', 'a', 'En proton har massan \\(1{,}67\\cdot10^{-27}\\) kg. Den påverkas', 'En proton påverkas'),
              ('kg', ['Protonens massa är 1,67·10⁻²⁷ kg.'], 'a'), ('kg', ['Protonens massa är 1,67·10⁻²⁷ kg.'], 'uppgift')],
}
for _uid in ('3.334', '3.335', '3.336', '3.337', '3.341', '3.342', '3.343', '3.344'):
    OPS[_uid] = [('byt', VEKTORTIPS, '')]

# Kedjor: id -> (frågor på papperet, delkortens frågor eller None)
KEDJOR = {
    '4.102': (['Bestäm friktionskraftens storlek.', 'Bestäm den resulterande horisontella kraften.'], None),
}


def kg_med(kg, meningar):
    kg = (kg or '').strip()
    for m in meningar:
        if m not in kg:
            kg = (kg + ' ' + m).strip()
    return kg


def texter(q, delar=True, uppgift=True):
    if uppgift:
        for k in ('t', 'spelIntro'):
            if isinstance(q.get(k), str):
                yield q, k
    if delar:
        for d in q.get('spelDelar') or []:
            for k in ('t', 'fraga'):
                if isinstance(d.get(k), str):
                    yield d, k


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    idx = {q['id']: q for q in bank}
    nya = {}

    def hamta(uid):
        if uid not in nya:
            nya[uid] = json.loads(json.dumps(idx[uid]))
        return nya[uid]

    # ”Antag” → ”Anta” i hela kapitel 4
    antag = []
    for q0 in bank:
        if q0.get('kap') == 4 and any(re.search(r'\bAntag(?= )', o[k]) for o, k in texter(q0)):
            q = hamta(q0['id'])
            for o, k in texter(q):
                o[k] = re.sub(r'\bAntag(?= )', 'Anta', o[k])
            antag.append(q0['id'])
    for uid, ops in OPS.items():
        q = hamta(uid)
        for op in ops:
            if op[0] in ('byt', 'tbyt', 'delbyt'):
                if op[0] == 'delbyt':
                    _, et, gl, ny = op
                    falt = [(d, k) for d in q['spelDelar'] if d['etikett'] == et for k in ('t', 'fraga') if d.get(k)]
                else:
                    _, gl, ny = op
                    falt = [(q, 't')] if op[0] == 'tbyt' else list(texter(q))
                n = 0
                for o, k in falt:
                    n += o[k].count(gl)
                    o[k] = o[k].replace(gl, ny)
                assert n >= 1, (uid, gl)
            elif op[0] == 'kg':
                _, meningar, vem = op
                if vem in ('alla', 'uppgift'):
                    q['kgInstruktion'] = kg_med(q.get('kgInstruktion'), meningar)
                for d in q.get('spelDelar') or []:
                    if vem == 'alla' or vem == d['etikett']:
                        d['kgInstruktion'] = kg_med(d.get('kgInstruktion'), meningar)
            elif op[0] == 'delfraga':
                _, et, fraga = op
                d = next(d for d in q['spelDelar'] if d['etikett'] == et)
                d['fraga'] = fraga
                d['t'] = q['spelIntro'] + f'<p>{fraga}</p>'
    for uid, (fragor, kortfragor) in KEDJOR.items():
        q = hamta(uid)
        intro = q['spelIntro']
        assert q['t'].startswith(intro + '<ol type="a">'), uid
        q['t'] = intro + '<ol type="a">' + ''.join(f'<li>{f}</li>' for f in fragor) + '</ol>'
        for d, f in zip(q['spelDelar'], kortfragor or fragor, strict=True):
            d['fraga'] = f
            d['t'] = intro + f'<p>{f}</p>'

    ny_src = src
    for uid, q in nya.items():
        start = ny_src.index('"id": ' + json.dumps(uid))
        indrag = '  ' if ny_src.rfind('\n  {', 0, start) > ny_src.rfind('\n{', 0, start) else ''
        a = ny_src.rfind('\n' + indrag + '{', 0, start) + 1 + len(indrag)
        slut = ny_src.index('\n' + indrag + '}', start) + 2 + len(indrag)
        assert json.loads(ny_src[a:slut]) == idx[uid], uid
        ny_src = (ny_src[:a] + json.dumps(q, ensure_ascii=False, indent=2).replace('\n', '\n' + indrag)
                  + ny_src[slut:])
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = {x['id']: sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k)) for x, y in zip(efter, bank) if x != y}
    assert set(andr) == set(nya), set(andr) ^ set(nya)
    for uid, k in andr.items():
        assert not ({'s', 'rättSvar', 'svarEnhet', 'tolerans'} & set(k)), (uid, k)
        x = next(e for e in efter if e['id'] == uid)
        for o, kk in texter(x):
            assert '<p></p>' not in o[kk] and 'Antag ' not in o[kk] and 'modelleras' not in o[kk], (uid, kk)
        for d in x.get('spelDelar') or []:
            for falt in ('s', 'ledtrad', 'rättSvar'):
                y = next(e for e in bank if e['id'] == uid)
                yd = next(e for e in y['spelDelar'] if e['etikett'] == d['etikett'])
                assert d.get(falt) == yd.get(falt), (uid, d['etikett'], falt)
    print(len(andr), 'uppgifter; Antag→Anta i', len(antag), ':', ' '.join(antag))
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)


if __name__ == '__main__':
    main()
