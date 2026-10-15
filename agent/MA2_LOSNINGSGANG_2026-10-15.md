# Ma2: lösningsgång även på delkort · 2026-10-15

## Avgränsning och orsak

Bilden avser Ma2 2.130 b, 6x²+x−2=0. Huvudfacit innehöll uträkningen men delkortets eget s innehöll endast rötterna. Konsumenten använder del.s före t.s, så formatering av huvudfacit löste inte bristen på delkortet.

Alla sju banker inventerades efter tomma och mycket korta facit. Träffarna är kandidater, inte automatiskt fel: ett kort avläsningsfacit kan vara tillräckligt, och ett saknat del.s kan ersättas av huvudfacit. Den manuella genomgången här avser samtliga 80 uppgifter i Ma2:s områden enkla_andragradsekvationer, nollproduktmetoden och losningsformel_andragrad. Övriga bankträffar är inte fullständigt granskade eller rättade i denna omgång.

## Åtgärdade — 12 uppgifter

| ID | Delar | Rättning |
|---|---|---|
| 2.10 | a | Kortfacit kompletterat med förklaring och beräkning. |
| 2.16 | a, b | Kortfacit kompletterat med förklaring och beräkning. |
| 2.41 | a | Kortfacit kompletterat med förklaring och beräkning. |
| 2.50 | a | Kortfacit kompletterat med förklaring och beräkning. |
| 2.89 | a, b, c | Kortfacit kompletterat med förklaring och beräkning. |
| 2.122 | a, b | Kortfacit kompletterat med förklaring och beräkning. |
| 2.130 | a, b, c | Alla tre delkort visar normalisering, p/q, insättning och exakta rötter. Huvudfacit omstrukturerat så att varje dels hela lösning hålls ihop. |
| 2.133 | a, b, c | Kortfacit kompletterat med förklaring och beräkning. |
| 2.134 | a, b | Nollproduktmetoden visas för varje faktor. Den missvisande skrivningen −4{,}1 i b ersatt med separata rötter −4, 1 och 3/2; rättningsmetadata var redan korrekt. |
| 2.171 | a, b, c | Kortfacit kompletterat med förklaring och beräkning. |
| 2.521 | a, b, c | Tre egna delkortsfacit tillagda; korten föll tidigare tillbaka på huvudfacit och avslöjade även andra delars svar. |
| 2.608 | Heluppgift | Enbart x=±9 kompletterat med varför båda tecknen behövs. |

Totalt ändrades 32 lösningsfält: 24 delkortsfacit och åtta huvudfacit. Nio pq-kort har fullständiga, uppgiftsspecifika beräkningar. Mellanleden visas på egna rader för mobilvisning. Ingen generell mall har lagts till i elevgränssnittet eller alla lösningar automatiskt.

## Granskad — inget motsvarande fel, 68 uppgifter

2.01, 2.02, 2.03, 2.04, 2.09, 2.42, 2.43, 2.49, 2.57, 2.81, 2.82, 2.96, 2.99, 2.121, 2.123, 2.124, 2.125, 2.126, 2.127, 2.128, 2.129, 2.132, 2.136, 2.138, 2.151, 2.152, 2.160, 2.169, 2.170, 2.256, 2.257, 2.269, 2.270, 2.481, 2.482, 2.483, 2.484, 2.519, 2.520, 2.522, 2.523, 2.524, 2.531, 2.532, 2.533, 2.551, 2.562, 2.563, 2.609, 2.701, 2.727, 2.728, 2.729, 2.730, 2.731, 2.732, 2.741, 2.742, 2.743, 2.744, 2.745, 2.746, 2.749, 2.750, 2.760, 2.761, 2.762, 2.766

Bedömningen gäller om lösningsgång finns och räcker för denna typ av uppgift, inte en ny fullständig klassificering av alla dessa uppgifter. Korta facit med relevant mellanled eller en tillräcklig förklaring har behållits, exempelvis 2.49 (division före rötter), 2.121/2.123/2.256 (faktorisering före nollprodukt), 2.532/2.562 (varför båda rötterna), 2.484 (varför ingen reell lösning).

## Matematik och metadata

För samtliga 32 kort inom de 12 ändrade föräldrarna har rötterna räknats om exakt med oberoende algebraiska modeller och Sympy. 2.122 b verifierades genom insättning x=0. Alla lagrade lösningsmängder stämmer; rättSvar, toleranser, ordning och självrättning är oförändrade. För pq-korten har även normaliseringen, p/q och diskriminanten kontrollerats. Bildens ekvation ger p=1/6, q=−1/3, x=−1/12 ±7/12, alltså 1/2 och −2/3.

Alla berörda uppgifter och deras delkort har miniräknare=false och geogebra=false. Det är rimligt här: exakt algebra, faktorval, pq-formel och små kvadrater/bråk prövas. Inga stora numeriska beräkningar behövs, och graf-/CAS-lösning skulle gå förbi den efterfrågade metoden. Alla delkort ärver förälderns verktygsval. Nivåer och övrig metadata bevaras. En separat figur tillför inget till dessa symboliska beräkningar.

## Verifiering

- 379/379 tester i Uppgiftslabbet och 174/174 i Kunskapsgymmet godkända. Den generella SVG-sviten kördes inte; inga figurer har ändrats.
- Kunskapsgymmets verkliga kortexpansion, svarsfält och Lösning testade på 390 och 1280 px: 64 kortvisningar och 124 rättningskontroller, inklusive omkastad ordning på rötterna. Inga KaTeX-fel, råa LaTeX-kommandon, överflödande beräkningsrader eller delkort som lånar hela huvudfacit i denna grupp.
- Skärmbilder av bildens uppgift med full lösning granskade på mobil och dator.
- Bankvalidator: 2 190 uppgifter; fynd minskar från 260 till 257, eftersom tre saknade delkortsfacit i 2.521 rättas. Inga nya fynd. Övriga 257 fynd ligger utanför denna avgränsning.
- Strukturerad diff: endast s och spelDelar[i].s i exakt dessa 12 uppgifter ändras. Antal, ID:n, frågor, svar och övrig metadata är identiska.
- Bankkopiorna var identiska före synkronisering och är identiska efteråt. Båda apparna får ny cacheversion.

## Rapportkommentar

Ma2 2.130 b: ”Tack! Delkortet visar nu hela lösningen: division med 6, p och q, insättning i pq-formeln och förenkling till 1/2 och −2/3. Samma brist har rättats i ytterligare uppgifter.”

Resultatet återges direkt i chatten med tydlig skillnad mellan Åtgärdad och Granskad — inget motsvarande fel; denna fil är internt granskningsspår.
