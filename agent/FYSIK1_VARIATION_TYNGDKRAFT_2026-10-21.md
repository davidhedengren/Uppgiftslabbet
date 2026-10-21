# Fysik 1: variation i massa och tyngd, 2026-10-21

## Lucka och resultat

Området hade 21 huvuduppgifter men bara **19 spelbara** och endast en figur. Många frågor gav massa och tyngdacceleration i text, ofta i en resa mellan planeter. Sex nya självständiga figuruppgifter varierar **avläsning, instrumentjämförelse, förhållanden, kraftbilder, fallacceleration och hastighet kontra tyngdkraft**. Området har nu **27 huvuduppgifter, varav 25 spelbara**, och sju med figur.

Området tas därför bort ur listan `OMRADEN_UNDER_25_2026-10-21.md`. Där ändras antalen kort under 25 från 142 till 141 och olika områden från 103 till 102; inga andra områdesuppgifter flyttas eller ändras.

## Alla nya uppgifter

| ID | Innehåll, korrekt svar och nivå |
|---|---|
| 4.758 | 24 N motsvarar 6 kg i det givna diagrammet. Nivå 1. |
| 4.759 | Bild C visar bara tyngdkraften nedåt efter att bollen släppts. Nivå 1. |
| 4.760 | B:s dubbla massa ger kraftmätarvärdet 30 N på samma modellplanet. Nivå 2. |
| 4.761 | Samma massa ger 20 N på B och 8 N på A, alltså faktorn 2,5. Nivå 2. |
| 4.762 | B har tre gånger större tyngdkraft och tre gånger större massa: samma fallacceleration. Nivå 2. |
| 4.763 | Samma massa och samma höjd ger lika stor tyngdkraft, oberoende av uppåt/noll/nedåt-hastighet. Nivå 1. |

Tre nivå 1, tre nivå 2. Alla har egna SVG och är självrättande, utan beroenden till andra delkort. Miniräknare tillåts; enkel avläsning i färdiga figurer kräver inte GeoGebra. Frågorna ger inga standardkonstanter eller färdiga lösningsformler. Modellplaneternas egenskaper bestäms av de givna diagrammen/mätningarna. Lösningarna förklarar den centrala idén med de mellanled som behövs, utan numrerade steg. Rätt enhet och svarsinstruktion står i slutparentes.

## Alla granskade befintliga jämförelser – Granskad – inget fel

Jämförelserna gäller innehåll, fysisk beräkning/facit och verktyg. De innebär inte en ny fullständig språk-/UX-granskning av alla äldre kort. Inga äldre bankobjekt har ändrats.

| ID | Färdigt kommentarsförslag |
|---|---|
| 4.347 | Granskad – inget fel: Modellplanetens givna 4,2 m/s² och massan 15 kg ger 63 N. Det lokala modellvärdet är nödvändig situationsdata, inte en lösningsledning om jordens standardkonstant. |
| 4.350 | Granskad – inget fel: 136,8 N och modellplanetens 5,7 m/s² ger massan 24 kg. |
| 4.356 | Granskad – inget fel: Tyngdkraften ökar från 66,6 till 133,2 N; ökningen är 66,6 N, med oförändrad massa. |
| 4.469 | Granskad – inget fel: Massan är oförändrad vid resan till månen, medan tyngdkraften minskar. |
| 4.474 | Granskad – inget fel: Mätvärdet 14,8 N vid 4,0 kg ger tyngdaccelerationen 3,7 m/s². |
| 4.504 | Granskad – inget fel: En massa på 60 kg ger tyngdkraften 589,2 N med g = 9,82 m/s². Uppgiften är ett direkt nivå 1-samband. |

**Åtgärdade befintliga uppgifter:** inga. **Nya:** 4.758–4.763. **Granskad – inget fel:** samtliga sex jämförelser ovan. **Kvar att utreda:** inget i de nya korten. Inga rapportstatusar eller elevkommentarer skrivs i databasen.

## Kontrollpunkter

- 4.758: diagrammet har massa på vågräta axeln och tyngdkraft på lodräta. Vid 24 N kan 6 kg läsas exakt på markerat rutnät. Svaret ska vara kg, inte N.
- 4.759: pilarna är **kraftpilar**, inte hastighetspilar. Efter släppet finns ingen kraft från handen; luftmotståndet är uttryckligen försummat. Bara den nedåtriktade tyngdkraften återstår.
- 4.760: båda föremålen hänger stilla på samma planet. Kraftmätarna visar då respektive tyngdkraft. En fördubblad massa fördubblar kraften, utan att något tabellvärde för g behöver ges eller gissas.
- 4.761: välj **samma massa** på båda planeterna. Vid 4 kg är krafterna 8 och 20 N; 20/8 = 2,5. Heldragen/streckad graf och tydliga ändetiketter gör figuren läsbar även utan färg. Formatet `multipel` accepterar även uttryck och "gånger".
- 4.762: B:s massförhållande 6:2 motsvaras av kraftpilarnas längdförhållande 135:45 = 3. Kraft per kilogram är samma, så fallaccelerationen är densamma. Det är ett annat problem än att fråga vilken boll som har störst kraft.
- 4.763: pilarna är uttryckligen **hastighetspilar**. B:s hastighet är noll i vändögonblicket, men tyngdkraften verkar ändå. Alla tre massor och höjder är lika.

## Tester och leverans

- `tools/fysik1-tyngdkraft-variation-2026-10-21.test.js` beräknar de tre numeriska svaren oberoende och skyddar skillnaden mellan kraft, acceleration och hastighet, vektorförhållandet, metadata, självständighet och de 25 spelbara uppgifterna.
- Det äldre fullständighetskravet i `tools/fysik1-kapitel4.test.js` är bevarat och utökat med de tre nya numeriska fallen, inte begränsat till ett urval. Alla tidigare kraftfall och formelsamlingstestet passerar.
- **60 svarskontroller och 12 kortvyer** i Kunskapsgymmet vid 390/1280 px. kg/g, N/kN, decimalkomma, bråk och "gånger" prövade. Samtliga rätta och felaktiga alternativ kontrollerade. Rätta alternativ har blandade platser i bankdata och får fortsatt blandas som hela objekt.
- Alla sex SVG visuellt granskade. Inga klippta texter, KaTeX-/JavaScript-fel, sidöverflöden eller överfulla displayformler.
- SVG-validatorns oförändrade DOM-/geometrifunktioner via Playwright ger 0 ERROR, 0 WARNING, 6 INFO. INFO gäller avsiktliga vita bakgrunder vid viewBox-kanten.
- Full bankvalidator före/efter: ERROR 1577, WARNING 227, INFO 1450 oförändrat; inga nya fynd. Äldre fynd utanför omgången kvarstår.
- Masterbas jämförd mot konsumenten före identisk banksynk. Cacheversion uppdaterad i båda apparna. Orelaterade prototyper och Python-cache bevaras.
