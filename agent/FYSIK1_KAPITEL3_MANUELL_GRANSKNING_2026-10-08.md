# Fysik 1: manuell granskning av kapitel 3

Alla 321 huvuduppgifter och deras 607 kort/deluppgifter (inklusive odelade uppgifter) har lästs. Områden: acceleration, rörelse med konstant acceleration, vektorer samt v–t-, läge–tid- och a–t-diagram. Efter ändringarna gjordes en andra genomläsning av de reviderade lösningarna, kortens egna givna värden och huvuduppgifternas motsvarande villkor. Detta är en avgränsad kapitelomgång; den innebär inte att hela Fysik 1 har genomgått två manuella rundor.

278 huvudposter har ändrats. Den maskinläsbara loggen anger exakt vilka fält som ändrats i varje post. Andra kursbanker har inte ändrats.

## Viktigaste rättningarna

- Fristående kort med saknade startfarter, tider, accelerationer eller höjder har fått egna givna värden. Bland annat 3.199, 3.206, 3.231, 3.311, 3.369, 3.370, 3.386, 3.405 och 3.408. Tillhörande facit utgår från kortets egna data.
- Huvuduppgifter har kontrollerats igen när kort delats om. De uppgifter som bara syntes på ett delkort finns också i huvuduppgiften, exempelvis hissens 7 s i 3.119 och mätningen av g i 3.392 d.
- Lösningar visar varför sambandet används, insatta värden och resultat. Reaktions- och bromssträckor, delsträckor, tidsförskjutningar och val av positiv rot redovisas där de behövs. Ingen numrerad steglista har införts.
- Avrundade mellanresultat används inte som nya exakta givna värden. Exempel: elektronens flygtid, farten i en mellanpunkt och balkonghöjden. Svar och toleranser följer frågans avrundningskrav; oavrundade korrekta värden accepteras också.
- 3.360 hade ett felaktigt generellt påstående om medelfart trots lastbilens försprång. Lösningen använder nu båda lägesfunktionerna.
- 3.371 skiljer tydligt bilens 1200 m från polisbilens 1300 m. 3.385 anger riktning och kortaste möjliga tid. 3.391 visar att krocken sker efter att främre bilen stannat.
- Diagramfacit visar sina egna areaberäkningar före medelfart eller slutläge. Positiv/negativ hastighet skiljs från fart och tillryggalagd sträcka. Enkla avläsningar har nivå 1 och rutinberäkningar nivå 2; svårare modeller behåller högre nivå.
- Deluppgifter visas på egna rader. Koordinater i diagramlösningar har parenteser och tydlig separator. Upprepade avrundningsinstruktioner och synliga flyttalsartefakter har tagits bort.

## Verifiering

- Alla 246 numeriskt självrättande huvuduppgifter i kapitel 3: 536 svar jämförda med oberoende beräkningar i `tools/fysik1-kapitel3.test.js`. Formlerna använder transkriberade givna värden, inte facittexten.
- 143 SVG-figurer i kapitlets huvudfrågor/facit visuellt granskade. Deras geometri och SVG-innehåll är oförändrade. De åtta dubblettvarningarna jämför text utan figur; de berörda uppgifterna har olika figurer eller givna grafvärden.
- Hela Fysik 1 i Kunskapsgymmet: 4977 aktiva kort, 13966 kontroller med appens faktiska självrättning, inga misslyckade kontroller eller KaTeX-fel.
- Extra browserkontroller: 14 avrundade/oavrundade svar, enhetsbyten, rot/bråk och tiopotenser, inklusive felaktiga närliggande tal som ska underkännas. Alla passerar.
- Samtliga frågor, facit, ledtrådar och deluppgifter renderade i båda apparna: 25471 matematikuttryck per app, inga KaTeX-fel eller numrerade fysiksteglistor.
- Utvalda fristående kort kontrollerade visuellt vid 390 och 1174 px: ingen sidöverströmning, ingen felrenderad matematik eller stegnumrering.
- Uppgiftslabbet: 100 relevanta testfall passerar. Kunskapsgymmet: 64 testfall passerar. SVG-källorna har inte ändrats och tidigare 47 SVG-testfall behöver därför inte upprepas för denna textomgång.
- Formatgranskning av Fysik 1: 0 ERROR, 8 WARNING, 655 INFO. Detta är teknisk verifiering och ersätter inte fortsatt manuell granskning av kapitel 4–9.

## Fortsättning

Nästa manuella kapitel är krafter, kapitel 4. Efter kapitelomgångarna återstår ytterligare en genomgång av hela Fysik 1. Fysik 2 och matematikuppdragen är pausade enligt användarens senaste prioritering.
