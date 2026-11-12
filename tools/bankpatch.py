"""Byter enskilda uppgifter i en bankfil utan att röra resten av filens format."""
import json
import re


def hitta(src, uid):
    """(start, slut, objekt, indrag) för uppgiften med id uid."""
    m = list(re.finditer(r'"id"\s*:\s*"' + re.escape(uid) + '"', src))
    assert len(m) == 1, (uid, len(m))
    pos = m[0].start()
    dec = json.JSONDecoder()
    start = src.rfind('{', 0, pos)
    while True:
        try:
            obj, slut = dec.raw_decode(src, start)
            if obj.get('id') == uid:
                break
        except json.JSONDecodeError:
            pass
        start = src.rfind('{', 0, start)
        assert start >= 0, uid
    radstart = src.rfind('\n', 0, start) + 1
    indrag = src[radstart:start]
    return start, slut, obj, indrag


def dumpa(obj, indrag, kompakt):
    if kompakt:
        return json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
    txt = json.dumps(obj, ensure_ascii=False, indent=2)
    return txt.replace('\n', '\n' + indrag)


def andra(fil, andringar):
    """andringar: {id: funktion(obj) -> None}. Kontrollerar att oförändrad dump återger originalet."""
    src = open(fil, encoding='utf-8').read()
    for uid, fn in andringar.items():
        start, slut, obj, indrag = hitta(src, uid)
        orig = src[start:slut]
        kompakt = '\n' not in orig
        assert dumpa(obj, indrag, kompakt) == orig, f'{uid}: formatet kan inte återges'
        fn(obj)
        src = src[:start] + dumpa(obj, indrag, kompakt) + src[slut:]
    json.loads(src[src.index('['):src.rindex(']') + 1])
    with open(fil, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src)
