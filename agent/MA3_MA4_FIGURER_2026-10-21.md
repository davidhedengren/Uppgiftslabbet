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
