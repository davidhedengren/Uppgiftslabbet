# Ma2 kap 3 geometri, omgång S2: problemlösning och textuppgifter, 2026-10-25

Fortsättning på serien S (se `MA2_STATISTIK_S1_2026-10-25.md`). Läraren bad om fortsatt påfyllnad i Ma2 med mycket problemlösning och textuppgifter.

## Samordning med den andra Ma2-serien

En annan session fyller på Ma2 kap 1–2 i omgångarna 1, 2, 4 och 6 (ID 1.1000+ och 2.1000+). Serien S tar kap 3 och 4 med ID **3.2000+** och **4.2000+**. Nästa lediga ID:n i serien S är **3.2053** och **4.2061**.

## Jämförelse med nationella prov

Bara teman och uppgiftstyper som återkommer i Ma2-prov användes. Ingen provtext är kopierad eller omskriven, och inget kort är märkt som NP.

Typerna som inspirerade omgången:

- vardagsmätning med likformighet (skuggor, spegelmetoden och kartskala);
- kordasatsen i ett sammanhang (brovalv, gångar i en trädgård);
- area i koordinatsystem genom uppdelning;
- inskriven kvadrat;
- största area med en given staketlängd.

## Nya kort (53, 3.2000–3.2052)

| Område | Antal | Nivå 1/2/3 | Figurer | Innehåll |
|---|---:|---|---:|---|
| `pythagoras` | 9 | 2/4/3 | 5 | Stege, decimaltal, tv-skärm ur diagonal och format, vinkeltyp ur sidor, rymddiagonal, likbent triangel, ramp, kvadratens diagonal ur area, känna igen rätvinkliga trianglar |
| `likformighet` | 8 | 4/1/3 | 3 | Skuggor, kartskala och verklig area, motsvarande sida, areaskala, spegelmetoden, pris efter area, modellskala, sida ur areaförhållande |
| `topptriangel_transversal` | 6 | 1/3/2 | 4 | Topptriangelsatsen, transversalsatsen, skugga vid gatlampa, takstol, ekvation för okänd del, välja proportion |
| `kordasatsen_biskarningssatsen` | 6 | 1/3/2 | 5 | Givna delar, brovalvets radie, radie ur korda, andragradsekvation, bisektrissatsen, decimaltal |
| `randvinkel_medelpunkt` | 6 | 2/3/1 | 4 | Randvinkel och medelpunktsvinkel, halvcirkel, två randvinklar med algebra, fyrhörning i cirkel, via likbent triangel, katet i halvcirkel |
| `avstandsformeln_mittpunktsformeln` | 6 | 1/3/2 | 0 | Punkt lika långt från två punkter, triangeltyp, cirkelns medelpunkt och radie, ändpunkt ur mittpunkt, båtens sträcka, okänd koordinat |
| `koordinatgeometri_problemlosning` | 6 | 2/2/2 | 2 | Triangelns area, parallellogrammens fjärde hörn, triangel mellan linje och axlar, fyrhörning genom uppdelning, omkrets, okänd koordinat ur area |
| `geometri_problemlosning` | 6 | 1/2/3 | 6 | Inskriven kvadrat, tangerande cirklar, kvadrat minus kvartscirkel, största hage mot vägg, bisektris i likbent triangel, välja sats |

- **Nivåer:** 14 kort på nivå 1, 21 på nivå 2 och 18 på nivå 3. Nivå 3 har `niva` C, `poang` 0/1/0 och `arbetsinsats` 2.
- **Kursspår:** Pythagoras, avstånd/mittpunkt och koordinatgeometri har 2a, 2b och 2c. Övriga områden har 2b och 2c, som i områdena.
- **Figurer:** 29 figurer, ritade ur verkliga koordinater med likformig skalning, så att vinklar och proportioner stämmer.
  - Kordfigurerna räknar fram en radie som gör de givna delsträckorna exakta.
  - Avståndskorten saknar figur. Där är koordinaterna själva uppgiften, och en figur skulle visa svaret eller inte tillföra något.
- **Facitform:** Ma2 har numrerad steglista. Området `geometri_problemlosning` är ett undantag med löpande facit och figur på varje kort, enligt `tools/ma2-problemlosning.test.js`. De sex nya korten där följer områdets form, och 3.2050 och 3.2052 fick figurer av det skälet.
- **Verktyg:** miniräknare är tillåten på alla kort, eftersom roten ur och decimaldivision inte är det som prövas. GeoGebra nekas, eftersom ingen uppgift kräver digital ritning eller grafanalys.

## Kontroll

- **Facit:** alla 53 facit räknades om oberoende, och figurernas geometri kontrollerades mot de givna måtten.
  - 25 kort fick nya tal eller frågor, så att inget facit krockar med ett annat kort i området.
  - Det fanns också 6 krockar inom omgången, som löstes på samma sätt.
- **Validatorn:** inga nya fynd. 3.2011 och 3.2026 formulerades om efter `VERY_SIMILAR_TEXT`.
- **SVG-granskaren:** inga verkliga fel kvar. Det som återstår är heuristiska fynd för vinkelbågar med ”?” och rutinfynd för etiketter.
  - Kordfigurerna fick jämnare delningar, så att skärningspunkten inte hamnar vid randen.
  - Etiketter i trianglar placerades på en uttalad sida.
  - Två figurer fick större marginal.
- **Självrättning i Kunskapsgymmet:** alla kort testades med 207 svar.
  - Fem kort med exakta decimalfacit anger nu exakthet i frågan: 3.2017, 3.2023, 3.2027, 3.2028 och 3.2043. Annars godtar appen ett avrundat svar.
- **Mobil (375 px):** inga överskridningar i bankens figurer eller text. Fyndet vid 3.2039 var appens egen `hide-tail`-ikon, inte bankinnehåll.
- **Test:**
  - `tools/ma2-geometri-s2-2026-10-25.test.js` ger 5/5.
  - `tools/ma2-problemlosning.test.js` har uppdaterat antal, 48 kort i `geometri_problemlosning`.
  - Alla `tools/ma2-*.test.js` går igenom.
