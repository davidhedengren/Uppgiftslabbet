"""Ma1 kapitel 1 (algebra): mängdträning 2026-11-06.

Användaren: "fortsätt leta efter områden och svårighetsgrader som saknar uppgifter". Kartläggningen visar att
algebraområdena i Ma1 kap 1 (undervisas v. 42–48 enligt Planering Ma1a 2627) har 25–48 kort på nivå 1–2 och
få kort på nivå 3. Samma upplägg som kapitel 0 (agent/MA1_KAP0_MANGDTRANING_2026-11-06.md): vanliga uppgifter,
1–4 delar med stigande svårighet a → d och en egen träningsnivå per del.

Talen är valda för hand. Svaren kontrolleras med sympy. Facit byggs steg för steg ur uttryckets struktur, och
varje rubrik visar just den uppgiftens tal och termer.
Logg: agent/MA1_KAP1_MANGDTRANING_2026-11-06.md

  python tools/bygg-ma1-kap1-mangdtraning-2026-11-06.py [--visa] [--skriv]
"""
import importlib.util
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy

HAR = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('kap0', HAR / 'bygg-ma1-kap0-mangdtraning-2026-11-06.py')
K0 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(K0)
li, mat, lista, tex_tal, sv_tal, som_json, huvudledtrad = K0.li, K0.mat, K0.lista, K0.tex_tal, K0.sv_tal, K0.som_json, K0.huvudledtrad

BANK = HAR.parent / 'uppgifterma1.js'
START_ID = 1623
F = Fraction


# ------------------------------------------------------------------ termer
# ('c', tal) konstant · ('m', koef, potens) koef·v^p · ('p', koef, potens, [termer]) koef·v^p·(…) · ('pp', [..], [..])
def dela_toppniva(s):
    """Delar ett led i termer på +/- utanför parenteser. Returnerar [(tecken, kropp)]."""
    delar, djup, start = [], 0, 0
    s = s.replace(' ', '')
    for i, ch in enumerate(s):
        if ch == '(':
            djup += 1
        elif ch == ')':
            djup -= 1
        elif ch in '+-' and djup == 0 and i > 0:
            delar.append(s[start:i]); start = i
    delar.append(s[start:])
    ut = []
    for d in delar:
        tecken = -1 if d.startswith('-') else 1
        ut.append((tecken, d.lstrip('+-')))
    return ut


def tolka(s, v):
    termer = []
    for tecken, k in dela_toppniva(s):
        V = re.escape(v)
        if (m := re.fullmatch(r'\((.+)\)\((.+)\)', k)):
            assert tecken == 1
            termer.append(('pp', tolka(m[1], v), tolka(m[2], v)))
        elif (m := re.fullmatch(rf'(\d*)({V}(?:\^(\d+))?)?\((.+)\)', k)):
            koef = F(int(m[1]) if m[1] else 1) * tecken
            p = (int(m[3]) if m[3] else 1) if m[2] else 0
            termer.append(('p', koef, p, tolka(m[4], v)))
        elif (m := re.fullmatch(rf'(\d*){V}(?:\^(\d+))?(?:/(\d+))?', k)):
            koef = F(int(m[1]) if m[1] else 1, int(m[3]) if m[3] else 1) * tecken
            termer.append(('m', koef, int(m[2]) if m[2] else 1))
        elif re.fullmatch(r'\d+(\.\d+)?', k):
            termer.append(('c', F(k) * tecken))
        else:
            raise ValueError(f'kan inte tolka termen {k!r} i {s!r}')
    return termer


def dtex(x):
    """Tal med ändlig decimalutveckling skrivs i decimalform."""
    x = F(x)
    n = x.denominator
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    if n == 1 and x.denominator != 1:
        from decimal import Decimal
        return tex_tal(Decimal(x.numerator) / Decimal(x.denominator))
    return tex_tal(x)


def mono(koef, p, v, forsta=True):
    """TeX för koef·v^p med tecken (utan + om forsta)."""
    tecken = '-' if koef < 0 else ('' if forsta else '+')
    a = abs(koef)
    if p == 0:
        return tecken + tex_tal(a)
    vp = v + (f'^{{{p}}}' if p > 1 else '')
    if a.denominator != 1:
        return tecken + f'\\frac{{{"" if a.numerator == 1 else a.numerator}{vp}}}{{{a.denominator}}}'
    return tecken + ('' if a == 1 else tex_tal(a)) + vp


def tex_term(t, v, forsta):
    if t[0] == 'c':
        return mono(t[1], 0, v, forsta)
    if t[0] == 'm':
        return mono(t[1], t[2], v, forsta)
    if t[0] == 'p':
        _, koef, p, inre = t
        tecken = '-' if koef < 0 else ('' if forsta else '+')
        a = abs(koef)
        fakt = ('' if a == 1 else tex_tal(a)) + (v + (f'^{{{p}}}' if p > 1 else '') if p else '')
        return f'{tecken}{fakt}({tex_led(inre, v)})'
    _, a, b = t
    return ('' if forsta else '+') + f'({tex_led(a, v)})({tex_led(b, v)})'


def tex_led(termer, v):
    return ''.join(tex_term(t, v, i == 0) for i, t in enumerate(termer)) or '0'


def poly(termer):
    """termer → {potens: koef}"""
    ut = {}
    def add(p, k):
        ut[p] = ut.get(p, 0) + k
    for t in termer:
        if t[0] == 'c':
            add(0, t[1])
        elif t[0] == 'm':
            add(t[2], t[1])
        elif t[0] == 'p':
            for p, k in poly(t[3]).items():
                add(p + t[2], k * t[1])
        else:
            pa, pb = poly(t[1]), poly(t[2])
            for p1, k1 in pa.items():
                for p2, k2 in pb.items():
                    add(p1 + p2, k1 * k2)
    return {p: k for p, k in ut.items() if k != 0}


def poly_termer(pd):
    ut = [('c', k) if p == 0 else ('m', k, p) for p, k in sorted(pd.items(), reverse=True) if k != 0]
    return ut or [('c', F(0))]


def poly_text(pd, v):
    """Svarssträng för förenklat_polynom, t.ex. x^2+3x-4."""
    s = ''
    for p, k in sorted(pd.items(), reverse=True):
        a = abs(k)
        assert a.denominator == 1, pd
        tecken = '-' if k < 0 else ('+' if s else '')
        if p == 0:
            s += tecken + str(a)
        else:
            s += tecken + ('' if a == 1 else str(a)) + v + (f'^{p}' if p > 1 else '')
    return s or '0'


def sp(termer, v):
    """sympy-uttryck för kontroll."""
    x = sympy.Symbol(v)
    return sum((sympy.Rational(k.numerator, k.denominator) * x ** p for p, k in poly(termer).items()), sympy.Integer(0))


# ------------------------------------------------------------------ steg: multiplicera in och samla termer
def expandera(termer, v):
    """Ett steg per parentes. Returnerar (nya termer, [li-steg])."""
    steg, ut = [], []
    for t in termer:
        if t[0] == 'p':
            _, koef, p, inre = t
            nya = [('c', k * koef) if q + p == 0 else ('m', k * koef, q + p)
                   for q, k in ((0, x[1]) if x[0] == 'c' else (x[2], x[1]) for x in inre)]
            fore = tex_term(t, v, True)
            efter = tex_led(nya, v)
            fakt = '-' if koef == -1 and p == 0 else ('+' if koef == 1 and p == 0 else mono(koef, p, v))
            if koef == -1 and p == 0:
                rub = f'Minustecknet framför parentesen byter tecken på varje term: \\({fore}={efter}\\)'
            elif koef == 1 and p == 0:
                rub = f'Plustecken framför parentesen: parentesen kan tas bort utan att tecknen ändras: \\({fore}={efter}\\)'
            else:
                rub = f'Multiplicera in \\({fakt}\\) i parentesen: \\({fore}={efter}\\)'
            steg.append(dict(typ='p', rub=rub, rad=f'{fore}={efter}', fakt=fakt))
            ut.extend(nya)
        elif t[0] == 'pp':
            _, a, b = t
            prod = []
            for x in a:
                for y in b:
                    prod.append((x, y))
            def fakt_tex(x):
                return mono(x[1], 0 if x[0] == 'c' else x[2], v)
            def ps(x):
                s = fakt_tex(x)
                return f'({s})' if s.startswith('-') else s
            rad1 = '+'.join(f'{fakt_tex(x)}\\cdot {ps(y)}' for x, y in prod).replace('+-', '-')
            nya = []
            for x, y in prod:
                px = 0 if x[0] == 'c' else x[2]; py = 0 if y[0] == 'c' else y[2]
                k = x[1] * y[1]
                nya.append(('c', k) if px + py == 0 else ('m', k, px + py))
            steg.append(dict(typ='pp', rub=f'Multiplicera varje term i \\(({tex_led(a, v)})\\) med varje term i \\(({tex_led(b, v)})\\)',
                             rad=f'({tex_led(a, v)})({tex_led(b, v)})=', rad1=f'={rad1}', rad2=f'={tex_led(nya, v)}'))   # tre rader, annars för brett på mobil
            ut.extend(nya)
        else:
            ut.append(t)
    return ut, steg


def expansionssteg(exp, fore, efter, v, helhet):
    """li-steg för parenteserna. helhet(efter) ger hela uttrycket/ekvationen efter steget."""
    if not exp:
        return []
    if len(exp) == 1:
        e = exp[0]
        if e['typ'] == 'pp':
            rader = [mat(e['rad']), mat(e['rad1']), mat(e['rad2'])]
            ensam = len(fore) == 1
            return [li(e['rub'], *rader, *([] if ensam else [mat(helhet(efter))]))]
        ensam = len(fore) == 1
        return [li(e['rub'], *([] if ensam else [mat(helhet(efter))]))]
    assert all(e['typ'] == 'p' for e in exp)
    def gor(e):
        inre = e['rad'].split('=')[0]
        if e['fakt'] == '-':
            return f'byt tecken i \\({inre[1:]}\\)'
        if e['fakt'] == '+':
            return f'ta bort plusparentesen \\({inre}\\)'
        return f'multiplicera in \\({e["fakt"]}\\)'
    delar = [gor(e) for e in exp]
    rub = 'Ta bort parenteserna: ' + (', '.join(delar[:-1]) + ' och ' + delar[-1])
    return [li(rub, *[mat(e['rad']) for e in exp], mat(helhet(efter)))]


def samla(termer, v):
    """Rubrik för att samla lika termer, eller None om inget finns att samla."""
    grupper = {}
    for t in termer:
        p = 0 if t[0] == 'c' else t[2]
        grupper.setdefault(p, []).append(t)
    delar = []
    for p in sorted(grupper, reverse=True):
        g = grupper[p]
        if len(g) < 2:
            continue
        summa = sum(t[1] for t in g)
        namn = 'talen' if p == 0 else (f'{v}-termerna' if p == 1 else f'\\({v}^{{{p}}}\\)-termerna')
        delar.append(f'{namn}: \\({tex_led(g, v)}={mono(summa, p, v) if summa != 0 else "0"}\\)')
    if not delar:
        return None
    return 'Samla ' + (delar[0] if len(delar) == 1 else ', '.join(delar[:-1]) + ' och ' + delar[-1])


# ------------------------------------------------------------------ deluppgiftstyper
def del_forenkla(uttr, L, v='x', fraga_ord='Förenkla'):
    termer = tolka(uttr, v)
    steg = []
    nu, exp = expandera(termer, v)
    steg += expansionssteg(exp, termer, nu, v, lambda vv: tex_led(vv, v))
    pd = poly(nu)
    rub = samla(nu, v)
    if rub:
        en_grupp = len({0 if t[0] == 'c' else t[2] for t in nu}) == 1
        rader = ([mat(tex_led(nu, v)), mat(f'={tex_led(poly_termer(pd), v)}')] if len(nu) >= 6     # långa rader delas för mobil
                 else [mat(f'{tex_led(nu, v)}={tex_led(poly_termer(pd), v)}')])
        steg.append(li(rub, *([] if en_grupp else rader)))
    assert sympy.expand(sp(termer, v) - sp(poly_termer(pd), v)) == 0
    svar = poly_text(pd, v)
    harp = any(t[0] in ('p', 'pp') for t in termer)
    if any(t[0] == 'pp' for t in termer):
        led = 'Varje term i den första parentesen ska multipliceras med varje term i den andra.'
    elif sum(t[0] == 'p' for t in termer) > 1:
        led = 'Ta bort en parentes i taget. Multiplicera in det som står framför parentesen i varje term inne i den.'
    elif any(t[0] == 'p' and t[1] == 1 and t[2] == 0 for t in termer):
        led = 'Det står ett plustecken framför parentesen. Vad händer då med tecknen inne i den?'
    elif any(t[0] == 'p' and t[1] == -1 and t[2] == 0 for t in termer):
        led = 'Vad händer med tecknen inne i parentesen när det står ett minustecken framför den?'
    elif harp:
        p = next(t for t in termer if t[0] == 'p')
        led = f'Multiplicera \\({mono(p[1], p[2], v)}\\) med varje term inne i parentesen.'
    elif 2 in poly(termer):
        led = f'\\({v}^2\\)-termer och {v}-termer är inte av samma slag. Samla varje sort för sig.'
    else:
        led = f'Vilka termer är av samma slag? Samla {v}-termerna för sig och talen för sig.'
    return dict(fraga=f'\\({tex_led(termer, v)}\\)', steg=steg, svar=svar, svarform='förenklat_polynom',
                svartex=tex_led(poly_termer(pd), v), ledtrad=f'<p>{led}</p>', L=L)


def led_lika(ve, he, v):
    return f'{tex_led(ve, v)}={tex_led(he, v)}'


def los_ekvation(ve, he, v, steg):
    """ve = he med bara c- och m-termer (potens 1). Lägger till steg och returnerar lösningen."""
    pv, ph = poly(ve), poly(he)
    a, b = pv.get(1, F(0)), pv.get(0, F(0))
    c, d = ph.get(1, F(0)), ph.get(0, F(0))
    # x-termerna samlas där koefficienten blir positiv
    vanster = a >= c if (a != 0 and c != 0) else a != 0
    if a != 0 and c != 0:
        if vanster:
            ord_ = f'Subtrahera \\({mono(c, 1, v)}\\) från båda leden' if c > 0 else f'Addera \\({mono(-c, 1, v)}\\) till båda leden'
            a, c = a - c, F(0)
        else:
            ord_ = f'Subtrahera \\({mono(a, 1, v)}\\) från båda leden' if a > 0 else f'Addera \\({mono(-a, 1, v)}\\) till båda leden'
            c, a = c - a, F(0)
        ve, he = poly_termer({1: a, 0: b}), poly_termer({1: c, 0: d})
        steg.append(li(ord_, mat(led_lika(ve, he, v))))
    k, kon, andra = (a, b, d) if vanster else (c, d, b)
    if kon != 0:
        ord_ = f'Subtrahera {sv_tal(kon)} från båda leden' if kon > 0 else f'Addera {sv_tal(-kon)} till båda leden'
        andra = andra - kon
        kon = F(0)
        ve, he = (poly_termer({1: k}), poly_termer({0: andra})) if vanster else (poly_termer({0: andra}), poly_termer({1: k}))
        steg.append(li(ord_, mat(led_lika(ve, he, v))))
    losning = andra / k
    if k != 1:
        if k == -1:
            ord_ = 'Multiplicera båda leden med −1 så att tecknet byts'
        elif k.denominator == 1:
            ord_ = f'Dividera båda leden med {sv_tal(k)}'
        elif k.numerator == 1:
            ord_ = f'Multiplicera båda leden med {k.denominator}'
        else:
            ord_ = f'Multiplicera båda leden med \\({tex_tal(1 / k)}\\)'
        rad = f'{v}={dtex(losning)}' if vanster else f'{dtex(losning)}={v}'
        steg.append(li(ord_, mat(rad)))
    return losning


def sub_tex(termer, v, varde):
    """Uttryckets TeX med värdet insatt."""
    vs = tex_tal(varde)
    vp = f'({vs})' if varde < 0 else vs
    def term(t, forsta):
        if t[0] == 'c':
            return mono(t[1], 0, v, forsta)
        if t[0] == 'm':
            koef, p = t[1], t[2]
            tecken = '-' if koef < 0 else ('' if forsta else '+')
            a = abs(koef)
            pot = (f'{vp}^{{{p}}}' if p > 1 else vp)
            if a.denominator != 1:
                return tecken + f'\\frac{{{"" if a.numerator == 1 else str(a.numerator) + chr(92) + "cdot "}{vp}}}{{{a.denominator}}}'
            return tecken + ('' if a == 1 else tex_tal(a) + '\\cdot ') + pot
        if t[0] == 'p':
            _, koef, p, inre = t
            tecken = '-' if koef < 0 else ('' if forsta else '+')
            a = abs(koef)
            fakt = ('' if a == 1 else tex_tal(a)) + ((('\\cdot ' if a != 1 else '') + vp) if p else '')
            return f'{tecken}{fakt}({"".join(term(x, i == 0) for i, x in enumerate(inre))})'
        raise ValueError(t)
    return ''.join(term(t, i == 0) for i, t in enumerate(termer))


def varde_av(termer, varde):
    return sum((k * F(varde) ** p for p, k in poly(termer).items()), F(0))


def del_ekvation(ekv, L, v='x', kontroll=True, forsteg=None):
    vs, hs = ekv.split('=')
    ve0, he0 = tolka(vs, v), tolka(hs, v)
    steg = list(forsteg or [])
    ve, se = expandera(ve0, v)
    he, sh = expandera(he0, v)
    exp = se + sh
    if exp:
        assert all(e['typ'] == 'p' for e in exp)
        if len(exp) == 1:
            steg.append(li(exp[0]['rub'], mat(led_lika(ve, he, v))))
        else:
            steg += expansionssteg(exp, ve0 + he0, None, v, lambda _: led_lika(ve, he, v))
    rv, rh = samla(ve, v), samla(he, v)
    if rv or rh:
        ve, he = poly_termer(poly(ve)), poly_termer(poly(he))
        rub = ' · '.join(x for x in [rv and 'Vänster led: ' + rv[0].lower() + rv[1:], rh and 'Höger led: ' + rh[0].lower() + rh[1:]] if x)
        steg.append(li(rub, mat(led_lika(ve, he, v))))
    losning = los_ekvation(ve, he, v, steg)
    x = sympy.Symbol(v)
    assert sympy.solve(sympy.Eq(sp(ve0, v), sp(he0, v)), x) == [sympy.Rational(losning.numerator, losning.denominator)]
    if kontroll:
        vl, hl = varde_av(ve0, losning), varde_av(he0, losning)
        assert vl == hl
        def kontrollrad(namn, termer, val):
            if not poly(termer).get(1) and all(t[0] == 'c' for t in termer):
                return mat(f'\\text{{{namn}}}={tex_tal(val)}')
            return mat(f'\\text{{{namn}}}={sub_tex(termer, v, losning)}={tex_tal(val)}')
        steg.append(li(f'Kontroll: sätt in \\({v}={tex_tal(losning)}\\) i ekvationen',
                       kontrollrad('VL', ve0, vl), kontrollrad('HL', he0, hl)))
    # ledtråd: första steget
    if sum(t[0] == 'p' for t in ve0 + he0) > 1:
        led = 'Börja med att ta bort parenteserna. Multiplicera in talet framför varje parentes, en i taget.'
    elif any(t[0] == 'p' for t in ve0 + he0):
        p = next(t for t in ve0 + he0 if t[0] == 'p')
        led = ('Börja med att ta bort parentesen. Tänk på minustecknet framför den.' if p[1] < 0
               else f'Börja med att multiplicera in \\({mono(p[1], p[2], v)}\\) i parentesen.')
    elif poly(ve0).get(1) and poly(he0).get(1):
        led = f'Det finns {v}-termer i båda leden. Samla dem i ett led genom att göra samma sak på båda sidor.'
    elif any(t[0] == 'm' and t[1].denominator != 1 for t in ve0 + he0):
        led = f'Få {v}-termen ensam först. Hur blir du sedan av med nämnaren?'
    elif any(poly(sida).get(0) and poly(sida).get(1) for sida in (ve0, he0)):
        led = f'Gör samma sak i båda leden så att {v}-termen blir ensam. Vad ska bort först?'
    else:
        led = f'Vilket tal är {v} multiplicerat med? Gör samma sak i båda leden.'
    return dict(fraga=f'\\({led_lika(ve0, he0, v)}\\)', steg=steg, svar=losning, svartex=f'{v}={dtex(losning)}',
                ledtrad=f'<p>{led}</p>', L=L)


def del_varde(uttr_tex, mall, varden, L):
    """Värdet av ett uttryck. mall är ett pythonuttryck med {x} osv. Räknas med kapitel 0-motorn."""
    sattin = {k: (f'({val})' if val < 0 else str(val)) for k, val in varden.items()}
    pyuttr = mall.format(**sattin)
    x = K0.del_uttryck(pyuttr, brakstreck='\\frac' in uttr_tex)
    givet = och_lista([f'\\({k}={tex_tal(F(val))}\\)' for k, val in varden.items()])
    givet_m = ',\\ '.join(f'{k}={tex_tal(F(val))}' for k, val in varden.items())
    K0.BRAKSTRECK[0] = '\\frac' in uttr_tex
    tr = K0.bygg(K0.ast.parse(pyuttr, mode='eval'), 'frac')
    K0.markera_forsta(tr)
    forsta = li(f'Sätt in {givet}', mat(K0.tex(tr)))
    neg = any(val < 0 for val in varden.values())
    rakna = ('Räkna ut täljaren och nämnaren för sig och dela sedan.' if '\\frac' in uttr_tex else x['ledtrad'][3:-4])
    led = ('Byt varje bokstav mot sitt tal. ' if len(varden) > 1 else 'Byt bokstaven mot talet. ') \
        + ('Håll koll på tecknet för det negativa talet. ' if neg and 'tecken' not in rakna else '') + rakna
    return dict(fraga=f'\\({uttr_tex}\\) då \\({givet_m}\\)', fragetext=f'Beräkna värdet av \\({uttr_tex}\\) då {givet}.',
                steg=[forsta] + x['steg'], svar=x['svar'], ledtrad=f'<p>{led}</p>', L=L)


def och_lista(delar):
    return delar[0] if len(delar) == 1 else ', '.join(delar[:-1]) + ' och ' + delar[-1]


def del_formel(formel_tex, givna, okand, sattin_tex, ekv, L, berakna=None):
    """Formel: sätt in givna värden. Är det okända inte ensamt löses ekvationen ekv (i variabeln okand)."""
    givet = och_lista([f'\\({k}={dtex(val)}\\)' for k, val in givna])
    fragetext = f'Beräkna \\({okand}\\) då {givet}.'
    if berakna:   # det sökta står ensamt: räkna som ett värde
        x = K0.del_uttryck(berakna, 'dec' if '.' in berakna else 'frac', brakstreck='\\frac' in sattin_tex)
        steg = [li(f'Sätt in {givet}', mat(f'{okand}={sattin_tex}'))] + x['steg']
        led = 'Sätt in värdena i formeln och räkna i rätt ordning.'
        return dict(fraga=fragetext, fragetext=fragetext, steg=steg, svar=x['svar'], ledtrad=f'<p>{led}</p>', L=L,
                    svartex=f'{okand}={tex_tal(x["svar"])}', intro=f'Formeln \\({formel_tex}\\) är given.')
    ekv_tex = led_lika(tolka(ekv.split('=')[0], okand), tolka(ekv.split('=')[1], okand), okand)
    forsteg = [li(f'Sätt in {givet}', mat(sattin_tex), *([] if ekv_tex == sattin_tex else [mat(ekv_tex)]))]
    x = del_ekvation(ekv, L, v=okand, kontroll=False, forsteg=forsteg)
    x['fraga'] = x['fragetext'] = fragetext
    x['intro'] = f'Formeln \\({formel_tex}\\) är given.'
    x['ledtrad'] = f'<p>Sätt in de kända värdena. Då får du en ekvation där \\({okand}\\) är det enda okända.</p>'
    return x


# ------------------------------------------------------------------ uppgifterna (talen valda för hand)
U = []


def uppg(omr, familj, instr, delar):
    """instr = (plural, singular) eller None när varje del har egen frågetext."""
    U.append((omr, familj, instr, delar))


EKV = ('Lös ekvationerna.', 'Lös ekvationen.')
FOR = ('Förenkla uttrycken.', 'Förenkla uttrycket.')
MUL = ('Multiplicera in och förenkla.', 'Multiplicera in och förenkla.')
Ek = lambda e, L, v='x': ('ekv', e, L, v)
Fo = lambda u, L, v='x': ('for', u, L, v)
Va = lambda tex, mall, varden, L: ('var', tex, mall, varden, L)
Fm = lambda *a: ('frm',) + a

# --- linjära ekvationer (Lösa enkla ekvationer)
LE = 'Lösa enkla ekvationer'
uppg('linjara_ekvationer', LE, EKV, [Ek('x+7=12', 1), Ek('4x=28', 1), Ek('3x-5=16', 2), Ek('8-2x=20', 3)])
uppg('linjara_ekvationer', LE, EKV, [Ek('x-9=-4', 1), Ek('5x+3=-12', 2)])
uppg('linjara_ekvationer', LE, EKV, [Ek('6x-7=29', 2)])
uppg('linjara_ekvationer', LE, EKV, [Ek('x/3=5', 1), Ek('x/4+3=7', 2), Ek('2x/5-1=7', 3)])
uppg('linjara_ekvationer', LE, EKV, [Ek('15=3x', 1), Ek('22=4+6x', 2), Ek('-14=10-3x', 3)])
uppg('linjara_ekvationer', LE, EKV, [Ek('7x=-35', 1), Ek('-2x+9=1', 2), Ek('x/6-4=-1', 2), Ek('11-3x/4=2', 4)])
uppg('linjara_ekvationer', LE, EKV, [Ek('9+x=3', 1)])
uppg('linjara_ekvationer', LE, EKV, [Ek('2t+13=31', 2, 't'), Ek('40-5t=15', 2, 't')])
# --- variabeltermer i båda leden
VB = 'Variabeltermer i båda leden'
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('5x=2x+12', 1), Ek('7x-4=3x+16', 2), Ek('2x+9=6x-11', 2), Ek('3-4x=13-9x', 3)])
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('4x+5=x+20', 2)])
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('6x=4x+10', 1), Ek('8x-3=5x+9', 2), Ek('x+14=7-6x', 3)])
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('10x-7=4x+5', 2), Ek('12-x=2x-9', 2)])
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('9a+2=5a+18', 2, 'a'), Ek('3a-8=7a+12', 3, 'a')])
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('5x+3-2x=x+15', 3), Ek('4x-7+x=2x+5+x', 3)])
uppg('ekv_flera_variabeltermer', VB, EKV, [Ek('2x-1=5x-16', 2)])
# --- ekvationer med parenteser
EP = 'Ekvationer med parenteser'
uppg('ekv_parenteser', EP, EKV, [Ek('2(x+3)=14', 1), Ek('3(x-4)=x+2', 2), Ek('5(2x-1)=3(x+3)', 3), Ek('4(x+2)-3(x-1)=17', 3)])
uppg('ekv_parenteser', EP, EKV, [Ek('6(x-2)=18', 1), Ek('2(3x+1)=4x+12', 2)])
uppg('ekv_parenteser', EP, EKV, [Ek('7(x+1)=5(x+3)', 2)])
uppg('ekv_parenteser', EP, EKV, [Ek('3(2x-5)=x+10', 2), Ek('2(x+6)=5(x-3)', 3), Ek('6(x-1)-2(x+4)=10', 3)])
MP = 'Minustecken framför parentes'
uppg('ekv_parenteser', MP, EKV, [Ek('20-(x+5)=9', 2), Ek('3x-(x-4)=16', 2), Ek('5-(2x-7)=x', 3)])
uppg('ekv_parenteser', MP, EKV, [Ek('12-(3x+3)=0', 2)])
uppg('ekv_parenteser', MP, EKV, [Ek('4x-2(x-5)=20', 2), Ek('10-3(x+2)=x-8', 3)])
# --- förenkla uttryck
FU = 'Förenkla uttryck'
uppg('forenkla_uttryck', FU, FOR, [Fo('3x+5x', 1), Fo('7x+4-2x', 1), Fo('6a+3-2a-8', 2, 'a'), Fo('5x-9+x-3x+4', 2)])
uppg('forenkla_uttryck', FU, FOR, [Fo('8y-3+2y+10', 1, 'y'), Fo('4x-7-6x+2', 2)])
uppg('forenkla_uttryck', FU, FOR, [Fo('2x^2+3x+x^2-5x', 3)])
uppg('forenkla_uttryck', FU, FOR, [Fo('9-4x+2x-1', 1), Fo('x+x+x-4', 2), Fo('3x^2-x+5-x^2+4x-2', 3)])
UP = 'Uttryck med parenteser'
uppg('forenkla_uttryck', UP, FOR, [Fo('5+(2x-3)', 1), Fo('8x-(3x+2)', 2), Fo('10-(4-x)', 2), Fo('2x-(5-3x)+7', 3)])
uppg('forenkla_uttryck', UP, FOR, [Fo('3(x+2)+2(x-1)', 2), Fo('4(2x-1)-3(x+2)', 3)])
uppg('forenkla_uttryck', UP, FOR, [Fo('6x-(x-4)', 2)])
uppg('forenkla_uttryck', UP, FOR, [Fo('2(a+5)+3a', 2, 'a'), Fo('7-2(a-3)', 3, 'a'), Fo('5(a-2)-(3a+4)', 3, 'a')])
# --- multiplicera uttryck
MI = 'Multiplicera in i en parentes'
uppg('multiplicera_uttryck', MI, MUL, [Fo('3(x+4)', 1), Fo('5(2x-3)', 1), Fo('-2(4x-1)', 2), Fo('x(x+6)', 3)])
uppg('multiplicera_uttryck', MI, MUL, [Fo('6(x-5)', 1), Fo('-(3x+7)', 2)])
uppg('multiplicera_uttryck', MI, MUL, [Fo('-4(2-3x)', 2)])
uppg('multiplicera_uttryck', MI, MUL, [Fo('2x(x-3)', 2), Fo('3x(2x+5)', 3), Fo('x(4-x)+2x', 3)])
uppg('multiplicera_uttryck', MI, MUL, [Fo('7(a+2)', 1, 'a'), Fo('-3(2a-5)', 2, 'a')])
MT = 'Multiplicera två parenteser'
uppg('multiplicera_uttryck', MT, MUL, [Fo('(x+2)(x+3)', 3), Fo('(x+5)(x-1)', 3), Fo('(x-4)(x-2)', 3), Fo('(2x+1)(x+3)', 4)])
uppg('multiplicera_uttryck', MT, MUL, [Fo('(x+4)(x+1)', 3)])
uppg('multiplicera_uttryck', MT, MUL, [Fo('(x-3)(x+6)', 3), Fo('(3x-2)(x-1)', 4)])
# --- värdet av ett uttryck
VU = 'Värdet av ett uttryck'
uppg('algebraiska_uttryck', VU, None, [Va('3x+5', '3*{x}+5', {'x': 4}, 1), Va('20-2x', '20-2*{x}', {'x': 7}, 1),
                                        Va('4x-9', '4*{x}-9', {'x': -2}, 2), Va('x^2+3x', '{x}**2+3*{x}', {'x': -5}, 3)])
uppg('algebraiska_uttryck', VU, None, [Va('6a-a', '6*{a}-{a}', {'a': 3}, 1), Va('5-3a', '5-3*{a}', {'a': -4}, 2)])
uppg('algebraiska_uttryck', VU, None, [Va('2x^2', '2*{x}**2', {'x': 3}, 2)])
uppg('algebraiska_uttryck', VU, None, [Va('2a+3b', '2*{a}+3*{b}', {'a': 5, 'b': 2}, 1), Va('4a-b', '4*{a}-{b}', {'a': 3, 'b': -6}, 2),
                                        Va('ab-2b', '{a}*{b}-2*{b}', {'a': -3, 'b': 4}, 3)])
uppg('algebraiska_uttryck', VU, None, [Va('\\frac{x+6}{3}', '({x}+6)/3', {'x': 9}, 2), Va('\\frac{2x-4}{x}', '(2*{x}-4)/{x}', {'x': -2}, 3)])
uppg('algebraiska_uttryck', VU, None, [Va('3(x-2)', '3*({x}-2)', {'x': 10}, 1), Va('-x^2+4', '-{x}**2+4', {'x': 3}, 3)])
uppg('algebraiska_uttryck', VU, None, [Va('x^2-2x+1', '{x}**2-2*{x}+1', {'x': -3}, 3)])
# --- formler
BF = 'Beräkningar med formler'
uppg('formler', BF, None, [Fm('P=2l+2b', [('l', 7), ('b', 4)], 'P', '2\\cdot 7+2\\cdot 4', None, 1, '2*7+2*4'),
                            Fm('P=2l+2b', [('P', 30), ('l', 9)], 'b', '30=2\\cdot 9+2b', '30=18+2b', 2),
                            Fm('P=2l+2b', [('P', 26), ('b', 5.5)], 'l', '26=2l+2\\cdot 5{,}5', '26=2l+11', 3)])
uppg('formler', BF, None, [Fm('A=\\frac{bh}{2}', [('b', 8), ('h', 5)], 'A', '\\frac{8\\cdot 5}{2}', None, 1, '8*5/2'),
                            Fm('A=\\frac{bh}{2}', [('A', 36), ('b', 9)], 'h', '36=\\frac{9h}{2}', '36=9h/2', 3)])
uppg('formler', BF, None, [Fm('s=vt', [('v', 80), ('t', 3)], 's', '80\\cdot 3', None, 1, '80*3'),
                            Fm('s=vt', [('s', 150), ('t', 2)], 'v', '150=v\\cdot 2', '150=2v', 2),
                            Fm('s=vt', [('s', 210), ('v', 70)], 't', '210=70t', '210=70t', 2)])
uppg('formler', BF, None, [Fm('K=45+12n', [('n', 6)], 'K', '45+12\\cdot 6', None, 1, '45+12*6'),
                            Fm('K=45+12n', [('K', 153)], 'n', '153=45+12n', '153=45+12n', 2)])
uppg('formler', BF, None, [Fm('F=1{,}8C+32', [('C', 25)], 'F', '1{,}8\\cdot 25+32', None, 2, '1.8*25+32')])
uppg('formler', BF, None, [Fm('y=3x-7', [('y', 20)], 'x', '20=3x-7', '20=3x-7', 2)])
uppg('formler', BF, None, [Fm('V=lbh', [('l', 6), ('b', 4), ('h', 3)], 'V', '6\\cdot 4\\cdot 3', None, 1, '6*4*3'),
                            Fm('V=lbh', [('V', 120), ('l', 5), ('b', 4)], 'h', '120=5\\cdot 4\\cdot h', '120=20h', 2),
                            Fm('V=lbh', [('V', 90), ('l', 6), ('h', 2.5)], 'b', '90=6\\cdot b\\cdot 2{,}5', '90=15b', 3)])


# ------------------------------------------------------------------ bygg
def bygg_del(d):
    typ = d[0]
    if typ == 'ekv':
        _, e, L, v = d
        return dict(del_ekvation(e, L, v), typ=typ)
    if typ == 'for':
        _, u, L, v = d
        return dict(del_forenkla(u, L, v), typ=typ)
    if typ == 'var':
        _, tex, mall, varden, L = d
        return dict(del_varde(tex, mall, varden, L), typ=typ)
    if typ == 'frm':
        _, ftex, givna, okand, sattin, ekv, L, *rest = d
        from decimal import Decimal
        givna = [(k, Decimal(str(val))) for k, val in givna]
        return dict(del_formel(ftex, givna, okand, sattin, ekv, L, rest[0] if rest else None), typ=typ)
    raise ValueError(typ)


def svar_falt(x):
    v = x['svar']
    if x.get('svarform') == 'förenklat_polynom':
        return v, 'förenklat_polynom'
    v = F(v)
    assert v.denominator in (1, 2, 4, 5, 10), v   # svar i decimalform utan avrundning
    return (int(v) if v.denominator == 1 else float(v)), 'numeriskt'


def svar_html(x):
    if x.get('svartex'):
        return f'\\({x["svartex"]}\\)'
    return f'\\({tex_tal(F(x["svar"]))}\\)'


def bygg_uppgifter():
    nya = []
    for nr, (omr, familj, instr, delar) in enumerate(U, START_ID):
        dd = [bygg_del(d) for d in delar]
        intro = dd[0].get('intro')
        if intro:
            assert all(x.get('intro') == intro for x in dd)
            instr = None
        rs, fm = zip(*[svar_falt(x) for x in dd])
        n = len(dd)
        etik = 'abcd'
        if n == 1:
            x = dd[0]
            text = x.get('fragetext') or f'{instr[1][:-1]} {x["fraga"]}.'
            t = (f'<p>{intro}</p>' if intro else '') + f'<p>{text}</p>'
            s = lista(x['steg'], svar_html(x))
            u = dict(svarstyp='uttryck' if fm[0] == 'förenklat_polynom' else 'numeriskt', rättSvar=rs[0], tolerans=1e-9,
                     svarFormat=fm[0], ledtrad=x['ledtrad'], traningsniva=x['L'], arbetsinsats=1)
        else:
            q = [x.get('fragetext') if instr is None else x['fraga'] for x in dd]
            t = ((f'<p>{instr[0]}</p>' if instr else f'<p>{intro}</p>' if intro else '') + '<div class="deluppgifter" style="display:grid;gap:0.85rem;margin:0.8rem 0;">'
                 + ''.join(f'<div>{etik[i]}) {qq}</div>' for i, qq in enumerate(q)) + '</div>')
            s = '<div class="facit-v2 facit-stegvis">' + ''.join(
                f'<p><strong>{etik[i]})</strong></p>' + lista(x['steg'], svar_html(x)) for i, x in enumerate(dd)) + '</div>'
            spel = [dict(etikett=etik[i], t=(f'<p>{instr[1]}</p><div class="spel-en-del">{x["fraga"]}</div>' if instr
                                              else (f'<p>{intro}</p>' if intro else '') + f'<p>{x["fragetext"]}</p>'),
                         s=lista(x['steg'], svar_html(x)), ledtrad=x['ledtrad'], niva='E', poang='1/0/0', traningsniva=x['L'])
                    for i, x in enumerate(dd)]
            u = dict(svarstyp='flera_delar', svarsstruktur='ordnad', rättSvar=list(rs), tolerans=1e-9, svarFormat=list(fm),
                     spelDelning='deluppgifter', spelDelar=spel, ledtrad=huvudledtrad(dd),
                     traningsniva=max(x['L'] for x in dd), arbetsinsats=2)
        bas = dict(id=f'1.{nr}', kap=1, omr=omr, kurs=['1a', '1b', '1c'], niva='E', poang=f'{n}/0/0', t=t, s=s, familj=familj,
                   geogebra=False, miniräknare=False, självrättning=True, formaga=['procedur'], spel=True)
        bas.update(u)
        nya.append(bas)
    return nya


def main():
    src = open(BANK, encoding='utf-8', newline='').read()
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    finns = {u['id'] for u in data}
    nya = bygg_uppgifter()
    for u in nya:
        assert u['id'] not in finns or '--skriv' not in sys.argv, u['id']
    from collections import Counter
    print(len(nya), 'uppgifter,', sum(len(u.get('spelDelar') or [0]) for u in nya), 'delar')
    print('delar per uppgift', sorted(Counter(len(u.get('spelDelar') or [1]) for u in nya).items()))
    print('per område', sorted(Counter(u['omr'] for u in nya).items()))
    if '--visa' in sys.argv:
        for u in nya:
            print(u['id'], u['omr'], json.dumps(u['rättSvar'], ensure_ascii=False), re.sub('<[^>]+>', ' ', u['t'])[:150])
    if '--skriv' in sys.argv:
        # efter sista uppgiften i filen (kapitel 1-ID:n sorteras inte i filen)
        nl = '\r\n' if '\r\n' in src else '\n'
        slut = src.rindex('}') + 1
        ny_src = src[:slut] + ''.join(',' + nl + '  ' + som_json(u, nl) for u in nya) + src[slut:]
        json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        open(BANK, 'w', encoding='utf-8', newline='').write(ny_src)
        print('skrivet')
    return nya


if __name__ == '__main__':
    main()
