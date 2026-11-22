# Ma3c: alla korta facit (en rad utan facit-rubrik) med steglista enligt FACITMALL (2026-11-22).
KVOT = r"Ändringskvoten: \(\frac{\Delta y}{\Delta x}=\frac{f(b)-f(a)}{b-a}\)"
POT = r"Deriveringsregeln för potenser: \(D\,x^n=nx^{n-1}\)"
TERM = r"Derivera term för term med \(D\,x^n=nx^{n-1}\); en konstant har derivatan 0"
AX = r"Derivatan av \(a^x\) är \(a^x\ln a\)"
EKX = r"Derivatan av \(Ce^{kx}\) är \(Cke^{kx}\)"
INT = r"Integralens värde: \(\int_a^bf(x)\,dx=F(b)-F(a)\)"
KONT = r"Kontinuitet i \(x=a\): de två uttrycken ska ge samma värde där de möts"


def potens(skriv, f1, svar, omskr=None):
    steg = []
    if omskr:
        steg.append(('Skriv bråken som potenser med negativ exponent', omskr))
    steg.append((TERM, f1))
    return (steg, svar)


F = {
    '1.121': ([(r"Kontinuitet: \(\lim_{x\to2}f(x)=f(2)\)", r"\lim_{x\to2}f(x)=5"),
               ('Gränsvärdet av en summa är summan av gränsvärdena', r"\lim_{x\to2}\big(f(x)+g(x)\big)=5+3=8")], "8"),
    '1.125': ([('Graden är den högsta exponenten', r"4x^5\ \Rightarrow\ \text{grad }5"),
               ('Konstanttermen är termen utan \\(x\\)', r"7")], "graden 5, konstanttermen 7"),
    '1.177': ([(r"Sätt in \(x=2\) i \(f\)", r"f(2)=2^2-1=3"), (r"Läs av \(g(2)\) i tabellen", r"g(2)=6"),
               ('Addera', r"f(2)+g(2)=3+6=9")], "9"),
    '1.279': ([(KONT, None, r'Vid \(x=1\) möts \(ax+b\) och \(x^2+2\). Vid \(x=3\) möts \(x^2+2\) och \(2x+a\).'),
               (r"Villkoret vid \(x=3\)", r"3^2+2=2\cdot3+a\quad\Rightarrow\quad11=6+a\quad\Rightarrow\quad a=5"),
               (r"Villkoret vid \(x=1\)", r"a\cdot1+b=1^2+2\quad\Rightarrow\quad5+b=3\quad\Rightarrow\quad b=-2")], r"\(a=5,\ b=-2\)"),
    '2.81': ([(KVOT, r"\frac{s(5)-s(2)}{5-2}"), ('Beräkna funktionsvärdena', r"s(5)=25+20=45,\qquad s(2)=4+8=12"),
              ('Sätt in', r"\frac{45-12}{3}=11")], "11 m/s"),
    '2.86': ([(KVOT, r"\frac{1\,680-1\,200}{4}=\frac{480}{4}=120")], "120 besökare per timme"),
    '2.91': ([(KVOT, r"\frac{24{,}6-18{,}0}{3}=\frac{6{,}6}{3}=2{,}2")], "2,2 °C per timme"),
    '2.96': ([(KVOT, r"\frac{s(3)-s(1)}{3-1}"), ('Beräkna funktionsvärdena', r"s(3)=27+6=33,\qquad s(1)=3+2=5"),
              ('Sätt in', r"\frac{33-5}{2}=14")], "14 m/s"),
    '2.149': ([(AX, r"V'(t)=20\,000\cdot1{,}04^t\cdot\ln1{,}04"), (r"Sätt in \(t=5\)", r"V'(5)=20\,000\cdot1{,}04^5\cdot\ln1{,}04\approx954")],
              "cirka 954 kr/år"),
    '2.154': ([(AX, r"f'(0)=a^0\ln a=\ln a"), ('Jämför med det givna värdet', r"\ln a=\ln4\quad\Rightarrow\quad a=4")], r"\(a=4\)"),
    '2.181': ([(TERM, r"f'(x)=3ax^2-8x+2"), (r"Sätt in \(x=1\) och använd \(f'(1)=6\)", r"3a-8+2=6\quad\Rightarrow\quad3a=12\quad\Rightarrow\quad a=4")], r"\(a=4\)"),
    '2.185': ([('Faktorisera derivatan', r"6x^2-12x=6x(x-2)"),
               ('En produkt är positiv när faktorerna har samma tecken', None,
                r'Båda faktorerna är negativa när \(x<0\) och båda positiva när \(x>2\). Mellan 0 och 2 har de olika tecken.')],
              r"\(x<0\) eller \(x>2\)"),
    '2.187': ([(TERM, r"f'(x)=4x^3+2ax"), (r"\(x=1\) ska ge \(f'(1)=0\)", r"4+2a=0\quad\Rightarrow\quad a=-2")], r"\(a=-2\)"),
    '2.285': potens(None, r"f'(x)=5\cdot4x^3-3+0=20x^3-3", r"\(f'(x)=20x^3-3\)"),
    '2.287': potens(None, r"f'(x)=7\cdot5x^4-2x+3=35x^4-2x+3", r"\(f'(x)=35x^4-2x+3\)"),
    '2.288': potens(None, r"f'(x)=\frac32\cdot4x^3-2\cdot2x+0=6x^3-4x", r"\(f'(x)=6x^3-4x\)"),
    '2.290': potens(None, r"f'(x)=9\cdot2x-5+0=18x-5", r"\(f'(x)=18x-5\)"),
    '2.291': potens(None, r"f'(x)=4\cdot7x^6+2\cdot3x^2-1=28x^6+6x^2-1", r"\(f'(x)=28x^6+6x^2-1\)"),
    '2.295': potens(None, r"f'(x)=4x+3\cdot(-1)x^{-2}=4x-\frac{3}{x^2}", r"\(f'(x)=4x-\frac{3}{x^2}\)", r"\frac3x=3x^{-1}"),
    '2.296': potens(None, r"f'(x)=-4+5\cdot(-1)x^{-2}=-4-\frac{5}{x^2}", r"\(f'(x)=-4-\frac{5}{x^2}\)", r"\frac5x=5x^{-1}"),
    '2.299': potens(None, r"f'(x)=3+2\cdot(-2)x^{-3}=3-\frac{4}{x^3}", r"\(f'(x)=3-\frac{4}{x^3}\)", r"\frac{2}{x^2}=2x^{-2}"),
    '2.300': potens(None, r"f'(x)=10x+(-3)x^{-4}=10x-\frac{3}{x^4}", r"\(f'(x)=10x-\frac{3}{x^4}\)", r"\frac{1}{x^3}=x^{-3}"),
    '2.392': ([(TERM, r"f'(x)=5x^4+8x"), ('Bryt gärna ut \\(x\\)', r"f'(x)=x(5x^3+8)")], r"\(f'(x)=5x^4+8x\)"),
    '2.397': ([(TERM, r"f'(x)=-12x^2+12x"), ('Bryt gärna ut \\(12x\\)', r"f'(x)=12x(1-x)")], r"\(f'(x)=-12x^2+12x\)"),
    '2.549': ([(POT, r"D\,x^k=kx^{k-1}"), (r"\(k\) är en konstant, så termen \(k\) har derivatan 0", r"f'(x)=kx^{k-1}+0")], r"\(f'(x)=kx^{k-1}\)"),
    '2.409': ([(AX, r"f'(x)=3^x\ln3"), (r"Sätt in \(x=0\)", r"f'(0)=3^0\ln3=\ln3")], r"\(\ln3\)"),
    '2.425': ([(AX, r"f'(x)=3^x\ln3"), (r"Sätt in \(x=1\)", r"f'(1)=3^1\ln3=3\ln3")], r"\(3\ln3\)"),
    '2.508': ([(r"Skriv basen som en e-potens: \(a=e^{\ln a}\)", r"2^x=\left(e^{\ln2}\right)^x=e^{x\ln2}"),
               (r"Jämför med \(e^{kx}\)", r"k=\ln2")], r"\(k=\ln2\)"),
    '2.525': ([(r"\(f'(t)\) är förändringshastigheten, med enheten hg per vecka", None,
                r'\(f\'(3)\) är alltså hur snabbt vikten ökar vid tiden 3 veckor.')],
              'Hur snabbt vattenmelonens vikt ökar (i hg per vecka) just när den är 3 veckor gammal.'),
    '2.528': ([(EKX, r"m'(t)=2\,000\cdot(-0{,}005)e^{-0{,}005t}=-10e^{-0{,}005t}"),
               (r"Sätt in \(t=1\,000\)", r"m'(1\,000)=-10e^{-5}")], r"\(-10e^{-5}\) µg/dygn"),
    '3.152': ([('Förändringen är integralen av förändringshastigheten', r"\int_0^6(50-5t)\,dt=\Big[50t-2{,}5t^2\Big]_0^6=300-90=210"),
               ('Lägg till startvärdet', r"P(6)=800+210=1\,010")], "1 010 individer"),
    '3.163': ([(INT, r"\int_0^2(3x^2+k)\,dx=\Big[x^3+kx\Big]_0^2=8+2k"), ('Sätt integralen lika med 14', r"8+2k=14\quad\Rightarrow\quad k=3")], r"\(k=3\)"),
    '3.191': ([(INT, r"\int_0^2(ax^2+1)\,dx=\Big[\frac{ax^3}{3}+x\Big]_0^2=\frac{8a}{3}+2"),
               ('Beräkna högerledet', r"\int_0^2(3x+1)\,dx=\Big[\frac{3x^2}{2}+x\Big]_0^2=6+2=8"),
               ('Sätt leden lika', r"\frac{8a}{3}+2=8\quad\Rightarrow\quad a=\frac94")], r"\(a=\frac94\)"),
    '3.508': ([('En minimipunkt är en dal och en maximipunkt en topp på grafen', None, 'Läs av punkterna där grafen vänder.'),
               ('Läs av koordinaterna', r"\text{min: }(-1,\,-1),\qquad\text{max: }(1,\,3)")],
              r"minimipunkt \((-1,-1)\), maximipunkt \((1,3)\)"),
}
