# Fysik 1: varierade rutinuppgifter om ström, 2026-10-21

## Lucka och resultat

Enligt användarens nya inriktning kompletteras andra rutinområden. Ström hade 31 huvuduppgifter och fyra med figur; många använder samma direkta Q/I/t-insättning. Sex nya uppgifter varierar **diagramavläsning, skillnad mellan två tabellvärden, två driftlägen, strömförgrening, korta signaler och kvalitativa grafval**. Nu finns 37 uppgifter, varav 10 med figur. Samma huvudidé kan tränas på flera sätt utan att varje uppgift bara byter siffror eller namn.

## Alla nya uppgifter

| ID | Innehåll, korrekt svar och nivå |
|---|---|
| 8.574 | 18 C på 6 s ger 3 A ur ett laddningsdiagram. Nivå 1. |
| 8.575 | Skillnaderna (7−1) C och (5−2) s ger 2 A i tabellintervallet. Nivå 2. |
| 8.576 | Två strömnivåer ger 0,40·10 + 0,10·20 = 6 C. Nivå 2. |
| 8.577 | I en förgrening ger 1,20 − 0,45 = 0,75 A i nedre ledningen. Nivå 1. |
| 8.578 | En kort signal ger 0,12 C över 2,0 s, alltså 60 mA i medelström. Nivå 2. |
| 8.579 | Diagram B har samma Q-t-lutning hela tiden och visar konstant ström. Nivå 2. |

Två nivå 1, fyra nivå 2. Inga avancerade härledningar, ingen integration eller egna tangentkonstruktioner behövs. Alla data är direkt läsbara. Miniräknare tillåts, och färdiga diagram kräver inga GeoGebra-funktioner. Frågorna är självständiga, med egna SVG, korta ledtrådar och förklarande facit utan numrerade lösningssteg. Svarsinstruktioner finns i slutparentes. Ingen standardkonstant eller lösningsformel skrivs i frågan. Befintlig familj återanvänds.

## Alla granskade jämförelseuppgifter

Sex äldre uppgifter är jämförda för numerisk fysik, facit och verktyg; ingen ny fullständig språk-/UX-granskning av de 31 äldre korten görs i denna avgränsning. Inget äldre bankobjekt har ändrats.

| ID | Färdigt kommentarsförslag |
|---|---|
| 8.26 | Granskad – inget fel: 18 mC på 4,0 s ger 4,5 mA. Prefixomvandlingen är korrekt i facit. |
| 8.191 | Granskad – inget fel: 7,5 C på 3,2 s ger 2,34375 A; facit visar också rimliga avrundningar. |
| 8.197 | Granskad – inget fel: 0,90 A under 150 s ger 135 C. |
| 8.377 | Granskad – inget fel: 0,50 A under 60 s ger 30 C. |
| 8.378 | Granskad – inget fel: 2,1 mC på 0,75 ms ger 2,8 A eftersom prefixen tar ut varandra. |
| 8.379 | Granskad – inget fel: 900 C vid 2,5 A kräver 360 s, alltså 6 minuter. |

**Åtgärdade befintliga uppgifter:** inga. **Nya:** alla sex ovan. **Nya felrapporter:** inga i omgången. **Kvar att utreda:** inget i de sex nya korten. Inga produktionsrapporter markeras avslutade.

## Kontrollpunkter

- 8.574: diagrammet visar sammanlagd passerad laddning, inte ström på lodräta axeln. En rak Q-t-linje har konstant ström.
- 8.575: startvärdet 1 C ska dras från 7 C. Intervalltiden är 3 s, inte sluttiden 5 s. Facit förklarar varför.
- 8.576: beräkna varje laddningsbidrag och summera. Tiderna är olika, så ett vanligt medelvärde av de två strömmarna ger fel laddning.
- 8.577: pilarna visar en ström in och två ut. 0,45 + 0,75 = 1,20 A. Det är en förgrening i en större krets, inte ett ofullständigt kopplingsschema som ska slutas av eleven.
- 8.578: ström går under 0,20 s av hela tvåsekundersperioden. Visa laddningen 0,12 C och fördela den sedan över hela perioden; 0,60 A är pulsens ström, inte medelströmmen. Formlerna är korta nog för mobil.
- 8.579: alla fyra grafer är monotont ökande passerad laddning. Endast B har samma lutning hela tiden. Inga axelvärden behöver gissas eftersom frågan gäller konstant/varierande ström, inte dess storlek. Låt B-beteckningen följa själva figuren när alternativen blandas.

## Tester och visning

- `tools/fysik1-strom-variation-2026-10-21.test.js` innehåller oberoende beräkningar, kurvlutningsjämförelse och metadata-/självständighetskrav. Även befintligt multimetertest och `fysik-formelsamling.test.js` passerar.
- 68 kontroller i verkliga Kunskapsgymmet: fem numeriska kort och alla fyra alternativ. A/mA och C/mC godtas som likvärdiga; fel intervall, fel summering, fel förgreningsmetod och förväxling av puls/medelvärde avvisas.
- 12 kortvyer vid 390/1280 px och samtliga sex SVG visuellt granskade. Inga klippta figurtexter, KaTeX-/JavaScript-fel, sidöverflöden eller horisontellt överfulla displayformler.
- Full bankvalidator: ERROR 1577, WARNING 227, INFO 1452 oförändrat före/efter, inga nya fynd. Äldre fynd utanför omgången kvarstår.
- Gemensam bankbas verifierad före identisk synk till Kunskapsgymmet. Cacheversion uppdaterad i båda repona. Inga rapportstatusar, elevdata eller kommentarer skrivs till databasen.
