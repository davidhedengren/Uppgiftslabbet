"""Ma3c Funktioner: rutinuppgifter av typen ”förenkla f(x+h) − f(x)”, 1.1129–1.1144 (2026-11-20).

Användaren: ”lägg till ett gäng med rutinuppgifter av typen f(x)=2x^2+3x, förenkla f(x+h)-f(x).”

Uppgifterna är medvetet rutinmässiga men varierar funktion, bokstav (f, g, p, s), variabel (x, t, a), punkt och
formulering. Svaren räknas exakt med bråk och rättas med formatet förenklat_polynom (termerna i valfri ordning).
Facit följer FACITMALL: sätt in, kvadreringsregeln med de faktiska bokstäverna, och vilka termer som tar ut varandra.

  python tools/bygg-ma3c-fxh-2026-11-20.py [--skriv]
"""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
import bankobjekt as B  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SKRIV = '--skriv' in sys.argv


def tal(c, latex=True):
    c = Fr(c)
    if c.denominator == 1:
        s = str(c.numerator)
    else:
        s = f'{float(c):g}'
    return s.replace('.', '{,}' if latex else '.')


def poly(termer, latex=True):
    """termer: lista (koef, monom) i önskad ordning. monom '' är konstant."""
    ut = ''
    for k, mon in termer:
        if k == 0:
            continue
        neg = k < 0
        a = abs(Fr(k))
        if mon == '':
            kt = tal(a, latex)
        elif a == 1:
            kt = mon
        else:
            kt = tal(a, latex) + mon
        if not ut:
            ut = ('-' if neg else '') + kt
        else:
            ut += ('-' if neg else '+') + kt
    return ut or '0'


def L(termer):
    return poly(termer, True).replace('h^2', 'h^2').replace('x^2', 'x^2')


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def al(*rader):
    return mt('\\begin{aligned}' + '\\\\'.join('&' + r for r in rader) + '\\end{aligned}')


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def m(t):
    return f'\\({t}\\)'


UPPG = []


def uppg(uid, fn, v, a, b, c, fraga, niva, tn, ledtrad, punkt=None, arg=None, kvot=False):
    """f(v) = a v² + b v + c. Sökt: f(arg+h) − f(arg) (arg = v, en annan bokstav eller ett tal), eller kvoten."""
    a, b, c = Fr(a), Fr(b), Fr(c)
    arg = arg or v
    fx = L([(a, f'{v}^2'), (b, v), (c, '')])
    # f(arg) och f(arg+h)
    if punkt is not None:
        p = Fr(punkt)
        fp = a * p * p + b * p + c
        # f(p+h) = a(p+h)^2 + b(p+h) + c = a h^2 + (2ap + b) h + fp
        lin = 2 * a * p + b
        diff = [(a, 'h^2'), (lin, 'h')]
        P = tal(p)
        steg = [
            li(f'Beräkna {m(f"{fn}({P})")}', mt(f'{fn}({P})=' + _insatt(a, b, c, P, tal_=True) + f'={tal(fp)}')),
            li(f'Sätt in {m(f"{P}+h")} och använd kvadreringsregeln {m(f"({P}+h)^2={tal(p * p)}+{tal(2 * p)}h+h^2")}',
               al(f'{fn}({P}+h)=' + _insatt(a, b, c, f'({P}+h)'),
                  '=' + L([(a, 'h^2'), (lin, 'h'), (fp, '')]))),
            li(f'Dra bort {m(f"{fn}({P})={tal(fp)}")}, så blir bara termerna med {m("h")} kvar',
               mt(f'{fn}({P}+h)-{fn}({P})={L(diff)}'))]
        svar_l, svar_r = L(diff), poly(diff, False)
    else:
        X = arg
        # f(X+h) - f(X) = 2a X h + a h^2 + b h
        diff = [(2 * a, f'{X}h'), (a, 'h^2'), (b, 'h')]
        if kvot:
            q = [(2 * a, X), (a, 'h'), (b, '')]
        insatt = _insatt(a, b, c, f'({X}+h)')
        utv = L([(a, f'{X}^2'), (2 * a, f'{X}h'), (a, 'h^2'), (b, X), (b, 'h'), (c, '')])
        fX = L([(a, f'{X}^2'), (b, X), (c, '')])
        bort = [t for t in (L([(a, f'{X}^2')]) if a else '', L([(b, X)]) if b else '', tal(c) if c else '') if t]
        bort_txt = ' och '.join(m(t) for t in bort) if len(bort) <= 2 else ', '.join(m(t) for t in bort[:-1]) + ' och ' + m(bort[-1])
        steg = [li(f'Ersätt {m(v)} med {m(f"{X}+h")} i {m(f"{fn}({v})={fx}")}', mt(f'{fn}({X}+h)={insatt}'))]
        if a != 0:
            ak = '' if a == 1 else '-' if a == -1 else tal(a)
            rest = L([(b, X), (b, 'h'), (c, '')]) if (b or c) else ''
            forsta = f'{fn}({X}+h)={ak}({X}^2+2{X}h+h^2)'
            rader = [forsta] + ([f'\\quad{rest if rest.startswith("-") else "+" + rest}'] if rest else []) + [f'={utv}']
            steg.append(li(f'Kvadreringsregeln: {m(f"({X}+h)^2={X}^2+2{X}h+h^2")}', al(*rader)))
        else:
            steg.append(li('Multiplicera in i parentesen', mt(f'{fn}({X}+h)={utv}')))
        steg.append(li(f'Dra bort {m(f"{fn}({X})={fX}")}: {bort_txt} tar ut varandra',
                       al(f'{fn}({X}+h)-{fn}({X})', f'=({utv})', f'\\quad-({fX})', f'={L(diff)}')))
        svar_l, svar_r = L(diff), poly(diff, False)
        if kvot:
            steg.append(li(f'Dela varje term med {m("h")}', mt(f'\\frac{{{L(diff)}}}{{h}}={L(q)}')))
            svar_l, svar_r = L(q), poly(q, False)
    q = {'id': uid, 'kap': 1, 'omr': 'funktioner', 'kurs': ['1b', '1c'], 'familj': 'Funktionsvärden',
         'niva': niva, 'poang': {'E': '1/0/0', 'C': '0/1/0'}[niva] if tn <= 2 or niva == 'C' else '1/0/0',
         'traningsniva': tn, 'arbetsinsats': 1 if tn == 1 else 2, 'formaga': ['procedur'],
         'miniräknare': False, 'geogebra': False, 'spel': True, 'självrättning': True,
         't': f'<p>{fraga}</p>', 'ledtrad': f'<p>{ledtrad}</p>', 's': facit(steg, m(svar_l) + '.'),
         'rättSvar': svar_r, 'svarstyp': 'uttryck', 'tolerans': None, 'svarFormat': 'förenklat_polynom'}
    UPPG.append(q)


def _insatt(a, b, c, X, tal_=False):
    """a·X² + b·X + c med X insatt. Med tal_ skrivs gångertecken ut (2·3 i stället för 23)."""
    gg = '\\cdot ' if tal_ else ''
    termer = []
    if a:
        termer.append(('' if a == 1 else '-' if a == -1 else tal(a) + gg) + f'{X}^2')
    if b:
        termer.append(('' if b == 1 else '-' if b == -1 else tal(b) + gg) + X)
    if c:
        termer.append(tal(c))
    if not termer:
        return ''
    ut = termer[0]
    for t in termer[1:]:
        ut += t if t.startswith('-') else '+' + t
    return ut


def bygg():
    uppg('1.1129', 'f', 'x', 0, 4, 1, 'Funktionen \\(f\\) ges av \\(f(x)=4x+1\\). Förenkla \\(f(x+h)-f(x)\\).', 'E', 1,
         'Byt ut varje \\(x\\) mot \\(x+h\\). Vad blir kvar när du drar bort \\(f(x)\\)?')
    uppg('1.1130', 'g', 't', 0, -2, 7, 'För \\(g(t)=7-2t\\) gäller det att förenkla \\(g(t+h)-g(t)\\).', 'E', 1,
         'Skriv först \\(g(t+h)\\). Glöm inte att \\(-2\\) multipliceras med både \\(t\\) och \\(h\\).')
    uppg('1.1131', 'f', 'x', 1, 0, 0, 'Låt \\(f(x)=x^2\\). Förenkla \\(f(x+h)-f(x)\\) så långt som möjligt.', 'E', 2,
         'Använd kvadreringsregeln på \\((x+h)^2\\).')
    uppg('1.1132', 'f', 'x', 3, 0, 0, 'Funktionen \\(f\\) ges av \\(f(x)=3x^2\\). Förenkla \\(f(x+h)-f(x)\\).', 'E', 2,
         'Utveckla \\((x+h)^2\\) först och multiplicera sedan med 3.')
    uppg('1.1133', 'f', 'x', 2, 3, 0, 'Funktionen \\(f\\) ges av \\(f(x)=2x^2+3x\\). Förenkla \\(f(x+h)-f(x)\\).', 'E', 3,
         'Ersätt \\(x\\) med \\(x+h\\) i båda termerna. Vilka termer tar ut varandra när du drar bort \\(f(x)\\)?')
    uppg('1.1134', 'f', 'x', 1, -5, 0, 'För funktionen \\(f(x)=x^2-5x\\) ska \\(f(x+h)-f(x)\\) förenklas. Skriv uttrycket '
         'utan parenteser.', 'E', 3, 'Skriv \\(f(x+h)=(x+h)^2-5(x+h)\\) och utveckla.')
    uppg('1.1135', 'p', 'x', 1, 4, 7, 'Polynomet \\(p(x)=x^2+4x+7\\) är givet. Förenkla \\(p(x+h)-p(x)\\).', 'E', 3,
         'Konstanten 7 finns i både \\(p(x+h)\\) och \\(p(x)\\). Vad händer med den?')
    uppg('1.1136', 's', 't', 5, -1, 0, 'Ett föremål har läget \\(s(t)=5t^2-t\\). Förenkla \\(s(t+h)-s(t)\\).', 'E', 3,
         'Byt \\(t\\) mot \\(t+h\\) och utveckla \\((t+h)^2\\).')
    uppg('1.1137', 'f', 'x', -1, 0, 6, 'Funktionen \\(f\\) ges av \\(f(x)=6-x^2\\). Förenkla \\(f(x+h)-f(x)\\).', 'E', 3,
         'Minustecknet framför \\((x+h)^2\\) gäller alla tre termerna när du utvecklar.')
    uppg('1.1138', 'f', 'x', -1, 6, 0, 'Förenkla \\(f(x+h)-f(x)\\) för \\(f(x)=-x^2+6x\\).', 'C', 3,
         'Utveckla \\(-(x+h)^2\\) med en parentes runt kvadraten, så att tecknen blir rätt.')
    uppg('1.1139', 'f', 'x', -3, 2, -1, 'Funktionen \\(f\\) ges av \\(f(x)=-3x^2+2x-1\\). Förenkla \\(f(x+h)-f(x)\\) så '
         'långt som möjligt.', 'C', 3, 'Sätt parentes runt hela \\(f(x)\\) när du drar bort det, och byt tecken på '
         'alla termer.')
    uppg('1.1140', 'f', 'x', Fr(1, 2), 2, 0, 'Låt \\(f(x)=0{,}5x^2+2x\\). Förenkla \\(f(x+h)-f(x)\\).', 'C', 3,
         'Halva av \\(2xh\\) är \\(xh\\). Utveckla \\((x+h)^2\\) och multiplicera med 0,5.')
    uppg('1.1141', 'f', 'x', 1, 3, 0, 'Funktionen \\(f\\) ges av \\(f(x)=x^2+3x\\). Förenkla \\(f(2+h)-f(2)\\).', 'E', 3,
         'Räkna ut \\(f(2)\\) som ett tal. Sätt sedan in \\(2+h\\) och utveckla.', punkt=2)
    uppg('1.1142', 'g', 'x', 2, -1, 4, 'För \\(g(x)=2x^2-x+4\\), förenkla \\(g(a+h)-g(a)\\).', 'E', 3,
         'Gör som med \\(x+h\\), men med bokstaven \\(a\\) i stället för \\(x\\).', arg='a')
    uppg('1.1143', 'f', 'x', 4, -3, 0, 'Funktionen \\(f\\) ges av \\(f(x)=4x^2-3x\\). Förenkla ändringskvoten '
         '\\(\\dfrac{f(x+h)-f(x)}{h}\\). Anta att \\(h\\ne0\\).', 'C', 3,
         'Förenkla först täljaren \\(f(x+h)-f(x)\\). Alla termer som blir kvar innehåller \\(h\\).', kvot=True)
    uppg('1.1144', 'f', 'x', 1, -2, 5, 'Skriv \\(f(x+h)-f(x)\\) utan parenteser när \\(f(x)=x^2-2x+5\\).', 'E', 3,
         'Vilka termer finns i både \\(f(x+h)\\) och \\(f(x)\\)?')


def main():
    bygg()
    src, bank = B.las(ROOT / 'uppgiftermato1.js')
    ids = {q['id'] for q in bank}
    for q in UPPG:
        assert q['id'] not in ids, q['id']
        q['poang'] = '1/0/0' if q['niva'] == 'E' else '0/1/0'
    sista = max(i for i, q in enumerate(bank) if q.get('kap') == 1)
    sp = B.spann(src)
    slut = sp[sista][1]
    prefix = B._prefix(src, sp[sista][0])
    ny_src = src[:slut] + ''.join(',\n' + B._dump(q, prefix) for q in UPPG) + src[slut:]
    json.loads(ny_src[ny_src.index('['):ny_src.rindex(']') + 1])
    for q in UPPG:
        print(q['id'], q['niva'], q['traningsniva'], q['rättSvar'])
    if SKRIV:
        B.skriv(ROOT / 'uppgiftermato1.js', ny_src)


if __name__ == '__main__':
    main()
