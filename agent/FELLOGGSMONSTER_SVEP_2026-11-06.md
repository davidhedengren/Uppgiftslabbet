# Svep efter felloggens återkommande mönster, 6 november 2026

## Uppdrag

Användaren vill att banken förbättras genom en sökning efter fel som liknar dem som har funnits i felloggen tidigare.

## Vilka mönster är vanligast?

`agent/FELRAPPORTER_*.md` har 93 rapporter med 1 134 tabellrader. Raderna har sorterats efter nyckelord:

| Mönster | Rader |
|---|---|
| Ett rätt svar underkänns av rättningen | 278 |
| Avrundning och precision | 212 |
| Enhet | 197 |
| Figur | 151 |
| Nivå | 124 |
| Delkort | 79 |
| Otydlig fråga | 51 |
| Miniräknare och GeoGebra | 50 |

De tre vanligaste mönstren går att pröva maskinellt i Kunskapsgymmets riktiga rättning.

## 1. Avrundade talsvar: `tools/kg-avrundningssvep.cjs`

Svepet kör `delSvarRatt` på alla 14 564 kort med ett talsvar i de sju bankerna. Det provar facit med svarets enhet, facit avrundat till frågans antal decimaler eller värdesiffror och facit med tre värdesiffror när frågan inte anger någon precision. Svar som avviker med 10 % ska underkännas. Kort med `svarVardesiffror` provas med facit avrundat till det antalet.

**Fynd och åtgärd:**

- **Systemfel i Kunskapsgymmet.** Regeln om fri avrundning (användarbeslut 2026-10-19) gällde bara kort med `svarFormat: "numeriskt"`. I bankerna finns 169 kort med ett decimalfacit utan `svarFormat`. 111 av dem anger ingen precision. Där underkändes korrekt avrundade svar, till exempel 1,13 mot 1,134 i Ma1 3.188a, 6,08 mot 6,075 i Ma1 7.27a och 589 N mot 589,2 N i Fy1 4.504.
  - Åtgärd i `index.html`: ett talfacit utan format behandlas som numeriskt i `friAvrundningRatt`.
  - De 58 kort som kräver en viss precision eller exakt form påverkas inte, eftersom regeln redan undantar dem.
  - Självtester i `KG_TEST_MA4_SVAR` täcker korrekt och felaktig avrundning och angiven precision.
- **Kvarvarande fynd är artefakter i provet.**
  - JavaScripts binära avrundning ger 7,54 för 7,545, men den korrekta avrundningen 7,55 godtas.
  - Frågor som handlar om avrundning, till exempel ”Ett tal avrundas till två decimaler och blir 2,76 …”, kräver exakt svar.
  - Frågor med ”Skriv som ett decimaltal” anger ingen precision.
- **Generös rättning, ingen ändring.** 79 kort godtar facit · 1,1. Det gäller överslag, avläsning i diagram och astronomi med uttrycklig tolerans, och Fy1-kort med en värdesiffra. I övriga fall är 1,1 · facit en korrekt grov avrundning, till exempel 0,02 för 0,0182.

## 2. Svarsenheter

- **Sökning:** 3 308 kort har en svarsenhet som inte är en naturlig SI-enhet. I ungefär 85 fysikkort står enheten varken i frågan eller i inledningen, till exempel mA, nm, µT, kN och THz.
- **Prov i rättningen:** Kunskapsgymmet godtar samma svar i SI-enhet när enheten skrivs ut, till exempel 0,018 A för 18 mA.
- **Ingen ändring:** Kunskapsgymmet skriver ”Svara i mA” ovanför varje svarsruta som har en enhet (`svarsenhet-*`). Eleven ser alltså enheten.
- **Kvar att besluta:** i Uppgiftslabbets egen visning saknas enheten i dessa frågor. Om användaren vill kan de få ”(Svara i mA.)” efter frågan, men det ska i så fall granskas uppgift för uppgift.
- **Omvandlingsuppgifter i Ma1** ska underkänna svar i fel enhet, och gör det.

## 3. Miniräknare

- **Sökning:** 6 818 kort har `miniräknare: false`. Fynden är kort med decimalfacit, trigonometri med vinklar som inte är standardvinklar eller krav på flera decimaler.
- **Ma1:** decimalsystemet och omvandlingar ska räknas för hand.
- **Ma5:** linjär approximation och Eulers metod ska räknas för hand.
- **Ma3c 4.574** ger cos 40° ≈ 0,766.
- **Ma4 1.672, 2.580, 3.521, 2.562 och 4.582** frågar efter svaret ”exakt eller med tre decimaler”. Rättningen godtar 2√2, 13/16 och 4/3. Inga ändringar behövs.
