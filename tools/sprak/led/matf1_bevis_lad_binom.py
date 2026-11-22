# Ma5 lådprincipen, binomialsatsen, talbaser, SGD, induktion och bevis: egna ledtrådar (2026-11-22).
LAD = r"Vilka är lådorna och vilka är föremålen? Om n föremål läggs i k lådor hamnar minst \(\lceil n/k\rceil\) i någon låda."
LADMIN = r"Tänk på det värsta fallet: hur många kan du ta utan att få tillräckligt många av samma sort? Ett föremål till räcker då."
REST = r"Lådorna är de möjliga resterna. Hur många olika rester finns vid division med det talet?"
PAR = r"Dela in talen i par som hör ihop. Hur många par finns det, och hur många tal väljs?"
BIN = r"Den allmänna termen i \((a+b)^n\) är \(\binom nk a^{n-k}b^k\). Välj k så att x får rätt exponent och glöm inte konstanterna och tecknen."
PASCAL = r"Använd binomialsatsen eller Pascals triangel: \((a+b)^n=\sum\binom nk a^{n-k}b^k\)."
TILL10 = r"Multiplicera varje siffra med basen upphöjd till platsens nummer, räknat från 0 längst till höger, och addera."
FRAN10 = r"Dela upprepat med den nya basen och skriv upp resterna. Resterna läst nedifrån och upp ger siffrorna."
BASRAKN = r"Räkna som vanligt kolumn för kolumn, men en tiotalsövergång sker när summan når basen, inte 10."
SGD = r"Primtalsfaktorisera talen. SGD är produkten av de gemensamma primfaktorerna med den minsta exponenten."
MGM = r"Primtalsfaktorisera talen. MGM är produkten av alla primfaktorer med den största exponenten."
IND = r"Visa basfallet. Anta sedan att påståendet gäller för \(n=k\) och visa att det då gäller för \(n=k+1\)."
INDSUM = IND + r" Lägg till nästa term på båda sidor av antagandet."
INDDEL = IND + r" Skriv uttrycket för \(k+1\) så att uttrycket för k syns."
MOTS = r"Anta motsatsen till det som ska visas och visa att det leder till något orimligt."
KONTRA = r"Visa det kontrapositiva påståendet: om n inte har egenskapen, så har inte \(n^2\) det heller."
JAMN = r"Skriv jämna tal som \(2a\) och udda tal som \(2a+1\), där a är ett heltal."
DELB = r"\(a\mid b\) betyder att \(b=a\cdot k\) för något heltal k."
L = {
    # ---------- lådprincipen ----------
    '1.19': LAD, '1.38': LADMIN, '1.51': PAR + r" Par: \(\{1,2\},\{3,4\},\ldots\).",
    '1.59': LADMIN, '1.60': LAD, '1.61': REST, '1.62': LAD + r" Hur många heltal finns från 150 till 159?",
    '1.63': PAR + r" Par: \(\{1,12\},\{2,11\},\ldots\).", '1.64': PAR + r" Par: \(\{1,2\},\{3,4\},\ldots\).",
    '1.65': LAD,
    '1.66': r"Dela kvadraten i fyra lika stora kvadrater. Två punkter hamnar i samma lilla kvadrat. Hur lång är dess diagonal?",
    '1.68': LAD, '1.119': LAD, '1.133': LADMIN, '1.134': REST, '1.135': LADMIN, '1.150': LADMIN,
    '1.151': PAR + r" Par: \(\{1,2\},\{3,4\},\ldots,\{19,20\}\).",
    '1.393': REST, '1.396': REST,
    '1.504': r"Det finns 10 möjliga entalssiffror. " + LAD,
    '1.505': LAD, '1.506': LADMIN, '1.507': LAD, '1.508': LAD,
    # ---------- binomialsatsen ----------
    '1.22': BIN, '1.401': BIN, '1.36': BIN, '1.49': BIN, '1.95': BIN, '1.97': BIN,
    '1.101': r"Koefficienten framför \(x^2\) i \((1+x)^n\) är \(\binom n2=\frac{n(n-1)}{2}\). Sätt den lika med 45.",
    '1.126': BIN, '1.144': BIN, '1.157': BIN,
    '1.533': PASCAL, '1.534': PASCAL, '1.535': PASCAL, '1.538': PASCAL, '1.543': PASCAL, '1.545': PASCAL + r" Tecknen växlar eftersom \(-1\) upphöjs.",
    '1.602': BIN, '1.604': BIN, '1.605': BIN,
    '1.606': r"Den konstanta termen är den utan x.",
    '1.607': BIN,
    '1.608': r"Binomialkoefficienterna \(\binom6k\) är störst i mitten av Pascals triangel.",
    '1.609': r"Utvecklingen av \((a+b)^n\) har en term för varje k från 0 till n.",
    # ---------- talbaser ----------
    '2.351': TILL10, '2.53': TILL10, '2.63': TILL10, '2.356': TILL10, '2.83': TILL10, '2.85': TILL10, '2.366': TILL10,
    '2.84': FRAN10, '2.138': FRAN10, '2.165': FRAN10, '2.168': FRAN10,
    '2.86': BASRAKN, '2.170': BASRAKN,
    '2.206': r"Räkna kolumn för kolumn. När du lånar från nästa kolumn får du 6, inte 10.",
    # ---------- SGD och MGM ----------
    '2.161': r"Antalet paket är SGD av 180 och 252. " + SGD,
    '2.163': r"Plattans sida ska dela båda måtten. " + SGD,
    '2.207': SGD, '2.210': SGD,
    '2.214': r"Antalet kassar är SGD av de tre talen. " + SGD,
    '2.346': r"Visa att varje tal som delar a och b också delar a och \(a+b\), och omvänt.",
    '2.218': r"Plattans sida ska dela båda måtten. " + SGD,
    '2.515': SGD, '2.523': SGD, '2.555': SGD,
    '2.649': {'b': SGD},
    '2.650': {'b': MGM},
    # ---------- induktionsbevis ----------
    '2.12': r"Ett induktionsbevis har ett basfall och ett induktionssteg. Varför räcker de tillsammans för att nå varje heltal?",
    '2.36': INDSUM, '2.37': INDDEL + r" Utveckla \((k+1)^3+2(k+1)\).",
    '2.40': INDSUM, '2.45': INDSUM, '2.47': INDSUM, '2.75': INDSUM, '2.111': INDSUM, '2.133': INDSUM,
    '2.42': r"Exempel visar bara att påståendet gäller för just de talen. Vad måste visas för att det ska gälla för alla?",
    '2.43': r"Här behövs att formeln gäller för två föregående index. Visa två basfall och använd rekursionen i steget.",
    '2.46': IND + r" Använd rekursionen \(F_{k+3}=F_{k+2}+F_{k+1}\).",
    '2.48': IND + r" Använd att \(2^{k+1}=2\cdot2^k\).",
    '2.50': r"Undersök steget från \(k=1\) till \(k=2\). Överlappar mängderna då?",
    '2.60': INDDEL + r" Skriv \(5^{2(k+1)}=25\cdot5^{2k}\).",
    '2.76': INDDEL + r" Skriv \(7^{2(k+1)}=49\cdot7^{2k}\).",
    '2.112': INDDEL + r" Skriv \(4^{k+1}=4\cdot4^k\).",
    '2.544': r"Vad måste vara sant innan induktionssteget kan användas?",
    '2.545': r"Induktionssteget ska ta dig ett steg vidare.",
    '2.548': r"Det finns bara 10 möjliga entalssiffror.",
    # ---------- indirekta bevis och motsägelse ----------
    '2.51': MOTS + r" Anta att \(\sqrt2=p/q\) i förkortad form och kvadrera.",
    '2.52': MOTS + r" Multiplicera alla primtal och lägg till 1.",
    '2.59': MOTS + r" Anta att \(\sqrt2+\sqrt3=r\) är rationellt och kvadrera.",
    '2.113': MOTS + r" Om n är jämnt, vad blir då \(n^2\)?",
    '2.134': MOTS + r" Om q är det minsta positiva rationella talet, vad är då \(q/2\)?",
    '2.144': KONTRA,
    '2.148': KONTRA + r" Skriv n som \(3k+1\) eller \(3k+2\).",
    '2.301': r"Motsägelsebeviset börjar med motsatsen till det som ska visas.",
    '2.302': r"Motsägelsebeviset börjar med motsatsen till det som ska visas.",
    '2.303': r"Vad betyder det att ett antagande leder till en motsägelse?",
    '2.304': r"Motsägelsebeviset börjar med motsatsen till det som ska visas.",
    '2.305': r"Det är svårt att gå direkt från \(n^2\) till n. Kan du gå åt andra hållet?",
    '2.312': MOTS + r" Om N är det största jämna talet, vad är då \(N+2\)?",
    '2.314': MOTS + r" Skriv de udda talen som \(2a+1\) och \(2b+1\), där a och b är heltal.",
    '2.316': KONTRA,
    '2.541': r"Det är svårt att gå direkt från \(n^2\) till n. Kan du gå åt andra hållet?",
    '2.543': r"Motsägelsebeviset börjar med motsatsen till det som ska visas.",
    '2.547': r"Ett enda fall där påståendet inte stämmer räcker.",
    '2.572': r"Ett indirekt bevis vänder och negerar båda leden i implikationen.",
    '2.573': r"Motsägelsebeviset börjar med motsatsen till det som ska visas.",
    '2.576': r"Ett enda fall där påståendet inte stämmer räcker.",
    '2.577': r"Ett indirekt bevis vänder och negerar båda leden i implikationen.",
    '2.578': r"Vad betyder det att ett antagande leder till en motsägelse?",
    # ---------- direkta bevis ----------
    '2.141': JAMN, '2.142': JAMN,
    '2.143': r"Skriv talen som \(\frac ab\) och \(\frac cd\) med heltal och addera.",
    '2.146': DELB + r" Skriv b och c på det sättet och sätt in.",
    '2.147': r"Skriv det udda talet som \(2k+1\) och kvadrera. Ett av talen k och \(k+1\) är jämnt.",
    '2.150': r"Bland tre på varandra följande heltal finns alltid ett jämnt tal och ett som är delbart med 3.",
    '2.315': DELB + r" Skriv talen som \(5a\) och \(5b\).",
    '2.508': DELB + r" Skriv b och c som multipler av a och sätt in i \(3b-2c\).",
    '2.510': r"Skriv talen som n och \(n+1\), kvadrera och addera. Är summan av formen \(2k+1\)?",
    '2.539': r"Hur skrivs ett jämnt heltal med en heltalsvariabel?",
    '2.540': r"Hur skrivs ett udda heltal med en heltalsvariabel?",
    '2.542': DELB,
    '2.546': r"Talen n och \(n+1\) följer direkt på varandra. Vad vet du om två sådana tal?",
    '2.569': r"Hur skrivs ett jämnt heltal med en heltalsvariabel?",
    '2.570': r"Hur skrivs ett udda heltal med en heltalsvariabel?",
    '2.571': r"Vilka rester kan ett tal ge vid division med 3 om resten inte är 0?",
    '2.574': DELB,
    '2.575': r"Talen n och \(n+1\) följer direkt på varandra. Vad vet du om två sådana tal?",
}
