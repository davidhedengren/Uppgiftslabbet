# Ma3: nivå 3 i tunna områden (2026-10-26)

Inventering i Kunskapsgymmet (spelbara kort på nivå 3, Ma3c):

| Område | Nivå 3 | Totalt |
|---|---|---|
| trig_ekvationer | 2 | 23 |
| derivata_a_x | 3 | 31 |
| trig_ratvinkliga | 3 | 31 |
| sinussatsen_tva_fall | 3 | 16 |
| deriveringsregler | 3 | 52 |
| rationella_uttryck | 4 | 31 |
| forkorta_rationella | 4 | 44 |
| problemlosning_derivata | 4 | 26 |
| primitiva_villkor | 4 | 52 |
| integral_area | 4 | 69 |
| areasatsen | 4 | 33 |
| enhetscirkeln | 4 | 65 |

En annan session fyllde 2026-10-25 flera Ma3-områden med C-kort: derivatagraf, cosinus- och sinussatsen, funktioner, derivatans begrepp, primitiva funktioner, potensderivata och logaritmer. De områdena väntar därför.

Regressionstest: `tools/ma3-niva3-tunna-2026-10-26.test.js`.

## 1. Deriveringsregler: 6 kort, 2.1259–2.1264

| ID | Familj | Innehåll |
|---|---|---|
| 2.1259 | Beräkna derivatans värde | För vilka x är f′(x) = 9? Derivatan ger en andragradsekvation |
| 2.1260 | Derivera polynom | \((x^2+4)/\sqrt x\) skrivs om till potenser innan deriveringen |
| 2.1261 | Beräkna derivatans värde | Punkten på y = 2√x där tangenten är parallell med y = 0,5x + 3 (ändrat 2026-10-26, se nedan) |
| 2.1262 | Beräkna derivatans värde | Volymen i en tank: ändringshastigheten och när ökningen upphör |
| 2.1263 | Beräkna derivatans värde | Vilken funktion har f′(2) = 0 (flerval) |
| 2.1264 | Derivera polynom | En kvot förenklas innan deriveringen |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom. Inga räkneled behövde radbrytas.
- 2.1260 fick ”Svara exakt.”. Annars godtogs 3 för 2,75.
- Validatorn ger 224 fynd både före och efter ändringen.
- Alla Ma3-tester går igenom.
- Självrättningen testades med 16 svar, och alla gav väntat resultat.

## 2. Derivatan av aˣ: 6 kort, 2.1265–2.1270

De befintliga korten handlade mest om att derivera aˣ eller skriva om till basen e. De nya korten är tillämpningar:

| ID | Familj | Innehåll |
|---|---|---|
| 2.1265 | Derivera a^x | Befolkningens ökningstakt år 2030, 116 invånare per år |
| 2.1266 | Derivera a^x | När ett läkemedel minskar med 4 mg/h. Derivatan sätts till −4, och svaret är 3,6 h |
| 2.1267 | Derivera a^x | Tangenten till y = 2ˣ i x = 3: k ≈ 5,55 och m ≈ −8,64 |
| 2.1268 | Skriva a^x med basen e | Basen som ger lutningen 2 i x = 0 är a = e² |
| 2.1269 | Derivera a^x | Derivatan av 2⁻ˣ (flerval). De fel alternativen bygger på vanliga misstag |
| 2.1270 | Derivera a^x | Ökningstakten 477 kr/år jämförs med ökningen 487 kr under ett helt år |

Kontroller:

- I 2.1267 har m toleransen 0,011, så att −8,65 godtas. Det svaret får man om man räknar vidare med det avrundade k-värdet.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 6 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Alla Ma3-tester går igenom.
- Självrättningen testades med 15 svar, och alla gav väntat resultat.

## 3. Förkorta rationella uttryck: 6 kort, 1.965–1.970

| ID | Familj | Innehåll |
|---|---|---|
| 1.965 | Förkorta rationella uttryck | x bryts ut i täljaren, och nämnaren är en kvadrat: x/(x + 5), där −5 är förbjudet |
| 1.966 | Förkorta rationella uttryck | Täljare av tredje graden: x(x − 2)/(x + 2), där ±2 är förbjudna |
| 1.967 | Förkorta rationella uttryck | Förkorta först och lös sedan R(x) = 1/2, som ger x = −1 |
| 1.968 | Förenkla och ange definitionsvillkor | Vilket uttryck är lika med 1/(x + 1) (flerval) |
| 1.969 | Förkorta rationella uttryck | Faktorer med omvänt tecken: (3 − x)/(x + 3), där ±3 är förbjudna |
| 1.970 | Förenkla och ange definitionsvillkor | Hålet i grafen till (x² − 1)/(x − 1), punkten (1, 2) (figur utan synligt hål) |

Svarsformatet följer 1.440: ett förenklat uttryck och en lista med förbjudna x-värden.

Kontroller:

- I 1.970 togs den öppna ringen bort ur figuren, eftersom hålet annars kunde läsas av direkt.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 5 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades via `answerLayout`, alltså samma väg som appen använder, och 1.440 användes som referens.
  - Likvärdiga former godtas, till exempel (x² − 2x)/(x + 2) och −(x − 3)/(x + 3).
  - Teckenfel underkänns.

## 4. Rationella uttryck: 6 kort, 1.971–1.976

| ID | Innehåll |
|---|---|
| 1.971 | När uttrycket är noll (täljaren) och när det inte är definierat (nämnaren) |
| 1.972 | Konstanten c ur ett förbjudet värde och det andra förbjudna värdet: c = −12 och x = −6 |
| 1.973 | Medelkostnaden per produkt blir 65 kr vid 200 produkter |
| 1.974 | Definierat för alla x kräver att a är större än 0 (flerval) |
| 1.975 | Förbjudna värden i en summa av bråk: 0, 1 och 4 |
| 1.976 | Välj uttrycket som har definitionsmängden alla x utom 0 och 3 (flerval) |

Alla kort tillhör familjen ”Definitionsmängd för rationella uttryck”, utom 1.973 som tillhör ”Räkna med rationella uttryck”.

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- I 1.973 står M(x) på en egen rad.
- 3 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades på samma väg som appen använder, både `answerLayout` och `flersvar`.
  - Svaren godtas i valfri ordning i 1.975.
  - Svaren måste stå i rätt ordning i 1.971 och 1.972.

- 2.1261 byttes 2026-10-26. Kortet gällde först en parabel och en tangent parallell med en linje, och det liknade 3.1185 på nivå 2 för mycket. Nu gäller det y = 2√x, och svaret är (4, 4).

## 5. Problemlösning med derivata: 6 kort, 3.1246–3.1251

| ID | Familj | Innehåll |
|---|---|---|
| 3.1246 | Rörelse och hastighet | När hastigheten är som störst. Svaret får man med derivatan av v(t) |
| 3.1247 | Tolka derivata i modeller | Temperaturen kl. 08 uppskattas ur T(6) = 12 och T′(6) = −1,5 |
| 3.1248 | Tangenter och bevis | Var två tangenter till y = x² − 2x skär varandra |
| 3.1249 | Tolka derivata i modeller | Marginalvinsten V′(50) och den största vinsten |
| 3.1250 | Rörelse och hastighet | När en boll stannar och hur långt den har rullat |
| 3.1251 | Tangenter och bevis | f(2) och f′(2) ur tangentens ekvation (flerval) |

Kontroller:

- 3.1246 gäller nu för 0 ≤ t ≤ 2,5. Med 0 ≤ t ≤ 4 hade bilen backat efter t = 8/3, och farten 16 m/s vid t = 4 hade då varit störst.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 2 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 14 svar, och alla gav väntat resultat.

## 6. Integral och area: 6 kort, 3.1252–3.1257

| ID | Familj | Innehåll |
|---|---|---|
| 3.1252 | Integral som area under en graf | Area när grafen delvis ligger under x-axeln, 23/3 (figur, svaret exakt) |
| 3.1253 | Integralens egenskaper | Övre gränsen a = 11 så att ∫₁ᵃ 2x dx = 120 |
| 3.1254 | Integralens egenskaper | Symmetriskt intervall: x³-delen blir 0, och a = 13 |
| 3.1255 | Integral som area under en graf | Utrunnen volym ur ett flöde som minskar, 36 liter (figur) |
| 3.1256 | Integralens egenskaper | Arean ovanför x-axeln ur integralen och arean under, 5 |
| 3.1257 | Integralens egenskaper | Jämför ∫x, ∫x² och ∫x³ på [0, 1] utan att räkna (flerval) |

Kontroller:

- Kort 3.1254 var först ”bestäm k i ∫₀² (kx + 1) dx”. Validatorn flaggade VERY_SIMILAR_TEXT mot 3.159, och kortet byttes mot uppgiften om symmetri.
- Fyra heltalssvar byttes för att undvika facitkrockar.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 4 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 11 svar, och alla gav väntat resultat. Svaret 23/3 godtas och 7,67 underkänns, eftersom frågan säger ”exakt”.

## Generiska facit-rubriker rättade (2026-10-26)

En genomsökning av dagens nya mattekort hittade åtta rubriker som var allmänna mallfraser. Alla skrevs om så att de beskriver just det steget:

- Ma2 1.1233: ”Beräkna y”
- Ma2 1.1240: ”Sätt uttrycken lika” och ”Kontrollera”
- Ma2 2.1222: ”Två lösningar”
- Ma2 2.1234: ”Multiplicera ut” och ”Kvadratkomplettera”
- Ma3 1.973: ”Kontrollera”
- Ma3 3.1254: ”Lös ekvationen”

Båda regressionstesterna underkänner nu sådana rubriker.

## 7. Areasatsen (Ma3c): 6 kort, 4.567–4.572

| ID | Familj | Innehåll |
|---|---|---|
| 4.567 | Areasatsen | Kostnaden för en triangulär gräsmatta (14 m, 9 m, 110°), 5 032 kr (figur) |
| 4.568 | Sammansatta figurer | Regelbunden femhörning i en cirkel med radien 5 cm, 59,4 cm² (figur) |
| 4.569 | Sammansatta figurer | Parallellogrammens area ur diagonalerna 10 och 14 cm och vinkeln 60°. sin 120° = sin 60° ger 60,6 cm² (figur) |
| 4.570 | Sammansatta figurer | Areaförhållandet när AD:DB = 1:2, 8 cm² (figur) |
| 4.571 | Areasatsen | Vilken triangel har störst area? 30° och 150° ger samma area (flerval) |
| 4.572 | Areasatsen | Vinklar som ger halva den största arean, 30° och 150° |

Kontroller:

- I första versionen av figuren till 4.567 var vinkeln vid A spetsig, fast den var märkt 110°. Det rättades.
- Fyra etiketter låg för nära linjerna och flyttades. SVG-granskaren ger nu bara INFO om vinkelbågar.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 3 räkneled radbröts. Raden i 4.571 delades på fyra rader.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 12 svar, och alla gav väntat resultat. I 4.572 godtas vinklarna i valfri ordning.

## 8. Enhetscirkeln: 6 kort, 4.573–4.578

| ID | Familj | Innehåll |
|---|---|---|
| 4.573 | Symmetri och exakta värden | sin² 37° + sin² 53° = 1. Komplementvinklar ger trigonometriska ettan |
| 4.574 | Symmetri och exakta värden | cos 140°, cos 220° och cos 320° ur cos 40° ≈ 0,766 |
| 4.575 | Koordinater och vinklar | En punkt i fjärde kvadranten med x = 0,28: y = −0,96 och v ≈ 286,3° (figur) |
| 4.576 | Symmetri och exakta värden | Exakt värde av sin 150° · cos 300° + cos 135° · sin 45° = −1/4 |
| 4.577 | Koordinater och vinklar | Vinkeln där sin v = sin 50° och cos v = −cos 50° samtidigt (flerval) |
| 4.578 | Koordinater och vinklar | cos v ur sin v = −0,4 i tredje kvadranten, ≈ −0,917 |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 3 räkneled radbröts. Ledet i 4.576 delades i två.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 15 svar, och alla gav väntat resultat. Tecken- och kvadrantfel underkänns.

## 9. Trigonometriska ekvationer: 6 kort, 4.579–4.584

| ID | Innehåll |
|---|---|
| 4.579 | Skriv om 3 sin x − 1 = 0,2 och lös med räknare, x ≈ 23,6° och 156,4° |
| 4.580 | Exakt: 2 sin x + √3 = 0 ger 240° och 300° |
| 4.581 | tan x = √3 ger 60° och 240° (tangens upprepas var 180:e grad) |
| 4.582 | Höjden i ett pariserhjul: 20 − 18 cos v = 11 ger 60° och 300° |
| 4.583 | Antal lösningar till sin x = 0,8 på två varv, 4 (flerval) |
| 4.584 | Den andra skärningspunkten med y = k ur grafen och värdet på k (figur) |

Kontroller:

- Pariserhjulet gällde först 29 m. Svaret [120, 240] krockade med 4.36, och höjden ändrades till 11 m.
- 4.584 fick en egen sinusfigur med skaltalen vid nederkanten. De vanliga skaltalen vid 180° och 360° krockade med kurvan.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 2 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 11 svar, och alla gav väntat resultat. Vinklarna godtas i valfri ordning och med eller utan gradtecken.

## Omgång 2 (användarens beslut 2026-10-26: fyll Ma3c där det är tunt)

En räkning per synligt kort visar att 17 kort i Ma3c har färre än 8 nivå 3-uppgifter. Ma2a:s ”mer om andragradsekvationer” finns redan i det gemensamma kortet ”Andragradsekvationer – tillämpningar och fördjupning”, som har 15 nivå 3-uppgifter. Där behövs ingen ändring.

### 10. Trigonometri i rätvinkliga trianglar: 6 kort, 4.585–4.590

| ID | Innehåll |
|---|---|
| 4.585 | Stegens vinkel och höjd: 68,9° och 4,66 m |
| 4.586 | Båten närmar sig klippan, och sänkningsvinkeln ändras från 12° till 20°. Båten kör 78,3 m (figur) |
| 4.587 | Höjden i en likbent triangel med basen 10 cm och toppvinkeln 40°, 13,7 cm (figur) |
| 4.588 | Exakta kateter i en 30°-triangel: 4 och 4√3 (figur) |
| 4.589 | Lutningen 8 % ger 4,6° och 199 m höjd på 2,5 km |
| 4.590 | Vinkeln mellan rymddiagonalen och bottenytan i ett rätblock, 21,8° (figur) |

### 11. Sinussatsens två fall (Ma3c): 6 kort, 4.591–4.596

| ID | Innehåll |
|---|---|
| 4.591 | Ett staket når gränsen i två punkter: AB = 4,3 eller 10,4 m (figur) |
| 4.592 | Intervallet 7,66 < a < 10 ger två trianglar |
| 4.593 | Trubbig vinkel A ger exakt en triangel (flerval) |
| 4.594 | Båda möjliga vinklarna C, 112,5° och 17,5° |
| 4.595 | När a är lika med höjden blir sin B = 1 och B = 90° |
| 4.596 | Arean av den större av två trianglar, 26,9 cm² |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- Figurerna rättades i flera omgångar:
  - Klippans topp hamnade på fel nivå.
  - ”40°” låg på höjdlinjen.
  - ”8 cm” och ”v” låg för nära linjerna.
- SVG-granskaren ger 0 varningar.
- 5 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 20 svar, och alla gav väntat resultat. Både 4√3 och 4sqrt(3) godtas, och 6,93 underkänns där frågan kräver exakt svar.

### 12. Primitiva funktioner med villkor: 5 kort, 3.1258–3.1262

| ID | Innehåll |
|---|---|
| 3.1258 | Läget ur hastigheten och startläget: s(5) = 9 m. Föremålet vänder vid t = 3 |
| 3.1259 | Grafen går genom (2, 5), vilket ger f(3) = 14 |
| 3.1260 | En tangent ger både k och C: F(x) = x³ + 2x |
| 3.1261 | Volym ur flöde och största volym: 100 liter efter 5 min |
| 3.1262 | Två primitiva funktioner skiljer sig med en konstant: F(5) − G(5) = 3 (flerval) |

### 13. Största och minsta värde: 4 kort, 3.1263–3.1266

| ID | Innehåll |
|---|---|
| 3.1263 | Öppen låda av kartong: x = 5 och V = 2 000 cm³ (figur) |
| 3.1264 | Det största värdet antas i en ändpunkt: största 20 och minsta 0 |
| 3.1265 | Hage mot en vägg med 40 m stängsel: 200 m² (figur) |
| 3.1266 | Det största värdet antas där f′ = 0 eller i en ändpunkt (flerval) |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 8 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 15 svar, och alla gav väntat resultat.

### 14. Polynomfunktioner: 4 kort, 1.977–1.980

| ID | Innehåll |
|---|---|
| 1.977 | Andragradsfunktionen ur grafens skärningspunkter: (x + 1)(x − 5) (figur) |
| 1.978 | Dubbelrot i 0 och nollstället 3 ger 2x²(x − 3) |
| 1.979 | Nollställena 2 och 8 och största värdet 18 ger −2(x − 2)(x − 8) |
| 1.980 | En parabelformad båge, 40 m bred och 10 m hög, är 4,4 m hög 5 m från fästet (figur) |

### 15. Tangent och sekant: 4 kort, 1.981–1.984

| ID | Innehåll |
|---|---|
| 1.981 | Tangenten är parallell med sekanten mellan x = 1 och x = 4 när x = 2,5 |
| 1.982 | Sekantens och tangentens lutning ur graf, 2 och 3 (figur) |
| 1.983 | Medelhastigheten 20 + 5h är 21 m/s när h = 0,2 |
| 1.984 | Vilket uttryck ger tangentens lutning (derivatans definition, flerval) |

Kontroller:

- Graferna har en ny figurtyp med skaltalen längs kanterna, så att de inte krockar med kurvorna.
- Etiketterna i 1.980 och 1.982 flyttades tills SVG-granskaren gav 0 fynd.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 2 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 16 svar, och alla gav väntat resultat.
  - Både faktoriserad och utvecklad form godtas.
  - Fel tecken eller fel koefficient underkänns.

### 16. Trigonometriska tillämpningar (Ma3c): 4 kort, 4.597–4.600

| ID | Familj | Innehåll |
|---|---|---|
| 4.597 | Areor i tillämpningar | Fyrhörnig tomt: diagonalen ger en rätvinklig triangel och en triangel som löses med cosinussatsen, 1 006 m² (figur) |
| 4.598 | Avstånd och triangulering | Avståndet till en fyr efter 5,0 km, 3,89 km (figur) |
| 4.599 | Avstånd och triangulering | Flyghöjden ur två höjdvinklar, 882 m (figur) |
| 4.600 | Välja metod | Två vinklar och den mellanliggande sidan: beräkna C och använd sinussatsen (flerval) |

Kontroller:

- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 4 räkneled radbröts.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 8 svar, och alla gav väntat resultat.
- I 4.598 finns en kvarstående ANGLE_ARC_DIRECTION_MISMATCH från SVG-granskaren. Det är en falsk träff:
  - Vinkeln 70° mäts mellan kursens fortsättning och riktningen mot fyren, och bågen ligger rätt.
  - Tre linjer möts i hörnet, och granskaren väljer det inre vinkelparet.
  - I 4.599 försvann motsvarande varning när marklinjen kortades till sträckan AB.

### 17. Kap 1, omgång 3: 11 kort, 1.985–1.995

Korten fyller fyra områden till 9 nivå 3-uppgifter vardera.

| ID | Område | Innehåll |
|---|---|---|
| 1.985 | algebra_polynom | (x + 3)² − (x − 3)² = 12x |
| 1.986 | algebra_polynom | Golvarea som inte täcks av mattan: 5x + 4 (figur) |
| 1.987 | algebra_polynom | (x + a)² = x² + 10x + b ger a = 5 och b = 25 |
| 1.988 | polynom | Gradtal för p·q och p + q: 5 och 3 |
| 1.989 | polynom | Minsta gradtal ur en graf med tre nollställen: grad 3 (figur, flerval) |
| 1.990 | polynom | p(2) = 15 ger a = 3, och då är p(−1) = 0 |
| 1.991 | rationella_ekvationer | 3/(x − 1) = 2/(x + 1) ger x = −5 |
| 1.992 | rationella_ekvationer | Falsk rot: x²/(x − 3) = 9/(x − 3) ger bara x = −3 |
| 1.993 | rationella_ekvationer | Cykelfarten ur tidsskillnaden, 10 km/h |
| 1.994 | rakna_rationella | Division av rationella uttryck: (x + 2)(x − 3) |
| 1.995 | rakna_rationella | 1/x − 1/(x + 2) = 2/(x(x + 2)) |

Kontroller:

- 1.992 fick talen 3 och 9 i stället för 2 och 4. Svaret −2 krockade med 1.535.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- 7 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 22 svar, och alla gav väntat resultat. Likvärdiga uttryck godtas.

### 18. Kap 2, omgång 3: 14 kort, 2.1271–2.1284

| ID | Område | Innehåll |
|---|---|---|
| 2.1271 | andringskvoter | Ökning per år i två perioder ur en tabell: 250 och 300 |
| 2.1272 | andringskvoter | Genomsnittlig förändring ur en graf, −2,5 °C/h (figur) |
| 2.1273 | andringskvoter | Genomsnittlig ökning för N = 500·2ᵗ mellan t = 2 och t = 5, 4 667/h |
| 2.1274 | derivata_exponential | f′ = 0,3f och f(0) = 50 ger f(5) ≈ 224 |
| 2.1275 | derivata_exponential | C och k ur en tabell med f och f′: 12 och −0,25 |
| 2.1276 | derivata_exponential | M′ = −0,12M vid 40 g ger 4,8 g/år |
| 2.1277 | numerisk_derivering | Central differenskvot ur en tabell, 24 m/s |
| 2.1278 | numerisk_derivering | Minimipunkt med digitalt verktyg: (1,10; −0,30) |
| 2.1279 | derivatans_definition | f′(2) för x² + 3x med definitionen, 7 |
| 2.1280 | derivatans_definition | Gränsvärdet (√(9 + h) − 3)/h tolkat som en derivata, 1/6 |
| 2.1281 | derivata_polynom | Avtagande intervall −2 ≤ x ≤ 1 |
| 2.1282 | derivata_polynom | En extrempunkt i (1, −2) ger a = 0 och b = −3 |
| 2.1283 | talet_e | e²ˣ har lutningen 6 när x ≈ 0,55 |
| 2.1284 | talet_e | Läkemedlet minskar med 10 mg/h efter 6,4 h |

Kontroller:

- Svaren för numerisk derivering (först 10) och avtagande intervall (först [−1, 3]) krockade med befintliga kort och byttes.
- Facit följer 1.116. Facit och ledtråd renderades och lästes igenom.
- Rubrikerna ”Derivera” och ”Logaritmera” skrevs om, så att de beskriver just det steget.
- En ny genomsökning av omgång 2 hittade tolv korta mallrubriker, till exempel ”Jämför”, ”Beräkna arean” och ”Sätt in värdena”. De skrevs om i 4.570, 4.590, 4.595, 3.1259, 3.1264, 3.1265, 1.993, 2.1259, 2.1271, 2.1273, 2.1277 och 2.1282. Testets spärr mot sådana rubriker har utökats.
- 9 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 224 fynd både före och efter ändringen.
- Självrättningen testades med 22 svar, och alla gav väntat resultat.

### Läge efter omgång 2

Alla 17 kort i Ma3c som hade färre än 8 nivå 3-uppgifter har nu minst 9. Totalt tillkom 69 kort i omgång 2.

## Ma3b (användarens beslut 2026-10-26: fyll på Ma3b också)

Lärarhandledningen till Matematik 5000 Kurs 3b har fyra kapitel:

1. Algebra och funktioner
2. Förändringshastigheter och derivator
3. Kurvor, derivator och integraler
4. Geometrisk summa och linjär optimering

Där finns ingen trigonometri, inget absolutbelopp och ingen deriverbarhet.

- **Trigonometrikorten:** de 18 nya trigonometrikorten (4.573–4.590) var märkta 1b+1c. De är nu bara märkta 1c, och testet låser det.
- **Äldre kort:** 17 äldre trigonometrikort är fortfarande märkta 1b, liksom 3 äldre absolutbeloppskort (1.451, 1.462 och 1.534). De har inte ändrats.
  - Trigonometri: 4.416, 4.417, 4.426, 4.427, 4.428, 4.442, 4.469–4.472, 4.487–4.492 och 4.495.
  - Läraren får avgöra om de ska bli bara 1c.

### 19. Ma3b-omgången: 15 kort

| ID | Område (kurs) | Innehåll |
|---|---|---|
| 1.996 | absolutbelopp (1c) | \|2x − 5\| = 7 ger x = −1 och x = 6 |
| 1.997 | absolutbelopp (1c) | \|x − 3\| = \|x + 1\| tolkat som avstånd ger x = 1 |
| 1.998 | absolutbelopp (1c) | \|x + 1\| = 2x − 5 med en falsk lösning, svaret är x = 6 |
| 1.999 | absolutbelopp (1c) | Grafisk lösning av \|x + 1\| = 0,5x + 2 ger x = ±2 (figur) |
| 1.1000 | absolutbelopp (1c) | Ett belopp kan inte vara negativt, så ekvationen saknar lösning (flerval) |
| 1.1001 | absolutbelopp (1c) | Temperaturavvikelse: 18,5 eller 23,5 °C |
| 1.1002 | faktorisera_polynom | x(x − 3)² |
| 1.1003 | faktorisera_polynom | Gruppering ger (x − 2)²(x + 2) |
| 3.1267 | andraderivatan | Grafen byter från att böja nedåt till uppåt vid x = 3 |
| 3.1268 | andraderivatan | Lokalt max 0 och lokalt min −16 för x⁴ − 8x² |
| 3.1269 | deriverbarhet | a = 1, och derivatan är 2 till vänster och 3 till höger (hörn) |
| 3.1270 | deriverbarhet | \|x − 3\| + \|x + 1\| är inte deriverbar i −1 och 3 |
| 4.601 | geometriska_summor (1b) | 5 + 10 + … + 2 560 = 5 115 |
| 4.602 | geometriska_summor (1b) | Ett meddelande sprids under 8 dagar, 148 personer |
| 4.603 | geometriska_summor (1b) | Kvoten ur summan av tre termer, k = 4 |

Kontroller:

- **Kursmärkning:** absolutbeloppskorten är bara märkta 1c, eftersom absolutbelopp inte finns i 3b-boken. Faktorisering, andraderivatan och deriverbarhet följer de befintliga kortens märkning 1b+1c.
- **Bytta tal:** två svar krockade med befintliga kort (1.998 och 3.1267) och fick andra tal.
- **Faktoriseringsformat:** 1.1002 och 1.1003 har formatet ”faktoriserat”, precis som de befintliga faktoriseringskorten. Annars godtogs det ofaktoriserade uttrycket.
- **Granskning:**
  - Etiketterna i 1.999 fick vit bakgrund.
  - 1.1002 omformulerades efter VERY_SIMILAR_TEXT mot 1.843.
  - Tre allmänna rubriker skrevs om.
  - SVG-granskaren ger 0 fynd, och validatorn ger 224 fynd både före och efter ändringen.
- **Självrättningen:** testades med 29 svar, och alla gav väntat resultat.

### 20. Trigonometri och absolutbelopp tas bort ur Ma3b (lärarbeslut 2026-10-26)

Läraren beslutade: ”ändra dem till bara Ma3c om det inte ingår i kursen”.

- **Kort som ändrats:** 20 kort har ändrats från 1b+1c till bara 1c:
  - Absolutbelopp: 1.451, 1.462 och 1.534.
  - Trigonometriska ekvationer: 4.416, 4.417, 4.426 och 4.495.
  - Enhetscirkeln: 4.427, 4.428 och 4.472.
  - Trigonometri i rätvinkliga trianglar: 4.442, 4.469–4.471 och 4.487–4.492.
- **Struktur:** I `strukturmato1.js` har områdena absolutbelopp, trig_ratvinkliga, enhetscirkeln och trig_ekvationer fått spåret ["1c"] i SPARMATO1.
  - Samma ändring gjordes i Kunskapsgymmets kopia.
  - Kunskapsgymmets avslutande `window.GRUPPMATO1 = {};` finns kvar.
- **Resultat i Kunskapsgymmet:** Ma3b har 41 kort och inga trigonometri- eller absolutbeloppsuppgifter. Inget Ma3b- eller Ma3c-område har färre än 8 nivå 3-uppgifter.
- **Deriverbarhet** finns inte heller i 3b-boken, men det beslutet gällde inte det området. Det är fortfarande märkt 1b+1c.

### 21. Kontroll mot ämnesplanen (2026-10-26)

Källa: ”Matematik – fortsättning” (MATO), nivå 1b och 1c, i lärarens OneDrive (Matematik/Ämnesplan matematik fortsättning.docx).

**Nivå 1b (Ma3b) innehåller:**

- rationella uttryck
- gränsvärde och derivatans begrepp
- villkor för deriverbarhet
- deriveringsregler, talet e och naturlig logaritm
- andraderivata och extremvärden
- polynom och polynomekvationer
- integraler
- linjär optimering
- geometrisk summa

Nivå 1b saknar absolutbelopp och trigonometri.

**Nivå 1c (Ma3c)** har samma kärna. Därtill kommer absolutbelopp, enhetscirkeln och cosinus-, sinus- och areasatsen. Linjär optimering och geometrisk summa ingår inte.

Beslut:

- Deriverbarhet ligger kvar på 1b+1c, eftersom ”Villkor för deriverbarhet” står uttryckligen i nivå 1b.
- Absolutbelopp och trigonometri är bara 1c. Det bekräftar ändringen i avsnitt 20.

Kontroll av alla 50 områden i SPARMATO1: varje område har rätt spår enligt ämnesplanen. Inget kort har en kursmärkning utanför sitt områdes spår.

Iakttagelser utan ändring:

- **Trigonometriska ekvationer:** metoder för att lösa trigonometriska ekvationer står i nivå 2 (Ma4), inte i nivå 1c. Området trig_ekvationer ligger ändå i Ma3c, som enkla ekvationer kopplade till enhetscirkeln.
- **Radianer:** begreppet radian hör till nivå 2. Det används i 4.416 och 4.417.
