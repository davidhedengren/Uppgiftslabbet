# A-uppgifter på nivå 4–5, omgång 2, 11 november 2026

## Uppdrag

Fortsättning på `A_UPPGIFTER_2026-11-10.md`: välkonstruerade A-uppgifter på träningsnivå 4–5 i centrala områden, med facit enligt `FACITMALL.md`. Den här omgången tar nästa grupp områden som saknade eller nästan saknade kort på nivå 5.

## Fysik 1 (`uppgifter.js`): 6 uppgifter, 17 kort

| ID | Område (delmoment) | Innehåll | Nivå per del |
|---|---|---|---|
| 4.912 | `friktion` (Friktion och Newtons andra lag) | Låda på ett lastbilsflak som bromsar: a) största retardation utan glidning, b) lådans retardation när den glider, c) tiden tills lådan slår i framstammen (relativ rörelse). | 3, 3, 5 |
| 5.639 | `rorelseenergi` (Nettoarbete och energiförluster) | Bil som bromsar för ett träd över vägen: a) bromssträckan från 50 km/h, b) avståndet till trädet, c) farten vid trädet om utgångsfarten är 70 km/h. | 3, 4, 5 |
| 5.640 | `effekt` (Verkningsgrad) | Länspump i en översvämmad källare: a) vattnets lägesenergi, b) verkningsgraden när vattnet får både lägesenergi och rörelseenergi, c) pumptiden med ett grövre munstycke. | 3, 4, 5 |
| 7.232 | `varme` (Värmebalans och termisk jämvikt) | Te i en kall porslinsmugg: a) gemensam temperatur, b) hur mycket kall mjölk som ger 60 °C när muggen också svalnar. | 4, 5 |
| 3.747 | `vektorer` (Relativ hastighet) | Ambulanshelikopter i sidvind: a) kursvinkeln, b) flygtiden, c) flygtiden när vinden blåser från sydväst (komposanter i två led). | 3, 4, 5 |
| 5.641 | `rorelsemangd` (Impuls och medelkraft) | Puck som slås tillbaka, med kraft–tid-graf: a) impulsen, b) farten efter slaget, c) tidpunkten då pucken står stilla (del av arean). | 3, 4, 5 |

Före påfyllnaden hade `friktion`, `varme`, `vektorer` och `rorelsemangd` 0–1 kort på nivå 5, och `rorelseenergi` och `effekt` hade 2 var.

### Idéer som byttes eftersom de redan fanns

Varje idé kontrollerades mot banken innan uppgiften skrevs. Fyra planerade uppgifter byttes:

- Pulka som dras eller skjuts snett (finns som 4.398, 4.547 och 4.551) byttes mot lådan på lastbilsflaket. Befintliga 4.118 frågar bara om lådan börjar glida.
- Hiss med motvikt (finns som 5.78 och 5.272) byttes mot länspumpen. Befintliga pumpuppgifter bortser uttryckligen från rörelseenergin.
- Tennisserve med triangelformad kraftkurva (finns som 5.366) byttes mot pucken, som har fart från början, vänder och kräver en del av arean.
- Flygplan i sidvind fanns som 3.657 (fart och kursavvikelse). Den nya uppgiften frågar åt andra hållet (vilken kurs som ger färd rakt norrut) och har vind snett bakifrån i sista delen.

## Utformning

Samma principer som i omgång 1:

- Alla uppgifter har `niva: "A"` och `traningsniva: 5`. Delarna går i stigande svårighet och den sista delen är A på nivå 5.
- Alla delkort börjar med samma inledning och figur. När en senare del bygger på ett tidigare resultat står det i delkortets fråga (till exempel ”Lådans retardation är då 3,93 m/s²”). Huvuduppgiftens text innehåller inte mellanresultaten, och inget delfacit avslöjar en senare dels svar.
- Varje delfacit börjar med ”Givet och sökt” och har formeln utskriven i en rubrik. Rubrikerna är skrivna för uppgiften. Svarsraden har enhet och stämmer med `rättSvar` och `svarVardesiffror`.
- Varje uppgift har en egen SVG-figur i frågan, och alla utom 7.232 har också en förklarande figur i facit: krafterna på lådan, sträckorna vid 50 och 70 km/h, energistaplar för pumpen, vektortrianglar för helikoptern och skuggade areor i kraft–tid-grafen.
- Enheten skrivs i frågan bara när den inte är en naturlig SI-enhet eller när givna värden har en annan enhet av samma slag (km/h, kJ, %, min, gram, ms). Inga avrundningskrav skrivs ut. Facit lagras oavrundat.
- Miniräknare är tillåten. GeoGebra är inte tillåten, eftersom uppgifterna prövar modellering och algebra.

### Nytt i den här omgången: tal som tål avrundade mellanresultat

Kunskapsgymmets rättning visade att tre deluppgifter i första utkastet var känsliga för avrundning. En elev som räknade vidare med sitt avrundade delsvar fick ett slutsvar som avrundas åt andra hållet:

- 5.639 c: med avståndet 25 m (i stället för 24,89 m) blev farten 56 km/h, inte 57 km/h.
- 5.640 c: med verkningsgraden 65 % (i stället för 65,3 %) blev tiden 8,0 min, inte 7,9 min.
- 7.232 b: med temperaturen 79 °C (i stället för 78,6 °C) blev mjölkmängden 120 g, inte 110 g.

Talen i uppgifterna är därför valda så att mellanresultatet ligger nära ett avrundat värde (24,03 m, 62,01 % och 80,99 °C). Slutsvaret blir då detsamma med två och tre värdesiffror, vare sig eleven räknar med det exakta eller det avrundade mellanresultatet. Regressionstestet kontrollerar detta för alla fyra uppgifter där en del bygger på en tidigare. Regeln är inlagd i `FELMONSTER_OCH_BESLUT.md`.

## Kontroll

- **Byggskript:** `tools/bygg-a-uppgifter-fy1-2026-11-11.py` (hjälpfunktioner i `tools/a_uppgifter_hjalp.py`). Varje svar räknas i skriptet och kontrolleras med assert mot en oberoende metod: lådan och framstammen i vägens system, rörelseformler i stället för energi, energibalans som går jämnt upp, vektorsumma utan östkomposant och numerisk integration av kraftkurvan.
- **Kunskapsgymmets rättning:** `tools/kg-sjalvrattning-kontroll.cjs` godtar alla prövade rätta svar (med två, tre och fyra värdesiffror, med och utan enhet) och underkänner alla prövade felsvar, bland annat föregående dels svar och typiska felräkningar. Den inbyggda facitkontrollen anmärker på oavrundat facit för kort med `svarVardesiffror`, precis som för befintliga kalibrerade kort.
- **Rendering:** alla 23 facit (huvudfacit och delfacit) renderas i 390 px utan KaTeX-fel eller för breda rader. Frågekorten, alla facit och alla facitfigurer är granskade som bilder. Efter granskningen bröts tre långa rader, figurtexterna förstorades, energistapeln gjordes om till rader och vinkelbeteckningen i vektortriangeln flyttades.
- **SVG-granskning:** `tools/granska-svg.js` ger inga fel på ERROR-nivå för de nya figurerna. Fyra varningar gäller text som ligger nära eller på geometri (etikett på lådan, etiketter i de skuggade areorna, måttext vid streckad linje). De är avsiktliga och kontrollerade i bild.
- **Regressionstest:** `tools/a-uppgifter-2026-11-11.test.js` kontrollerar nivåer, facitformat, figurer, oberoende omräkning, tålighet mot avrundade mellanresultat, självbärande delkort och svarsinstruktioner.
- **Områdestester i Fy1:** de nya uppgifterna är inlagda med egna uttryck i beräkningstabellerna i `fysik1-kapitel3` (vektorer), `fysik1-kapitel4` (friktion), `fysik1-rorelseenergi`, `fysik1-effekt` och `fysik1-rorelsemangd`. Antalen är höjda i dem och i `fysik1-kap23-slutkontroll`. `fysik1-prosa` undantar 7.232 och 5.641, som följer facitmallen. `fysik1-varme` har två tester som var röda redan före påfyllnaden (de kräver den äldre regeln utan steglista och en äldre avrundning i 7.144); bara antalet uppgifter är höjt där.
- **Valideraren:** 0 fel, och samma antal varningar och infofynd som före påfyllnaden (inga nya likhetsfynd).

## Fortsättning

Områden i Fy1 som fortfarande saknar nivå 5: `acceleration`, `at_diagram`, `tryck`, `kretsar`, `falt`, `parallellkoppling`, `seriekoppling`, `aktivitet` och flera mindre områden i kapitel 9.
