# Ma4 trigonometriska modeller, skivmetoden, komplexa tal och polynomdivision: facit enligt FACITMALL (2026-11-22).
MODELL = r"Modellen \(f(t)=D+A\sin(Bt)\): medellinje \(D\), amplitud \(A\) och period \(T=\frac{2\pi}{B}\)"
MODELL_GR = r"I grader: perioden är \(T=\frac{360^\circ}{B}\)"
SINGR = r"Sinus varierar mellan \(-1\) och \(1\)"
COSGR = r"Cosinus varierar mellan \(-1\) och \(1\)"
SKIV = r"Skivmetoden: \(V=\pi\int_a^b\big(f(x)\big)^2\,dx\)"
KONJ = r"Konjugatet: \(\overline{a+bi}=a-bi\)"
ABS = r"Absolutbeloppet: \(|a+bi|=\sqrt{a^2+b^2}\)"
I2 = r"Multiplicera ut och använd \(i^2=-1\)"
DM = r"De Moivres formel: \(\left(re^{iv}\right)^n=r^ne^{inv}\)"
PQ = r"pq-formeln: \(x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}\)"
ROT = r"Roten ur ett negativt tal: \(\sqrt{-a}=i\sqrt a\) när \(a>0\)"
REST = r"Restsatsen: resten vid division med \(x-a\) är \(P(a)\)"
KONJR = r"Konjugatregeln: \(a^2-b^2=(a+b)(a-b)\)"


def delar(*d):
    huvud, svar, ut = [], [], {}
    for et, steg, s in d:
        ut[et] = (steg, s)
        huvud.append((f'{et}) ' + steg[0][0],) + tuple(steg[0][1:]))
        huvud.extend(steg[1:])
        svar.append(f'{et}) {s}')
    ut[''] = (huvud, ' '.join(svar))
    return ut


def division(steg, kvot, rest='0'):
    """steg = [(term, produkt, ny_rest)] för lång division."""
    ut = []
    for term, prod, ny in steg:
        ut.append((rf"Nästa term i kvoten är \({term}\)", rf"{prod}\quad\Rightarrow\quad\text{{kvar: }}{ny}"))
    return ut


def zn(z, n, rhs, steg_text):
    return ([(DM, None, steg_text), ('Kontrollera genom att upphöja', rf"\left({z}\right)^{{{n}}}={rhs}")], rf"till exempel \(z={z}\)")


F = {
    # trigonometriska modeller
    '1.482': ([(MODELL, r"B=\frac{2\pi}{10}\quad\Rightarrow\quad T=\frac{2\pi}{B}=10")], "10"),
    '1.484': delar(
        ('a', [(MODELL, r"D=25", 'Konstanttermen är medellinjen.')], "25"),
        ('b', [(MODELL, r"A=5", 'Amplituden är koefficienten framför sinus.')], "5"),
    ),
    '1.485': delar(
        ('a', [(SINGR, r"f_{\min}=8-2\cdot1=6")], "6"),
        ('b', [(SINGR, r"f_{\max}=8+2\cdot1=10")], "10"),
    ),
    '1.491': delar(
        ('a', [('Medellinjen ligger mitt emellan största och minsta värdet', r"D=\frac{90+10}{2}=50")], "50"),
        ('b', [('Amplituden är halva skillnaden mellan största och minsta värdet', r"A=\frac{90-10}{2}=40")], "40"),
        ('c', [(r"Perioden: \(T=\frac{2\pi}{B}\)", r"B=\frac{2\pi}{T}=\frac{2\pi}{12}=\frac{\pi}{6}")], r"\(\frac{\pi}{6}\)"),
    ),
    '1.600': ([(SINGR, r"d_{\max}=3+1{,}5\cdot1=4{,}5")], "4,5 m"),
    '1.601': ([(SINGR, r"d_{\min}=3+1{,}5\cdot(-1)=1{,}5")], "1,5 m"),
    '1.603': ([(SINGR, r"D_{\max}=12{,}2+6{,}3\cdot1=18{,}5")], "18,5 timmar"),
    '1.604': ([(COSGR, None, r'Eftersom cosinus står med minustecken blir höjden minst när \(\cos=1\).'),
               ('Sätt in cosinusvärdet 1', r"h_{\min}=20-18\cdot1=2")], "2 m"),
    '1.606': ([(r"Sätt in \(t=15\) i modellen", r"h(15)=20-18\cos(12\cdot15)^\circ=20-18\cos180^\circ"),
               (r"Använd \(\cos180^\circ=-1\)", r"h(15)=20-18\cdot(-1)=38")], "38 m"),
    '1.607': ([('Tiden mellan två högvatten är en period', None), (MODELL_GR, r"T=\frac{360^\circ}{30^\circ}=12")], "12 timmar"),
    # skivmetoden
    '3.111': ([(SKIV, r"V=\pi\int_0^4\left(\sqrt x\right)^2dx=\pi\int_0^4x\,dx"),
               ('Bestäm en primitiv funktion och sätt in gränserna', r"\pi\Big[\frac{x^2}{2}\Big]_0^4=\pi\cdot8=8\pi")], r"\(8\pi\) volymenheter"),
    '3.194': ([(SKIV, r"V=\pi\int_0^1\left(x^2\right)^2dx=\pi\int_0^1x^4\,dx"),
               ('Bestäm en primitiv funktion och sätt in gränserna', r"\pi\Big[\frac{x^5}{5}\Big]_0^1=\frac{\pi}{5}")], r"\(\frac{\pi}{5}\)"),
    '3.203': ([(SKIV, r"V=\pi\int_0^2(2-x)^2\,dx=\pi\int_0^2(4-4x+x^2)\,dx"),
               ('Bestäm en primitiv funktion och sätt in gränserna', r"\pi\Big[4x-2x^2+\frac{x^3}{3}\Big]_0^2=\pi\left(8-8+\frac83\right)=\frac{8\pi}{3}")],
              r"\(\frac{8\pi}{3}\)"),
    '3.512': ([(SKIV, r"V=\pi\int_0^52^2\,dx=\pi\cdot4\cdot5=20\pi"),
               ('Kontroll: kroppen är en cylinder', r"V=\pi r^2h=\pi\cdot2^2\cdot5=20\pi")], r"\(20\pi\)"),
    '3.514': ([(SKIV, r"V=\pi\int_0^2\left(\sqrt x\right)^2dx=\pi\int_0^2x\,dx"),
               ('Bestäm en primitiv funktion och sätt in gränserna', r"\pi\Big[\frac{x^2}{2}\Big]_0^2=2\pi")], r"\(2\pi\)"),
    '3.516': ([(SKIV, r"V=\pi\int_0^6\left(\frac x2\right)^2dx=\pi\int_0^6\frac{x^2}{4}\,dx"),
               ('Bestäm en primitiv funktion och sätt in gränserna', r"\pi\Big[\frac{x^3}{12}\Big]_0^6=\pi\cdot\frac{216}{12}=18\pi")], r"\(18\pi\)"),
    '3.517': ([(SKIV, r"V=\pi\int_0^3\left(\sqrt{2x}\right)^2dx=\pi\int_0^32x\,dx"),
               ('Bestäm en primitiv funktion och sätt in gränserna', r"\pi\Big[x^2\Big]_0^3=9\pi")], r"\(9\pi\)"),
    # konjugat och räknesätt
    '4.274': delar(
        ('a', [(ABS, r"|3-4i|=\sqrt{3^2+(-4)^2}=\sqrt{25}=5")], "5"),
        ('b', [(KONJ, r"\bar z=3+4i")], r"\(3+4i\)"),
        ('c', [(r"Ett tal gånger sitt konjugat: \(z\bar z=a^2+b^2\)", r"z\bar z=(3-4i)(3+4i)=9+16=25")], "25"),
    ),
    '4.465': ([('Addera realdelarna för sig och imaginärdelarna för sig', r"(3+1)+(2-5)i=4-3i")], r"\(4-3i\)"),
    '4.467': ([('Multiplicera in 3 i båda termerna', r"3(2+i)=6+3i")], r"\(6+3i\)"),
    '4.468': ([(KONJR, r"(1+i)(1-i)=1^2-i^2=1-(-1)=2")], r"\(2\)"),
    '4.469': ([(I2, r"(2+3i)(1+i)=2+2i+3i+3i^2=2+5i-3=-1+5i")], r"\(-1+5i\)"),
    '4.471': ([(ABS, r"|3+4i|=\sqrt{3^2+4^2}=\sqrt{25}=5")], "5"),
    '4.472': ([(KONJ, r"\bar z=5+2i", 'Konjugatet har samma realdel men motsatt tecken på imaginärdelen.')], r"\(5+2i\)"),
    # ekvationen z^n = w
    '4.156': zn(r"e^{i\pi/4}", 8, r"e^{i\cdot8\pi/4}=e^{i2\pi}=1",
                r'Skriv \(1=e^{i2\pi}\). Då ger \(8v=2\pi\) argumentet \(v=\frac{\pi}{4}\), och beloppet är 1.'),
    '4.157': zn(r"e^{i\pi/6}", 6, r"e^{i\cdot6\pi/6}=e^{i\pi}=-1",
                r'Skriv \(-1=e^{i\pi}\). Då ger \(6v=\pi\) argumentet \(v=\frac{\pi}{6}\), och beloppet är 1.'),
    '4.159': zn(r"2e^{i\pi/4}", 4, r"2^4e^{i\pi}=16\cdot(-1)=-16",
                r'Skriv \(-16=16e^{i\pi}\). Beloppet blir \(\sqrt[4]{16}=2\) och \(4v=\pi\) ger \(v=\frac{\pi}{4}\).'),
    '4.158': zn(r"2e^{i2\pi/5}", 5, r"2^5e^{i2\pi}=32",
                r'Skriv \(32=32e^{i2\pi}\). Beloppet blir \(\sqrt[5]{32}=2\) och \(5v=2\pi\) ger \(v=\frac{2\pi}{5}\).'),
    '4.160': zn(r"e^{i2\pi/9}", 9, r"e^{i2\pi}=1",
                r'Skriv \(1=e^{i2\pi}\). Då ger \(9v=2\pi\) argumentet \(v=\frac{2\pi}{9}\), och beloppet är 1.'),
    '4.494': ([(r"Ekvationen \(z^n=w\), \(w\ne0\), har exakt \(n\) komplexa lösningar", r"n=5")], "5"),
    '4.495': ([(ROT, r"z^2=-9\quad\Rightarrow\quad z=\pm\sqrt{-9}=\pm3i"),
               ('Kontrollera roten med positiv imaginärdel', r"(3i)^2=9i^2=-9")], r"\(3i\)"),
    '4.496': ([('Lös som en andragradsekvation i \\(z^2\\)', r"z^4=16\quad\Rightarrow\quad z^2=4\ \text{eller}\ z^2=-4"),
               ('Lös de två ekvationerna', r"z=\pm2\quad\text{eller}\quad z=\pm2i"),
               ('Räkna de reella lösningarna', None, r'Bara \(2\) och \(-2\) är reella.')], "2"),
    '4.594': ([('Lösningarna ligger jämnt fördelade på ett helt varv', r"\frac{360^\circ}{6}=60^\circ")], r"\(60^\circ\)"),
    '4.597': ([(ROT, r"z^2=-9\quad\Rightarrow\quad z=\pm3i"), ('Läs av imaginärdelarna', r"\operatorname{Im}(3i)=3,\quad\operatorname{Im}(-3i)=-3")],
              r"\(-3\) och \(3\)"),
    # andragradsekvationer med komplexa rötter
    '4.401': ([(ROT, r"x^2=-4\quad\Rightarrow\quad x=\pm\sqrt{-4}=\pm2i")], r"\(2i\)"),
    '4.402': ([(PQ, r"x^2-4x+13=0,\quad p=-4,\ q=13:\quad x=2\pm\sqrt{4-13}=2\pm\sqrt{-9}"), (ROT, r"x=2\pm3i"),
               ('Realdelen är talet utan \\(i\\)', None, 'Båda rötterna har realdelen 2.')], "2"),
    '4.499': ([(ROT, r"x^2=-4\quad\Rightarrow\quad x=\pm\sqrt{-4}=\pm2i")], r"\(2i\)"),
    '4.500': ([(PQ, r"x^2-2x+5=0,\quad p=-2,\ q=5:\quad x=1\pm\sqrt{1-5}=1\pm\sqrt{-4}"), (ROT, r"x=1\pm2i")], r"\(1+2i\)"),
    '4.516': ([(PQ, r"z^2-6z+10=0,\quad p=-6,\ q=10:\quad z=3\pm\sqrt{9-10}=3\pm\sqrt{-1}"), (ROT, r"z=3\pm i")], r"\(z=3+i\) eller \(z=3-i\)"),
    '4.554': ([(ROT, r"x^2=-9\quad\Rightarrow\quad x=\pm\sqrt{-9}=\pm3i")], r"\(x=3i\) eller \(x=-3i\)"),
    '4.555': ([(PQ, r"x^2-2x+10=0,\quad p=-2,\ q=10:\quad x=1\pm\sqrt{1-10}=1\pm\sqrt{-9}"), (ROT, r"x=1\pm3i")], r"\(x=1+3i\) eller \(x=1-3i\)"),
    '4.556': ([(PQ, r"x^2+6x+25=0,\quad p=6,\ q=25:\quad x=-3\pm\sqrt{9-25}=-3\pm\sqrt{-16}"), (ROT, r"x=-3\pm4i")], r"\(x=-3+4i\) eller \(x=-3-4i\)"),
    # polynomdivision
    '4.49': (division([("x^2", r"x^2(x-2)=x^3-2x^2", r"4x^2-5x-6"),
                       ("4x", r"4x(x-2)=4x^2-8x", r"3x-6"),
                       ("3", r"3(x-2)=3x-6", r"0")], None) +
             [('Kontrollera genom att multiplicera', r"(x-2)(x^2+4x+3)=x^3+4x^2+3x-2x^2-8x-6=x^3+2x^2-5x-6")], r"\(x^2+4x+3\)"),
    '4.279': delar(
        ('a', [(KONJR, r"\frac{x^2-9}{x-3}=\frac{(x+3)(x-3)}{x-3}=x+3")], r"\(x+3\)"),
        ('b', division([("x^2", r"x^2(x+1)=x^3+x^2", r"-x^2+1"),
                        ("-x", r"-x(x+1)=-x^2-x", r"x+1"),
                        ("1", r"1\cdot(x+1)=x+1", r"0")], None), r"\(x^2-x+1\)"),
        ('c', [('Faktorisera genom att gruppera termerna', r"x^3-3x^2-4x+12=x^2(x-3)-4(x-3)=(x^2-4)(x-3)"),
               ('Förkorta med \\(x-3\\)', r"\frac{(x^2-4)(x-3)}{x-3}=x^2-4")], r"\(x^2-4\)"),
    ),
    '4.312': delar(
        ('a', division([("x^2", r"x^2(x-2)=x^3-2x^2", r"-2x^2+x+6"),
                        ("-2x", r"-2x(x-2)=-2x^2+4x", r"-3x+6"),
                        ("-3", r"-3(x-2)=-3x+6", r"0")], None), r"kvoten \(x^2-2x-3\), rest 0"),
        ('b', division([("2x^2", r"2x^2(x+2)=2x^3+4x^2", r"-3x^2-8x-4"),
                        ("-3x", r"-3x(x+2)=-3x^2-6x", r"-2x-4"),
                        ("-2", r"-2(x+2)=-2x-4", r"0")], None), r"kvoten \(2x^2-3x-2\), rest 0"),
    ),
    '4.454': ([(REST, r"P(2)=2\cdot2^3-3\cdot2+5=16-6+5=15")], "15"),
    '4.501': ([(KONJR, r"\frac{x^2-1}{x-1}=\frac{(x+1)(x-1)}{x-1}=x+1")], r"\(x+1\)"),
    '4.502': (division([("x^2", r"x^2(x-2)=x^3-2x^2", r"2x^2-8"),
                        ("2x", r"2x(x-2)=2x^2-4x", r"4x-8"),
                        ("4", r"4(x-2)=4x-8", r"0")], None), r"\(x^2+2x+4\)"),
    '4.503': ([(REST, r"p(1)=1^2+3\cdot1+1=5")], "5"),
    '4.527': ([(REST, r"x+2=x-(-2):\quad p(-2)=(-2)^4-3\cdot(-2)+5=16+6+5=27")], "27"),
}
