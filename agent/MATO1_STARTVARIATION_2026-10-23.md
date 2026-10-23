# Mato1: variation från kursens början, 2026-10-23

Efter sex avancerade Fy2-problem fortsätter arbetet från början av mato1.
Denna omgång gäller de två första områdena: **algebra_polynom** och **polynom**.
Tolv nya fristående uppgifter, **1.888–1.899**, för både 1b och 1c. Äldre
matematikuppgifter är oförändrade. Detta är en avgränsad påfyllnad, inte en
färdig genomgång av hela mato1.

## Behov och variation

Före tillägget hade algebra_polynom 24 huvuduppgifter, varav sju uttryckligen
på nivå 1, och polynom 29, varav nio på nivå 1. Dessa områden får sex nya
uppgifter vardera: **30 respektive 35 huvuduppgifter** efteråt. Den nya
omgången innehåller fyra på nivå 1, tre på nivå 2 och fem på nivå 3.

Variation kommer från olika elevhandlingar: känna igen en koefficient,
utveckla en area, resonera om bortklippta kanter, jämföra priser, välja bara
de produkter som bidrar till en viss potens, analysera en kostnadsökning,
bedöma polynombegreppet, läsa ett koefficientdiagram, bestämma en skalfaktor,
hantera gradvillkor och skilja en värdetabell från en entydig modell.

Inga frågor är framställda genom att bara byta siffror i samma mall.
Jämförelsen mot tidigare 1.855–1.861 och 1.868–1.879 avsåg innehåll och
variation; deras äldre facit är inte på nytt certifierade i denna omgång.

## Samtliga nya och detaljgranskade uppgifter

| ID | Nivå | Innehåll | Facit / föreslagen kommentar |
| --- | --- | --- | --- |
| 1.888 | 1 / E | Koefficient från algebrabitar | **3**. ”Ny enkel begreppsuppgift med algebrabitar.” |
| 1.889 | 1 / E | Delad rektangel och utvecklat areauttryck | **3x+6**. ”Ny enkel koppling mellan en areabild och ett polynom.” |
| 1.890 | 3 / C | Omkrets efter bortklippt hörn | **6x+10**. ”Ny resonemangsuppgift: nya kanter ersätter de borttagna utan att ändra omkretsen.” |
| 1.891 | 2 / E | Prisskillnad mellan två tryckerier | **3x+7**. ”Ny modelluppgift med två priser och subtraktion av en hel parentes.” |
| 1.892 | 3 / C | Välja parameter så att x²-termen i en produkt försvinner | **a=3**. ”Ny uppgift där bara relevanta delprodukter behöver undersökas.” |
| 1.893 | 3 / C | Kostnadsökning K(n+1)−K(n) | **4n+7**. ”Ny uppgift om förändring i en kvadratisk modell, utan krav på derivata.” |
| 1.894 | 1 / E | Identifiera ett polynom | **x²/3−2x+1**. ”Ny begreppsfråga som skiljer bråkkoefficient från x i nämnaren.” |
| 1.895 | 1 / E | Grad från koefficientdiagram | **3**. ”Ny avläsningsuppgift: en negativ koefficient påverkar inte graden.” |
| 1.896 | 2 / E | Bestäm skalfaktor och därefter p(2) | **−4**. ”Ny uppgift som kopplar markerad punkt och faktorform.” |
| 1.897 | 2 / E | Parametervillkor för exakt grad 2 | **m=2**. ”Ny uppgift där högsta termen ska försvinna men nästa måste finnas kvar.” |
| 1.898 | 3 / C | Två olika polynom passar samma tabell | **Båda passar, men de kan skilja sig för andra x**. ”Ny resonemangsuppgift om vad en värdetabell faktiskt bestämmer.” |
| 1.899 | 3 / C | Återskapa ett andragradspolynom från tre värden | **p(3)=18**. ”Ny uppgift som kombinerar funktionsvärden och ekvationssystem.” |

## Figurer, facit och verktyg

Nio egna SVG-figurer/diagram/tabeller. 1.892, 1.893 och 1.894 saknar figur
medvetet: respektive algebraisk produkt, kostnadsmodell och uttrycksalternativ
är redan den information eleven ska arbeta med. En dekorativ bild tillför
inget i dessa fall.

Alla tillåter miniräknare; vanlig räknare tar inte bort begrepps-, algebra-
eller modelleringsarbetet. GeoGebra behövs inte för givna figurer och enkla
exakta polynom. I de symboliska uppgifterna är just förenklingen det som
prövas. Inga frågor om digital grafritning eller regression ingår.

De fyra frågorna som uttryckligen kräver förenklat polynom använder
`förenklat_polynom`: ekvivalenta omordnade termer godtas, men exempelvis
3(x+2) besvarar inte kravet ”utan parenteser” i 1.889. Faciten innehåller
den centrala idén och nödvändiga mellanled utan generiska steglistor.
1.899 har angiven grad, medan 1.898 medvetet saknar ett sådant villkor.

## Granskningsutfall och verifiering

**Samtliga detaljgranskade:** 1.888, 1.889, 1.890, 1.891, 1.892, 1.893,
1.894, 1.895, 1.896, 1.897, 1.898, 1.899.

**Åtgärdade äldre matematikfel:** inga. Under konstruktionen delades en lång
rad i 1.893:s facit upp för mobilvisning.

**Granskad – inget fel efter konstruktionskontrollen:** alla tolv ovan.
Kommentarer finns per ID i tabellen. Inga externa rapporter stängs.

- `tools/ma3-startvariation-2026-10-23.test.js`: fem godkända grupper med
  självständiga modeller för area, omkrets, kostnad, koefficienter och tabeller.
  Tidigare `ma3-polynom-2026-10-22.test.js`: två grupper fortsatt godkända.
- `tools/ma3-startvariation-2026-10-23.browser.cjs`: 98 rättningskontroller,
  24 elevvyer och 24 lärarvyer vid 390/1280 px. Alternativ, olika termordningar,
  uttryck med prefix och fel svar testade. Inga JavaScript-, KaTeX- eller
  överflödesfel efter korrigeringen.
- Full validator: ERROR 1485 → 1485, WARNING 230 → 230, INFO 1446 → 1446.
  Inga nya fynd. Äldre fynd ligger utanför denna påfyllnad.
- SVG-regler körda med Playwright: nio figurer, inga ERROR, en WARNING,
  nio INFO. Varningen gäller den underliggande polynomkurvan i 1.896 som
  fortsätter utanför bildrutan; dess uttryckliga `clipPath` begränsar den
  synliga kurvan till rutnätet. Detta är avsiktligt och visuellt verifierat
  i båda bredderna. INFO avser vita bakgrundsrektanglar längs bildkanten.
- Alla figurer visuellt granskade. Synkade bankkopior ska vara identiska.
  Orelaterade lokala Fy1-utkast i `uppgifter.js` bevaras och pushas inte.

## Liten uppföljning från föregående Fy2-omgång

3.534 och 3.535 får exakt befintliga familjenamn för masspektrometer respektive
transformator. Därmed hamnar de i etablerade delmoment, inte i nya enstaka
grupper. Innehåll, facit och nivåer är oförändrade; fysikens regressionstest
skyddar nu även denna placering. Se `FY2_FORDJUPNING_2026-10-23.md`.
