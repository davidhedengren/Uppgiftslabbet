# Ma4 kort om derivator, sammansatta funktioner och primitiva funktioner: facit enligt FACITMALL (2026-11-22).
POT = r"Derivatan av en potens: \(D\,x^n=nx^{n-1}\)"
TERM = r"Derivera term för term: \(D\,x^n=nx^{n-1}\), och en konstant har derivatan 0"
KED = r"Kedjeregeln: \(D\,f(g(x))=f'(g(x))\cdot g'(x)\)"
EXP = r"Derivatan av \(e^{kx}\) är \(ke^{kx}\)"
SIN = r"Derivatan av \(\sin kx\) är \(k\cos kx\)"
PRIM = r"Primitiv funktion till en potens: \(\int x^n\,dx=\frac{x^{n+1}}{n+1}+C\)"
INT = r"Integralens värde: \(\int_a^bf(x)\,dx=F(b)-F(a)\)"
NUM = ('Integranden saknar en enkel primitiv funktion', None,
       'Beräkna integralen numeriskt, till exempel med Integral(…) i GeoGebra eller med räknarens integralfunktion.')


def delar(*d):
    """d = (etikett, steg, svar). Huvudfacit: alla steg, rubriken på första steget får etiketten."""
    huvud, svar, ut = [], [], {}
    for et, steg, s in d:
        ut[et] = (steg, s)
        forsta = steg[0]
        huvud.append((f'{et}) ' + forsta[0],) + tuple(forsta[1:]))
        huvud.extend(steg[1:])
        svar.append(f'{et}) {s}')
    ut[''] = (huvud, ' '.join(svar))
    return ut


F = {
    # kort om derivator
    '2.48': ([(POT, r"f'(x)=3x^2+a"), (r"Tangentens lutning vid \(x=1\) är \(f'(1)\)", r"f'(1)=3+a=7\quad\Rightarrow\quad a=4")], r"\(a=4\)"),
    '2.214': ([(TERM, r"f'(x)=4x^3-4x"), ('Andraderivatan får du genom att derivera en gång till', r"f''(x)=12x^2-4")], r"\(f''(x)=12x^2-4\)"),
    '2.499': ([(POT, r"f'(x)=5x^{5-1}=5x^4")], r"\(f'(x)=5x^4\)"),
    '2.500': ([(TERM, r"f'(x)=3\cdot2x-4\cdot1+0=6x-4")], r"\(f'(x)=6x-4\)"),
    '2.501': ([('En konstant ändras inte, så derivatan är 0', r"f'(x)=0")], r"\(f'(x)=0\)"),
    '2.502': ([('Skriv om funktionen som en potens', r"f(x)=\frac4x=4x^{-1}"),
               (POT, r"f'(x)=4\cdot(-1)x^{-2}=-\frac{4}{x^2}")], r"\(f'(x)=-\frac{4}{x^2}\)"),
    '2.503': ([('Skriv om roten som en potens', r"f(x)=\sqrt x=x^{1/2}"),
               (POT, r"f'(x)=\frac12x^{-1/2}=\frac{1}{2\sqrt x}")], r"\(f'(x)=\frac{1}{2\sqrt x}\)"),
    '2.506': ([(POT, r"f'(x)=3x^2"), (r"Sätt in \(x=2\)", r"f'(2)=3\cdot2^2=12")], "12"),
    # sammansatta funktioner
    '2.112': ([(KED, r"h'(x)=f'(g(x))\cdot g'(x)"),
               (r"Sätt in \(x=1\) och använd \(g(1)=2\)", r"h'(1)=f'(2)\cdot g'(1)=3\cdot(-4)=-12")], r"\(-12\)"),
    '2.507': ([(KED, None, r'Yttre funktionen är \(u^3\) och inre funktionen \(u=x+1\), med inre derivatan 1.'),
               ('Derivera den yttre och multiplicera med den inre derivatan', r"f'(x)=3(x+1)^2\cdot1=3(x+1)^2")], r"\(f'(x)=3(x+1)^2\)"),
    '2.508': ([(KED, None, r'Yttre funktionen är \(u^2\) och inre funktionen \(u=2x+1\), med inre derivatan 2.'),
               ('Derivera den yttre och multiplicera med den inre derivatan', r"f'(x)=2(2x+1)\cdot2=4(2x+1)")], r"\(f'(x)=4(2x+1)\)"),
    '2.509': ([(EXP, r"f'(x)=5e^{5x}")], r"\(f'(x)=5e^{5x}\)"),
    '2.510': ([(KED, None, r'Yttre funktionen är \(\sqrt u=u^{1/2}\) och inre funktionen \(u=2x+1\), med inre derivatan 2.'),
               ('Derivera den yttre och multiplicera med den inre derivatan', r"f'(x)=\frac{1}{2\sqrt{2x+1}}\cdot2=\frac{1}{\sqrt{2x+1}}")],
              r"\(f'(x)=\frac{1}{\sqrt{2x+1}}\)"),
    '2.511': ([(KED, None, r'Yttre funktionen är \(u^4\) och inre funktionen \(u=x^2+1\), med inre derivatan \(2x\).'),
               ('Derivera den yttre och multiplicera med den inre derivatan', r"f'(x)=4(x^2+1)^3\cdot2x=8x(x^2+1)^3")], r"\(f'(x)=8x(x^2+1)^3\)"),
    '2.512': ([(KED, r"f'(x)=3(5-x)^2\cdot(-1)=-3(5-x)^2"), (r"Sätt in \(x=4\)", r"f'(4)=-3\cdot1^2=-3")], r"\(-3\)"),
    '2.513': ([(r"Beräkna den inre funktionen \(g(1)\) först", r"g(1)=1+3=4"), (r"Sätt in resultatet i \(f\)", r"f(g(1))=f(4)=4^2=16")], "16"),
    '2.514': ([(r"Beräkna den inre funktionen \(f(2)\) först", r"f(2)=2^2=4"), (r"Sätt in resultatet i \(g\)", r"g(f(2))=g(4)=4+3=7")], "7"),
    '2.255': delar(
        ('a', [(EXP, r"D\,e^{-2x}=-2e^{-2x}")], r"\(-2e^{-2x}\)"),
        ('b', [(r"Kedjeregeln med \(D\ln u=\frac{u'}{u}\)", r"D\ln(x^2+1)=\frac{2x}{x^2+1}")], r"\(\frac{2x}{x^2+1}\)"),
        ('c', [(SIN, r"D\sin5x=5\cos5x")], r"\(5\cos5x\)"),
        ('d', [(r"Derivatan av \(\cos kx\) är \(-k\sin kx\)", r"D\cos\frac x3=-\frac13\sin\frac x3")], r"\(-\frac13\sin\frac x3\)"),
    ),
    '2.403': ([(EXP, r"f'(x)=-2e^{-2x}")], r"\(f'(x)=-2e^{-2x}\)"),
    '2.409': ([(KED, r"f'(x)=e^{2x+1}\cdot2=2e^{2x+1}"), (r"Sätt in \(x=0\)", r"f'(0)=2e^{1}=2e")], r"\(2e\)"),
    '2.518': ([(EXP, r"f'(x)=3\cdot4e^{4x}=12e^{4x}")], r"\(f'(x)=12e^{4x}\)"),
    '2.521': ([(SIN, r"f'(x)=4\cos4x")], r"\(f'(x)=4\cos4x\)"),
    # primitiva funktioner och integraler
    '3.86': delar(
        ('a', [(INT, r"\int_0^2(3x+1)\,dx=\Big[\frac32x^2+x\Big]_0^2=6+2=8")], "8"),
        ('b', [(r"En primitiv funktion till \(\cos x\) är \(\sin x\)", r"\Big[\sin x\Big]_0^{\pi/2}=1-0=1")], "1"),
        ('c', [(r"En primitiv funktion till \(\frac1x\) är \(\ln x\)", r"\Big[\ln x\Big]_1^e=1-0=1")], "1"),
    ),
    '3.237': ([NUM, ('Numeriskt värde', r"\int_0^3\sqrt{1+x^3}\,dx\approx7{,}341")], r"\(7{,}341\)"),
    '3.188': ([(INT, r"\int_0^2(ax+1)\,dx=\Big[\frac{ax^2}{2}+x\Big]_0^2=2a+2"),
               ('Sätt integralen lika med 8', r"2a+2=8\quad\Rightarrow\quad a=3")], r"\(a=3\)"),
    '3.190': delar(
        ('a', [(PRIM, r"\Big[\frac{x^3}{3}\Big]_0^2=\frac83")], r"\(\frac83\)"),
        ('b', [(r"En primitiv funktion till \(\sin x\) är \(-\cos x\)", r"\Big[-\cos x\Big]_0^\pi=1+1=2")], "2"),
        ('c', [(r"En primitiv funktion till \(e^x\) är \(e^x\)", r"\Big[e^x\Big]_0^1=e-1")], r"\(e-1\)"),
        ('d', [(r"En primitiv funktion till \(\frac1x\) är \(\ln x\)", r"\Big[\ln x\Big]_1^e=1-0=1")], "1"),
    ),
    '3.192': ([(INT, r"\int_1^a2x\,dx=\Big[x^2\Big]_1^a=a^2-1"),
               ('Sätt integralen lika med 15', r"a^2-1=15\quad\Rightarrow\quad a^2=16"),
               (r"Välj roten som uppfyller \(a>1\)", r"a=4")], r"\(a=4\)"),
    '3.226': delar(
        ('a', [(PRIM, r"\Big[x^2\Big]_0^3=9")], "9"),
        ('b', [(PRIM, r"\Big[2x^3-2x\Big]_0^1=2-2=0")], "0"),
        ('c', [(r"En primitiv funktion till \(\frac1x\) är \(\ln x\)", r"\Big[\ln x\Big]_1^e=1-0=1")], "1"),
        ('d', [(r"En primitiv funktion till \(2\sin x\) är \(-2\cos x\)", r"\Big[-2\cos x\Big]_0^{\pi/2}=0+2=2")], "2"),
    ),
    '3.479': ([(PRIM, r"F(x)=4\cdot\frac{x^4}{4}=x^4"), ('Kontrollera genom att derivera', r"F'(x)=4x^3")], r"\(F(x)=x^4\)"),
    '3.480': ([(PRIM, r"F(x)=6\cdot\frac{x^2}{2}=3x^2"), ('Kontrollera genom att derivera', r"F'(x)=6x")], r"\(F(x)=3x^2\)"),
    '3.481': ([(PRIM, r"F(x)=x^3"), (INT, r"\Big[x^3\Big]_0^2=8-0=8")], "8"),
    '3.483': ([(PRIM, r"F(x)=x^2+x"), (INT, r"\Big[x^2+x\Big]_0^1=2-0=2")], "2"),
    '3.484': ([(r"En primitiv funktion till \(\sin x\) är \(-\cos x\)", None),
               (INT, r"\Big[-\cos x\Big]_0^\pi=-\cos\pi+\cos0=1+1=2")], "2"),
    '3.485': ([(r"En primitiv funktion till \(\frac1x\) är \(\ln x\) när \(x>0\)", None),
               (INT, r"\Big[\ln x\Big]_1^e=\ln e-\ln1=1-0=1")], "1"),
    '3.486': ([(PRIM, r"F(x)=x^2+C"), (r"Villkoret \(F(0)=5\) bestämmer \(C\)", r"F(0)=0+C=5\quad\Rightarrow\quad C=5")], r"\(F(x)=x^2+5\)"),
    '4.625': ([NUM, ('Numeriskt värde', r"\int_0^6e^{-x}\sin2x\,dx\approx0{,}399")], r"\(0{,}399\)"),
}
