# Matf1: derivatrepetition – manuell områdesgranskning 2026-10-26

**27 huvuduppgifter granskade och förbättrade, varav 23 är spelbara och fyra endast finns i lärarbanken. Granskad – inget fel: inga.** De lagrade matematiska slutsvaren var korrekta. Rättningen, förklaringarna, en figur och flera nivåer behövde däremot förbättras. Detta är ett helt område, inte ett färdigt manuellt kvalitetsintyg för hela banken.

## Fynd och beslut

- Alla 27 facit och ledtrådar är manuellt genomgångna och har uppgiftsspecifika rubriker, beräkningar och slutsvar. Exempel på samma brist: 3.330–3.337 saknade antingen tydliga steg eller viktiga mellanled. Ingen rubrik har genererats ur första meningen i en mall.
- 3.29 hade en irrelevant ledtråd om absolutbelopp. Frågan preciserar nu x-värden där tangenten är horisontell, i stället för det tvetydiga ”kritiska punkterna”. Lösningen skiljer var derivatan är positiv från de största intervall där funktionen är växande; ändpunkter med derivatan noll kan ingå. Jämfört med 3.207/212/332/334/339.
- Maximum/minimum motiveras, inte bara genom att sätta derivatan till noll. 3.52/83/332/334/336/339 har kontrollerats med tecken, definitionsmängd eller en undre gräns som nås. 3.83:s gamla bild visade redan den optimala rektangeln med bredd 4 och höjd 8. Den nya bilden använder x=1,25 som illustrativt värde utan att ange det i frågan. 3.52 får en motsvarande figur. Dessa figurer ger ingen numerisk lösning. Befintliga 3.344/345 är geometriskt och visuellt kontrollerade och oförändrade. Rena symboliska derivatuppgifter behöver ingen dekorativ figur.
- 3.207/212/333 har uttrycklig oordnad rotmängd; 3.287 behåller sin oordnade mängd. 3.346 behåller däremot ordnade, namngivna fält för produkt och kvot. Omvänd ordning och felaktigt dubblerad rot testas.
- 3.209 använder tolerans 0,0005 för tre decimaler, i stället för 0,002 som även accepterade 1,605 och 1,607. 3.287:s två irrationella rötter har samma halvstegstolerans. 3.338 hade redan korrekt tolerans och behåller den. 3.227 använder fullprecisionsreferens och konsumentens fria avrundning i stället för bred tolerans.
- 3.207 och 3.52 kräver inte exakt form. De har därför numeriskt format med fullprecisionsreferenser som accepterar både rotuttryck och korrekta avrundningar. 3.333 kräver uttryckligen exakt svar och behåller uttrycksformat. 3.341:s maskinreferens är nu 3e, inte det redan avrundade talet 8,15. Ingen global rättningsregel ändras. Jämförelser omfattar 3.207/209/227/52/287/338/341.
- 3.287:s text sade både ”bekräfta exakt” och ”svara exakt eller med tre decimaler”. Den motsägelsen är borttagen; lösningen visar fortfarande hela den exakta faktoriseringen. Digitala verktyg från beslutet 2026-10-14 behålls.
- 3.74 visar nu hur nära noll det föreslagna värdet ligger samt ett närliggande teckenbyte. Kontrollen mellan enbart 1 och 2 var för grov för att särskilt stödja 1,521.

## Nivåer och verktyg

- Direkt digital ekvationslösning 3.209/227/338 blir **E/nivå 2**. Högre nivå ska inte komma enbart av att ekvationen saknar en enkel algebraisk lösning när digital metod uttryckligen tillåts.
- 3.29, 3.340 och 3.343 blir **nivå 2**: ekvation och tecken, alternativt kedjeregel plus insättning, är flera beroende led. 3.83 blir **C/nivå 3**, jämförbar med 3.52 och med tydligt uppdelad väg till modellen och maximum.
- 3.344/345 behåller **nivå 3** och får C-metadata: eleven kombinerar grafavläsning med en sammansatt funktion. 3.346 blir **E/nivå 2**: två separata rutinregler med givna tabellvärden är mer arbete men inte automatiskt C. Övriga nivåer behålls efter manuell bedömning.
- Miniräknare är tillåten i alla 27 uppgifter. Nytillåten i 3.207/212/340/342/343/344/345/346: vanlig räknare tar inte bort det som prövas och banken ska inte testa handräkningsförmåga.
- GeoGebra är tillåtet i 3.209/227/287/338. I övriga uppgifter krävs symbolisk metod, tolkning eller redan given graf/tabell. 3.74 behöver bara vanlig räknare för insättningskontrollen av ett redan givet närmevärde och får därför GeoGebra avstängt. Detta skiljer uppgiften från att själv hitta roten digitalt. GeoGebra innebär alltid miniräknare.
- 3.29/54/74/83 behåller `spel:false` och manuell bedömning. Ingen ny självrättning av fria resonemang införs. Inga delkort finns i detta område.

## Alla granskade ID:n och föreslagna kommentarer

Samtliga är **åtgärdade**, inklusive pedagogiska förtydliganden av redan korrekta svar. Ingen rapportstatus har ändrats i Supabase och ingen kommentar har skickats.

| ID | Status | Kommentar att använda |
|---|---|---|
| #3.207 | Åtgärdad | Facit visar derivatan och båda rötterna. Svaren godtas i valfri ordning, som exakta rotuttryck eller korrekt avrundade decimaltal eftersom frågan inte kräver exakt form. |
| #3.209 | Åtgärdad | Facit visar hur skärningen bestäms i GeoGebra och varför lösningen är unik. Tre decimaler ger 1,606; angränsande felavrundningar godtas inte längre. Nivå 2. |
| #3.212 | Åtgärdad | Facit visar hela ekvationen för horisontell tangent. −2 och 2 godtas i valfri ordning. |
| #3.52 | Åtgärdad | En figur har lagts till. Facit visar både areamodellen och varför derivatans tecken ger ett globalt maximum. Både 12√3 och korrekt avrundade decimaler godtas. |
| #3.29 | Åtgärdad | Den irrelevanta ledtråden om absolutbelopp är ersatt. Frågan preciserar x-värden för horisontell tangent. Facit förklarar derivatans tecken och hur ändpunkterna kan ingå i växande intervall. Nivå 2. |
| #3.227 | Åtgärdad | Facit visar digital metod, definitionsmängd och kontroll av att lösningen är unik. Korrekt fri avrundning bevaras medan för bred bastolerans tas bort. Nivå 2. |
| #3.54 | Åtgärdad | Facit skiljer den icke-negativa kvadratroten från ekvationens två lösningar och visar ett konkret motexempel. Slutsatsen var korrekt. |
| #3.74 | Åtgärdad | Facit visar den faktiska avvikelsen från noll och ett teckenbyte mellan 1,521 och 1,522. Vanlig miniräknare räcker för kontrollen; GeoGebra behövs inte. |
| #3.83 | Åtgärdad | Figuren visar nu en möjlig rektangel utan att redan ge optimal bredd och höjd. Facit binder ihop area, derivata och globalt maximum. Uppgiften är C/nivå 3. |
| #3.287 | Åtgärdad | Facit visar faktoriseringen och alla tre lösningar. Frågan kräver inte längre både exakt bekräftelse och ett valfritt decimalsvar samtidigt. Exakta svar och rätt tresiffriga avrundningar godtas i valfri ordning. |
| #3.330 | Åtgärdad | Facit visar både inre och yttre derivata innan x=1 sätts in. Tangentens lutning är 1. |
| #3.331 | Åtgärdad | Båda deriveringarna visas separat, följt av insättningen som ger f″(2)=6. |
| #3.332 | Åtgärdad | Facit visar båda termerna i produktregeln, faktorisering och tecken på hela definitionsmängden. Största värdet nås vid x=1. |
| #3.333 | Åtgärdad | Facit visar hur lutningsvillkoret ger x²=2. Båda exakta rötterna godtas i valfri ordning; decimalsvar besvarar inte kravet på exakt form. |
| #3.334 | Åtgärdad | Facit visar nollproduktmetoden och skiljer maximum vid x=0 från minimum vid x=2 med andraderivatan. |
| #3.335 | Åtgärdad | Facit visar att a är en konstant vid derivering och löser det givna tangentvillkoret. Svaret är a=−3. |
| #3.336 | Åtgärdad | Facit motiverar kvadratkompletteringen och visar att den nedre gränsen −16 verkligen nås vid x=±2. |
| #3.337 | Åtgärdad | Facit förklarar att parallella linjer har samma lutning och varför linjens konstantterm inte påverkar svaret x=3. |
| #3.338 | Åtgärdad | Facit visar båda digitala skärningarna, valet av den större och kontroll genom insättning. Svaret är 1,512. Nivå 2. |
| #3.339 | Åtgärdad | Facit visar både lösningen till derivataekvationen och teckenundersökningen på x>0. Största värdet nås vid x=2. |
| #3.340 | Åtgärdad | Kedjeregelns båda faktorer och insättningen visas separat. Flera beroende led motiverar nivå 2. Miniräknare tillåts. |
| #3.341 | Åtgärdad | Facit visar produktregel, exakt värde 3e och avrundning till 8,15. Rättningen lagrar nu hela referensvärdet 3e. |
| #3.342 | Åtgärdad | Facit visar täljarens och nämnarens derivator, kvotregeln och insättningen vid noll. Miniräknare tillåts. |
| #3.343 | Åtgärdad | Facit visar båda kedjeregelns faktorer och minustecknet vid derivering av cosinus. Nivå 2, med tillåten miniräknare. |
| #3.344 | Åtgärdad | Facit visar hur tangentens lutning läses ur två punkter innan kedjeregeln används. Figuren stämmer. C/nivå 3, med tillåten miniräknare. |
| #3.345 | Åtgärdad | Facit visar vilket argument som ska användas, hur tangentlutningen beräknas och varför den multipliceras med 2. Figuren stämmer. C/nivå 3. |
| #3.346 | Åtgärdad | Facit skiljer produktregelns addition från kvotregelns subtraktion och visar hanteringen av negativa tabellvärden. Fälten är fortsatt märkta och ordnade. E/nivå 2. |

## Verifiering och filer

- Alla 27 uppgifter: oberoende symbolisk eller numerisk kontroll av derivator, rötter, globala/lokala extrema och exempel. Fyra SVG-figurers punktkoordinater och geometriska samband kontrollerade, och figurerna visuellt inspekterade.
- **234 rättningsfall**, samtliga godkända i riktiga svarsfält på mobil och dator. Inkluderar rottecknet √, omordnade rötter, exakt/avrundat, fel grannavrundning och felaktig ordning i produkt/kvot-fälten.
- Efter manuella radbrytningar: **54 elevvyer och 54 lärarvyer**, utan LaTeX-fel, sidöverflöde eller för breda formelrader. De fyra manuella korten renderas i testet men blir inte spelbara i produkten.
- Matf1-validator: **0 ERROR, 8 WARNING, 67 INFO**, oförändrat. Den automatiska helbankskörningen har fortfarande 1479 äldre ERROR i andra banker; de är inte rättade i denna områdesrunda.
- Befintliga testsviter för verktygspolicy 2026-10-14 och facitgranskning 2026-10-25: godkända.
- Föregående områden linjär approximation och partiell integration: 39 respektive 36 huvuduppgifters skyddstester fortsatt godkända.
- Semantisk diff: exakt 27 avsedda huvuduppgifter ändrade; inga nya/borttagna ID:n. Revisionen är idempotent. Master och konsument har identiska bankfiler.

Ändrade produktionsfiler: `uppgiftermatf1.js` och cacheversion i `index.html` i båda repona. Revisionsskript: `tools/revidera-matf1-derivator-facit-2026-10-26.py`. Oberoende skyddstest: `tools/matf1-derivator-facit-2026-10-26.test.py`. Konsumentens `tools/matf1-derivator-facit-2026-10-26.cases.json` körs med befintlig browserharness och de 27 ID:na i denna logg. JSON-loggen innehåller ändrade fält per ID. Äldre byggskript får inte återställa korta facit; kör revisionen efter dem.

Parallell ändring 5048157/500ffa3 integrerad före push: åtta Ma3-kort flyttade till Ma4. Dessa ändringar är bevarade. Enda konflikten gällde cacheversionen, som nu omfattar båda rundorna. Efter rebase passerade derivatkontrollen, bankflyttens regression och jämförelsen av bankkopior. Inventeringen är uppdaterad.
