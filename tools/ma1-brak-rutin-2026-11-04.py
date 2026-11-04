"""56 manuellt författade rutinuppgifter. Kör bara i master; återkörning är säker."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
ROWS = []

def add(level, tex, expr, answer, hint, steps, good, bad, *, rhs=None, domain=None):
    ROWS.append(dict(level=level, tex=tex, expr=expr, answer=answer, hint=hint,
                     steps=steps, good=good, bad=bad, rhs=rhs, domain=domain or []))

# Förenklingar. Varje rubrik och mellanled är skrivet för den enskilda uppgiften.
add(1, r'\frac{7x}{7}', '7*x/7', 'x',
    'Sju gånger ett tal delas med sju.',
    [(r'Förkorta med \(7\)', r'\frac{7x}{7}=\frac77\cdot x=x')],
    ['x', 'X'], ['7x', '1', '7x/7'])
add(1, r'\frac{2x}{7}+\frac{3x}{7}', '2*x/7+3*x/7', '5*x/7',
    'Bråken har redan samma nämnare. Lägg ihop täljarna.',
    [(r'Addera sjundedelar: \(\frac a7+\frac b7=\frac{a+b}{7}\)',
      r'\frac{2x}{7}+\frac{3x}{7}=\frac{2x+3x}{7}=\frac{5x}{7}')],
    ['5x/7', '(5/7)*x'], ['5x/14', 'x', '2x/7+3x/7'])
add(1, r'\frac{9x}{5}-\frac{4x}{5}', '9*x/5-4*x/5', 'x',
    'Subtrahera täljarna och behåll nämnaren.',
    [(r'Subtrahera femtedelar: \(\frac a5-\frac b5=\frac{a-b}{5}\)',
      r'\frac{9x}{5}-\frac{4x}{5}=\frac{5x}{5}=x')],
    ['x', 'X'], ['5x', 'x/5', '5x/5'])
add(2, r'\frac{2x}{3}+\frac{x}{6}', '2*x/3+x/6', '5*x/6',
    'Skriv tredjedelarna som sjättedelar.',
    [(r'Förläng med \(\frac22=1\)', r'\frac{2x}{3}=\frac{4x}{6}'),
     (r'Addera de två täljarna över \(6\)', r'\frac{4x}{6}+\frac{x}{6}=\frac{5x}{6}')],
    ['5x/6', '5/6*x'], ['x/3', '5x/9', '2x/3+x/6'])
add(2, r'\frac{3x}{4}-\frac{x}{6}', '3*x/4-x/6', '7*x/12',
    'Tolv är en gemensam nämnare till fjärdedelar och sjättedelar.',
    [(r'Förläng till nämnaren \(12\)', r'\frac{3x}{4}=\frac{9x}{12},\qquad\frac{x}{6}=\frac{2x}{12}'),
     (r'Subtrahera \(2x\) från \(9x\)', r'\frac{9x-2x}{12}=\frac{7x}{12}')],
    ['7x/12', '(7/12)x'], ['x', 'x/5', '3x/4-x/6'])
add(2, r'x-\frac{3x}{8}', 'x-3*x/8', '5*x/8',
    'Skriv den hela x-termen som åttondelar.',
    [(r'Skriv \(x=\frac{8x}{8}\)', r'x-\frac{3x}{8}=\frac{8x-3x}{8}=\frac{5x}{8}')],
    ['5x/8', '0,625x'], ['-2x/8', '5/8', '8x/8-3x/8'])
add(2, r'\frac{2x}{5}+\frac{x}{15}', '2*x/5+x/15', '7*x/15',
    'Förläng femtedelarna till femtondelar.',
    [(r'Förläng med \(\frac33=1\)', r'\frac{2x}{5}=\frac{6x}{15}'),
     (r'Addera \(6x+x\) över nämnaren \(15\)', r'\frac{6x+x}{15}=\frac{7x}{15}')],
    ['7x/15', '(7/15)x'], ['3x/20', 'x/5', '2x/5+x/15'])
add(2, r'\frac{5x}{4}-\frac{x}{2}', '5*x/4-x/2', '3*x/4',
    'Skriv halvan som fjärdedelar.',
    [(r'Förläng till nämnaren \(4\)', r'\frac{x}{2}=\frac{2x}{4}'),
     (r'Subtrahera \(2x\) från \(5x\)', r'\frac{5x-2x}{4}=\frac{3x}{4}')],
    ['3x/4', '0,75x'], ['2x', 'x', '5x/4-x/2'])
add(2, r'\frac{3x}{10}+\frac{2x}{5}', '3*x/10+2*x/5', '7*x/10',
    'Gör om femtedelarna till tiondelar.',
    [(r'Förläng med \(\frac22=1\)', r'\frac{2x}{5}=\frac{4x}{10}'),
     (r'Addera \(3x+4x\) över nämnaren \(10\)', r'\frac{3x+4x}{10}=\frac{7x}{10}')],
    ['7x/10', '0,7x'], ['x/3', 'x/2', '3x/10+2x/5'])
add(3, r'\frac{x+1}{2}-\frac{x-2}{3}-\frac{x+5}{6}', '(x+1)/2-(x-2)/3-(x+5)/6', '1/3',
    'Skriv alla bråk med nämnaren sex. Behåll parenteserna tills du hanterat minustecknen.',
    [(r'Gemensam nämnare: \(6\)', r'\frac{3(x+1)-2(x-2)-(x+5)}{6}'),
     (r'Alla x-termer tar ut varandra: \(3x-2x-x=0\)', r'\begin{aligned}\frac{3x+3-2x+4-x-5}{6}&=\frac{2}{6}\\&=\frac13\end{aligned}')],
    ['1/3', '\\frac{1}{3}'], ['-1/3', '2/6', 'x/6'])
add(3, r'\frac{5x-2}{4}-\left(\frac{x+2}{3}-\frac{x+7}{6}\right)',
    '(5*x-2)/4-((x+2)/3-(x+7)/6)', '13*x/12',
    'Förenkla först parentesen. När parentesen tas bort byter dess båda termer tecken.',
    [(r'Parentesens gemensamma nämnare är \(6\)', r'\frac{x+2}{3}-\frac{x+7}{6}=\frac{x-3}{6}'),
     (r'Subtrahera hela täljaren \(x-3\)', r'\begin{gathered}\frac{5x-2}{4}-\frac{x-3}{6}\\=\frac{3(5x-2)-2(x-3)}{12}\\=\frac{15x-6-2x+6}{12}\\=\frac{13x}{12}\end{gathered}')],
    ['13x/12', '(13/12)*x'], ['13x/12-1', '17x/12', '(5x-2)/4-((x+2)/3-(x+7)/6)'])
add(4, r'\frac{x^2+4x}{3x}-\frac{x-2}{3}', '(x**2+4*x)/(3*x)-(x-2)/3', '2',
    'Bryt ut x ur den första täljaren. Förkorta faktorer, inte enskilda termer.',
    [(r'Bryt ut \(x\): \(x^2+4x=x(x+4)\)', r'\frac{x^2+4x}{3x}=\frac{x(x+4)}{3x}=\frac{x+4}{3}'),
     (r'x-termerna tar ut varandra: \(x-x=0\)', r'\frac{x+4-(x-2)}{3}=\frac6{3}=2')],
    ['2'], ['6', '2/x', '(x^2+4x)/(3x)-(x-2)/3'], domain=[0])
add(4, r'\frac{x^2-4}{x-2}-\frac{x^2+2x}{x}', '(x**2-4)/(x-2)-(x**2+2*x)/x', '0',
    'Använd konjugatregeln i första täljaren och bryt ut x i den andra.',
    [(r'Konjugatregeln: \(x^2-4=(x-2)(x+2)\)', r'\frac{x^2-4}{x-2}=x+2'),
     (r'Bryt ut \(x\) ur \(x^2+2x\)', r'\frac{x^2+2x}{x}=\frac{x(x+2)}{x}=x+2'),
     (r'Samma uttryck subtraheras: \((x+2)-(x+2)\)', r'(x+2)-(x+2)=0')],
    ['0'], ['4', '2x+4', '(x+2)-(x+2)'], domain=[0,2])
add(5, r'\frac{x^2-9}{x-3}\div\frac{x+3}{2x}', '(x**2-9)/(x-3)/((x+3)/(2*x))', '2*x',
    'Faktorisera skillnaden av två kvadrater. Division med ett bråk är multiplikation med dess invers.',
    [(r'Konjugatregeln: \(x^2-9=(x-3)(x+3)\)', r'\frac{x^2-9}{x-3}=x+3'),
     (r'Invertera divisorn: \(\frac ab\div\frac cd=\frac ab\cdot\frac dc\)', r'(x+3)\cdot\frac{2x}{x+3}=2x')],
    ['2x', '2*X'], ['x/2', '2x+6', '(x+3)*2x/(x+3)'], domain=[-3,0,3])

# Ekvationer: samma operation i båda leden, därefter kontroll av definitionsmängd.
add(1, r'\frac{x}{7}=-3', 'x/7', '-21', 'Multiplicera båda leden med nämnaren.',
    [(r'Multiplicera båda leden med \(7\)', r'x=7\cdot(-3)=-21')], ['-21','x=-21'], ['21','-3/7'], rhs='-3')
add(2, r'\frac{x}{2}-\frac{x}{3}=10', 'x/2-x/3', '60', 'Multiplicera varje term i båda leden med sex.',
    [(r'Ta bort nämnarna med \(6\)', r'3x-2x=60'),
     (r'En x-term återstår: \(3x-2x=x\)', r'x=60')], ['60','x=60'], ['10','12'], rhs='10')
add(2, r'\frac{x}{4}+\frac{x}{6}=5', 'x/4+x/6', '12', 'Tolv är delbart med båda nämnarna.',
    [(r'Multiplicera båda leden med \(12\)', r'3x+2x=60'),
     (r'Dividera \(5x=60\) med \(5\)', r'x=12')], ['12','x=12'], ['50','2'], rhs='5')
add(2, r'\frac{3x}{4}+1=7', '3*x/4+1', '8', 'Ta först bort ettan genom att subtrahera ett från båda leden.',
    [(r'Subtrahera \(1\) från båda leden', r'\frac{3x}{4}=6'),
     (r'Multiplicera med \(4\) och dividera med \(3\)', r'3x=24\quad\Rightarrow\quad x=8')], ['8','x=8'], ['9','28/3'], rhs='7')
add(2, r'\frac{x}{2}-3=\frac{x}{4}+5', 'x/2-3', '32', 'Samla x-termerna i vänsterledet och konstanterna i högerledet.',
    [(r'Subtrahera \(\frac{x}{4}\) och addera \(3\)', r'\frac{x}{2}-\frac{x}{4}=8'),
     (r'Skriv halvan som \(\frac{2x}{4}\)', r'\frac{2x-x}{4}=8'),
     (r'Multiplicera \(\frac{x}{4}=8\) med \(4\)', r'x=32')], ['32','x=32'], ['8','16'], rhs='x/4+5')
add(2, r'\frac{x}{3}-2=\frac{x}{5}', 'x/3-2', '15', 'Multiplicera alla termer med femton, även den ensamma tvåan.',
    [(r'Multiplicera båda leden med \(15\)', r'5x-30=3x'),
     (r'Samla x-termerna: \(5x-3x=30\)', r'2x=30\quad\Rightarrow\quad x=15')], ['15','x=15'], ['1','30'], rhs='x/5')
add(2, r'\frac{2x}{3}-\frac{x}{4}=-5', '2*x/3-x/4', '-12',
    'Multiplicera båda leden med tolv.',
    [(r'Ta bort nämnarna med \(12\)', r'8x-3x=-60'),
     (r'Samla till \(5x=-60\)', r'x=-12')],
    ['-12','x=-12'], ['12','-60'], rhs='-5')
add(2, r'\frac{x}{3}-\frac{2x}{5}=1', 'x/3-2*x/5', '-15',
    'Multiplicera båda leden med femton. Skillnaden mellan x-termerna blir negativ.',
    [(r'Ta bort nämnarna med \(15\)', r'5x-6x=15'),
     (r'Dividera \(-x=15\) med \(-1\)', r'x=-15')], ['-15','x=-15'], ['15','-1'], rhs='1')
add(3, r'\frac{2x-1}{3}-\frac{x+2}{4}=\frac{x}{6}+1', '(2*x-1)/3-(x+2)/4', '22/3',
    'Tolv tar bort alla tre nämnarna. Glöm inte att även ettan multipliceras.',
    [(r'Multiplicera båda leden med \(12\)', r'4(2x-1)-3(x+2)=2x+12'),
     (r'Utveckla täljarna och samla till \(5x-10=2x+12\)', r'8x-4-3x-6=2x+12'),
     (r'Subtrahera \(2x\) och addera \(10\)', r'3x=22\quad\Rightarrow\quad x=\frac{22}{3}')],
    ['22/3','x=22/3'], ['7,33','22','3/22'], rhs='x/6+1')
add(3, r'\frac{x-2}{3}-\frac{x+1}{4}=\frac{x+4}{6}', '(x-2)/3-(x+1)/4', '-19',
    'Använd nämnaren tolv och samla sedan x-termerna på samma sida.',
    [(r'Multiplicera alla bråk med \(12\)', r'4(x-2)-3(x+1)=2(x+4)'),
     (r'Utveckla parenteserna till \(x-11=2x+8\)', r'4x-8-3x-3=2x+8'),
     (r'Subtrahera \(x+8\) från båda leden', r'-19=x')], ['-19','x=-19'], ['19','-3'], rhs='(x+4)/6')
add(4, r'\frac{x+4}{x}=\frac32', '(x+4)/x', '8', 'Vilket värde får x inte ha? Multiplicera sedan med två gånger x.',
    [(r'Nämnaren kräver \(x\ne0\)', r'x\ne0'),
     (r'Multiplicera båda leden med \(2x\)', r'2(x+4)=3x'),
     (r'Subtrahera \(2x\) från båda leden', r'2x+8=3x\quad\Rightarrow\quad x=8'),
     (r'Kontrollera \(x=8\) i ursprungsekvationen', r'\frac{8+4}{8}=\frac{12}{8}=\frac32')], ['8','x=8'], ['0','4'], rhs='3/2', domain=[0])
add(4, r'\frac{3}{x-1}=\frac{2}{x+2}', '3/(x-1)', '-8', 'Multiplicera båda leden med produkten av nämnarna.',
    [(r'Nämnarna kräver \(x\ne1\) och \(x\ne-2\)', r'x\ne1,\quad x\ne-2'),
     (r'Multiplicera med \((x-1)(x+2)\)', r'3(x+2)=2(x-1)'),
     (r'Samla termerna i \(3x+6=2x-2\)', r'x=-8'),
     (r'Kontrollera \(x=-8\): båda leden är \(-\frac13\)', r'\frac{3}{-9}=-\frac13,\qquad\frac{2}{-6}=-\frac13')], ['-8','x=-8'], ['1','-2','8'], rhs='2/(x+2)', domain=[1,-2])
add(4, r'\frac{x+1}{x-2}-\frac{x+4}{x-2}=\frac12', '(x+1)/(x-2)-(x+4)/(x-2)', '-4',
    'Bråken i vänsterledet har samma nämnare. Subtrahera hela den andra täljaren.',
    [(r'Nämnaren kräver \(x\ne2\)', r'x\ne2'),
     (r'Subtrahera täljarna: \((x+1)-(x+4)=-3\)', r'\frac{-3}{x-2}=\frac12'),
     (r'Multiplicera båda leden med \(2(x-2)\)', r'-6=x-2\quad\Rightarrow\quad x=-4'),
     (r'Kontrollera \(x=-4\): nämnaren är \(-6\)', r'\frac{-3}{-6}-\frac0{-6}=\frac12')], ['-4','x=-4'], ['2','4','-6'], rhs='1/2', domain=[2])
add(5, r'\frac{2}{x-1}-\frac{3}{x+1}=\frac{2x-7}{x^2-1}',
    '2/(x-1)-3/(x+1)', '4', 'Faktorisera x²−1. Då kan samma produkt ta bort alla tre nämnarna.',
    [(r'Konjugatregeln: \(x^2-1=(x-1)(x+1)\)', r'x\ne1,\quad x\ne-1'),
     (r'Multiplicera båda leden med \((x-1)(x+1)\)', r'2(x+1)-3(x-1)=2x-7'),
     (r'Samla till \(-x+5=2x-7\)', r'2x+2-3x+3=2x-7'),
     (r'Addera \(x+7\) och dividera med \(3\)', r'12=3x\quad\Rightarrow\quad x=4'),
     (r'Kontrollera \(x=4\): båda leden är \(\frac1{15}\)', r'\begin{gathered}\frac23-\frac35=\frac1{15}\\\frac{2\cdot4-7}{4^2-1}=\frac1{15}\end{gathered}')],
    ['4','x=4'], ['1','-1','12'], rhs='(2*x-7)/(x**2-1)', domain=[-1,1])

# Ytterligare 28 enligt användarens utökning, med tonvikt på rutin på nivå 1–2.
add(1, r'\frac{x}{9}+\frac{x}{9}', 'x/9+x/9', '2*x/9',
    'Nämnaren är densamma. Lägg ihop täljarna.',
    [(r'Addera niondelar: \(\frac a9+\frac b9=\frac{a+b}{9}\)', r'\frac{x+x}{9}=\frac{2x}{9}')],
    ['2x/9','(2/9)x'], ['x/18','2x/18','x/9+x/9'])
add(1, r'\frac{8x}{12}', '8*x/12', '2*x/3',
    'Både åtta och tolv är delbara med fyra.',
    [(r'Förkorta täljare och nämnare med \(4\)', r'\frac{8x}{12}=\frac{8x/4}{12/4}=\frac{2x}{3}')],
    ['2x/3','(2/3)*x'], ['4x/6','8x/12','x/4'])
add(2, r'\frac{x}{5}+\frac{x}{10}', 'x/5+x/10', '3*x/10',
    'En femtedel är två tiondelar.',
    [(r'Förläng femtedelarna med \(\frac22\)', r'\frac{x}{5}=\frac{2x}{10}'),
     (r'Addera \(2x+x\) över samma nämnare', r'\frac{2x+x}{10}=\frac{3x}{10}')],
    ['3x/10','0,3x'], ['2x/15','x/15','x/5+x/10'])
add(2, r'\frac{7x}{8}-\frac{x}{4}', '7*x/8-x/4', '5*x/8',
    'Skriv fjärdedelarna som åttondelar.',
    [(r'Förläng med \(\frac22=1\)', r'\frac{x}{4}=\frac{2x}{8}'),
     (r'Subtrahera täljarna: \(7x-2x=5x\)', r'\frac{7x}{8}-\frac{2x}{8}=\frac{5x}{8}')],
    ['5x/8','0.625*x'], ['6x/4','3x/2','7x/8-x/4'])
add(2, r'\frac{2x}{3}-\frac{x}{2}', '2*x/3-x/2', 'x/6',
    'Använd sex som gemensam nämnare.',
    [(r'Förläng båda bråken till nämnaren \(6\)', r'\frac{2x}{3}=\frac{4x}{6},\qquad\frac{x}{2}=\frac{3x}{6}'),
     (r'Skillnaden i täljarna är \(4x-3x=x\)', r'\frac{4x-3x}{6}=\frac{x}{6}')],
    ['x/6','(1/6)*x'], ['x','x/5','2x/3-x/2'])
add(2, r'\frac{3x}{5}+\frac{x}{4}', '3*x/5+x/4', '17*x/20',
    'Vilket litet tal är delbart med både fem och fyra?',
    [(r'Förläng till gemensamma nämnaren \(20\)', r'\frac{3x}{5}=\frac{12x}{20},\qquad\frac{x}{4}=\frac{5x}{20}'),
     (r'Addera \(12x+5x\)', r'\frac{12x+5x}{20}=\frac{17x}{20}')],
    ['17x/20','0,85x'], ['4x/9','7x/20','3x/5+x/4'])
add(2, r'\frac{x}{2}-\frac{x}{5}-\frac{x}{10}', 'x/2-x/5-x/10', 'x/5',
    'Skriv alla tre termer som tiondelar. Båda de sista termerna ska subtraheras.',
    [(r'Gemensam nämnare för alla tre bråk: \(10\)', r'\frac{5x}{10}-\frac{2x}{10}-\frac{x}{10}=\frac{2x}{10}'),
     (r'Förkorta med \(2\)', r'\frac{2x}{10}=\frac{x}{5}')],
    ['x/5','0,2x'], ['2x/5','2x/10','x/2-x/5-x/10'])
add(2, r'\frac{x}{3}+\frac{x}{4}+\frac{x}{6}', 'x/3+x/4+x/6', '3*x/4',
    'Skriv alla tre bråk som tolftedelar.',
    [(r'Gemensam nämnare: \(12\)', r'\frac{4x}{12}+\frac{3x}{12}+\frac{2x}{12}=\frac{9x}{12}'),
     (r'Förkorta med \(3\)', r'\frac{9x}{12}=\frac{3x}{4}')],
    ['3x/4','0,75x'], ['x/13','9x/12','x/3+x/4+x/6'])
add(2, r'\frac{5x}{6}-\frac{x}{4}', '5*x/6-x/4', '7*x/12',
    'Skriv sjättedelar och fjärdedelar som tolftedelar.',
    [(r'Förläng till nämnaren \(12\)', r'\frac{5x}{6}=\frac{10x}{12},\qquad\frac{x}{4}=\frac{3x}{12}'),
     (r'Subtrahera \(10x-3x\)', r'\frac{10x-3x}{12}=\frac{7x}{12}')],
    ['7x/12','(7/12)x'], ['2x','x/3','5x/6-x/4'])
add(2, r'\frac{4x}{3}-x', '4*x/3-x', 'x/3',
    'Skriv den hela x-termen som tredjedelar.',
    [(r'Skriv \(x=\frac{3x}{3}\)', r'\frac{4x}{3}-x=\frac{4x-3x}{3}=\frac{x}{3}')],
    ['x/3','(1/3)x'], ['x','3x/2','4x/3-x'])
add(2, r'2x-\frac{x}{2}-\frac{x}{4}', '2*x-x/2-x/4', '5*x/4',
    'Skriv alla termer som fjärdedelar, även två gånger x.',
    [(r'Använd \(2x=\frac{8x}{4}\) och \(\frac{x}{2}=\frac{2x}{4}\)', r'\frac{8x}{4}-\frac{2x}{4}-\frac{x}{4}'),
     (r'Subtrahera de två sista täljarna: \(8x-2x-x=5x\)', r'\frac{8x-2x-x}{4}=\frac{5x}{4}')],
    ['5x/4','1,25x'], ['7x/4','x/4','2x-x/2-x/4'])
add(3, r'\frac{2x+1}{3}-\frac{x-2}{4}-\frac{5x+10}{12}',
    '(2*x+1)/3-(x-2)/4-(5*x+10)/12', '0',
    'Tolv fungerar för alla nämnare. Behåll parenteserna när du skriver ihop täljarna.',
    [(r'De två första bråkens gemensamma nämnare är \(12\)', r'\begin{gathered}\frac{2x+1}{3}-\frac{x-2}{4}\\=\frac{8x+4-3x+6}{12}\\=\frac{5x+10}{12}\end{gathered}'),
     (r'Samma bråk subtraheras: \(a-a=0\)', r'\frac{5x+10}{12}-\frac{5x+10}{12}=0')],
    ['0'], ['1','-1','x/12'])
add(4, r'\frac{4x^2-2x}{2x}-(x-3)', '(4*x**2-2*x)/(2*x)-(x-3)', 'x+2',
    'Bryt ut två gånger x ur täljaren. Förkorta innan du tar bort den sista parentesen.',
    [(r'Bryt ut \(2x\): \(4x^2-2x=2x(2x-1)\)', r'\frac{4x^2-2x}{2x}=2x-1'),
     (r'Fördela minustecknet: \(-(x-3)=-x+3\)', r'2x-1-x+3=x+2')],
    ['x+2','2+X'], ['x-4','3x-4','2x-1-x+3'], domain=[0])
add(5, r'\frac{x^2-16}{x+4}\cdot\frac{x}{x^2-4x}',
    '(x**2-16)/(x+4)*x/(x**2-4*x)', '1',
    'Faktorisera både skillnaden av kvadrater och nämnaren i det andra bråket.',
    [(r'Konjugatregeln: \(x^2-16=(x-4)(x+4)\)', r'\frac{x^2-16}{x+4}=x-4'),
     (r'Bryt ut \(x\): \(x^2-4x=x(x-4)\)', r'\frac{x}{x^2-4x}=\frac1{x-4}'),
     (r'Förkorta faktorn \(x-4\)', r'(x-4)\cdot\frac1{x-4}=1')],
    ['1'], ['x','x-4','(x-4)/(x-4)'], domain=[-4,0,4])

add(1, r'\frac{x}{9}=4', 'x/9', '36', 'Multiplikation med nio tar bort divisionen med nio.',
    [(r'Multiplicera båda leden med \(9\)', r'x=4\cdot9=36')], ['36','x=36'], ['4/9','13'], rhs='4')
add(1, r'\frac{x}{6}=-2', 'x/6', '-12', 'Multiplicera båda leden med sex och behåll minustecknet.',
    [(r'Multiplicera båda leden med \(6\)', r'x=(-2)\cdot6=-12')], ['-12','x=-12'], ['12','-1/3'], rhs='-2')
add(2, r'\frac{x}{3}+5=-2', 'x/3+5', '-21', 'Subtrahera fem från båda leden innan du tar bort nämnaren.',
    [(r'Subtrahera \(5\) från båda leden', r'\frac{x}{3}=-7'),
     (r'Multiplicera båda leden med \(3\)', r'x=-21')], ['-21','x=-21'], ['-11','9'], rhs='-2')
add(2, r'\frac{4x}{5}-3=1', '4*x/5-3', '5', 'Lägg till tre i båda leden innan du tar bort divisionen.',
    [(r'Addera \(3\) till båda leden', r'\frac{4x}{5}=4'),
     (r'Multiplicera med \(5\) och dividera med \(4\)', r'4x=20\quad\Rightarrow\quad x=5')], ['5','x=5'], ['2','20'], rhs='1')
add(2, r'\frac{x}{3}+\frac{x}{4}=7', 'x/3+x/4', '12', 'Multiplicera båda leden med tolv.',
    [(r'Nämnarna tas bort med \(12\)', r'4x+3x=84'),
     (r'Dividera \(7x=84\) med \(7\)', r'x=12')], ['12','x=12'], ['49','7'], rhs='7')
add(2, r'\frac{5x}{6}-\frac{x}{2}=-3', '5*x/6-x/2', '-9', 'Gör om halvorna till sjättedelar, eller multiplicera båda leden med sex.',
    [(r'Multiplicera båda leden med \(6\)', r'5x-3x=-18'),
     (r'Samla till \(2x=-18\)', r'x=-9')], ['-9','x=-9'], ['9','-18'], rhs='-3')
add(2, r'\frac{x}{5}-2=\frac{x}{7}+4', 'x/5-2', '105', 'Samla bråken på ena sidan och konstanterna på den andra.',
    [(r'Subtrahera \(\frac{x}{7}\) och addera \(2\)', r'\frac{x}{5}-\frac{x}{7}=6'),
     (r'Multiplicera båda leden med \(35\)', r'7x-5x=210'),
     (r'Dividera \(2x=210\) med \(2\)', r'x=105')], ['105','x=105'], ['17','35'], rhs='x/7+4')
add(2, r'\frac{3x}{4}-\frac{x}{2}=-2', '3*x/4-x/2', '-8',
    'Multiplicera båda leden med fyra.',
    [(r'Ta bort nämnarna med \(4\)', r'3x-2x=-8'),
     (r'En x-term återstår: \(3x-2x=x\)', r'x=-8')], ['-8','x=-8'], ['8','-2'], rhs='-2')
add(2, r'\frac{x}{2}+1=\frac{x}{3}-6', 'x/2+1', '-42',
    'Multiplicera med sex. Båda konstanterna måste också multipliceras.',
    [(r'Multiplicera båda leden med \(6\)', r'3x+6=2x-36'),
     (r'Subtrahera \(2x+6\) från båda leden', r'x=-42')], ['-42','x=-42'], ['42','-18'], rhs='x/3-6')
add(2, r'\frac{x}{4}+\frac{x}{6}=\frac{x}{3}+2', 'x/4+x/6', '24',
    'Tolv tar bort alla nämnare. Multiplicera även tvåan med tolv.',
    [(r'Multiplicera båda leden med \(12\)', r'3x+2x=4x+24'),
     (r'Samla vänsterledet: \(5x=4x+24\)', r'x=24')], ['24','x=24'], ['2','12'], rhs='x/3+2')
add(3, r'\frac{3x-2}{5}+\frac{x+1}{2}=\frac{7x+4}{10}', '(3*x-2)/5+(x+1)/2', '3/4',
    'Multiplicera med tio och samla sedan alla x-termer i samma led.',
    [(r'Multiplicera båda leden med \(10\)', r'2(3x-2)+5(x+1)=7x+4'),
     (r'Samla termerna: \(11x+1=7x+4\)', r'6x-4+5x+5=7x+4'),
     (r'Subtrahera \(7x+1\) och dividera med \(4\)', r'4x=3\quad\Rightarrow\quad x=\frac34')],
    ['3/4','0,75','x=0.75'], ['0,8','4/3','3'], rhs='(7*x+4)/10')
add(3, r'\frac{x-1}{3}-\frac{x+2}{4}=\frac{x-5}{2}', '(x-1)/3-(x+2)/4', '4',
    'Multiplicera med tolv. Ta sedan bort parenteserna, med rätt tecken.',
    [(r'Multiplicera båda leden med \(12\)', r'4(x-1)-3(x+2)=6(x-5)'),
     (r'Utveckla till \(x-10=6x-30\)', r'4x-4-3x-6=6x-30'),
     (r'Addera \(30\) och subtrahera \(x\)', r'20=5x\quad\Rightarrow\quad x=4')],
    ['4','x=4'], ['8','-4'], rhs='(x-5)/2')
add(4, r'\frac{2x-1}{x+3}=3', '(2*x-1)/(x+3)', '-10',
    'Nämnaren får inte vara noll. Multiplicera båda leden med hela nämnaren.',
    [(r'Nämnaren kräver \(x\ne-3\)', r'x\ne-3'),
     (r'Multiplicera båda leden med \(x+3\)', r'2x-1=3(x+3)'),
     (r'Samla termerna i \(2x-1=3x+9\)', r'-10=x'),
     (r'Kontrollera \(x=-10\) i ursprungsekvationen', r'\frac{2\cdot(-10)-1}{-10+3}=\frac{-21}{-7}=3')],
    ['-10','x=-10'], ['-3','10','-4'], rhs='3', domain=[-3])
add(4, r'\frac{x+2}{x-1}=\frac{x+5}{x+1}', '(x+2)/(x-1)', '7',
    'Multiplicera med produkten av nämnarna. Se vad som händer med kvadrattermerna.',
    [(r'Nämnarna kräver \(x\ne1\) och \(x\ne-1\)', r'x\ne1,\quad x\ne-1'),
     (r'Multiplicera med \((x-1)(x+1)\)', r'(x+2)(x+1)=(x+5)(x-1)'),
     (r'Utveckla produkterna och stryk \(x^2\) i båda leden', r'\begin{gathered}x^2+3x+2=x^2+4x-5\\3x+2=4x-5\end{gathered}'),
     (r'Subtrahera \(3x\) och addera \(5\)', r'x=7'),
     (r'Kontrollera \(x=7\): båda leden är \(\frac32\)', r'\begin{gathered}\frac{7+2}{7-1}=\frac96=\frac32\\\frac{7+5}{7+1}=\frac{12}8=\frac32\end{gathered}')],
    ['7','x=7'], ['1','-1','-7'], rhs='(x+5)/(x+1)', domain=[-1,1])

def facit(steps, answer):
    items = ''.join('<li><p class="facit-rubrik">'+title+'</p><div class="facit-matte">\\['+math+'\\]</div></li>' for title, math in steps)
    return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'+items+'</ol><p class="facit-svar"><strong>Svar:</strong> \\('+answer+'\\).</p></div>'

def build():
    x = sp.Symbol('x')
    qs=[]
    for i,r in enumerate(ROWS):
        id='1.'+str(1567+i); level=r['level']; eq=r['rhs'] is not None
        a=sp.sympify(r['answer']); expression=sp.sympify(r['expr'])
        if eq:
            roots=sp.solve(expression-sp.sympify(r['rhs']),x)
            assert roots==[a], (id,roots,a)
            assert a not in r['domain']
        else: assert sp.cancel(expression-a)==0, id
        # Exakt algebraisk rutin: inga digitala lösningsverktyg behövs.
        q=dict(id=id,kap=1,omr='ekv_brak',kurs=['1a','1b','1c'],
               niva='E' if level<=2 else 'C',
               poang='1/0/0' if level<=2 else '0/2/0' if level<=4 else '0/3/0',
               familj='Ekvationer med nämnare' if eq else 'Bråk i uttryck',
               formaga=['procedur'],traningsniva=level,arbetsinsats=1 if level==1 else 2 if level<=3 else 3,
               miniräknare=False,geogebra=False,spel=True,självrättning=True,
               t='<p>'+('Lös ekvationen.' if eq else 'Förenkla uttrycket.')+'</p><p>\\['+r['tex']+'\\]</p>',
               ledtrad='<p>'+r['hint']+'</p>')
        if eq and a.q!=1:q['t']+='<p>Svara exakt.</p>'
        if not eq and r['domain']:
            q['t']+='<p>Uttrycket är definierat för \\('+',\\ '.join('x\\ne'+str(v) for v in r['domain'])+'\\).</p>'
        ans_tex=sp.latex(a)
        if eq:ans_tex='x='+ans_tex
        elif r['domain']:ans_tex+=r'\quad ('+',\\ '.join('x\\ne'+str(v) for v in r['domain'])+')'
        q['s']=facit(r['steps'],ans_tex)
        q['svarstyp']='numeriskt' if eq else 'uttryck'
        q['svarFormat']='numeriskt' if eq else 'förenklat_polynom'
        q['rättSvar']=int(a) if eq and a.q==1 else r['answer'].replace('**','^')
        q['tolerans']=0 if eq else None
        qs.append(q)
    return qs

if __name__=='__main__':
    import sys
    qs=build();p=ROOT/'uppgifterma1.js';src=p.read_text();start=src.index('[');bank,end=json.JSONDecoder().raw_decode(src,start)
    existing={q['id']:q for q in bank}
    assert len(qs)==56
    for q in qs:
        if q['id'] in existing and '--refresh' not in sys.argv:assert existing[q['id']]==q, 'ID-konflikt: '+q['id']
    new=[q for q in qs if q['id'] not in existing]
    if new:
        insert=',\n'+',\n'.join('  '+json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ') for q in new)+'\n'
        src=src[:end-1].rstrip()+insert+src[end-1:]
    replacements={q['id']:q for q in qs}
    old_steps={
        '1.1364': ([(r'Multiplicera båda leden med \(5\)',r'2x=4\cdot5=20'),(r'Dividera \(2x=20\) med \(2\)',r'x=10')],r'x=10'),
        '1.270': ([(r'Multiplicera båda leden med \(5\)',r'2x-3=15'),(r'Addera \(3\) i båda leden',r'2x=18'),(r'Dividera båda leden med \(2\)',r'x=9')],r'x=9')}
    pos=src.index('[')+1; changes=[];dec=json.JSONDecoder()
    while True:
        while src[pos].isspace() or src[pos]==',':pos+=1
        if src[pos]==']':break
        q,end=dec.raw_decode(src,pos)
        if q['id'] in replacements or q['id'] in old_steps:
            if q['id'] in replacements:q=replacements[q['id']]
            else:q['s']=facit(*old_steps[q['id']])
            changes.append((pos,end,json.dumps(q,ensure_ascii=False,indent=2).replace('\n','\n  ')))
        pos=end
    for start,end,value in reversed(changes):src=src[:start]+value+src[end:]
    p.write_text(src)
    cases=[dict(id=q['id'],good=r['good'],bad=r['bad']) for q,r in zip(qs,ROWS)]
    (ROOT/'tools/ma1-brak-rutin-2026-11-04.cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
    print('56 uppgifter verifierade med exakt symbolisk algebra; nya:',len(new))
