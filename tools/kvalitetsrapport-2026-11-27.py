"""Kvalitetsrapporten i Kunskapsgymmet 2026-11-27: Ma2 3.67 kunde inte rättas, och i Fy1 4.852 låg en etikett på
rampens kant.

`rättSvar` var LaTeX-strängen \\(y=45^\\circ-\\frac{x}{2}\\) utan `svarFormat`, så Kunskapsgymmet underkände alla
rimliga svar (y=45-x/2, 45°-x/2, y=45-0,5x). Facit är rätt: medelpunktsvinkeln är 2x, ∠MBA = 90° − x,
∠MBD = 90° + x och y = (180° − (90° + x))/2 = 45° − x/2. Nu är `rättSvar` "y=45-x/2" med `svarFormat` "uttryck",
som Ma2:s övriga uttryckssvar. Text och facit är oförändrade.

Fy1 4.852: etiketten ”f = 20 N” stod över rampens lutande kant. Den flyttas ned i rampen, under kanten och nära
friktionspilens spets (338, 130 → 335, 178), där den varken krockar med lådan eller kanten.

Fy1, inledningar i plural (kontrollen ”Kortinledning i plural”): på ett delkort med en enda fråga blir ”i varje
del” och ”i alla tre fallen” konstigt. Inledningarna i 4.747, 4.647, 6.88, 6.530, 6.538 och 7.139 skrivs om så att de
fungerar både på papper och på kort. Frågor, tal och facit är oförändrade.

  python tools/kvalitetsrapport-2026-11-27.py [--skriv]
"""
import json
import os
import sys

ROT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
FIL = os.path.join(ROT, 'uppgifterma2.js')
FY1 = os.path.join(ROT, 'uppgifter.js')
F_GL = '<text x=\\"338\\" y=\\"130\\" fill=\\"#22764a\\" font-family=\\"Arial,sans-serif\\" font-size=\\"18\\" text-anchor=\\"middle\\">f = 20 N'
F_NY = '<text x=\\"335\\" y=\\"178\\" fill=\\"#22764a\\" font-family=\\"Arial,sans-serif\\" font-size=\\"18\\" text-anchor=\\"middle\\">f = 20 N'


def fy1_4852(skriv):
    src = open(FY1, encoding='utf-8', newline='').read()
    if F_NY in src and F_GL not in src:
        print('4.852 redan flyttad')
        return
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    assert src.count(F_GL) == 1
    src = src.replace(F_GL, F_NY)
    efter = json.loads(src[src.index('['):src.rindex(']') + 1])
    andr = [x['id'] for x, y in zip(efter, fore) if x != y]
    assert andr == ['4.852'], andr
    print(andr)
    if skriv:
        with open(FY1, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src)


PLURAL = {
    '4.747': [('Utgå från detta ursprungliga fall i varje del.', 'Utgå hela tiden från de ursprungliga värdena.')],
    '4.647': [('Vikten är stilla relativt hissen i varje fall.', 'Vikten är stilla i förhållande till hissen.')],
    '6.88': [('Varje del beskriver en instängd gas före och efter en förändring.', 'En instängd gas förändras.')],
    '6.530': [('Varje del beskriver en instängd gas.', 'En instängd gas byter tillstånd.')],
    '6.538': [('I alla tre fallen är temperaturen och gasmängden konstanta.', 'Temperaturen och gasmängden är konstanta.')],
    '7.139': [('Bestäm den specifika värmekapaciteten i varje fall.', 'Tre olika metallbitar värms upp.')],
}


def fy1_plural(skriv):
    src = open(FY1, encoding='utf-8', newline='').read()
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    ny = src
    for uid, byten in PLURAL.items():
        for gl, nytt in byten:
            a = json.dumps(gl, ensure_ascii=False)[1:-1]
            b = json.dumps(nytt, ensure_ascii=False)[1:-1]
            if a not in ny and b in ny:
                continue
            assert ny.count(a) >= 2, (uid, ny.count(a))   # minst t och spelIntro
            ny = ny.replace(a, b)
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = sorted(x['id'] for x, y in zip(efter, fore) if x != y)
    assert set(andr) <= set(PLURAL), andr
    for x in efter:
        if x['id'] in PLURAL:
            d = x.get('spelDelar') or []
            for k in ['t', 'spelIntro'] + [f'del{i}' for i in range(len(d))]:
                v = x.get(k) if k in ('t', 'spelIntro') else d[int(k[3:])]['t']
                assert not any(gl in (v or '') for gl, _ in PLURAL[x['id']]), (x['id'], k)
    print('plural', andr)
    if skriv and andr:
        with open(FY1, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


def objekt_spann(src, uid):
    dec = json.JSONDecoder()
    i = src.index('[') + 1
    while True:
        while src[i] in ' \n\r\t,':
            i += 1
        obj, slut = dec.raw_decode(src, i)
        if str(obj.get('id')) == uid:
            return i, slut, obj
        i = slut


def main():
    fy1_4852('--skriv' in sys.argv)
    fy1_plural('--skriv' in sys.argv)
    src = open(FIL, encoding='utf-8', newline='').read()
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    a, b, q = objekt_spann(src, '3.67')
    if q['rättSvar'] == 'y=45-x/2':
        print('3.67 redan ändrad')
        return
    assert q['rättSvar'] == '\\(y=45^\\circ-\\frac{x}{2}\\)' and 'svarFormat' not in q
    ny = dict(q)
    ny['rättSvar'] = 'y=45-x/2'
    # svarFormat direkt efter rättSvar
    ordnad = {}
    for k, v in ny.items():
        ordnad[k] = v
        if k == 'rättSvar':
            ordnad['svarFormat'] = 'uttryck'
    bit = src[a:b]
    kompakt = '\n' not in bit
    text = json.dumps(ordnad, ensure_ascii=False, indent=None if kompakt else 2)
    if not kompakt:
        ind = src[src.rfind('\n', 0, a) + 1:a]
        text = text.replace('\n', '\n' + ind)
    src = src[:a] + text + src[b:]
    efter = json.loads(src[src.index('['):src.rindex(']') + 1])
    andr = [(x['id'], sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))) for x, y in zip(efter, fore) if x != y]
    assert andr == [('3.67', ['rättSvar', 'svarFormat'])], andr
    print(andr)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src)


if __name__ == '__main__':
    main()
