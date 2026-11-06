# Ma2: hitta ett okänt medelvärde, 2026-11-06

## Omfattning och beslut

Användaren vill förstå hur 5,90 hittas i #4.257 och få fyra liknande men varierade uppgifter. Uppgiftslabbet är master. Utgångslägen efter hämtning: master 725e766, Kunskapsgymmet 1a2e583; Ma2-bankerna var identiska. Inga orelaterade bankuppgifter ändrades. Före leverans integrerades samtidiga ändringar till master 2539299 och Kunskapsgymmet ecbc548, inklusive det utvidgade beslutet att inte uppmana till GeoGebra i Ma2-frågor och de nya svarsnormaliseringarna.

### Ändrad: 4.257

- Facit visar först varför mittpunkten 5,95 ger ungefär 95,4 %, för mycket.
- Bredden är fyra standardavvikelser. Banden från μ−σ till μ+3σ ger 34,13+34,13+13,59+2,14 = 83,99 %, ungefär 84 %.
- Den nedre gränsen ger μ−0,05=5,85, alltså μ≈5,90 mm. Övre gränsen kontrolleras separat.
- Symmetrin ger även 6,00 mm. Frågan gäller det mindre medelvärdet.
- GeoGebra-kontrollen kommer efter härledningen. En alternativ systematisk sökning startar vid mittpunkten och visar fyra kontrollvärden.
- Frågan anger nu två decimaler i mm. Verkligt rättningsprov visade att den generella fria avrundningen annars godtog 6 för 5,9, vilket suddar ut skillnaden mot den andra lösningen. 5,9 och 5,90 är fortfarande numeriskt samma korrekta svar; 6 och 5,95 underkänns.
- Svar 5,9, tolerans 0,001, nivå 4 och verktygsmetadata bevarade.

### Nya uppgifter

Alla finns i **Normalfördelning**, `normalfordelat_material`, familjen **Svansar och standardavvikelse**, för 2a/2b/2c. Alla tillåter miniräknare och GeoGebra, har självrättning, ledtråd, normalfördelningsfigur och fullständig lösning med riktiga GeoGebra-bilder. Inga dolda deluppgifter eller facitvärden i frågefiguren.

| ID | Variation | Svar | Träningsnivå |
|---|---|---|---|
| 4.2148 | Hitta båda möjliga medellängderna för metallstift | cirka 50 och 54 mm, valfri ordning | 4 |
| 4.2149 | Välj medelvikten med ett extra villkor och tre band | cirka 210 g | 4 |
| 4.2150 | Största sänkning med oförändrad spridning och krav på andelen inom intervallet | cirka 5 ml; 495 ml är mellanresultatet | 5 |
| 4.2151 | Utgå från båda svansarna tillsammans och välj rätt spegelplacering | cirka 27 minuter | 4 |

Nivåerna bygger på att eleven själv behöver placera intervallet, tolka symmetri eller komplement och skilja mellan parameter och förändring. Detta är fördjupad problemlösning inom normalfördelning, inte rutinfrågor på nivå 1–2.

Figurens procenttal är avrundade. För tre band ger exakt normalmodell cirka 81,85946 %, medan figurens summa ger 81,85 %. Facit förklarar skillnaden och svarstoleranserna täcker de numeriska lösningarna. I komplementbilden summerar GeoGebra med fler siffror än de två visade svansandelarna.

### Granskad – inget fel

Uppföljning av fem närliggande äldre uppgifter, avseende matematiken och vägen till parametrar/andelar:

- **4.51:** Det uttryckligen symmetriska intervallet 22–38 ger medelvärdet 30. 95,4 % ger cirka två standardavvikelser åt varje håll, alltså σ≈4. Lösningen motiverar mittpunkt och gränsavstånd.
- **4.261:** Godispåsar: gränsen 250 g och σ=4 g kombineras med invers normalfördelning för 2,3 %. Det leder till μ≈257,9816 g; medelvärdet gissas inte.
- **4.285:** Mjölpåsar: ändrat underfyllnadskrav leder via invers normalfördelning till μ≈504,0458 g. Minskningen av kasserade påsar och ökningen av total fyllnad beräknas med rätt antal påsar.
- **4.286:** Två maskiner: svansandelarna viktas med respektive produktionsantal innan den betingade andelen beräknas. Ungefär 91 % är rimligt; ingen omotiverad parameter väljs.
- **4.124:** Medelvärdet 12 och standardavvikelsen 3 är givna. Gränsen 15 motsvarar +1σ och ger cirka 84,13 %. Ingen sökning efter okänt medelvärde behövs.

### Visningsfel som hittades under test

Uppgiftslabbets rena kursadress `/ma2/` gjorde att relativa `bilder/...`-adresser söktes under `/ma2/bilder/`. `uppgiftsText` och `LOS` löser nu lokala bildreferenser mot `APP_ROOT`, även på GitHubs reservadress. Externa adresser, data-URL:er och SVG-referenser ändras inte. Fem äldre bildfacit följs upp i browserharnessen: 4.07, 4.261, 4.285, 4.124 och 4.51.

## Verifiering

- 16 riktade Node-tester godkända: nya metod-/bildregressioner samt tidigare normalfördelnings-, normalintervall- och GeoGebra-instruktionsbeslut.
- Oberoende normalintegral med `math.erf` och bisektion: alla fem problem, båda spegelvärdena, förändringsriktningen och söktabellen kontrollerade.
- 52 faktiska rättningsförsök i Kunskapsgymmets `checkAnswer`: kommatecken, enheter, enhetsbyten, omvänd svarsordning, dubblettsvar, fel spegelplacering och förväxling mellan medelvärde och sänkning.
- 10 kortvisningar per app, vid 390 och 1280 pixlar, med öppna facit och bildavkodning. Inga JavaScript- eller KaTeX-fel. Långa formler radbrutna efter uppmätt mobilöverflöde.
- Sex nya riktiga GeoGebra-skärmbilder visuellt granskade. Parametrar och intervall verifierade mot appens XML och resultatet mot appens visade värde. Komplementbilden omfotograferad så att hela resultatraden syns.
- Riktad bankvalidator: fem uppgifter, noll fynd. Strukturell diff: endast `t` och `s` ändras i gamla 4.257; fyra nya ID:n. Bankerna identiska efter synk.

## Reproducerbarhet och begränsningar

- Författarkälla: `tools/ma2-medelvarden-2026-11-06.py`.
- Tester: `tools/ma2-medelvarden-2026-11-06.test.js` och `.browser.cjs`.
- Bildkälla: `tools/ma2-medelvarden-skarmbilder-2026-11-06.cjs`, resultatlogg `tools/ma2-medelvarden-geogebra-2026-11-06.json`.
- Bilderna kommer från riktig lokal GeoGebra Classic 5.4.916.2 (paketet node-geogebra 1.3.2). Webbåtkomst till geogebra.org blockerades i miljön. Inga behörigheter till urklipp begärs eller används av den nya bildharnessen. GeoGebra-bunten ligger utanför repot; ange `GGB_BUNDLE` vid omkörning.
- Kör den nya författarkällan efter äldre normalfördelningsgeneratorer om 4.257 genereras om. Återinför inte den gamla omotiverade uppmaningen att pröva 5,90.
- Browserproven använder lokala appar utan inloggning; inga rapportstatusar eller kommentarer har skrivits till databasen. Produktionens publicering kontrolleras inte av dessa prov.

## Färdigt kommentarsförslag

**4.257:** ”Facit visar nu hur 5,90 hittas: mittpunkten ger för stor andel, medan fyra standardavvikelseband ger ungefär 84 %. Båda möjliga medelvärdena förklaras innan GeoGebra används för kontroll. En systematisk sökmetod finns också. Frågan anger två decimaler så att de två lösningarna kan skiljas åt.”
