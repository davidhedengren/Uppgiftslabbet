# Ma3 gränsvärden – 24 oktober 2026

Åtta nya uppgifter, tio äldre uppgifter reviderade. Båda spåren 1b/1c.
Ingen rapportstatus ändrad. Kommentarerna nedan är förslag.

## Nya och granskade uppgifter

| ID | Nivå | Innehåll och verifierat svar |
| --- | --- | --- |
| 1.941 | 1 | Vänstergränsvärde från graf, skilt från punktvärdet: 2. |
| 1.942 | 1 | Avläsa gränsnivå för spänning: 12 V. |
| 1.943 | 2 | Tabell som stöd, algebra som motivering: (2x+1)/(x+2) → 2. |
| 1.944 | 2 | Kombinera två grafiskt givna gränsvärden: 2·3−(−2) = 8. |
| 1.945 | 3 | Rörelse och differenskvot: 7+h → 7 m/s. |
| 1.946 | 3 | Bråk i täljaren: −1/(1+x) → −1. |
| 1.947 | 2 | Spädning: koncentrationen närmar sig 0 men förblir positiv vid ändlig vattenmängd. |
| 1.948 | 4 | Konjugat och parameter: a/2 = 3 ger a = 6. |

Fyra egna SVG-figurer och en tabell. Miniräknare tillåten; GeoGebra behövs
inte för givna grafer eller dessa algebraiska metoder. Facit visar de
avgörande mellanleden och avslutas med svar.

## Åtgärdade äldre uppgifter och kommentarer

| ID | Ändring | Föreslagen kommentar |
| --- | --- | --- |
| 1.103 | Felaktigt 0/0-resonemang ersatt; nivå 1. | Direkt insättning ger 1+1 = 2. Facit är rättat. |
| 1.106 | Samma mallfel; nivå 1. | Direkt insättning ger 2+2 = 4. Facit är rättat. |
| 1.109 | Samma mallfel; nivå 1. | Direkt insättning ger −3−3 = −6. Facit är rättat. |
| 1.112 | Samma mallfel; nivå 1. | Direkt insättning ger 4+4 = 8. Facit är rättat. |
| 1.115 | Samma mallfel; nivå 1. | Direkt insättning ger 0+3 = 3. Facit är rättat. |
| 1.431 | Nivå 5 → 2. | Gränsvärdet är 15000/3 = 5000. Nivån är sänkt eftersom metoden är rutinmässig. |
| 1.432 | Nivå 5 → 2. | Kostnaden per minut närmar sig 0,69 kr. Nivån är omkalibrerad. |
| 1.435 | Nivå 4 → 2; rättning av fel enhet. | Gränsvärdet är 11 miljarder. Både 11 och 11 miljarder godtas; 11 kg godtas inte. |
| 1.436 | Nivå 5 → 2. | A/4 = 1/7 ger A = 4/7. Nivån är omkalibrerad. |
| 1.437 | Nivå 5 → 2. | Gränsvärdet är √(16/4) = 2. Nivån är omkalibrerad. |

Alla tio får miniräknare, inte GeoGebra. Fem tidigare direktinsättningsfrågor
var felklassificerade som nivå 2; fem rutinmodeller låg på nivå 4–5.

## Granskad – inget fel: jämförelser av insättning

Avgränsad matematisk kontroll, inte ny fullständig visningsgranskning.

| ID | Föreslagen kommentar |
| --- | --- |
| 1.454 | Granskad – inget fel: e⁰+7 = 8 genom direkt insättning. |
| 1.474 | Granskad – inget fel: 2²+3 = 7. |
| 1.505 | Granskad – inget fel: nämnaren är 5, så direkt insättning ger 3/5. |
| 1.513 | Granskad – inget fel: 2/(x+1) går mot 0 och gränsvärdet är 40. |
| 1.524 | Granskad – inget fel: √(4+5) = 3. |
| 1.94 | Granskad – inget fel: ursprungsuttrycket ger faktiskt 0/0; förkortning ger gränsvärdet 1. |
| 3.791 | Granskad – inget fel: ursprungsuttrycket ger faktiskt 0/0; förkortning ger gränsvärdet 5. |

## Rättningsfel med ord som svarsenhet

Kunskapsgymmet kunde godta 11 kg när målenheten var ”miljarder”. Kända
fysiska enheter avvisas nu när målenheten saknar fysisk enhetsdefinition.
Vanliga tal och rätt ordform fortsätter till befintlig formatspecifik rättning.
Ingen ny generell feltolerans eller ändring av enhetsregistret införs.

Fem ytterligare faktiska kort kontrollerade: **1.434, 3.896, 3.917, 3.957,
3.1045**. Samtliga 42 rättningsförsök godkända, inklusive tal utan enhet,
rätt ord och fel kg. Föreslagen kommentar för samtliga: ”Rättningen har
kontrollerats: rätt tal med eller utan efterfrågad enhet godtas, fel fysisk
enhet avvisas.” Matematiska facit ändrades inte i dessa fem uppgifter.

Separat kvarstående visningsfynd: 3.896 och 3.917 har var sin lång befintlig
facitrad på mobil. Detta är inte ett fel i enhetstestet och är inte åtgärdat
i denna avgränsade leverans.

## Verifiering

- Egen genomräkning samt exakta Sympy-gränsvärden för algebrafrågorna.
- 112 verkliga rättningsförsök för de 18 huvuduppgifterna; 36 kortvisningar
  på 390/1280 px, båda spår, inga rättnings-, KaTeX- eller JavaScript-fel.
- Uppgiftslabbet: de 18 uppgifterna finns i rätt ordinarie områden på båda spår.
- SVG-figurer kontrollerade visuellt och geometriskt; etiketter flyttade
  för att undvika kollisioner. Vita bakgrundsrektanglar vid bildkanten är avsiktliga.
- `ma3-gransvarden-2026-10-24.test.js`, Ma3-facit- och validatorregressioner.
- Enhetsregressioner: `okand-malenhet-fysisk-enhet.test.js`,
  `numeriska-enhetsprefix.test.js`, `astronomiska-enheter-2026-10-23.test.js`,
  `elektriska-enheter.test.js`, `procent-enheter.test.js`,
  `fri-avrundning-heltal.test.js`.
- Inga validatorfynd för de åtta nya uppgifterna. De fem gamla linjära
  frågorna ger sedan tidigare INFO om likartade texter; de är kvar som mängdträning.
- Författarkälla: `tools/bygg-ma3-gransvarden-2026-10-24.py`.
  Browserharness: `tools/ma3-bankomgang.browser.cjs` i båda repona.
