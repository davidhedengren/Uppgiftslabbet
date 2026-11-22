# Ma5 förändringshastigheter, generaliserade integraler och talföljder: egna ledtrådar (2026-11-22).
CIRK = r"Arean är \(A=\pi r^2\). Derivera med avseende på tiden: \(\frac{dA}{dt}=2\pi r\frac{dr}{dt}\)."
OMKR = r"Omkretsen är \(O=2\pi r\), så \(\frac{dO}{dt}=2\pi\frac{dr}{dt}\)."
KVAD = r"Arean är \(A=s^2\), så \(\frac{dA}{dt}=2s\frac{ds}{dt}\)."
KUB = r"Volymen är \(V=s^3\), så \(\frac{dV}{dt}=3s^2\frac{ds}{dt}\)."
KLOT = r"Volymen är \(V=\frac{4\pi r^3}{3}\), så \(\frac{dV}{dt}=4\pi r^2\frac{dr}{dt}\)."
CYLH = r"Volymen är \(V=\pi r^2h\) med konstant r. Derivera med avseende på tiden."
KON = r"Likformighet ger radien uttryckt i djupet. Skriv konens volym med bara h och derivera med avseende på tiden."
STEGE = r"Pythagoras sats ger \(x^2+y^2=L^2\). Derivera med avseende på tiden: \(2x\frac{dx}{dt}+2y\frac{dy}{dt}=0\)."
PYTH = r"Avståndet ges av Pythagoras sats. Derivera sambandet med avseende på tiden och sätt in värdena först efteråt."
LIM_OO = r"Ersätt \(\infty\) med en variabel b, beräkna integralen och låt b gå mot oändligheten."
LIM_0 = r"Integranden är inte definierad vid gränsen. Ersätt gränsen med en variabel, beräkna integralen och undersök gränsvärdet."
PTEST = r"Beräkna integralen med en variabel som gräns och undersök när gränsvärdet blir ändligt. Jämför exponenten med 1."
ARIT = r"Skillnaden mellan termerna är konstant. Använd \(a_n=a_1+(n-1)d\)."
SUMARIT = r"Summan av en aritmetisk talföljd är antalet termer gånger medelvärdet av första och sista termen."
SKRIV = r"Sätt in k = 1, 2, 3, … i uttrycket och addera termerna."
SIGMA = r"Hitta ett uttryck för term nummer k och skriv summan som \(\sum\) med rätt start- och slutindex."
L = {
    # ---------- talföljder ----------
    '2.405': SUMARIT, '2.415': SUMARIT, '2.430': SUMARIT, '2.107': SUMARIT,
    '2.02': SKRIV, '2.72': SKRIV, '2.105': SKRIV + r" Här börjar k på 0.",
    '2.408': ARIT, '2.423': ARIT, '2.438': ARIT,
    '2.04': SKRIV + r" Termerna bildar en geometrisk talföljd.",
    '2.55': r"Jämför termerna med kvadrattalen 1, 4, 9, 16, 25.",
    '2.67': r"Skillnaden mellan termerna är densamma hela tiden.",
    '2.97': r"Jämför termerna med \(1^2,2^2,3^2,\ldots\).",
    '2.98': r"Jämför termerna med kvadrattalen. Hur mycket större är varje term än \(n^2\)?",
    '2.416': r"Använd formeln \(\sum_{k=1}^nk^2=\frac{n(n+1)(2n+1)}{6}\).",
    '2.421': r"Använd formeln \(\sum_{k=1}^nk^2=\frac{n(n+1)(2n+1)}{6}\).",
    '2.123': ARIT,
    '2.16': r"Dela upp summan i \(5\sum k\) och \(\sum2\), och använd att \(\sum_{k=1}^nk=\frac{n(n+1)}{2}\).",
    '2.73': SIGMA, '2.106': SIGMA, '2.190': SIGMA + r" Hur många termer finns det?",
    '2.128': r"Skriv ut termerna från \(k=3\) till \(k=7\) och addera dem.",
    '2.154': SUMARIT + r" Räkna antalet termer från \(k=3\) till \(k=12\).",
    '2.189': SUMARIT + r" Räkna antalet termer från \(k=2\) till \(k=6\).",
    '2.191': r"Sätt in n = 1, 2, 3 och 4 i formeln.",
    '2.193': r"Dela upp summan i \(2\sum k-\sum1\) och använd att \(\sum_{k=1}^nk=\frac{n(n+1)}{2}\).",
    '2.194': r"Använd att \(\sum_{k=1}^nk=\frac{n(n+1)}{2}\).",
    # ---------- generaliserade integraler ----------
    '3.155': LIM_OO, '3.156': LIM_OO, '3.05': LIM_OO,
    '3.04': PTEST, '3.06': PTEST, '3.17': PTEST + r" Problemet ligger vid \(x=2\).",
    '3.159': LIM_OO + r" Jämför sedan \(I(2a)\) med \(I(a)\).",
    '3.16': r"Arean är \(\int_1^\infty\frac1{x^2}\,dx\). " + LIM_OO,
    '3.25': LIM_OO, '3.35': LIM_OO, '3.36': LIM_OO,
    '3.38': LIM_0, '3.88': LIM_0,
    '3.39': PTEST, '3.59': LIM_OO,
    '3.61': r"Integranden är inte definierad vid \(x=0\), som ligger inne i intervallet. Dela integralen där och undersök varje del.",
    '3.62': PTEST, '3.89': PTEST,
    '3.106': LIM_OO, '3.107': LIM_OO,
    '3.108': LIM_0 + r" Den primitiva funktionen till \(\ln x\) är \(x\ln x-x\).",
    '3.269': LIM_OO, '3.270': LIM_OO, '3.271': LIM_OO,
    '3.272': LIM_OO + r" Den primitiva funktionen är \(\ln x\).",
    '3.273': LIM_OO, '3.274': LIM_0, '3.276': LIM_0,
    # ---------- förändringshastigheter ----------
    '3.191': CIRK, '3.20': CIRK, '3.246': CIRK, '3.247': CIRK, '3.248': CIRK, '3.261': CIRK,
    '3.44': r"Skriv arean med diametern: \(A=\frac{\pi d^2}{4}\). Derivera med avseende på tiden.",
    '3.193': KON, '3.205': KON, '3.11': KON + r" Tänk på enheterna: 50 liter är 0,050 m³.",
    '3.48': r"Skriv konens volym med bara h, eftersom \(r=h/3\). Derivera med avseende på tiden.",
    '3.113': r"Skriv konens volym med bara h, eftersom \(r=2h\). Derivera med avseende på tiden.",
    '3.09': PYTH + r" Tänk på enheterna km/h och m.",
    '3.10': PYTH,
    '3.112': PYTH + r" Tänk på enheterna km/h och m.",
    '3.115': PYTH + r" Höjden är konstant, så bara den vågräta sträckan ändras.",
    '3.19': STEGE, '3.47': STEGE,
    '3.100': PYTH + r" Repets längd är hypotenusan och kajens höjd är konstant.",
    '3.27': KVAD, '3.249': KVAD, '3.250': KVAD, '3.251': KVAD,
    '3.262': KVAD + r" Skriv om mm/s till cm/s först.",
    '3.45': KLOT, '3.69': KLOT + r" Lös ut \(dr/dt\).", '3.101': KLOT + r" Lös ut \(dr/dt\).",
    '3.255': KLOT, '3.256': KLOT, '3.264': KLOT,
    '3.46': KUB, '3.252': KUB, '3.253': KUB, '3.254': KUB, '3.263': KUB,
    '3.66': r"Arean är \(A=lb\). Derivera med produktregeln med avseende på tiden.",
    '3.67': CYLH, '3.257': CYLH, '3.258': CYLH,
    '3.111': CYLH + r" Lös ut \(dh/dt\).",
    '3.265': CYLH + r" Lös ut \(dh/dt\).",
    '3.266': r"Volymen är \(V=\pi r^2h\) med konstant h. Derivera med avseende på tiden och skriv om mm/s till cm/s.",
    '3.68': r"Likformiga trianglar ger ett samband mellan personens avstånd till lyktan och skuggans längd. Derivera det med avseende på tiden.",
    '3.79': OMKR, '3.259': OMKR, '3.260': OMKR,
    '3.98': OMKR + r" Använd det för att bestämma \(dr/dt\) och sedan \(dA/dt\).",
    '3.110': r"Kvadratens area är \(A=d^2/2\), uttryckt med diagonalen. Derivera med avseende på tiden.",
    '3.114': r"\(\tan v=\frac{y}{12}\), där y är höjden på väggen. Derivera båda leden med avseende på tiden.",
    '3.117': CIRK + r" Bestäm \(dr/dt\) och använd sedan \(\frac{dO}{dt}=2\pi\frac{dr}{dt}\).",
    '3.267': r"\(\frac{dA}{dt}=2\pi r\frac{dr}{dt}\). Vad händer med \(\frac{dr}{dt}\) när r växer men \(\frac{dA}{dt}\) är konstant?",
    '3.268': r"\(\frac{dV}{dt}=4\pi r^2\frac{dr}{dt}\). Vad händer med \(\frac{dr}{dt}\) när r ändras men \(\frac{dV}{dt}\) är konstant?",
}
