# Ma1 – ekvationsproblem på högre nivå, 2026-11-06

Tio nya, handskrivna uppgifter i **Algebra och ekvationer → Problemlösning med ekvationer**, familjen *Problemlösning i flera steg*, för 1a, 1b och 1c. Åtta på träningsnivå 4 (C) och två på nivå 5 (A). Alla har egen SVG, specifik ledtråd, numrerat stegvis facit och ett självrättande numeriskt svarsfält.

## Samtliga nya och granskade uppgifter

| ID | Innehåll | Nivå | Svar | Centralt metodval |
| --- | --- | --- | --- | --- |
| 1.1675 | Bensin till 4,5 liter olja | 4 · C | 220,5 liter | Oljan ingår i hela blandningens volym; 225 liter är inte tillsatt bensin. |
| 1.1676 | Två fruktdrycker med olika halter | 4 · C | 6,4 liter | Både juicemängd och totalvolym växer när den starkare drycken tillförs. |
| 1.1677 | Tappa ur kylvätska och ersätta med vatten | 4 · C | 6,75 liter | Urtappad vätska innehåller också glykol; slutvolymen är oförändrad. |
| 1.1678 | Koka sockerlag och sedan tillföra socker | 4 · C | 1 kg | Vattenavgång ändrar först bara totalmassan; sockertillsats ändrar sedan både delen och det hela. |
| 1.1679 | Två föreningskassor | 4 · C | 3 200 kr | Skriv det andra startbeloppet som 5 000 minus det första; procentminskning och fast tillskott. |
| 1.1680 | Två olika rabatter och en kupong | 4 · C | 900 kr | Prisskillnad före rabatter, skilda förändringsfaktorer, kupongen sist. |
| 1.1681 | Stängsel, mellanvägg och grind | 4 · C | 28 m | Tre bredder och två längder, grinden räknas bort en gång; frågan gäller längd, inte ekvationens bredd. |
| 1.1682 | Kabelrulle, spill och fem korta kablar | 4 · C | 11 m | Del av ursprungslängd kombineras med skillnaden mellan två kabellängder. |
| 1.1683 | Cyklist som stannar, annan hinner ikapp | 5 · A | 38,75 min efter 09.00 | Avgör först i vilket tidsintervall mötet sker; startfördröjning och enhetsbyte. |
| 1.1684 | Extra ritblock på köpet | 5 · A | 15 block | Modellera samma ordinarie styckepris med två erbjudanden och eliminera det. |

Nivå 4 motiveras av att eleven själv bygger samband med flera beroende storheter. Nivå 5 kräver dessutom ett strategival mellan rörelseförlopp respektive att reducera två prisbeskrivningar till en obekant. Höga nivåer kommer inte från besvärlig huvudräkning. Alla ryms inom linjär ekvationslösning i Ma1; inga andragradsekvationer, formella ekvationssystem eller analysmetoder behövs. I 1.1684 uttrycks priset på två sätt, vilket ger en enda linjär ekvation i antalet.

## Verktyg, precision och självrättning

Miniräknare tillåts på alla tio eftersom modelleringen är det som tränas. GeoGebra krävs inte. Standardformatet `numeriskt` och uppgiftens svarsenhet används; inga nya rättningsregler införs. Ingen dold avrundning krävs. Alla svar kan anges exakt med ändliga decimaler; antal block är heltal. Kunskapsgymmets befintliga policy för avrundning gäller.

Browserprovet kontrollerar riktiga `kvFacit`, `delSvarRatt` och `renderTraining`: ett fält, svar med komma/punkt, naturlig enhet och relevanta enhetsbyten (ml, cl, g, cm och sekunder). Typiska fel, exempelvis 225 liter bensin, bredden 12 m i stället för längden 28 m och 18,75 minuter i stället för tid sedan 09.00, ska inte godtas. Ingen inloggning eller elevdatabas används.

## Facit och figurer

Varje facit definierar den obekanta, förklarar vad ekvationen betyder, visar mellanled och kontrollerar svaret i ursprungssituationen. Ledtrådar pekar på metodval men lämnar inte ut den färdiga ekvationen. Figurerna sammanfattar givna förhållanden; inga svar läcker ut. Volymbilder och längdskisser markeras schematiska. Alla tio figurer har granskats visuellt tillsammans; särskild kontroll av grinden, mellanväggen och tidslinjens proportioner. Både fråga, facit och ledtråd renderas i verkliga appvyer vid 390 och 1280 px.

## Kontroller och filer

- `tools/bygg-ma1-ekvationsproblem-2026-11-06.py`: dokumenterar de tio handskrivna uppgifterna; avbryter vid befintligt ID.
- `tools/ma1-ekvationsproblem-2026-11-06.test.js`: sju tester, oberoende återinsättning i situationernas samtliga villkor, positivt/heltalsantal där det krävs, första mötet, metadata och bankvalidator.
- `tools/ma1-ekvationsproblem-2026-11-06.browser.py`: faktisk visning och rättning, KaTeX, SVG-text inom viewBox, inga för breda ekvationer, mobil/dator i båda apparna.
- SVG-validator: inga fynd i samtliga tio slutliga figurer. I denna miljö användes Playwright som transport för validatorns webbläsarmätning, eftersom Chromiums kommandoradsstart inte slutfördes. Samma geometrianalys användes.
- Bankvalidator: inga fynd i de tio nya objekten. Syntax och diff kontrollerade. Befintliga objekt bevaras vid strukturerad jämförelse.

**Åtgärdade gamla fel:** inga i denna omgång. **Granskad – inget fel (gamla rapporter):** inga rapporter ingår. Alla tio nya uppgifters facit är kontrollerade. Inga rapportstatusar har ändrats och inga elevkommentarer har skickats.

De först valda ID-numren krockade med en samtidigt publicerad algebraomgång. Dessa opublicerade utkast flyttades därför till 1.1675–1.1684 innan leverans. Samtliga redan publicerade objekt från båda sessionerna bevarades oförändrade.
