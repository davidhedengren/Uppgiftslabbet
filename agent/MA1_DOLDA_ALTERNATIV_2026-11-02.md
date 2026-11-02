# Ma1: saknade alternativ, fortsättning 2026-11-02

Fortsättning på `FELRAPPORTER_2026-11-02_1352.md`. Ändrade 0.51, 0.264, 0.267, 0.280, 0.301, 0.309 och 0.404. De hänvisar till svarsalternativ som tidigare inte visades i Uppgiftslabbet; de anger nu uttryckligen att ett alternativ ska väljas. Varje felaktigt svar har fått en egen förklaring som visas i Kunskapsgymmet. Frågedata, rätt svar, nivå, poäng och verktyg är annars oförändrade.

| ID | Oberoende kontroll |
|---|---|
| 0.51 | 3/5 dividerat med 0 är inte definierat; övriga tre uttryck är definierade. |
| 0.264 | 20−(3+2)·4=0, de andra uttrycken ger 76, 25 respektive 15. |
| 0.267 | 6+2·5=16 medan (6+2)·5=40. |
| 0.280 | 24÷6·2=8 medan 24÷(6·2)=2. |
| 0.301 | 56/98=4/7. 28/49 och 8/14 är likvärdiga men kan förkortas. |
| 0.309 | 4/9=44/99 och 5/11=45/99, så det förra bråket är mindre. |
| 0.404 | 1,099 är mindre än 1,100; övriga tre påståenden är fel. |

Granskade utan motsvarande fel: 0.36, 0.166, 0.167, 0.259 och 0.278 är självständigt besvarbara som öppna frågor, så deras alternativ för träning behöver inte föras in i lärarfrågan. Miniräknare och GeoGebra är inte tillåtna på de sju ändrade uppgifterna eftersom de prövar prioriteringsregler, bråkjämförelse och taluppfattning med enkla beräkningar. Nya figurer behövs inte.

Skydd: `tools/ma1-dolda-alternativ-2026-11-02.test.js` verifierar matematiken, tillåtna hjälpmedel, synliga alternativ och förklaringar. Faktiska lärarkort och rättning av samtliga alternativ, inklusive att felkommentarer visas, prövas i webbläsare på mobil och dator. Validatorn ger inga nya fynd i Ma1. Full svit: Uppgiftslabbet 1 084 godkända och 43 kända SVG-fel på grund av saknad Chrome-sökväg; Kunskapsgymmet 309 godkända och sex tidigare kända fel. Ingen rapportstatus har ändrats i appen.
