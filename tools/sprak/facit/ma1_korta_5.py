# Ma1 kapitel 5: sannolikhet, risk, korrelation, urval och felkällor (2026-11-23).
import os
exec(open(os.path.join('tools', 'sprak', 'facit', 'ma1_korta_gemensamt.py'), encoding='utf-8').read())
KLASS = r"Klassisk sannolikhet: \(P=\frac{\text{antal gynnsamma utfall}}{\text{antal möjliga utfall}}\)"
FORV = r"Förväntat antal: \(\text{sannolikhet}\cdot\text{antal försök}\)"
RELF = r"Relativ frekvens: \(\frac{\text{antal gånger det inträffade}}{\text{antal försök}}\)"
KOMP = r"Komplementhändelse: \(P(\text{inte }A)=1-P(A)\)"
OBER = r"Oberoende händelser: \(P(A\text{ och }B)=P(A)\cdot P(B)\)"
BERO = 'Utan återläggning: räkna med det som finns kvar efter förra dragningen, och multiplicera längs grenen'
MULTP = 'Multiplikationsprincipen: multiplicera antalet val i varje steg'
TRAD = 'Grenarna från samma punkt har summan 1'
RISKP = 'Skriv risken som ett bråk och sedan i procent'
REL = r"Relativ förändring: \(\frac{\text{förändringen}}{\text{ursprungligt värde}}\)"
PE = 'Skillnaden mellan två procentsatser mäts i procentenheter'
KORR = 'Positiv korrelation: y ökar när x ökar. Negativ: y minskar när x ökar'
RSTARK = r"Korrelationskoefficienten \(r\) ligger mellan −1 och 1; ju närmare ±1, desto starkare samband"
KAUS = 'Korrelation visar inte orsak; en tredje variabel kan påverka båda'
FELM = 'Osäkerhetsintervall: resultatet ± felmarginalen'


def gem(text, svar):
    return mc(KAUS, text, svar)


F = {
    # grundläggande sannolikhet och relativ frekvens
    '5.13': ett(KLASS, r"P(\text{jämnt})=\frac36=\frac12", r"\(\frac12\)", 'De jämna utfallen är 2, 4 och 6.'),
    '5.48': ett(KLASS, r"P(\text{vit})=\frac{1}{1+3}=\frac14", r"\(\frac14\)", 'För varje vit boll finns tre röda, så en av fyra lika delar är vit.'),
    '5.239': ett(KLASS, r"P(\text{utan A})=\frac{20-7}{20}=\frac{13}{20}", r"\(\frac{13}{20}\)"),
    '5.164': ett(KLASS, r"\frac3n=\frac38\quad\Rightarrow\quad n=8", "8 fält"),
    '5.237': ett(KLASS, r"\frac5n=\frac5{12}\quad\Rightarrow\quad n=12", "12 kulor"),
    '5.235': mc(KLASS, 'De jämna utfallen på en tärning är 2, 4 och 6.', "6"),
    '5.416': mc('En sannolikhet ligger mellan 0 och 1', None, "1,2"),
    '5.415': ett(FORV, r"0{,}15\cdot200=30", "30"),
    '5.556': ett(RELF, r"\frac{36}{48}=0{,}75", "0,75"),
    '5.557': ett(RELF, r"\frac{74}{200}=0{,}37=37\ \%", "37 %"),
    '5.561': ett(RELF, r"\frac{132}{480}=0{,}275\approx0{,}28", "cirka 0,28"),
    '5.558': ([(RELF, r"\frac{15}{1\,250}=0{,}012"), (FORV, r"0{,}012\cdot6\,000=72")], "72"),
    '5.562': ([(RELF, r"\frac{18}{60}=0{,}3"), (FORV, r"0{,}3\cdot250=75")], "75"),
    # komplementhändelse
    '5.145': ett(KOMP, r"1-0{,}96=0{,}04", "0,04"),
    '5.449': ett(KOMP, r"1-0{,}35=0{,}65", "0,65"),
    '5.450': ett(KOMP, r"1-0{,}08=0{,}92", "0,92"),
    '5.451': ett(KOMP, r"1-0{,}625=0{,}375", "0,375"),
    '5.452': ett(KOMP, r"1-\frac16=\frac56", r"\(\frac56\)"),
    '5.453': ett(KOMP, r"100\ \%-30\ \%=70\ \%", "70 %"),
    '5.458': ([('Minst en felaktig är komplementet till ingen felaktig', r"P(\text{ingen})=0{,}9^5"), (KOMP, r"1-0{,}9^5\approx0{,}410")], "0,410"),
    '5.459': ([('Minst en träff är komplementet till ingen träff', r"P(\text{ingen})=0{,}7^4"), (KOMP, r"1-0{,}7^4\approx0{,}760")], "0,760"),
    '5.462': mc('”Minst en” och ”ingen” täcker tillsammans alla utfall', None, 'Ingen sexa'),
    '5.463': ett(KOMP, r"1-0{,}4=0{,}6", r"Det är fel, eftersom \(P(\text{inte }A)=0{,}6\)."),
    # oberoende händelser
    '5.424': ett(OBER, r"0{,}3\cdot0{,}6=0{,}18", "0,18"),
    '5.425': ett(OBER, r"0{,}5\cdot0{,}4=0{,}2", "0,2"),
    '5.426': ett(OBER, r"0{,}2\cdot0{,}1=0{,}02", "0,02"),
    '5.427': ett(OBER, r"0{,}7\cdot0{,}7\cdot0{,}7=0{,}343", "0,343"),
    '5.431': ett(OBER, r"0{,}9^4=0{,}6561", "0,6561"),
    '5.429': ([(KOMP, r"P(\text{grönt})=1-0{,}4=0{,}6"), (OBER, r"0{,}6\cdot0{,}6=0{,}36")], "0,36"),
    '5.635': ett(OBER, r"0{,}04\cdot0{,}03=0{,}0012=0{,}12\ \%", "0,12 %"),
    '5.14': delar(
        ('a', [(FORV, r"0{,}75\cdot40=30")], "30 frön"),
        ('b', [(OBER, r"0{,}75\cdot0{,}75=0{,}5625")], "0,5625"),
        ('c', [('Två sätt: första gror och andra inte, eller tvärtom', r"0{,}75\cdot0{,}25+0{,}25\cdot0{,}75=2\cdot0{,}1875=0{,}375")], "0,375"),
    ),
    '5.152': delar(
        ('a', [(OBER, r"0{,}70\cdot0{,}70=0{,}49")], "0,49"),
        ('b', [(KOMP, r"P(\text{miss})=1-0{,}70=0{,}30"), (OBER, r"0{,}30\cdot0{,}30=0{,}09")], "0,09"),
    ),
    # beroende händelser
    '5.248': ett(BERO, r"P(\text{röd igen})=\frac{4}{7}", r"\(\frac47\)", 'Efter en röd kula finns 4 röda av 7 kulor kvar.'),
    '5.433': ett(BERO, r"\frac{3}{9}=\frac13", r"\(\frac13\)", 'Kvar: 3 röda av 9 kulor.'),
    '5.434': ett(BERO, r"\frac{2}{7}", r"\(\frac27\)", 'Kvar: 2 röda av 7 kulor.'),
    '5.435': ett(BERO, r"\frac{4}{6}=\frac23", r"\(\frac23\)", 'Kvar: 4 röda av 6 kulor.'),
    '5.436': ett(BERO, r"\frac{2}{10}\cdot\frac{1}{9}=\frac{2}{90}=\frac1{45}", r"\(\frac1{45}\)"),
    '5.437': ett(BERO, r"\frac{6}{12}\cdot\frac{5}{11}=\frac{30}{132}=\frac5{22}", r"\(\frac5{22}\)"),
    '5.438': ett(BERO, r"\frac{3}{10}\cdot\frac{2}{9}=\frac{6}{90}=\frac1{15}", r"\(\frac1{15}\)"),
    '5.439': ett(BERO, r"\frac{4}{10}\cdot\frac{6}{9}=\frac{24}{90}=\frac4{15}", r"\(\frac4{15}\)"),
    '5.440': ett(BERO, r"\frac{3}{8}\cdot\frac{5}{7}=\frac{15}{56}", r"\(\frac{15}{56}\)"),
    '5.441': ett(BERO, r"\frac{5}{7}\cdot\frac{2}{6}=\frac{10}{42}=\frac5{21}", r"\(\frac5{21}\)"),
    '5.445': ett(BERO, r"\frac{4}{52}\cdot\frac{3}{51}=\frac{12}{2\,652}=\frac1{221}", r"\(\frac1{221}\)"),
    '5.611': ett(BERO, r"\frac{7}{10}\cdot\frac{3}{9}=\frac{21}{90}=\frac7{30}", r"\(\frac7{30}\)"),
    '5.600': ett(BERO, r"\frac58", r"\(\frac58\)", 'Efter en röd kula finns 5 röda kvar av 8 kulor.'),
    '5.602': ett(BERO, r"\frac16", r"\(\frac16\)", 'Efter en vit kula finns 1 vit kvar av 6 kulor.'),
    '5.608': ett(BERO, r"\frac4{11}", r"\(\frac4{11}\)", 'Efter ett hjärter finns 4 hjärter kvar av 11 kort.'),
    '5.601': ett(TRAD, r"1-\frac25=\frac35", r"\(\frac35\)"),
    '5.612': mc(BERO, r'\(\frac37\cdot\frac26\) följer grenen röd och sedan röd igen.', 'Sannolikheten att båda kulorna är röda.'),
    # flera steg och kombinatorik
    '5.277': ett(MULTP, r"4\cdot3\cdot2=24", "24"),
    '5.278': ett(MULTP, r"3\cdot3\cdot3=3^3=27", "27"),
    '5.279': ett(MULTP, r"5\cdot4=20", "20", 'Andra siffran får inte vara samma som den första, så 4 val återstår.'),
    '5.464': ett(MULTP, r"3\cdot4=12", "12"),
    '5.478': ett(MULTP, r"26\cdot26=676", "676"),
    '5.469': ett(OBER, r"\frac12\cdot\frac12=\frac14", r"\(\frac14\)"),
    '5.476': ett(OBER, r"\frac14\cdot\frac14\cdot\frac14=\frac1{64}", r"\(\frac1{64}\)"),
    '5.474': ett(KLASS, r"\frac{3}{36}=\frac1{12}", r"\(\frac1{12}\)", 'Summan 10 fås med (4, 6), (5, 5) och (6, 4) av 36 lika möjliga utfall.'),
    # risk
    '5.06': ett(FORV, r"0{,}005\cdot2\,000=10", "ungefär 10 fel"),
    '5.481': ett(FORV, r"0{,}003\cdot10\,000=30", "30"),
    '5.482': ett(FORV, r"0{,}02\cdot1\,250=25", "25"),
    '5.483': ett(FORV, r"0{,}008\cdot1\,000=8", "8"),
    '5.631': ett(FORV, r"\frac{3}{1\,000}\cdot5\,000=15", "15 patienter"),
    '5.633': ett('Förväntad kostnad: sannolikhet gånger kostnad', r"0{,}15\cdot1\,800=270", "270 kr"),
    '5.638': ([(KOMP, r"1-0{,}98=0{,}02"), (FORV, r"0{,}02\cdot1\,200=24")], "24 varor"),
    '5.23': ett(RISKP, r"\frac1{500}=0{,}002=0{,}2\ \%", "0,2 %"),
    '5.271': ett(RISKP, r"\frac1{250}=0{,}004=0{,}4\ \%", "0,4 %"),
    '5.479': ett(RISKP, r"\frac1{250}=0{,}004=0{,}4\ \%", "0,4 %"),
    '5.480': ett(RISKP, r"\frac1{20\,000}=0{,}00005=0{,}005\ \%", "0,005 %"),
    '5.639': ett(RISKP, r"\frac1{50}=0{,}02=2\ \%", "2 %"),
    '5.630': ett(RISKP, r"\frac4{100}=4\ \%", "4 %", 'Räkna de orange personerna i figuren.'),
    '5.226': ett(RELF, r"\frac{12}{800}=0{,}015=1{,}5\ \%", "1,5 %"),
    '5.487': ett(REL, r"\frac{3-2}{2}=0{,}5=50\ \%", "50 %"),
    '5.636': ett(REL, r"\frac{8-5}{5}=0{,}6=60\ \%", "60 %"),
    '5.491': ett(REL, r"\frac{5-4}{5}=0{,}2=20\ \%", "20 %"),
    '5.488': ett(PE, r"\frac3{1\,000}-\frac2{1\,000}=0{,}3\ \%-0{,}2\ \%=0{,}1", "0,1 procentenheter"),
    '5.637': ett(PE, r"1{,}2-0{,}9=0{,}3", "0,3 procentenheter"),
    '5.489': ([(FORV, r"0{,}008\cdot50\,000=400,\qquad0{,}004\cdot50\,000=200"), ('Skillnaden', r"400-200=200")], "200"),
    '5.632': ett('Dela de två riskerna', r"\frac{3}{0{,}4}=7{,}5", "7,5 gånger", 'Läs av bil 3 och buss 0,4 i diagrammet.'),
    # korrelation och kausalitet
    '5.75': mc(KORR, 'När x ökar tenderar y att minska.', 'Negativ korrelation'),
    '5.77': mc(KORR, 'Punkterna visar ingen tydlig riktning uppåt eller nedåt.', 'Ingen tydlig korrelation'),
    '5.150': mc(KORR, 'Punktmolnet följer en stigande trend.', 'Positiv korrelation'),
    '5.194': mc(KORR, 'x och y ökar tillsammans.', 'Positiv korrelation'),
    '5.195': mc(KORR, 'y minskar när x ökar.', 'Negativ korrelation'),
    '5.494': mc(KORR, 'Båda variablerna ökar tillsammans.', 'Positiv korrelation'),
    '5.495': mc(KORR, 'När hastigheten ökar minskar tiden.', 'Negativ korrelation'),
    '5.201': mc(RSTARK, 'Alla punkter på en stigande linje ger r = 1.', 'Perfekt positiv korrelation'),
    '5.202': mc(RSTARK, 'Alla punkter på en fallande linje ger r = −1.', 'Perfekt negativ korrelation'),
    '5.496': mc(RSTARK, 'Tecknet visar bara riktningen.', r"\(r=-0{,}91\)"),
    '5.497': mc(RSTARK, '1,3 ligger utanför intervallet.', r"\(r=1{,}3\)"),
    '5.498': mc(RSTARK, 'Stigande och tät samling ger r nära 1.', "0,95"),
    '5.83': gem('Andra variabler, till exempel föräldrarnas utbildning, kan påverka både bokägande och resultat.', 'Nej, korrelation visar inte orsak.'),
    '5.84': gem('Regn gör att fler använder paraply och att gatorna blir blöta.', 'Regn'),
    '5.185': gem('Varmt väder ger både mer glassköp och mer bad.', 'Varmt väder'),
    '5.506': gem('Större städer har både fler bränder och fler brandmän.', 'Stadens storlek'),
    '5.509': gem('Äldre barn har större fötter och har läst längre.', 'Ålder'),
    '5.504': mc('Kausalitet är ett orsakssamband', None, 'Att en variabel orsakar en förändring i en annan.'),
    # urval och felkällor
    '5.219': mc('Urvalet är de som faktiskt väljs ut ur populationen', None, 'Urvalet'),
    '5.521': mc('Systematiskt urval: var n:te i en lista efter en slumpad start', None, 'Systematiskt urval'),
    '5.522': mc('I en totalundersökning ingår hela populationen', None, 'Totalundersökning'),
    '5.529': mc('Bortfall: de som valts ut men inte svarar', None, 'Bortfall'),
    '5.533': mc('Bortfall: de som valts ut men inte svarar', None, 'Bortfall'),
    '5.111': mc('En ledande fråga antyder vilket svar som förväntas', 'Orden ”också” och ”fantastiska” styr svaret.', 'Ledande formulering'),
    '5.530': mc('En ledande fråga antyder vilket svar som förväntas', None, 'Ledande fråga'),
    '5.531': mc('Systematiskt fel: lika stort och åt samma håll varje gång', None, 'Systematiskt fel'),
    '5.532': mc('Slumpmässigt fel: varierar åt båda hållen', None, 'Slumpmässigt fel'),
    '5.537': mc('Man svarar som man tror är socialt accepterat', None, 'Social önskvärdhet'),
    '5.540': mc('Vanor kan skilja sig mellan årstider', None, 'Tidpunkten är kanske inte representativ för hela året.'),
    '5.549': ett(FELM, r"34-2{,}5=31{,}5", "31,5 %"),
    '5.550': ett(FELM, r"34+2{,}5=36{,}5", "36,5 %"),
    '5.551': ett(FELM, r"(58+3)-(58-3)=61-55=6", "6 procentenheter"),
    '5.552': ett(FELM, r"13{,}6-12=12-10{,}4=1{,}6", "1,6 procentenheter"),
    '5.553': ([(r"Felmarginalen är proportionell mot \(\frac1{\sqrt n}\)", None, r'För att halvera \(\frac1{\sqrt n}\) måste \(\sqrt n\) fördubblas.'),
               (r"\(\sqrt n\) fördubblas när \(n\) blir fyra gånger större", r"\sqrt{4n}=2\sqrt n")], "4 gånger"),
}
