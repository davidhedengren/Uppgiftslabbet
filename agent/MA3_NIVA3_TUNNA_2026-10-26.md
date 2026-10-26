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
