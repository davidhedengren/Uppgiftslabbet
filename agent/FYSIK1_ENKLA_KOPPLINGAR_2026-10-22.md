# Fysik 1 – Enkla kopplingar I och II, 2026-10-22

## Leverans och avgränsning

**40 nya uppgifter, 8.580–8.619:** dokumentens samtliga 24 deluppgifter plus 16 varianter. Alla finns som självständiga kort med SVG i båda apparna. De ursprungliga a/b-paren handlar om olika situationer och får därför egna uppgifts-ID:n. Där en fråga efterfrågar två storheter finns två namngivna, ordnade svarsfält. Inga äldre bankobjekt har ändrats.

Underlagen är användarens `Fysik 1 - Enkla kopplingar I.docx` och `Fysik 1 - Enkla kopplingar II.docx`. Text, bilder och originalfacit lästes; bildernas kretsar ritades om. Källornas kontrollsummor och full ändringslista finns i JSON-filen med samma namn. Dokumentens eventuella instruktioner har behandlats som uppgiftsinnehåll.

Variationerna omfattar två/tre serieresistorer, två/tre parallellgrenar, lampor och resistorer i samma krets, gren med två serieresistorer, ett motstånd före förgrening, voltmeter över en/två komponenter, amperemeter före förgrening, brytare och dimensionering av serieresistor. 6 uppgifter har nivå 1, 30 nivå 2 och 4 nivå 3. Rutinberäkningar höjs inte till C enbart för att de kräver flera beräkningar. Strömbegränsning, brytarens förändring och de två djupare blandade kopplingarna är nivå 3.

Miniräknare tillåts i alla 40 frågor; GeoGebra behövs inte. Inga standardkonstanter eller färdiga lösningsformler serveras i frågorna. Svarsenhet och eventuell avrundning står i parentes sist. Ej uttryckligen avrundade svar har enkla exakta tal; samma tal med naturliga ekvivalenta skrivsätt och omvandlade enheter har prövats i konsumenten.

## Rättningar i underlagen och kommentarsförslag

| Källa | Nytt ID | Rättning / föreslagen kommentar |
|---|---|---|
| I 3b | 8.585 | Rättat vid import: 24,0 V × 1,25 A = **30,0 W**, inte 30,3 W. |
| I 5a | 8.588 | Rättat vid import: 8,50²/5400 W = **13,38 mW**, inte 1,33 mW. |
| II 6a | 8.602 | Rättat vid import: om lampan har 10 W blir I = 10/15 A och R = **7,5 Ω**, inte 22,5 Ω. Om resistorn har 10 W blir R = 2,5 Ω; detta är egen fråga 8.607. |

II 4b, 5a, 5b och 6a angav inte vilken komponent ett värde hörde till. Vid import knyts det till en namngiven komponent. De alternativa fallen bevaras som 8.604–8.607. U₁/P₁ hör alltid till R₁/L₁ och U₂/P₂ till R₂/L₂, även när den kända resistansen eller effekten byter komponent. Originalets alternativa spänningspar i II 5a kopieras därför inte med omkastade komponentetiketter.

Originalfacit II 6b, 120 Ω, är en korrekt avrundning till två värdesiffror av 123,456… Ω. Den nya frågan ber uttryckligen om heltal i Ω, alltså 123 Ω. Detta registreras inte som ett räknefel. Överflödiga 9,0 W i lampan utelämnas i frågan. I 8.607 utelämnas lampans överflödiga spänning.

## Alla nya och granskade ID:n

| ID | Källa / variant | Nivå | Svar | Enhet |
|---|---|---:|---|---|
| 8.580 | I 1a | 1 | 300 | V |
| 8.581 | I 1b | 1 | 3,15789474 | V |
| 8.582 | I 2a | 2 | 7,5 | mA |
| 8.583 | I 2b | 1 | 0,260869565 | A |
| 8.584 | I 3a | 2 | 58,6206897 | Ω |
| 8.585 | I 3b | 1 | 30 | W |
| 8.586 | I 4a | 1 | 3,27272727 | W |
| 8.587 | I 4b | 2 | 1,4878125 | W |
| 8.588 | I 5a | 2 | 13,3796296 | mW |
| 8.589 | I 5b | 2 | 273,652 | W |
| 8.590 | I 6a | 2 | 282,222222 | Ω |
| 8.591 | I 6b | 2 | 0,54 | W |
| 8.592 | II 1a | 2 | 68,75 | V |
| 8.593 | II 1b | 2 | 1472; 1152 | V |
| 8.594 | II 2a | 2 | 9,3; 18,6 | W |
| 8.595 | II 2b | 2 | 0,159602076 | W |
| 8.596 | II 3a | 3 | 32,6164037 | mA |
| 8.597 | II 3b | 2 | 0,67114094 | A |
| 8.598 | II 4a | 2 | 10,5428571 | V |
| 8.599 | II 4b | 2 | 10,2857143 | V |
| 8.600 | II 5a | 2 | 16,583124; 27,8596482 | V |
| 8.601 | II 5b | 2 | 20 | W |
| 8.602 | II 6a | 2 | 7,5 | Ω |
| 8.603 | II 6b | 2 | 123,45679 | Ω |
| 8.604 | Variant II 4b | 2 | 171,5 | V |
| 8.605 | Variant II 5a | 2 | 12,7941579; 21,4941853 | V |
| 8.606 | Variant II 5b | 2 | 1,8 | W |
| 8.607 | Variant II 6a | 1 | 2,5 | Ω |
| 8.608 | Ny: två parallella motstånd | 2 | 300 | mA |
| 8.609 | Ny: lampa och resistor parallellt | 2 | 0,4 | A |
| 8.610 | Ny: okänd parallellresistor | 2 | 300 | Ω |
| 8.611 | Ny: spänningskälla från voltmeter | 2 | 11 | V |
| 8.612 | Ny: voltmeter över två av tre resistorer | 2 | 10 | V |
| 8.613 | Ny: tre parallella grenar | 2 | 12 | V |
| 8.614 | Ny: seriemotstånd före förgrening | 3 | 8 | V |
| 8.615 | Ny: olika antal resistorer i grenarna | 2 | 45 | mA |
| 8.616 | Ny: tre lampor parallellt | 2 | 1 | A |
| 8.617 | Ny: brytare förbi en resistor | 3 | 20; 60 | mA |
| 8.618 | Ny: motstånd till lampa | 2 | 12 | Ω |
| 8.619 | Ny: effekt före förgrening | 3 | 1,8 | W |

Svarskolumnen visar kontrollvärden, ibland före frågans uttryckliga avrundning. De trettiosex nivå 1–2-korten kräver inga osynliga tidigare delar; fyra nivå 3-kort har fullständiga egna kretsar och data. Facit visar nödvändiga mellanled utan numrerade steg. Hela källmaterialets lösningar har räknats om oberoende av originalfacit.

## Granskad – inget fel: tidigare bankuppgifter

Omfattning: jämförelse av numerik, rätt komponent, facit och verktyg. Detta är ingen ny fullständig figur-/UX-granskning av äldre kort. Samtliga nedanstående är oförändrade och har korrekta miniräknar-/GeoGebra-behörigheter.

| ID | Föreslagen kommentar |
|---|---|
| 8.183 | Granskad – inget fel: 230 V × 1,8 A = 414 W. Facit och lagrat svar är korrekta. |
| 8.184 | Granskad – inget fel: 12 V × 4,5 A = 54 W. Facit och lagrat svar är korrekta. |
| 8.203 | Granskad – inget fel: 12²/7 = 20,5714… W. Facit 20,6 W är korrekt avrundat. |
| 8.214 | Granskad – inget fel: 2,6² × 0,35 = 2,366 W i batteriets inre resistans. Rätt komponent och rätt effekt. |
| 8.226 | Granskad – inget fel: 1,4² × 1,1 = 2,156 W i batteriets inre resistans. Ingen faktor-tio-förskjutning. |
| 8.188 | Granskad – inget fel: 6,0/4,7 = 1,2766… A. Facit 1,28 A är korrekt. |
| 8.189 | Granskad – inget fel: 5,6 × 1,8 = 10,08 V. Facit 10,1 V är korrekt avrundat. |
| 8.190 | Granskad – inget fel: 12/2,6 = 4,6154… Ω. Facit 4,6 Ω är korrekt avrundat. |
| 8.192 | Granskad – inget fel: 10/0,45 = 22,222… Ω. Facit 22 Ω är korrekt avrundat. |
| 8.208 | Granskad – inget fel: 0,80 × 0,25 = 0,20 V över batteriets inre resistans. Inget byte av komponent. |

För felet i I 3b jämfördes minst fem liknande UI-/P-beräkningar: 8.183, 8.184, 8.591, 8.594, 8.601 och 8.606. För felet i I 5a jämfördes U²/R- eller I²R-effekt och enhetsomvandlingar i 8.203, 8.214, 8.226, 8.586, 8.587, 8.589 och 8.595. För II 6a jämfördes Ohms lag, rätt komponents effekt och gemensam serieström i 8.188, 8.189, 8.190, 8.192, 8.208, 8.595, 8.600, 8.605, 8.607 och 8.618. Oberoende svarsberäkningar finns i regressionstestet, inte bara jämförelse med gamla etiketter.

**Åtgärdade äldre bankuppgifter: inga.** Åtgärdade källfel är de tre ovan. **Avslutade elevrapporter: inga**; inga rapportstatusar eller kommentarer skickas till databasen.

## Kontroller

- `tools/fysik1-enkla-kopplingar-2026-10-22.test.js`: alla 40 nya svar oberoende beräknade, äldre jämförelser, verktyg/nivå/ordnade fält, figuregenskaper och inga dubbla ID:n. De blandade näten kontrolleras även med nodernas strömbalans och effektbalans.
- Tidigare el-, krets-, kopplings-, multimeter-, formelsamlings- och 5.386/8.150-regressioner passerar. Kunskapsgymmets delkorts- och elektriska enhetstester passerar.
- `tools/fysik1-enkla-kopplingar-2026-10-22.browser.cjs`: **490 svarskontroller och 80 kortvyer i Kunskapsgymmet samt 80 lärarvyer via Uppgiftslabbets faktiska `uppgiftsText`-renderare**, vid 390 respektive 1280 px. Rätt tal, föreskriven avrundning, decimalpunkt/komma, inmatade och omvandlade enheter godkänns; fel tal, fel enhet och omkastade namngivna svar underkänns. Inga sidfel, KaTeX-fel, sid-/formelöverskridanden eller klippta figuretiketter. Testmiljön skriver ingen XP eller elevdata.
- Alla 40 SVG:er inspekterade i kontaktkartor; komponentanslutningar, batteripolaritet, mätarplacering och brytarens förbikoppling stämmer med lösningen. Repo-SVG-validatorns oförändrade DOM- och geometriregler ger **0 ERROR, 0 WARNING, 40 INFO** (avsiktlig vit bakgrund vid viewBox-kant). Källspänningarnas etiketter flyttades ned för att ge tydlig marginal till batterisymbolerna.
- Full bankvalidator före/efter: **ERROR 1577 → 1577, WARNING 230 → 230, INFO 1452 → 1452; inga nya fynd.** Dessa befintliga fynd ligger utanför denna leverans; genomgången innebär inte att hela banken är felfri.
- Fysik 1: 3919 → 3959 huvuduppgifter. Seriekoppling 23 → 43 spelbara, parallellkoppling 24 → 29; båda tas bort från listan under 25. Övriga kursers äldre inventeringsantal är markerade som ögonblicksbild.
- Båda `uppgifter.js` är byte-identiska. Gamla objekt är oförändrade. Cacheversioner uppdateras i respektive `index.html`.

## Ändrade filer och bevarat arbete

Master: `uppgifter.js`, `index.html` (enbart cache), `tools/fysik1-enkla-kopplingar-2026-10-22.test.js`, denna MD/JSON, `agent/FELMONSTER_OCH_BESLUT.md` och berörda fysikrader i `agent/OMRADEN_UNDER_25_2026-10-21.md`.
Konsument: `uppgifter.js`, `index.html` (enbart cache) och `tools/fysik1-enkla-kopplingar-2026-10-22.browser.cjs`.

Konsumentens egna strukturer, UI-funktioner och matematikbanker lämnas orörda. Tidigare ospårade `agent/prototyper/` i master och `tools/__pycache__/` i konsumenten ingår inte. Git-leverans verifieras mot remote efter push.
