# Fy1: blandade kopplingar – manuell facitgranskning 2026-11-04

## Omfattning och utfall

Alla **26 huvuduppgifter och 37 explicita delkort** i `kopplingar` / `Blandade kopplingar` är manuellt genomgångna. Samtliga får uppgiftsspecifika, numrerade lösningssteg enligt FACITMALL.md och fullständiga svarsrader. Relevanta ledtrådar har också förbättrats. **Åtgärdade: alla 26 nedan. Granskad – inget fel: inga i denna omgång**, eftersom samtliga behövde pedagogiska förbättringar. De numeriska rättningsnycklarna var däremot korrekta och är bevarade.

Detta följer [inventeringen av alla sju banker](FACIT_INVENTERING_2026-11-04.md). Inventeringen är en strukturskanning; den innebär inte att samtliga bankers lösningar har granskats manuellt.

## Viktiga beslut och jämförelser

- Varje del ska ha hela sitt svar. Jämförda flerledssvar: 8.18, 8.87, 8.90, 8.524, 8.526, 8.527 och 8.529. Tidigare sammanfattningar utelämnade exempelvis en av de två strömmarna/spänningarna.
- Fristående delkort ska kunna läsas utan andra kort: 8.43, 8.53, 8.54, 8.126, 8.130 och 8.133. Kort 8.54 d får inte använda huvuduppgiftens 180 och 120 mA. Kort 8.126 b/c får inte hänvisa till krets A/B som saknas i korttexten.
- Kortets egna givna mellanvärden gäller: 8.43 c anger 0,03429 A och ger 6,858 V; d anger 6,86 V. 8.53 d anger 0,05455 A och ger 6,546 V. Huvuduppgiften använder full precision. Dessa avsiktliga skillnader får inte normaliseras bort.
- Skillnaden mellan totalström och grenström förklaras i bland annat 8.4, 8.52, 8.53, 8.134, 8.154, 8.256 och 8.529. I 8.256 används exakta mellanled; slutströmmen är 18/13 A.
- Nivå och verktyg är granskade och bevarade. Alla huvuduppgifter tillåter miniräknare; inget delkort förbjuder den. Dessa beräkningar kräver inte digital grafanalys eller GeoGebra. 8.153 förblir en läraruppgift (`spel:false`).
- Frågetext, figurer, nivå, svarstyp, numeriskt svar och tolerans har inte ändrats. Ändringarna begränsas till facit och ledtråd.

## Figurer och validering

24 huvuduppgifter har befintliga figurer (25 SVG totalt eftersom 8.126 visar två kopplingar). Alla frågefigurer har kontrollerats visuellt i kontaktkartor. 8.153:s symboliska generalisering och 8.370:s enkla resistansberäkning behöver ingen ytterligare figur för denna faciträttning.

- Oberoende fysikmodeller verifierar samtliga 24 numeriska huvudnycklar och tillämpliga delkort, inklusive deras egna mellanvärden. Begreppssvar och symboliska 8.153 har granskats manuellt.
- `tools/fysik1-blandade-kopplingar-facit-2026-11-04.test.js` skyddar numeriken, de fullständiga dubbelsvaren, verktygen och fristående kort utan osynliga data.
- Tidigare `fysik1-kopplingar.test.js` och `fysik1-kopplingsscheman-2026-11-02.test.js` passerar.
- Browserharnessen `tools/fysik1-kopplingar-facit-2026-11-04.browser.py` har renderat **alla 63 facit och ledtrådar vid 390 px med båda apparnas CSS**: inga KaTeX-fel eller överflödande facit. Utvalda fullständiga huvud-/delfacit har dessutom lästs visuellt, inklusive 8.18, 8.43 c, 8.54 d, 8.87, 8.126 b, 8.153, 8.524 och 8.529.
- Den manuella redigeringsplanen finns i `tools/fy1-facit-kap23/kopplingar.py`. Den innehåller uppgiftsspecifikt författade lösningar, inte automatisk semantisk massomskrivning.

## Alla granskade och åtgärdade uppgifter – kommentarsförslag

Kommentarerna är förslag, inte inskickade meddelanden till elever. Ingen rapportstatus ändras i Supabase av en bankpush.

| Uppgift | Status | Förslag på kommentar |
|---|---|---|
| 8.4 | Åtgärdad | Lösningen visar parallellresistans, totalström och grenspänning innan effekten beräknas. |
| 8.18 | Åtgärdad | Båda strömmarna finns nu i svaret till a). Effektförhållandet förklaras med strömmarnas kvadrater. |
| 8.43 | Åtgärdad | Serie- och parallellstegen förklaras. Fristående kort använder sina egna givna mellanvärden. |
| 8.52 | Åtgärdad | Facit visar hur serien i en gren först ersätts och hur spänningen över rätt resistor sedan beräknas. |
| 8.53 | Åtgärdad | Totalström och grenspänning skiljs åt. Kort d använder sin angivna ström utan att byta till huvuduppgiftens värde. |
| 8.54 | Åtgärdad | Knuten och strömfördelningen förklaras. Kort d hänvisar inte längre till tal som saknas i kortet. |
| 8.87 | Åtgärdad | Svarsraderna innehåller nu båda spänningarna och båda strömmarna med tydlig koppling till resistorerna. |
| 8.90 | Åtgärdad | Båda spänningarna redovisas i b). Facit förklarar ström och effekt när en resistor förbikopplas. |
| 8.123 | Åtgärdad | Facit visar varför resistorer i samma gren summeras före parallellberäkningen. |
| 8.126 | Åtgärdad | Batteriets drifttid och effekten förklaras. Fristående kort använder kopplingarnas namn i stället för osynliga A/B-beteckningar. |
| 8.127 | Åtgärdad | Facit visar hur samma ström går genom serieresistorn och hela parallellkopplingen. |
| 8.252 | Åtgärdad | Beräkningen har tydliga steg från parallellresistans till den sökta spänningen. |
| 8.130 | Åtgärdad | Enhetsbytet från mA visas. Kort d beräknar totalresistansen direkt från sina egna givna data. |
| 8.133 | Åtgärdad | Huvuduppgift och delkort har tydliga, separata lösningar utifrån respektive givna värden. |
| 8.253 | Åtgärdad | Facit förklarar varför grenströmmarna ska adderas innan spänningsfallet i serieresistorn beräknas. |
| 8.134 | Åtgärdad | Amperemeterns grenström skiljs tydligt från kretsens totalström. |
| 8.254 | Åtgärdad | Facit visar ersättningsresistans och spänningsfördelning utan för tidig avrundning. |
| 8.255 | Åtgärdad | Totalresistansen byggs upp stegvis innan totalströmmen beräknas. |
| 8.153 | Åtgärdad | Det symboliska resonemanget visar varför strömmen blir I/n i serie och nI parallellt. |
| 8.154 | Åtgärdad | De tre parallella grenarna och strömmen i den efterfrågade grenen förklaras stegvis. |
| 8.256 | Åtgärdad | Beräkningen behåller full precision genom mellanleden och avrundar först slutsvaret. |
| 8.370 | Åtgärdad | Facit visar tydligt varför parallellparet ersätts innan serieresistorn adderas. |
| 8.524 | Åtgärdad | Öppen och sluten brytare behandlas var för sig. Både källspänning och okänd resistans sammanfattas. |
| 8.526 | Åtgärdad | Facit förklarar hur voltmeterns resistans påverkar kopplingen och beräknar båda efterfrågade storheterna. |
| 8.527 | Åtgärdad | Båda ledningarnas resistans räknas med. Källspänning och verkningsgrad förklaras i egna steg. |
| 8.529 | Åtgärdad | Nollströmmen kopplas till lika potential. Facit härleder både den okända resistansen och totalströmmen. |
