"""Ma3c (mato1) kapitel 1, omgång 3: förkorta och räkna med rationella uttryck, 6 november 2026.

Svaren rättas med Kunskapsgymmets nya format "förkortat_uttryck": algebraiskt lika med facit och
dessutom förkortat. Då godtas inte längre frågan avskriven. Hjälpfunktioner från omgång 1.

  python tools/bygg-ma3c-kap1-mangdtraning3-2026-11-06.py [--skriv] [--varianter fil.json]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
_s = importlib.util.spec_from_file_location('k1', Path(__file__).with_name('bygg-ma3c-kap1-mangdtraning-2026-11-06.py'))
k1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(k1)
sp, x = k1.sp, k1.x
tal, tal_tex, poly, m, mt, p, li, fortecken = k1.tal, k1.tal_tex, k1.poly, k1.m, k1.mt, k1.p, k1.li, k1.fortecken
del_, uppgift = k1.del_, k1.uppgift
BANK = k1.BANK
FMT = 'förkortat_uttryck'


def lin(a, b):
    return poly(a * x + b)


def fak(*faktorer):
    """Produkt av faktorer som text: konstant, x-potens och parenteser."""
    s = ''
    for f in faktorer:
        if isinstance(f, (int, sp.Integer)):
            s = (str(f) if f != -1 else '-') + s
        elif f == x:
            s += 'x'
        else:
            s += f'({poly(f)})'
    return s or '1'


def frac(t, n):
    return f'\\dfrac{{{t}}}{{{n}}}'


def svarstext(num, den):
    """Elevtext för ett bråk."""
    if den == '1':
        return num
    nt = num if re.fullmatch(r'-?\d*x?', num) else f'({num})'
    dt = den if re.fullmatch(r'-?\d*x', den) or re.fullmatch(r'\d+', den) else f'({den})'
    return f'{nt}/{dt}'


def kontroll(fraga_sympy, svar):
    """Svaret ska vara lika med frågan och förkortat."""
    s = k1.till_sympy(svar)
    assert sp.simplify(fraga_sympy - s) == 0, (svar,)
    n, d = sp.fraction(sp.together(s))
    n, d = sp.expand(n), sp.expand(d)
    assert sp.degree(sp.gcd(n, d), x) == 0, svar
    return True


def forkorta_del(T, N, Tf, Nf, gemensam, svar_num, svar_den, ledtrad, niva, regel_t, regel_n):
    """T/N med faktoriseringar Tf, Nf (text) och den gemensamma faktorn."""
    svar = svarstext(svar_num, svar_den)
    kontroll(T / N, svar)
    steg = [li(f'Faktorisera täljaren – {regel_t}', mt(f'{poly(T)}={Tf}')),
            li(f'Faktorisera nämnaren – {regel_n}', mt(f'{poly(N)}={Nf}')) if regel_n else None,
            li(f'Stryk den gemensamma faktorn {m(gemensam)}',
               mt(f'{frac(Tf, Nf)}={frac(svar_num, svar_den) if svar_den != "1" else svar_num}'))]
    steg = [s for s in steg if s]
    svar_tex = frac(svar_num, svar_den) if svar_den != '1' else svar_num
    fraga = m(frac(poly(T), poly(N)))
    return del_(fraga, steg, m(svar_tex), ledtrad, svar, FMT, niva,
                ratt_txt=[svar], fel=[f'({poly(T)})/({poly(N)})', f'({Tf})/({Nf})'])


def forkorta(nr):
    U = []
    F = 'Förkorta rationella uttryck'
    serier = [(3, (2, -15), (5, 2), (2, 3)), (4, (1, -12), (3, 1), (3, 5)), (5, (-1, -6), (2, 3), (2, 4)),
              (2, (3, -10), (4, 3), (5, 1)), (6, (5, 6), (3, 2), (3, 2)), (7, (-2, -8), (4, 1), (4, 6)),
              (1, (7, 12), (4, 3), (2, 2)), (8, (-3, -18), (6, 3), (6, 1))]
    for k, (a, (b, c), (r_extra, _), (kk, mm)) in enumerate(serier):
        delar = []
        # a) (x^2-a^2)/(x+a) = x-a
        T, N = x**2 - a * a, x + a
        delar.append(forkorta_del(T, N, f'(x+{a})(x-{a})', f'x+{a}', f'(x+{a})', f'x-{a}', '1',
                                  'Kan täljaren faktoriseras med konjugatregeln?', 2,
                                  f'konjugatregeln {m("a^2-b^2=(a+b)(a-b)")}', None))
        # b) (x^2+bx+c)/(x^2-r^2) med en gemensam faktor
        r1, r2 = sorted(sp.solve(x**2 + b * x + c, x))
        gem = r1 if abs(r1) != abs(r2) or True else r2
        # nämnaren väljs som konjugat med samma nollställe gem
        g = abs(int(gem))
        T, N = x**2 + b * x + c, x**2 - g * g
        Tf = f'(x{fortecken(str(-int(r1)))})(x{fortecken(str(-int(r2)))})'
        Nf = f'(x+{g})(x-{g})'
        annan_t = int(r2) if gem == r1 else int(r1)
        gem_f = f'(x{fortecken(str(-int(gem)))})'
        annan_n = -g if int(gem) == g else g
        svar_num, svar_den = f'x{fortecken(str(-annan_t))}', f'x{fortecken(str(-annan_n))}'
        delar.append(forkorta_del(T, N, Tf, Nf, gem_f, svar_num, svar_den,
                                  'Faktorisera både täljare och nämnare. Vilken faktor finns i båda?', 2,
                                  f'nollställena {m(f"x={int(r1)}")} och {m(f"x={int(r2)}")} ger faktorerna',
                                  f'konjugatregeln {m("a^2-b^2=(a+b)(a-b)")}'))
        # c) (k x^2 - k m x)/(x^2 - 2 m x + m^2) = k x/(x-m)
        T, N = kk * x**2 - kk * mm * x, x**2 - 2 * mm * x + mm * mm
        delar.append(forkorta_del(T, N, f'{kk}x(x-{mm})', f'(x-{mm})^2', f'(x-{mm})', f'{kk}x', f'x-{mm}',
                                  'Bryt ut den gemensamma faktorn i täljaren. Känner du igen nämnaren som en kvadrat?', 3,
                                  f'bryt ut {m(f"{kk}x")}', f'kvadreringsregeln {m("(a-b)^2=a^2-2ab+b^2")}'))
        intro = ['<p>Förkorta så långt som möjligt.</p>', '<p>Förenkla uttrycken genom att förkorta.</p>',
                 '<p>Faktorisera och förkorta.</p>'][k % 3]
        U.append(uppgift(nr, 'forkorta_rationella', F, intro, delar, formaga=('procedur',)))
        nr += 1
    return U, nr


def definitionsvillkor(nr):
    U = []
    F = 'Förenkla och ange definitionsvillkor'
    # (x-a)(x-b)/((x-a)(x-c)) -> (x-b)/(x-c); ekvation (x-b)/(x-c) = q
    data = [(2, -3, 4, 2), (-1, 4, 2, 3), (3, 1, -2, 2), (-4, -1, 1, 3), (5, -6, 3, 4), (1, -5, -3, 2)]
    for k, (a, b, c, q) in enumerate(data):
        T, N = sp.expand((x - a) * (x - b)), sp.expand((x - a) * (x - c))
        Tf = f'(x{fortecken(str(-a))})(x{fortecken(str(-b))})'
        Nf = f'(x{fortecken(str(-a))})(x{fortecken(str(-c))})'
        num, den = f'x{fortecken(str(-b))}', f'x{fortecken(str(-c))}'
        rt1, rt2 = sorted(sp.solve(T, x)); rn1, rn2 = sorted(sp.solve(N, x))
        uteslut = sorted({int(a), int(c)})
        steg_a = [li('Faktorisera täljaren med hjälp av dess nollställen', mt(f'{poly(T)}={Tf}')),
                  li('Faktorisera nämnaren på samma sätt', mt(f'{poly(N)}={Nf}')),
                  li(f'Stryk den gemensamma faktorn {m(f"(x{fortecken(str(-a))})")}', mt(f'{frac(Tf, Nf)}={frac(num, den)}'))]
        svar = f'({num})/({den})'
        kontroll(T / N, svar)
        steg_b = [li('Det ursprungliga uttrycket är inte definierat där nämnaren är noll', mt(f'{Nf}=0')),
                  li(f'Nollproduktmetoden: en produkt är noll när någon faktor är noll', p(f'Nämnaren är noll för {m(f"x={uteslut[0]}")} och {m(f"x={uteslut[1]}")}. '
                                             f'Båda ska uteslutas, även {m(f"x={a}")} vars faktor försvinner när man förkortar.'))]
        # c) (x-b)/(x-c) = q  =>  x-b = q(x-c)  =>  x = (q c - b)/(q - 1)
        xs = sp.Rational(q * c - b, q - 1)
        assert xs not in (a, c) and xs.q == 1
        steg_c = [li('Det förenklade uttrycket gäller för alla tillåtna x', mt(f'{frac(num, den)}={q}')),
                  li('Multiplicera båda leden med nämnaren', mt(f'{num}={q}({den})={poly(q * (x - c))}')),
                  li('Samla x-termerna i vänsterledet och talen i högerledet',
                     mt(f'{poly((1 - q) * x)}={tal_tex(b - q * c)}' + (f'\\Rightarrow x={tal_tex(xs)}' if q != 0 else ''))),
                  li('Kontrollera att lösningen är tillåten', p(f'{m(f"x={tal_tex(xs)}")} är inte ett av de uteslutna värdena {m(f"x={uteslut[0]}")} och {m(f"x={uteslut[1]}")}.'))]
        intro = f'<p>Uttrycket är {m(frac(poly(T), poly(N)))}.</p>'
        delar = [del_('Förkorta uttrycket så långt som möjligt.', steg_a, m(frac(num, den)),
                      'Faktorisera täljare och nämnare. Båda har en faktor gemensamt.', svar, FMT, 2,
                      ratt_txt=[svar], fel=[f'({poly(T)})/({poly(N)})']),
                 del_('Vilka värden på x är inte tillåtna i uttrycket?', steg_b, ', '.join(m(f'x={v}') for v in uteslut),
                      'Utgå från nämnaren i det ursprungliga uttrycket, inte i det förkortade.', uteslut, 'numeriskt', 2),
                 del_(f'Lös ekvationen {m(frac(poly(T), poly(N)) + f"={q}")}.', steg_c, m(f'x={tal_tex(xs)}'),
                      'Förkorta först. Multiplicera sedan med nämnaren och kontrollera att svaret är tillåtet.',
                      int(xs), 'numeriskt', 3, ratt_txt=[str(int(xs)), f'x={int(xs)}'], fel=[str(int(xs) + 1)])]
        U.append(uppgift(nr, 'forkorta_rationella', F, intro, delar, formaga=('procedur', 'begrepp')))
        nr += 1
    return U, nr


def rakna(nr):
    U = []
    F = 'Räkna med rationella uttryck'
    data = [(3, 2, 4, 1, (2, 1, 3, 2)), (5, 1, 2, 3, (1, 2, 4, -1)), (2, 4, 6, 2, (3, 1, 2, 3)), (4, 3, 1, 5, (2, -3, 1, 2)),
            (6, 1, 3, 4, (1, 4, 3, -2)), (1, 5, 5, 1, (4, 1, 1, 3)), (7, 2, 2, 3, (2, 5, 1, -1)), (3, 6, 4, 4, (5, 2, 2, 1))]
    for k, (a, b, c, d, (p1, a1, q1, b1)) in enumerate(data):
        delar = []
        # a) (x^2-a^2)/(x+b) * (x+b)/(x-a) = x+a
        e = (x**2 - a * a) / (x + b) * (x + b) / (x - a)
        svar = f'x+{a}'
        kontroll(e, svar)
        steg = [li('Multiplicera täljare med täljare och nämnare med nämnare', mt(frac(f'({poly(x**2 - a*a)})(x+{b})', f'(x+{b})(x-{a})'))),
                li(f'Konjugatregeln: {m(f"x^2-{a*a}=(x+{a})(x-{a})")}', mt(frac(f'(x+{a})(x-{a})(x+{b})', f'(x+{b})(x-{a})'))),
                li(f'Stryk de gemensamma faktorerna {m(f"(x+{b})")} och {m(f"(x-{a})")}', mt(f'x+{a}'))]
        delar.append(del_(m(frac(poly(x**2 - a * a), f'x+{b}') + '\\cdot' + frac(f'x+{b}', f'x-{a}')), steg, m(f'x+{a}'),
                          'Skriv produkten som ett enda bråk och faktorisera innan du förkortar.', svar, FMT, 2,
                          ratt_txt=[svar], fel=[f'({poly(x**2 - a*a)})/(x-{a})']))
        # b) (x^2-c^2)/(x+d) ÷ (x-c)/(x+d) = x+c
        e = ((x**2 - c * c) / (x + d)) / ((x - c) / (x + d))
        svar = f'x+{c}'
        kontroll(e, svar)
        steg = [li('Division med ett bråk är multiplikation med det inverterade bråket',
                   mt(frac(poly(x**2 - c*c), f'x+{d}') + '\\div' + frac(f'x-{c}', f'x+{d}') + '=' + frac(poly(x**2 - c*c), f'x+{d}') + '\\cdot' + frac(f'x+{d}', f'x-{c}'))),
                li(f'Konjugatregeln och förkortning', mt(frac(f'(x+{c})(x-{c})(x+{d})', f'(x+{d})(x-{c})') + f'=x+{c}'))]
        delar.append(del_(m(frac(poly(x**2 - c * c), f'x+{d}') + '\\div' + frac(f'x-{c}', f'x+{d}')), steg, m(f'x+{c}'),
                          'Byt division mot multiplikation med det inverterade bråket.', svar, FMT, 2,
                          ratt_txt=[svar], fel=[f'({poly(x**2 - c*c)})/(x-{c})']))
        # c) p1/(x-a1) + q1/(x+b1)
        e = sp.Rational(p1) / (x - a1) + sp.Rational(q1) / (x + b1)
        tal_ = sp.expand(p1 * (x + b1) + q1 * (x - a1))
        nf = f'(x{fortecken(str(-a1))})(x{fortecken(str(b1))})'
        svar = f'({poly(tal_)})/({nf})'
        kontroll(e, svar)
        steg = [li('Gemensam nämnare: produkten av de två nämnarna',
                   p(f'Förläng varje bråk med den faktor som saknas, så att båda får nämnaren {m(nf)}.'),
                   mt(frac(f'{p1 if p1 != 1 else ""}(x{fortecken(str(b1))})', nf) + '+' + frac(f'{q1 if q1 != 1 else ""}(x{fortecken(str(-a1))})', nf))),
                li('Addera täljarna och förenkla', mt(frac(f'{poly(p1*(x+b1))}{fortecken(poly(q1*(x-a1)))}', nf) + '=' + frac(poly(tal_), nf))),
                li('Kontrollera att bråket inte kan förkortas', p(f'Täljaren {m(poly(tal_))} har inte någon faktor gemensam med nämnaren.'))]
        delar.append(del_('Skriv som ett enda bråk: ' + m(frac(str(p1), f'x{fortecken(str(-a1))}') + '+' + frac(str(q1), f'x{fortecken(str(b1))}')), steg,
                          m(frac(poly(tal_), nf)), 'Skriv bråken med gemensam nämnare. Använd produkten av de två nämnarna.', svar, FMT, 3,
                          ratt_txt=[svar, f'({poly(tal_)})/({poly(sp.expand((x - a1) * (x + b1)))})'],
                          fel=[f'{p1}/(x{fortecken(str(-a1))})+{q1}/(x{fortecken(str(b1))})', f'{p1 + q1}/({nf})']))
        intro = ['<p>Förenkla så långt som möjligt.</p>', '<p>Beräkna och förkorta så långt som möjligt.</p>',
                 '<p>Skriv som ett enda bråk i förkortad form.</p>'][k % 3]
        U.append(uppgift(nr, 'rakna_rationella', F, intro, delar, formaga=('procedur',)))
        nr += 1
    return U, nr


def main():
    src = BANK.read_text(encoding='utf-8')
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    nr = 1 + max(int(q['id'].split('.')[1]) for q in bank if re.match(r'^1\.\d+$', q['id']))
    U = []
    for bygg in (forkorta, definitionsvillkor, rakna):
        nya, nr = bygg(nr)
        U += nya
    assert not {q['id'] for q in bank} & {q['id'] for q in U}
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
