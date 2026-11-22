# Ma4 exp/log-derivator, derivata i problemlösning, komplexa tal i talplanet, polär form, de Moivre och faktorsatsen:
# facit enligt FACITMALL (2026-11-22).
KED = r"Kedjeregeln: \(D\,f(g(x))=f'(g(x))\cdot g'(x)\)"
LN = r"Derivatan av \(\ln x\) är \(\frac1x\)"
LNU = r"Kedjeregeln med \(D\ln u=\frac{u'}{u}\)"
EXP = r"Derivatan av \(e^{kx}\) är \(ke^{kx}\)"
SIN = r"Derivatan av \(\sin kx\) är \(k\cos kx\)"
COS = r"Derivatan av \(\cos kx\) är \(-k\sin kx\)"
POT = r"Derivatan av en potens: \(D\,x^n=nx^{n-1}\)"
EXTR = r"Största eller minsta värdet finns där \(f'(x)=0\)"
ROTI = r"Multiplikation med \(i\): \(i(a+bi)=ai+bi^2=-b+ai\)"
PUNKT = r"Punkten \((a,b)\) motsvarar talet \(a+bi\)"
ABS = r"Absolutbeloppet: \(|a+bi|=\sqrt{a^2+b^2}\)"
AVST = r"Avståndet mellan två tal: \(|z_1-z_2|\)"
POLAR = r"Polär form: \(r(\cos v+i\sin v)=r\cos v+i\,r\sin v\)"
MULT = r"Multiplikation i polär form: belopp multipliceras, argument adderas"
DM = r"De Moivres formel: \(\left(re^{iv}\right)^n=r^ne^{inv}\)"
FAKT = r"Faktorsatsen: \(x=a\) är ett nollställe precis när \(x-a\) är en faktor, det vill säga \(p(a)=0\)"
PQ = r"pq-formeln: \(x=-\frac p2\pm\sqrt{\left(\frac p2\right)^2-q}\)"


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
    # exp och log
    '2.218': ([(LNU, None, r'Inre funktionen är \(u=1+x^2\) med \(u\'=2x\).'),
               ('Sätt in i regeln', r"f'(x)=\frac{2x}{1+x^2}")], r"\(f'(x)=\frac{2x}{1+x^2}\)"),
    '2.215': delar(
        ('a', [(EXP, r"D\,e^{4x}=4e^{4x}")], r"\(4e^{4x}\)"),
        ('b', [(LNU, r"D\ln(3x+1)=\frac{3}{3x+1}")], r"\(\frac{3}{3x+1}\)"),
        ('c', [(SIN, r"D\sin5x=5\cos5x")], r"\(5\cos5x\)"),
        ('d', [(COS, r"D\cos2x=-2\sin2x")], r"\(-2\sin2x\)"),
    ),
    '2.515': ([(LN, r"f'(x)=\frac1x")], r"\(f'(x)=\frac1x\)"),
    '2.519': ([(r"Logaritmlagen \(\ln x^2=2\ln x\) när \(x>0\)", r"f(x)=2\ln x"), (LN, r"f'(x)=2\cdot\frac1x=\frac2x")], r"\(f'(x)=\frac2x\)"),
    '2.520': ([(r"Derivatan av \(a^x\) är \(a^x\ln a\)", r"f'(x)=2^x\ln2")], r"\(f'(x)=2^x\ln2\)"),
    '2.522': ([(r"Derivatan av \(e^x\) är \(e^x\)", r"f'(x)=e^x"), (r"Sätt in \(x=0\)", r"f'(0)=e^0=1")], "1"),
    # derivata i problemlösning
    '2.405': ([('Tangenten skär x-axeln där \\(y=0\\)', r"0=x+1\quad\Rightarrow\quad x=-1")], r"\(-1\)"),
    '2.406': ([(LN, r"y'=\frac1x"), (r"Tangentens lutning vid \(x=e\) är \(y'(e)\)", r"y'(e)=\frac1e\approx0{,}368")], r"\(\frac1e\approx0{,}368\)"),
    '2.524': ([(POT, r"y'=2x"), (r"Tangentens lutning vid \(x=3\) är \(y'(3)\)", r"y'(3)=2\cdot3=6")], "6"),
    '2.528': ([(EXTR, r"f'(x)=-2x+8=0\quad\Rightarrow\quad x=4"),
               ('Grafen är en parabel som vänder nedåt, så det är ett maximum', r"f(4)=-4^2+8\cdot4=-16+32=16")], "16"),
    '2.530': ([('Bollen är som högst när höjden slutar öka, det vill säga när \\(h\'(t)=0\\)', r"h'(t)=12-10t"),
               ('Lös ekvationen', r"12-10t=0\quad\Rightarrow\quad t=1{,}2")], "1,2 s"),
    # multiplikation och division i polär form, talplanet
    '4.42': delar(
        ('a', [(ROTI, r"i(3+2i)=3i+2i^2=-2+3i")], r"\(-2+3i\)"),
        ('b', [(ROTI, r"i(-4+i)=-4i+i^2=-1-4i")], r"\(-1-4i\)"),
        ('c', [(ROTI, r"i(2-5i)=2i-5i^2=5+2i")], r"\(5+2i\)"),
        ('d', [(ROTI, r"i(-1-3i)=-i-3i^2=3-i")], r"\(3-i\)"),
    ),
    '4.219': ([(PUNKT, None, 'x-koordinaten blir realdel och y-koordinaten imaginärdel.'),
               ('Skriv punkterna som tal', r"A=2-3i,\quad B=-4+i,\quad C=0+5i=5i")], r"A: \(2-3i\), B: \(-4+i\), C: \(5i\)"),
    '4.412': ([('Multiplicera ut och använd \\(i^2=-1\\)', r"w=-i(2+3i)=-2i-3i^2=3-2i"), ('Realdelen är talet utan \\(i\\)', None)], "3"),
    '4.479': ([(ROTI, r"i(2+i)=2i+i^2=-1+2i")], r"\(-1+2i\)"),
    '4.485': ([(MULT, r"|z_1z_2|=|z_1|\cdot|z_2|=2\cdot3=6")], "6"),
    '4.486': ([(MULT, r"\arg(z_1z_2)=20^\circ+40^\circ=60^\circ")], r"\(60^\circ\)"),
    # komplexa tal som vektorer
    '4.473': ([(PUNKT, r"(2,-3)\ \leftrightarrow\ 2-3i")], r"\(2-3i\)"),
    '4.474': ([(PUNKT, r"-1+4i\ \leftrightarrow\ (-1,4)"),
               ('Negativ realdel och positiv imaginärdel ger andra kvadranten', None)], "andra kvadranten (2)"),
    '4.475': ([(ABS, r"|6+8i|=\sqrt{6^2+8^2}=\sqrt{100}=10")], "10"),
    '4.477': ([(AVST, r"(4+5i)-(1+i)=3+4i"), (ABS, r"|3+4i|=\sqrt{9+16}=5")], "5"),
    '4.480': ([(r"Mittpunkten: \(\frac{z_1+z_2}{2}\)", r"\frac{(2+4i)+(6-2i)}{2}=\frac{8+2i}{2}=4+i")], r"\(4+i\)"),
    '4.522': ([(AVST, r"z_1-z_2=(2+5i)-(-1+i)=3+4i"), (ABS, r"|3+4i|=\sqrt{9+16}=5")], "5"),
    # polär form
    '4.39': delar(
        ('a', [(POLAR, r"2(\cos0+i\sin0)=2(1+0i)=2")], "2"),
        ('b', [(POLAR, r"4\left(\cos\frac\pi2+i\sin\frac\pi2\right)=4(0+i)=4i")], r"\(4i\)"),
        ('c', [(POLAR, r"6(\cos\pi+i\sin\pi)=6(-1+0i)=-6")], r"\(-6\)"),
        ('d', [(POLAR, r"2\sqrt2\left(\frac{\sqrt2}{2}-i\frac{\sqrt2}{2}\right)=2-2i")], r"\(2-2i\)"),
    ),
    '4.309': delar(
        ('a', [(POLAR, r"2(\cos0+i\sin0)=2(1+0i)=2")], "2"),
        ('b', [(POLAR, r"4\left(\cos\frac\pi2+i\sin\frac\pi2\right)=4(0+i)=4i")], r"\(4i\)"),
        ('c', [(POLAR, r"2(\cos\pi+i\sin\pi)=2(-1+0i)=-2")], r"\(-2\)"),
        ('d', [(POLAR, r"6\left(\cos\frac{3\pi}2+i\sin\frac{3\pi}2\right)=6(0-i)=-6i")], r"\(-6i\)"),
    ),
    '4.481': ([(r"I polär form \(r(\cos v+i\sin v)\) är \(r\) absolutbeloppet", r"r=2")], "2"),
    '4.482': ([(r"I polär form \(r(\cos v+i\sin v)\) är \(v\) argumentet", r"v=30^\circ")], r"\(30^\circ\)"),
    '4.487': ([(POLAR, r"4(\cos90^\circ+i\sin90^\circ)=4(0+i\cdot1)=4i")], r"\(4i\)"),
    # de Moivre och potenser av i
    '4.277': ([(DM, r"\left(2e^{i\pi/4}\right)^3=2^3e^{i\cdot3\pi/4}=8e^{i3\pi/4}")], r"\(8e^{i3\pi/4}\)"),
    '4.489': ([(r"Använd \(i^2=-1\)", r"i^3=i^2\cdot i=-i")], r"\(-i\)"),
    '4.490': ([(r"Använd \(i^2=-1\)", r"i^4=\left(i^2\right)^2=(-1)^2=1")], "1"),
    '4.491': ([(r"Kvadreringsregeln och \(i^2=-1\)", r"(1+i)^2=1+2i+i^2=1+2i-1=2i")], r"\(2i\)"),
    '4.492': ([(r"De Moivres formel: \(|z^n|=|z|^n\)", r"|z^2|=2^2=4")], "4"),
    '4.611': ([(ABS, r"|1+2i|=\sqrt{1^2+2^2}=\sqrt5"),
               (r"De Moivres formel: \(|z^n|=|z|^n\)", r"|(1+2i)^5|=\left(\sqrt5\right)^5=25\sqrt5\approx55{,}9")], r"\(55{,}9\)"),
    # faktorsatsen
    '4.280': ([(FAKT, None, r'Eftersom \(x=2\) är ett nollställe är \(x-2\) en faktor. Dividera med den.'),
               (r"Nästa term i kvoten är \(x^2\)", r"x^2(x-2)=x^3-2x^2\quad\Rightarrow\quad\text{kvar: }-3x^2+2x+8"),
               (r"Nästa term i kvoten är \(-3x\)", r"-3x(x-2)=-3x^2+6x\quad\Rightarrow\quad\text{kvar: }-4x+8"),
               (r"Nästa term i kvoten är \(-4\)", r"-4(x-2)=-4x+8\quad\Rightarrow\quad\text{kvar: }0"),
               (PQ, r"x^2-3x-4=0:\quad x=\frac32\pm\sqrt{\frac94+4}=\frac32\pm\frac52"),
               ('Rötterna 4 och \\(-1\\) ger faktorerna', r"x^2-3x-4=(x-4)(x+1)")], r"\((x-2)(x-4)(x+1)\)"),
    '4.464': ([(FAKT, r"P(-2)=(-2)^2+k(-2)+6=10-2k"), ('Sätt uttrycket lika med 0', r"10-2k=0\quad\Rightarrow\quad k=5")], r"\(k=5\)"),
    '4.497': ([(r"Sätt in \(x=1\)", r"p(1)=1^3-2\cdot1+1=0"), (FAKT, None, r'Eftersom \(p(1)=0\) är \(x=1\) ett nollställe.')], "0"),
    '4.498': ([(PQ, r"x=\frac52\pm\sqrt{\frac{25}{4}-6}=\frac52\pm\frac12"), ('De två rötterna', r"x_1=2,\quad x_2=3")], "3"),
    '4.618': ([('Grafen skär y-axeln där \\(x=0\\)', r"p(0)=k\cdot3\cdot(-1)\cdot(-2)=6k"),
               ('Sätt värdet lika med 12', r"6k=12\quad\Rightarrow\quad k=2")], "2"),
    '4.619': ([(FAKT, r"p(-1)=(-1)^4+a(-1)+3=4-a"), ('Sätt uttrycket lika med 0', r"4-a=0\quad\Rightarrow\quad a=4")], r"\(a=4\)"),
}
