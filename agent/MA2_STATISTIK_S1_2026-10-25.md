# Ma2 kap 4 statistik, omgång S1: problemlösning och textuppgifter, 2026-10-25

Läraren bad om fortsatt påfyllnad i Ma2, gärna med mycket problemlösning och textuppgifter. Gamla nationella prov skulle användas som jämförelse.

## Samordning med den andra Ma2-serien

En annan session fyller samtidigt på Ma2 kap 1–2 i omgångarna 1, 2, 4 och 6 (ID 1.1000+ och 2.1000+), se `MA2_OMGANG_*.md`. Den här serien, S1 och framåt, tar därför **kap 3 (geometri) och kap 4 (statistik)**. Den använder ID **3.2000+** och **4.2000+** för att undvika krockar. Den andra serien bör hålla sig till sina ID-intervall, och kap 3–4 bör inte dubbleras utan att läsa dessa loggar.

## Jämförelse med nationella prov

Jag läste Ma2c VT15 från Umeå universitets officiella arkiv (kallregistret i `nationella-prov/`), med pdf.js lokalt. Bara teman och uppgiftstyper användes, inte provtexter. Ingen uppgift är en omskrivning av en provuppgift, och ingen är märkt som NP.

Typerna som inspirerade denna omgång:

- okända värden i en ordnad lista som ska stämma med ett lådagram (4.2036);
- antal i ett intervall ur normalfördelningens andelar (4.2042, 4.2044, 4.2045);
- procentuell förändring med vilseledande diagram (4.2001);
- modeller och rimlighet långt utanför mätvärdena (4.2059, 4.2060).

Övriga Ma2-prov i arkivet var över 10 MB och kunde inte hämtas med verktygen här.

## Nya kort (61, 4.2000–4.2060)

| Område | Antal | Nivå 1/2/3 | Innehåll |
|---|---:|---|---|
| `tabeller_diagram` | 12 | 4/6/2 | Stapeldiagram, avkortad y-axel, korstabell, cirkeldiagram, linjediagram, största procentuella ökning, procent av olika stora grupper, val av diagramtyp, total andel ur två grupper, histogram, proportionell stapelhöjd, procent och procentenheter |
| `lagesmatt` | 11 | 3/6/2 | Summa ur medelvärde, borttaget värde, viktat medelvärde, typvärde och medelvärde ur frekvenstabell, okänt värde ur median, extremvärde (flerval), rättat medelvärde, krav på nästa resultat, åldersbyte i ett lag |
| `kvartiler_percentiler` | 9 | 3/4/2 | Nedre kvartil, skalat kvartilavstånd, percentiler, ordningsnummer för övre kvartilen, kvartilavstånd när största värdet ändras |
| `ladagram` | 10 | 3/5/2 | Avläsning, mittersta hälften, jämföra två lådagram (även flera rätta påståenden), x och y ur lådagram, femtalssammanfattning, välja datamaterial till lådagram |
| `normalfordelat_material` | 10 | 2/6/2 | Antal inom μ ± σ, mittersta 95 %, svansar, σ ur andelar, osymmetriska intervall, känna igen normalfördelning, jämföra resultat i standardavvikelser, största tillåtna σ |
| `korrelation_koefficient` | 4 | 2/2/0 | r ur punktdiagram, korrelation och orsak, tolkning av r |
| `linjar_regression` | 5 | 2/2/1 | Prognos, lutningens betydelse, avvikelse från linjen, lösa ut x, modellen långt utanför mätvärdena |

- **Nivåer:** 19 kort på nivå 1, 31 på nivå 2 och 11 på nivå 3. Nivå 3 har `niva` C och `poang` 0/1/0.
- **Kursspår:** korrelation och regression har 2b och 2c, övriga områden 2a, 2b och 2c, som i områdena.
- **Figurer:** 15 figurer, alla nya diagramtyper i samma stil som tidigare: stapeldiagram, histogram, lådagram, normalkurvor och punktdiagram.
- **Delmoment:** nytt delmoment ”Procent och jämförelser i tabeller och diagram” med 8 kort.
- **Ingen kopierad kvartilmetod:** kvartilerna räknas, som i resten av banken, med ett jämnt antal värden, så att metoden inte blir tvetydig.
- **Normalfördelning:** konventionen är 34,1/13,6/2,1/0,1 %. Facit till 4.2049 räknar 50 + 34,1 + 13,6 = 97,7 % direkt, i stället för 100 − 2,2.
- **Verktyg:** miniräknare är tillåten och GeoGebra nekas. Inget kort kräver statistikfunktion på rådata.

## Kontroll

- **Facit:** alla 61 facit räknades om oberoende, bland annat kvartiler med bankens metod och normalandelar. 15 kort fick nya tal eller frågor, så att inget facit krockar med ett annat kort i området.
- **Validatorn:** 224 fynd i ma2 före och efter.
- **SVG-granskaren** kördes via appens webbläsare och gav 4 rutinfynd för etiketter på 17 SVG:er.
  - Rutnätet i tre lådagram tätades, så att alla efterfrågade värden ligger på en linje.
  - Normalkurvan i 4.2047 fick etiketterna μ − σ … μ + 3σ.
- **Självrättning i Kunskapsgymmet:** alla 61 kort testades med 221 svar.
  - Appen godtar ett korrekt avrundat svar när frågan inte anger precision. Det gjorde att 2 godtogs för 1,85 och 9 för 9,25.
  - Sex kort med exakta decimalfacit anger därför precisionen i frågan (4.2010, 4.2016, 4.2017, 4.2019, 4.2049, 4.2058).
  - Enheterna %, cm, g, kr, min, s, mm, år och °C fungerar.
- **Mobil (375 px):** ingen överskridning av sidbredden och inga KaTeX-fel, med och utan facit.
- **Test:** `tools/ma2-statistik-s1-2026-10-25.test.js` ger 6/6, och alla övriga `tools/ma2-*.test.js` går igenom.
