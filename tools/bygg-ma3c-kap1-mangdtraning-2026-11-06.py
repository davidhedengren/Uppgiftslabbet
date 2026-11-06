"""Ma3c (mato1) kapitel 1: mängdträning på nivå 2–3, 6 november 2026.

Användaren vill ha många vanliga räkneuppgifter att mängdträna på: ibland en ensam uppgift,
ibland a), b), c) … där a) är enklast och de senare delarna svårare. Varje svar räknas fram och
kontrolleras med sympy innan uppgiften skrivs. Facit följer agent/FACITMALL.md.

  python tools/bygg-ma3c-kap1-mangdtraning-2026-11-06.py [--skriv] [--varianter fil.json]
"""
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / 'uppgiftermato1.js'
x = sp.Symbol('x')
FORSTA_ID = 1004
VARIANTER = {}  # kort-id -> {"ratt": [...], "fel": [...]} för tools/kg-sjalvrattning-kontroll.cjs


# ---------------------------------------------------------------- formattering
def tal(v):
    """Tal med decimalkomma, utan onödiga decimaler."""
    v = Fraction(v).limit_denominator(1000)
    if v.denominator == 1:
        return str(v.numerator).replace('-', '−')
    return f'{float(v):g}'.replace('.', ',').replace('-', '−')


def tal_tex(v):
    return tal(v).replace('−', '-').replace(',', '{,}')


def poly(e, var='x'):
    """Utvecklat polynom i x som text (fungerar både som elevsvar och i LaTeX)."""
    e = sp.expand(e)
    if e == 0:
        return '0'
    p = sp.Poly(e, x)
    delar = []
    for (d,), c in sorted(p.terms(), key=lambda t: -t[0][0]):
        c = sp.Rational(c)
        assert c.q == 1, e
        c = int(c)
        mag = abs(c)
        if d == 0:
            term = str(mag)
        else:
            term = ('' if mag == 1 else str(mag)) + (var if d == 1 else f'{var}^{d}')
        delar.append(('-' if c < 0 else '+', term))
    s = ''.join(f'{t}' if i == 0 and sg == '+' else f'{sg}{t}' for i, (sg, t) in enumerate(delar))
    return s


def lin(a, b):
    """ax+b som text, t.ex. 3x-2, x+5, -x+4, 2x."""
    return poly(a * x + b)


def par(s):
    return f'({s})'


def m(t):
    return f'\\({t}\\)'


def _toppnivå_split(t, tecken):
    delar, djup, start, i = [], 0, 0, 0
    while i < len(t):
        c = t[i]
        if c in '{(':
            djup += 1
        elif c in '})':
            djup -= 1
        elif djup == 0 and t.startswith(tecken, i):
            delar.append(t[start:i]); start = i + len(tecken); i += len(tecken); continue
        i += 1
    delar.append(t[start:])
    return delar


def _synlig_langd(t):
    import re
    t = re.sub(r'\\(cdot|quad|tfrac|sqrt|left|right|pm|Rightarrow)', 'x', t)
    return len(re.sub(r'[{}\\^]', '', t))


BS = '\\\\'[0]


def mt(t):
    """Matematikrad. Långa kedjor bryts så att varje likhetstecken börjar en ny rad (mobil)."""
    if '\\quad' in t:
        rader = [r.strip(', ') for r in t.split('\\quad')]
        t = '\\begin{aligned}' + '\\\\'.join('&' + r for r in rader) + '\\end{aligned}'
    elif 'aligned' in t:
        pass
    elif 'Rightarrow' in t and _synlig_langd(t) > 18:
        led = t.split(BS + ';' + BS + 'Rightarrow' + BS + ';')
        if len(led) == 1:
            led = t.split(BS + 'Rightarrow')
        t = BS + 'begin{aligned}&' + (BS * 2 + '&' + BS + 'Rightarrow' + BS + ';').join(led) + BS + 'end{aligned}'
    elif _synlig_langd(t) > 18:
        led = _toppnivå_split(t, '=')
        if len(led) > 2 and _synlig_langd(led[0]) <= 3:
            led = [led[0] + '=' + led[1]] + led[2:]
        if len(led) > 1:
            rader = [led[0]] + ['=' + r for r in led[1:]]
            t = '\\begin{aligned}' + '\\\\'.join('&' + r2 for r in rader for r2 in _bryt_lang(r)) + '\\end{aligned}'
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def _bryt_lang(r):
    """Dela ett för långt led vid ett plus- eller minustecken på toppnivå nära mitten."""
    if _synlig_langd(r) <= 24:
        return [r]
    djup, kandidater = 0, []
    for i, c in enumerate(r):
        if c in '{(':
            djup += 1
        elif c in '})':
            djup -= 1
        elif djup == 0 and c in '+-' and i > 1 and r[i - 1] not in '=(^{':
            kandidater.append(i)
    if not kandidater:
        return [r]
    mitt = len(r) / 2
    i = min(kandidater, key=lambda k: abs(k - mitt))
    return [r[:i], '\\quad ' + r[i:]]


def p(t):
    return f'<p>{t}</p>'


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def steglista(steg):
    return '<ol class="facit-steglista" role="list">' + ''.join(steg) + '</ol>'


def svarsrad(text):
    return f'<p class="facit-svar"><strong>Svar:</strong> {text}</p>'


def tex(s):
    """Elevtext (x^2, *) till LaTeX."""
    return s.replace('*', '\\cdot ')


# ---------------------------------------------------------------- uppgiftsbygge
NIVA = {2: ('E', '1/0/0', 1), 3: ('C', '0/1/0', 2)}


def del_(fraga, steg, svar_tex, ledtrad, ratt, fmt, niva, ratt_txt=None, fel=()):
    return dict(fraga=fraga, steg=steg, svar=svar_tex, ledtrad=ledtrad, ratt=ratt, fmt=fmt, niva=niva,
                ratt_txt=ratt_txt or [], fel=list(fel))


def uppgift(nr, omr, familj, intro, delar, formaga=('procedur',), mr=False, gg=False):
    uid = f'1.{nr}'
    if len(delar) == 1:
        d = delar[0]
        en, po, ai = NIVA[d['niva']]
        q = dict(id=uid, kap=1, omr=omr, kurs=['1b', '1c'], familj=familj, niva=en, poang=po,
                 traningsniva=d['niva'], arbetsinsats=ai, formaga=list(formaga), miniräknare=mr, geogebra=gg,
                 spel=True, självrättning=True, t=intro + d['fraga'],
                 s='<div class="facit-v2 facit-stegvis">' + steglista(d['steg']) + svarsrad(d['svar']) + '</div>',
                 ledtrad=p(d['ledtrad']), rättSvar=d['ratt'])
        if isinstance(d['ratt'], list):
            q.update(svarstyp='flera_delar', svarFormat=[d['fmt']] * len(d['ratt']), svarsstruktur='mängd',
                     antalSvar=len(d['ratt']), tolerans=[1e-9] * len(d['ratt']))
        else:
            q.update(svarstyp='numeriskt' if d['fmt'] == 'numeriskt' else 'uttryck', svarFormat=d['fmt'],
                     tolerans=1e-9 if d['fmt'] == 'numeriskt' else None)
        VARIANTER[uid] = dict(ratt=d['ratt_txt'], fel=d['fel'])
        return q
    bok = 'abcdefg'
    niv = [d['niva'] for d in delar]
    e_ = sum(1 for n in niv if n == 2)
    c_ = sum(1 for n in niv if n == 3)
    t = intro + ''.join(f'<p>{bok[i]}) {d["fraga"]}</p>' for i, d in enumerate(delar))
    def delfacit(d):
        return '<div class="facit-v2 facit-stegvis">' + steglista(d['steg']) + svarsrad(d['svar']) + '</div>'
    s = '<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{bok[i]})</span><div class="facit-arbete">{delfacit(d)}</div></div>'
        for i, d in enumerate(delar)) + '</div>'
    q = dict(id=uid, kap=1, omr=omr, kurs=['1b', '1c'], familj=familj,
             niva='C' if c_ else 'E', poang=f'{e_}/{c_}/0', traningsniva=max(niv),
             arbetsinsats=min(3, len(delar)), formaga=list(formaga), miniräknare=mr, geogebra=gg,
             spel=True, självrättning=True, t=t, s=s,
             ledtrad=p(delar[0]['ledtrad']),
             rättSvar=[d['ratt'] for d in delar],
             svarFormat=[([d['fmt']] * len(d['ratt']) if isinstance(d['ratt'], list) else d['fmt']) for d in delar],
             tolerans=[([1e-9] * len(d['ratt']) if isinstance(d['ratt'], list) else (1e-9 if d['fmt'] == 'numeriskt' else None)) for d in delar],
             svarstyp='flera_delar', svarsstruktur='ordnad', svarEtiketter=list(bok[:len(delar)]),
             spelDelning='deluppgifter', spelIntro=intro, spelDelar=[])
    for i, d in enumerate(delar):
        en, po, ai = NIVA[d['niva']]
        q['spelDelar'].append(dict(etikett=bok[i], fraga=d['fraga'], s=delfacit(d), ledtrad=p(d['ledtrad']),
                                   niva=en, poang=po, traningsniva=d['niva'], arbetsinsats=ai))
        VARIANTER[uid + bok[i]] = dict(ratt=d['ratt_txt'], fel=d['fel'])
    return q


# ---------------------------------------------------------------- byggstenar: utveckla
def produkt(a, b, c, d):
    """(ax+b)(cx+d)."""
    A, B = lin(a, b), lin(c, d)
    e = (a * x + b) * (c * x + d)
    fyra = f'{poly(a*c*x**2)}{fortecken(poly(a*d*x))}{fortecken(poly(b*c*x))}{fortecken(poly(b*d))}'
    steg = [li(f'Multiplicera varje term i {m(par(A))} med varje term i {m(par(B))}',
               mt(f'{par(A)}{par(B)}={fyra}')),
            li(f'Samla x-termerna: {m(poly(a*d*x))} och {m(poly(b*c*x))} ger {m(poly((a*d+b*c)*x))}',
               mt(f'{fyra}={poly(e)}'))]
    return e, steg, f'{par(A)}{par(B)}'


def fortecken(s):
    if s == '0':
        return '+0'
    return s if s.startswith('-') else '+' + s


def kvadrat(a, b):
    """(ax+b)^2 med kvadreringsregeln."""
    A = lin(a, b)
    e = (a * x + b) ** 2
    ax_ = poly(a * x)
    minus = b < 0
    regel = r'(a-b)^2=a^2-2ab+b^2' if minus else r'(a+b)^2=a^2+2ab+b^2'
    bb = abs(b)
    ax_t = f'({ax_})' if a != 1 else ax_
    steg = [li(f'Kvadreringsregeln: {m(regel)}',
               p(f'Här är {m("a=" + ax_)} och {m("b=" + str(bb))}.')),
            li(f'Sätt in och beräkna de tre termerna',
               mt(f'{par(A)}^2={ax_t}^2{"-" if minus else "+"}2\\cdot {ax_}\\cdot {bb}+{bb}^2={poly(e)}'))]
    return e, steg, f'{par(A)}^2'


def konjugat(a, b):
    """(ax+b)(ax-b) med konjugatregeln (b > 0)."""
    A1, A2 = lin(a, b), lin(a, -b)
    e = (a * x + b) * (a * x - b)
    ax_ = poly(a * x)
    ax_t = f'({ax_})' if a != 1 else ax_
    steg = [li(f'Konjugatregeln: {m(r"(a+b)(a-b)=a^2-b^2")}',
               p(f'Parenteserna har samma termer {m(ax_)} och {m(str(b))} men olika tecken.')),
            li('Kvadrera båda termerna och subtrahera',
               mt(f'{par(A1)}{par(A2)}={ax_t}^2-{b}^2={poly(e)}'))]
    return e, steg, f'{par(A1)}{par(A2)}'


def utveckla_del(e, steg, uttr, ledtrad, niva, extra_fel=()):
    svar = poly(e)
    alt = [svar, poly_omvand(e)]
    fel = [uttr] + list(extra_fel)
    return del_(f'{m(tex(uttr))}', steg, m(svar), ledtrad, svar, 'förenklat_polynom', niva, ratt_txt=alt, fel=fel)


def poly_omvand(e):
    """Samma polynom med termerna i stigande grad (ska också godtas)."""
    p_ = sp.Poly(sp.expand(e), x)
    termer = sorted(p_.terms(), key=lambda t: t[0][0])
    s = ''
    for (d,), c in termer:
        c = int(c)
        mag = abs(c)
        term = str(mag) if d == 0 else ('' if mag == 1 else str(mag)) + ('x' if d == 1 else f'x^{d}')
        s += ('-' if c < 0 else ('+' if s else '')) + term
    return s


def kombination(termer, ledtrad, niva):
    """Summa/differens av produkter: termer = [(tecken, faktor, typ, args)]."""
    steg, delresultat, uttr_delar, total = [], [], [], 0
    for tecken, k, typ, args in termer:
        e, st, u = {'produkt': produkt, 'kvadrat': kvadrat, 'konjugat': konjugat}[typ](*args)
        uttr_delar.append((tecken, k, u))
        for li_ in st:
            steg.append(li_)
        delresultat.append((tecken, k, e))
        total += (1 if tecken == '+' else -1) * k * e
    uttr = ''.join(('' if i == 0 and tg == '+' else tg) + (f'{k}' if k != 1 else '') + u
                   for i, (tg, k, u) in enumerate(uttr_delar))
    # Sätt ihop: multiplicera med faktorer och ta bort parenteser.
    led = ''.join(('' if i == 0 and tg == '+' else tg) + (f'{k}' if k != 1 else '') + par(poly(e))
                  for i, (tg, k, e) in enumerate(delresultat))
    utan = ''.join(fortecken(poly((1 if tg == '+' else -1) * k * e)) if i else poly((1 if tg == '+' else -1) * k * e)
                   for i, (tg, k, e) in enumerate(delresultat))
    minus = any(tg == '-' for tg, _, _ in delresultat)
    rub = ('Ta bort parenteserna – minustecknet framför en parentes byter tecken på alla termer i den'
           if minus else 'Multiplicera in faktorerna och ta bort parenteserna')
    steg.append(li(rub, mt(f'{led}={utan}')))
    steg.append(li('Samla termer av samma grad', mt(f'{utan}={poly(total)}')))
    return utveckla_del(total, steg, uttr, ledtrad, niva)


# ---------------------------------------------------------------- område 1: algebra_polynom
def algebra_polynom(nr):
    U = []
    F = 'Förenkla, utveckla och räkna med potenser'
    intros = ['<p>Utveckla och förenkla.</p>', '<p>Skriv utan parenteser och förenkla så långt som möjligt.</p>',
              '<p>Multiplicera ut parenteserna och förenkla.</p>', '<p>Förenkla uttrycken.</p>']
    serier = [
        # (produkt a,b,c,d), (kvadrat a,b), kombination
        ((2, 3, 1, -4), (3, -2), [('+', 1, 'kvadrat', (1, 3)), ('-', 1, 'produkt', (1, 2, 1, -5))]),
        ((3, -1, 2, 5), (2, 5), [('+', 2, 'kvadrat', (1, -2)), ('-', 1, 'konjugat', (1, 3))]),
        ((4, 1, -1, 3), (5, -1), [('+', 1, 'produkt', (2, 1, 1, 3)), ('-', 1, 'kvadrat', (1, 1))]),
        ((1, -6, 3, 2), (4, 3), [('+', 3, 'konjugat', (1, 2)), ('-', 1, 'kvadrat', (2, -1))]),
        ((2, -5, 2, 5), (1, -7), [('+', 1, 'kvadrat', (3, 1)), ('-', 2, 'produkt', (2, 1, 2, -1))]),
        ((5, 2, 1, -3), (6, -1), [('+', 1, 'konjugat', (2, 5)), ('-', 1, 'produkt', (2, -3, 2, 1))]),
        ((3, 4, 3, -2), (2, -9), [('+', 2, 'produkt', (1, -4, 1, 2)), ('-', 1, 'kvadrat', (1, -3))]),
        ((-2, 1, 3, 4), (3, 4), [('+', 1, 'kvadrat', (2, 3)), ('+', 1, 'kvadrat', (2, -3))]),
    ]
    for k, ((a, b, c, d), (ka, kb), komb) in enumerate(serier):
        e1, s1, u1 = produkt(a, b, c, d)
        e2, s2, u2 = kvadrat(ka, kb)
        regel2 = 'kvadreringsregeln' + (' med minustecken' if kb < 0 else '')
        delar = [
            utveckla_del(e1, s1, u1, f'Multiplicera varje term i {m(par(lin(a, b)))} med båda termerna i den andra parentesen. Samla sedan x-termerna.', 2),
            utveckla_del(e2, s2, u2, f'Använd {regel2}. Den mittersta termen är dubbla produkten av {m(poly(ka*x))} och {m(str(abs(kb)))}.', 2,
                         extra_fel=[poly(ka**2 * x**2 + kb**2)]),
            kombination(komb, 'Utveckla varje produkt för sig och sätt resultatet inom parentes innan du subtraherar eller adderar.', 3),
        ]
        U.append(uppgift(nr, 'algebra_polynom', F, intros[k % len(intros)], delar))
        nr += 1
    # Ensamma uppgifter på nivå 3: tre faktorer och kuber.
    ensamma = [
        ('(x+2)^3', (x + 2) ** 3, [li(f'Skriv kuben som en kvadrat gånger en faktor', mt(r'(x+2)^3=(x+2)^2(x+2)')),
                                   li(f'Kvadreringsregeln: {m("(a+b)^2=a^2+2ab+b^2")}', mt(r'(x+2)^2=x^2+4x+4')),
                                   li('Multiplicera med den sista faktorn', mt(r'(x^2+4x+4)(x+2)=x^3+2x^2+4x^2+8x+4x+8')),
                                   li('Samla termer av samma grad', mt('x^3+6x^2+12x+8'))],
         'Skriv kuben som en kvadrat gånger parentesen och utveckla i två steg.'),
        ('2x(x-3)^2', 2 * x * (x - 3) ** 2, [li(f'Kvadreringsregeln: {m("(a-b)^2=a^2-2ab+b^2")}', mt(r'(x-3)^2=x^2-6x+9')),
                                             li(f'Multiplicera varje term med {m("2x")}', mt(r'2x(x^2-6x+9)=2x^3-12x^2+18x'))],
         'Utveckla kvadraten först och multiplicera sedan med 2x.'),
        ('(x-1)(x+1)(x^2+1)', (x - 1) * (x + 1) * (x**2 + 1), [li(f'Konjugatregeln: {m("(a+b)(a-b)=a^2-b^2")}', mt(r'(x-1)(x+1)=x^2-1')),
                                                              li(f'Konjugatregeln igen, nu med {m("a=x^2")} och {m("b=1")}', mt(r'(x^2-1)(x^2+1)=x^4-1'))],
         'Multiplicera de två första parenteserna med konjugatregeln. Vad ser du då?'),
        ('(2x+1)(x^2-3x+4)', (2 * x + 1) * (x**2 - 3 * x + 4), [li('Multiplicera båda termerna i första parentesen med hela den andra parentesen', mt(r'2x(x^2-3x+4)+1\cdot(x^2-3x+4)=2x^3-6x^2+8x+x^2-3x+4')),
                                                              li('Samla termer av samma grad', mt(r'2x^3-5x^2+5x+4'))],
         'Multiplicera 2x med varje term i den andra parentesen, och därefter 1 med varje term.'),
        ('(x+4)^2-(x-4)^2', (x + 4) ** 2 - (x - 4) ** 2, [li(f'Kvadreringsreglerna för {m("(x+4)^2")} och {m("(x-4)^2")}', mt(r'(x^2+8x+16)-(x^2-8x+16)')),
                                                        li('Minustecknet byter tecken på alla termer i den andra parentesen', mt(r'x^2+8x+16-x^2+8x-16=16x'))],
         'Utveckla båda kvadraterna inom parentes. Vilka termer tar ut varandra?'),
        ('(3x-2)^2-(3x+2)(3x-2)', (3 * x - 2) ** 2 - (3 * x + 2) * (3 * x - 2),
         [li(f'Kvadreringsregeln: {m("(a-b)^2=a^2-2ab+b^2")}', mt(r'(3x-2)^2=9x^2-12x+4')),
          li(f'Konjugatregeln: {m("(a+b)(a-b)=a^2-b^2")}', mt(r'(3x+2)(3x-2)=9x^2-4')),
          li('Subtrahera hela den andra parentesen', mt(r'9x^2-12x+4-(9x^2-4)=9x^2-12x+4-9x^2+4=-12x+8'))],
         'Använd kvadreringsregeln på den första termen och konjugatregeln på den andra.'),
    ]
    for uttr, e, steg, led in ensamma:
        svar = poly(e)
        d = del_(f'<p>Utveckla och förenkla {m(uttr)}.</p>', steg, m(svar), led, svar, 'förenklat_polynom', 3,
                 ratt_txt=[svar, poly_omvand(e)], fel=[uttr])
        U.append(uppgift(nr, 'algebra_polynom', F, '', [d]))
        nr += 1
    return U, nr


# ---------------------------------------------------------------- område 2: polynom (värden, grad, koefficienter)
def varde_steg(e, a):
    """Steg för p(a) med insättning."""
    pp = sp.Poly(e, x)
    ins = ''
    for (d,), c in sorted(pp.terms(), key=lambda t: -t[0][0]):
        c = int(c)
        av = f'({tal_tex(a)})' if a < 0 or not float(a).is_integer() else tal_tex(a)
        mag = abs(c)
        if d == 0:
            term = str(mag)
        else:
            term = ('' if mag == 1 else f'{mag}\\cdot ') + (av if d == 1 else f'{av}^{d}')
        ins += ('-' if c < 0 else ('+' if ins else '')) + term
    v = e.subs(x, a)
    termvarden = ''
    for (d,), c in sorted(pp.terms(), key=lambda t: -t[0][0]):
        tv = sp.Rational(c) * sp.Rational(a) ** d
        termvarden += (tal_tex(tv) if not termvarden else fortecken(tal_tex(tv)))
    return v, ins, termvarden


def polynom_omrade(nr):
    U = []
    F = 'Polynombegrepp, grad och värden'
    polyn = [
        (2 * x**3 - 5 * x**2 + x - 4, [2, -1, 3], (2, -1)),
        (-x**3 + 4 * x**2 - 2 * x + 7, [1, -2, 3], (3, -2)),
        (3 * x**4 - x**2 + 5 * x - 2, [1, -1, 2], (2, 1)),
        (x**4 - 3 * x**3 + 2 * x - 6, [2, -1, 3], (1, 3)),
        (4 * x**3 + 2 * x**2 - 7 * x + 1, [-1, 2, -2], (2, -1)),
        (-2 * x**4 + x**3 + 6 * x**2 - 3, [1, -2, 2], (1, -1)),
    ]
    for k, (e, vals, (u, v)) in enumerate(polyn):
        intro = f'<p>Polynomet är {m("p(x)=" + poly(e))}.</p>'
        delar = []
        for j, a in enumerate(vals[:2]):
            val, ins, tv = varde_steg(e, a)
            steg = [li(f'Ersätt x med {m(tal_tex(a))} i varje term', mt(f'p({tal_tex(a)})={ins}')),
                    li('Beräkna potenserna först och addera sedan termerna', mt(f'p({tal_tex(a)})={tv}={tal_tex(val)}'))]
            led = (f'Sätt in {m(tal_tex(a))} med parentes, så att tecknet följer med i potenserna.' if a < 0
                   else f'Sätt in {m(tal_tex(a))} i varje term och beräkna potenserna först.')
            delar.append(del_(f'Beräkna {m(f"p({tal_tex(a)})")}.', steg, m(f'p({tal_tex(a)})={tal_tex(val)}'), led,
                              int(val), 'numeriskt', 2, ratt_txt=[tal(val).replace('−', '-'), f'p({a})={int(val)}'],
                              fel=[str(int(val) + 2)]))
        # c) kombination av värden
        pu, pv = e.subs(x, u), e.subs(x, v)
        res = pu - 2 * pv
        steg = [li(f'Beräkna {m(f"p({tal_tex(u)})")} och {m(f"p({tal_tex(v)})")} för sig',
                   mt(f'p({tal_tex(u)})={tal_tex(pu)},\\quad p({tal_tex(v)})={tal_tex(pv)}')),
                li('Sätt in värdena med parenteser', mt(f'p({tal_tex(u)})-2p({tal_tex(v)})={tal_tex(pu)}-2\\cdot({tal_tex(pv)})={tal_tex(res)}'))]
        delar.append(del_(f'Beräkna {m(f"p({tal_tex(u)})-2p({tal_tex(v)})")}.', steg, m(tal_tex(res)),
                          'Beräkna de två funktionsvärdena var för sig först. Sätt parentes kring ett negativt värde.',
                          int(res), 'numeriskt', 3, ratt_txt=[tal(res).replace('−', '-')],
                          fel=[str(int(v_)) for v_ in (pu + 2 * pv, pu - pv, pu + pv, -res) if v_ != res][:2]))
        U.append(uppgift(nr, 'polynom', F, intro, delar))
        nr += 1
    # Grad, koefficient och konstantterm efter utveckling.
    produkter = [
        ((2 * x - 1), (x**2 + 3 * x - 4)), ((x + 3), (2 * x**2 - x + 5)), ((3 * x + 2), (x**2 - 2 * x - 1)),
        ((x - 4), (x**3 + 2 * x - 3)), ((2 * x + 5), (2 * x**2 + x - 2)), ((x**2 - 3), (x**2 + 4 * x + 1)),
    ]
    for k, (f1, f2) in enumerate(produkter):
        e = sp.expand(f1 * f2)
        pp = sp.Poly(e, x)
        g = pp.degree()
        k2 = int(pp.coeff_monomial(x**2))
        k0 = int(pp.coeff_monomial(1))
        P = f'{par(poly(f1))}{par(poly(f2))}'
        intro = f'<p>Polynomet är {m("p(x)=" + P)}.</p>'
        hog1, hog2 = sp.Poly(f1, x).degree(), sp.Poly(f2, x).degree()
        delar = [
            del_('Vilken grad har polynomet?',
                 [li('Graden är den högsta exponenten efter utveckling',
                     p(f'Den högsta termen får man av de två högsta termerna: grad {hog1} gånger grad {hog2} ger grad {hog1}+{hog2}.'),
                     mt(f'{hog1}+{hog2}={g}'))],
                 f'Graden är {g}.', 'Vilka termer ger den högsta exponenten när parenteserna multipliceras?', g, 'numeriskt', 2,
                 ratt_txt=[str(g)], fel=[str(max(hog1, hog2))]),
            del_('Vilken är konstanttermen?',
                 [li('Konstanttermen är produkten av de två konstanttermerna', mt(f'{tal_tex(int(f1.subs(x, 0)))}\\cdot({tal_tex(int(f2.subs(x, 0)))})={tal_tex(k0)}')),
                  li(f'Kontroll: konstanttermen är {m("p(0)")}', p(f'När x = 0 försvinner alla x-termer, så p(0) = {tal(k0)}.'))],
                 f'Konstanttermen är {m(tal_tex(k0))}.', 'Vilka termer blir kvar om du sätter x = 0?', k0, 'numeriskt', 2,
                 ratt_txt=[str(k0)], fel=[str(-k0)] if k0 else ['1']),
            del_(f'Vilken koefficient har {m("x^2")}-termen?',
                 [li('Utveckla produkten', mt(f'{P}={poly(e)}')),
                  li(f'Läs av talet framför {m("x^2")}', p(f'Koefficienten är {tal(k2)}.'))],
                 f'Koefficienten är {m(tal_tex(k2))}.', 'Utveckla hela produkten och samla termerna av grad 2.', k2, 'numeriskt', 3,
                 ratt_txt=[str(k2)], fel=[str(k2 + 1)]),
        ]
        U.append(uppgift(nr, 'polynom', F, intro, delar, formaga=('begrepp', 'procedur')))
        nr += 1
    return U, nr


# ---------------------------------------------------------------- område 3: faktorisera_polynom
def faktor_del(uttr_tex, svar, steg, ledtrad, niva, fel_ex, alt):
    return del_(m(uttr_tex), steg, m(svar), ledtrad, svar, 'faktoriserat', niva, ratt_txt=alt, fel=fel_ex)


def faktorisera(nr):
    U = []
    F = 'Faktorisera polynom'
    serier = [
        # (gemensam faktor), (konjugat), (kombinerat), (via nollställen)
        dict(g=(6 * x**3 - 9 * x**2, '3x^2(2x-3)', '3x^2', '(2x-3)'),
             k=(4, 25), kb=(2, 18), z=(1, -1, -12)),
        dict(g=(10 * x**2 + 15 * x, '5x(2x+3)', '5x', '(2x+3)'),
             k=(9, 4), kb=(3, 12), z=(1, 2, -15)),
        dict(g=(8 * x**4 - 12 * x**3, '4x^3(2x-3)', '4x^3', '(2x-3)'),
             k=(16, 49), kb=(5, 20), z=(1, -3, -10)),
        dict(g=(14 * x**3 + 21 * x, '7x(2x^2+3)', '7x', '(2x^2+3)'),
             k=(25, 9), kb=(2, 50), z=(1, 5, 6)),
        dict(g=(12 * x**2 - 18 * x**3, '6x^2(2-3x)', '6x^2', '(2-3x)'),
             k=(1, 64), kb=(4, 36), z=(1, -8, 15)),
        dict(g=(9 * x**5 + 6 * x**3, '3x^3(3x^2+2)', '3x^3', '(3x^2+2)'),
             k=(36, 1), kb=(3, 27), z=(1, 1, -20)),
        dict(g=(20 * x**3 - 5 * x**2, '5x^2(4x-1)', '5x^2', '(4x-1)'),
             k=(49, 16), kb=(2, 8), z=(1, -2, -24)),
        dict(g=(15 * x**4 + 10 * x**2, '5x^2(3x^2+2)', '5x^2', '(3x^2+2)'),
             k=(4, 81), kb=(6, 6), z=(1, 7, 10)),
    ]
    intros = ['<p>Faktorisera så långt som möjligt.</p>', '<p>Skriv polynomen i faktorform.</p>',
              '<p>Faktorisera uttrycken.</p>', '<p>Skriv som en produkt av faktorer.</p>']
    for k, ser in enumerate(serier):
        delar = []
        # a) bryt ut gemensam faktor
        ge, gsvar, gf, grest = ser['g']
        steg = [li(f'Största gemensamma faktorn är {m(gf)}', p(f'Både koefficienterna och x-potenserna delas av {m(gf)}.')),
                li(f'Bryt ut {m(gf)}: dela varje term med {m(gf)}', mt(f'{poly(ge)}={gf}{grest}')),
                li('Kontroll: multiplicera in igen', mt(f'{gf}{grest}={poly(ge)}'))]
        delar.append(faktor_del(poly(ge), gsvar, steg, 'Vilken är den största faktorn som både talen och x-potenserna har gemensamt?', 2,
                                [poly(ge)], [gsvar, f'{grest}*{gf}']))
        # b) konjugat: a2 x^2 - b2
        a2, b2 = ser['k']
        ra, rb = int(sp.sqrt(a2)), int(sp.sqrt(b2))
        e = a2 * x**2 - b2
        A = poly(ra * x)
        svar = f'({A}+{rb})({A}-{rb})'
        At = f'({A})' if ra != 1 else A
        steg = [li(f'Konjugatregeln baklänges: {m("a^2-b^2=(a+b)(a-b)")}', p(f'Båda termerna är kvadrater: {m(poly(e).split("-")[0] + "=" + At + "^2")} och {m(f"{b2}={rb}^2")}.')),
                li('Skriv som produkt', mt(f'{poly(e)}={At}^2-{rb}^2={svar}'))]
        delar.append(faktor_del(poly(e), svar, steg, 'Är båda termerna kvadrater? Använd i så fall konjugatregeln baklänges.', 2,
                                [poly(e), f'({A}-{rb})^2'], [svar, f'({A}-{rb})({A}+{rb})']))
        # c) gemensam faktor + konjugat: kb=(c, d) -> c x^3 - d x  med d/c kvadrat
        c, dd = ser['kb']
        r = int(sp.sqrt(sp.Rational(dd, c)))
        assert r * r * c == dd
        e = c * x**3 - dd * x
        inner = poly(x**2 - r * r)
        svar = f'{c}x(x+{r})(x-{r})'
        steg = [li(f'Bryt ut den gemensamma faktorn {m(f"{c}x")}', mt(f'{poly(e)}={c}x({inner})')),
                li(f'Konjugatregeln: {m("a^2-b^2=(a+b)(a-b)")}', mt(f'{inner}=x^2-{r}^2=(x+{r})(x-{r})')),
                li('Sätt ihop faktorerna', mt(f'{poly(e)}={svar}'))]
        delar.append(faktor_del(poly(e), svar, steg, 'Bryt först ut den gemensamma faktorn. Kan det som blir kvar faktoriseras igen?', 3,
                                [poly(e), f'{c}x({inner})'], [svar, f'{c}x(x-{r})(x+{r})']))
        # d) andragradspolynom via nollställen (pq-formeln)
        if k % 2 == 0:
            a_, b_, c_ = ser['z']
            e = a_ * x**2 + b_ * x + c_
            r1, r2 = sorted(sp.solve(e, x))
            pq_p, pq_q = sp.Rational(b_, a_), sp.Rational(c_, a_)
            half = -pq_p / 2
            disk = half**2 - pq_q
            svar = f'(x{fortecken(tal_tex(-r1))})(x{fortecken(tal_tex(-r2))})'.replace('{,}', '.')
            steg = [li(f'Faktorsatsen: om {m("x=a")} är ett nollställe är {m("(x-a)")} en faktor',
                       p(f'Lös därför {m(poly(e) + "=0")}.')),
                    li(f'pq-formeln: {m(r"x=-\tfrac p2\pm\sqrt{\left(\tfrac p2\right)^2-q}")}',
                       p(f'Här är {m(f"p={tal_tex(pq_p)}")} och {m(f"q={tal_tex(pq_q)}")}.'),
                       mt(f'x={tal_tex(half)}\\pm\\sqrt{{{tal_tex(half**2)}{fortecken(tal_tex(-pq_q))}}}={tal_tex(half)}\\pm{tal_tex(sp.sqrt(disk))}')),
                    li(f'Nollställena {m(f"x={tal_tex(r1)}")} och {m(f"x={tal_tex(r2)}")} ger faktorerna', mt(f'{poly(e)}={svar}'))]
            delar.append(faktor_del(poly(e), svar, steg, 'Bestäm polynomets nollställen. Varje nollställe a ger faktorn (x − a).', 3,
                                    [poly(e), f'(x{fortecken(tal_tex(r1))})(x{fortecken(tal_tex(r2))})'],
                                    [svar, f'(x{fortecken(tal_tex(-r2))})(x{fortecken(tal_tex(-r1))})']))
        U.append(uppgift(nr, 'faktorisera_polynom', F, intros[k % len(intros)], delar))
        nr += 1
    return U, nr


# ---------------------------------------------------------------- område 4: polynomekvationer
def graf(e, rotter, beskrivning):
    """SVG av y = p(x) med nollställena markerade (grafisk lösning)."""
    import math
    W, H, ml, mr_, mt_, mb = 400, 250, 34, 14, 14, 30
    lo, hi = min(rotter) - 1.5, max(rotter) + 1.5
    lo, hi = math.floor(lo), math.ceil(hi)
    f = sp.lambdify(x, e)
    xs = [lo + (hi - lo) * i / 400 for i in range(401)]
    ys = [float(f(v)) for v in xs]
    # Skala efter kurvan mellan (och strax utanför) nollställena, så att extrempunkterna syns.
    inre = [abs(float(f(min(rotter) - 0.4 + (max(rotter) - min(rotter) + 0.8) * i / 200))) for i in range(201)]
    ymax = max(2.0, max(inre) * 1.25)
    steg_y = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    sy = next(v for v in steg_y if ymax / v <= 4)
    ymax = sy * math.ceil(ymax / sy)
    X = lambda v: ml + (v - lo) / (hi - lo) * (W - ml - mr_)
    Y = lambda v: mt_ + (ymax - v) / (2 * ymax) * (H - mt_ - mb)
    ink = '#24435e'
    out = [f'<line x1="{X(lo):.1f}" y1="{Y(0):.1f}" x2="{X(hi):.1f}" y2="{Y(0):.1f}" stroke="{ink}" stroke-width="1.5"/>']
    if lo < 0 < hi:
        out.append(f'<line x1="{X(0):.1f}" y1="{Y(ymax):.1f}" x2="{X(0):.1f}" y2="{Y(-ymax):.1f}" stroke="{ink}" stroke-width="1.5"/>')
    yaxel = X(0) if lo < 0 < hi else X(lo)
    for v in range(lo, hi + 1):
        out.append(f'<line x1="{X(v):.1f}" y1="{Y(0)-4:.1f}" x2="{X(v):.1f}" y2="{Y(0)+4:.1f}" stroke="{ink}"/>')
        if v != 0 and v not in rotter:
            out.append(f'<text x="{X(v):.1f}" y="{Y(0)+18:.1f}" font-size="13" text-anchor="middle" fill="{ink}">{tal(v)}</text>')
    for v in (sy, -sy):
        if abs(v) <= ymax:
            out.append(f'<line x1="{yaxel-4:.1f}" y1="{Y(v):.1f}" x2="{yaxel+4:.1f}" y2="{Y(v):.1f}" stroke="{ink}"/>')
            out.append(f'<text x="{yaxel-7:.1f}" y="{Y(v)+4:.1f}" font-size="13" text-anchor="end" fill="{ink}">{tal(v)}</text>')
    seg, segs = [], []
    for xv, yv in zip(xs, ys):
        if abs(yv) <= ymax * 1.02:
            seg.append(f'{X(xv):.1f},{Y(yv):.1f}')
        elif seg:
            segs.append(seg); seg = []
    if seg:
        segs.append(seg)
    for sg in segs:
        out.append(f'<polyline points="{" ".join(sg)}" fill="none" stroke="#096c9a" stroke-width="2.5"/>')
    for k, r in enumerate(sorted(rotter)):
        ty = Y(0) - 12 if k % 2 == 0 else Y(0) + 24
        out.append(f'<circle cx="{X(r):.1f}" cy="{Y(0):.1f}" r="5" fill="#b25c17" stroke="#fff" stroke-width="1.5"/>')
        out.append(f'<text x="{X(r):.1f}" y="{ty:.1f}" font-size="14" font-weight="bold" text-anchor="middle" fill="#b25c17" '
                   f'stroke="#fff" stroke-width="3" paint-order="stroke">{tal(r)}</text>')
    out.append(f'<text x="{W-mr_:.1f}" y="{Y(0)-6:.1f}" font-size="13" text-anchor="end" fill="{ink}">x</text>')
    return (f'<span class="fig"><svg viewBox="0 0 {W} {H}" width="100%" style="max-width:400px;height:auto" role="img" '
            f'aria-label="{beskrivning}" xmlns="http://www.w3.org/2000/svg">' + ''.join(out) + '</svg></span>')


def graf_steg(e, rotter):
    rot = ', '.join(tal(r) for r in sorted(rotter))
    return li('Grafisk kontroll: lösningarna är där grafen skär x-axeln',
              p(f'Grafen till {m("y=" + poly(e))} skär x-axeln där {m("x=" + ",\\ ".join(tal_tex(r) for r in sorted(rotter)))}.'),
              graf(e, rotter, f'Grafen till y = {poly(e)} skär x-axeln vid x = {rot}.'))


def ekv_del(e_vl, rotter, steg, ledtrad, niva, fraga_tex=None):
    rotter = sorted(rotter)
    assert sorted(sp.solve(sp.expand(e_vl), x)) == rotter, (e_vl, rotter)
    vals = [int(r) if float(r).is_integer() else float(r) for r in rotter]
    svar = ', '.join(m(f'x={tal_tex(r)}') for r in rotter)
    txt = ', '.join(tal(r).replace('−', '-') for r in rotter)
    fel = ', '.join(tal(r).replace('−', '-') for r in rotter[:-1]) if len(rotter) > 1 else str(vals[0] + 1)
    return del_(m((fraga_tex or poly(e_vl)) + '=0'), steg + [graf_steg(sp.expand(e_vl), rotter)], svar, ledtrad, vals, 'numeriskt', niva,
                ratt_txt=[], fel=[])


def polynomekvationer(nr):
    U = []
    F = 'Lösa polynomekvationer'
    intros = ['<p>Lös ekvationerna.</p>', '<p>Lös ekvationerna. Ange alla lösningar.</p>',
              '<p>Bestäm alla reella lösningar.</p>', '<p>Lös ekvationerna exakt.</p>']
    serier = [
        dict(np=(0, 3, -5), kon=9, pq=(1, -6), bi=(1, 2)),
        dict(np=(2, -1, 4), kon=16, pq=(2, -8), bi=(1, 3)),
        dict(np=(0, -2, 6), kon=4, pq=(-1, -12), bi=(2, 3)),
        dict(np=(1, 5, -3), kon=25, pq=(3, -10), bi=None),
        dict(np=(0, 4, -1), kon=1, pq=(-2, -15), bi=(1, 4)),
        dict(np=(3, -4, -2), kon=36, pq=(5, 6), bi=None),
        dict(np=(0, 1, -7), kon=49, pq=(-4, 3), bi=(2, 4)),
        dict(np=(-3, 2, 6), kon=64, pq=(1, -20), bi=None),
    ]
    for k, ser in enumerate(serier):
        delar = []
        # a) nollproduktmetoden: (x-r1)(x-r2)(x-r3)=0 skrivet med x som faktor om r1 = 0
        r = sorted(set(ser['np']))
        faktorer = ['x' if v == 0 else f'(x{fortecken(str(-v))})' for v in ser['np']]
        uttr = ''.join(faktorer)
        e = sp.Mul(*[(x - v) for v in ser['np']])
        steg = [li('Nollproduktmetoden: en produkt är noll när någon faktor är noll',
                   mt('\\begin{aligned}' + '\\\\'.join(f'&{("x" if v == 0 else "x" + fortecken(str(-v)))}=0\\;\\Rightarrow\\;x={v}'
                                                        for v in ser['np']) + '\\end{aligned}'))]
        delar.append(ekv_del(e, r, steg, 'Vänsterledet är redan en produkt. När blir en produkt lika med noll?', 2, fraga_tex=uttr))
        # b) x^3 - k x = 0
        kk = ser['kon']; rr = int(sp.sqrt(kk))
        e = x**3 - kk * x
        steg = [li('Bryt ut x', mt(f'x^3-{kk}x=x(x^2-{kk})=0')),
                li('Nollproduktmetoden', p(f'Antingen är {m("x=0")} eller {m(f"x^2-{kk}=0")}.'),
                   mt(f'x^2={kk}\\;\\Rightarrow\\;x=\\pm{rr}'))]
        delar.append(ekv_del(e, [-rr, 0, rr], steg, 'Bryt ut den gemensamma faktorn x. Glöm inte lösningen x = 0.', 2))
        # c) x^3 + b x^2 + c x = 0 via pq
        bb, cc = ser['pq']
        e = x**3 + bb * x**2 + cc * x
        kvad = x**2 + bb * x + cc
        r1, r2 = sorted(sp.solve(kvad, x))
        half = sp.Rational(-bb, 2); disk = half**2 - cc
        steg = [li('Bryt ut x', mt(f'{poly(e)}=x({poly(kvad)})=0')),
                li('Nollproduktmetoden', p(f'Antingen är {m("x=0")} eller {m(poly(kvad) + "=0")}.')),
                li(f'pq-formeln: {m(r"x=-\tfrac p2\pm\sqrt{\left(\tfrac p2\right)^2-q}")}',
                   p(f'Här är {m(f"p={bb}")} och {m(f"q={cc}")}.'),
                   mt(f'x={tal_tex(half)}\\pm\\sqrt{{{tal_tex(half**2)}{fortecken(tal_tex(-cc))}}}={tal_tex(half)}\\pm{tal_tex(sp.sqrt(disk))}'),
                   p(f'Det ger {m(f"x={tal_tex(r1)}")} och {m(f"x={tal_tex(r2)}")}.'))]
        delar.append(ekv_del(e, sorted([0, r1, r2]), steg, 'Bryt ut x. Den andragradsekvation som blir kvar kan lösas med pq-formeln.', 3))
        # d) bikvadratisk
        if ser['bi']:
            a_, b_ = ser['bi']
            s1, s2 = a_ * a_, b_ * b_
            e = x**4 - (s1 + s2) * x**2 + s1 * s2
            t = sp.Symbol('t')
            half = sp.Rational(s1 + s2, 2); disk = half**2 - s1 * s2
            steg = [li(f'Substitution: sätt {m("t=x^2")}', mt(f'{poly(e)}=0\\;\\Rightarrow\\;t^2-{s1+s2}t+{s1*s2}=0')),
                    li(f'pq-formeln: {m(r"t=-\tfrac p2\pm\sqrt{\left(\tfrac p2\right)^2-q}")}',
                       mt(f't={tal_tex(half)}\\pm\\sqrt{{{tal_tex(half**2)}-{s1*s2}}}={tal_tex(half)}\\pm{tal_tex(sp.sqrt(disk))}'),
                       p(f'Det ger {m(f"t={s1}")} och {m(f"t={s2}")}.')),
                    li(f'Gå tillbaka till x: {m("x^2=t")}',
                       mt(f'\\begin{{aligned}}&x^2={s1}\\;\\Rightarrow\\;x=\\pm{a_}\\\\&x^2={s2}\\;\\Rightarrow\\;x=\\pm{b_}\\end{{aligned}}'))]
            delar.append(ekv_del(e, sorted([-b_, -a_, a_, b_]), steg,
                                 'Ekvationen innehåller bara x⁴ och x². Ersätt x² med t och lös andragradsekvationen i t.', 3))
        U.append(uppgift(nr, 'polynomekvationer', F, intros[k % len(intros)], delar, mr=True, gg=True))
        nr += 1
    return U, nr


# ---------------------------------------------------------------- kontroll och skrivning
def till_sympy(t):
    """Elevtext som 3x^2(2x-3) eller (x+2)^2-(x-1)(x+1) till ett sympy-uttryck."""
    import re
    t = t.replace('\\cdot', '*').replace('−', '-').replace('^', '**').replace(' ', '')
    t = re.sub(r'(?<=[0-9x)])(?=[x(])', '*', t)
    return sp.sympify(t, locals={'x': x})


def fraga_uttryck(d, q):
    fraga = d.get('fraga') or q['t']
    return fraga.split('\\(')[1].split('\\)')[0]


def kontrollera(U):
    """Oberoende kontroll av varje del med sympy."""
    n = 0
    for q in U:
        delar = q.get('spelDelar') or [q]
        svar = q['rättSvar'] if q.get('spelDelar') else [q['rättSvar']]
        fmts = q['svarFormat'] if q.get('spelDelar') else [q['svarFormat']]
        for d, r, f in zip(delar, svar, fmts):
            if f in ('förenklat_polynom', 'faktoriserat'):
                uttr = till_sympy(fraga_uttryck(d, q))
                assert sp.expand(uttr - till_sympy(r)) == 0, (q['id'], d.get('etikett'), r)
                n += 1
                if f == 'faktoriserat':
                    # Svaret ska vara en produkt, inte en summa.
                    assert till_sympy(r).is_Mul or till_sympy(r).is_Pow, (q['id'], r)
    return n


def main():
    nr = FORSTA_ID
    U = []
    for bygg in (algebra_polynom, polynom_omrade, faktorisera, polynomekvationer):
        nya, nr = bygg(nr)
        U += nya
    print('sympy-kontrollerade delar', kontrollera(U))
    src = BANK.read_text(encoding='utf-8')
    bank = json.loads(src[src.index('['):src.rindex(']') + 1])
    befintliga = {q['id'] for q in bank}
    assert not befintliga & {q['id'] for q in U}, befintliga & {q['id'] for q in U}
    kort = sum(len(q.get('spelDelar') or [1]) for q in U)
    print('uppgifter', len(U), 'kort', kort, 'id', U[0]['id'], '–', U[-1]['id'])
    if '--varianter' in sys.argv:
        Path(sys.argv[sys.argv.index('--varianter') + 1]).write_text(json.dumps(VARIANTER, ensure_ascii=False, indent=1), encoding='utf-8')
    if '--skriv' in sys.argv:
        end = src.rindex(']')
        ny = src[:end].rstrip() + ',\n' + json.dumps(U, ensure_ascii=False, indent=2)[1:-1].strip('\n') + '\n' + src[end:]
        with open(BANK, 'w', encoding='utf-8', newline='') as f:
            f.write(ny)


if __name__ == '__main__':
    main()
