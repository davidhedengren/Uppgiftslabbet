"""Felrapporter 2026-11-22 19:35. Se agent/FELRAPPORTER_2026-11-22_1935.md.

Fy1  2.143 a  ”Mer tydlig vilken densitet som hör till vad”: densiteterna knyts till materialen. Samma i 2.275, 2.277.
Fy1  3.361    ”Enheter på axlarna”: a (m/s²) och t (s). Samma i 3.105, 3.355 och 3.603.
Fy1  3.202 a  ”För stor sluthastighet”: värdena är John Stapps raketsläde 1954; sammanhanget står nu i texten.
              Svaren har tre värdesiffror (b och d hade fem och fyra).
Ma2  2.631    rättSvar var lagrat som LaTeX och saknade format; nu uttryck (godtar också f(x) = …).
Ma3c 3.799    x³ − 8 kan inte faktoriseras med kursens metoder på nivå 3: A, träningsnivå 5, facit med ansatsen
              (x − 2)(x² + ax + b) som läraren föreslog. Samma för gränsvärdet 1.136. 1.44 och 1.506 (E2, samma
              uttryck) löses i stället med en tabell respektive räknare.
Ma3c 1.1131   h(2x + h) godtas (ändring i Kunskapsgymmets förenklat_polynom, ingen bankändring).

  python tools/felrapporter-2026-11-22-1935.py [--skriv]
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKRIV = '--skriv' in sys.argv


def byt(text, gammal, ny, n=None):
    c = text.count(gammal)
    assert c >= 1 and (n is None or c == n), (gammal, c)
    return text.replace(gammal, ny)


def kopia(q):
    return json.loads(json.dumps(q))


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def alla_text(q, f):
    """Kör f på t, spelIntro och delkortens t."""
    q['t'] = f(q['t'])
    if q.get('spelIntro'):
        q['spelIntro'] = f(q['spelIntro'])
    for d in q.get('spelDelar') or []:
        if d.get('t'):
            d['t'] = f(d['t'])


# ================================================================ Fy1
def fy1(bank):
    Q = {q['id']: q for q in bank}
    nya = {}

    # ---- densiteter knutna till material
    for uid, gammal, ny in [
            ('2.143', 'Densiteterna är 2,70 och 1,20 g/cm³.', 'Aluminium har densiteten 2,70 g/cm³ och plasten 1,20 g/cm³.'),
            ('2.275', 'Densiteterna är 2,70 respektive 7,80 g/cm³.', 'Aluminium har densiteten 2,70 g/cm³ och stål 7,80 g/cm³.'),
            ('2.277', 'Densiteterna är 2,70 och 7,80 g/cm³.', 'Aluminium har densiteten 2,70 g/cm³ och stål 7,80 g/cm³.')]:
        q = kopia(Q[uid])
        alla_text(q, lambda t, g=gammal, n=ny: t.replace(g, n))
        synligt = [q['t'], q.get('spelIntro') or ''] + [d.get('t') or '' for d in q.get('spelDelar') or []]
        assert not any(gammal in x for x in synligt) and ny in q['t'], uid
        nya[uid] = q

    # ---- enheter på axlarna
    axlar = {
        '3.105': [('font-style="italic">t</text>', 'font-style="italic">t (s)</text>'),
                  ('font-style="italic">s</text>', 'font-style="italic">s (m)</text>')],
        '3.355': [('font-style="italic">t</text>', 'font-style="italic">t (s)</text>'),
                  ('text-anchor="start" font-style="italic">a</text>', 'text-anchor="start" font-style="italic">a (m/s²)</text>')],
        '3.361': [('<text x="398" y="135.9" font-family="Arial" font-size="14" font-style="italic">t</text>',
                   '<text x="410" y="135.9" font-family="Arial" font-size="14" font-style="italic" text-anchor="end">t (s)</text>'),
                  ('font-style="italic">a</text>', 'font-style="italic">a (m/s²)</text>')],
        '3.603': [('fill="#5b6773">t</text>', 'fill="#5b6773">t (s)</text>'),
                  ('fill="#5b6773">a</text>', 'fill="#5b6773">a (m/s²)</text>')],
    }
    for uid, byten in axlar.items():
        q = kopia(nya.get(uid, Q[uid]))
        for g, n in byten:
            # Vit kontur så att det längre axelnamnet syns även där det korsar en rutnätslinje.
            n = re.sub(r'>(t \(s\)|s \(m\)|a \(m/s²\))</text>',
                       r' stroke="#fff" stroke-width="3" paint-order="stroke" stroke-linejoin="round">\1</text>', n)
            q['t'] = byt(q['t'], g, n)
        nya[uid] = q

    # ---- 3.202: raketsläden
    q = kopia(Q['3.202'])
    intro_g = ('<p>I ett försök ökar en släde farten från stillastående till 282 m/s på 5,00 s. Därefter stannar den på '
               '1,40 s. Rörelsen är rak.</p>')
    intro_n = ('<p>År 1954 testade det amerikanska flygvapnet hur mycket en människa tål. En raketsläde med en pilot ökade '
               'farten längs en rak räls från stillastående till 282 m/s på 5,00 s. Därefter bromsades släden till '
               'stillastående på 1,40 s.</p>')
    q['t'] = byt(q['t'], intro_g, intro_n, 1)
    q['spelIntro'] = byt(q['spelIntro'], intro_g, intro_n, 1)
    for d in q['spelDelar']:
        d['t'] = d['t'].replace('En släde ökar farten från stillastående till 282 m/s på 5,00 s längs en rak bana.',
                                'En raketsläde ökar farten längs en rak räls från stillastående till 282 m/s på 5,00 s.')
        d['t'] = d['t'].replace('En släde bromsar från 282 m/s till vila på 1,40 s längs en rak bana.',
                                'En raketsläde bromsar längs en rak räls från 282 m/s till stillastående på 1,40 s.')
        assert 'raketsläde' in d['t'], d['etikett']
    for obj in [q] + q['spelDelar']:
        if 'approx-201{,}43' in obj['s'] or '201{,}43' in obj['s']:
            obj['s'] = (obj['s'].replace('\\approx-201{,}43', '\\approx-201').replace('−201,43 m/s²', '−201 m/s²')
                        .replace('\\approx201{,}43', '\\approx201{,}4')
                        .replace('\\frac{201{,}43}{9{,}82}\\approx20{,}51', '\\frac{201{,}4}{9{,}82}\\approx20{,}5')
                        .replace('</strong> 20,51', '</strong> 20,5'))
            assert '201{,}43' not in obj['s'] and '20,51' not in obj['s'], obj.get('etikett')
    q['rättSvar'] = [56.4, -282 / 1.40, 282 / 5.00 / 9.82, 282 / 1.40 / 9.82]
    q['tolerans'] = [0.05, 0.5, 0.005, 0.05]
    q['svarVardesiffror'] = [3, 3, 3, 3]
    nya['3.202'] = q
    return nya


# ================================================================ Ma3c
TAB = '<table class="data" style="width:100%;max-width:440px;border-collapse:collapse;text-align:center">'
ANSATS_LEDTRAD = ('<p>Eftersom \\(2^3-8=0\\) är \\(x-2\\) en faktor i täljaren. Skriv '
                  '\\(x^3-8=(x-2)(x^2+ax+b)\\), multiplicera ut och jämför koefficienterna.</p>')


def ansats_steg():
    return [
        li('\\(x-2\\) är en faktor i täljaren', '<p>Insättning av \\(x=2\\) ger \\(\\tfrac00\\), eftersom '
           '\\(2^3-8=0\\). Då kan täljaren skrivas som \\((x-2)\\) gånger ett andragradspolynom.</p>'),
        li('Ansätt \\(x^3-8=(x-2)(x^2+ax+b)\\) och multiplicera ut',
           mt('\\begin{aligned}&(x-2)(x^2+ax+b)\\\\&=x^3+ax^2+bx-2x^2-2ax-2b\\\\&=x^3+(a-2)x^2+(b-2a)x-2b\\end{aligned}')),
        li('Jämför koefficienterna med \\(x^3+0x^2+0x-8\\)',
           mt('\\begin{aligned}&a-2=0\\ \\Rightarrow\\ a=2\\\\&b-2a=0\\ \\Rightarrow\\ b=4\\\\&-2b=-8\\ \\text{stämmer}\\end{aligned}')),
        li('Förkorta bort \\(x-2\\) för \\(x\\ne2\\)', mt('\\frac{(x-2)(x^2+2x+4)}{x-2}=x^2+2x+4')),
        li('Låt \\(x\\) gå mot 2', mt('2^2+2\\cdot2+4=12'))]


def mato1(bank):
    Q = {q['id']: q for q in bank}
    nya = {}

    q = kopia(Q['3.799'])
    q['niva'], q['poang'], q['traningsniva'], q['arbetsinsats'] = 'A', '0/0/2', 5, 3
    q['s'] = facit(ansats_steg() + [li('Kontinuitet: \\(f(2)\\) ska vara lika med gränsvärdet',
                                       '<p>Funktionen blir kontinuerlig i \\(x=2\\) om \\(f(2)=12\\).</p>')],
                   '\\(f(2)=12\\)')
    q['ledtrad'] = ANSATS_LEDTRAD
    nya['3.799'] = q

    q = kopia(Q['1.136'])
    q['niva'], q['poang'], q['traningsniva'], q['arbetsinsats'] = 'A', '0/1/2', 5, 3
    q['t'] = ('<p>Bestäm \\(\\displaystyle\\lim_{x\\to2}\\frac{x^3-8}{x-2}\\) algebraiskt.</p>')
    q['s'] = facit(ansats_steg(), '12')
    q['ledtrad'] = ANSATS_LEDTRAD
    nya['1.136'] = q

    xs = ['1,9', '1,99', '1,999', '2,001', '2,01', '2,1']
    fs = ['11,41', '11,9401', '11,994001', '12,006001', '12,0601', '12,61']
    for x, fx in zip(xs, fs):
        v = float(x.replace(',', '.'))
        assert abs((v ** 3 - 8) / (v - 2) - float(fx.replace(',', '.'))) < 1e-9, x
    q = kopia(Q['1.44'])
    q['t'] = ('<p>Tabellen visar värden på \\(f(x)=\\dfrac{x^3-8}{x-2}\\) för några \\(x\\) nära 2.</p>'
              + '<table class="data" style="max-width:260px;border-collapse:collapse;text-align:center">'
              + '<tr><th>\\(x\\)</th><th>\\(f(x)\\)</th></tr>'
              + ''.join(f'<tr><td>{x}</td><td>{y}</td></tr>' for x, y in zip(xs, fs)) + '</table>'
              + '<p>Bestäm \\(\\displaystyle\\lim_{x\\to2}\\frac{x^3-8}{x-2}\\).</p>')
    q['s'] = facit([li('Funktionen är inte definierad i \\(x=2\\)', '<p>Insättning ger \\(\\tfrac00\\). '
                       'Gränsvärdet avgörs av värdena nära 2.</p>'),
                    li('Värdena närmar sig 12 från båda hållen',
                       '<p>Från vänster: 11,41, 11,9401, 11,994001. Från höger: 12,61, 12,0601, 12,006001.</p>')],
                   '12')
    q['ledtrad'] = '<p>Vilket tal kommer funktionsvärdena närmare och närmare när \\(x\\) närmar sig 2 från båda hållen?</p>'
    nya['1.44'] = q

    q = kopia(Q['1.506'])
    q['t'] = ('<p>Funktionen \\(f\\) ges av \\(f(x)=\\dfrac{x^3-8}{x-2}\\) för \\(x\\ne2\\). Beräkna \\(f(1{,}99)\\) och '
              '\\(f(2{,}01)\\) med räknare. Vilket värde verkar \\(f(x)\\) närma sig när \\(x\\) går mot 2?</p>')
    q['s'] = facit([li('Beräkna funktionsvärdena på var sin sida om 2',
                       mt('\\begin{aligned}f(1{,}99)&=\\frac{1{,}99^3-8}{1{,}99-2}=11{,}9401\\\\'
                          'f(2{,}01)&=\\frac{2{,}01^3-8}{2{,}01-2}=12{,}0601\\end{aligned}')),
                    li('Värdena ligger på var sin sida om 12 och nära 12',
                       '<p>Ju närmare 2 man väljer \\(x\\), desto närmare 12 kommer \\(f(x)\\).</p>')], '12')
    q['ledtrad'] = '<p>Räkna ut båda värdena. Vilket heltal ligger de nära?</p>'
    q['miniräknare'] = True
    nya['1.506'] = q
    return nya


# ================================================================ Ma2 (kompakta objekt)
def ma2_bytes(src):
    i = src.index('{"id":"2.631"') if '{"id":"2.631"' in src else None
    gammal_rs = '"rättSvar":"\\\\(x^2-8x+7\\\\)"'
    assert src.count(gammal_rs) == 1, src.count(gammal_rs)
    return src.replace(gammal_rs, '"rättSvar":"x^2-8x+7","svarFormat":"uttryck"')


def main():
    for fil, funk in (('uppgifter.js', fy1), ('uppgiftermato1.js', mato1)):
        src, bank = B.las(ROOT / fil)
        nya = funk(bank)
        assert not B.kontrollera_rundresa(ROOT / fil, set(nya)), fil
        ny_src = B.ersatt(src, nya)
        nb = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        andr = [q['id'] for q, r in zip(nb, bank) if q != r]
        assert sorted(andr) == sorted(nya), (fil, set(andr) ^ set(nya))
        print(fil, andr)
        if SKRIV:
            B.skriv(ROOT / fil, ny_src)
    src, bank = B.las(ROOT / 'uppgifterma2.js')
    ny_src = ma2_bytes(src)
    nb = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = [q['id'] for q, r in zip(nb, bank) if q != r]
    assert andr == ['2.631'], andr
    q = next(x for x in nb if x['id'] == '2.631')
    assert q['rättSvar'] == 'x^2-8x+7' and q['svarFormat'] == 'uttryck'
    print('uppgifterma2.js', andr)
    if SKRIV:
        B.skriv(ROOT / 'uppgifterma2.js', ny_src)


if __name__ == '__main__':
    main()
