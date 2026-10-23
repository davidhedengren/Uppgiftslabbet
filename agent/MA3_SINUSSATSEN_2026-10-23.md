# Ma3c: sinussatsen, 2026-10-23

Sex nya uppgifter **4.526–4.531**, två vardera på nivå 1, 2 och 3.
Området hade 26 huvuduppgifter, varav 22 spelbara och två uttryckligen
på nivå 1. Nu 32/28/4. Alla tillhör spår 1c enligt kursstrukturen.

De 26 äldre uppgiftstexterna inventerades för variation, bland annat
4.32, 4.42, 4.72, 4.87, 4.273, 4.493 och 4.494. De nya korten
kompletterar direkt sidberäkning med motstående vinkelpar, ett känt
kvotvärde, felsökning, höjdberäkning och samband mellan sidlängder.
Inventeringen är inte en fullständig omgranskning av äldre uppgifter.

## Samtliga granskade uppgifter och kommentarsförslag

| ID | Nivå | Innehåll och verifierat facit / kommentarsförslag |
|---|---:|---|
| 4.526 | 1 | Sidan 10 cm hör ihop med den motstående vinkeln 75°, inte med vinklarna vid sidans ändpunkter. |
| 4.527 | 1 | Det gemensamma kvotvärdet är 12 cm, så b=12sin30°=6 cm. |
| 4.528 | 2 | Korrigera omvända sinusfaktorer: b=6sin75°/sin45°≈8,20 cm. Sidan mot större vinkel måste också vara längre. |
| 4.529 | 3 | Toppvinkeln är 80°. Vänstra taksidan är 10sin60°/sin80°, vilket ger h=10sin60°sin40°/sin80°≈5,65 m. |
| 4.530 | 3 | b/a=√3 och b−a=4 ger a=4/(√3−1)≈5,46 cm. |
| 4.531 | 2 | En dubbelt så stor vinkel ger inte automatiskt en dubbelt så lång sida: b/a=sin50°/sin25°≈1,81. |

- **Granskad – inget fel efter slutkontroll:** samtliga sex nya uppgifter.
- **Åtgärdade äldre uppgifter:** inga. Tidigare texter, facit och metadata bevaras.
- **Konstruktionsjusteringar:** figurernas alternativtexter beskriver sida–vinkel-
  sambanden. En intern `data-height`-markör byttes till `data-altitude`, eftersom
  SVG-validatorn annars misstolkade den som ett numeriskt höjdattribut. Själva
  höjdgeometrin var korrekt och kontrolleras separat.
- Kommentarerna är dokumentation/förslag. Inga rapportstatusar ändrades
  och inga kommentarer skickades till elever.

## Pedagogik, figurer och verktyg

Nivå 1 prövar ett direkt grundsamband. Nivå 2 kräver att eleven ställer
upp eller rättar en kvot och beräknar den. Nivå 3 kombinerar sinussatsen
med ett andra samband: rätvinklig trigonometri respektive en längdskillnad.
Alla kort är fristående och har egna skalenliga SVG-figurer. Bågarna
sitter på rätt hörn; sidan a ligger mittemot A och sidan b mittemot B.

Alla sex tillåter miniräknare. GeoGebra behövs inte eftersom figurerna
är givna och beräkningarna kan göras med vanlig räknare. De numeriska
uppgifterna har tydlig svarsenhet. Två decimaler efterfrågas i 4.528–4.530;
full precision behålls i maskinfacit, toleransen är 0,005. Faciten visar
de mellanled som behövs och avrundar först på slutet.

## Verifiering och ändrade filer

- Master: `uppgiftermato1.js`, cacheversion i `index.html`, denna logg,
  felmönsterregistret och `tools/ma3-sinussatsen-2026-10-23.test.js`.
- Konsument: identisk bank, cacheversion och motsvarande `.browser.cjs`.
- Tre testgrupper: oberoende beräkningar, metadata samt mätning av alla
  triangelvinklar, bågändpunkter, sidförhållanden och tältets lodräta höjd.
  Tälthöjden verifieras också med en separat beräkning från två tangenssamband.
  Föregående cosinusomgångs tre testgrupper är fortsatt godkända.
- 108 kontroller genom faktisk självrättning: alla alternativkombinationer,
  vanliga svarsetiketter, enheter samt rätt och fel avrundning.
- Spårfilter: inga nya kort i 1b och sex i 1c. Verktygsflaggor kontrollerade
  på de verkliga elevkorten.
- 12 elevvyer och 12 lärarvyer på 390/1280 px: inga JS-/KaTeX-fel eller
  överflöden. Figurgalleri och mobilkort visuellt kontrollerade.
- SVG: inga kvarvarande ERROR/WARNING. INFO om vinkelbågar följs upp av
  koordinattestet; vit bakgrund vid bildkanten är avsiktlig.
- Full bankvalidator: 1519 ERROR / 230 WARNING / 1446 INFO före och efter,
  inga nya fynd. Äldre fynd ligger utanför denna nykonstruktion.
- Strukturell diff: endast sex nya objekt; inga äldre ändrade eller borttagna.
  Orelaterade fysikutkast och prototyper är bevarade.
