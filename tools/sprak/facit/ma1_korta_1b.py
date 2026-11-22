# Ma1 kapitel 1, del 2: ekvationer med parenteser och bråk, problemlösning, mönster, uttryck (2026-11-22).
import os
exec(open(os.path.join('tools', 'sprak', 'facit', 'ma1_korta_gemensamt.py'), encoding='utf-8').read())
SAMLA = 'Samla variabeltermerna för sig och konstanterna för sig'
MULTIN = 'Multiplicera in faktorn i varje term i parentesen'
MINUSP = 'Ett minustecken framför en parentes byter tecken på alla termer i den'
LIKA = 'Gör samma sak i båda leden'
DELA = 'Dela båda leden med talet framför parentesen'
MULTN = 'Multiplicera båda leden med nämnaren'
EKVST = 'Kalla det okända talet x och ställ upp en ekvation'
VARDE = 'Ersätt variabeln med talet och räkna'
FORMEL = 'Sätt in de kända värdena i formeln'
MONST = 'Se hur talen ändras från ett steg till nästa'
TRI = 'Vinkelsumman i en triangel är 180°'
OMKR = r"Rektangelns omkrets: \(O=2l+2b\)"


def ekv(steg, x):
    return (steg, rf"\(x={x}\)")


def prob(ekvation, losning, svar, text=None):
    return ([(EKVST, ekvation, text) if text else (EKVST, ekvation), (LIKA, losning)], svar)


F = {
    # ekvationer med parenteser
    '1.1324': ekv([(DELA, r"x+3=7"), (LIKA, r"x=4")], 4),
    '1.1333': ekv([(DELA, r"x+4=7"), (LIKA, r"x=3")], 3),
    '1.1344': ekv([(DELA, r"x+1=3{,}5"), (LIKA, r"x=2{,}5")], "2{,}5"),
    '1.1325': ekv([(MULTIN, r"3x-3=2x+5"), (SAMLA, r"x=8")], 8),
    '1.1326': ekv([(MINUSP, r"-x+4=1"), (LIKA, r"-x=-3\quad\Rightarrow\quad x=3")], 3),
    '1.1327': ekv([(MINUSP, r"12-x+3=10\quad\Rightarrow\quad15-x=10"), (LIKA, r"x=5")], 5),
    '1.1328': ett(MINUSP, r"9-(2x-1)=9-2x+1=10-2x", r"\(10-2x\)"),
    '1.1330': ([(MULTIN, r"4x=3x+6"), (SAMLA, r"x=6")], r"\(x=6\), alltså 6 cm"),
    '1.1331': ([(DELA, r"x+25=95"), (LIKA, r"x=70")], "70 kr"),
    '1.1332': ekv([(MULTIN, r"6x-3=15"), (LIKA, r"6x=18\quad\Rightarrow\quad x=3")], 3),
    '1.1334': ett(r"Sätt in \(x=2\) i båda leden", r"\text{VL}=3(2+1)=9,\qquad\text{HL}=4\cdot2+1=9", 'Ja, båda leden blir 9.'),
    '1.1335': ekv([(MULTIN, r"2x+10=3x+6"), (SAMLA, r"10-6=3x-2x\quad\Rightarrow\quad x=4")], 4),
    '1.1336': ekv([(MULTIN, r"-2x+6=4"), (LIKA, r"-2x=-2\quad\Rightarrow\quad x=1")], 1),
    '1.1337': ekv([(r"Rektangelns area: \(A=b\cdot h\)", r"4(x+3)=32"), (DELA, r"x+3=8\quad\Rightarrow\quad x=5")], 5),
    '1.1338': ett(MULTIN, r"5(x-2)=5x-10", r"\(5x-10=20\)"),
    '1.1339': ([(DELA, r"x+2=6"), (LIKA, r"x=4")], "4 bitar"),
    '1.1340': ekv([(MULTIN, r"4x-8+3=11\quad\Rightarrow\quad4x-5=11"), (LIKA, r"4x=16\quad\Rightarrow\quad x=4")], 4),
    '1.1341': ekv([(MULTIN, r"2x-8=x"), (SAMLA, r"x=8")], 8),
    '1.1342': ([(DELA, r"x+10=16"), (LIKA, r"x=6")], "6 m"),
    '1.1343': ekv([(MINUSP, r"3x=20-x-4=16-x"), (SAMLA, r"4x=16\quad\Rightarrow\quad x=4")], 4),
    '1.1526': ekv([(MULTIN, r"2x+10=48"), (LIKA, r"2x=38\quad\Rightarrow\quad x=19")], 19),
    # ekvationer med bråk
    '1.1346': ekv([(MULTN, r"x=6\cdot4=24")], 24),
    '1.1347': ekv([(LIKA, r"\frac x5=3"), (MULTN, r"x=15")], 15),
    '1.1348': ekv([(MULTN, r"2x=24"), ('Dela med 2', r"x=12")], 12),
    '1.1349': ekv([(MULTN, r"x+3=14"), (LIKA, r"x=11")], 11),
    '1.1350': ekv([(MULTN, r"x+10=16"), (LIKA, r"x=6")], 6),
    '1.1351': ([(MULTN, r"x=3\cdot145=435")], "435 kr"),
    '1.1353': ekv([(r"Multiplicera båda leden med \(x\)", r"12=3x"), ('Dela med 3', r"x=4")], 4),
    '1.1354': ett(MULTN, r"5\cdot\frac x5+5\cdot1=5\cdot4\quad\Rightarrow\quad x+5=20", r"\(x+5=20\)"),
    '1.1355': ([(MULTN, r"x=3\cdot9=27")], "27 elever"),
    '1.1359': ekv([(MULTN, r"3x=36"), ('Dela med 3', r"x=12")], 12),
    '1.1360': ekv([(MULTN, r"x-1=12"), (LIKA, r"x=13")], 13),
    '1.1361': ([(LIKA, r"\frac x2=7"), (MULTN, r"x=14")], "14"),
    '1.1363': ([(EKVST, r"\frac x4=3", 'x är hela vägen i km.'), (MULTN, r"x=12")], "12 km"),
    '1.1527': ekv([(LIKA, r"\frac x3=6"), (MULTN, r"x=18")], 18),
    '1.1352': ett('Samma nämnare: addera täljarna', r"\frac x2+\frac x2=\frac{2x}{2}=x", r"\(x\)"),
    '1.1358': ett('Samma nämnare: addera täljarna', r"\frac x4+\frac x4=\frac{2x}{4}=\frac x2", r"\(\frac x2\)"),
    '1.1357': ett(FORL, r"\frac{6x}{3}=2x", r"\(2x\)"),
    '1.1356': ett(VARDE, r"\frac{12}{3}+\frac{12}{6}=4+2=6", "6"),
    '1.1365': ett('Att dela med 2 är samma sak som att multiplicera med en halv', r"\frac x2=\frac12\cdot x=0{,}5x", r"\(0{,}5x\)"),
    # problemlösning
    '1.1366': prob(r"3x+5=26", r"3x=21\quad\Rightarrow\quad x=7", "7"),
    '1.1367': prob(r"4x+30=230", r"4x=200\quad\Rightarrow\quad x=50", "50 kr", 'x är priset för en biljett.'),
    '1.1368': ett(EKVST, r"200+150x=1\,250", r"\(200+150x=1\,250\)", 'Startavgiften plus 150 kr för varje månad.'),
    '1.1369': prob(r"45+12x=189", r"12x=144\quad\Rightarrow\quad x=12", "12 km", 'x är antalet kilometer.'),
    '1.1370': prob(r"x+3x=48", r"4x=48\quad\Rightarrow\quad x=12", "12 år", 'x är Leos ålder.'),
    '1.1373': prob(r"x+(x+1)+(x+2)=48", r"3x+3=48\quad\Rightarrow\quad x=15", "15"),
    '1.1374': prob(r"x+2x=27", r"3x=27\quad\Rightarrow\quad x=9", "9 km"),
    '1.1375': prob(r"5x+3=43", r"5x=40\quad\Rightarrow\quad x=8", "8 bullar", 'x är antalet bullar i en påse.'),
    '1.1376': prob(r"130x+200=2\,280", r"130x=2\,080\quad\Rightarrow\quad x=16", "16 timmar"),
    '1.1377': prob(r"2x-7=25", r"2x=32\quad\Rightarrow\quad x=16", "16"),
    '1.1379': prob(r"99x=594", r"x=\frac{594}{99}=6", "6 månader"),
    '1.1380': prob(r"x+2x=36", r"3x=36\quad\Rightarrow\quad x=12", "12"),
    '1.1381': prob(r"x+(x-8)=30", r"2x=38\quad\Rightarrow\quad x=19", "19 kr", 'x är pennans pris.'),
    '1.1382': prob(r"x+(x+4)=20", r"2x=16\quad\Rightarrow\quad x=8", "8 m", 'x är den kortare delen.'),
    '1.1383': prob(r"4x=36", r"x=9", "9 cm", 'x är sidan.'),
    '1.1384': prob(r"600+150x=2\,400", r"150x=1\,800\quad\Rightarrow\quad x=12", "12 månader"),
    '1.1385': ([(SAMLA, r"40x-25x=60\quad\Rightarrow\quad15x=60"), ('Dela med 15', r"x=4")], "Efter 4 timmar"),
    '1.1524': prob(r"3x+5=50", r"3x=45\quad\Rightarrow\quad x=15", "15"),
    '1.1525': prob(r"250+99x=1\,834", r"99x=1\,584\quad\Rightarrow\quad x=16", "16 månader"),
    '1.1529': prob(r"x+3x=68", r"4x=68\quad\Rightarrow\quad x=17", "17 år", 'x är Livs ålder.'),
    '1.1371': ([(TRI, r"x+2x+60=180"), (LIKA, r"3x=120\quad\Rightarrow\quad x=40")], r"\(x=40^\circ\)"),
    '1.1522': ([(TRI, r"x+2x+60=180"), (LIKA, r"3x=120\quad\Rightarrow\quad x=40")], r"\(40^\circ\)"),
    '1.1378': ([('Omkretsen är summan av sidorna', r"x+x+10=34"), (LIKA, r"2x=24\quad\Rightarrow\quad x=12")], "12 cm"),
    '1.1521': ([(OMKR, r"2x+2\cdot6=34"), (LIKA, r"2x=22\quad\Rightarrow\quad x=11")], "11 cm"),
    '1.1530': ([(OMKR, r"2x+2(x+5)=90"), (MULTIN, r"4x+10=90\quad\Rightarrow\quad x=20")], "20 cm"),
    '1.1520': ([('Vågen väger jämnt: vänster sida = höger sida', r"3x+1=31"), (LIKA, r"3x=30\quad\Rightarrow\quad x=10")], "10 kg"),
    '1.1523': ([('Vågen väger jämnt: vänster sida = höger sida', r"4x+3=x+21"), (SAMLA, r"3x=18\quad\Rightarrow\quad x=6")], "6 kg"),
    '1.1531': ekv([(LIKA, r"0{,}4x=2{,}6+1{,}2=3{,}8"), ('Dela med 0,4', r"x=\frac{3{,}8}{0{,}4}=9{,}5")], "9{,}5"),
    '1.1372': ([('Kostnaderna är lika där linjerna skär varandra', r"300+2x=100+4x\quad\Rightarrow\quad200=2x\quad\Rightarrow\quad x=100"),
                ('Kontroll', r"300+2\cdot100=500=100+4\cdot100")], "Vid 100 km"),
    # ekvationer med x i båda leden
    '1.1300': ekv([(SAMLA, r"5x-2x=12\quad\Rightarrow\quad3x=12"), ('Dela med 3', r"x=4")], 4),
    '1.1302': ekv([(SAMLA, r"8x-5x=6\quad\Rightarrow\quad3x=6"), ('Dela med 3', r"x=2")], 2),
    '1.1304': ett('Subtrahera 3x i båda leden', r"7x-3x+2=18\quad\Rightarrow\quad4x+2=18", r"\(4x+2=18\)"),
    '1.1305': ([('Vågen väger jämnt: vänster sida = höger sida', r"3x+5=x+13"), (SAMLA, r"2x=8\quad\Rightarrow\quad x=4")], "4 kulor i varje påse"),
    '1.1309': ett(MULTIN, r"3(x+2)=3x+6", 'Oändligt många, eftersom leden är identiska.'),
    '1.1310': ekv([(SAMLA, r"10-2=x+x\quad\Rightarrow\quad8=2x"), ('Dela med 2', r"x=4")], 4),
    '1.1312': ([(SAMLA, r"3x-x=40\quad\Rightarrow\quad2x=40"), ('Dela med 2', r"x=20")], "20 minuter"),
    '1.1313': ([(SAMLA, r"20-14=2x-x\quad\Rightarrow\quad x=6")], "Efter 6 timmar"),
    '1.1314': ekv([(SAMLA, r"1{,}5x-0{,}5x=6-2\quad\Rightarrow\quad x=4")], 4),
    '1.1315': ([(r"Sätt in \(x=2\)", r"6+c=2+10"), (LIKA, r"c=6")], r"\(c=6\)"),
    '1.1316': ([(r"Sätt in \(x=5\)", r"5a=2\cdot5+15=25"), ('Dela med 5', r"a=5")], r"\(a=5\)"),
    '1.1318': ([('Tankarna innehåller lika mycket', r"200+30x=500+10x"), (SAMLA, r"20x=300\quad\Rightarrow\quad x=15")], "Efter 15 minuter"),
    '1.1319': ([(SAMLA, r"120-30=25x-15x\quad\Rightarrow\quad90=10x"), ('Dela med 10', r"x=9")], "Efter 9 veckor"),
    '1.1320': ([(SAMLA, r"4x-2x=12\quad\Rightarrow\quad2x=12"), ('Dela med 2', r"x=6")], r"\(x=6\), alltså 6 cm"),
    '1.1321': ekv([(SAMLA, r"11-2=4x-x\quad\Rightarrow\quad9=3x"), ('Dela med 3', r"x=3")], 3),
    '1.1322': ([(SAMLA, r"9x-5x=5+7\quad\Rightarrow\quad4x=12\quad\Rightarrow\quad x=3"), ('Kontroll', r"9\cdot3-7=20=5\cdot3+5")], "3"),
    '1.1323': ekv([(SAMLA, r"7x-4x=9-3\quad\Rightarrow\quad3x=6"), ('Dela med 3', r"x=2")], 2),
    # mönster
    '1.1500': ett(MONST, r"4\cdot4=16", "16 prickar", 'Figur n är en kvadrat med n prickar på varje sida.'),
    '1.1502': ett(MONST, r"17+5+5=27", "27", 'Antalet ökar med 5 för varje figur.'),
    '1.1504': ett(MONST, r"27\cdot3=81", "81", 'Varje tal är tre gånger så stort som det före.'),
    '1.1505': ett(MONST, r"7+4=11", "11", 'Talen ökar med 4.'),
    '1.1508': ([('Sätt uttrycket lika med 50', r"4n+2=50"), (LIKA, r"4n=48\quad\Rightarrow\quad n=12")], "Figur 12"),
    '1.1510': ett(MONST, r"9+1=10", "10 stolpar", 'Det behövs en stolpe mer än antalet sektioner.'),
    '1.1512': ett(r"I \(7n+3\) är 7 ökningen per figur", r"7(n+1)+3-(7n+3)=7", "7 stickor"),
    '1.1514': ett(MONST, r"n\cdot(n+1)", r"\(n(n+1)\)", 'Figur n har n rader med n + 1 prickar i varje.'),
    '1.1516': ett('Starthöjden minus minskningen', r"30-8\cdot1{,}5=30-12=18", "18 cm"),
    # algebraiska uttryck
    '1.1540': ett(VARDE, r"7\cdot4-3=28-3=25", "25"),
    '1.1541': ett(VARDE, r"(-2)^2-2\cdot(-2)=4+4=8", "8"),
    '1.1550': ett(VARDE, r"\frac{9+(-4)}{2}=\frac52=2{,}5", "2,5"),
    '1.1545': ett(FORMEL, r"S=1{,}5\cdot26+2=39+2=41", "Storlek 41"),
    '1.1546': ett(FORMEL, r"F=1{,}8\cdot(-10)+32=-18+32=14", "14 °F"),
    '1.1542': ett('En kvadrat har fyra lika långa sidor', r"s+s+s+s=4s", r"\(4s\)"),
    '1.1543': ett('Översätt orden till ett uttryck', r"\text{dubbla talet}=2x\quad\Rightarrow\quad2x-3", r"\(2x-3\)"),
    '1.1544': ett('Fast avgift plus kostnad per träning', r"150+40n", r"\(40n+150\) kr"),
    '1.1547': ett('Hönor har 2 ben och kor 4', r"2x+4y", r"\(2x+4y\)"),
    '1.1548': ([(r"Rektangelns area: \(A=b\cdot h\)", r"3(x+2)"), (MULTIN, r"3x+6")], r"\(3x+6\)"),
    '1.1549': ([('Skriv åldrarna', r"\text{Ali: }a,\quad\text{Bea: }a+4,\quad\text{Cem: }2(a+4)"), (MULTIN, r"a+a+4+2a+8=4a+12")], r"\(4a+12\)"),
}
