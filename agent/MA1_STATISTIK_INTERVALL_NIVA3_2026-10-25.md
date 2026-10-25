# Ma1: nivå 3 i urval, felkällor, korrelation och intervall, 2026-10-25

Läraren bad om fler kort i de områden som har minst på nivå 3. Enligt `NIVAINVENTERING_2026-10-25.md` var Ma1:s statistikresonemang tunnast bland de spelbara korten:

- Stickprov och urvalsmetoder: 1 nivå 3-kort (5.571).
- Signifikans och felkällor: 1 (5.282).
- Korrelation och kausalitet: 3.
- Intervall: 2.

Övriga nivå 3-uppgifter i dessa områden har `spel:false`.

## Nya kort: 26 st, alla på nivå 3 med C-poäng och arbetsinsats 2

| Område | ID | Innehåll |
|---|---|---|
| urvalsmetoder (7) | 5.665–5.671 | Stratifierat urval baklänges. Bortfall som ger min- och maxandel. Systematiskt urval med startnummer. Viktning efter tätort och landsbygd. Två urvalsplaner jämförda i en tabell (flerval). Bortfall som tycker annorlunda. Minsta urval så att den minsta gruppen får minst 12. |
| signifikans (6) | 5.672–5.677 | När två osäkerhetsintervall inte överlappar. Hur många fler som måste tillfrågas (felmarginalen ∝ 1/√n). Systematiskt fel i en våg (tabell). Simulering av ett mynt: 58 av 1 000 serier (flerval). Osäkerhetsintervall omräknat till antal personer. Olika mätmetoder i två klasser (flerval). |
| korrelation (7) | 5.678–5.684 | Tre punktmoln paras ihop med r. Simpsons paradox för två körskolor (tabell). Självvald försöksgrupp med lottning som förbättring. Byte av enheter ändrar inte r. Vad r = −0,9 säger och inte säger. Två årskurser i samma punktdiagram, där åldern är den bakomliggande variabeln. Alla punkter på en fallande linje, r = −1. |
| intervall (6) | 1.1551–1.1556 | Villkor i °C omräknat till °F. Taxiresa med två villkor. Tolerans före och efter kylning. Intervall avläst ur en graf med ifylld och ofylld ändpunkt. Union av två intervall på tallinjer. Antal heltal som uppfyller två villkor. |

Kurstaggar:

- Kap 5 har 1a, 1b och 1c.
- Intervall har 1b och 1c, som befintliga intervallkort.

Svarsformerna är numeriskt, flera delar, flerval och `intervall`. Korrekt flervalsalternativ står aldrig först. Det finns fyra figurer, med punktmoln, grupperat punktdiagram, funktionsgraf med definitionsmängd och tallinjer, och fyra tabeller.

Verktyg:

- Miniräknare är tillåten där beräkningen inte är det som prövas.
- Miniräknare är avstängd på grafavläsningen, tallinjen, heltalsräkningen och r = −1.
- GeoGebra används inte.

## Kontroll

- Facit räknades separat i byggskriptet och räknas om igen i testet. Testet kontrollerar bland annat:
  - binomialsannolikheten 0,0577 bakom simuleringen;
  - korrelationskoefficienterna för de ritade punktmolnen: 0,97, −0,75 och 0,02;
  - att varje årskurs i det grupperade diagrammet saknar trend, men att alla tillsammans har r > 0,8.
- Inget nytt kort har samma facit som ett annat kort i området.
- Validatorn för Ma1 ger 201 fynd både före och efter ändringen, alltså inga nya.
- SVG-granskaren ger 0 fynd efter att x-etiketten i 1.1554 flyttats bort från rutnätet.
- `tools/ma1-statistik-intervall-niva3-2026-10-25.test.js` passerar 2 av 2.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 44 svar, bland annat:
  - procent med och utan %-tecken;
  - tusentalsmellanrum;
  - ≤ och <=;
  - decimalkomma i intervall;
  - fel ändpunkt och fel ordning.
- Alla 44 svar gav väntat resultat. Undantaget är att 38 godkänns för 37,5, vilket följer avrundningsregeln eftersom frågan inte anger precision.
