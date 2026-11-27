"""Felrapporter Kunskapsgymmet 2026-11-27 08:09, Fy1.

4.271 del b (lärare: ”Lite väl många värdesiffror krävs”). `svarVardesiffror` var [5, 6, 3], så Kunskapsgymmet
krävde 122,75 N och 3068,75 N/m fast de givna värdena (75 kg, 4,0 cm) har två värdesiffror. Samma fel fanns i fler
Fy1-uppgifter: värdesiffrorna hade satts efter antalet siffror i facits svarsrad (två decimaler), inte efter de givna
värdena. Varje uppgift med 5–7 värdesiffror har bedömts för sig (tabellen VS nedan):
- värdesiffrorna följer de minst noggranna givna värdena (Kunskapsgymmet godtar n−2 till n+2 vid korrekt avrundning);
- absoluttryck (lufttryck plus vätsketryck) får 4, så att bara lufttrycket (≈ 100 kPa) inte godtas med en värdesiffra;
- oförändrade: omvandlingar mellan °C och K (6.38, 6.138, 7.31), atommassor (9.389, 9.392, 9.397, 9.403, 9.572) och
  uppgifter med fyrsiffriga data (6.505 a, 5.470 a), där precisionen behövs;
- facit är oförändrat (användarbeslut 2026-11-24: facits antal värdesiffror spelar ingen roll, men rimligt avrundade
  svar ska godtas). `rättSvar` är oförändrat, utom 4.271 c där det avrundade 5,33 ersätts med det exakta 16/3.
4.271 får också en enklare inledning (”Den extra lasten”, utan ”Bortse från övrig deformation”).

3.283 del a (elev: ”Frågan är otydlig”, utan kommentar). Figuren stämmer (spetsen i (5, −2)), men frågan sa bara
”x-komposant”. Nu står vad komposanten betyder (hur långt personen förflyttar sig i x-led respektive y-led) och vilken
riktning som räknas positivt. Svaren 5 m och −2 m är oförändrade.

  python tools/felrapporter-2026-11-27-0809.py [--skriv]
"""
import json
import os
import re
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

# id -> nya svarVardesiffror (lista per del eller tal). None = delen är oförändrad.
VS = {
    '3.158': [4, 2, 4], '4.4': [3, 3, 3, 3], '4.24': [4, 3], '4.82': [4, 2], '4.85': [1, 2, 2, 1, 4],
    '4.97': [2, 2], '4.98': [2, 2, None], '4.206': [4, 2, 4, 4], '4.230': [3, 1, 3, 2], '4.236': [3, 3],
    '4.271': [2, 2, 2], '4.575': [2, 2, 2], '4.655': [None, 2, None], '5.24': [2, 3, 4, 4], '5.32': [1, 3, 3, 2],
    '5.52': [3, 2, 4], '5.59': [2, None], '5.68': 2, '5.100': [2, 4], '5.114': [2, 2], '5.115': [4, 2],
    '5.123': [2, 4], '5.124': [2, 2], '5.126': [2, 4], '5.132': [3, 3, 2, 2], '5.133': [None, None, 2],
    '5.158': [3, 2, 1], '6.2': [4, 2, 2], '6.8': [2, 4, 3], '6.255': 4, '6.309': 4, '6.327': 2, '6.308': 2,
    '6.152': [4, 5], '6.52': [3, 4, 2], '6.59': [2, 3], '6.258': 2, '6.259': 4, '6.97': 2, '6.246': 2, '6.265': 4,
    '6.155': [2, 2], '6.109': [3, 2, 2], '6.133': [3, 3, 2], '6.249': 3, '4.313': 3, '4.316': 2, '3.203': [None, 3],
    '3.213': 2, '3.214': 3, '3.215': 2, '5.187': 2, '5.191': 2, '3.377': [4, 4, 2], '3.386': [4, 4, 2, 3],
    '3.389': [2, 4, 4], '5.228': [3, 4, 4, 2], '5.243': 2, '3.710': 3, '3.718': 3,
}
ORORDA = {'6.38', '6.138', '7.31', '9.389', '9.392', '9.397', '9.403', '9.572', '6.505', '5.470'}

TEXT = {
    '4.271': [
        ('En soffa stöds av sex likadana fjädrar. När en person som väger 75 kg sitter stilla sjunker soffan ytterligare '
         '4,0 cm jämfört med utan person. Extra lasten fördelas lika på fjädrarna. Bortse från övrig deformation.',
         'En soffa vilar på sex likadana fjädrar. När en person som väger 75 kg sätter sig i soffan sjunker den '
         'ytterligare 4,0 cm. Den extra lasten fördelas lika på fjädrarna.'),
    ],
    '3.283': [
        ('En person går från origo till punkten dit pilen pekar. Pilen \\(s\\) är personens förflyttning. '
         'Skala: 1 ruta = 1 m.',
         'En person går rakt från origo till punkten där pilen slutar. Pilen \\(s\\) visar personens förflyttning. '
         'Varje ruta i rutnätet är 1 m.'),
        ('Bestäm förflyttningens x-komposant \\(s_x\\).',
         'Bestäm förflyttningens x-komposant \\(s_x\\), alltså hur långt personen förflyttar sig i x-led. '
         'Förflyttning åt höger räknas positivt.'),
        ('Bestäm förflyttningens y-komposant \\(s_y\\).',
         'Bestäm förflyttningens y-komposant \\(s_y\\), alltså hur långt personen förflyttar sig i y-led. '
         'Förflyttning uppåt räknas positivt och nedåt negativt.'),
    ],
}

def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    efter_q = {}
    for q in bank:
        uid = q['id']
        if uid not in VS and uid not in TEXT:
            continue
        nq = json.loads(json.dumps(q))
        if uid in VS:
            vs, rs = VS[uid], q['rättSvar']
            gl = q['svarVardesiffror']
            if isinstance(vs, list):
                assert isinstance(gl, list) and len(gl) == len(vs) == len(rs), uid
                nytt = [g if v is None else v for g, v in zip(gl, vs)]
                andrade = [i for i, (g, v) in enumerate(zip(gl, vs)) if v is not None and v != g]
                assert andrade, uid
                assert all(gl[i] >= 5 or uid == '4.271' for i in andrade), (uid, gl)
                assert any(isinstance(g, int) and g >= 5 for g in gl), uid
                nq['svarVardesiffror'] = nytt
            else:
                assert isinstance(gl, int) and gl >= 5 and not isinstance(rs, list), uid
                nq['svarVardesiffror'] = vs
        if uid == '4.271':
            # 5,33 var avrundat; med exakt värde godtas även 5,333 cm
            assert q['rättSvar'][2] == 5.33
            nq['rättSvar'] = [q['rättSvar'][0], q['rättSvar'][1], 4.0 * 100 / 75]
        for gammal, ny in TEXT.get(uid, []):
            antal = 0
            for k, v in list(nq.items()):
                if isinstance(v, str):
                    antal += v.count(gammal)
                    nq[k] = v.replace(gammal, ny)
            for d in nq.get('spelDelar') or []:
                for k, v in list(d.items()):
                    if isinstance(v, str):
                        antal += v.count(gammal)
                        d[k] = v.replace(gammal, ny)
            assert antal >= 2, (uid, gammal[:40], antal)
        efter_q[uid] = nq
    assert set(efter_q) == set(VS) | set(TEXT), set(VS) - set(efter_q)
    assert not (set(VS) & ORORDA)
    # kvarvarande 5+ ska bara vara de medvetet orörda
    for q in bank:
        v = (efter_q.get(q['id']) or q).get('svarVardesiffror')
        vs = v if isinstance(v, list) else [v]
        if any(isinstance(x, int) and x >= 5 for x in vs):
            assert q['id'] in ORORDA or q['id'] == '6.152', q['id']
    ny = src
    for q in bank:
        if q['id'] not in efter_q:
            continue
        nq = efter_q[q['id']]
        for k in nq:
            if nq[k] == q.get(k):
                continue
            a = json.dumps(q[k], ensure_ascii=False)
            b = json.dumps(nq[k], ensure_ascii=False)
            if isinstance(q[k], str):
                assert ny.count(a) == 1, (q['id'], k)
                ny = ny.replace(a, b)
            else:
                # listor och spelDelar: byt fältvärdet inom uppgiftens objekt
                start = ny.index('"id": ' + json.dumps(q['id']))
                slut = ny.index('\n  }', start)
                del_ = ny[start:slut]
                nyckel = json.dumps(k, ensure_ascii=False) + ': '
                i = del_.index(nyckel) + len(nyckel)
                dec = json.JSONDecoder()
                _, j = dec.raw_decode(del_, i)
                gammal_txt = del_[i:j]
                assert json.loads(gammal_txt) == q[k], (q['id'], k)
                indent = re.search(r'\n( *)' + re.escape(nyckel), del_).group(1)
                if '\n' in gammal_txt:
                    nytt_txt = json.dumps(nq[k], ensure_ascii=False, indent=2).replace('\n', '\n' + indent)
                else:
                    nytt_txt = json.dumps(nq[k], ensure_ascii=False)
                ny = ny[:start] + del_[:i] + nytt_txt + del_[j:] + ny[slut:]
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = {x['id']: sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k)) for x, y in zip(efter, bank) if x != y}
    assert set(andr) == set(efter_q), set(andr) ^ set(efter_q)
    for x in efter:
        if x['id'] in efter_q:
            assert x == efter_q[x['id']], x['id']
    for uid, k in sorted(andr.items(), key=lambda p: [float(t) for t in p[0].split('.')]):
        print(uid, k)
    if '--visa' in sys.argv:
        for x in efter:
            if x['id'] in VS:
                print(x['id'], x['svarVardesiffror'])
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
