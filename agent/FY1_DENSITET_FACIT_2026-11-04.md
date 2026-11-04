# Fy1 densitet: facitgranskning 2026-11-04

## Omfattning och beslut

Samtliga **178 huvuduppgifter och 53 explicita delkort** i området `densitet` är manuellt genomgångna. Faciten följer nu FACITMALL.md från 2026-11-04: numrerade steg, uppgiftsspecifika regel-/formelrubriker, beräkningar med förklaringar och egen svarsruta för varje del. Den nya mallen ersätter här den äldre onumrerade fysikprosan. Inget generellt regelverk har använts för att gissa lösningsrubriker; authoringskriptet innehåller de granskade lösningarna.

Alla 178 räknas som åtgärdade eftersom facitstrukturen ändrats. **Granskad – inget fel: inga i denna omgång.** Detta innebär inte att alla tidigare slutsvar var numeriskt fel. Inga rapportstatusar eller kommentarer har skickats till Supabase.

## Sakliga och pedagogiska förbättringar

- Avrundning och mellanled: 2.2, 2.26, 2.37, 2.38, 2.43, 2.54, 2.166, 2.180 och 2.275. Bevara full precision i fortsatta beräkningar, men visa slutsvaret i relevant precision.
- Frågans verkliga delindelning: särskilt 2.80, 2.83, 2.86, 2.88, 2.89 och 2.90. Facit får inte hitta på delar eller avslöja senare efterfrågade resultat i förtid.
- **2.90:** förutsättningen att volymer adderas flyttas från b till den gemensamma inledningen, eftersom den behövs redan i a. Det är enda ändrade frågetexten.
- Grafavläsning och mätfel: 2.80 och 2.92–2.106 samt 2.169–2.174. 2.99 använder koordinater inom grafens gränser. Linjeanpassning skiljs från kvoten av enskilda mätvärden. Bubblor ökar uppmätt volym och förklarar inte en punkt ovanför masslinjen.
- Flytvillkor och modeller: 2.91 har en strikt gräns; vid likhet är kroppen neutralt flytande. 2.182 visar både exakt skalgeometri och tunnplåtsapproximationen. 2.290 skiljer yttervolym från materialvolym.
- 2.203 visar massans ackumulation genom tre material. Den befintliga korrekta grafen bevaras och görs responsiv. 2.80 får två tydligare lösningsdiagram med graderade axlar.

Varje strukturell feltyp har följts upp i minst fem analoger där sådana finns, inklusive hela områdets delindelning, enhetsbyten, mellanled och svarsrutor. Avsiktliga skillnader i givna data på delkort (exempelvis 2.26) är bevarade.

## Verktyg och ändringsavgränsning

Miniräknare är tillåten på samtliga 178 huvuduppgifter och inget delkort förbjuder den. GeoGebra tillåts även i **2.80, 2.92–2.95, 2.99–2.106 och 2.203**, eftersom eleven ska konstruera/anpassa en graf. Att bara läsa av en redan given linje kräver inte detta. Övriga verktygstillstånd bevaras.

Ändrade bankfält: 178 `s`, 53 `spelDelar[].s`, de 14 `geogebra` ovan samt `2.90.t`. Rättningsnycklar, toleranser, precision, nivåer, ledtrådar och frågefigurer är oförändrade. De befintliga fullprecisionsnycklarna behövs för korrekt avrundning till elevens precision och ska inte ersättas med det kortare visningssvaret.

## Verifiering

- Oberoende numeriska regressioner i `fysik1-kapitel2.test.js` och densitetstesterna från 2026-10-21/22 passerar.
- Nytt `fysik1-densitet-facit-2026-11-04.test.js` skyddar täckning, faktisk delindelning, digitala verktyg, grafdata, flytgräns och oavrundade geometriska beräkningar.
- Tidigare kapitel 2-malltester och fysikprosatestet passerar. Densitet undantas från den äldre prosamallen eftersom det nya användarbeslutet gäller.
- Alla **231 huvud-/delfacit** renderade i Chromium/KaTeX 0.16.11 med respektive apps CSS i **390 px** bredd: inga KaTeX-fel eller överskjutande formelrader/svarsrutor. För långa formler har radbrutits.
- Områdets **69 fråge-SVG** visuellt lästa i nio kontaktkartor, samt de två nya lösningsgraferna i 2.80 och den bevarade grafen i 2.203. Axlar, mått och samband kontrollerade mot lösningarna.
- Authoringskriptet är idempotent. Strukturerad bankjämförelse bekräftar ändringsavgränsningen ovan.

## Alla granskade, åtgärdade och kommentarsförslag

Fullständig maskinläsbar lista: [JSON](FY1_DENSITET_FACIT_2026-11-04.json).

| ID | Status | Föreslagen kommentar |
|---|---|---|
| 2.2 | Åtgärdad | Facit visar uträkningarnas fulla värden och avrundade slutsvar med rätt antal värdesiffror. |
| 2.6 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.7 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.8 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.17 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.18 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.23 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.24 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.25 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.26 | Åtgärdad | Facit visar volym, densitet och massa stegvis. Delkortens avsiktligt olika givna data är bevarade. |
| 2.27 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.31 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.37 | Åtgärdad | Hålrummets volym beräknas med oavrundad metallvolym. Mellanled och avrundat slutsvar är tydliga. |
| 2.38 | Åtgärdad | Facit visar 1967,5 kg före avrundning och 2,0 ton som slutsvar. |
| 2.39 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.40 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.41 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.42 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.43 | Åtgärdad | Blandningens densitet beräknas med hela sirapsmassan, utan för tidig avrundning. |
| 2.50 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.274 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.51 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.52 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.53 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.54 | Åtgärdad | Facit hänvisar inte längre till ett avrundningskrav som saknas i frågan. |
| 2.55 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.56 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.77 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.78 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.79 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.80 | Åtgärdad | Facit följer frågans tre delar och visar två tydliga diagram, först mätpunkterna och sedan den anpassade linjen. |
| 2.81 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.82 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.83 | Åtgärdad | Facit följer frågornas ordning: massa, volym och sedan densitet och flytförmåga. |
| 2.84 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.85 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.86 | Åtgärdad | Facit har separata svar för densiteter, luftandel och flytförmåga. |
| 2.87 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.88 | Åtgärdad | Facit besvarar den enda frågan utan att lägga till egna deluppgifter. |
| 2.89 | Åtgärdad | Facit visar atomvolym, avstånd och modellens begränsningar i samma ordning som frågorna. |
| 2.90 | Åtgärdad | Antagandet om adderbara volymer står nu före beräkningen. Facit har två delar och förklarar varför receptet bara är ungefärligt. |
| 2.91 | Åtgärdad | Facit skiljer gränsen för neutral flytkraft från villkoret för att flyta med en del ovanför ytan. |
| 2.92 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.93 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.94 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.95 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.96 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.97 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.98 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.99 | Åtgärdad | Lutningen visas med koordinater inom diagrammet. Facit förklarar varför hela mätserien bör användas. |
| 2.100 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.101 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.102 | Åtgärdad | Facit förklarar vilka mätfel som kan ge en punkt ovanför linjen och varför luftbubblor ger motsatt effekt. |
| 2.103 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.104 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.105 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.106 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.107 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.108 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.275 | Åtgärdad | Facit visar masskillnaden mellan materialen och räknar fram kärnans radie med noggranna mellanled. |
| 2.109 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.110 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.111 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.112 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.113 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.114 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.115 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.116 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.117 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.118 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.119 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.120 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.121 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.122 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.123 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.124 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.125 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.126 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.127 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.128 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.129 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.130 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.131 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.132 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.133 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.134 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.135 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.136 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.137 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.138 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.139 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.140 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.141 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.142 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.143 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.144 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.145 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.146 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.276 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.147 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.148 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.149 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.150 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.151 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.152 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.153 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.154 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.155 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.156 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.157 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.158 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.159 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.160 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.161 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.162 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.163 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.164 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.165 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.166 | Åtgärdad | Oavrundad volym används vid beräkning av densiteten. |
| 2.167 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.168 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.169 | Åtgärdad | Facit visar hur diagrammets SI-enheter används i lutningsberäkningen. |
| 2.170 | Åtgärdad | Facit kopplar rätt linje till rätt densitet och visar enhetsbytet. |
| 2.171 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.172 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.173 | Åtgärdad | Facit skiljer vätskans densitet från den tomma behållarens massa. |
| 2.174 | Åtgärdad | Mätfelet och densiteten förklaras var för sig, i frågornas ordning. |
| 2.175 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.176 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.177 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.178 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.179 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.180 | Åtgärdad | Facit visar hålrummets volym, metallens densitet och massan före borrningen utan för tidig avrundning. |
| 2.181 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.182 | Åtgärdad | Facit räknar med både botten och lock och förklarar även den tillåtna tunnplåtsapproximationen. |
| 2.183 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.184 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.277 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.185 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.186 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.187 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.188 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.189 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.190 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.191 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.192 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.193 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.194 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.195 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.196 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.197 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.198 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.199 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.200 | Åtgärdad | Blandningens ekvation löses stegvis och massandelen skiljs från volymandelen. |
| 2.201 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.202 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.203 | Åtgärdad | Facit härleder den styckvisa massgrafen och förklarar lutningen i varje material. |
| 2.278 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.279 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.280 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.281 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.282 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.283 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.284 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.285 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.286 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.287 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.288 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.289 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.290 | Åtgärdad | Facit skiljer yttervolymen som tränger undan vatten från stålskalets volym. |
| 2.327 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.328 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.329 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.330 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.331 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.332 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.333 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
| 2.334 | Åtgärdad | Facit har fått tydliga steg med relevanta formler, visade beräkningar och ett fullständigt slutsvar. |
