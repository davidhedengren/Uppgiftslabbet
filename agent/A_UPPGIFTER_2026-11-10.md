# Välkonstruerade A-uppgifter på nivå 4–5 i Ma3c och Fysik 1, 10 november 2026

## Uppdrag

Användaren: ”Fortsätt förbättra banken, kanske med välkonstruerade A-uppgifter på nivå 4–5 i de olika områdena. Börja med de vanligaste och viktigaste områdena och skippa de små specificerade. Kör igång med Ma3 och Fysik 1. Se också till att facit ser bra ut och följer mallen.”

## Urval

Före påfyllnaden hade Fy1 nästan inga kort på träningsnivå 5 och få A-uppgifter, också i centrala områden: `newton2` hade 1 kort på nivå 5, och `lutande_plan`, `kollisioner`, `gaslagen`, `fasandring` och `friktion` hade 0. I Ma3c hade `extrempunkter`, `areasatsen`, `cosinussatsen` och `faktorisera_polynom` inga kort på nivå 5.

Den här första omgången lägger en A-uppgift i vart och ett av femton centrala områden. Små och specialiserade områden är överhoppade. Varje uppgift är handskriven med egen situation, och idéerna är kontrollerade mot banken så att de inte dubblerar befintliga uppgifter. Två planerade uppgifter byttes av det skälet: gemensam tangent i stället för tangenter genom en yttre punkt (2.51 finns), och en vänd cylinder med kolv i stället för en varmluftsballong (6.22 finns).

## Ma3c (`uppgiftermato1.js`): 7 uppgifter, 17 kort

| ID | Område (delmoment) | Innehåll | Nivå per del |
|---|---|---|---|
| 2.1285 | `tangenter` (Fördjupade tangentproblem) | Den andra gemensamma tangenten till y = x² och y = −x² + 4x − 4. Svar y = 4x − 4. | 5 |
| 3.1271 | `integralberakning` (Area mellan två grafer) | y = x³ och tangenten i (1, 1): a) tangentens ekvation, b) den andra skärningspunkten med dubbelrotsresonemang, c) arean 27/4. | 3, 4, 5 |
| 3.1272 | `extrempunkter` (Extrempunkter med parameter) | f(x) = x³ + ax² − 9x med maximum i x = −1: a) a, b) minimivärdet, c) antalet heltal k som ger tre lösningar till f(x) = k. | 3, 4, 5 |
| 4.609 | `areasatsen` (omvända problem) | Två sidor och arean givna, två möjliga trianglar: a) de två vinklarna, b) de två längderna på den tredje sidan. | 4, 5 |
| 1.1100 | `polynomekvationer` (Parameter och antal lösningar) | p(x) = x³ + ax² − 4x − 12 med nollstället 2: a) a, b) övriga nollställen, c) det c som ger p(x) = c(x − 2) en dubbelrot. | 3, 4, 5 |
| 3.1273 | `problemlosning_derivata` (Tolka derivata i modeller) | Vinst och skatt: a) största vinsten, b) den skatt per enhet som ger staten störst intäkt (optimering i två led). | 4, 5 |
| 4.610 | `cosinussatsen` (samband och problemlösning) | Parallellogram med en känd diagonal: a) vinkeln, b) den andra diagonalen, c) konstanten k i d₁² + d₂² = k(a² + b²). | 3, 4, 5 |

## Fysik 1 (`uppgifter.js`): 8 uppgifter, 21 kort

| ID | Område (delmoment) | Innehåll | Nivå per del |
|---|---|---|---|
| 3.746 | `konstacc` (Möte och ikapp) | Persontåg bakom godståg: a) avståndet när bromsningen börjar, b) minsta retardation för att undvika kollision. | 3, 5 |
| 4.910 | `newton2` (F = ma) | Hiss med badrumsvåg i tre faser: a) accelerationen, b) högsta farten, c) hur högt hissen åker. | 3, 3, 5 |
| 4.911 | `lutande_plan` (Glidning på lutande plan) | Kloss uppför plan med friktion: a) sträckan till vändpunkten, b) farten tillbaka i startpunkten. | 4, 5 |
| 5.637 | `blandat_energi` | Fjäder, sträv yta och ramp: a) farten vid rampens fot, b) höjden, c) var klossen till sist stannar. | 4, 4, 5 |
| 5.638 | `kollisioner` (Rekyl och isärskjutning) | Två klossar skjuts isär och bromsas av friktion: a) A:s fart, b) B:s glidsträcka, c) B:s andel av fjäderenergin. | 3, 4, 5 |
| 6.565 | `gaslagen` (Boyles lag) | Cylinder med kolv som vänds upp och ned: a) trycket i gasen, b) luftpelarens nya höjd. | 4, 5 |
| 7.231 | `fasandring` (Energikedjor och värmebalans) | Isbitar i dryck: a) energi för att värma och smälta isen, b) sluttemperaturen, c) minsta antal isbitar för 0 °C. | 3, 4, 5 |
| 8.739 | `kopplingar` (Kretsanalys) | Batteri med inre resistans och blandad koppling: a) polspänningen, b) effekten i R₃, c) ny resistor som ger polspänningen 11,0 V. | 3, 4, 5 |

## Utformning

- **Nivå och poäng.** Alla uppgifter har `niva: "A"` och `traningsniva: 5`. Delarna går i stigande svårighet, och den sista delen är alltid A på nivå 5. De inledande delarna (nivå 3–4, C-poäng) leder in i problemet.
- **Självbärande delkort.** Alla delkort börjar med samma inledning och figur. När en senare del behöver ett tidigare resultat står det i delkortets fråga, till exempel ”Tangenten har ekvationen y = 3x − 2”. Huvuduppgiftens text innehåller inte de mellanresultaten. Inget delfacit avslöjar en senare dels svar.
- **Facit enligt `FACITMALL.md`.** Varje steg har en rubrik som är skriven för uppgiften, och minst en rubrik per delfacit innehåller formeln eller regeln (tidlösa formeln, Newtons andra lag, Boyles lag, areasatsen, cosinussatsen, pq-formeln och så vidare). Fysikfacit börjar med ”Givet och sökt” med omvandlade enheter, positiv riktning och vad som söks. Insättningarna har enheter, och svarsraden stämmer med `rättSvar` och `svarVardesiffror`. Andragradsekvationer löses med pq-formeln och har en grafisk kontroll.
- **Figurer.** Varje uppgift har minst en egen SVG-figur, i frågan eller i facit:
  - Ma3c: parablerna med tangent, kurvan med skuggat område, grafen med extremvärden, de två trianglarna, grafen över skatteintäkten och parallellogrammen.
  - Fy1: tågen, hissen med vågens utslag, det lutande planet med och utan krafter, fjädern med sträv yta och ramp, klossarna med fjäder, cylindern i två lägen och kretsschemat. I facit finns också s–t-graf, v–t-graf och ett stapeldiagram över isbitarnas energi.
  - Figurerna har vit bakgrund och fasta färger, som övriga Fy1-figurer, och fungerar därför i mörkt läge.
- **Ledtrådar.** Varje uppgift och varje delkort har en egen ledtråd som pekar mot nästa tanke utan att ge svaret.
- **Verktyg.** Miniräknare är tillåten i fysikuppgifterna och i de tre matematikuppgifter som har numeriska svar. GeoGebra är inte tillåten, eftersom uppgifterna prövar algebraisk problemlösning.
- **Fysikens svar.** Enheten skrivs i frågan bara när den inte är en naturlig SI-enhet eller när givna värden har en annan enhet av samma slag (kPa, cm, kJ, %, m efter cm). Inga avrundningskrav skrivs ut: precisionen ligger i `svarVardesiffror`. Facit lagras oavrundat, enligt bankens konvention. Materialdata står i uppgiften, och g och lufttrycket slås upp.
- **3.746 a rättas exakt** (`svarVardesiffror: null`). Med tre värdesiffror godtogs annars startavståndet 600 m som en avrundning av 580 m.

## Kontroll

- **Byggskript:** `tools/bygg-a-uppgifter-ma3c-2026-11-10.py` och `tools/bygg-a-uppgifter-fy1-2026-11-10.py`, med gemensamma hjälpfunktioner i `tools/a_uppgifter_hjalp.py`. Varje svar räknas i skriptet och kontrolleras med assert: sympy för matematiken och energi- eller gränsfallskontroller för fysiken.
- **Kunskapsgymmets rättning:** `tools/kg-sjalvrattning-kontroll.cjs` ger 0 fel på de 23 Ma3c-korten. För Fy1 godtas och underkänns alla prövade elevsvar rätt. Den inbyggda facitkontrollen anmärker på det oavrundade facit för kort med `svarVardesiffror`, precis som för befintliga kalibrerade kort (till exempel 2.18). Delar med två svar är prövade med avrundade svar, omvänd ordning och enhet.
- **Rendering:** alla 52 facit (huvudfacit och delfacit) renderas i 390 px utan KaTeX-fel eller för breda rader. Frågekorten och ett urval facit är granskade som bilder, och figurerna är justerade efter granskningen.
- **SVG-granskning:** `tools/granska-svg.js` ger inga fel på ERROR-nivå för de nya figurerna. Fyra varningar om krockande etiketter är åtgärdade. De som återstår gäller axelsiffror med vit kontur mot rutnät och kurvor, vilket är avsiktligt. Granskningen körs i molnmiljön med `CHROME_PATH` satt till ett startskript som anropar `chrome-headless-shell` med `--no-sandbox --disable-dev-shm-usage`.
- **Regressionstest:** `tools/a-uppgifter-2026-11-10.test.js` räknar om alla svar oberoende i JavaScript och kontrollerar nivåer, facitformat, figurer och att delkorten är självbärande.
- **Områdestester i Fy1:** åtta befintliga tester räknar om varje numerisk uppgift i ett område och kräver ett exakt antal uppgifter. De nya uppgifterna är inlagda i testernas beräkningstabeller med egna, oberoende uttryck (`fysik1-kapitel3`, `fysik1-newton2`, `fysik1-lutande-plan`, `fysik1-blandat-energi` och `fysik1-kollisioner`), och antalen är höjda i `fysik1-kap23-slutkontroll`, `fysik1-konstacc-facit` och `fysik1-fasandring`. Testerna för fasändring och fysikprosa förbjöd steglista enligt den äldre regeln och undantar nu uppgifter som följer facitmallen. Svarsraderna i Fy1 är skrivna som vanlig text (”2,8 m/s.”), eftersom testerna läser talet därifrån.
- **Övriga tester:** de 178 testfiler som går igenom Fy1, Ma3c, facit och delkort ger samma resultat som före påfyllnaden. Fem tester var röda redan innan och berörs inte av de nya uppgifterna.
- **Valideraren:** 0 fel för båda bankerna, och samma antal varningar och infofynd som före påfyllnaden (inga nya likhetsfynd).

## Fortsättning

Nästa omgång kan ta fler centrala områden som saknar nivå 5: i Fy1 `friktion`, `rorelseenergi`, `effekt`, `arkimedes`, `varme`, `vektorer` och `kretsar`, och i Ma3c `derivata_potens`, `deriveringsregler`, `primitiva`, `sinussatsen`, `rationella_ekvationer` och `gransvarde`. Därefter Ma4, Ma5, Fy2, Ma1 och Ma2.
