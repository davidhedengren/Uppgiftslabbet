"""Manuell granskning av Fy1 densitet (omgång 2), 2026-11-27.

Alla 193 uppgifter i området är lästa och kontrollräknade. Ändringar:

1. Tabelldensiteter som stod kvar i uppgiftstexten flyttas till `kgInstruktion` (användarbeslut 2026-11-27: densiteter
   och andra tabellvärden står bara i kgInstruktion, aldrig i frågetexterna). Värdet läggs på uppgiften och på varje
   delkort. Kvar i texten står, enligt undantagen: omvandlingsuppgifter där densiteten är uppgiftens tal (2.6, 2.107,
   2.108, 2.111, 2.113), uppgifter där eleven identifierar eller jämför ämnen (2.24, 2.40, 2.88, 2.92, 2.100, 2.101,
   2.104, 2.106, 2.165, 2.169, 2.188), värden i en formel eller ett påstående (2.51, 2.116) och uppgiftens egna
   material (trä, plast, granit, saltvatten, ägg, sten, spolarvätska, saft, palladium i 2.201).
   2.367: vattnets och glykolens densitet saknades helt i delkortens instruktion; nu finns de där.
2. ”Antag” → ”Anta” (2.142, 2.184, 2.195), som i resten av banken.

Svar och facit är oförändrade.

  python tools/fy1-granskning-densitet-2026-11-27.py [--skriv]
"""
import json
import os
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

# id -> (ersättningar i frågetexterna, meningar som ska finnas i kgInstruktion)
ANDR = {
    '2.117': ([(' Titanets densitet är 4,51 g/cm³.', '')], ['Titanets densitet är 4,51 g/cm³.']),
    '2.122': ([(' Massan är 340 g och mässing har densiteten 8,50 g/cm³.', ' Massan är 340 g.')], []),
    '2.125': ([(' Titan har densiteten 4,51 g/cm³.', '')], ['Titanets densitet är 4,51 g/cm³.']),
    '2.132': ([(' Glycerol har densiteten 1,26 g/cm³.', '')], ['Glycerolens densitet är 1,26 g/cm³.']),
    '2.143': ([(' Aluminium har densiteten 2,70 g/cm³ och plasten 1,20 g/cm³.', ' Plasten har densiteten 1,20 g/cm³.')],
              []),
    '2.147': ([('Den ena är av titan med densiteten 4,51 g/cm³ och den andra av aluminium.',
                'Den ena är av titan och den andra av aluminium.')], ['Titanets densitet är 4,51 g/cm³.']),
    '2.149': ([('och flyter stilla i vatten, som har densiteten 1,00 g/cm³.', 'och flyter stilla i vatten.')], []),
    '2.150': ([('Is har densiteten 0,917 g/cm³ och flyter stilla i vatten, som har densiteten 1,00 g/cm³.',
                'En isbit flyter stilla i vatten.')], []),
    '2.157': ([(' Densiteter: guld \\(19{,}3\\ \\mathrm{g/cm^3}\\), platina \\(21{,}5\\ \\mathrm{g/cm^3}\\).', '')],
              ['Guldets densitet är 19,3 g/cm³.', 'Platinans densitet är 21,5 g/cm³.']),
    '2.158': ([(' Densiteter: stål \\(7{,}80\\ \\mathrm{g/cm^3}\\), uran \\(19{,}1\\ \\mathrm{g/cm^3}\\).', '')],
              ['Stålets densitet är 7,80 g/cm³.', 'Uranets densitet är 19,1 g/cm³.']),
    '2.162': ([(' och densiteten 7800 kg/m³. Plåten', '. Plåten')], []),
    '2.198': ([(' Etanol har densiteten 0,789 g/cm³ och glycerol 1,26 g/cm³.', '')], ['Glycerolens densitet är 1,26 g/cm³.']),
    '2.201': ([(' Guld har densiteten 19,3 g/cm³, silver 10,5 g/cm³ och palladium 12,0 g/cm³.',
                ' Palladium har densiteten 12,0 g/cm³.')], []),
    '2.202': ([(' Glycerol har densiteten 1,26 g/cm³ och metanol 0,792 g/cm³.', '')],
              ['Glycerolens densitet är 1,26 g/cm³.', 'Metanolens densitet är 0,792 g/cm³.']),
    '2.203': ([(' Densiteterna är 19,3 g/cm³ för guld, 2,70 g/cm³ för aluminium och 10,5 g/cm³ för silver.', '')], []),
    '2.274': ([(' Densiteterna är \\(2{,}70\\,\\mathrm{g/cm^3}\\) för aluminium och \\(7{,}80\\,\\mathrm{g/cm^3}\\) för stål.',
                '')], ['Aluminiumets densitet är 2,70 g/cm³.', 'Stålets densitet är 7,80 g/cm³.']),
    '2.277': ([(' Aluminium har densiteten 2,70 g/cm³ och stål 7,80 g/cm³.', '')], []),
    '2.367': ([('<p>Vatten har densiteten 1,00 g/cm³ och glykol 1,11 g/cm³. Anta att', '<p>Anta att'),
               ('<p>Glykol har densiteten 1,11 g/cm³. Anta att', '<p>Anta att')],
              ['Vattnets densitet är 1,00 g/cm³.', 'Glykolens densitet är 1,11 g/cm³.']),
    '2.368': ([('<p>Is har densiteten 0,917 g/cm³, stenen 2,60 g/cm³ och vattnet 1,00 g/cm³.</p>',
                '<p>Stenen har densiteten 2,60 g/cm³.</p>')], ['Vattnets densitet är 1,00 g/cm³.']),
    '2.373': ([(' Lisa häller sedan i vanligt vatten, som har densiteten 1,00 g/cm³.',
                ' Lisa häller sedan i vanligt vatten.')], []),
    '2.375': ([('<p>Is har densiteten 0,917 g/cm³, fotogen 0,800 g/cm³ och vatten 1,00 g/cm³.</p>', '')],
              ['Isens densitet är 0,917 g/cm³.', 'Fotogenens densitet är 0,800 g/cm³.', 'Vattnets densitet är 1,00 g/cm³.']),
    '2.142': ([('Antag att den totala volymen', 'Anta att den totala volymen')], []),
    '2.184': ([('Antag att guld kostar', 'Anta att guld kostar')], []),
    '2.195': ([('Antag att jorden är', 'Anta att jorden är')], []),
}


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
    for uid, (byten, meningar) in ANDR.items():
        q = json.loads(json.dumps(idx[uid]))
        for gl, ny in byten:
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
        if meningar:
            q['kgInstruktion'] = kg_med(q.get('kgInstruktion'), meningar)
            for d in q.get('spelDelar') or []:
                d['kgInstruktion'] = kg_med(d.get('kgInstruktion'), meningar)
        nya[uid] = q
    ny_src = src
    for uid, q in nya.items():
        gq = idx[uid]
        start = ny_src.index('"id": ' + json.dumps(uid))
        a = ny_src.rfind('\n  {', 0, start) + 3
        slut = ny_src.index('\n  }', start) + 4
        gammal = ny_src[a:slut]
        assert json.loads(gammal) == gq, uid
        # behåll filens format: objektet indraget två steg, en nyckel per rad
        nytt = json.dumps(q, ensure_ascii=False, indent=2).replace('\n', '\n  ')
        ny_src = ny_src[:a] + nytt + ny_src[slut:]
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = {x['id']: sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k)) for x, y in zip(efter, bank) if x != y}
    assert set(andr) == set(ANDR), set(andr) ^ set(ANDR)
    for uid, k in andr.items():
        assert not ({'s', 'rättSvar', 'svarEnhet'} & set(k)), (uid, k)
        print(uid, k)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)


if __name__ == '__main__':
    main()
