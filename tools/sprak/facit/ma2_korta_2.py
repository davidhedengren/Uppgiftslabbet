# Ma2 korta facit, del 2: funktioner och modeller, ekvationssystem, geometri (2026-11-22).
import os
exec(open(os.path.join('tools', 'sprak', 'facit', 'ma2_korta_gemensamt.py'), encoding='utf-8').read())
LIKF = r"Likformighet: motsvarande sidor har samma längdskala \(k=\frac{\text{stor}}{\text{liten}}\)"
AREASK = r"Areaskala: areor ändras med kvadraten på längdskalan, \(k^2\)"
KORDA = r"Kordasatsen: \(a\cdot b=c\cdot d\) för delsträckorna på två kordor som skär varandra"
PYTH = r"Pythagoras sats: \(c^2=a^2+b^2\)"
MITT = r"Mittpunktsformeln: \(\left(\frac{x_1+x_2}{2},\,\frac{y_1+y_2}{2}\right)\)"
AVST = r"Avståndsformeln: \(d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\)"
RAND = 'Randvinkelsatsen: medelpunktsvinkeln är dubbelt så stor som randvinkeln på samma båge'
TRI = 'Vinkelsumman i en triangel är 180°'
DIFF1 = 'Konstant skillnad mellan på varandra följande y-värden betyder linjär modell'
KVOT1 = 'Konstant kvot mellan på varandra följande y-värden betyder exponentiell modell'
FFAKT = r"Förändringsfaktor: \(1+\text{ökning}\) eller \(1-\text{minskning}\) i decimalform"
POTF = r"Potensfunktion: när \(x\) multipliceras med 2 multipliceras \(Cx^n\) med \(2^n\)"

F = {
    # funktioner, grafer och modeller
    '2.569': ett(r"Rektangelns area: \(A=\text{längd}\cdot\text{bredd}\)", r"A=x(x+3)", r"\(A=x(x+3)\)"),
    '2.571': mc('Nollställena är där grafen skär x-axeln', 'Läs av skärningspunkterna i figuren: x = 1 och x = 5.', r"\(x=1\) och \(x=5\)"),
    '2.572': ett(r"Varje nollställe \(a\) ger en faktor \(x-a\)", r"f(x)=(x-1)(x-5)", r"\(f(x)=(x-1)(x-5)\)"),
    '2.573': ett(FUNK, r"f(3)=2\cdot3^3=2\cdot27=54", "54"),
    '2.606': ett(FUNK, r"y=3\cdot4^2=3\cdot16=48", "48"),
    '2.589': ett(FUNK, r"f(2)=3\cdot2+4=10", "10"),
    '2.599': ett(FUNK, r"V(2)=200\cdot1{,}1^2=200\cdot1{,}21=242", "242"),
    '2.574': ett(POTF, r"2^2=4", "faktorn 4"),
    '2.595': ([(r"Sätt in \(2x\) i stället för \(x\)", r"f(2x)=(2x)^2=4x^2"), ('Jämför med \\(f(x)=x^2\\)', r"f(2x)=4\cdot f(x)")], "4 gånger"),
    '2.577': mc(r"Exponentialfunktion: \(f(x)=C\cdot a^x\), med \(x\) i exponenten", r'I \(3\cdot1{,}2^x\) står \(x\) i exponenten.', 'Exponentialfunktion'),
    '2.594': mc(r"Exponentialfunktion: \(f(x)=C\cdot a^x\), med \(x\) i exponenten", r'I \(3\cdot2^x\) står \(x\) i exponenten. I \(3x^2\) står \(x\) i basen, så det är en potensfunktion.', 'B'),
    '2.578': ett(r"Startvärdet är \(f(0)\)", r"f(0)=7\cdot1{,}3^0=7", "7"),
    '2.580': mc(r"Startvärdet är \(f(0)\)", 'Läs av var grafen skär y-axeln: y = 4.', "4"),
    '2.579': mc('Förändringsfaktor mellan 0 och 1 ger en avtagande funktion', r'\(0<0{,}75<1\), så värdet minskar i varje steg.', 'Avtagande'),
    '2.596': ett(FFAKT, r"1{,}06=1+0{,}06", "6 %"),
    '2.597': ett(FFAKT, r"1+0{,}20=1{,}20", "1,20"),
    '2.598': ett(FFAKT, r"1-0{,}15=0{,}85", "0,85"),
    '2.581': mc(r"I \(y=kx+m\) anger \(k\) hur mycket \(y\) ökar när \(x\) ökar med 1", r'Här är \(k=2{,}4\).', "2,4"),
    '2.582': ett(DIFF1, r"8-5=11-8=14-11=17-14=3", 'Linjär'),
    '2.613': ett(DIFF1, r"11-7=15-11=19-15=4", 'Linjär modell'),
    '2.583': ett(KVOT1, r"\frac{15}{10}=\frac{22{,}5}{15}=\frac{33{,}75}{22{,}5}=1{,}5", 'Exponentiell'),
    '2.600': ett('Konstanta andra differenser betyder andragradsmodell', r"6-4=8-6=10-8=2", 'Andragrad'),
    '2.590': mc(r"\(f(a)=b\) betyder att funktionsvärdet är \(b\) när \(x=a\)", r'Punkten \((4,9)\) ligger på grafen.', 'När x = 4 är funktionsvärdet 9.'),
    '2.591': mc('Läs av i tabellen', r'I kolumnen där x = 3 står funktionsvärdet 8.', r"\(f(3)=8\)"),
    '2.592': ([('Sätt funktionsuttrycket lika med 9', r"2x+1=9"), (r"Lös ut \(x\)", r"2x=8\quad\Rightarrow\quad x=4")], r"\(x=4\)"),
    '2.593': ([(r"Beräkna den inre funktionen \(g(2)\) först", r"g(2)=2\cdot2=4"), (r"Sätt in resultatet i \(f\)", r"f(4)=4+3=7")], "7"),
    '2.723': ([('Sätt in punkten \\((2,15)\\) i funktionen', r"a\cdot2^2+3=15"), (r"Lös ut \(a\)", r"4a=12\quad\Rightarrow\quad a=3")], r"\(a=3\)"),
    '2.724': ([('Nollställen: sätt \\(f(x)=0\\)', r"-x^2+c=0\quad\Rightarrow\quad x^2=c"),
               (r"\(x^2=c\) har två lösningar \(x=\pm\sqrt c\) när \(c\) är positivt", None, r'Om \(c=0\) finns en lösning och om \(c<0\) ingen.')], r"\(c>0\)"),
    # kvadratkomplettering och andragradsekvationer
    '2.584': ett(KK, r"x^2+6x+10=(x+3)^2-9+10=(x+3)^2+1", r"\((x+3)^2+1\)"),
    '2.585': ett(r"En kvadrat är aldrig negativ: \((x-4)^2\ge0\)", r"f(x)\ge0+2=2\quad\text{med likhet när }x=4", "2"),
    '2.612': ett(SYM, r"x=\frac{1+7}{2}=4", r"\(x=4\)"),
    '2.609': ett(NOLL, r"x=0\quad\text{eller}\quad x-6=0\ \Rightarrow\ x=6", lika(0, 6)),
    '2.610': ([('Varje rot \\(r\\) ger en faktor \\(x-r\\)', r"(x-2)(x-5)=0"), (MULT, r"x^2-5x-2x+10=x^2-7x+10")], r"\(x^2-7x+10=0\)"),
    '2.766': ([(PQ, r"x^2+6x+5=0,\quad p=6,\ q=5"), ('Sätt in', r"x=-3\pm\sqrt{9-5}=-3\pm2")], lika(-1, -5)),
    '2.719': ett(r"Rötternas summa: \(x_1+x_2=-p\) för \(x^2+px+q=0\)", r"p=-9\quad\Rightarrow\quad x_1+x_2=9", "9"),
    '2.720': ([(r"Rötternas produkt: \(x_1\cdot x_2=q\) för \(x^2+px+q=0\)", r"3\cdot x_2=12"), ('Lös ut den andra roten', r"x_2=\frac{12}{3}=4")], r"\(x=4\)"),
    # potens-, exponential- och rotekvationer
    '2.575': ett(KUBROT, r"x=\sqrt[3]{64}=4", r"\(x=4\)"),
    '2.576': ett(SAMBAS, r"2^x=8=2^3\quad\Rightarrow\quad x=3", r"\(x=3\)"),
    '2.586': ett(SAMBAS, r"2^x=32=2^5\quad\Rightarrow\quad x=5", r"\(x=5\)"),
    '2.611': ett(SAMBAS, r"3^x=27=3^3\quad\Rightarrow\quad x=3", r"\(x=3\)"),
    '2.588': ett(SAMBAS, r"10^x=1\,000=10^3\quad\Rightarrow\quad x=3", r"\(x=3\)"),
    '2.587': ([('Dela båda leden med 100', r"1{,}05^t=1{,}5"), (r"Logaritmera båda leden: \(\lg a^t=t\lg a\)", r"t\lg1{,}05=\lg1{,}5"),
               (r"Lös ut \(t\)", r"t=\frac{\lg1{,}5}{\lg1{,}05}\approx8{,}3")], r"\(t\approx8{,}3\)"),
    '2.763': ([(r"Logaritmera båda leden: \(\lg a^x=x\lg a\)", r"x\lg3=\lg12"), (r"Lös ut \(x\)", r"x=\frac{\lg12}{\lg3}")], r"\(x=\frac{\lg12}{\lg3}\)"),
    '2.604': ([(r"Kvadrera båda leden: \(\left(\sqrt a\right)^2=a\)", r"x+7=16"), (r"Lös ut \(x\)", r"x=9"),
               ('Kontrollera i ursprungsekvationen', r"\sqrt{9+7}=\sqrt{16}=4")], r"\(x=9\)"),
    # potenser och logaritmer
    '2.607': ett(POTD, r"\frac{x^9}{x^4}=x^{9-4}=x^5", r"\(x^5\)"),
    '2.681': ett(r"Potenslagarna: \(a^m\cdot a^n=a^{m+n}\) och \(\frac{a^m}{a^n}=a^{m-n}\)", r"x^{5/2+3/2-3}=x^{4-3}=x", r"\(x\)"),
    '2.725': ett(r"Potens med bråkexponent: \(a^{m/n}=\left(\sqrt[n]a\right)^m\)", r"8^{2/3}=\left(\sqrt[3]8\right)^2=2^2=4", "4"),
    '2.726': ett(r"Negativ exponent: \(a^{-n}=\frac{1}{a^n}\)", r"2^{-3}\cdot16=\frac{16}{2^3}=\frac{16}{8}=2", "2"),
    '2.602': ett(LGP, r"\lg4+\lg25=\lg(4\cdot25)=\lg100=2", "2"),
    '2.603': ett(LG, r"\lg x=3\quad\Rightarrow\quad x=10^3=1\,000", r"\(x=1\,000\)"),
    '2.696': ([('Skriv om argumentet så att \\(5a\\) syns', r"500a=100\cdot5a"), (LGP, r"\lg(500a)=\lg100+\lg(5a)=2+4=6")], "6"),
    '2.765': ([(r"Skriv roten som en potens av 10", r"\sqrt{1\,000}=\left(10^3\right)^{1/2}=10^{3/2}"), (LGINV, r"\lg10^{3/2}=\frac32=1{,}5")], "1,5"),
    # ekvationssystem och linjer
    '1.674': ([(KONJ, r"(x-4)(x+4)=x^2-16"), ('Dra bort 16', r"x^2-16-16=x^2-32")], r"\(x^2-32\)"),
    '1.316': ett('På x-axeln är y = 0', r"0=3x-6\quad\Rightarrow\quad x=2", r"\(x=2\)"),
    '1.318': ([(r"Sätt in \(x=2\) i den första ekvationen", r"y=3\cdot2-1=5"), ('Sätt in x och y i den andra ekvationen', r"k=2\cdot2+5=9")], r"\(k=9\)"),
    '1.320': ([('Substitutionsmetoden: sätt de två uttrycken för y lika', r"2x+3=2x+b\quad\Rightarrow\quad3=b"),
               ('Samma linje ger oändligt många lösningar', None, 'När b = 3 är ekvationerna identiska. För andra b är linjerna parallella och saknar skärningspunkt.')], r"\(b=3\)"),
    '1.324': ([('Oändligt många lösningar: ekvationerna beskriver samma linje', None, 'Vänsterledet i den andra ekvationen är det första gånger 2.'),
               ('Multiplicera den första ekvationen med 2', r"4x-2y=6\quad\Rightarrow\quad c=6")], r"\(c=6\)"),
    # likformighet och skala
    '3.18': ett(AREASK, r"A=14\cdot3^2=14\cdot9=126", "126 cm²"),
    '3.247': ([('Areaskalan', r"\frac{100}{25}=4"), (AREASK, r"k^2=4\quad\Rightarrow\quad k=\sqrt4=2")], "2"),
    '3.65': ett(LIKF, r"k=\frac{30}{18}=\frac53", r"\(\frac53\)", 'Omkretsar ändras med samma skala som längder.'),
    '3.115': ett(LIKF, r"k=\frac{45}{18}=2{,}5", "2,5", 'Omkretsar ändras med samma skala som längder.'),
    '3.244': ett(LIKF, r"k=\frac{10}{4}=2{,}5", "2,5"),
    '3.245': ett(LIKF, r"5\cdot1{,}8=9", "9 cm"),
    '3.285': ett(LIKF, r"5\cdot3=15", "15 cm"),
    '3.261': ([('Topptriangelsatsen: \\(DE\\parallel BC\\) gör triangel ADE likformig med ABC', r"\frac{AD}{AB}=\frac{AE}{AC}"),
               ('Sätt in och lös ut AC', r"\frac{4}{10}=\frac{6}{AC}\quad\Rightarrow\quad AC=\frac{6\cdot10}{4}=15")], "15"),
    # kordor och cirkel
    '3.44': ([(KORDA, r"4\cdot9=6x"), (r"Lös ut \(x\)", r"36=6x\quad\Rightarrow\quad x=6")], "6 cm"),
    '3.299': ([(KORDA, r"2\cdot9=3x"), (r"Lös ut \(x\)", r"18=3x\quad\Rightarrow\quad x=6")], "6"),
    '3.167': ([(KORDA, r"9x=6\cdot12=72"), (r"Lös ut \(x\)", r"x=\frac{72}{9}=8")], 'Ja, påståendet är korrekt.'),
    '3.171': ett(KORDA, r"4x=6\cdot8", r"\(4x=6\cdot8\)"),
    '3.91': mc('En korda förbinder två punkter på cirkeln', 'En diameter är en korda som går genom medelpunkten.', 'En korda som går genom cirkelns medelpunkt'),
    '3.95': mc('Korda: en sträcka mellan två punkter på cirkeln', 'Båda ändpunkterna ligger på cirkelns rand.', 'En sträcka vars båda ändpunkter ligger på cirkelns rand'),
    '3.113': mc('Randvinklar som står på samma båge är lika stora', None, r"\(v=37^\circ\)"),
    '3.307': ett(RAND, r"2\cdot35^\circ=70^\circ", r"\(70^\circ\)"),
    '3.308': ett('Randvinkel på en diameter (Thales sats)', r"\angle ACB=\frac{180^\circ}{2}=90^\circ", r"\(90^\circ\)", 'Medelpunktsvinkeln på en diameter är 180°, och randvinkeln är hälften.'),
    # Pythagoras och koordinatgeometri
    '3.62': ett(PYTH, r"c=\sqrt{7^2+24^2}=\sqrt{49+576}=\sqrt{625}=25", "25 cm"),
    '3.294': ett(PYTH, r"x=\sqrt{3^2+4^2}=\sqrt{25}=5", "5"),
    '3.54': ([(f'a) {MITT}', r"\left(\frac{2+8}{2},\,\frac{-3+5}{2}\right)=(5,\,1)"),
              (f'b) {AVST}', r"d=\sqrt{(8-2)^2+(5-(-3))^2}=\sqrt{36+64}=10")], r"a) \((5,1)\) b) 10"),
    '3.184': ett(MITT, r"\left(\frac{-7+5}{2},\,\frac{9+(-3)}{2}\right)=(-1,\,3)", r"\((-1,3)\)"),
    '3.295': ett(MITT, r"x=\frac{2+8}{2}=5", "5"),
    '3.188': ([(MITT, r"\frac{-1+x}{2}=3\quad\text{och}\quad\frac{5+y}{2}=-2"), ('Lös ut koordinaterna', r"x=7,\qquad y=-9")], r"\(B=(7,-9)\)"),
    '3.267': ett(AVST, r"AC=\sqrt{(8-0)^2+(6-0)^2}=\sqrt{100}=10", "10"),
    '3.296': ett('Samma y-koordinat: avståndet är skillnaden i x', r"AB=7-1=6", "6 längdenheter"),
    '3.205': ett('Samma y-koordinat: avståndet är skillnaden i x', r"AB=2-(-3)=5", "5", r'Läs av \(A=(-3,1)\) och \(B=(2,1)\) i figuren.'),
    '3.301': ett(r"Triangelns area: \(A=\frac{b\cdot h}{2}\)", r"A=\frac{8\cdot5}{2}=20", "20 areaenheter", 'Basen AB ligger på x-axeln och är 8. Höjden är C:s y-koordinat, 5.'),
    # geometriska begrepp och vinklar
    '3.210': mc('Sträcka: en begränsad del av en linje', 'Den har två ändpunkter.', 'Sträcka'),
    '3.211': mc('Stråle: en del av en linje med en ändpunkt', 'Den fortsätter obegränsat åt ett håll.', 'Stråle'),
    '3.214': mc('En linje som skär två andra linjer kallas transversal', None, 'Transversal'),
    '3.215': ett('Sidovinklar har summan 180°', r"180^\circ-68^\circ=112^\circ", r"\(112^\circ\)"),
    '3.216': mc('Vertikalvinklar är lika stora', None, r"\(47^\circ\)"),
    '3.217': mc('Alternatvinklar vid parallella linjer är lika stora', None, r"\(124^\circ\)"),
    '3.218': mc('Likbelägna vinklar vid parallella linjer är lika stora', None, r"\(73^\circ\)"),
    '3.220': ett(TRI, r"180^\circ-48^\circ-67^\circ=65^\circ", r"\(65^\circ\)"),
    '3.221': ([('Basvinklarna i en likbent triangel är lika stora', None), (TRI, r"\frac{180^\circ-38^\circ}{2}=\frac{142^\circ}{2}=71^\circ")], r"\(71^\circ\)"),
    '3.223': ett('Vinkelsumman i en fyrhörning är 360°', r"360^\circ-90^\circ-105^\circ-82^\circ=83^\circ", r"\(83^\circ\)"),
    '3.224': ett('En bisektris delar vinkeln mitt itu', r"\frac{86^\circ}{2}=43^\circ", r"\(43^\circ\)"),
    '3.292': ett('Yttervinkelsatsen: yttervinkeln är summan av de två motstående inre vinklarna', r"125^\circ-55^\circ=70^\circ", r"\(70^\circ\)"),
    # satser och bevis
    '3.280': mc('Kvadrera båda leden', r'Om \(x=5\) gäller säkert \(x^2=25\). Det omvända gäller inte, eftersom även \(x=-5\) ger 25.', r"\(x^2=25\)"),
    '3.304': mc('Ett ”alla”-påstående är falskt om det finns ett enda undantag', None, 'Ett motexempel'),
    '3.305': ett(r"Sätt in \(x=2\)", r"2^2=4", 'Ja, påståendet är sant.'),
}
