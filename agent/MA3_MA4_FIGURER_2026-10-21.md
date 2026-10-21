# Ma4 tangenskurvan och Ma3c deriverbarhet, 2026-10-21

## Ämnesplan

Båda områdena är kontrollerade mot Gy25-planen för matematik – fortsättning (SKOLFS 2024:186):

- Nivå 2c (Ma4) innehåller "Egenskaper hos trigonometriska funktioner, däribland period, amplitud och fasförskjutning" samt tangensfunktionen.
- Nivå 1c (Ma3c) innehåller "Villkor för deriverbarhet".

## Ma4 Kurvan y = tan x (2.605–2.612)

Området hade 12 uppgifter, alla algebraiska och utan figur. Det har fått åtta nya
med tangensgrafer, där kurvan bryts vid asymptoterna och asymptoterna är streckade.
Det nya delmomentet heter "Tolka och använda tangenskurvan".

| ID | Nivå | Innehåll | Svar |
|---|---|---|---|
| 2.605 | 1 | Nollställen ur grafen | 2 |
| 2.606 | 2 | b ur avståndet mellan asymptoter | 2 |
| 2.607 | 2 | a ur punkten (45°, 3) | 3 |
| 2.608 | 3 | tan x = 2 med graf och räknare | 63,4° och 243,4° |
| 2.609 | 3 | Asymptot efter förskjutning | 120° |
| 2.610 | 2 | Egenskaper (flera rätt) | Period 180°, växande, alla reella tal |
| 2.611 | 3 | Strålkastare, h = 5 tan v | 63,4° |
| 2.612 | 4 | a och b ur asymptot och punkt | b = 2, a ≈ 3,46 |

## Ma3c Deriverbarhet (3.1157–3.1164)

Området hade 15 uppgifter, men bara 3.1143 och 3.1149 handlar om deriverbarhet.
De övriga 13 gäller extrempunkter och derivatans tecken (`omrTidigare`:
`grafanalys_derivata`). De ligger kvar, men användaren tillfrågas om de ska
flyttas till "Vad säger derivatan om funktionens graf?".

Åtta nya uppgifter med grafer:

| ID | Nivå | Innehåll | Svar |
|---|---|---|---|
| 3.1157 | 1 | Hörn i \|x − 2\| + 1 | x = 2 |
| 3.1158 | 2 | Hopp, ofylld och ifylld ändpunkt | Inte kontinuerlig och därför inte deriverbar |
| 3.1159 | 2 | Punkter A–D, flera rätt | B (hörn) och D (hopp) |
| 3.1160 | 2 | \|x\|: kontinuerlig men inte deriverbar | Nej, lutningen är −1 och 1 |
| 3.1161 | 3 | x² och 4x − 4 i x = 2 | Deriverbar |
| 3.1162 | 3 | Vänster- och högerlutning | 2 och 3 |
| 3.1163 | 4 | Parametrar | a = 2, b = −8 |
| 3.1164 | 4 | ∛x, lodrät tangent | Inte deriverbar |

3.1163 saknar figur, eftersom figuren skulle visa svaret.

## Verifiering

- Alla 16 uppgifter rättas korrekt i Kunskapsgymmet (mato2/2c och mato1/1c), med rätt och med fel svar.
- Gradsvar godtas med och utan °.
- Alla figurer är granskade på skärmbild.
- Test: `tools/ma3-ma4-figurer-2026-10-21.test.js`.

## Flyttade uppgifter (användarbeslut samma dag)

Användaren godkände att de 13 extrempunktsuppgifterna flyttas från `deriverbarhet`.
Jag lade dem i de områden som motsvarar innehållet, i stället för att lägga alla i
"Vad säger derivatan om funktionens graf?":

- Extrempunkter och terrasspunkter:
  - Teckenstudium: 3.633, 3.634, 3.635, 3.639 och 3.640.
  - Terrasspunkter: 3.637, 3.638 och 2.278.
  - Bestämma extrempunkter: 2.673.
- Vad säger derivatan om funktionens graf? (Växande och avtagande): 3.636 och 2.678.
- Andraderivatan och funktionens graf: 2.638 och 2.639.

Bara `omr` och `familj` ändrades. `deriverbarhet` och `Deriverbarhet` lades till i
`omrTidigare` och `familjTidigare`, och övriga fält och filens format är oförändrade.

Kunskapsgymmets `migreraFamiljer()` flyttar inget områdesvärde, eftersom 9 av 213
uppgifter är under tröskeln på 20 %. Elevernas värde för Deriverbarhet ligger
därför kvar, och historiken räknas om per uppgift.

Deriverbarhet innehåller nu 3.1143, 3.1149 och 3.1157–3.1164, alltså 10 uppgifter
i spår 1c. Genomgångarna för deriverbarhet (spets, parametrar) passar fortfarande.
