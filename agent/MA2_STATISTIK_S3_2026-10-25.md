# Ma2 kap 4 statistik, omgång S3: textuppgifter och problemlösning, 2026-10-25

Fortsättning på serien S (se `MA2_STATISTIK_S1_2026-10-25.md` och `MA2_GEOMETRI_S2_2026-10-25.md`). Omgången fyller på de statistikområden som efter S1 hade minst på nivå 1–2. Nästa lediga ID:n i serien S är **3.2053** och **4.2112**.

## Nya kort (51, 4.2061–4.2111)

| Område | Antal | Nivå 1/2/3 | Figurer | Innehåll |
|---|---:|---|---:|---|
| `tabeller_diagram` | 13 | 4/7/2 | 3 | Skillnad i tabell, tomma platser ur stapeldiagram, andel ur frekvenstabell, pristabell, andel av en delgrupp i korstabell, ökning ur linjediagram, prisindex, fyrfältstabell med överlapp, andel ur histogram, antal ur relativ frekvens, samma antal ur olika andelar, baklänges genom två ökningar, andel av en period |
| `kvartiler_percentiler` | 6 | 3/2/1 | 0 | Nedre kvartil, tolka percentil, antal över percentil, övre kvartil ur frekvenstabell, jämföra kvartilavstånd, okänt värde ur kvartilavstånd |
| `ladagram` | 6 | 1/3/2 | 5 | Variationsbredd, antal över övre kvartilen, två lådagram (flera rätt), femtalssammanfattning, vilka mått som ändras, andel över den andra gruppens median |
| `normalfordelning_digitala_verktyg` | 10 | 3/4/3 | 5 | Andel i intervall, över och under, antal ägg i storleksklass, gräns för de 5 % lättaste, kassation utanför tolerans, jämföra två maskiner, minsta μ, största σ, förväntat antal |
| `linjar_regression` | 10 | 4/4/2 | 1 | Modellvärde, tolka m, k och prognos med GeoGebra, när två modeller är lika, lösa ut x, avläsa linjen, byta tidsenhet, när modellen når ett värde, punkt ovanför linjen |
| `korrelation_koefficient` | 6 | 2/3/1 | 3 | r ur diagram, r med GeoGebra, r vid enhetsbyte, negativ korrelation, avvikande punkt, para ihop två diagram |

- **Nivåer:** 17 kort på nivå 1, 23 på nivå 2 och 11 på nivå 3. Nivå 3 har `niva` C och `poang` 0/1/0.
- **Kursspår:** korrelation och regression har 2b och 2c. Övriga områden har 2a, 2b och 2c.
- **Verktyg:**
  - Miniräknare är tillåten på alla kort.
  - GeoGebra är tillåtet på de 14 kort som uttryckligen ber om det:
    - alla tio normalfördelningskort (sannolikhetskalkylatorn);
    - tre regressionskort;
    - ett kort där r räknas ur data.
  - Övriga kort nekar GeoGebra. Där prövas avläsning, tolkning eller en kort beräkning.
  - Regressionsdata har `x` som år efter start, så att `m` blir tolkningsbart.
- **Figurer:** 17 figurer. Kvartilkorten har listor och tabeller i stället för figur, eftersom det är talen som ska ordnas.

## Kontroll

- **Facit:** alla facit räknades om oberoende.
  - Normalfördelningen räknades med Simpsons regel på täthetsfunktionen. Generatorn använder en egen erf-funktion.
  - Regression och r räknades med minsta kvadratmetoden.
  - Kvartiler räknades med bankens metod (medianer av två lika stora halvor).
  - Tio facit krockade med äldre kort i samma område och fick nya tal.
  - Flervalsdiagrammens verkliga r-värden kontrollerades: 0,74 i 4.2106, −0,997 och 0,25 i 4.2111, och 0,68 → 0,997 utan P i 4.2110.
- **Validatorn:** inga fynd för 4.2061–4.2111. 4.2106 fick ett eget sammanhang efter `EXACT_TEXT_DUPLICATE` mot 4.2052.
- **SVG-granskaren:** 18 figurer och 15 rutinfynd, där etiketter korsar rutnätslinjer. Etiketterna 62 och 63 i äggfiguren 4.2089 överlappade, så etiketten för μ togs bort.
- **Självrättning i Kunskapsgymmet:** 125 kontroller i appen.
  - Rätt svar godtas, med och utan enhet (%, kr, min, cm, g, kWh, veckor och år).
  - Fel svar avvisas, utom där felet ligger inom avsedd tolerans: ±3 ägg i 4.2089 och ±1 elev i 4.2095.
  - Flervalskorten godtar rätt kombination och avvisar fel val.
- **Mobil (375 px):** ingen överskridning och inga KaTeX-fel, varken i frågor eller facit.
- **Test:**
  - `tools/ma2-statistik-s3-2026-10-25.test.js` ger 5/5.
  - Alla `tools/ma2-*.test.js` går igenom.
  - Tre andra tester faller redan på grund av Fy1-banken `uppgifter.js`, inte Ma2: `felrapporter-2026-10-16`, `svg-bredd-2026-10-21` och `granska-svg` test 41 om kraftbilden i 4.133. Det är inte åtgärdat här.
