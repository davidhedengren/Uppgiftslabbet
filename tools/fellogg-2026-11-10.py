"""Fellogg 2026-11-10 08:28: Ma3c 1.41 c (otydlig faktorisering) och Ma1 1.982 (jämnt tal i antagandet).

Facit, delfacit och ledtrådar skrivs om enligt agent/FACITMALL.md. Svaren (rättSvar) är oförändrade
och kontrolleras med sympy. Objekten i bankerna är kompakt JSON och skrivs tillbaka i samma form.

  python tools/fellogg-2026-11-10.py [--skriv]
"""
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
_s = importlib.util.spec_from_file_location('k1', Path(__file__).with_name('bygg-ma3c-kap1-mangdtraning-2026-11-06.py'))
k1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(k1)
sp, x = k1.sp, k1.x
m, mt, p, li, steglista, svarsrad, graf = k1.m, k1.mt, k1.p, k1.li, k1.steglista, k1.svarsrad, k1.graf


def facit(steg, svar):
    return '<div class="facit-v2 facit-stegvis">' + steglista(steg) + svarsrad(svar) + '</div>'


def delad(*delar):
    return ('<div class="facit-v2 facit-stegvis">' + ''.join(
        f'<div class="facit-del"><span class="facit-mark">{b})</span><div class="facit-arbete">{f}</div></div>'
        for b, f in delar) + '</div>')


# ---------------------------------------------------------------- Ma3c 1.41
A = (3 * x - 2) * (x + 2)
B = x**2 - 3 * x - 10
C = 3 * x**2 + 4 * x - 4
assert sp.expand(A) == C and sp.expand((x - 5) * (x + 2)) == B and sp.expand((x + 2) * (3 * x - 2)) == C
assert sorted(sp.solve(C, x)) == [-2, sp.Rational(2, 3)]

STEG_A = [
    li(r'Multiplicera varje term i \((3x-2)\) med varje term i \((x+2)\)',
       mt(r'(3x-2)(x+2)=3x\cdot x+3x\cdot2-2\cdot x-2\cdot2')),
    li(r'Förenkla: \(6x-2x=4x\)', mt(r'3x^2+6x-2x-4=3x^2+4x-4')),
]
STEG_B = [
    li('Sök två tal med produkten −10 och summan −3',
       p(r'För \(x^2+px+q=(x+a)(x+b)\) gäller \(a\cdot b=q\) och \(a+b=p\). Här är \(q=-10\) och \(p=-3\).'),
       mt(r'(-5)\cdot2=-10,\quad -5+2=-3')),
    li(r'Talen \(-5\) och \(2\) ger faktorerna', mt(r'x^2-3x-10=(x-5)(x+2)')),
    li('Kontroll: multiplicera tillbaka', mt(r'(x-5)(x+2)=x^2+2x-5x-10=x^2-3x-10')),
]
def _graf_c():
    svg = graf(C, [-2, sp.Rational(2, 3)], 'Grafen till y = 3x² + 4x − 4 skär x-axeln vid x = −2 och x = 2/3.')
    # Etiketten för nollstället skrivs som bråk, inte som avrundat decimaltal.
    assert svg.count('>0,666667<') == 1
    return svg.replace('>0,666667<', '>2/3<')


STEG_C = [
    li(r'Faktorsatsen: om \(x=a\) är ett nollställe är \((x-a)\) en faktor',
       p(r'Ett andragradspolynom med ledande koefficient 3 kan skrivas \(3(x-x_1)(x-x_2)\), där \(x_1\) och \(x_2\) är nollställena. Lös därför \(3x^2+4x-4=0\).')),
    li(r'Normalform: dividera båda leden med 3', mt(r'x^2+\tfrac43x-\tfrac43=0')),
    li(r'pq-formeln: \(x=-\tfrac p2\pm\sqrt{\left(\tfrac p2\right)^2-q}\) med \(p=\tfrac43\) och \(q=-\tfrac43\)',
       mt(r'x=-\tfrac23\pm\sqrt{\tfrac49+\tfrac43}=-\tfrac23\pm\sqrt{\tfrac{16}9}=-\tfrac23\pm\tfrac43'),
       p(r'Nollställena är \(x_1=-2\) och \(x_2=\tfrac23\).')),
    li('Grafisk kontroll: grafen skär x-axeln i nollställena',
       p(r'Grafen till \(y=3x^2+4x-4\) skär x-axeln i \(x=-2\) och \(x\approx0{,}67\), alltså \(\tfrac23\).'),
       _graf_c()),
    li(r'Sätt in nollställena och ta med den ledande koefficienten 3',
       mt(r'3x^2+4x-4=3(x+2)\left(x-\tfrac23\right)'),
       p(r'Multiplicera in 3 i den sista parentesen: \(3\left(x-\tfrac23\right)=3x-2\).'),
       mt(r'3x^2+4x-4=(x+2)(3x-2)')),
    li('Kontroll: multiplicera tillbaka', mt(r'(x+2)(3x-2)=3x^2-2x+6x-4=3x^2+4x-4')),
]
SV_A, SV_B, SV_C = m('3x^2+4x-4'), m('(x-5)(x+2)'), m('(x+2)(3x-2)')
LED_A = '<p>Multiplicera varje term i den första parentesen med varje term i den andra och samla sedan x-termerna.</p>'
LED_B = '<p>Sök två tal vars produkt är konstanttermen −10 och vars summa är koefficienten −3 framför x.</p>'
LED_C = ('<p>Bestäm polynomets nollställen. Dividera först med 3 så att du kan använda pq-formeln. '
         'Varje nollställe a ger en faktor (x − a), och den ledande koefficienten 3 måste också vara med.</p>')


def ma3c_141(q):
    # Del a: uttrycket är redan en produkt, så ”Förenkla eller faktorisera” var tvetydigt och formatet
    # uttryck godtog frågan avskriven. Frågan anger nu att man ska multiplicera ut, och svaret rättas som
    # ett förenklat polynom.
    gammal = r'\((3x-2)(x+2)\)'
    ny = r'Multiplicera ut och förenkla \((3x-2)(x+2)\)'
    assert q['t'].count('a) ' + gammal) == 1 and q['spelDelar'][0]['t'].count('>' + gammal + '<') == 1
    q['t'] = q['t'].replace('a) ' + gammal, 'a) ' + ny)
    q['spelDelar'][0]['t'] = q['spelDelar'][0]['t'].replace('>' + gammal + '<', '>' + ny + '<')
    q['svarFormat'][0] = 'förenklat_polynom'
    q['s'] = delad(('a', facit(STEG_A, SV_A)), ('b', facit(STEG_B, SV_B)), ('c', facit(STEG_C, SV_C)))
    q['ledtrad'] = ('<p>a) Multiplicera varje term i den första parentesen med varje term i den andra. '
                    'b) och c) Varje nollställe a ger en faktor (x − a). I c) måste den ledande koefficienten 3 också vara med.</p>')
    for d, steg, sv, led in zip(q['spelDelar'], (STEG_A, STEG_B, STEG_C), (SV_A, SV_B, SV_C), (LED_A, LED_B, LED_C)):
        d['s'] = facit(steg, sv)
        d['ledtrad'] = led


# ---------------------------------------------------------------- Ma1 1.982
n = sp.symbols('n')
assert sp.solve(2 * n + (2 * n + 2) + (2 * n + 4) - 126, n) == [20] and 40 + 42 + 44 == 126


def ma1_1982(q):
    q['s'] = facit([
        li(r'Ett jämnt tal kan skrivas \(2n\), där \(n\) är ett heltal',
           p(r'Låt det minsta talet vara \(2n\). Jämna tal som följer på varandra skiljer sig med 2, så de två '
             r'följande talen är \(2n+2\) och \(2n+4\). Då är alla tre talen säkert jämna.')),
        li('Summan av de tre talen är 126', mt(r'2n+(2n+2)+(2n+4)=126')),
        li(r'Samla termerna och lös ut \(n\)', mt(r'\begin{aligned}6n+6&=126\\6n&=120\\n&=20\end{aligned}'),
           p(r'\(n=20\) är ett heltal, så det finns tre sådana jämna tal.')),
        li(r'Talen är \(2n=40\), \(42\) och \(44\)', mt(r'40+42+44=126'),
           p('Kontrollen visar att summan stämmer och att alla tre talen är jämna.')),
    ], 'Det största talet är 44.')
    q['ledtrad'] = ('<p>Ett jämnt tal kan skrivas 2n. Hur mycket skiljer det mellan två jämna tal som följer på varandra?</p>')


OBJEKT = {'uppgiftermato1.js': {'1.41': ma3c_141}, 'uppgifterma1.js': {'1.982': ma1_1982}}


def spann(src, uid):
    dec = json.JSONDecoder()
    pos = src.index('[') + 1
    while True:
        while src[pos] in ' \t\r\n,':
            pos += 1
        obj, slut = dec.raw_decode(src, pos)
        if obj.get('id') == uid:
            return pos, slut
        pos = slut


def main():
    for fil, uppg in OBJEKT.items():
        path = ROOT / fil
        src = path.read_text(encoding='utf-8')
        for uid, funk in uppg.items():
            a, b = spann(src, uid)
            q = json.loads(src[a:b])
            # Bankerna är antingen kompakt JSON eller indragna med två steg (objektet på nivå 2).
            format_ = [f for f in (lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':')),
                                   lambda o: json.dumps(o, ensure_ascii=False, indent=2).replace('\n', '\n  '))
                       if f(q) == src[a:b]]
            assert format_, uid
            fore = json.dumps(q['rättSvar'])
            funk(q)
            assert json.dumps(q['rättSvar']) == fore
            src = src[:a] + format_[0](q) + src[b:]
            print(fil, uid, 'omskriven')
        json.loads(src[src.index('['):src.rindex(']') + 1])
        if '--skriv' in sys.argv:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(src)


if __name__ == '__main__':
    main()
