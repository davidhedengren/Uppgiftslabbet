# Ma5: alla korta facit (en rad utan facit-rubrik) med steglista enligt FACITMALL (2026-11-22).
MULT = 'Multiplikationsprincipen: antalet sätt är produkten av antalet val i varje steg'
PERM = r"Permutationer: \(n\) olika saker kan ordnas på \(n!\) sätt"
POS = r"Positionssystemet: \((d_2d_1d_0)_b=d_2\cdot b^2+d_1\cdot b+d_0\)"
TILL = 'Dela upp talet i potenser av den nya basen, den största först'
KONG = r"Resten: \(a\equiv r\pmod m\) när \(a=qm+r\) och \(0\le r<m\)"
RAKN = 'Räkneregler för kongruens: räkna med resterna i stället för talen'
INKL = r"Principen om inklusion och exklusion: \(|A\cup B|=|A|+|B|-|A\cap B|\)"
INKL3 = r"Inklusion och exklusion för tre mängder: \(|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|\)"
D11 = 'Delbarhet med 11: den alternerande siffersumman är delbar med 11'
D4 = 'Delbarhet med 4: talet som bildas av de två sista siffrorna är delbart med 4'
SNITT = r"Snittet \(A\cap B\) består av de element som finns i båda mängderna"
DIFF = r"Differensen \(A\setminus B\) består av elementen i \(A\) som inte finns i \(B\)"
SGD = 'Största gemensamma delaren (SGD): den längsta bit som går jämnt upp i alla längder'
MGM = 'Minsta gemensamma multipeln (MGM): det första tal som båda talen går jämnt upp i'
SUMMA = r"Summatecknet: \(\sum_{k=a}^{b}f(k)=f(a)+f(a+1)+\dots+f(b)\)"


def rest(a, m, q, r):
    return ([(KONG, rf"{a}={q}\cdot{m}+{r}")], str(r))


def kong(uttryck, rakning, m, r):
    return ([(RAKN, rf"{uttryck}\equiv{rakning}\pmod{{{m}}}")], str(r))


def mult(kalkyl, svar, text=None):
    return ([(MULT, kalkyl, text)] if text else [(MULT, kalkyl)], svar)


F = {
    # mängdlära och Venndiagram
    '1.09': ([('Området ligger inuti alla tre cirklarna', None, FIG('1.09')),
              (r"Snittet \(\cap\) betyder ”både … och”", r"A\cap B\cap C")], r"\(A\cap B\cap C\)"),
    '1.12': ([('a) Området ligger i \\(B\\) men utanför \\(A\\)', None, FIG('1.12', 0)),
              (r"Differensen \(B\setminus A\) betyder ”i \(B\) men inte i \(A\)”", r"B\setminus A"),
              ('b) Området ligger utanför båda cirklarna', None, FIG('1.12', 1)),
              (r"Komplementet \(^c\) av unionen betyder ”varken i \(A\) eller i \(B\)”", r"(A\cup B)^c")],
             r"a) \(B\setminus A\) b) \((A\cup B)^c\)"),
    '1.145': ([('Mängdbyggare: \\(\\{x\\mid \\text{villkor}\\}\\)', None, 'Skriv vilken sorts tal x är och vilka olikheter som ska gälla.'),
               ('Villkoren: heltal mellan −2 och 5, båda inräknade', r"\{x\mid x\in\mathbb Z,\ -2\le x\le5\}")],
              r"\(\{x\mid x\in\mathbb Z,\ -2\le x\le5\}\)"),
    '1.474': ([('Mängden är redan uppräknad', None, 'Elementen är talen mellan klamrarna.')], r"\(A=\{1,3,5,7\}\)"),
    '1.475': ([('Räkna upp elementen mellan klamrar', None, 'De naturliga talen från 2 till 6 är 2, 3, 4, 5 och 6.')], r"\(\{2,3,4,5,6\}\)"),
    '1.476': ([(r"Ett tal tillhör \(A\) om det finns bland elementen", r"6\in A")], "ja"),
    '1.477': ([(r"Ett tal tillhör \(A\) om det finns bland elementen", r"5\notin A")], "nej"),
    '1.481': ([(r"Villkoret \(0\le n<5\): 0 är med men inte 5", r"A=\{0,1,2,3,4\}")], r"\(\{0,1,2,3,4\}\)"),
    '1.482': ([(r"Villkoret \(-2<n\le2\): −2 är inte med men 2 är det", r"A=\{-1,0,1,2\}")], r"\(\{-1,0,1,2\}\)"),
    '1.484': ([(r"\(|A|\) är antalet element i \(A\)", r"|\{2,4,6\}|=3")], "3"),
    '1.478': ([(SNITT, r"A\cap B=\{3,4\}")], r"\(\{3,4\}\)"),
    '1.480': ([(DIFF, r"A\setminus B=\{1,3,5\}", 'Ta bort 2 och 4 ur A. Talet 6 finns inte i A och påverkar inte.')], r"\(\{1,3,5\}\)"),
    '1.485': ([(INKL, r"|A\cup B|=3+2-1=4"), ('Kontroll: räkna upp unionen', r"A\cup B=\{1,2,3,4\}")], "4"),
    '1.490': ([(INKL, r"|F\cup I|=22+15-6=31"), ('Resten av klassen spelar ingen av sporterna', r"40-31=9")], "9"),
    '1.491': ([(INKL3, r"25+20+12-8-4-5+2=42")], "42"),
    '1.492': ([(INKL, r"50=30+28-x"), ('Lös ut antalet som gjort båda', r"x=58-50=8")], "8"),
    # multiplikationsprincipen
    '1.148': mult(r"5\cdot5\cdot5=5^3=125", "125 flaggor", 'Varje fält har 5 val, oberoende av de andra.'),
    '1.576': mult(r"5\cdot5\cdot5\cdot5\cdot5=5^5=3\,125", "3 125", 'Var och en av de fem positionerna har fem möjliga siffror.'),
    '1.578': mult(r"29\cdot29\cdot29=29^3=24\,389", "24 389", 'Tre positioner med 29 val på varje.'),
    '1.582': mult(r"4^5=1\,024", "1 024", 'Varje fråga har fyra alternativ, oberoende av de andra.'),
    '1.585': mult(r"6\cdot6\cdot10=360", "360"),
    '1.625': mult(r"6\cdot6\cdot6\cdot6=6^4=1\,296", "1 296 koder"),
    '1.641': ([('Räkna det motsatta: armband utan guld', None, 'Det är enklare att räkna alla armband och ta bort dem som saknar guld.'),
               (MULT, r"\text{alla: }3^5=243,\qquad\text{utan guld: }2^5=32"),
               ('Minst en guldpärla', r"243-32=211")], "211 armband"),
    '1.729': mult(r"6\cdot5=30", "30 paket", 'Varje dator kan kombineras med varje skärm.'),
    '1.730': mult(r"5\cdot8\cdot12=480", "480 sätt"),
    '1.731': mult(r"4\cdot5\cdot6=120", "120 vägval"),
    '1.736': mult(r"8\cdot10^6=8\,000\,000", "8 000 000 nummer", 'Första siffran har 8 val (2–9), de sex övriga 10 val var.'),
    '1.747': mult(r"60\cdot59\cdot59=208\,860", "208 860 koder", 'Första talet har 60 val. Andra och tredje talet får inte vara lika med talet före, så de har 59 val var.'),
    # permutationer
    '1.152': ([('Rotationer räknas som samma placering', None, 'Låt en person sitta fast. Då återstår att ordna de övriga fem.'),
               (PERM, r"5!=120")], "120 sätt"),
    '1.188': ([(PERM, r"6!=6\cdot5\cdot4\cdot3\cdot2\cdot1=720")], "720 ordningar"),
    '1.587': ([(PERM, r"7!=5\,040")], "5 040"),
    '1.591': ([(PERM, r"4!=4\cdot3\cdot2\cdot1=24")], "24"),
    '1.594': ([(r"Permutationer med upprepning: dela \(n!\) med fakulteten för varje upprepad bokstav", None,
                'KANAN har fem bokstäver: två A, två N och ett K.'),
               ('Sätt in', r"\frac{5!}{2!\cdot2!}=\frac{120}{4}=30")], "30"),
    '1.662': ([('Ordningen spelar roll, och ingen får två poster', None, 'Ordföranden väljs bland 15, sekreteraren bland de 14 som är kvar och kassören bland 13.'),
               (MULT, r"15\cdot14\cdot13=2\,730")], "2 730 sätt"),
    # talbaser
    '2.350': ([(TILL, r"20=16+4=1\cdot2^4+0\cdot2^3+1\cdot2^2+0\cdot2^1+0\cdot2^0"), ('Läs av siffrorna', r"20=10100_2")], r"\(10100_2\)"),
    '2.351': ([(POS, r"(210)_4=2\cdot4^2+1\cdot4+0=32+4=36")], "36"),
    '2.355': ([(TILL, r"55=2\cdot27+1=2\cdot3^3+0\cdot3^2+0\cdot3^1+1\cdot3^0"), ('Läs av siffrorna', r"55=2001_3")], r"\(2001_3\)"),
    '2.356': ([(POS, r"(331)_5=3\cdot5^2+3\cdot5+1=75+15+1=91")], "91"),
    '2.357': ([(POS, r"(41)_8=4\cdot8+1=33,\qquad(10)_8=1\cdot8+0=8"), ('Addera i bas tio', r"33+8=41")], "41"),
    '2.116': ([(POS, r"243_5=2\cdot5^2+4\cdot5+3=50+20+3=73")], "73"),
    '2.366': ([(POS, r"(101001)_2=1\cdot2^5+1\cdot2^3+1\cdot2^0=32+8+1=41")], "41"),
    '2.166': ([(POS, r"1011_2=8+2+1=11,\qquad110_2=4+2=6"), ('Addera i bas tio', r"11+6=17"),
               (TILL, r"17=16+1=10001_2")], r"\(10001_2\)"),
    '2.169': ([(POS, r"\mathrm{1C}_{16}=1\cdot16+12=28", 'Siffran C betyder 12.')], "28"),
    '2.380': ([(POS, r"\mathrm{A3}_{16}=10\cdot16+3=163", 'Siffran A betyder 10.')], "163"),
    '2.381': ([(TILL, r"37=32+4+1=1\cdot2^5+0\cdot2^4+0\cdot2^3+1\cdot2^2+0\cdot2^1+1\cdot2^0"), ('Läs av siffrorna', r"37=100101_2")], r"\(100101_2\)"),
    '2.205': ([(TILL, r"45=32+8+4+1=1\cdot2^5+0\cdot2^4+1\cdot2^3+1\cdot2^2+0\cdot2^1+1\cdot2^0"), ('Läs av siffrorna', r"45=101101_2")], r"\(101101_2\)"),
    '2.691': ([(POS, r"120_{\text{fem}}=1\cdot25+2\cdot5+0=35,\qquad 43_x=4x+3"), ('Sätt talen lika', r"4x+3=35\quad\Rightarrow\quad x=8")], r"\(x=8\)"),
    # summor
    '2.02': ([(SUMMA, r"\sum_{k=1}^{4}2k^2=2\cdot1^2+2\cdot2^2+2\cdot3^2+2\cdot4^2"), ('Beräkna termerna och addera', r"2+8+18+32=60")], "60"),
    '2.04': ([(SUMMA, r"3\cdot0{,}6^1+3\cdot0{,}6^2+3\cdot0{,}6^3+3\cdot0{,}6^4"),
              ('Beräkna termerna', r"1{,}8+1{,}08+0{,}648+0{,}3888=3{,}9168")], r"termerna \(1{,}8;\ 1{,}08;\ 0{,}648;\ 0{,}3888\), summan \(3{,}9168\)"),
    '2.16': ([('Dela upp summan', r"\sum_{k=1}^{n}(5k-2)=5\sum_{k=1}^{n}k-\sum_{k=1}^{n}2"),
              (r"Summan av de \(n\) första heltalen: \(\sum_{k=1}^{n}k=\frac{n(n+1)}{2}\)", r"5\cdot\frac{n(n+1)}{2}-2n=\frac{5n^2+5n-4n}{2}=\frac{n(5n+1)}{2}")],
             r"\(\frac{n(5n+1)}{2}\)"),
    '2.105': ([(SUMMA, r"3\cdot2^0+3\cdot2^1+3\cdot2^2+3\cdot2^3+3\cdot2^4"), ('Beräkna termerna och addera', r"3+6+12+24+48=93")], "93"),
    '2.189': ([(SUMMA, r"(3\cdot2-2)+(3\cdot3-2)+\dots+(3\cdot6-2)"), ('Beräkna termerna och addera', r"4+7+10+13+16=50")], "50"),
    # delbarhet
    '2.511': ([('Delbarhet med 3: siffersumman är delbar med 3', r"7+1+1=9")], "ja"),
    '2.512': ([(D11, r"4-4+4-4=0", '0 är delbart med 11.')], "ja"),
    '2.513': ([('Delbarhet med 6: talet ska vara delbart med både 2 och 3', None, '45270 slutar på 0 och är därför jämnt.'),
               ('Siffersumman avgör delbarheten med 3', r"4+5+2+7+0=18")], "ja"),
    '2.518': ([(D11, r"9-2+8-4=11")], "ja"),
    '2.550': ([(D11, r"5-2+9-3=9", '9 är inte delbart med 11.')], "nej"),
    '2.521': ([(D4, None, '30 är inte delbart med 4.')], "nej"),
    '2.553': ([(D4, r"12=3\cdot4")], "ja"),
    '2.669': ([('Primtalsfaktorisera 2 002', r"2\,002=2\cdot1\,001=2\cdot7\cdot11\cdot13"),
               ('Kvadrera och addera', r"2^2+7^2+11^2+13^2=4+49+121+169=343")], "343"),
    '2.653': ([(MGM, r"\text{MGM}(4,6)=12", 'Multiplerna av 4 är 4, 8, 12, … och av 6 är 6, 12, …')], "om 12 dagar"),
    '2.655': ([(SGD, r"\text{SGD}(120,210)=30", 'Räkna i centimeter: 120 = 2²·2·3·5 och 210 = 2·3·5·7 har 2·3·5 = 30 gemensamt.')], "30 cm"),
    '2.656': ([(MGM, r"\text{MGM}(14,12)=84", '14 = 2·7 och 12 = 2²·3 ger MGM = 2²·3·7 = 84.')], "84 jordgubbar"),
    '2.662': ([(SGD, r"\text{SGD}(45,75,81)=3", '45 = 3²·5, 75 = 3·5² och 81 = 3⁴ har bara faktorn 3 gemensamt.'),
               ('Räkna bitarna', r"\frac{45}{3}+\frac{75}{3}+\frac{81}{3}=15+25+27=67")], "67 bitar"),
    # kongruens
    '2.525': rest(38, 7, 5, 3),
    '2.526': rest(59, 7, 8, 3),
    '2.527': rest(83, 9, 9, 2),
    '2.528': rest(125, 11, 11, 4),
    '2.529': kong('a+3', '2+3=5', 7, 5),
    '2.530': kong('a+4', r'5+4=9\equiv2', 7, 2),
    '2.531': kong('2a', r'2\cdot3=6\equiv0', 6, 0),
    '2.532': kong('a^2', r'4^2=16\equiv7', 9, 7),
    '2.533': kong('a+b', r'2+3=5\equiv0', 5, 0),
    '2.534': kong('ab', r'2\cdot3=6\equiv1', 5, 1),
    '2.537': ([('Veckodagarna upprepas med perioden 7', r"30=4\cdot7+2\quad\Rightarrow\quad30\equiv2\pmod7"),
               ('Räkna två dagar framåt från fredag', None, 'Lördag, söndag.')], "söndag"),
    '2.675': ([(r"\(n\equiv5\pmod{36}\) betyder \(n=5+36k\)", r"5,\ 41,\ 77,\ \dots"), ('Första talet större än 5', r"n=41")], "41"),
    '2.685': ([(r"Samma rest 1 betyder att \(a-1\) är delbart med 3, 5 och 7", r"\text{MGM}(3,5,7)=105"),
               (r"Minsta \(a>1\)", r"a-1=105\quad\Rightarrow\quad a=106")], "106"),
    # bevis, differentialekvationer, induktion
    '2.570': ([('Ett udda heltal kan skrivas \\(2a+1\\)', None, 'Använd olika bokstäver, eftersom talen kan vara olika.'),
               ('Addera och bryt ut 2', r"(2a+1)+(2b+1)=2a+2b+2=2(a+b+1)")], r"\(2a+1\) och \(2b+1\), där \(a\) och \(b\) är heltal"),
    '4.117': ([('Tolka med enheterna', None, r'\(y\) är mängden i liter och \(t\) tiden i minuter, så \(y(5)\approx3{,}84\) betyder liter efter 5 minuter.')],
              'Modellen förutsäger att det finns ungefär 3,84 liter vätska efter 5 minuter.'),
    '4.600': ([('Derivera ansatsen två gånger', r"y_p=Ae^x,\quad y_p''=Ae^x"),
               ('Sätt in i ekvationen', r"Ae^x+4Ae^x=5Ae^x=10e^x"), ('Jämför koefficienterna', r"5A=10\quad\Rightarrow\quad A=2")], r"\(A=2\)"),
    '4.602': ([('Derivera partikulärlösningen två gånger', r"y_p=3\sin x,\quad y_p''=-3\sin x"),
               ('Sätt in i vänsterledet', r"-3\sin x+4\cdot3\sin x=9\sin x"), ('Jämför med högerledet', r"k=9")], r"\(k=9\)"),
    '2.707': ([(r"Sätt in \(n=6\) i formeln", r"a_6=2^{6-1}+1=32+1=33"),
               ('Kontrollera med rekursionen', r"2,\ 3,\ 5,\ 9,\ 17,\ 33")], "33"),
}
