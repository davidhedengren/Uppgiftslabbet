# Ma4 sista korta facit: kurvor, asymptoter, areor, produkt- och kvotregeln, Euler, imaginära tal m.m.
# Facit enligt FACITMALL (2026-11-22).
SINMAX = r"Sinus och cosinus varierar mellan \(-1\) och \(1\)"
PROD = r"Produktregeln: \(D(f\cdot g)=f'g+fg'\)"
KVOT = r"Kvotregeln: \(D\frac fg=\frac{f'g-fg'}{g^2}\)"
AREA = r"Arean under kurvan: \(A=\int_a^bf(x)\,dx\) när \(f(x)\ge0\)"
INT = r"Integralens värde: \(\int_a^bf(x)\,dx=F(b)-F(a)\)"
LOD = 'En lodrät asymptot finns där nämnaren är 0 men täljaren inte är det'
EULER = r"Eulers formel: \(e^{iv}=\cos v+i\sin v\)"
ABS = r"Absolutbeloppet: \(|a+bi|=\sqrt{a^2+b^2}\)"
DERIV = 'Ändringstakten är derivatan'


def delar(*d):
    huvud, svar, ut = [], [], {}
    for et, steg, s in d:
        ut[et] = (steg, s)
        huvud.append((f'{et}) ' + steg[0][0],) + tuple(steg[0][1:]))
        huvud.extend(steg[1:])
        svar.append(f'{et}) {s}')
    ut[''] = (huvud, ' '.join(svar))
    return ut


F = {
    '1.402': ([(r"Cosinus är 1 bara när vinkeln är ett helt antal varv", r"\cos x=1\quad\Rightarrow\quad x=0^\circ+n\cdot360^\circ"),
               (r"Välj lösningarna i \(0\le x<360^\circ\)", None, r'Bara \(x=0^\circ\) ligger i intervallet, eftersom \(360^\circ\) inte ingår.')], "1"),
    '1.584': ([(r"Amplituden i \(y=A\sin x\) är \(|A|\)", r"A=3")], "3"),
    '1.585': ([('Sinus upprepar sig efter ett helt varv', r"T=360^\circ")], r"\(360^\circ\)"),
    '1.586': ([(SINMAX, r"y_{\max}=2\cdot1+1=3")], "3"),
    '1.587': ([(SINMAX, r"y_{\min}=4\cdot(-1)-1=-5")], r"\(-5\)"),
    '1.685': ([(SINMAX, None, r'Arean \(T=12\sin v\) blir störst när \(\sin v\) är störst.'),
               (r"\(\sin v=1\) när \(v=90^\circ\)", r"T_{\max}=12\cdot1=12\ \text{m}^2")], r"\(90^\circ\)"),
    '1.686': ([('Sätt in värdena i formeln', r"R=\frac{20^2\cdot\sin(2\cdot30^\circ)}{9{,}82}=\frac{400\sin60^\circ}{9{,}82}"),
               ('Beräkna', r"R\approx\frac{346{,}4}{9{,}82}\approx35{,}3")], "35,3 m"),
    '2.153': delar(
        ('a', [(PROD, None, r'\(x^2e^x\) är en produkt av \(x^2\) och \(e^x\).')], "A (produktregeln)"),
        ('b', [(KVOT, None, r'\(\frac{\ln x}{x}\) är en kvot med \(\ln x\) i täljaren och \(x\) i nämnaren.')], "B (kvotregeln)"),
        ('c', [(r"Kedjeregeln: \(D\,f(g(x))=f'(g(x))\cdot g'(x)\)", None, r'Funktionen \(x^2\) ligger inuti sinus.')], "C (kedjeregeln)"),
    ),
    '2.216': ([(PROD, r"f'(x)=2x\cdot e^x+x^2\cdot e^x"), ('Bryt ut \\(e^x\\)', r"f'(x)=e^x(x^2+2x)")], r"\(f'(x)=e^x(x^2+2x)\)"),
    '2.411': ([(PROD, r"f'(x)=2xe^x+x^2e^x"), (r"Sätt in \(x=1\)", r"f'(1)=2e+e=3e\approx8{,}15")], r"\(3e\approx8{,}15\)"),
    '2.504': ([('Multiplicera in först', r"f(x)=x^3+x^2"), (r"Derivera term för term: \(D\,x^n=nx^{n-1}\)", r"f'(x)=3x^2+2x")], r"\(f'(x)=3x^2+2x\)"),
    '2.505': ([(KVOT, r"f'(x)=\frac{1\cdot(x+1)-x\cdot1}{(x+1)^2}"), ('Förenkla täljaren', r"f'(x)=\frac{1}{(x+1)^2}")], r"\(f'(x)=\frac{1}{(x+1)^2}\)"),
    '2.516': ([(r"Derivatan av \(\sin x\) är \(\cos x\)", r"f'(x)=\cos x")], r"\(f'(x)=\cos x\)"),
    '2.517': ([(r"Derivatan av \(\cos x\) är \(-\sin x\)", r"f'(x)=-\sin x")], r"\(f'(x)=-\sin x\)"),
    '2.523': ([('Hastigheten är derivatan av sträckan', r"s'(t)=10t"), (r"Sätt in \(t=3\)", r"s'(3)=10\cdot3=30")], "30 m/s"),
    '2.526': ([(DERIV, r"h'(t)=0{,}3-0{,}02t"), (r"Sätt in \(t=5\)", r"h'(5)=0{,}3-0{,}1=0{,}2")], "0,2 m/h"),
    '2.527': ([('Marginalkostnaden är derivatan av kostnaden', r"K'(x)=20+0{,}2x"), (r"Sätt in \(x=50\)", r"K'(50)=20+10=30")], "30 kr per produkt"),
    '2.531': ([(LOD, r"x-3=0\quad\Rightarrow\quad x=3")], r"\(x=3\)"),
    '2.532': ([(LOD, r"x+2=0\quad\Rightarrow\quad x=-2")], r"\(x=-2\)"),
    '2.533': ([(r"\(\frac1x\to0\) när \(x\to\pm\infty\)", r"f(x)=2+\frac1x\to2")], r"\(y=2\)"),
    '2.535': ([(r"Skriv om: \(e^{-x}=\frac{1}{e^x}\)", r"\frac{1}{e^x}\to0\quad\text{när }x\to\infty")], r"\(y=0\)"),
    '2.536': ([(r"\(\frac1x\to0\) när \(x\to\pm\infty\)", None, r'Kvar blir den linjära delen, så grafen närmar sig \(y=x+1\).')], r"\(y=x+1\)"),
    '2.597': ([(r"Amplituden i \(y=a\sin x\) är \(|a|\)", None, r'Läs av största värdet i figuren: 2,5 vid \(x=90^\circ\).'),
               (r"Vid \(x=90^\circ\) är \(\sin x=1\)", r"2{,}5=a\cdot1\quad\Rightarrow\quad a=2{,}5")], r"\(a=2{,}5\)"),
    '2.607': ([(r"Sätt in punkten \((45^\circ,\,3)\)", r"3=a\tan45^\circ"), (r"Använd \(\tan45^\circ=1\)", r"3=a\cdot1\quad\Rightarrow\quad a=3")], r"\(a=3\)"),
    # areor
    '3.414': ([(AREA, r"A=\int_0^4x\,dx"), (INT, r"\Big[\frac{x^2}{2}\Big]_0^4=8")], "8 areaenheter"),
    '3.80': ([('Linjen skär x-axeln där \\(2-x=0\\)', r"x=2"), (AREA, r"A=\int_0^2(2-x)\,dx"),
              (INT, r"\Big[2x-\frac{x^2}{2}\Big]_0^2=4-2=2")], "2 areaenheter"),
    '3.418': ([('Kurvan skär x-axeln där \\(4-x^2=0\\)', r"x=\pm2"), (AREA, r"A=\int_{-2}^2(4-x^2)\,dx"),
               (INT, r"\Big[4x-\frac{x^3}{3}\Big]_{-2}^2=\left(8-\frac83\right)-\left(-8+\frac83\right)=\frac{32}{3}")], r"\(\frac{32}{3}\) areaenheter"),
    '3.191': ([(AREA, r"A=\int_0^23x^2\,dx"), (INT, r"\Big[x^3\Big]_0^2=8")], "8 areaenheter"),
    '3.404': ([(AREA, r"\int_0^2ax\,dx=a\Big[\frac{x^2}{2}\Big]_0^2=2a"), ('Sätt arean lika med 4', r"2a=4\quad\Rightarrow\quad a=2")], r"\(a=2\)"),
    '3.405': ([(AREA, r"\int_0^3kx\,dx=k\Big[\frac{x^2}{2}\Big]_0^3=\frac{9k}{2}"), ('Sätt arean lika med 9', r"\frac{9k}{2}=9\quad\Rightarrow\quad k=2")], r"\(k=2\)"),
    '3.488': ([(AREA, r"A=\int_1^53\,dx=3\cdot(5-1)=12"), ('Kontroll: området är en rektangel', r"3\cdot4=12")], "12 areaenheter"),
    '3.489': ([(AREA, r"A=\int_0^2(2x+1)\,dx"), (INT, r"\Big[x^2+x\Big]_0^2=4+2=6")], "6 areaenheter"),
    '3.490': ([(AREA, r"A=\int_0^3x^2\,dx"), (INT, r"\Big[\frac{x^3}{3}\Big]_0^3=9")], "9 areaenheter"),
    '3.492': ([(AREA, r"A=\int_0^1e^x\,dx"), (r"En primitiv funktion till \(e^x\) är \(e^x\)", r"\Big[e^x\Big]_0^1=e-1")], r"\(e-1\) areaenheter"),
    # komplexa tal
    '4.466': ([('Definitionen av den imaginära enheten', r"i^2=-1")], r"\(-1\)"),
    '4.470': ([(r"Realdelen av \(a+bi\) är \(a\)", r"\operatorname{Re}(7-4i)=7")], "7"),
    '4.308': delar(
        ('a', [(r"Realdelen av \(a+bi\) är \(a\)", r"\operatorname{Re}z=-4")], r"\(-4\)"),
        ('b', [(r"Imaginärdelen av \(a+bi\) är \(b\)", r"\operatorname{Im}z=3")], "3"),
        ('c', [(ABS, r"|z|=\sqrt{(-4)^2+3^2}=\sqrt{25}=5")], "5"),
        ('d', [(r"Konjugatet: \(\overline{a+bi}=a-bi\)", r"\overline z=-4-3i")], r"\(-4-3i\)"),
    ),
    '4.476': ([(r"\(|z|\) är avståndet från origo till punkten \(z\)", None, r'Alla punkter på avståndet 3 från origo bildar en cirkel med radien 3.')], "3"),
    '4.585': ([(r"Cirkel i talplanet: \(|z-z_0|=r\) har medelpunkt \(z_0\) och radie \(r\)", None),
               ('Skriv om villkoret på den formen', r"|z+1-2i|=|z-(-1+2i)|=4"),
               ('Läs av medelpunkt och radie', r"z_0=-1+2i,\quad r=4")], r"realdel \(-1\), imaginärdel 2, radie 4"),
    '4.588': ([('Pröva båda villkoren för varje punkt', None, r'Punkten måste ha realdel större än 1 och imaginärdel mindre än 2.'),
               (r"Kontrollera \(3+i\)", r"\operatorname{Re}=3>1,\quad\operatorname{Im}=1<2")], r"A, \(3+i\)"),
    '4.407': ([(EULER, r"e^{i\pi/3}=\cos\frac\pi3+i\sin\frac\pi3"), ('Realdelen är cosinusvärdet', r"\cos\frac\pi3=\frac12")], r"\(\frac12\)"),
    '4.411': ([(EULER, r"e^{i3\pi/2}=\cos\frac{3\pi}2+i\sin\frac{3\pi}2"), ('Imaginärdelen är sinusvärdet', r"\sin\frac{3\pi}2=-1")], r"\(-1\)"),
    '4.488': ([(EULER, r"e^{i\pi}=\cos\pi+i\sin\pi=-1+0i=-1")], r"\(-1\)"),
    '4.403': ([(r"\(x=2\) är en rot, så \(x-2\) är en faktor", r"x^3-8=(x-2)(x^2+2x+4)"),
               (r"pq-formeln: \(x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}\)", r"x^2+2x+4=0:\quad x=-1\pm\sqrt{1-4}=-1\pm i\sqrt3"),
               ('Räkna de icke-reella rötterna', None, r'\(-1+i\sqrt3\) och \(-1-i\sqrt3\) är icke-reella.')], "2"),
    '4.606': ([('Varje rot \\(r\\) ger en faktor \\(x-r\\)', r"p(x)=(x-2)(x-i)(x+i)"),
               (r"Konjugatregeln och \(i^2=-1\)", r"(x-i)(x+i)=x^2+1"),
               ('Multiplicera ut', r"p(x)=(x-2)(x^2+1)=x^3-2x^2+x-2")], r"\(d=-2\)"),
}
