"""Felrapporter 2026-11-12 18:41 (Ma5 och Ma2). Se agent/FELRAPPORTER_2026-11-12_1841.md.

- Ma5 2.217 (Lars-Åke Andersson): heltalskombinationen av sgd (Bézouts identitet) finns inte i de flesta
  läroböcker för Matematik 5. Samma del fanns i 2.115 och 2.327. Uppgifterna frågar nu efter sgd med
  Euklides algoritm och mgm (2.217, 2.115), och beviset i 2.327 följer Euklides algoritm i stället för
  en heltalskombination. Facit följer agent/FACITMALL.md.
- Ma2 3.439 (Lars-Åke Andersson): måttet 15 cm stod under BD och såg ut att gälla BD. Figuren har nu
  en måttlinje över hela BC med texten ”BC = 15 cm”.

Idempotent: en uppgift som redan är ändrad lämnas.
  python tools/fellogg-2026-11-12-1841.py
"""
import importlib.util
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_s = importlib.util.spec_from_file_location('bankpatch', Path(__file__).with_name('bankpatch.py'))
BP = importlib.util.module_from_spec(_s)
_s.loader.exec_module(BP)


def li(rubrik, *delar):
    return f'<li><p class="facit-rubrik">{rubrik}</p>{"".join(delar)}</li>'


def mt(t):
    return f'<div class="facit-matte">\\[{t}\\]</div>'


def al(*rader):
    return mt('\\begin{aligned}' + '\\\\'.join('&' + r for r in rader) + '\\end{aligned}')


def p(t):
    return f'<p>{t}</p>'


def facit(steg, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(steg)
            + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


SGD = r'\mathrm{sgd}'
MGM = r'\mathrm{mgm}'

# ---------------------------------------------------------------- Ma5 2.217
assert math.gcd(612, 342) == 18 and 612 * 342 // 18 == 11628 == math.lcm(612, 342)
T_2217 = p(rf'Bestäm \({SGD}(612,\,342)\) med Euklides algoritm. Bestäm sedan \({MGM}(612,\,342)\).')
S_2217 = facit([
    li('Euklides algoritm: dela med resten tills resten blir 0',
       al(r'612=342\cdot1+270', r'342=270\cdot1+72', r'270=72\cdot3+54', r'72=54\cdot1+18', r'54=18\cdot3+0')),
    li(rf'Den sista resten som inte är 0 är \({SGD}\)', mt(rf'{SGD}(612,\,342)=18')),
    li(rf'Sambandet \({SGD}(a,b)\cdot {MGM}(a,b)=a\cdot b\)',
       al(rf'{MGM}(612,\,342)=\frac{{612\cdot342}}{{18}}', r'=612\cdot19=11\,628')),
    li('Kontroll med primtalsfaktorisering',
       al(r'612=2^2\cdot3^2\cdot17', r'342=2\cdot3^2\cdot19', rf'{SGD}=2\cdot3^2=18',
          rf'{MGM}=2^2\cdot3^2\cdot17\cdot19=11\,628')),
], rf'\({SGD}(612,\,342)=18\) och \({MGM}(612,\,342)=11\,628\).')
L_2217 = p('Dela det större talet med det mindre och fortsätt med divisorn och resten tills resten blir 0. '
           'Hur hänger sgd och mgm ihop med produkten av talen?')

# ---------------------------------------------------------------- Ma5 2.115
assert math.gcd(84, 30) == 6 and math.lcm(84, 30) == 420
T_2115 = p(rf'Visa med Euklides algoritm att \({SGD}(84,\,30)=6\). Bestäm sedan \({MGM}(84,\,30)\).')
S_2115 = facit([
    li('Euklides algoritm: dela med resten tills resten blir 0', al(r'84=30\cdot2+24', r'30=24\cdot1+6', r'24=6\cdot4+0')),
    li(rf'Den sista resten som inte är 0 är \({SGD}\)', mt(rf'{SGD}(84,\,30)=6'),
       p('Det var det som skulle visas.')),
    li(rf'Sambandet \({SGD}(a,b)\cdot {MGM}(a,b)=a\cdot b\)', mt(rf'{MGM}(84,\,30)=\frac{{84\cdot30}}{{6}}=420')),
    li('Kontroll med primtalsfaktorisering',
       al(r'84=2^2\cdot3\cdot7', r'30=2\cdot3\cdot5', rf'{MGM}=2^2\cdot3\cdot5\cdot7=420')),
], rf'\({SGD}(84,\,30)=6\) och \({MGM}(84,\,30)=420\).')
L_2115 = p('Dela 84 med 30 och fortsätt med divisorn och resten tills resten blir 0. '
           'Hur hänger sgd och mgm ihop med produkten av talen?')

# ---------------------------------------------------------------- Ma5 2.327
rester = []
a, b = 42, 26
while b:
    rester.append((a, b, a // b, a % b))
    a, b = b, a % b
assert a == 2 and [r[3] for r in rester] == [16, 10, 6, 4, 2, 0]
T_2327 = p(rf'Låt \(d\) vara ett positivt heltal som delar både 26 och 42. Visa att \(d\) också delar \({SGD}(26,\,42)=2\). '
           'Använd stegen i Euklides algoritm och att ett tal som delar två tal också delar deras skillnad.')
S_2327 = facit([
    li(r'Om \(d\mid a\) och \(d\mid b\) så gäller \(d\mid a-kb\)',
       p(r'Skriv \(a=dm\) och \(b=dn\), där \(m\) och \(n\) är heltal. Då är \(a-kb=d(m-kn)\), alltså en multipel av \(d\).')),
    li('Euklides algoritm för 42 och 26',
       al(*[rf'{x}={y}\cdot{k}+{r}' for x, y, k, r in rester])),
    li('Varje ny rest är en skillnad av två tal som \\(d\\) delar',
       al(r'16=42-26\cdot1\ \Rightarrow\ d\mid16', r'10=26-16\cdot1\ \Rightarrow\ d\mid10', r'6=16-10\cdot1\ \Rightarrow\ d\mid6',
          r'4=10-6\cdot1\ \Rightarrow\ d\mid4', r'2=6-4\cdot1\ \Rightarrow\ d\mid2'),
       p('I varje rad delar \\(d\\) de två talen till höger, så \\(d\\) delar också resten.')),
    li(rf'Den sista resten som inte är 0 är \({SGD}(26,\,42)=2\)',
       p(r'Alltså delar \(d\) talet 2. De enda positiva delarna till 2 är 1 och 2, och båda delar 26 och 42.')),
], rf'Varje gemensam delare \(d\) till 26 och 42 delar \({SGD}(26,\,42)=2\), så \(d=1\) eller \(d=2\).')
L_2327 = p('Skriv \\(42=26\\cdot1+16\\). Varför måste \\(d\\) dela 16 om \\(d\\) delar både 42 och 26?')


def ny_2217(q):
    if q['t'] == T_2217:
        return
    q.update(t=T_2217, s=S_2217, ledtrad=L_2217, typ='Euklides algoritm, sgd och mgm', poang='0/2/0', traningsniva=3)


def ny_2115(q):
    if q['t'] == T_2115:
        return
    q.update(t=T_2115, s=S_2115, ledtrad=L_2115, typ='Euklides algoritm, sgd och mgm', traningsniva=3)


def ny_2327(q):
    if q['t'] == T_2327:
        return
    q.update(t=T_2327, s=S_2327, ledtrad=L_2327, typ='bevisa egenskap hos sgd med Euklides algoritm')


# ---------------------------------------------------------------- Ma2 3.439: måttet 15 cm gäller BC
GAMMAL_TEXT = ('<text x="177.6" y="306.0" font-size="17" fill="#101318" text-anchor="middle" '
               'font-family="Arial, sans-serif">15 cm</text>')
MATT = ('<line x1="60" y1="326" x2="480" y2="326" stroke="#29272a" stroke-width="1.6"/>'
        '<line x1="60" y1="318" x2="60" y2="334" stroke="#29272a" stroke-width="1.6"/>'
        '<line x1="480" y1="318" x2="480" y2="334" stroke="#29272a" stroke-width="1.6"/>'
        '<text x="270" y="331.5" font-size="17" fill="#101318" text-anchor="middle" font-family="Arial, sans-serif" '
        'stroke="#fff" stroke-width="7" paint-order="stroke">BC = 15 cm</text>')


def figur_3439(txt):
    if 'BC = 15 cm</text>' in txt or '<svg' not in txt:
        return txt
    for gammal, ny in [('width="540" height="320" viewBox="0 0 540 320"', 'width="540" height="350" viewBox="0 0 540 350"'),
                       ('<rect x="1" y="1" width="538" height="318"', '<rect x="1" y="1" width="538" height="348"'),
                       (GAMMAL_TEXT, MATT)]:
        assert txt.count(gammal) == 1, gammal
        txt = txt.replace(gammal, ny)
    return txt


def ny_3439(q):
    q['t'] = figur_3439(q['t'])
    for k in q.get('spelDelar') or []:
        if 't' in k:
            k['t'] = figur_3439(k['t'])


if __name__ == '__main__':
    BP.andra(str(ROOT / 'uppgiftermatf1.js'), {'2.217': ny_2217, '2.115': ny_2115, '2.327': ny_2327})
    BP.andra(str(ROOT / 'uppgifterma2.js'), {'3.439': ny_3439})
    print('Ma5 2.217, 2.115, 2.327 och Ma2 3.439 rättade')
    sys.exit(0)
