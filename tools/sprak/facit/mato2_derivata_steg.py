"""Ma4 2.426–2.450 (2026-11-20): facit var bara en svarsrad i räknarsyntax (\\boxed{f'(x)=3*x^2+6*x}) och
ledtrådarna en allmän mall. Nya facit enligt FACITMALL: regeln utskriven i rubriken, mellanled och svarsrad.
Körs: PYTHONUTF8=1 python tools/sprak/facit/mato2_derivata_steg.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

PROD = r"Produktregeln: \((uv)'=u'v+uv'\)"
KEDJA = r"Kedjeregeln: \(f'(x)=g'(h(x))\cdot h'(x)\)"


def mobil(m):
    """Två funktioner på samma rad bryts till två rader."""
    return r'\begin{gathered}' + m.replace(r',\qquad ', r'\\') + r'\end{gathered}' if r'\qquad' in m else m


def facit(steg, svar):
    steg = [(r, mobil(m)) for r, m in steg]
    li = ''.join(f'<li><p class="facit-rubrik">{r}</p><div class="facit-matte">\\[{m}\\]</div></li>' for r, m in steg)
    return (f'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">{li}</ol>'
            f'<p class="facit-svar"><strong>Svar:</strong> \\({svar}\\)</p></div>')


def p(t):
    return f'<p>{t}</p>'


NYA = {
    '2.432': (facit([(PROD, r"u=x^2,\ u'=2x,\qquad v=x+3,\ v'=1"),
                     ('Sätt in i produktregeln', r"f'(x)=2x(x+3)+x^2\cdot1"),
                     ('Multiplicera ut och samla termerna', r"f'(x)=2x^2+6x+x^2=3x^2+6x")],
                    r"f'(x)=3x^2+6x"),
              p(r'Funktionen är en produkt av \(x^2\) och \(x+3\). Du kan också multiplicera ut först.')),
    '2.433': (facit([(PROD, r"u=2x+1,\ u'=2,\qquad v=x-4,\ v'=1"),
                     ('Sätt in i produktregeln', r"f'(x)=2(x-4)+(2x+1)\cdot1"),
                     ('Multiplicera ut och samla termerna', r"f'(x)=2x-8+2x+1=4x-7")],
                    r"f'(x)=4x-7"),
              p(r'Vilka är de två faktorerna, och vad är deras derivator?')),
    '2.435': (facit([(PROD, r"u=x^3,\ u'=3x^2,\qquad v=\ln x,\ v'=\frac1x"),
                     ('Sätt in i produktregeln', r"f'(x)=3x^2\ln x+x^3\cdot\frac1x"),
                     (r'Förenkla: \(x^3\cdot\frac1x=x^2\)', r"f'(x)=3x^2\ln x+x^2")],
                    r"f'(x)=3x^2\ln x+x^2"),
              p(r'Derivatan av \(\ln x\) är \(\frac1x\). Vad blir \(x^3\cdot\frac1x\)?')),
    '2.442': (facit([(KEDJA, r"g(u)=u^4,\ g'(u)=4u^3,\qquad h(x)=3x+1,\ h'(x)=3"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=4(3x+1)^3\cdot3=12(3x+1)^3")],
                    r"f'(x)=12(3x+1)^3"),
              p(r'Derivera potensen som vanligt och multiplicera med derivatan av \(3x+1\).')),
    '2.443': (facit([(r'Skriv roten som en potens', r"f(x)=(2x+5)^{1/2}"),
                     (KEDJA, r"g(u)=u^{1/2},\ g'(u)=\frac{1}{2\sqrt u},\qquad h(x)=2x+5,\ h'(x)=2"),
                     ('Sätt in och förkorta med 2', r"f'(x)=\frac{1}{2\sqrt{2x+5}}\cdot2=\frac{1}{\sqrt{2x+5}}")],
                    r"f'(x)=\frac{1}{\sqrt{2x+5}}"),
              p(r'Skriv roten som potensen \((2x+5)^{1/2}\).')),
    '2.444': (facit([(KEDJA, r"g(u)=e^u,\ g'(u)=e^u,\qquad h(x)=x^2,\ h'(x)=2x"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=e^{x^2}\cdot2x=2xe^{x^2}")],
                    r"f'(x)=2xe^{x^2}"),
              p(r'Derivatan av \(e^u\) är \(e^u\). Glöm inte den inre derivatan av \(x^2\).')),
    '2.445': (facit([(KEDJA, r"g(u)=\sin u,\ g'(u)=\cos u,\qquad h(x)=4x,\ h'(x)=4"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=\cos(4x)\cdot4=4\cos(4x)")],
                    r"f'(x)=4\cos(4x)"),
              p(r'Vad är den inre derivatan av \(4x\)?')),
    '2.446': (facit([(KEDJA, r"g(u)=\ln u,\ g'(u)=\frac1u,\qquad h(x)=5x-2,\ h'(x)=5"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=\frac{1}{5x-2}\cdot5=\frac{5}{5x-2}")],
                    r"f'(x)=\frac{5}{5x-2}"),
              p(r'Derivatan av \(\ln u\) är \(\frac1u\). Multiplicera med den inre derivatan.')),
    '2.447': (facit([(KEDJA, r"g(u)=u^5,\ g'(u)=5u^4,\qquad h(x)=x^2+1,\ h'(x)=2x"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=5(x^2+1)^4\cdot2x=10x(x^2+1)^4")],
                    r"f'(x)=10x(x^2+1)^4"),
              p(r'Den inre funktionen är \(x^2+1\).')),
    '2.448': (facit([(KEDJA, r"g(u)=\cos u,\ g'(u)=-\sin u,\qquad h(x)=x^3,\ h'(x)=3x^2"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=-\sin(x^3)\cdot3x^2=-3x^2\sin(x^3)")],
                    r"f'(x)=-3x^2\sin(x^3)"),
              p(r'Derivatan av \(\cos u\) är \(-\sin u\). Den inre funktionen är \(x^3\).')),
    '2.449': (facit([(KEDJA, r"g(u)=e^u,\ g'(u)=e^u,\qquad h(x)=\sin x,\ h'(x)=\cos x"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=e^{\sin x}\cdot\cos x")],
                    r"f'(x)=e^{\sin x}\cos x"),
              p(r'Den inre funktionen är \(\sin x\).')),
    '2.450': (facit([(KEDJA, r"g(u)=\ln u,\ g'(u)=\frac1u,\qquad h(x)=1+x^4,\ h'(x)=4x^3"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=\frac{1}{1+x^4}\cdot4x^3=\frac{4x^3}{1+x^4}")],
                    r"f'(x)=\frac{4x^3}{1+x^4}"),
              p(r'Den inre funktionen är \(1+x^4\).')),
    '2.426': (facit([(r"Derivatan av \(e^{kx}\) är \(ke^{kx}\)", r"\frac{d}{dx}e^{2x}=2e^{2x}"),
                     ('Konstanten 5 står kvar', r"f'(x)=5\cdot2e^{2x}=10e^{2x}")],
                    r"f'(x)=10e^{2x}"),
              p(r'Vad är derivatan av \(e^{kx}\)? Konstanten 5 står kvar.')),
    '2.428': (facit([(PROD, r"u=e^x,\ u'=e^x,\qquad v=\sin x,\ v'=\cos x"),
                     ('Sätt in i produktregeln', r"f'(x)=e^x\sin x+e^x\cos x"),
                     (r'Bryt ut \(e^x\)', r"f'(x)=e^x(\sin x+\cos x)")],
                    r"f'(x)=e^x(\sin x+\cos x)"),
              p(r'Funktionen är en produkt. Vilka är faktorerna, och vad är deras derivator?')),
    '2.429': (facit([(KEDJA, r"g(u)=\ln u,\ g'(u)=\frac1u,\qquad h(x)=x^2+1,\ h'(x)=2x"),
                     ('Derivera den yttre funktionen och multiplicera med den inre derivatan', r"f'(x)=\frac{1}{x^2+1}\cdot2x=\frac{2x}{x^2+1}")],
                    r"f'(x)=\frac{2x}{x^2+1}"),
              p(r'Den inre funktionen är \(x^2+1\).')),
}

b = Bank('mato2')
for id_, (s, led) in NYA.items():
    u = b.obj(id_)
    assert not u.get('spelDelar'), id_
    b.ersatt(id_, [(u['s'], s), (u['ledtrad'], led)])
print(b.spara(), 'objekt skrivna')
