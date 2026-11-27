"""Manuell granskning av Fy1 kap 3 (omgång 2), 2026-11-27: acceleration, at-diagram, konstant acceleration,
st-diagram, vektorer och vt-diagram.

Alla uppgifter i områdena är lästa och kontrollräknade, utom svar som bara kan läsas av i en figur (se
agent/FY1_GRANSKNING_2026-11-27.md). Ändringar:

- Sakfel i uppgiftstexten:
  3.231 c frågade när godstågets bakände lämnar ”tunneln”, men tunneln fanns bara i delkortet. Den står nu i
  frågan. Delkorten är kedjade, och b och c får omkörningstiden som mellanresultat.
  3.46 c frågade efter ”personens hastighet”, men på papperet stod inte att personen går nedåt. Delkorten är kedjade.
  3.44 b: ”tåget” → ”det snabbare tåget” (två tåg i inledningen).
  3.386: delkorten upprepade inledningen med nya ord, och d hänvisade till ”bilen i c”. Varje del är nu inledning +
  fråga, och d har sina egna värden. b får accelerationen från a som mellanresultat.
  3.387 a: delkortet saknade A och B, som frågan använder. Nu ingår inledningen med figuren.
  3.388: ”Partikeln … En bil passerar” → en bil. b får farten i A som mellanresultat.
  3.380–3.384: ”Partikeln rör sig … En partikel passerar” → en mening. 3.389: inledningen ”Partikeln …” passade inte
  bilarna och cyklisten.
  3.407 b: ”Bestäm h” utan h i delen → ”Från vilken höjd faller partikeln?”
- Avrundnings- och enhetsinstruktioner bort ur texten, eller till kgInstruktion när rättningen kräver dem:
  3.88 (tolerans 0,5 godtar redan exakta svar), 3.388 b (två decimaler, till kgInstruktion), 3.403, 3.407 b (tre
  värdesiffror, svarVardesiffror finns), 3.21-typen ”i m/i s/i m/s²” när enheten är underförstådd (3.43, 3.47 b,
  3.106 d, 3.140 a, 3.151 c, 3.163 c, 3.175).
- Metatext och lösningsanvisningar bort: 3.39 (”Modellera fordonen som punkter …”), 3.73 (”Räkna även ut …
  modellen …”, ”enligt modellen”), 3.94 (”behandla tiderna som exakta i modellen”), 3.95 (”i modellen”), 3.230
  (”I den generella modellen gäller …”), 3.362 (”Bestäm tangentens lutning.”), 3.47 (”Diagrammet använder en
  förenklad modell …”, till kgInstruktion som ”Använd värdena i diagrammet.”), 3.75 (dubblerad mening), 3.76
  (”Föremålen …”, ”diagrammets linjära förlopp …”), 3.144 (dubblerad beskrivning).
- 3.618: ”På vilken höjd ligger den?” → ”Vilken acceleration har bilen?”
- ”elevens/eleven” → namnet (3.38 Hugo, 3.253 Leo, 3.439 Ella).
- Bindestreck som minustecken → ”−” (3.197, 3.198).
- ”Antag” → ”Anta” i kap 3, som i resten av banken.

Svar och facit är oförändrade, utom en mening i 3.386 b:s delfacit (”Från a):” → ”Accelerationen är given:”).

  python tools/fy1-granskning-kap3-2026-11-27.py [--skriv]
"""
import json
import os
import re
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

ANTAG = ['3.7', '3.12', '3.18', '3.24', '3.31', '3.56', '3.60', '3.63', '3.65', '3.69', '3.76', '3.95', '3.113',
         '3.157', '3.212', '3.237', '3.363', '3.739']

PARTIKEL_AB = ('<p>Partikeln rör sig längs en rät linje med konstant acceleration.</p><p>En partikel passerar A och '
               'senare B.</p>')
PARTIKEL = '<p>Partikeln rör sig längs en rät linje med konstant acceleration.</p>'
PARTIKEL_NY = ('<p>En partikel rör sig längs en rät linje med konstant acceleration. Den passerar först punkten A och '
               'sedan punkten B.</p>')

# id -> lista av operationer
#   ('byt', gammalt, nytt)        i t, spelIntro och delkortens t/fraga
#   ('kg', [meningar], vem)       vem = 'alla' (uppgift + delkort), 'uppgift' eller en etikett
#   ('delfraga', etikett, fraga)  delkortet blir spelIntro + fråga (kedjan)
OPS = {
    '3.94': [('byt', '; behandla tiderna som exakta i modellen.', '.')],
    '3.151': [('byt', 'Bestäm tiden i sekunder.', 'Bestäm t.')],
    '3.197': [('byt', 'Sluthastigheten är -10 m/s.', 'Sluthastigheten är −10 m/s.')],
    '3.198': [('byt', 'a = -3,5', 'a = −3,5'), ('byt', 'v₀ = -11', 'v₀ = −11')],
    '3.618': [('byt', 'På vilken höjd ligger den?', 'Vilken acceleration har bilen?')],
    '3.140': [('byt', 'Läs av accelerationen under 0–5 s i m/s².', 'Läs av accelerationen under 0–5 s.')],
    '3.88': [('byt', 'Bestäm accelerationen i m/s², avrundad till heltal.', 'Bestäm accelerationen.'),
             ('byt', 'Bestäm kvoten a/g, avrundad till heltal.', 'Bestäm kvoten a/g.')],
    '3.39': [('byt', 'Modellera fordonen som punkter som rör sig i samma riktning och befinner sig på samma plats vid '
              't = 0. ', '')],
    '3.73': [('byt', '<p>Räkna även ut hur lång sträcka modellen skulle kräva om startbanan inte tog slut efter 800 m.'
              '</p>', ''),
             ('byt', 'Bestäm tiden för att nå 65 m/s enligt modellen.', 'Bestäm tiden för att nå 65 m/s.')],
    '3.75': [('byt', '<p>Diagrammet visar bollens vertikala hastighet. Vid t', '<p>Vid t')],
    '3.43': [('byt', 'Beräkna förflyttningen i m om', 'Beräkna förflyttningen om')],
    '3.253': [('byt', 'elevens metod', 'Leos metod')],
    '3.163': [('byt', 'Bestäm stopptiden i s från starten.', 'Bestäm stopptiden räknat från starten.')],
    '3.380': [('byt', PARTIKEL_AB, PARTIKEL_NY)],
    '3.381': [('byt', PARTIKEL_AB, PARTIKEL_NY)],
    '3.382': [('byt', PARTIKEL_AB, PARTIKEL_NY)],
    '3.383': [('byt', PARTIKEL_AB, PARTIKEL_NY)],
    '3.384': [('byt', PARTIKEL, PARTIKEL_NY)],
    '3.389': [('byt', PARTIKEL, '<p>Alla rörelser sker längs raka linjer.</p>')],
    '3.388': [('byt', '<p>Partikeln rör sig längs en rät linje med konstant acceleration.</p><p>En bil passerar A',
               '<p>En bil kör längs en rak väg med konstant acceleration.</p><p>Bilen passerar A'),
              ('byt', ' (två decimaler)?', '?'),
              ('delfraga', 'b', 'Farten i A är 12,91 m/s. Hur lång tid tar det från A till mittpunkten på AB?'),
              ('kg', ['Svara med två decimaler.'], 'b')],
    '3.386': [('delfraga', 'a', 'AB = 280 m och BC = 220 m. En bil passerar A med 4,0 m/s och C 21 s senare. '
               'Bestäm accelerationen.'),
              ('delfraga', 'b', 'AB = 280 m och BC = 220 m. En bil passerar A med 4,0 m/s och C 21 s senare. '
               'Bilens acceleration är 1,887 m/s². Bestäm farten i B.'),
              ('delfacit', 'b', 'Från a): \\(a=', 'Accelerationen är given: \\(a='),
              ('delfraga', 'c', 'AB = 28 m. Den andra bilen passerar A med 11 m/s, B med 15 m/s och C med 29 m/s. '
               'Bestäm sträckan AC.'),
              ('delfraga', 'd', 'AB = 28 m. Den andra bilen passerar A med 11 m/s, B med 15 m/s och C med 29 m/s. '
               'Hur lång tid tar det för bilen att köra från A till C?')],
    '3.387': [('delfraga', 'a', 'Bestäm retardationens storlek mellan A och B.')],
    '3.403': [('byt', ' (tre värdesiffror)?', '?')],
    '3.407': [('byt', ' Bestäm \\(h\\) (tre värdesiffror).', ' Från vilken höjd faller partikeln?')],
    '3.362': [('byt', ' Bestäm tangentens lutning.', '')],
    '3.38': [('byt', 'elevens slutsatser', 'Hugos slutsatser')],
    '3.439': [('byt', 'vad eleven har blandat ihop', 'vad Ella har blandat ihop')],
    '3.230': [('byt', '<p>I den generella modellen gäller \\(L>0\\) och \\(v_A>v_B>0\\).</p>', '')],
    '3.44': [('byt', 'Hur långt hinner tåget köra?', 'Hur långt hinner det snabbare tåget köra?')],
    '3.95': [('byt', 'mellan spåren i modellen.', 'mellan spåren.')],
    '3.175': [('byt', 'Bestäm markfarten i km/h.', 'Bestäm markfarten.')],
    '3.47': [('byt', '<p>Diagrammet använder en förenklad modell; bestäm värdena ur grafen.</p>', ''),
             ('byt', 'Bestäm accelerationen i m/s².', 'Bestäm accelerationen.'),
             ('kg', ['Använd värdena i diagrammet.'], 'alla')],
    '3.76': [('byt', 'Föremålen startar samtidigt från samma plats och rör sig längs samma räta linje. Anta att '
              'diagrammets linjära förlopp fortsätter när du diskuterar om de möts senare.',
              'Cyklisterna startar samtidigt från samma plats och cyklar längs samma raka väg. Anta att farterna '
              'fortsätter att öka på samma sätt efter den tid som diagrammet visar.')],
    '3.106': [('byt', 'Bestäm slutläget i höjd relativt startpunkten i m.',
               'Bestäm drönarens höjd över startpunkten i slutet av förloppet.')],
    '3.144': [('byt', 'Diagrammet visar två bilar på samma väg.',
               'Diagrammet visar hastigheten för två bilar som kör åt samma håll i var sitt körfält på en rak väg.'),
              ('byt', 'Två bilar följer hastighetsgraferna på parallella raka banor i samma riktning. ', '')],
}

# Kedjor: (frågor på papperet, delkortens frågor)
KEDJOR = {
    '3.231': (['Hur lång tid tar hela omkörningen?',
               'Hur långt färdas passagerartåget under omkörningen?',
               'Godstågets front kör in i en 600 m lång tunnel i startögonblicket. Hur många sekunder efter '
               'omkörningens slut lämnar godstågets bakände tunneln?'],
              ['Hur lång tid tar hela omkörningen?',
               'Omkörningen tar 24 s. Hur långt färdas passagerartåget under omkörningen?',
               'Omkörningen tar 24 s. Godstågets front kör in i en 600 m lång tunnel i startögonblicket. Hur många '
               'sekunder efter omkörningens slut lämnar godstågets bakände tunneln?']),
    '3.46': (['Hur lång tid tar det att åka stående hela vägen?',
              'Hur lång tid tar det om du samtidigt går uppför?',
              'Du går i stället nedåt i rulltrappan. Vilken hastighet har du relativt byggnaden?'], None),
}


def kg_med(kg, meningar):
    kg = (kg or '').strip()
    for m in meningar:
        if m not in kg:
            kg = (kg + ' ' + m).strip()
    return kg


def texter(q):
    for k in ('t', 'spelIntro'):
        if isinstance(q.get(k), str):
            yield q, k
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

    for uid in ANTAG:
        q = hamta(uid)
        n = 0
        for o, k in texter(q):
            o[k], m = re.subn(r'\bAntag(?= )', 'Anta', o[k])
            n += m
        assert n >= 1, uid
    for uid, ops in OPS.items():
        q = hamta(uid)
        for op in ops:
            if op[0] == 'byt':
                _, gl, ny = op
                n = 0
                for o, k in texter(q):
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
            elif op[0] == 'delfacit':
                # delkortets facit hänvisade till en annan del; mellanresultatet står nu i frågan
                _, et, gl, ny = op
                d = next(d for d in q['spelDelar'] if d['etikett'] == et)
                assert d['s'].count(gl) == 1, (uid, et, gl)
                d['s'] = d['s'].replace(gl, ny)
    for uid, (fragor, kortfragor) in KEDJOR.items():
        q = hamta(uid)
        intro = q['spelIntro']
        assert q['t'].startswith(intro + '<ol type="a">'), uid
        q['t'] = intro + '<ol type="a">' + ''.join(f'<li>{f}</li>' for f in fragor) + '</ol>'
        kortfragor = kortfragor or fragor
        assert len(q['spelDelar']) == len(fragor), uid
        for d, f in zip(q['spelDelar'], kortfragor):
            d['fraga'] = f
            d['t'] = intro + f'<p>{f}</p>'

    ny_src = src
    for uid, q in nya.items():
        start = ny_src.index('"id": ' + json.dumps(uid))
        # filen har objekt både med två stegs indrag och utan indrag; behåll objektets eget format
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
            assert '<p></p>' not in o[kk] and 'Partikeln rör sig' not in o[kk], (uid, kk)
        for d in x.get('spelDelar') or []:
            if x.get('spelIntro') and uid in KEDJOR or uid in ('3.386', '3.387'):
                assert d['t'].startswith(x['spelIntro']), (uid, d['etikett'])
        print(uid, k)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny_src)


if __name__ == '__main__':
    main()
