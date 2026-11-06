"""Ma1 kapitel 1: mängdträning i att bryta ut största gemensamma faktor (2026-11-06).

Användaren: "Kanske ett nytt svarsformat eller liknande? för det är ju viktigt att de kan bryta ut största
möjliga faktor". Kunskapsgymmet har därför fått formatet "största_faktor" (index.html, storstaFaktorRatt).
Det godtar svaret om det är algebraiskt lika med facit och parentesen saknar gemensam faktor, både talfaktor
och variabel. 3x(2x+3) godtas alltså, men inte 3(2x²+3x), x(6x+9) eller den oförändrade frågan.

Samma upplägg som tools/bygg-ma1-kap1-mangdtraning-2026-11-06.py (vars uppgiftsbyggare återanvänds):
1–4 delar, a) är enklast och varje del har en egen träningsnivå. Svar och facit räknas med sympy.
Logg: agent/MA1_FAKTORISERING_2026-11-06.md

  python tools/bygg-ma1-faktorisering-2026-11-06.py [--visa] [--skriv]
"""
import importlib.util
import io
import contextlib
import json
import re
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

import sympy

HAR = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('kap1', HAR / 'bygg-ma1-kap1-mangdtraning-2026-11-06.py')
K1 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(K1)
li, mat, sv_tal = K1.li, K1.mat, K1.sv_tal
START_ID = 1685


# ------------------------------------------------------------------ monom med flera variabler
def tolka_monom(s):
    """'-12x^2y' → (-12, {'x': 2, 'y': 1})"""
    m = re.fullmatch(r'([+-]?)(\d*)((?:[a-z](?:\^\d+)?)*)', s)
    assert m and (m[2] or m[3]), s
    k = int(m[2] or 1) * (-1 if m[1] == '-' else 1)
    exp = {}
    for v, p in re.findall(r'([a-z])(?:\^(\d+))?', m[3]):
        exp[v] = exp.get(v, 0) + int(p or 1)
    return k, exp


def tolka_polynom(s):
    return [tolka_monom(t) for t in re.findall(r'[+-]?[^+-]+', s.replace(' ', ''))]


def mon_tex(k, exp, forsta=True, plain=False):
    """TeX (eller ren text för rättSvar) för k·x^a·y^b."""
    tecken = '-' if k < 0 else ('' if forsta else '+')
    a = abs(k)
    vars_ = ''.join(v + ((f'^{p}' if plain else f'^{{{p}}}') if p > 1 else '') for v, p in sorted(exp.items()) if p)
    return tecken + ('' if a == 1 and vars_ else str(a)) + vars_


def pol_tex(termer, plain=False):
    return ''.join(mon_tex(k, e, i == 0, plain) for i, (k, e) in enumerate(termer))


def sp_monom(k, exp):
    r = sympy.Integer(k)
    for v, p in exp.items():
        r *= sympy.Symbol(v) ** p
    return r


# ------------------------------------------------------------------ deluppgift: bryt ut största faktor
def del_bryt_ut(uttr, L, negativ=False):
    termer = tolka_polynom(uttr)
    g = 0
    for k, _ in termer:
        g = gcd(g, abs(k))
    if negativ:
        g = -g
    vars_ = sorted({v for _, e in termer for v in e})
    fexp = {v: min(e.get(v, 0) for _, e in termer) for v in vars_}
    fexp = {v: p for v, p in fexp.items() if p}
    faktor = (g, fexp)
    inre = [(k // g, {v: e.get(v, 0) - fexp.get(v, 0) for v in vars_}) for k, e in termer]
    M = mon_tex(*faktor)
    svar_tex = f'{M}({pol_tex(inre)})'
    svar_plain = f'{mon_tex(*faktor, plain=True)}({pol_tex(inre, plain=True)})'
    # kontroll med sympy: produkten är frågan, och parentesen har ingen gemensam faktor kvar
    P = sum((sp_monom(k, e) for k, e in termer), sympy.Integer(0))
    I = sum((sp_monom(k, e) for k, e in inre), sympy.Integer(0))
    assert sympy.expand(sp_monom(*faktor) * I - P) == 0
    innehall, primitiv = sympy.Poly(I, *[sympy.Symbol(v) for v in vars_]).terms_gcd()
    assert all(p == 0 for p in innehall) and abs(sympy.Poly(I, *[sympy.Symbol(v) for v in vars_]).content()) == 1, uttr
    assert abs(g) > 1 or fexp, uttr

    steg = []
    tal = [abs(k) for k, _ in termer]
    talrad = '\\qquad '.join(f'{t}={abs(g)}\\cdot {t // abs(g)}' for t in tal) if abs(g) > 1 else None
    if abs(g) > 1:
        steg.append(li(f'Största gemensamma faktorn till talen {K1.och_lista([str(t) for t in tal])} är {abs(g)}',
                       *([mat(talrad)] if len(tal) <= 2 else [mat(f'{t}={abs(g)}\\cdot {t // abs(g)}') for t in tal])))
    else:
        steg.append(li(f'Talen {K1.och_lista([str(t) for t in tal])} har ingen gemensam faktor större än 1'))
    if fexp:
        vt = K1.och_lista([f'\\({mon_tex(1, {v: p})}\\)' for v, p in fexp.items()])
        steg.append(li(f'Alla termer innehåller {vt}. Den lägsta potensen som finns i alla termer bryts ut'))
    if negativ:
        steg.append(li(f'Alla termer är negativa. Bryt ut \\({M}\\), så att termerna i parentesen blir positiva'))
    steg.append(li(f'Dividera varje term med \\({M}\\)',
                   *[mat(f'\\frac{{{mon_tex(k, e)}}}{{{M}}}={mon_tex(ki, ei)}') for (k, e), (ki, ei) in zip(termer, inre)]))
    steg.append(li(f'Skriv uttrycket som \\({M}\\) gånger parentesen', mat(f'{pol_tex(termer)}={svar_tex}')))
    steg.append(li(f'Kontroll: multiplicera in \\({M}\\). Termerna i parentesen har ingen gemensam faktor kvar, så det finns inget mer att bryta ut',
                   mat(f'{svar_tex}={pol_tex(termer)}')))
    alla = f'både {tal[0]} och {tal[1]} är' if len(tal) == 2 else f'{K1.och_lista([str(t) for t in tal])} alla är'
    tal_led = f'Vilket är det största tal som {alla} delbara med?' if abs(g) > 1 else ''
    var_led = ('Finns samma bokstav i alla termer? Bryt i så fall ut den lägsta potensen av den.' if fexp else
               'Finns det någon bokstav som står i alla termer?')
    led = (tal_led + ' ' + var_led).strip()
    return dict(fraga=f'\\({pol_tex(termer)}\\)',
                fragetext=f'Faktorisera \\({pol_tex(termer)}\\) genom att bryta ut största möjliga faktor.', steg=steg, svar=svar_plain, svarform='största_faktor', svartex=svar_tex,
                ledtrad=f'<p>{led}</p>', L=L, typ='fak')


# ------------------------------------------------------------------ uppgifterna (talen valda för hand)
U = []
BRY = ('Faktorisera uttrycken genom att bryta ut största möjliga faktor.', 'Faktorisera genom att bryta ut största möjliga faktor.')
SG = 'Bryt ut största gemensamma faktor'
FV = 'Faktorisera uttryck med potenser och flera variabler'
Fk = lambda u, L, neg=False: ('fak', u, L, neg)
uppg = lambda familj, delar: U.append(('faktorisering', familj, BRY, delar))

uppg(SG, [Fk('5x+15', 1), Fk('6x+9', 2), Fk('8x^2-12x', 3), Fk('15x^3+10x^2', 3)])
uppg(SG, [Fk('4x-12', 1), Fk('10x-15', 2)])
uppg(SG, [Fk('12x+18', 2)])
uppg(SG, [Fk('7x+14', 1), Fk('x^2+5x', 2), Fk('6x^2+9x', 3)])
uppg(SG, [Fk('9x-6', 1), Fk('12-8x', 2), Fk('14x^2-21x', 3), Fk('4x^3-6x^2+2x', 4)])
uppg(SG, [Fk('3x^2-x', 2)])
uppg(SG, [Fk('20x+30', 2), Fk('-4x-8', 3, True)])
uppg(SG, [Fk('16x^2+24x', 3)])
uppg(SG, [Fk('2x+10', 1), Fk('x^3-4x^2', 2), Fk('18x^2-12x+6', 3)])
uppg(FV, [Fk('6ab+9a', 2), Fk('4xy-8x^2y', 3), Fk('10a^2b+15ab^2', 3), Fk('12x^2y^3-18xy^2', 4)])
uppg(FV, [Fk('5ab+10b', 2), Fk('3x^2y+6xy', 3)])
uppg(FV, [Fk('8a^2-4ab', 3)])
uppg(FV, [Fk('7xy+21y', 2), Fk('9a^3b^2-6a^2b', 4)])
uppg(SG, [Fk('3x+6', 1), Fk('15x-25', 2), Fk('6x^2-15x', 3)])
uppg(SG, [Fk('x^2-7x', 2)])
uppg(SG, [Fk('11x+33', 1), Fk('24x^2+16x', 3)])
uppg(SG, [Fk('10x^3-25x^2+5x', 4)])
uppg(SG, [Fk('8+6x', 1), Fk('-6x^2-9x', 3, True)])
uppg(FV, [Fk('2ab+6b^2', 2), Fk('15x^2y-5xy', 3)])
uppg(FV, [Fk('ab+ab^2', 2)])


def bygg_del(d):
    if d[0] == 'fak':
        _, u, L, neg = d
        return del_bryt_ut(u, L, neg)
    return BYGG_DEL_K1(d)


BYGG_DEL_K1 = K1.bygg_del
K1.bygg_del = bygg_del
K1.U = U
K1.START_ID = START_ID


def main():
    BANK = K1.BANK
    src = open(BANK, encoding='utf-8', newline='').read()
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    finns = {u['id'] for u in data}
    nya = K1.bygg_uppgifter()
    for u in nya:
        assert u['id'] not in finns or '--skriv' not in sys.argv, u['id']
    from collections import Counter
    print(len(nya), 'uppgifter,', sum(len(u.get('spelDelar') or [0]) for u in nya), 'delar',
          sorted(Counter(len(u.get('spelDelar') or [1]) for u in nya).items()))
    if '--visa' in sys.argv:
        for u in nya:
            print(u['id'], json.dumps(u['rättSvar'], ensure_ascii=False), re.sub('<[^>]+>', ' ', u['t'])[:150])
    if '--skriv' in sys.argv:
        nl = '\r\n' if '\r\n' in src else '\n'
        slut = src.rindex('}') + 1
        ny_src = src[:slut] + ''.join(',' + nl + '  ' + K1.som_json(u, nl) for u in nya) + src[slut:]
        json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
        open(BANK, 'w', encoding='utf-8', newline='').write(ny_src)
        print('skrivet')
    return nya


if __name__ == '__main__':
    main()
