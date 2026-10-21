# Fysik 1: varierade densitetsuppgifter, 2026-10-21

## Omfattning och urval

Efter enhetsomgången 2.321–2.326 fortsätter utbyggnaden med densitet.
Området hade redan 170 uppgifter, många med direkt insättning i massa/volym
eller med talvarianter av samma situation. En inventering av texter har
använts för urvalet; detta är inte en manuell granskning av alla 170.
Åtta nya uppgifter kompletterar med olika tankegångar, inte åtta talbyten.

## Alla nya och manuellt granskade uppgifter

| ID | Innehåll | Nivå | Kontrollerat svar |
|---|---|---:|---|
| 2.327 | Jämför massa vid samma volym | 1 | B |
| 2.328 | Skilj vätskans massa från bägarens | 2 | 1,2 g/cm³ |
| 2.329 | Oförändrad massa och kompression | 2 | 1,5 gånger |
| 2.330 | Plastandel i en 3D-utskriven kloss | 3 | 40 % |
| 2.331 | Upptäck avvikande densitet i en mättabell | 2 | C |
| 2.332 | Luftutrymme mellan småsten | 3 | 40 % |
| 2.333 | Bestäm torr färgs tjocklek från massökningen | 4 | 100 µm |
| 2.334 | Bestäm luftbubblans bidrag till felmätt volym | 3 | 4 cm³ |

Alla har egen SVG, specifik ledtråd, kort förklarande lösning, rätt enhet och
självrättning. Varje uppgift är ett fristående kort och behöver inga tidigare
resultat. Miniräknare är tillåten i samtliga. GeoGebra behövs inte. Standardkonstanter
eller formler ges inte som ledning; angivna materialvärden hör till situationen.
Nivå 1 kräver en enda begreppsjämförelse. Nivå 2 använder enkla kvoter och
differenser. Nivå 3 kräver att eleven skiljer på materialvolym och hålrum eller
mätfel. Nivå 4 kombinerar masskillnad, densitet, area och enhetsomvandling.

## Granskad – inget fel konstaterat

Följande befintliga jämförelseuppgifter har granskats och lämnats oförändrade:

| ID | Kontroll | Föreslagen kommentar |
|---|---|---|
| 2.284 | Massa och volym halveras; densiteten är 0,60 g/cm³. Nivå 1. | Granskad – inget fel: densiteten är oförändrad när klossen delas. |
| 2.285 | Volymökning 20 cm³ och massa 54 g ger 2,7 g/cm³. Nivå 2. | Granskad – inget fel: stenens volym är ökningen av vattennivån, 20 cm³. |
| 2.287 | 120/40 · 70 = 210 g. Nivå 2. | Granskad – inget fel: bitarna har samma densitet och den större väger 210 g. |

Verktyg kontrollerade även för dessa jämförelseuppgifter: miniräknare tillåten, GeoGebra
behövs inte. Testerna omfattar rätta och felaktiga elevsvar samt oavrundade
beräkningsuttryck där relevant. Kommentarerna är dokumentation; inga rapporter
har stängts eller kommentarer skickats i produktion.

## Åtgärdade befintliga fel

Den faktiska rättningen av **2.190** underkände det korrekta oavrundade
beräkningsuttrycket. Maskinfacit var redan avrundat och hade tolerans noll.
Kontrollen utökades med fem liknande uppgifter: **2.175–2.179**. 2.175 hade
redan fullvärde och korrekt tolerans (granskad – inget fel; kommentar:
”Både 5 140 kg och det oavrundade beräkningsvärdet godkänns.”).

Sex äldre uppgifter har nu rättats:

| ID | Ändrade fält | Föreslagen kommentar |
|---|---|---|
| 2.176 | rättSvar, tolerans, t | Rättningen godtar nu både 322 cm³ och det oavrundade värdet. Svarsinstruktionen är samlad i parentes. |
| 2.177 | rättSvar, tolerans | Rättningen godtar nu både 4,29 kg och det oavrundade beräkningsvärdet. |
| 2.178 | rättSvar, tolerans | Rättningen godtar nu både 9,62 cm³ och det oavrundade beräkningsvärdet. |
| 2.179 | rättSvar, tolerans, s | Rättningen och lösningen använder full precision fram till slutsvaret 6,33 kg. |
| 2.190 | rättSvar, tolerans, s | Rättningen godtar nu både 0,853 g/cm³ och det oavrundade värdet. Lösningen avrundar inte mellanleden. |
| 2.194 | rättSvar, tolerans, s | Rättningen godtar nu både 94,1 µm och det oavrundade värdet. Ungefärliga mellanled markeras med ≈. |

Fullständiga före/efter-objekt finns i `FYSIK1_DENSITET_2026-10-21_ANDRINGAR.json`.
Övriga gamla bankobjekt är oförändrade. Inga nya avrundningskrav har införts.
Nivåer och verktyg är oförändrade efter bedömning: dessa är beräkningsuppgifter
med miniräknare utan behov av GeoGebra.

## Verifiering och filer

- `uppgifter.js` är master, identisk kopia synkas till Kunskapsgymmet.
- `tools/fysik1-densitet-2026-10-21.test.js` verifierar fysikaliska beräkningar,
  unika ID:n, figurer, nivå och verktygsmetadata.
- Konsumentens `tools/fysik1-densitet-2026-10-21.browser.cjs` provar faktisk
  renderare och rättning vid 390 och 1280 px, utan XP- eller elevdataskrivningar.
- SVG-validator: inga ERROR eller WARNING för de åtta nya figurerna. INFO om
  vita bakgrundsrektanglar vid viewBox-kanten är väntad, inte avklippt innehåll.
- Alla åtta figurer visuellt kontrollerade. Bägare, mätglas och stenmarkeringar
  förbättrades under kontrollen så att de föreställer situationerna tydligare.
- Bankvalidator jämförd före/efter: inga nya fynd.
- Konsumentens BANK_VERSION uppdateras så att banken laddas om.

Nästa område i kapitel 2 är mätnoggrannhet. Hela fysikbankens utbyggnad och
manuella granskning är ännu inte slutförd.

Slutlig kontroll: **118 rättningsfall och 36 kort-/lösningsvisningar** för
samtliga 18 nya eller jämförda uppgifter, utan rättnings-, layout- eller
renderingsfel. Både godkända och felaktiga svar ingår. Fyra befintliga
uppgifter lämnas oförändrade (2.175, 2.284, 2.285, 2.287), sex rättas och
åtta tillkommer.
