# Ma4: optimeringsfacit

Sex uppgifter har granskats: 2.131, 2.205, 2.224, 2.251, 2.260 och 2.269.
Generiska geometriråd har ersatts med uppgiftsspecifika mellanled och
motiveringar för extremvärdet. Verktygen behålls: samtliga tillåter både
miniräknare och GeoGebra. Nivå och poäng är oförändrade.

| ID | Oberoende kontroll och ändring |
|---|---|
| 2.131 | \(V=x(30-2x)(20-2x)\). Enda stationära punkten för \(0<x<10\) är \((25-5\sqrt7)/3\approx3,92375\) cm. Volymen är noll i ändarna och positiv inuti, vilket ger maximum. Facit visar begränsningen och motiveringen. |
| 2.205 | Samma volymmodell och maximum som 2.131. Facit visar mellanled och maximum. Den självrättande numeriska målpunkten har ändrats från 3,92 till 3,9237478148923493 så att rättningen utgår från det beräknade värdet. |
| 2.224 | \(P=2x+200/x\); derivatan byter tecken från minus till plus vid \(x=10\). Minsta omkretsen är 40 cm. |
| 2.251 | \(A=2\pi r^2+2000/r\), \(r^3=500/\pi\) och \(h=2r\). Andra derivatan är positiv. Radien är cirka 5,42 cm och höjden 10,84 cm. |
| 2.260 | \(A=12x-x^3\), med maximum vid \(x=2\) och höjd 8. Den största arean är 16 areaenheter; derivatans tecken visas. |
| 2.269 | \(A'=200\cos v+100\cos2v\). Med \(c=\cos v\) fås \(2c^2+2c-1=0\) och den enda giltiga roten \((\sqrt3-1)/2\). Derivatan byter från plus till minus; vinkeln är cirka 68,5° och arean cirka 220 cm². Den långa formeln i frågan delas upp för mobilvisning utan att ändra innehållet. |

2.131 och 2.205 använder samma låda och nästan samma fråga. 2.131 är
avstängd från ordinarie träning i Kunskapsgymmet, vilket minskar risken för
upprepning där. Ingen av uppgifterna eller deras ID har tagits bort.

Författarkällorna `tools/ma4-optimering-facit-2026-10-27.py` och
`tools/ma4-optimering-mobil-2026-10-27.py` bygger på det dåtida
bankinnehållet och ska inte köras blint på en senare version. Inga
rapportstatusar har ändrats i produktionsdatabasen.

Uppgiftslabbet har visat alla sex frågor utan rapporterade renderingsfel.
I Kunskapsgymmet testades fem tillgängliga frågor med 46 svarsförsök och
tio vyer, inklusive korrekt avrundade värden och felaktiga svar. Den första
kontrollen hittade en för bred fråga i 2.269; efter uppdelning testades den
igen på mobil och dator och mobilvyn granskades visuellt. 2.131 är spärrad
från ordinarie träning. Bankkopiorna är identiska och syntax samt diff är
kontrollerade. Svarsfall finns i konsumentens
`tools/ma4-optimering-2026-10-27.cases.json`.
