# Ma4: integral- och areafacit

## Granskade och ändrade uppgifter

| ID | Bedömning och ändring |
|---|---|
| 3.11 a–d | Frågan säger nu tydligt att eleven ska beräkna integralen och bedöma om den också är den geometriska arean. En ledtråd om asymptoter ersätts med en om grafens läge. Varje del har ett eget facit med beräkning och förklaring. Integralerna är 4, 0, 2 och 0; motsvarande geometriska areor är 4, 1, 2 och 4. Manuell bedömning behålls eftersom frågan även kräver ett resonemang. |
| 3.461 | Irrelevant generell text om längder och vinklar samt dimensionskontroll tas bort. Grafen avgränsar en kvarts cirkel med radie 3 och arean är \(9\pi/4\). |
| 3.473 | Generell text tas bort och lösningen delas upp: nollställen ±1, de två positiva delareorna 2/3 och 4/3 och symmetri ger arean 4. |
| 3.475 | Generell text tas bort; lösningen visar delintegralerna 2 och −2 och förklarar varför den geometriska arean är 4. |
| 3.206 | Generell text tas bort; facit visar skärningarna 0 och 4, vilken kurva som ligger över den andra och integralen som ger \(32/3\). |
| 3.179 | Generell text tas bort; facit visar att skärningarna är 0 och a, att arean är \(a^3/6\) och att \(a=3\). |

Samtliga matematiska slutsvar har kontrollerats oberoende och är oförändrade.
Lösningarna för 3.473, 3.475, 3.206 och 3.179 har också kortare formelrader
för mobilskärm. Uppgifterna 3.473 och 3.475 klaras med exakta värden utan
räknare. Övriga behåller tillåtna hjälpmedel; GeoGebra är tillåtet endast
tillsammans med miniräknare. Nivå, poäng och befintlig svarsrättning behålls.

Författarkällor: `tools/ma4-integralfacit-2026-10-27.py`,
`tools/ma4-integralfacit-mobil-2026-10-27.py` och
`tools/ma4-integralfacit-olikhet-2026-10-27.py`. De förutsätter det dåvarande
bankinnehållet och ska inte köras blint på senare versioner. Detta är ett
urval av liknande träffar, inte en fullständig manuell granskning av alla
facit i banken. Inga rapportstatusar har ändrats i produktionsdatabasen.

Visningen kontrollerades i båda apparna. Kunskapsgymmets kontroll omfattade
20 svarsförsök och 18 kortvisningar på mobil och dator; 3.11 är manuellt
bedömd. En efterföljande riktad kontroll prövade 3.11 och 3.179 igen. Vid
visuell kontroll upptäcktes att råa olikhetstecken dolde delar av facit;
de har HTML-kodats och mobilbilderna granskats på nytt. Konsumentens
`tools/ma4-integralfacit-2026-10-27.browser.cjs` kontrollerar att både
matematiken och den efterföljande förklaringen faktiskt visas. Bankkopiorna
är identiska och syntax samt diff är kontrollerade.
