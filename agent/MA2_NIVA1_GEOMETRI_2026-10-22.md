# Ma2 kap 3: kort på nivå 1 i geometri – 2026-10-22

Detta är första omgången mot målet om 50–100 varierade kort på nivå 1 per område. Målet står i `CLAUDE.md`.

## Kartläggning

`niva1_oversikt.js` i scratchpad räknar kort som Kunskapsgymmet visar på nivå 1 per område. Den använder appens egna `expandGameTask` och `levelOf`.

| Bank | Områden | Kort på nivå 1 | Områden under 10 | Områden under 25 |
|---|---|---|---|---|
| fy1 | 55 | 1200 | 12 | 37 |
| fy2 | 37 | 263 | 26 | 36 |
| ma1 | 79 | 1197 | 22 | 70 |
| ma2 | 63 | 741 | 35 | 55 |
| mato1 | 50 | 236 | 45 | 50 |
| mato2 | 49 | 1056 | 21 | 35 |
| matf1 | 35 | 384 | 19 | 33 |

Ma2c har prov på kapitel 3–4 vecka 45. Därför började påfyllnaden med de svagaste geometriområdena i kapitel 3.

## Nya uppgifter (3.600–3.647)

Alla har träningsnivå 1, E-nivå, figur och tillåten miniräknare. Det finns 12 kort per område.

| Område | Före | Efter | Innehåll |
|---|---|---|---|
| topptriangel_transversal | 1 | 13 | mittpunkt, givna längdskalor (1/3, 2/3), klätterställning, tält, korsande vägar, välj rätt förhållande, delningsförhållande 1:2 |
| kordasatsen_biskarningssatsen | 1 | 13 | givna delar i figur, produkten PC·PD, välj likheten ab = cd, när satsen gäller, pizza, park, bordsskiva, bisektris (även likbent och 2:3) |
| pythagoras | 5 | 17 | hypotenusa och katet, hitta hypotenusan, skriv satsen, mobilskärm, fotbollsplan, drake, rutnät, ramp, tv, omvändning (8-15-17 ja, 5-6-8 nej) |
| likformighet | 7 | 19 | motsvarande sidor, modellbil 1:20, fotoförstoring, längdskala ur figur, ritning 1:50, rektanglar, omkrets, skuggor (pinne och person), vinkelkriteriet, areaskala |

## Omgång 2: statistik och regressionsmodeller (4.500–4.530, 2.900–2.907)

Alla har träningsnivå 1 och en figur eller tabell.

| Område | Före | Efter | Innehåll |
|---|---|---|---|
| tabeller_diagram | 3 | 15 | stapel-, linje- och cirkeldiagram samt tabeller: avläsa, jämföra, summera och andel av helhet |
| kvartiler_percentiler | 16 | 26 | median (udda och jämnt antal), lådagram (median, kvartilavstånd, största värde, andel i lådan), Q1, percentilbegreppet (Ali, BVC), medianen som 50:e percentil |
| normalfordelning_digitala_verktyg | 4 | 13 | ett steg i GeoGebra (vänster, höger, intervall) i sju olika sammanhang med olika facit, vilka parametrar som ska anges, vad P(X ≤ 60) betyder |
| regressionsanalys_olika_modeller | 8 | 16 | välja linjär, exponentiell eller andragradsmodell ur punkter eller tabell, sätta in i modell, tolka förändringsfaktor, startvärde och R² |

Testet `tools/ma2-niva1-statistik-modeller-2026-10-22.test.js` räknar om normalfördelningsandelarna ur texten och kontrollerar att de sju svaren är olika. Övriga facit räknas om från figurernas och tabellernas data.

## Omgång 3: problemlösning, koordinater och bevis (3.650–3.697)

| Område | Före | Efter | Innehåll |
|---|---|---|---|
| geometri_problemlosning | 2 | 14 | Thales sats, randvinkelsatsen, tangent och radie, L-formad tomt, parallellogrammets diagonal, likbent triangel, fyrhörning, alternat- och sidovinklar, välj sats (korda, Pythagoras), rektangel i cirkel |
| koordinatgeometri_problemlosning | 5 | 17 | area och omkrets i rutnät, fjärde hörnet, höjd, punkt på axel, avstånd till axel, kvadrant, lodrät sträcka, lodrät bas, parallellogram, rät vinkel |
| avstandsformeln_mittpunktsformeln | 9 | 21 | Pythagoreiska taltripplar (5–12–13, 8–15–17, 9–12–15, 5–12–13 med drönare), √13, mittpunkt med decimaler, karta, formelval, cirkelns radie |
| bevis_likformighet | 11 | 23 | tredje vinkeln avgör, sidkvoter (ja/nej, segel), vertikalvinklar, motsvarande sida och vinkel, rätvinkliga och likbenta trianglar, längdskala |

Koordinatfigurerna har etiketter med vit bakgrund, och axelsiffror utelämnas där en punkt ligger på axeln. SVG-granskningen ger en kvarstående varning i 3.651 (DEGREE_LABEL_MISPLACED). Den är heuristisk, och figuren är granskad visuellt. Validatorn ger inga nya fynd efter att två texter skrevs om för att inte likna befintliga uppgifter. Testet ligger i `tools/ma2-niva1-geometri-omgang3-2026-10-22.test.js`.

## Kontroller

- **Variation:** inga två frågetexter är lika. Validatorn ger inga nya fynd, inte heller `VERY_SIMILAR_TEXT`.
- **Facit:** varje facit räknas om oberoende i `tools/ma2-niva1-geometri-2026-10-22.test.js`. Toleranserna är under 1 % av svaret.
- **Figurer:** granskade i webbläsaren och med `tools/granska-svg.js`, körd på de 87 nya figurerna. Efter justeringarna återstår bara INFO-fynd. Chrome avslutade ibland med felkod 21 när den vanliga Chrome var igång. Granskningsskriptet försöker då igen. Skuggfigurerna har parallella solstrålar, med samma förhållande mellan höjd och skugga. Den likbenta bisektrisuppgiften har en likbent figur.
- **Kunskapsgymmet:** alla 48 kort visas på nivå 1 utan KaTeX-fel eller överbredd vid 340 px. Svar med och utan enhet godtas, liksom 1/4 för 0,25 och rimligt avrundade decimalsvar.
- **Svarsenhet:** ingen `svarEnhet` är satt, så att mobilen behåller siffertangentbordet. Svar i en annan enhet än den efterfrågade, till exempel 60 cm i stället för 0,6 m, godkänns därför inte.

## Nästa steg

Fortsätt i Ma2 kapitel 3–4. Följande områden har fortfarande färre än 10 kort på nivå 1:

- geometri_problemlosning (2)
- tabeller_diagram (3)
- normalfordelning_digitala_verktyg (4)
- regressionsanalys_olika_modeller (8)
- bevis_likformighet (11)
- kvartiler_percentiler (16)

Därefter kommer Ma2 kapitel 1–2 och mato1, som har flest områden med under 10 kort.
