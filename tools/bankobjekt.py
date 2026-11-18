"""Byt hela uppgiftsobjekt i en bankfil utan att formatet i resten av filen ändras.

Bankfilerna är skrivna med json.dumps(..., indent=2, ensure_ascii=False), där varje uppgift står på nivån "  {"
(uppgifter som lagts till senare kan stå på nivån "{"; indraget behålls).
`spann(src)` ger (start, slut) för varje uppgifts text i filen, och `ersatt(src, nya)` skriver om de objekt vars id
finns i `nya` med samma indrag. `kontrollera_rundresa(fil)` visar att omskrivningen ger exakt samma text för
oförändrade objekt.
"""
import json
from pathlib import Path


def las(fil):
    src = Path(fil).read_text(encoding='utf-8')
    return src, json.loads(src[src.index('['):src.rindex(']') + 1])


def _dump(obj, prefix='  '):
    return '\n'.join(prefix + rad for rad in json.dumps(obj, ensure_ascii=False, indent=2).split('\n'))


def _prefix(src, start):
    rad = src[start:src.index('{', start)]
    return rad if not rad.strip() else '  '


def spann(src):
    """Startindex för "  {" och slutindex efter "  }" för varje uppgift, i filens ordning."""
    dec = json.JSONDecoder()
    i = src.index('[') + 1
    ut = []
    while True:
        while src[i] in ' \n\r\t,':
            i += 1
        if src[i] == ']':
            return ut
        start = src.rindex('\n', 0, i) + 1
        obj, slut = dec.raw_decode(src, i)
        ut.append((start, slut, obj))
        i = slut


def ersatt(src, nya):
    """nya: {id: nytt objekt}. Byter bara de objekten."""
    delar, pos, gjorda = [], 0, set()
    for start, slut, obj in spann(src):
        uid = str(obj.get('id'))
        if uid in nya:
            delar.append(src[pos:start])
            delar.append(_dump(nya[uid], _prefix(src, start)))
            pos = slut
            gjorda.add(uid)
    delar.append(src[pos:])
    saknas = set(nya) - gjorda
    assert not saknas, saknas
    return ''.join(delar)


def kontrollera_rundresa(fil, ids=None):
    src, _ = las(fil)
    fel = []
    for start, slut, obj in spann(src):
        if ids is None or str(obj.get('id')) in ids:
            if src[start:slut] != _dump(obj, _prefix(src, start)):
                fel.append(obj.get('id'))
    return fel


def skriv(fil, src):
    json.loads(src[src.index('['):src.rindex(']') + 1])
    with open(fil, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src)
