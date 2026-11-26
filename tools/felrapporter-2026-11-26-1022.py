"""Felrapport 2026-11-26 10:22, Fy1 2.370 (lärare: ”Steg 4 i lösningen förstår jag inte. Sitter inte blyet under
flötet? Eller sitter det inuti flötet?”).

Facit räknar med att blyvikten är en del av flötet: trä och bly har tillsammans volymen 12,0 cm³, så träets volym är
12,0 − V_bly. Texten (”en liten blyvikt längst ner”, ”Hela flötet har volymen 12,0 cm³”) och figuren (blyet sticker
ut under träkroppen) sa inte det. Nu:
- texten säger att blyvikten är ingjuten i flötets nedre ände och att trä och bly tillsammans har volymen 12,0 cm³;
- figuren visar blyet inuti träkroppens nedre ände;
- steg 4 i facit förklarar varför träets volym är 12,0 − V_bly.
Bly och vatten är tabellvärden och står, enligt beslutet om rena uppgifter (2026-11-23), i kgInstruktion; balsaträets
densitet är uppgiftens eget värde och står kvar i texten. Svaret 7,8 g är oförändrat.

  python tools/felrapporter-2026-11-26-1022.py [--skriv]
"""
import json
import os
import sys

FIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'uppgifter.js')

T_BYTEN = [
    ('Ett fiskeflöte är gjort av balsaträ och har en liten blyvikt längst ner. Hela flötet har volymen 12,0 cm³.',
     'Ett fiskeflöte är gjort av balsaträ med en liten blyvikt ingjuten i den nedre änden. Hela flötet, trä och bly '
     'tillsammans, har volymen 12,0 cm³.'),
    ('Balsaträ har densiteten 0,16 g/cm³, bly 11,3 g/cm³ och vatten 1,00 g/cm³.', 'Balsaträ har densiteten 0,16 g/cm³.'),
    # figuren: träkroppen räcker ner till 196 och blyet sitter inuti dess nedre ände
    ('<rect x="196" y="71.0" width="28" height="115.0" rx="12" fill="#f2dcb3" stroke="#203746" stroke-width="2"/>'
     '<rect x="202" y="178.0" width="16" height="18" rx="3" fill="#7d8a95" stroke="#203746" stroke-width="1.5"/>',
     '<rect x="196" y="71.0" width="28" height="125.0" rx="12" fill="#f2dcb3" stroke="#203746" stroke-width="2"/>'
     '<rect x="202" y="172.0" width="16" height="17" rx="3" fill="#7d8a95" stroke="#203746" stroke-width="1.5"/>'),
    ('med en liten blyvikt längst ner flyter upprätt', 'med en liten blyvikt ingjuten i den nedre änden flyter upprätt'),
]
S_BYTE = ('Låt \\(V_{\\text{bly}}\\) vara blyets volym i cm³. Då är balsaträets volym',
          'Blyvikten är ingjuten i flötet, så trä och bly fyller tillsammans flötets 12,0 cm³. Låt '
          '\\(V_{\\text{bly}}\\) vara blyets volym i cm³. Då är balsaträets volym')
KG = 'Bly har densiteten 11,3 g/cm³ och vatten 1,00 g/cm³.'


def lit(v):
    return json.dumps(v, ensure_ascii=False)


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    q = next(x for x in bank if x['id'] == '2.370')
    t = q['t']
    for a, b in T_BYTEN:
        n = t.count(a)
        assert n >= 1, a[:50]
        t = t.replace(a, b)
    s = q['s']
    assert s.count(S_BYTE[0]) == 1
    s = s.replace(S_BYTE[0], S_BYTE[1])
    ny = src
    for gl, nytt in ((q['t'], t), (q['s'], s)):
        assert ny.count(lit(gl)) == 1
        ny = ny.replace(lit(gl), lit(nytt))
    # kgInstruktion efter t
    i = ny.index(lit(t)) + len(lit(t))
    rad = ny.rfind('\n', 0, ny.index(lit(t))) + 1
    ind = ny[rad:ny.index(lit(t))].split('"')[0]
    ny = ny[:i] + ',\n' + ind + '"kgInstruktion": ' + lit(KG) + ny[i:]
    efter = json.loads(ny[ny.index('['):ny.rindex(']') + 1])
    andr = [(x['id'], sorted(k for k in set(x) | set(y) if x.get(k) != y.get(k))) for x, y in zip(efter, bank) if x != y]
    assert andr == [('2.370', ['kgInstruktion', 's', 't'])], andr
    m = q['rättSvar']
    assert abs((m + 0.16 * (12.0 - m / 11.3)) / 12.0 - 0.80) < 1e-9
    print(andr)
    if '--skriv' in sys.argv:
        with open(FIL, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
