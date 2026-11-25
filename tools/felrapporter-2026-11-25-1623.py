"""Felrapporter Uppgiftslabbet 2026-11-25 16:23.

Ma2 4.2036 och 4.2040 (lådagram, spår 2c), tagg ”Fel nivå / poäng”: nuvarande C · 0/1/0, lärarbedömning (1/0/0).
Uppgifterna (bestämma två okända värden ur lådagrammets minsta värde och median, respektive välja det datamaterial som
har lådagrammets median och kvartiler) är ett rakt användande av definitionerna. Nivån sätts till E med poängen 1/0/0
och träningsnivån till 2 (E-uppgifter har träningsnivå 1–2). Text, facit och svar är oförändrade.

Fy1 3.63 (”konstig bild, cyklisten syns inte”) och 2.18 (zinks densitet 7,13 g/cm³) åtgärdades redan 2026-11-23 i
commit 7bf6e0a och ändras inte här.

  python tools/felrapporter-2026-11-25-1623.py [--skriv]
"""
import json
import os
import sys

sys.dont_write_bytecode = True

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifterma2.js')


def objekt_spann(src, uid):
    """(start, slut) för objektet med id uid, även när flera objekt står på samma rad."""
    dec = json.JSONDecoder()
    i = src.index('[') + 1
    while True:
        while src[i] in ' \n\r\t,':
            i += 1
        obj, slut = dec.raw_decode(src, i)
        if str(obj.get('id')) == uid:
            return i, slut
        i = slut


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    fore = json.loads(src[src.index('['):src.rindex(']') + 1])
    for uid in ('4.2036', '4.2040'):
        a, b = objekt_spann(src, uid)
        bit = src[a:b]
        for falt, gl, ny in (('niva', '"C"', '"E"'), ('poang', '"0/1/0"', '"1/0/0"'), ('traningsniva', '3', '2')):
            hit = [m for m in (f'"{falt}": {gl}', f'"{falt}":{gl}') if bit.count(m) == 1]
            assert len(hit) == 1, (uid, falt)
            bit = bit.replace(hit[0], hit[0].replace(gl, ny))
        src = src[:a] + bit + src[b:]
    efter = json.loads(src[src.index('['):src.rindex(']') + 1])
    andr = [(x['id'], sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))) for x, y in zip(efter, fore) if x != y]
    assert andr == [('4.2036', ['niva', 'poang', 'traningsniva']), ('4.2040', ['niva', 'poang', 'traningsniva'])], andr
    print(andr)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src)


if __name__ == '__main__':
    main()
