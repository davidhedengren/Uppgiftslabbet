# Ma3c: cosinussatsen, 2026-10-23

Sex nya uppgifter **4.520–4.525**, två vardera på nivå 1, 2 och 3.
Området hade 33 huvuduppgifter, varav 26 spelbara och tre uttryckligen
på nivå 1. Efter tillägget: 39/32/5. Bara spår 1c, enligt kursstrukturen.

De 33 äldre uppgiftstexterna inventerades för variation; de domineras av
direkt sid-/vinkelberäkning. Särskilda jämförelser: 4.02, 4.07, 4.12,
4.123, 4.430, 4.446, 4.461 och 4.478. Detta är innehållsinventering,
inte en fullständig omgranskning av äldre lösningar.

## Alla granskade uppgifter och kommentarsförslag

| ID | Nivå | Innehåll och verifierat facit / kommentarsförslag |
|---|---:|---|
| 4.520 | 1 | Välj rätt samband: x²=7²+4²−2·7·4·cos60°. Den sökta sidan ligger mittemot vinkeln. |
| 4.521 | 2 | Avstånd mellan två stigar: x²=25+9−30cos120°=49 ger 7 m. Det negativa cosinusvärdet gör sista termen positiv. |
| 4.522 | 1 | Med samma två sidlängder ger större mellanliggande vinkel längre motstående sida: y>x. |
| 4.523 | 2 | cos v=(49+25−100)/70=−13/35, alltså v≈111,8°. |
| 4.524 | 3 | Addera cosinussambanden för parallellogrammens diagonaler: 64+100=2x²+72, så x=√46≈6,78 cm. |
| 4.525 | 3 | De två lika sidorna är båda x: 144=2x²−2x²cos120°=3x² ger x=√48≈6,93 cm. |

- **Granskad – inget fel efter slutkontroll:** samtliga sex nya uppgifter.
- **Åtgärdade äldre uppgifter:** inga. Inga tidigare objekt ändrades.
- **Konstruktionsjusteringar:** 4.522 fick gemensam skala för båda
  trianglarna och större avstånd mellan rubrik och mått. I 4.524 flyttades
  diagonalmåtten bort från linjerna. Alla sex figurers etiketter kontrollerades.
- Kommentarerna ovan är dokumentation/förslag, inte skickad återkoppling.
  Inga rapportstatusar ändrades.

## Pedagogik och verktyg

Nivå 1 tränar samband och jämförelse utan längre beräkning. Nivå 2
kräver insättning, rot eller invers cosinus. Nivå 3 kräver att eleven
själv bygger en ekvation med återkommande okänd sida eller kombinerar
två cosinussamband. Fler siffror är inte skälet till högre nivå.

Alla sex har miniräknare; GeoGebra behövs inte för dessa givna figurer
och algebraiska samband. Vinkelberäkningen använder grader. Alla kort
är fristående. Faciten visar metoden och de avgörande mellanleden i
`facit-v2`, med tydlig slutrad. Uttryckliga avrundningskrav motsvaras av
toleransen; uppgiften utan avrundningskrav har inget dolt precisionskrav.

## Verifiering och ändrade filer

- Master: `uppgiftermato1.js`, cacheversion i `index.html`, denna logg,
  felmönsterregistret och `tools/ma3-cosinussatsen-2026-10-23.test.js`.
- Konsument: identisk bank, cacheversion och motsvarande `.browser.cjs`.
- Tre testgrupper: oberoende facitberäkning, metadata samt geometrisk
  mätning av samtliga trianglar, vinkelbågar och parallellogrammens diagonaler.
  Jämförelsefigurens gemensamma skala kontrolleras uttryckligen.
- 104 svarskontroller, inklusive alla alternativkombinationer,
  enheter och rätt/fel avrundning. Spårfilter: noll nya kort i 1b, sex i 1c.
- 12 elevvyer och 12 lärarvyer på 390/1280 px. Inga JS-/KaTeX-fel eller
  överflöden. SVG-galleri och mobilkort visuellt kontrollerade.
- SVG-validatorns INFO om vinkelbågar följs upp av koordinattestet:
  bågarnas ändpunkter ligger på rätt vinkelben och vinklarna stämmer.
  Vit bakgrund vid bildkanten är avsiktlig. Inga kvarvarande ERROR/WARNING.
- Full bankvalidator: 1519 ERROR / 230 WARNING / 1446 INFO före och efter,
  inga nya fynd. Äldre fynd ligger utanför denna nykonstruktion.
- Endast sex nya bankobjekt; äldre innehåll och orelaterade fysikutkast bevaras.
