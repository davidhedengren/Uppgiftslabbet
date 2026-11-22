# Ma2 korta facit, del 3: geometri, statistik, programmens tillämpningar, diagram (2026-11-22).
import os
exec(open(os.path.join('tools', 'sprak', 'facit', 'ma2_korta_gemensamt.py'), encoding='utf-8').read())
LIKF = r"Likformighet: motsvarande sidor har samma längdskala \(k=\frac{\text{stor}}{\text{liten}}\)"
AREASK = r"Areaskala: areor ändras med kvadraten på längdskalan, \(k^2\)"
KORDA = r"Kordasatsen: \(a\cdot b=c\cdot d\) för delsträckorna på två kordor som skär varandra"
PYTH = r"Pythagoras sats: \(c^2=a^2+b^2\)"
PYTHO = r"Pythagoras sats omvänd: om \(a^2+b^2=c^2\) är triangeln rätvinklig"
MITT = r"Mittpunktsformeln: \(\left(\frac{x_1+x_2}{2},\,\frac{y_1+y_2}{2}\right)\)"
AVST = r"Avståndsformeln: \(d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\)"
RAND = 'Randvinkelsatsen: medelpunktsvinkeln är dubbelt så stor som randvinkeln på samma båge'
TOPP = r"Topptriangelsatsen: \(DE\parallel BC\) ger \(\frac{AD}{AB}=\frac{AE}{AC}\)"
NORM = r"Normalfördelning: \(\mu\pm\sigma\) är en standardavvikelse från medelvärdet"
KORR = r"Korrelationskoefficienten \(r\): tecknet ger riktningen och \(|r|\) nära 1 ett starkt samband"
REGR = r"Sätt in x-värdet i modellen \(y=kx+m\)"
FFAKT = r"Förändringsfaktor: \(1+\text{ökning}\) eller \(1-\text{minskning}\) i decimalform"
EXPM = r"Exponentialmodell: \(y=C\cdot a^x\)"
ANDEL = r"Del av helhet: \(\text{antal}=\text{andel}\cdot\text{helhet}\)"
DIAG = 'Läs av i diagrammet'
TAB = 'Läs av i tabellen'

F = {
    # Pythagoras, likformighet, kordor och cirkel
    '3.309': ett(PYTH, r"c=\sqrt{6^2+8^2}=\sqrt{100}=10", "10 cm"),
    '3.349': ett(PYTH, r"d=\sqrt{6^2+8^2}=\sqrt{100}=10", "10 m", 'Diagonalen är hypotenusa i en rätvinklig triangel med rummets sidor som kateter.'),
    '3.635': ett(PYTH, r"d=\sqrt{80^2+45^2}=\sqrt{8\,425}\approx91{,}8", "cirka 91,8 cm"),
    '3.334': ett(PYTHO, r"7^2+24^2=49+576=625=25^2", 'Ja, triangeln är rätvinklig.'),
    '3.464': ett(PYTHO, r"9^2+12^2=81+144=225=15^2", 'Ja, eftersom 9² + 12² = 15².'),
    '3.312': ett(AREASK, r"2^2=4", "4"),
    '3.350': ett(AREASK, r"3^2=9", "9 gånger"),
    '3.646': ett(AREASK, r"7\cdot2^2=7\cdot4=28", "28 cm²"),
    '3.325': ett(LIKF, r"k=\frac{36}{24}=1{,}5", "1,5", 'Omkretsar ändras med samma skala som längder.'),
    '3.336': ett(LIKF, r"14\cdot3=42", "42 cm", 'Omkretsen är en längd och multipliceras med längdskalan.'),
    '3.354': ett(LIKF, r"4\cdot2{,}5=10", "10 cm"),
    '3.694': ett(LIKF, r"k=\frac{7{,}5}{3}=2{,}5", "2,5"),
    '3.640': ([('Skala 1:50: verkligheten är 50 gånger större', r"8\cdot50=400\ \mathrm{cm}"), ('Omvandla till meter', r"400\ \mathrm{cm}=4\ \mathrm m")], "4 m"),
    '3.314': mc('Två par lika vinklar räcker för likformighet', 'Då är även den tredje vinkeln lika, eftersom vinkelsumman är 180°.', 'Vinkel–vinkel (VV)'),
    '3.337': ([(TOPP, r"\frac{4}{10}=\frac{AE}{15}"), ('Lös ut AE', r"AE=\frac{4\cdot15}{10}=6")], "6"),
    '3.338': ([(TOPP, r"\frac{5}{10}=\frac{6}{AC}"), ('Lös ut AC', r"AC=\frac{6\cdot10}{5}=12")], "12"),
    '3.316': ([(KORDA, r"5\cdot8=4x"), (r"Lös ut \(x\)", r"x=\frac{40}{4}=10")], "10 cm"),
    '3.339': ([(KORDA, r"4\cdot6=3x"), (r"Lös ut \(x\)", r"x=\frac{24}{3}=8")], "8"),
    '3.360': ([(KORDA, r"2\cdot6=3x"), (r"Lös ut \(x\)", r"x=\frac{12}{3}=4")], "4"),
    '3.615': ([(KORDA, r"6\cdot6=3x"), (r"Lös ut \(x\)", r"x=\frac{36}{3}=12")], r"\(x=12\)"),
    '3.616': ([(KORDA, r"2{,}5\cdot4=2x"), (r"Lös ut \(x\)", r"x=\frac{10}{2}=5")], "5 dm"),
    '3.618': ([(KORDA, r"20\cdot45=30x"), (r"Lös ut \(x\)", r"x=\frac{900}{30}=30")], "30 m"),
    '3.623': ([(KORDA, r"30\cdot50=25x"), (r"Lös ut \(x\)", r"x=\frac{1\,500}{25}=60")], "60 cm"),
    '3.622': ([(r"Bisektrissatsen: \(\frac{AB}{AC}=\frac{BD}{DC}\)", r"\frac{8}{AC}=\frac23"), ('Lös ut AC', r"AC=\frac{3\cdot8}{2}=12")], "12 cm"),
    '3.345': ett(RAND, r"2\cdot44^\circ=88^\circ", r"\(88^\circ\)"),
    '3.332': ett('Thales sats: randvinkeln på en diameter är rät', r"\frac{180^\circ}{2}=90^\circ", r"\(90^\circ\)"),
    '3.652': mc('En tangent är vinkelrät mot radien i tangeringspunkten', None, r"\(90^\circ\)"),
    '3.346': ett('Yttervinkelsatsen: yttervinkeln är summan av de två motstående inre vinklarna', r"120^\circ-50^\circ=70^\circ", r"\(70^\circ\)"),
    '3.352': ett('Vinkelsumman i en triangel är 180°', r"x=180^\circ-45^\circ-65^\circ=70^\circ", r"\(70^\circ\)"),
    '3.321': mc('En median går från ett hörn till mitten av motstående sida', None, 'Median'),
    '3.351': mc('Parallellogram: två par parallella motstående sidor', None, 'Parallellogram'),
    '3.324': mc('Allt som är större än 3 är också större än 1', r'Implikationen \(x>3\Rightarrow x>1\) gäller därför för alla reella \(x\).', 'Ja'),
    # koordinatgeometri
    '3.317': ett('Samma y-koordinat: avståndet är skillnaden i x', r"AB=5-(-2)=7", "7 längdenheter"),
    '3.318': ett(MITT, r"\left(\frac{-4+6}{2},\,\frac{2+8}{2}\right)=(1,\,5)", r"\((1,5)\)"),
    '3.357': ett(MITT, r"\left(\frac{-2+4}{2},\,\frac{3+7}{2}\right)=(1,\,5)", r"\((1,5)\)"),
    '3.678': ett(MITT, r"\left(\frac{-5+2}{2},\,\frac{2+(-6)}{2}\right)=(-1{,}5;\,-2)", r"\((-1{,}5;\ -2)\)"),
    '3.679': ett(MITT, r"\left(\frac{0+6}{2},\,\frac{10+0}{2}\right)=(3,\,5)", r"\((3,5)\)"),
    '3.680': ett(MITT, r"\left(\frac{2+14}{2},\,\frac{9+3}{2}\right)=(8,\,6)", r"\((8,6)\)"),
    '5.148': ett(MITT, r"\left(\frac{2+8}{2},\,\frac{2+8}{2}\right)=(5,\,5)", r"\((5,5)\)"),
    '5.166': ett(MITT, r"\left(\frac{2+8}{2},\,\frac{2+6}{2}\right)=(5,\,4)", r"\((5,4)\)"),
    '3.674': ett(AVST, r"d=\sqrt{(2-(-3))^2+(13-1)^2}=\sqrt{25+144}=\sqrt{169}=13", "13 längdenheter"),
    '3.675': ett(AVST, r"d=\sqrt{(8-0)^2+(10-(-5))^2}=\sqrt{64+225}=\sqrt{289}=17", "17 längdenheter"),
    '3.676': ett(AVST, r"d=\sqrt{(4-1)^2+(3-1)^2}=\sqrt{13}\approx3{,}61", "cirka 3,61 längdenheter"),
    '3.677': ett(AVST, r"d=\sqrt{9^2+12^2}=\sqrt{225}=15", "15 längdenheter", 'Origo är punkten (0, 0).'),
    '3.683': ett(AVST, r"d=\sqrt{(13-1)^2+(7-2)^2}=\sqrt{144+25}=13", "13 km"),
    '5.114': ett(AVST, r"d=\sqrt{(8-2)^2+(9-1)^2}=\sqrt{36+64}=10", "10 km"),
    '5.159': ett(AVST, r"d=\sqrt{(4-1)^2+(5-1)^2}=\sqrt{9+16}=5", "5 m"),
    '3.320': mc('En axelparallell rektangel har sidor längs rutnätet', r'D har samma x-koordinat som A och samma y-koordinat som C.', r"\(D=(2,5)\)"),
    '3.667': mc('En punkt på y-axeln har x-koordinaten 0', r'Det gäller \(Q=(0,4)\).', 'Q'),
    '3.668': mc('Avståndet till x-axeln är y-koordinatens storlek', r'\(P=(5,-3)\) ligger 3 längdenheter under x-axeln.', "3 längdenheter"),
    '3.662': ett(r"Rektangelns area: \(A=b\cdot h\)", r"A=6\cdot4=24", "24 areaenheter", 'Räkna rutorna: 6 i bredd och 4 i höjd.'),
    '3.672': ett(r"Parallellogrammets area: \(A=b\cdot h\)", r"A=6\cdot3=18", "18 areaenheter", 'Höjden mäts vinkelrätt mot basen.'),
    '3.653': ett('Hela rektangeln minus hörnet som saknas', r"10\cdot6-4\cdot3=60-12=48", "48 m²"),
    '1.685': mc(r"I \(y=kx+m\) är \(m\) där linjen skär y-axeln och \(k\) lutningen", r'\(m=1\) betyder skärning med y-axeln i 1, och \(k=-2\) att linjen lutar nedåt.', 'A'),
    '1.711': ([(r"Sätt in punkten i \(y=3x+m\)", r"7=3\cdot2+m"), (r"Lös ut \(m\)", r"m=7-6=1")], r"\(m=1\)"),
    # normalfördelning, regression och korrelation
    '4.50': ett(NORM, r"72+2\cdot5=82", "82 cm"),
    '4.154': ett(NORM, r"50-2\cdot8=34", "34 besökare"),
    '4.196': ett(NORM, r"50+4=54", "54"),
    '4.214': ett(NORM, r"80+6=86", "86 cm"),
    '4.107': mc('Liten standardavvikelse ger en smal och hög kurva', 'Värdena ligger då tätt kring medelvärdet.', 'Kurva C'),
    '4.198': mc('Positivt samband: y tenderar att öka när x ökar', None, 'Positivt linjärt samband'),
    '4.199': mc(KORR, r'Ett starkt negativt samband har \(r\) nära \(-1\).', r"\(r=-0{,}92\)"),
    '4.219': mc(KORR, 'Punkterna ligger nära en stigande linje, så r ligger nära 1.', r"\(r=0{,}93\)"),
    '4.220': mc(KORR, r'\(r=-0{,}85\) är negativt och nära \(-1\).', 'Ett starkt negativt linjärt samband'),
    '5.170': mc(KORR, r'\(r=-0{,}91\) är negativt och nära \(-1\).', 'Ett starkt negativt linjärt samband'),
    '4.227': mc(KORR, r'\(r=-0{,}63\) har negativt tecken.', 'Negativt'),
    '5.141': mc(KORR, r'\(r=-0{,}72\) har negativt tecken: högre pris hänger ihop med färre sålda enheter.', 'Negativt'),
    '4.228': ett(r"Styrkan avgörs av \(|r|\)", r"|-0{,}81|=0{,}81>0{,}42", r"\(r=-0{,}81\)"),
    '4.222': ett(REGR, r"y=2{,}5\cdot4+6=16", "16"),
    '4.229': ett(REGR, r"y=3{,}5\cdot4+12=26", "26"),
    '2.903': ett(REGR, r"y=3{,}5\cdot4+12=26", "26 kr"),
    '5.154': ett(REGR, r"y=1{,}8\cdot10+12=30", "30"),
    '5.167': ett(REGR, r"S(4)=48+1{,}5\cdot4=54", "54"),
    '5.155': ett(REGR, r"T(5)=8\cdot5+20=60", "60 min"),
    '2.906': ett(r"Startvärdet är modellens värde när \(x=0\)", r"y=-2{,}5\cdot0+40=40", "40 liter"),
    '4.223': mc(r"I \(y=kx+m\) är \(k\) ökningen per enhet av \(x\)", r'1,8 är ökningen i cm när t ökar med 1 vecka.', 'Höjden ökar med 1,8 cm per vecka.'),
    '4.225': mc(r"I \(y=kx+m\) är \(m\) värdet när \(x=0\)", 'Kostnaden är 45 kr redan innan man har kört.', 'En fast startavgift på 45 kr.'),
    '5.145': mc(r"I \(y=kx+m\) är \(k\) ökningen per enhet av \(x\)", r'Här är \(k=12\).', "12 minuter"),
    '4.230': ett('Skillnaden mätvärde minus modellvärde', r"49-52=-3", r"\(-3\)"),
    '5.160': mc('Percentil: andelen observationer som ligger på eller under värdet', None, 'Ungefär 90 % av väntetiderna är lika långa eller kortare.'),
    '5.171': ett(r"Kvartilavstånd: \(Q_3-Q_1\)", r"8-3=5", "5", r'Läs av \(Q_1=3\) och \(Q_3=8\) i lådagrammet.'),
    # exponentialmodeller och programmens tillämpningar
    '5.112': ett(EXPM, r"L(4)=18\,000\cdot1{,}12^4\approx28\,300", "cirka 28 300 läsare"),
    '5.153': ett(EXPM, r"25\,000\cdot1{,}04^3\approx28\,100", "cirka 28 100 kr"),
    '5.172': ett(EXPM, r"A(2)=2\,000\cdot1{,}10^2=2\,000\cdot1{,}21=2\,420", "2 420"),
    '5.137': ett(FFAKT, r"1+0{,}06=1{,}06", "1,06"),
    '5.143': ett(FFAKT, r"1-0{,}08=0{,}92", "0,92"),
    '5.149': ett(FFAKT, r"1-0{,}12=0{,}88", "0,88"),
    '5.140': ett(r"En kvadrat är aldrig negativ: \(-8(p-45)^2\le0\)", r"V\ \text{störst när}\ p-45=0\ \Rightarrow\ p=45", "45 kr"),
    '5.152': ett(r"En kvadrat är aldrig negativ: \(-2(x-30)^2\le0\)", r"V_{\max}=0+1\,800=1\,800\quad\text{när }x=30", "1 800 kr"),
    '5.146': ([('Arean som funktion av x', r"A(x)=x(12-x)"), (SYM, r"\text{nollställen }0\text{ och }12:\quad x=\frac{0+12}{2}=6")], r"\(x=6\) m"),
    '5.158': ett(FUNK, r"S(5)=\frac{100}{5^2}=\frac{100}{25}=4", "4"),
    '5.161': ett(FUNK, r"\Delta p=0{,}02\cdot50^2=0{,}02\cdot2\,500=50", "50 Pa"),
    '5.163': ([('Låt gren B ha flödet x', r"x+(x+10)=70"), (r"Lös ut \(x\)", r"2x=60\quad\Rightarrow\quad x=30")], "A: 40 L/min, B: 30 L/min"),
    # tabeller och diagram
    '4.307': mc(TAB, 'På raden för 0 husdjur står 5 elever.', "5 elever"),
    '4.506': ett('Addera säsongerna', r"11+14+9+16=50", "50 matcher"),
    '4.507': ett('Addera spelarna med storlek 40 och större', r"7+4+2=13", "13 spelare"),
    '4.509': ett('Ta skillnaden mellan orterna', r"6\,100-4\,200=1\,900", "1 900 invånare"),
    '4.309': mc(DIAG, 'Den högsta punkten ligger vid torsdag, med 80 besök.', "Torsdag"),
    '4.500': mc(DIAG, 'Stapeln för banan når upp till 6.', "6 elever"),
    '4.502': mc(DIAG, 'Punkten vid klockan 12 ligger på 22 °C.', "22 °C"),
    '4.503': mc(DIAG, 'Linjen når sin högsta punkt vid klockan 13, med 150 besökare.', "Klockan 13"),
    '4.505': mc(DIAG, 'Den största sektorn är uppvärmning, 45 %.', "Uppvärmning"),
    '4.510': mc(DIAG, 'Den lägsta stapeln är onsdagens, 10 minuter.', "Onsdag"),
    '4.501': ett('Läs av staplarna och ta skillnaden', r"50-20=30", "30 böcker"),
    '4.508': ett('Läs av priserna och ta skillnaden', r"18-12=6", "6 kr"),
    '4.313': ett(ANDEL, r"0{,}25\cdot240=60", "60 elever", 'Simningens sektor är 25 %.'),
    '4.504': ett(ANDEL, r"0{,}25\cdot200=50", "50 elever", 'Orienteringens sektor är en fjärdedel, 25 %.'),
    '4.511': ett(ANDEL, r"0{,}50\cdot40=20", "20 elever", 'Hälften av cirkeln är cykel.'),
}
