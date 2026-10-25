# Ma3: kvalitet, progression och variation – 2026-10-25

69 uppgifter granskade individuellt: **22 ändrade i banken, 5 ytterligare med rättad självrättning och 42 granskade utan konstaterat fel**. Inga nya uppgifter eller ID:n, inga borttagna uppgifter. Alla ID:n och kommentarförslag finns nedan och i JSON-filen. Inga felrapporter har stängts automatiskt.

## Omfattning och fynd

Strukturell inventering av 393 huvuduppgifter i fem områden. Detta är **inte** ett påstående om full manuell granskning av alla 393. De 69 nedan har fått riktad manuell kontroll; ytterligare kort har bara deltagit i tekniska tester. Uppgifter som kräver fri motivering är fortsatt manuella.

- Typografiska primtecken fungerade för talargument men inte variabelargument i `hogerled`. Korrekt `f′(x)=…` kunde ge fel medan ASCII-apostrof fungerade. Nu stöds även ′, ″ och ’ utan att ändra tecken inne i högerledet eller vinkelenheter.
- #3.921 och #3.1052 hade avrundat jämförelsemål och för stor tolerans. De var också dubbletter. De har nu olika frågor, fullprecisionsmål och tolerans 0,005. #3.1011 behålls med sin redan korrekta tidigare rättning.
- Sex uppgifter har fått andra frågeidéer: omvänd tangentlutning, derivatans tecken, förändring utan startvärde, baklängesbestämt startvärde och vertikal förskjutning. Originalrutinerna behålls.
- Nio nivåer justeras utifrån metodkraven. Flera termvisa operationer flyttas från 1 till 2; enkel koefficientjämförelse från 4 till 2; tangentproblemet #2.812 från 5 till 3, jämfört med #2.1227. En rutin kan fortfarande höra till nivå 3 när algebra och samband kräver det.
- #3.198: växande innebär inte strikt positiv derivata i varje punkt. #3.178 får intervallet som behövs för slutsatsen om en konstant skillnad.
- Formelrader som blev för breda på mobil har delats. #3.1106 får hastighetsenhet även i svarsfält och slutrad; #3.1016 får tydligare definition av tidsvariabeln och mellanled.

## Fem jämförelser per feltyp

- Primtecken: #2.02 samt #2.10, #2.212, #2.250, #2.539, #2.1167. Även talargument #2.30/#2.34 och äldre vänsterledstester.
- Precision: #3.921 samt #3.1052, #3.1011, #2.08, #2.44, #2.48, #2.52.
- Mobila formelrader: #3.283 samt #3.134, #3.138, #3.142, #3.146, #3.150; utökades till alla 69 och gav fler layoutfixar.
- Monotoni: #3.198 samt #2.176, #2.1258, #2.140, #2.150, #3.207. Korrekt givna derivatatecken ändras inte.
- Intervall/konstanter: #3.178 samt #3.58, #3.82, #3.142, #3.1217, #3.1226.
- Enhet: #3.1106 samt #3.898, #3.1014, #3.1100, #3.1105, #3.1079.

## Verktyg och figurer

Verktygen kontrollerades på verkliga kort. GeoGebra behövs inte för dessa algebraiska metod- och begreppsuppgifter. De befintliga uppgifterna utan miniräknare har små enkla tal eller testar symboliska samband; inga större numeriska beräkningar krävs. #2.825 har bara x²=4 och 2+4/2. Uppgifter med exponentialfunktioner/numeriska logaritmer tillåter miniräknare.

#2.812 får en egen SVG med korrekt placerad y-axel, given punkt och tangentpunkt. Kurvan och tangenten kontrolleras mot √x och y=(x+4)/4; P=(4,2). P-etiketten flyttades efter kollisionstest. Slutlig SVG-kontroll har ingen varning; enda informationen gäller den avsiktliga bakgrundsrektangeln. De andra algebraiska ändringarna behöver ingen dekorativ figur. Befintliga figurer i jämförelseuppgifterna kontrollerades också visuellt.

## Tester

- Oberoende SymPy-derivering av bankens faktiska svar, initialvillkor, tangentgeometri och avrundning: godkänt (`tools/ma3-kvalitet-2026-10-25.test.py`).
- Verkliga svarsfält och renderade facit vid 390/1280 px i båda apparna: godkända, inklusive negativa svarskontroller, fel enhet och ordnade koordinatfält. Fallfilen innehåller även naturliga rot-, potens-, funktions- och konstantnotationer.
- 132 jämförelser för 36 primitivkort och tidigare exponentialregressioner: godkända. Detta är en teknisk formatkontroll, inte separat manuell granskning av alla dessa kort.
- 60 deterministiska urvalsfall, varav 54 med tillgängliga kort, totalt 507 val: ingen upprepad kortidentitet inom respektive pass innan urvalet är slut. Tomma nivå-4-urval redovisas som tomma, inte som genomförda pass. Ingen ändring av urvalsmotorn behövdes. Detta säger inte att varje vald rutin är pedagogiskt unik.
- Tidigare sex Ma3-/primitivregressioner och tre tester av uttryck/vänsterled: godkända.
- Hela Ma3-banken: 0 ERROR, 47 WARNING, 177 INFO (före rundan 0/50/178). Kvarvarande historiska varningar redovisas, de är inte alla utredda här.

## Nästa prioritet

I Kunskapsgymmets faktiska 1c-urval finns 24 C-kort i potensderivata, 20 i primitiva funktioner och 20 i derivatabegreppet. Däremot finns bara **3 C-kort i deriveringsregler och 4 i primitiva funktioner med villkor**. Nästa påfyllnad bör riktas dit, med omvända frågor, parametrar och tolkning vid sidan av vanlig mängdträning. Antalet huvuduppgifter är inte samma sak som antalet spelbara kort.

## Samtliga granskade uppgifter och kommentarförslag

| ID | Status | Kommentar |
| --- | --- | --- |
| #2.02 | Åtgärdad i självrättningen | Åtgärdad: typografiskt primtecken i exempelvis f′(x)= godkänns nu. Facit är oförändrat. |
| #2.08 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.10 | Åtgärdad i självrättningen | Åtgärdad: typografiskt primtecken i exempelvis f′(x)= godkänns nu. Facit är oförändrat. |
| #2.30 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.34 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.44 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.48 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.52 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.140 | Granskad – inget fel | Granskad – inget fel: derivatan byter + till − vid −1 och − till + vid 3. |
| #2.150 | Granskad – inget fel | Granskad – inget fel: minimum vid −2 och maximum vid 2. |
| #2.176 | Granskad – inget fel | Granskad – inget fel: x³ är ett giltigt exempel på en växande funktion med derivatan noll i en punkt. |
| #2.212 | Åtgärdad i självrättningen | Åtgärdad: typografiskt primtecken i exempelvis f′(x)= godkänns nu. Facit är oförändrat. |
| #2.250 | Åtgärdad i självrättningen | Åtgärdad: typografiskt primtecken i exempelvis f′(x)= godkänns nu. Facit är oförändrat. |
| #2.539 | Åtgärdad | Åtgärdad: Delar upp derivatans potensform och bråkform i facit för mobilvisning; samma svar. |
| #2.585 | Granskad – inget fel | Granskad – inget fel: derivatan av 1/x vid x=1 är −1. Bevarad rutinuppgift. |
| #2.605 | Granskad – inget fel | Granskad – inget fel: derivatan av √x vid x=4 är 1/4. Bevarad rutinuppgift. |
| #2.740 | Åtgärdad | Åtgärdad: Nära dubblett av #2.605 blir omvänd användning av samma derivata; nivå 2 kvar. |
| #2.744 | Åtgärdad | Åtgärdad: Nära dubblett av #2.585 blir kvalitativ teckenfråga för negativ x; nivå 2 kvar. |
| #2.812 | Åtgärdad | Åtgärdad: 5 → 3: samma metodkrav som #2.1227, en okänd tangentpunkt och en linjär ekvation efter förenkling. Tydligare mellanled och situationsfigur. |
| #2.825 | Åtgärdad | Åtgärdad: 4 → 3: vanlig extremvärdesundersökning med negativ potens, positiv domän och teckenkontroll. |
| #2.1167 | Åtgärdad i självrättningen | Åtgärdad: typografiskt primtecken i exempelvis f′(x)= godkänns nu. Facit är oförändrat. |
| #2.1227 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #2.1258 | Granskad – inget fel | Granskad – inget fel: den vågräta tangenten är inte ett extremställe. |
| #3.46 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.52 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.58 | Åtgärdad | Åtgärdad: 4 → 3: kort samband mellan derivatan av en skillnad och en konstant funktion; manuell motivering kvar. Kortare formelrader för mobilvisning. |
| #3.82 | Granskad – inget fel | Granskad – inget fel: derivatan av 2x³+4/x+C är 6x²−4/x². Uppgiften är fortsatt manuell. |
| #3.134 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.138 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.142 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.146 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.150 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.162 | Granskad – inget fel | Granskad – inget fel: både derivatan och det givna funktionsvärdet stämmer. En godtycklig konstant ska inte godkännas här. |
| #3.174 | Granskad – inget fel | Granskad – inget fel: både derivatan och det givna funktionsvärdet stämmer. En godtycklig konstant ska inte godkännas här. |
| #3.178 | Åtgärdad | Åtgärdad: Samma intervall måste anges, i linje med den tidigare rättningen av #3.58. Kortare formelrader för mobilvisning. |
| #3.182 | Åtgärdad | Åtgärdad: 4 → 2: derivera en given funktion och jämför en koefficient. |
| #3.194 | Åtgärdad | Åtgärdad: 4 → 2: F′ är redan given som f. Horisontell tangent ger en enkel insättning. |
| #3.198 | Åtgärdad | Åtgärdad: Korrigerar slutsatsen växande ⇒ strikt positiv derivata. Enstaka nollvärden kan förekomma. |
| #3.207 | Granskad – inget fel | Granskad – inget fel: maximum vid −3 och minimum vid 1. |
| #3.213 | Granskad – inget fel | Granskad – inget fel: skillnadens derivata är noll och skillnaden vid x=0 är 3. |
| #3.236 | Granskad – inget fel | Granskad – inget fel: uppgiften efterfrågar en primitiv funktion; extra konstant godkänns. |
| #3.283 | Åtgärdad | Åtgärdad: Nivå 2 och mobilfacit med separata mellanled; svaret och primitiv-formatet oförändrade. |
| #3.284 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.355 | Åtgärdad | Åtgärdad: Kortare formelrader i fråga och facit så båda funktionerna syns på mobil; samma matematik och nivå. |
| #3.551 | Åtgärdad | Åtgärdad: 1 → 2: flera termvisa operationer eller jämförelse av flera derivator; behålls som E-mängdträning. Mobilanpassat facit. |
| #3.617 | Åtgärdad | Åtgärdad: 1 → 2: flera termvisa operationer eller jämförelse av flera derivator; behålls som E-mängdträning. |
| #3.727 | Åtgärdad | Åtgärdad: 1 → 2: flera termvisa operationer eller jämförelse av flera derivator; behålls som E-mängdträning. |
| #3.792 | Åtgärdad | Åtgärdad: Kortare formelrader i facit för mobil; konstanten och svaret oförändrade. |
| #3.898 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.921 | Åtgärdad | Åtgärdad: Exakt dubblett blir förändring mellan två x-värden; fullprecisionsmål och halv hundradels tolerans ersätter för stor tolerans. |
| #3.923 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.1011 | Granskad – inget fel | Granskad – inget fel: e+3 ger 5,72. 5,71 och 5,73 underkänns korrekt; tidigare precisionsrättning bevaras. |
| #3.1012 | Granskad – inget fel | Granskad – inget fel: villkoret ger C=1 och F(2)=13. Bevarad rutinuppgift. |
| #3.1014 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.1015 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.1016 | Åtgärdad | Åtgärdad: Förtydligar tidsvariabeln och visar insättning och startvolym i facit. Svaret 28 liter oförändrat. |
| #3.1052 | Åtgärdad | Åtgärdad: Exakt dubblett av #3.1011 blir baklängesberäkning av ett startvärde; nivå 2 kvar. |
| #3.1057 | Åtgärdad | Åtgärdad: Exakt dubblett av #3.1015 blir enkel vertikal förskjutning av en primitiv funktion; nivå 1 kvar. |
| #3.1063 | Åtgärdad | Åtgärdad: Exakt dubblett av #3.1012 blir bestämning av skillnad utan givet startvärde; nivå 2 kvar. |
| #3.1079 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.1100 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.1105 | Granskad – inget fel | Granskad – inget fel: facit och de kontrollerade svarssätten stämmer. |
| #3.1106 | Åtgärdad | Åtgärdad: Anger hastighetens enhet i frågan och svarsfältet; korrekt svar med eller utan m/s. |
| #3.1147 | Granskad – inget fel | Granskad – inget fel: dubbelrot ger C=4/3. |
| #3.1217 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.1218 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.1220 | Granskad – inget fel | Granskad – inget fel: derivering av facit ger den angivna funktionen. Ekvivalenta uttryck med en fri konstant godkänns. |
| #3.1223 | Granskad – inget fel | Granskad – inget fel: förändringen är integralen av √x; sekantens lutning blir 13/6. |
| #3.1226 | Granskad – inget fel | Granskad – inget fel: på åtskilda intervall kan integrationskonstanterna vara olika. |
