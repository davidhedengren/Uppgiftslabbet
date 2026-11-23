"""”Motivera ditt svar.” efter ja/nej- och valfrågor, som i lärarens prov (korpus 2026-11-23), och en trasig
mening i Fy1 6.182 och 6.536.

Korpusen har ”Motivera ditt svar.” 7,5 gånger per 1 000 meningar i matematik, banken 1,1. Uppgifter med en ensam
ja/nej- eller valfråga utan motivering får meningen sist. I Kunskapsgymmet säger `kgInstruktion` hur svaret skrivs:
”Börja svaret med ja eller nej.” (rättningen godtar ”Ja, eftersom …”) eller ”Svara med ett ord: …” där
rättningen bara godtar ordet.

Fy1 6.182 och 6.536: ”Är temperaturen konstant, gasmängden oförändrad och lungluftens tryck lika med vattnets
tryck.” var en påståendemening med frågeordföljd. Nu: ”Antag att temperaturen är konstant, att gasmängden inte
ändras och att lungluftens tryck är lika med vattnets tryck.”

Bara strängliteralerna byts eller läggs till, så filernas format behålls.

  python tools/sprak/omskr/motivera_2026-11-23.py [--skriv]
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
JANEJ = 'Börja svaret med ja eller nej.'
PLAN = {
    'uppgifterma1.js': {'5.27': JANEJ},
    'uppgiftermato1.js': {'3.171': None, '3.190': None},
    'uppgiftermatf1.js': {i: JANEJ for i in ['1.483', '2.511', '2.512', '2.513', '2.521', '1.574', '2.553', '3.267',
                                             '3.268', '4.506']}
    | {'3.273': 'Svara med ett ord: konvergent eller divergent.',
       '3.276': 'Svara med ett ord: konvergent eller divergent.'},
    'uppgifter2.js': {i: 'Svara med ett ord: nordpol eller sydpol.' for i in ['3.209', '3.210', '3.213', '3.214']}
    | {'2.108': None},
}
TRASIG = ('Är temperaturen konstant, gasmängden oförändrad och lungluftens tryck lika med vattnets tryck.',
          'Antag att temperaturen är konstant, att gasmängden inte ändras och att lungluftens tryck är lika med '
          'vattnets tryck.')


def objekt_spann(src, uid):
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import bankobjekt as B
    for start, slut, obj in B.spann(src):
        if str(obj.get('id')) == uid:
            return start, slut, obj
    raise AssertionError(uid)


def main():
    for fil, plan in PLAN.items():
        path = os.path.join(ROOT, fil)
        src = open(path, encoding='utf-8', newline='').read()
        fore = json.loads(src[src.index('['):src.rindex(']') + 1])
        for uid, kg in plan.items():
            start, slut, obj = objekt_spann(src, uid)
            bit = src[start:slut]
            t = obj['t']
            assert 'Motivera' not in t, uid
            ny_t = re.sub(r'(\?)(</p>)\s*$', r'\1 Motivera ditt svar.\2', t)
            assert ny_t != t, uid
            lit = json.dumps(t, ensure_ascii=False)
            assert bit.count(lit) == 1, uid
            bit = bit.replace(lit, json.dumps(ny_t, ensure_ascii=False))
            if kg:
                if 'kgInstruktion' in obj:
                    gl = '"kgInstruktion": ' + json.dumps(obj['kgInstruktion'], ensure_ascii=False)
                    gl2 = '"kgInstruktion":' + json.dumps(obj['kgInstruktion'], ensure_ascii=False)
                    if gl in bit:
                        bit = bit.replace(gl, '"kgInstruktion": ' + json.dumps(kg, ensure_ascii=False), 1)
                    else:
                        assert gl2 in bit, uid
                        bit = bit.replace(gl2, '"kgInstruktion":' + json.dumps(kg, ensure_ascii=False), 1)
                else:
                    m = re.search(r'\n(\s*)"t": ', bit)
                    if m:
                        ind = m.group(1)
                        bit = bit.replace(json.dumps(ny_t, ensure_ascii=False),
                                          json.dumps(ny_t, ensure_ascii=False) + ',\n' + ind + '"kgInstruktion": '
                                          + json.dumps(kg, ensure_ascii=False), 1)
                    else:
                        bit = bit.replace(json.dumps(ny_t, ensure_ascii=False),
                                          json.dumps(ny_t, ensure_ascii=False) + ',"kgInstruktion":'
                                          + json.dumps(kg, ensure_ascii=False), 1)
            src = src[:start] + bit + src[slut:]
        efter = json.loads(src[src.index('['):src.rindex(']') + 1])
        andr = [q['id'] for q, r in zip(efter, fore) if q != r]
        assert sorted(andr) == sorted(plan), (fil, set(andr) ^ set(plan))
        for q, r in zip(efter, fore):
            if q != r:
                assert {k for k in set(q) | set(r) if q.get(k) != r.get(k)} <= {'t', 'kgInstruktion'}, q['id']
        print(fil, len(andr))
        if '--skriv' in sys.argv:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(src)
    # Fy1 6.182 och 6.536
    path = os.path.join(ROOT, 'uppgifter.js')
    src = open(path, encoding='utf-8', newline='').read()
    assert src.count(TRASIG[0]) == 2, src.count(TRASIG[0])
    src = src.replace(TRASIG[0], TRASIG[1])
    json.loads(src[src.index('['):src.rindex(']') + 1])
    print('uppgifter.js 6.182, 6.536')
    if '--skriv' in sys.argv:
        with open(path, 'w', encoding='utf-8', newline='') as fh:
            fh.write(src)


if __name__ == '__main__':
    main()
