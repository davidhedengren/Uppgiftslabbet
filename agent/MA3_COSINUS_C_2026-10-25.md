# Ma3c: Cosinussatsen på nivå 3 – omgång 7

18 nya uppgifter #4.549–4.566 ger 20 spelbara C-uppgifter i området. Endast spår 1c. Alla tillåter miniräknare.

## Alla granskade uppgifter

| ID | Status | C-motivering | Förslag till kommentar / verifierat svar |
|---|---|---|---|
| 4.549 | Ny, granskad – inget fel. | Algebraisk rutin: bygger och löser en andragradsekvation med geometriskt rotvillkor. | 5. |
| 4.550 | Ny, granskad – inget fel. | Tränar parameteruttryck, trubbig vinkel och val av positiv rot. | 5,29. |
| 4.551 | Ny, granskad – inget fel. | Kombinerar cosinussatsen och areasatsen och kopplar rätt vinkel till rätt sidor. | 17,32 cm². |
| 4.552 | Ny, granskad – inget fel. | Använder cosinussatsen i två sammanhängande trianglar och utnyttjar mittpunkten. | 8,54 cm. |
| 4.553 | Ny, granskad – inget fel. | Översätter en riktning i verkligheten till rätt triangelvinkel. | 6,08 km. |
| 4.554 | Ny, granskad – inget fel. | Kombinerar hastighet och tid med avstånd i två olika riktningar. | 6,29 km. |
| 4.555 | Ny, granskad – inget fel. | Kombinerar vinkelbestämning med två uttryck för samma area. | 6,84 m. |
| 4.556 | Ny, granskad – inget fel. | Kopplar cosinussatsen till rät vinkel och skiljer ny längd från förändring. | 1,55 cm. |
| 4.557 | Ny, granskad – inget fel. | För över en beräknad längd från en triangel till en annan. | 71,68 °. |
| 4.558 | Ny, granskad – inget fel. | Kombinerar area med cosinussats och återanvänder ett exakt mellanresultat. | 6 cm. |
| 4.559 | Ny, granskad – inget fel. | Kombinerar bisektrissats med cosinussats i två trianglar. | 8,45 cm. |
| 4.560 | Ny, granskad – inget fel. | Översätter ett längdvillkor till vinkelgräns och väljer rätt heltal. | 96 °. |
| 4.561 | Ny, granskad – inget fel. | Väljer motstående sida, löser en andragradsekvation och kontrollerar geometriska villkor. | 1,50. |
| 4.562 | Ny, granskad – inget fel. | Utnyttjar en parallellograms egenskaper och väljer rätt av två möjliga vinklar. | 10,44 cm. |
| 4.563 | Ny, granskad – inget fel. | Kombinerar regelbunden månghörning, medelpunktsvinkel och cosinussats. | 35,27 cm. |
| 4.564 | Ny, granskad – inget fel. | Bestämmer två vinkellägen och kombinerar dem med en avståndsberäkning. | 9,20 cm. |
| 4.565 | Ny, granskad – inget fel. | Kombinerar två geometriska beräkningar med relativ förändring. | 67,76 %. |
| 4.566 | Ny, granskad – inget fel. | Tolkar negativ cosinus som en projektion utanför sidan och bestämmer ett positivt avstånd. | 5,43 cm. |

## Innehåll och kontroll

Variation: parameteruttryck och andragradsekvationer, area, median, svängvinkel, två båtar, masthöjd, rätvinkelgräns, fyrhörning, bisektris, vinkelolikhet, parallellogram, regelbunden femhörning, klockvisare, procentuell ändring och höjdfot utanför en triangel. Uppgifterna är individuellt formulerade; figurbiblioteket återanvänder ritregler, inte frågemallar.

Alla 18 får egna SVG-figurer. Konstruktionsgranskningen fångade formelrader som blev för breda på mobil och etiketter nära linjer. De rättades före publicering. Samtliga figurer inspekterades, inklusive fem ytterligare etikett-/vinkelkontroller i #4.549, #4.552, #4.553, #4.559 och #4.561. Före rättningen fanns också en hjälplinje förbi B i #4.566; den slutar nu vid B när höjdfoten ligger till vänster om A.

Viktiga principer: en sväng mäts från fortsatt färdriktning; triangelns inre vinkel är supplementvinkeln. En klockas timvisare flyttar sig under minuten. Vid procentuell ändring av en sträcka måste kvadratrötterna tas före jämförelsen. En trubbig vinkels cosinus kan vara negativ utan att en längd blir negativ.

## Testresultat

- Svaren kontrolleras även med andra metoder: Herons formel, koordinater, Apollonios sats och bisektrislängdens formel. Dessa metoder används bara som oberoende test, inte som krav på eleverna.
- Sju tester i `ma3-cosinus-c-2026-10-25.test.js`, befintliga sinus-/cosinusregressioner och alla fem tidigare C-rundors tester godkända. Minimikravet på antal kort tillåter framtida påfyllning.
- Verklig självrättning: 276 svarskontroller, inklusive avrundning, enheter och felaktiga svar. Inga fel.
- 36 elevvyer och 36 lärarvyer på 390 och 1280 px: inga KaTeX-fel eller för breda formelrader. Utvalda fullständiga mobilkort också visuellt granskade.
- Alla 18 figurer visuellt och maskinellt kontrollerade. SVG: 0 ERROR, 0 WARNING, 30 INFO (vit bakgrund vid bildkant och vinkelbågar med separat kontrollerade ben). Trianglar, fyrhörning, parallellogram och femhörning har geometriska regressionstester.
- Bankvalidatorn: 0 ERROR, 50 WARNING, 178 INFO; oförändrade äldre fynd, inga på omgångens nya uppgifter. Samtliga 3158 äldre bankobjekt oförändrade. Inga ID-krockar.

Ingen äldre uppgift behövde ändras i denna runda. Ingen felrapport har stängts automatiskt.

Källfil: `tools/bygg-ma3-cosinus-c-2026-10-25.py`. Gemensam figurkod: `tools/ma3-trig-c-figurer-2026-10-25.py`. Svarsinmatningar: `tools/ma3-cosinus-c-2026-10-25.cases.json`.
