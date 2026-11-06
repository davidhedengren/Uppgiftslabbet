"""Ma3c (mato1) kapitel 1, omgång 2: mängdträning på nivå 2–3, 6 november 2026.

Rationella uttryck (definitionsmängd och nollställen), polynomfunktioner (nollställen,
symmetrilinje, extremvärde och att bestämma f(x)) samt sekant och tangent. Hjälpfunktionerna
kommer från omgång 1 (tools/bygg-ma3c-kap1-mangdtraning-2026-11-06.py). Varje svar räknas fram
och kontrolleras med sympy.

  python tools/bygg-ma3c-kap1-mangdtraning2-2026-11-06.py [--skriv] [--varianter fil.json]
"""
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
_s = importlib.util.spec_from_file_location('k1', Path(__file__).with_name('bygg-ma3c-kap1-mangdtraning-2026-11-06.py'))
k1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(k1)
sp, x = k1.sp, k1.x
tal, tal_tex, poly, m, mt, p, li, fortecken = k1.tal, k1.tal_tex, k1.poly, k1.m, k1.mt, k1.p, k1.li, k1.fortecken
del_, uppgift, graf = k1.del_, k1.uppgift, k1.graf
BANK = k1.BANK
h = sp.Symbol('h')
PQ = r'x=-\tfrac p2\pm\sqrt{\left(\tfrac p2\right)^2-q}'


def rotter_pq(b, c):
    """Steg och rötter för x^2+bx+c=0 med pq-formeln (heltalsrötter)."""
    half = sp.Rational(-b, 2)
    disk = half**2 - c
    r = sorted(sp.solve(x**2 + b * x + c, x))
    steg = li(f'pq-formeln: {m(PQ)}', p(f'Här är {m(f"p={b}")} och {m(f"q={c}")}.'),
              mt(f'x={tal_tex(half)}\\pm\\sqrt{{{tal_tex(half**2)}{fortecken(tal_tex(-c))}}}={tal_tex(half)}\\pm{tal_tex(sp.sqrt(disk))}'),
              p('Det ger ' + ' och '.join(m(f'x={tal_tex(v)}') for v in r) + '.'))
    return r, steg


def mangd_del(fraga, steg, rotter, ledtrad, niva):
    rotter = sorted(rotter)
    vals = [int(v) if float(v).is_integer() else float(v) for v in rotter]
    svar = ', '.join(m(f'x={tal_tex(v)}') for v in rotter)
    if len(vals) == 1:
        return del_(fraga, steg, svar, ledtrad, vals[0], 'numeriskt', niva, ratt_txt=[tal(vals[0]).replace('−', '-'), f'x={vals[0]}'],
                    fel=[str(vals[0] + 1)])
    return del_(fraga, steg, svar, ledtrad, vals, 'numeriskt', niva)


# ---------------------------------------------------------------- rationella uttryck
def pa(v):
    """Tal i LaTeX, inom parentes bara när det är negativt."""
    return f'({tal_tex(v)})' if v < 0 else tal_tex(v)


def frac(t, n):
    return f'\\dfrac{{{t}}}{{{n}}}'


def rationella(nr):
    U = []
    F = 'Definitionsmängd för rationella uttryck'
    serier = [
        dict(a=(3, (2, -7)), b=('x+1', 16), c=('x-3', (2, -15)), d=('2x', 9)),
        dict(a=(5, (-4, 1)), b=('3x', 25), c=('x+2', (-1, -12)), d=('x-1', 4)),
        dict(a=(1, (6, 3)), b=('x-5', 49), c=('2x+1', (3, -10)), d=('7', 1)),
        dict(a=(4, (-2, -9)), b=('x', 36), c=('x+4', (-4, -21)), d=('x+3', 16)),
        dict(a=(2, (5, -1)), b=('x^2', 81), c=('5', (6, 8)), d=('x', 25)),
        dict(a=(7, (-3, 8)), b=('x+6', 4), c=('x-1', (1, -20)), d=('3x-2', 36)),
    ]
    for k, ser in enumerate(serier):
        delar = []
        # a) faktoriserad nämnare
        tl, (r1, r2) = ser['a']
        n = f'(x{fortecken(str(-r1))})(x{fortecken(str(-r2))})'
        steg = [li('Ett bråk är inte definierat när nämnaren är noll', mt(f'{n}=0')),
                li('Nollproduktmetoden', mt(f'\\begin{{aligned}}&x{fortecken(str(-r1))}=0\\;\\Rightarrow\\;x={r1}\\\\&x{fortecken(str(-r2))}=0\\;\\Rightarrow\\;x={r2}\\end{{aligned}}'))]
        delar.append(mangd_del(m(frac(tl, n)), steg, [r1, r2], 'När är ett bråk inte definierat? Sätt nämnaren lika med noll.', 2))
        # b) x^2 - k
        tl, kk = ser['b']
        r = int(sp.sqrt(kk))
        steg = [li('Nämnaren får inte vara noll', mt(f'x^2-{kk}=0\\;\\Rightarrow\\;x^2={kk}')),
                li('Dra roten ur – glöm inte den negativa lösningen', mt(f'x=\\pm{r}'))]
        delar.append(mangd_del(m(frac(tl, f'x^2-{kk}')), steg, [-r, r], 'Lös x² = ett tal. Hur många lösningar finns det?', 2))
        # c) x^2+bx+c med pq
        tl, (bb, cc) = ser['c']
        rr, pqsteg = rotter_pq(bb, cc)
        steg = [li('Nämnaren får inte vara noll', mt(f'{poly(x**2 + bb * x + cc)}=0')), pqsteg]
        if tl.startswith('x') and sp.sympify(tl.replace('x', '*x').lstrip('*')).subs(x, 0) is not None:
            pass
        delar.append(mangd_del(m(frac(tl, poly(x**2 + bb * x + cc))), steg, rr,
                               'Sätt nämnaren lika med noll och lös andragradsekvationen. Täljaren påverkar inte svaret.', 3))
        # d) x^3 - k x
        tl, kk = ser['d']
        r = int(sp.sqrt(kk))
        steg = [li('Nämnaren får inte vara noll', mt(f'x^3-{kk}x=0')),
                li('Bryt ut x', mt(f'x(x^2-{kk})=0')),
                li('Nollproduktmetoden', mt(f'x=0\\quad\\text{{eller}}\\quad x^2={kk}\\;\\Rightarrow\\;x=\\pm{r}'))]
        delar.append(mangd_del(m(frac(tl, f'x^3-{kk}x')), steg, [-r, 0, r], 'Bryt ut x ur nämnaren och använd nollproduktmetoden.', 3))
        intro = ['<p>För vilka värden på \\(x\\) är uttrycken inte definierade?</p>',
                 '<p>Bestäm de värden på \\(x\\) som inte ingår i uttryckens definitionsmängd.</p>',
                 '<p>Vilka \\(x\\)-värden måste uteslutas ur definitionsmängden?</p>'][k % 3]
        U.append(uppgift(nr, 'rationella_uttryck', F, intro, delar, formaga=('begrepp', 'procedur')))
        nr += 1
    # När är uttrycket lika med noll? Täljaren noll, men nämnaren inte noll.
    noll = [((x - 3) * (x + 1), (x - 3) * (x + 4)), ((x - 2) * (x + 2), (x - 2) * (x - 5)), ((x + 5) * (x - 1), x * (x + 5)),
            ((x - 4) * (x + 3), (x + 3) * (x - 6))]
    for k, (T, N) in enumerate(noll):
        tz = sorted(sp.solve(T, x)); nz = sorted(sp.solve(N, x))
        svar = [v for v in tz if v not in nz]
        steg = [li('Ett bråk är noll när täljaren är noll', mt(f'{poly(T)}=0\\;\\Rightarrow\\;' + '\\ \\text{eller}\\ '.join(f'x={tal_tex(v)}' for v in tz))),
                li('Nämnaren får inte vara noll', p(f'Nämnaren {m(poly(N))} är noll för ' + ' och '.join(m(f'x={tal_tex(v)}') for v in nz) + '.')),
                li('Stryk de x-värden där nämnaren är noll', p(f'Kvar blir {m("x=" + tal_tex(svar[0]))}.'))]
        d = mangd_del(f'<p>För vilket \\(x\\) är {m(frac(poly(T), poly(N)))} lika med noll?</p>', steg, svar,
                      'Bestäm när täljaren är noll. Kontrollera sedan att nämnaren inte också är noll för samma x.', 3)
        U.append(uppgift(nr, 'rationella_uttryck', F, '', [d], formaga=('begrepp', 'procedur')))
        nr += 1
    return U, nr


# ---------------------------------------------------------------- polynomfunktioner
def polynomfunktioner(nr):
    U = []
    F1 = 'Andragradsfunktioner och extremvärden'
    for k, (a, r1, r2) in enumerate([(1, -1, 5), (1, -6, 2), (-1, -3, 1), (2, 1, 5), (-1, -2, 6), (1, -4, 0), (-2, -1, 3), (1, 2, 8)]):
        e = sp.expand(a * (x - r1) * (x - r2))
        xs = sp.Rational(r1 + r2, 2)
        ys = e.subs(x, xs)
        art = 'minsta' if a > 0 else 'största'
        intro = f'<p>Funktionen är {m("f(x)=" + poly(e))}.</p>'
        b_, c_ = sp.Rational(int(sp.Poly(e, x).coeff_monomial(x)), a), sp.Rational(int(sp.Poly(e, x).coeff_monomial(1)), a)
        r, pqsteg = rotter_pq(int(b_), int(c_))
        nst = [li('Nollställena är lösningarna till f(x) = 0', mt(f'{poly(e)}=0'))]
        if a != 1:
            nst.append(li(f'Dela båda leden med {a}', mt(f'{poly(sp.expand(e / a))}=0')))
        nst.append(pqsteg)
        delar = [mangd_del('Bestäm funktionens nollställen.', nst, [r1, r2],
                           'Sätt f(x) = 0. Se till att koefficienten framför x² är 1 innan du använder pq-formeln.', 2),
                 del_('Bestäm symmetrilinjen.', [
                     li('Symmetrilinjen ligger mitt emellan nollställena', mt(f'x=\\frac{{{tal_tex(r1)}{fortecken(tal_tex(r2))}}}{{2}}={tal_tex(xs)}'))],
                     m(f'x={tal_tex(xs)}'), f'Nollställena är {m(f"x={r1}")} och {m(f"x={r2}")}. Var ligger punkten mitt emellan dem?',
                     int(xs) if xs.q == 1 else float(xs), 'numeriskt', 2,
                     ratt_txt=[tal(xs).replace('−', '-'), f'x={tal(xs).replace("−", "-").replace(",", ".")}'], fel=[str(int(xs) + 1)]),
                 del_(f'Bestäm funktionens {art} värde.', [
                     li('Extremvärdet finns på symmetrilinjen', p(f'Symmetrilinjen är {m(f"x={tal_tex(xs)}")}. '
                                                                  f'Grafen är en parabel som är {"öppen uppåt" if a > 0 else "öppen nedåt"}, eftersom koefficienten framför x² är {"positiv" if a > 0 else "negativ"}.')),
                     li(f'Beräkna {m(f"f({tal_tex(xs)})")}', mt(f'f({tal_tex(xs)})={k1.varde_steg(e, xs)[1]}={tal_tex(ys)}'),
                        graf(e, [r1, r2], f'Parabeln y = {poly(e)} med nollställena {r1} och {r2} och vertex i ({tal(xs)}, {tal(ys)}).',
                             punkter=[(float(xs), float(ys), f'({tal(xs)}; {tal(ys)})')]))],
                     f'Det {art} värdet är {m(tal_tex(ys))}.',
                     f'Funktionen har nollställena {r1} och {r2}. Extremvärdet finns mitt emellan dem.',
                     int(ys) if ys.q == 1 else float(ys), 'numeriskt', 3,
                     ratt_txt=[tal(ys).replace('−', '-')], fel=[str(int(ys) + 1), tal(xs).replace('−', '-')] if ys != xs else [str(int(ys) + 1)])]
        if k % 2 == 1:
            delar = delar[:2] + [delar[2]]
        U.append(uppgift(nr, 'polynomfunktioner', F1, intro, delar, mr=True, gg=True, formaga=('begrepp', 'procedur')))
        nr += 1
    F2 = 'Bestämma polynomfunktion från villkor'
    villkor = [((-2, 3), (0, -12), (1, 4, 2), (3, 6)), ((1, 5), (0, 10), (0, 3, -1), (2, -12)),
               ((-4, 2), (0, 16), (-1, 1, 3), (2, 30)), ((-3, -1), (0, 6), (0, 2, 4), (1, 6)),
               ((2, 6), (0, -24), (-2, 0, 1), (2, -32)), ((-5, 1), (0, 15), (1, 3, -3), (0, 18))]
    for k, ((a1, a2), (x0, y0), rot3, (xv, yv)) in enumerate(villkor):
        e1 = sp.expand((x - a1) * (x - a2))
        f1 = f'(x{fortecken(str(-a1))})(x{fortecken(str(-a2))})'
        kk = sp.Rational(y0, (x0 - a1) * (x0 - a2))
        e2 = sp.expand(kk * (x - a1) * (x - a2))
        f2 = (f'{tal(kk).replace("−", "-")}' if kk not in (1, -1) else ('-' if kk == -1 else '')) + f1
        r1_, r2_, r3_ = rot3
        prod3 = (x - r1_) * (x - r2_) * (x - r3_)
        k3 = sp.Rational(yv, prod3.subs(x, xv))
        e3 = sp.expand(k3 * prod3)
        f3_fakt = ''.join('x' if v == 0 else f'(x{fortecken(str(-v))})' for v in rot3)
        f3 = (f'{tal(k3).replace("−", "-")}' if k3 not in (1, -1) else ('-' if k3 == -1 else '')) + f3_fakt
        assert k3.q == 1 and kk.q == 1
        def ins(fakt, v):
            return fakt.replace('x', f'({v})' if v < 0 else str(v))
        delar = [
            del_(f'En andragradsfunktion har nollställena {m(f"x={a1}")} och {m(f"x={a2}")}, och koefficienten framför {m("x^2")} är 1. Bestäm {m("f(x)")}.',
                 [li(f'Faktorsatsen: nollstället {m("x=a")} ger faktorn {m("(x-a)")}', mt(f'f(x)={f1}')),
                  li('Utveckla om du vill skriva funktionen i allmän form', mt(f'f(x)={poly(e1)}'))],
                 m(f'f(x)={f1}={poly(e1)}'), 'Varje nollställe a ger en faktor (x − a).', f1, 'uttryck', 2,
                 ratt_txt=[f1, poly(e1), f'f(x)={poly(e1)}'], fel=[f'(x{fortecken(str(a1))})(x{fortecken(str(a2))})']),
            del_(f'En andragradsfunktion har nollställena {m(f"x={a1}")} och {m(f"x={a2}")}. Dessutom är {m(f"f({x0})={y0}")}. Bestäm {m("f(x)")}.',
                 [li(f'Nollställena ger formen {m("f(x)=k(x-a)(x-b)")}', mt(f'f(x)=k{f1}')),
                  li(f'Sätt in villkoret {m(f"f({x0})={y0}")}', mt(f'k\\cdot {ins(f1, x0)}={y0}\\;\\Rightarrow\\;k={tal_tex(kk)}')),
                  li('Skriv funktionen', mt(f'f(x)={f2}={poly(e2)}'))],
                 m(f'f(x)={f2}'), f'Skriv f(x) = k(x − a)(x − b) och använd villkoret f({x0}) = {y0} för att bestämma k.', f2, 'uttryck', 3,
                 ratt_txt=[f2, poly(e2)], fel=[f1]),
            del_(f'En tredjegradsfunktion har nollställena ' + ', '.join(m(f'x={v}') for v in rot3) + f'. Dessutom är {m(f"f({xv})={yv}")}. Bestäm {m("f(x)")}.',
                 [li(f'Tre nollställen ger formen {m("f(x)=k(x-a)(x-b)(x-c)")}', mt(f'f(x)=k\\,{f3_fakt}')),
                  li(f'Sätt in villkoret {m(f"f({xv})={yv}")}', mt(f'k\\cdot {tal_tex(prod3.subs(x, xv))}={yv}\\;\\Rightarrow\\;k={tal_tex(k3)}')),
                  li('Skriv funktionen', mt(f'f(x)={f3}'))],
                 m(f'f(x)={f3}'), 'Skriv funktionen med en okänd konstant k framför faktorerna och bestäm k med villkoret.', f3, 'uttryck', 3,
                 ratt_txt=[f3, poly(e3)], fel=[f3_fakt] if k3 != 1 else [poly(e3 + 1)]),
        ]
        for d, e in zip(delar, (e1, e2, e3)):
            assert sp.expand(k1.till_sympy(d['ratt']) - e) == 0, d['ratt']
        U.append(uppgift(nr, 'polynomfunktioner', F2, '', delar, formaga=('procedur', 'problemlösning')))
        nr += 1
    return U, nr


# ---------------------------------------------------------------- sekant och tangent
def sekant(nr):
    U = []
    F = 'Sekant, tangent och gränsvärde'
    funk = [(1, 2, 0, 1, 3, 2), (2, -1, 0, 0, 2, 1), (1, -4, 3, 1, 4, 3), (3, 0, -2, -1, 2, 1),
            (-1, 6, 0, 1, 5, 2), (2, 3, 1, -2, 1, 1), (1, 0, 5, 2, 6, 3), (-2, 4, 1, 0, 3, 2)]
    for k, (a, b, c, x1, x2, x0) in enumerate(funk):
        e = a * x**2 + b * x + c
        f = lambda v: e.subs(x, v)
        intro = f'<p>Funktionen är {m("f(x)=" + poly(e))}.</p>'
        k12 = (f(x2) - f(x1)) / (x2 - x1)
        x3 = sp.Rational(x0) + sp.Rational(1, 10)
        k03 = (f(x3) - f(x0)) / sp.Rational(1, 10)
        kv = sp.expand((e.subs(x, x0 + h) - f(x0)) / h)
        kv = sp.simplify(kv)
        tang = kv.subs(h, 0)
        kvt = poly(sp.expand(kv).subs(h, x)).replace('x', 'h')
        regel = r'k=\dfrac{f(x_2)-f(x_1)}{x_2-x_1}'
        delar = [
            del_(f'Bestäm lutningen för sekanten genom punkterna på grafen där {m(f"x={x1}")} och {m(f"x={x2}")}.',
                 [li(f'Beräkna funktionsvärdena', mt(f'f({tal_tex(x1)})={tal_tex(f(x1))},\\quad f({tal_tex(x2)})={tal_tex(f(x2))}')),
                  li(f'Sekantens lutning: {m(regel)}', mt(f'k=\\dfrac{{{tal_tex(f(x2))}-{pa(f(x1))}}}{{{tal_tex(x2)}-{pa(x1)}}}={tal_tex(k12)}'))],
                 f'Lutningen är {m(tal_tex(k12))}.', 'Beräkna y-värdena i de två punkterna och dela förändringen i y med förändringen i x.',
                 int(k12), 'numeriskt', 2, ratt_txt=[tal(k12).replace('−', '-')], fel=[str(int(-k12))] if k12 else ['1']),
            del_(f'Bestäm lutningen för sekanten mellan {m(f"x={x0}")} och {m(f"x={tal_tex(x3)}")}.',
                 [li('Beräkna funktionsvärdena', mt(f'f({tal_tex(x0)})={tal_tex(f(x0))},\\quad f({tal_tex(x3)})={tal_tex(f(x3))}')),
                  li(f'Sekantens lutning: {m(regel)}', mt(f'k=\\dfrac{{{tal_tex(f(x3))}-{pa(f(x0))}}}{{0{{,}}1}}={tal_tex(k03)}'))],
                 f'Lutningen är {m(tal_tex(k03))}.', 'Skillnaden i x är bara 0,1. Var noga med decimalerna i f-värdena.',
                 float(k03), 'numeriskt', 2, ratt_txt=[tal(k03).replace('−', '-'), tal(k03).replace('−', '-').replace(',', '.')],
                 fel=[tal(k03 + 1).replace('−', '-')]),
            del_(f'Förenkla ändringskvoten {m(f"\\dfrac{{f({x0}+h)-f({x0})}}{{h}}")}, där {m("h\\ne0")}.',
                 [li(f'Beräkna {m(f"f({x0}+h)")}', mt(f'f({x0}+h)={poly(sp.expand(e.subs(x, x0 + h)).subs(h, x)).replace("x", "h")}')),
                  li(f'Dra bort {m(f"f({x0})={tal_tex(f(x0))}")} och dela med h', mt(f'\\dfrac{{{poly(sp.expand(e.subs(x, x0 + h) - f(x0)).subs(h, x)).replace("x", "h")}}}{{h}}={kvt}'))],
                 m(kvt), f'Sätt in {x0} + h i stället för x och utveckla. Varje term i täljaren ska innehålla h innan du delar.',
                 kvt, 'uttryck', 3, ratt_txt=[kvt, kvt.replace('h', '*h').lstrip('*') if False else kvt], fel=[poly(sp.expand(kv + 1).subs(h, x)).replace('x', 'h')]),
            del_(f'Bestäm tangentens lutning i punkten där {m(f"x={x0}")}.',
                 [li(f'Tangentens lutning är gränsvärdet av ändringskvoten när {m("h\\to0")}', mt(f'\\dfrac{{f({x0}+h)-f({x0})}}{{h}}={kvt}')),
                  li(f'Låt h gå mot 0', mt(f'\\lim_{{h\\to0}}({kvt})={tal_tex(tang)}'))],
                 f'Tangentens lutning är {m(tal_tex(tang))}.', 'Förenkla ändringskvoten och låt h gå mot noll.',
                 int(tang), 'numeriskt', 3, ratt_txt=[tal(tang).replace('−', '-')], fel=[tal(k03).replace('−', '-')]),
        ]
        assert sp.simplify(k1.till_sympy(kvt.replace('h', 'x')).subs(x, h) - kv) == 0
        U.append(uppgift(nr, 'tangent_sekant', F, intro, delar, mr=True, formaga=('begrepp', 'procedur')))
        nr += 1
    return U, nr


def main():
    src = BANK.read_text(encoding='utf-8')
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    import re
    nr = 1 + max(int(q['id'].split('.')[1]) for q in bank if re.match(r'^1\.\d+$', q['id']))
    if '--start' in sys.argv:
        nr = int(sys.argv[sys.argv.index('--start') + 1])
    U = []
    for bygg in (rationella, polynomfunktioner, sekant):
        nya, nr = bygg(nr)
        U += nya
    befintliga = {q['id'] for q in bank}
    assert not befintliga & {q['id'] for q in U}
    kort = sum(len(q.get('spelDelar') or [1]) for q in U)
    print('uppgifter', len(U), 'kort', kort, 'id', U[0]['id'], '–', U[-1]['id'])
    if '--varianter' in sys.argv:
        Path(sys.argv[sys.argv.index('--varianter') + 1]).write_text(json.dumps(k1.VARIANTER, ensure_ascii=False, indent=1), encoding='utf-8')
    if '--skriv' in sys.argv:
        end = src.rindex(']')
        ny = src[:end].rstrip() + ',\n' + json.dumps(U, ensure_ascii=False, indent=2)[1:-1].strip('\n') + '\n' + src[end:]
        with open(BANK, 'w', encoding='utf-8', newline='') as fh:
            fh.write(ny)


if __name__ == '__main__':
    main()
