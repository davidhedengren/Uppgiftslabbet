"""Ma3c Funktioner: variera 1.545, 1.546, 1.551 och 1.552 och ta bort begreppet ”diskret funktion” (2026-11-20).

Användaren 2026-11-20, med en skärmbild av fyra nästan likadana uppgifter (”En diskret funktion har värdena f(1)=…,
f(2)=… och f(3)=…. Bestäm f(1)+f(2)+f(3).”): ”Detta ser inte bra ut, variera dessa och ta bort begreppet diskret
funktion.”

- 1.545: tabell med sålda lotter, summan av tre funktionsvärden.
- 1.546: graf med en solrosplantas höjd vecka för vecka, skillnaden mellan två avlästa värden.
- 1.551: tabell med biljettpris per antal zoner, baklänges: vilket x ger ett givet funktionsvärde.
- 1.552: två bowlinghallar med var sin prisfunktion, jämför funktionsvärdena.
- 1.453 (NP Ma3c ht 2012, uppg. 6) frågar nu vilken variabel som bara kan anta heltal, utan ordet diskret.
- Facit och ledtrådar i 1.175, 1.457, 3.120, 3.737 (Ma3c) och ledtråden i Ma1 2.85 skrivs utan ”diskret”.

  python tools/ma3c-funktioner-utan-diskret-2026-11-20.py [--skriv]
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
TAB = '<table class="data" style="width:100%;max-width:440px;border-collapse:collapse;text-align:center">'


def byt(text, gammal, ny, n=1):
    assert text.count(gammal) == n, (gammal, text.count(gammal))
    return text.replace(gammal, ny)


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def tabell(rubrik_x, xs, rubrik_y, ys):
    return (TAB + f'<tr><th>{rubrik_x}</th>' + ''.join(f'<td>{x}</td>' for x in xs) + '</tr>'
            + f'<tr><th>{rubrik_y}</th>' + ''.join(f'<td>{y}</td>' for y in ys) + '</tr></table>')


def solros_svg():
    """Höjden h(v) cm vecka v = 1–4: 10, 20, 35, 45. Rutnät var 5:e cm."""
    W, H = 380, 270
    x0, y0, sx, sy = 52, 230, 60, 4.0   # 1 vecka = 60 px, 1 cm = 4 px
    b = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    for c in range(0, 55, 5):
        y = y0 - c * sy
        b.append(f'<line x1="{x0}" y1="{y}" x2="{x0 + 5 * sx}" y2="{y}" stroke="#dfe7ef" stroke-width="1"/>')
        if c % 10 == 0:
            b.append(f'<text x="{x0 - 7}" y="{y + 4}" font-family="Arial,sans-serif" font-size="12" text-anchor="end" '
                     f'fill="#203746">{c}</text>')
    for v in range(0, 6):
        x = x0 + v * sx
        b.append(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0 - 50 * sy}" stroke="#dfe7ef" stroke-width="1"/>')
        b.append(f'<text x="{x}" y="{y0 + 17}" font-family="Arial,sans-serif" font-size="12" text-anchor="middle" '
                 f'fill="#203746">{v}</text>')
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0 + 5 * sx + 14}" y2="{y0}" stroke="#203746" stroke-width="1.6"/>')
    b.append(f'<polygon points="{x0 + 5 * sx + 20},{y0} {x0 + 5 * sx + 10},{y0 - 5} {x0 + 5 * sx + 10},{y0 + 5}" fill="#203746"/>')
    b.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0 - 50 * sy - 12}" stroke="#203746" stroke-width="1.6"/>')
    b.append(f'<polygon points="{x0},{y0 - 50 * sy - 18} {x0 - 5},{y0 - 50 * sy - 8} {x0 + 5},{y0 - 50 * sy - 8}" fill="#203746"/>')
    b.append(f'<text x="{x0 + 8}" y="{y0 - 50 * sy - 6}" font-family="Arial,sans-serif" font-size="13" fill="#203746">'
             f'h (cm)</text>')
    b.append(f'<text x="{x0 + 5 * sx + 4}" y="{y0 - 9}" font-family="Arial,sans-serif" font-size="13" text-anchor="end" '
             f'fill="#203746">v (vecka)</text>')
    for v, h in zip(range(1, 5), (10, 20, 35, 45)):
        b.append(f'<circle cx="{x0 + v * sx}" cy="{y0 - h * sy}" r="6" fill="#2f8f4e" stroke="#1d5e33" stroke-width="1.5"/>')
    # liten solros i hörnet
    b.append('<g transform="translate(338,30)"><line x1="0" y1="10" x2="0" y2="46" stroke="#2f8f4e" stroke-width="3"/>'
             '<ellipse cx="-8" cy="32" rx="8" ry="3.5" fill="#4caf63" transform="rotate(-25 -8 32)"/>'
             + ''.join(f'<ellipse cx="0" cy="-9" rx="4" ry="9" fill="#f2c230" transform="rotate({a})"/>' for a in range(0, 360, 30))
             + '<circle r="7" fill="#7a4b1e"/></g>')
    titel = 'Punkter som visar solrosplantans höjd vecka 1 till 4: 10, 20, 35 och 45 centimeter.'
    return (f'<span class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'role="img" aria-label="{titel}" style="max-width:100%;height:auto"><title>{titel}</title>{"".join(b)}</svg></span>')


def mato1(bank):
    Q = {q['id']: q for q in bank}
    nya = {}

    # ---- 1.545: lotter, tabell och summa
    q = json.loads(json.dumps(Q['1.545']))
    q['t'] = ('<p>En skolklass säljer lotter under tre dagar. Funktionen \\(L(d)\\) anger hur många lotter klassen säljer '
              'dag \\(d\\).</p>' + tabell('\\(d\\)', [1, 2, 3], '\\(L(d)\\)', [14, 9, 22])
              + '<p>Hur många lotter säljer klassen sammanlagt?</p>')
    q['s'] = facit([li('Sammanlagt antal: \\(L(1)+L(2)+L(3)\\)', '<p>Läs av funktionsvärdena i tabellen.</p>',
                       mt('14+9+22=45'))], '45 lotter')
    q['rättSvar'] = 45
    q['ledtrad'] = '<p>Vad betyder \\(L(2)\\)? Lägg ihop försäljningen för alla tre dagarna.</p>'
    nya['1.545'] = q

    # ---- 1.546: solros, graf och skillnad
    q = json.loads(json.dumps(Q['1.546']))
    q['t'] = ('<p>Ida mäter sin solrosplanta en gång i veckan. Funktionen \\(h(v)\\) anger plantans höjd i centimeter '
              'vecka \\(v\\).</p>' + solros_svg() + '<p>Hur mycket växer plantan från vecka 1 till vecka 3?</p>')
    q['s'] = facit([li('Läs av \\(h(1)\\) och \\(h(3)\\) i grafen', mt('h(1)=10,\\qquad h(3)=35')),
                    li('Tillväxten är skillnaden \\(h(3)-h(1)\\)', mt('35-10=25'))], '25 cm')
    q['rättSvar'] = 25
    q['svarEnhet'] = 'cm'
    q['ledtrad'] = '<p>Vilken höjd har plantan vecka 1, och vilken har den vecka 3?</p>'
    nya['1.546'] = q

    # ---- 1.551: zonpriser, baklänges
    q = json.loads(json.dumps(Q['1.551']))
    q['t'] = ('<p>Priset för en bussbiljett beror på hur många zoner man reser. Funktionen \\(k(n)\\) anger priset i '
              'kronor för \\(n\\) zoner.</p>' + tabell('\\(n\\)', [1, 2, 3, 4], '\\(k(n)\\)', [25, 38, 48, 55])
              + '<p>Nora betalar 48 kr för sin biljett. Hur många zoner reser hon?</p>')
    q['s'] = facit([li('Sök det \\(n\\) som ger \\(k(n)=48\\)',
                       '<p>Nu är funktionsvärdet känt, och det är \\(n\\) som söks. Leta upp 48 på raden \\(k(n)\\).</p>',
                       mt('k(3)=48'))], '3 zoner')
    q['rättSvar'] = 3
    q['ledtrad'] = '<p>Här vet du priset. Leta i tabellen efter det värde på \\(n\\) som ger det priset.</p>'
    nya['1.551'] = q

    # ---- 1.552: två bowlinghallar
    q = json.loads(json.dumps(Q['1.552']))
    q['t'] = ('<p>Två bowlinghallar tar betalt på olika sätt. I hall A betalar man 60 kr för skor och 45 kr per serie. '
              'I hall B ingår skorna, och varje serie kostar 70 kr. Kostnaden i kronor för \\(n\\) serier är</p>'
              '<p>\\(A(n)=60+45n\\) och \\(B(n)=70n\\).</p>'
              '<p>Hur mycket dyrare är hall B än hall A för den som spelar 4 serier?</p>')
    q['s'] = facit([li('Sätt in \\(n=4\\) i båda funktionerna',
                       mt('\\begin{aligned}&A(4)=60+45\\cdot4=240\\\\&B(4)=70\\cdot4=280\\end{aligned}')),
                    li('Skillnaden är \\(B(4)-A(4)\\)', mt('280-240=40'))], '40 kr')
    q['rättSvar'] = 40
    q['svarEnhet'] = 'kr'
    q['ledtrad'] = '<p>Räkna ut vad 4 serier kostar i varje hall och jämför.</p>'
    nya['1.552'] = q

    # ---- 1.453: NP-uppgiften utan ordet diskret
    q = json.loads(json.dumps(Q['1.453']))
    q['t'] = ('<p>I vilken av situationerna kan den oberoende variabeln bara anta heltalsvärden, till exempel 0, 1, 2, '
              '3, …?</p>')
    q['s'] = byt(q['s'], '<li><p class="facit-rubrik">Diskret betyder att variabeln bara kan anta separata värden</p>'
                         '<p>Ofta är det heltal, till exempel ett antal saker. Mellan två tillåtna värden finns inga andra.</p></li>',
                 '<li><p class="facit-rubrik">Ett antal saker är alltid ett heltal</p><p>Den oberoende variabeln är den '
                 'som funktionen beror av. Är den ett antal, finns inga värden mellan två heltal.</p></li>')
    q['s'] = byt(q['s'], 'De ger kontinuerliga funktioner.', 'Funktionen har då ett värde för varje tal i intervallet.')
    q['ledtrad'] = '<p>Vilken variabel räknar man i hela styck?</p>'
    for a in q['alternativ']:
        if a.get('kommentar'):
            a['kommentar'] = (a['kommentar'].replace(' Den varierar kontinuerligt, inte i separata steg.',
                                                     ' Den kan alltså anta decimaltal, inte bara heltal.')
                              .replace(' Volymen blir då en kontinuerlig funktion.', ' Den är alltså inte bara heltal.')
                              .replace(' Det ger en kontinuerlig funktion.', ' Vikten är alltså inte bara heltal.'))
            assert 'kontinuerlig' not in a['kommentar'], a['kommentar']
    nya['1.453'] = q

    # ---- facit i 1.175, 1.457, 3.120 och 3.737
    q = json.loads(json.dumps(Q['1.175']))
    q['s'] = byt(q['s'], 'Därför är en diskret definitionsmängd relevant', 'Därför består definitionsmängden bara av heltal')
    nya['1.175'] = q
    q = json.loads(json.dumps(Q['1.457']))
    q['s'] = byt(q['s'], 'Eftersom antalet bananer är diskret', 'Eftersom man bara kan köpa ett helt antal bananer')
    nya['1.457'] = q
    q = json.loads(json.dumps(Q['3.120']))
    q['s'] = byt(q['s'], 'ankomster sker diskret,', 'personerna kommer in en och en vid enskilda tillfällen,')
    nya['3.120'] = q
    q = json.loads(json.dumps(Q['3.737']))
    q['s'] = byt(q['s'], 'Insättningarna sker diskret vid heltalsåldrarna', 'Insättningarna sker bara vid heltalsåldrarna')
    q['s'] = byt(q['s'], 'mindre än den diskreta summan', 'mindre än summan av insättningarna')
    nya['3.737'] = q
    return nya


def ma1(bank):
    q = json.loads(json.dumps(next(x for x in bank if x['id'] == '2.85')))
    gammal = 'antal personer är heltal, så mängderna är diskreta — inte hela intervall'
    ny = 'antal personer är heltal, så mängderna består bara av heltal och är inte hela intervall'
    q['ledtrad'] = byt(q['ledtrad'], gammal, ny)
    for d in q['spelDelar']:
        d['ledtrad'] = byt(d['ledtrad'], gammal, ny)
    return {'2.85': q}


def main():
    for fil, funk in (('uppgiftermato1.js', mato1), ('uppgifterma1.js', ma1)):
        src, bank = B.las(ROOT / fil)
        nya = funk(bank)
        assert not B.kontrollera_rundresa(ROOT / fil, set(nya)), fil
        for q in nya.values():
            fritt = json.dumps({k: v for k, v in q.items() if not k.endswith('Tidigare') and k not in ('typ', 'kalla')},
                               ensure_ascii=False)
            assert not re.search('diskret', fritt, re.I), q['id']
        ny_src = B.ersatt(src, nya)
        ny_bank = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        andr = [q['id'] for q, r in zip(ny_bank, bank) if q != r]
        assert sorted(andr) == sorted(nya), (fil, set(andr) ^ set(nya))
        print(fil, andr)
        if SKRIV:
            B.skriv(ROOT / fil, ny_src)


if __name__ == '__main__':
    main()
