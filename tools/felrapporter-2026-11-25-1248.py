"""Felrapport 2026-11-25 12:48, Ma4 2.165 del b (elev: ”övningarna skulle handla om kvoter men blandar in andra
funktioner också”).

Området `kvotregeln` (”Derivatan av en kvot”) fick vid omstruktureringen med sig blandade uppgifter från det gamla
området `deriveringsregler`. Eleven har rätt: i 2.165 är a) cos²x och b) (x² − 3x)⁵ kedjeregeln. Samma sak gäller
2.163 a–b (e^(2x+1), ln(4x+3)), 2.108 a–b (x²eˣ, x sin x: produktregeln) och 2.117 ((ax + b)eˣ, ingen kvot alls).

Åtgärd:
- 2.165, 2.163 och 2.108: delarna som inte är kvoter byts mot kvoter med samma karaktär (trigonometrisk funktion,
  polynom, exponential- och logaritmfunktion). Delarna som redan var kvoter står kvar. Hela facit skrivs om enligt
  FACITMALL (kvotregeln i rubriken, u, v och derivatorna, insättning, förenkling, svarsrad), eftersom det gamla facit
  hade rubriker i löptext och trasig struktur.
- 2.117 flyttas till `produktregeln` (”Derivering med produktregeln”); omrTidigare och familjTidigare sparas. Facit får
  rubriker med formeln, och delkort b ett facit utan tomt steg.
- 2.153 (”Vilken huvudregel behövs först?”) står kvar: uppgiften tränar att välja regel, vilket förutsätter att
  kvotregeln är genomgången.

Varje derivata kontrolleras numeriskt mot en centraldifferens i skriptet.

  python tools/felrapporter-2026-11-25-1248.py [--skriv]
"""
import json
import math
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
FIL = os.path.join(ROOT, 'uppgiftermato2.js')
KVOT = 'Kvotregeln: \\(\\left(\\frac{u}{v}\\right)\'=\\frac{u\'v-uv\'}{v^2}\\)'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def p(t):
    return f'<p>{t}</p>'


def delfacit(steg, svar):
    return ('<ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p>')


def huvud(delar):
    return ('<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{e})</span><div class="facit-arbete">{delfacit(s, sv)}</div></div>'
        for e, s, sv in delar) + '</div>')


def kort(s, sv):
    return '<div class="facit-v2 facit-stegvis"><div class="spel-en-del">' + delfacit(s, sv) + '</div></div>'


def uv(u, du, v, dv):
    return li('Täljare \\(u\\) och nämnare \\(v\\) med derivator',
              mt(f'u={u},\\quad u\'={du}'), mt(f'v={v},\\quad v\'={dv}'))


# id → (intro, ledtråd, delar); del = (etikett, fråga-LaTeX, steg, svar-LaTeX, rättSvar, f, f')
NYA = {
    '2.165': ('<p>Derivera.</p>',
              '<p>Alla tre funktionerna är kvoter. Skriv upp täljaren och nämnaren och deras derivator innan du sätter in '
              'i kvotregeln. I a) kan trigonometriska ettan förenkla täljaren.</p>', [
        ('a', 'f(x)=\\frac{\\sin x}{2+\\cos x}',
         [uv('\\sin x', '\\cos x', '2+\\cos x', '-\\sin x'),
          li(KVOT, mt("f'(x)=\\frac{\\cos x\\,(2+\\cos x)-\\sin x\\,(-\\sin x)}{(2+\\cos x)^2}")),
          li('Trigonometriska ettan: \\(\\sin^2x+\\cos^2x=1\\)',
             mt("f'(x)=\\frac{2\\cos x+\\cos^2x+\\sin^2x}{(2+\\cos x)^2}"), mt("f'(x)=\\frac{2\\cos x+1}{(2+\\cos x)^2}"))],
         "\\(f'(x)=\\dfrac{2\\cos x+1}{(2+\\cos x)^2}\\).", '(2cos(x)+1)/((2+cos(x))^2)',
         lambda x: math.sin(x) / (2 + math.cos(x)), lambda x: (2 * math.cos(x) + 1) / (2 + math.cos(x)) ** 2),
        ('b', 'g(x)=\\frac{x^2-3x}{x+1}',
         [uv('x^2-3x', '2x-3', 'x+1', '1'),
          li(KVOT, mt("g'(x)=\\frac{(2x-3)(x+1)-(x^2-3x)\\cdot1}{(x+1)^2}")),
          li('Multiplicera ut och samla termerna i täljaren',
             mt("g'(x)=\\frac{2x^2-x-3-x^2+3x}{(x+1)^2}"), mt("g'(x)=\\frac{x^2+2x-3}{(x+1)^2}"))],
         "\\(g'(x)=\\dfrac{x^2+2x-3}{(x+1)^2}\\).", '(x^2+2x-3)/((x+1)^2)',
         lambda x: (x * x - 3 * x) / (x + 1), lambda x: (x * x + 2 * x - 3) / (x + 1) ** 2),
        ('c', 'h(x)=\\frac{e^x}{x}',
         [uv('e^x', 'e^x', 'x', '1'),
          li(KVOT, mt("h'(x)=\\frac{e^x\\cdot x-e^x\\cdot1}{x^2}")),
          li('Bryt ut \\(e^x\\) i täljaren', mt("h'(x)=\\frac{e^x(x-1)}{x^2}"))],
         "\\(h'(x)=\\dfrac{e^x(x-1)}{x^2}\\).", '\\frac{e^x(x-1)}{x^2}',
         lambda x: math.exp(x) / x, lambda x: math.exp(x) * (x - 1) / x ** 2)]),
    '2.163': ('<p>Derivera.</p>',
              '<p>Alla tre funktionerna är kvoter. I a) behöver du kedjeregeln för att derivera täljaren.</p>', [
        ('a', 'f(x)=\\frac{e^{2x}}{x+1}',
         [uv('e^{2x}', '2e^{2x}', 'x+1', '1'),
          li(KVOT, mt("f'(x)=\\frac{2e^{2x}(x+1)-e^{2x}\\cdot1}{(x+1)^2}")),
          li('Bryt ut \\(e^{2x}\\) i täljaren', mt("f'(x)=\\frac{e^{2x}(2x+2-1)}{(x+1)^2}"), mt("f'(x)=\\frac{e^{2x}(2x+1)}{(x+1)^2}"))],
         "\\(f'(x)=\\dfrac{e^{2x}(2x+1)}{(x+1)^2}\\).", '(e^(2x)(2x+1))/((x+1)^2)',
         lambda x: math.exp(2 * x) / (x + 1), lambda x: math.exp(2 * x) * (2 * x + 1) / (x + 1) ** 2),
        ('b', 'g(x)=\\frac{x}{\\ln x},\\ x&gt;0,\\ x\\ne1',
         [uv('x', '1', '\\ln x', '\\frac{1}{x}'),
          li(KVOT, mt("g'(x)=\\frac{1\\cdot\\ln x-x\\cdot\\frac{1}{x}}{(\\ln x)^2}")),
          li('\\(x\\cdot\\frac{1}{x}=1\\)', mt("g'(x)=\\frac{\\ln x-1}{(\\ln x)^2}"))],
         "\\(g'(x)=\\dfrac{\\ln x-1}{(\\ln x)^2}\\).", '(ln(x)-1)/((ln(x))^2)',
         lambda x: x / math.log(x), lambda x: (math.log(x) - 1) / math.log(x) ** 2),
        ('c', 'h(x)=\\frac{x^2+1}{x-1}',
         [uv('x^2+1', '2x', 'x-1', '1'),
          li(KVOT, mt("h'(x)=\\frac{2x(x-1)-(x^2+1)\\cdot1}{(x-1)^2}")),
          li('Multiplicera ut och samla termerna i täljaren', mt("h'(x)=\\frac{2x^2-2x-x^2-1}{(x-1)^2}"), mt("h'(x)=\\frac{x^2-2x-1}{(x-1)^2}"))],
         "\\(h'(x)=\\dfrac{x^2-2x-1}{(x-1)^2}\\).", '(x^2-2x-1)/((x-1)^2)',
         lambda x: (x * x + 1) / (x - 1), lambda x: (x * x - 2 * x - 1) / (x - 1) ** 2)]),
    '2.108': ('<p>Derivera och förenkla så långt som möjligt.</p>',
              '<p>Alla fyra funktionerna är kvoter. Förenkla genom att bryta ut gemensamma faktorer i täljaren och '
              'förkorta mot nämnaren.</p>', [
        ('a', 'f(x)=\\dfrac{x^2}{e^x}',
         [uv('x^2', '2x', 'e^x', 'e^x'),
          li(KVOT, mt("f'(x)=\\frac{2x\\,e^x-x^2e^x}{(e^x)^2}")),
          li('Bryt ut \\(e^x\\) och förkorta', mt("f'(x)=\\frac{e^x(2x-x^2)}{e^{2x}}"), mt("f'(x)=\\frac{2x-x^2}{e^x}"))],
         "\\(f'(x)=\\dfrac{2x-x^2}{e^x}\\).", '(2x-x^2)/e^x',
         lambda x: x * x / math.exp(x), lambda x: (2 * x - x * x) / math.exp(x)),
        ('b', 'g(x)=\\dfrac{x}{\\sin x},\\ 0&lt;x&lt;\\pi',
         [uv('x', '1', '\\sin x', '\\cos x'),
          li(KVOT, mt("g'(x)=\\frac{1\\cdot\\sin x-x\\cos x}{\\sin^2x}"))],
         "\\(g'(x)=\\dfrac{\\sin x-x\\cos x}{\\sin^2x}\\).", '(sin(x)-x*cos(x))/((sin(x))^2)',
         lambda x: x / math.sin(x), lambda x: (math.sin(x) - x * math.cos(x)) / math.sin(x) ** 2),
        ('c', 'h(x)=\\dfrac{e^x}{x},\\ x\\ne0',
         [uv('e^x', 'e^x', 'x', '1'),
          li(KVOT, mt("h'(x)=\\frac{x\\,e^x-e^x}{x^2}")),
          li('Bryt ut \\(e^x\\) i täljaren', mt("h'(x)=\\frac{e^x(x-1)}{x^2}"))],
         "\\(h'(x)=\\dfrac{e^x(x-1)}{x^2}\\).", '\\frac{e^x(x-1)}{x^2}',
         lambda x: math.exp(x) / x, lambda x: math.exp(x) * (x - 1) / x ** 2),
        ('d', 'p(x)=\\dfrac{\\ln x}{x^2},\\ x&gt;0',
         [uv('\\ln x', '\\frac{1}{x}', 'x^2', '2x'),
          li(KVOT, mt("p'(x)=\\frac{\\frac{1}{x}\\cdot x^2-\\ln x\\cdot2x}{x^4}"), mt("p'(x)=\\frac{x-2x\\ln x}{x^4}")),
          li('Bryt ut \\(x\\) och förkorta', mt("p'(x)=\\frac{x(1-2\\ln x)}{x^4}"), mt("p'(x)=\\frac{1-2\\ln x}{x^3}"))],
         "\\(p'(x)=\\dfrac{1-2\\ln x}{x^3}\\).", '\\frac{1-2\\ln x}{x^3}',
         lambda x: math.log(x) / x ** 2, lambda x: (1 - 2 * math.log(x)) / x ** 3)]),
}

S_2117 = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
          + li('Funktionsvärdet \\(f(0)=2\\) ger \\(b\\)', mt('f(0)=(a\\cdot0+b)e^0=b=2'))
          + li('Produktregeln: \\((uv)\'=u\'v+uv\'\\)', mt("f'(x)=a\\,e^x+(ax+b)e^x"))
          + li("Derivatavärdet \\(f'(0)=5\\) ger \\(a\\)", mt("f'(0)=a+b=5\\quad\\Rightarrow\\quad a=5-2=3"))
          + '</ol><p class="facit-svar"><strong>Svar:</strong> \\(a=3\\) och \\(b=2\\).</p></div>')


def kontroll(f, df):
    for x in (0.4, 0.9, 1.7, 2.6):
        h = 1e-6
        num = (f(x + h) - f(x - h)) / (2 * h)
        assert abs(num - df(x)) < 1e-5 * max(1, abs(num)), (x, num, df(x))


def main():
    src = open(FIL, encoding='utf-8', newline='').read()
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    Q = {q['id']: q for q in bank}
    nya = {}
    for uid, (intro, ledtrad, delar) in NYA.items():
        q = json.loads(json.dumps(Q[uid]))
        assert [d['etikett'] for d in q['spelDelar']] == [d[0] for d in delar], uid
        for d in delar:
            kontroll(d[5], d[6])
        rad = '<br><span aria-hidden="true" style="display:block;height:7px"></span>'
        q['t'] = intro + '<p>' + rad.join(f'{e}) \\({fr}\\)' for e, fr, *_ in delar) + '</p>'
        q['s'] = huvud([(e, st, sv) for e, fr, st, sv, *_ in delar])
        q['rättSvar'] = [d[4] for d in delar]
        q['ledtrad'] = ledtrad
        for d, (e, fr, st, sv, *_r) in zip(q['spelDelar'], delar):
            d['fraga'] = f'<p>\\({fr}\\)</p>'
            d['s'] = kort(st, sv)
        nya[uid] = q
    q = json.loads(json.dumps(Q['2.117']))
    q['omr'] = 'produktregeln'
    q['familj'] = 'Derivering med produktregeln'
    q['familjNyckel'] = 'produktregeln__derivering_med_produktregeln'
    q['omrTidigare'] = list(dict.fromkeys((q.get('omrTidigare') or []) + ['kvotregeln']))
    q['familjTidigare'] = list(dict.fromkeys((q.get('familjTidigare') or []) + ['Derivering med kvotregeln']))
    q['s'] = S_2117
    # Delkort b hade ett trasigt facit (tomt steg 2). Delkort a står kvar (låst av delfacitgranskning-2026-11-01).
    q['spelDelar'][1]['s'] = kort([li('Funktionsvärdet \\(f(0)=2\\) ger \\(b\\)', p('Eftersom \\(e^0=1\\) och \\(a\\cdot0=0\\) är'),
                                     mt('f(0)=(a\\cdot0+b)e^0=b=2'))], '\\(b=2\\).')
    nya['2.117'] = q

    import bankobjekt as B  # noqa: E402
    ny_src = B.ersatt(src, nya)
    efter = json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    andr = sorted(x['id'] for x, y in zip(efter, bank) if x != y)
    assert andr == sorted(nya), andr
    for x in efter:
        if x['id'] in nya:
            assert x == nya[x['id']], x['id']
    print('ändrade:', andr)
    if '--skriv' in sys.argv:
        B.skriv(FIL, ny_src)


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.dont_write_bytecode = True
    main()
