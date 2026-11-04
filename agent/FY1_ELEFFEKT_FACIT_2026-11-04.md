# Fy1: elektrisk effekt och energi – facitgranskning 2026-11-04

## Omfattning och utfall

Hela familjen **Elektrisk effekt och energi**, `omr:kopplingar`: **80 huvuduppgifter och 78 explicita delkort**, baslinje master `199ac59`. Samtliga frågor, facit, ledtrådar och beräkningar är genomlästa. Facit följer nu FACITMALL.md med namngivna, numrerade steg, insättningar och fullständiga svarsrader. Den manuellt skrivna redigeringsplanen är `tools/fy1-facit-kap23/eleffekt.py`; den gissar inga rubriker från äldre text.

**Åtgärdade: alla 80 i tabellen. Granskad – inget fel: inga**, eftersom alla behövde den nya facitstrukturen. Det betyder inte att alla hade räknefel. Numeriska huvud- och delkortssvar var korrekta, förutom att **8.659 hade ett avrundat rättningsmål** som kunde underkänna korrekta svar med fler siffror. Det målet är nu oavrundat. Visat svar är fortsatt 17,7 V. Tolerans, precision, nivå och verktygsmetadata har bevarats.

Frågetexter, figurer, ID:n och delindelningar är oförändrade. Ändrade bankfält: `s`, `ledtrad`, `spelDelar[].s`, `spelDelar[].ledtrad` och `8.659.rättSvar`. Kapitel 4:s parallella granskning lämnas orörd.

## Pedagogiska fynd och följdgranskning

- **Ofullständiga svarsrader:** 8.98 b/c hade bara strömmen i huvudfacitets svar, trots att även värmeeffekten efterfrågades. Jämförelser 8.528, 8.594, 8.600, 8.605 och 8.658 har nu också kompletta namngivna svar. 8.89 har egna svar i alla fyra delar, utan dubblerade delbokstäver.
- **Enheter och mellanled:** 8.98:s delkort hoppade direkt från SI-insättning till MW. Nu redovisas W och omvandlingen till MW. Jämförda 8.14, 8.202, 8.205, 8.453, 8.588 och 8.591 har explicita och korrekta enhetsbyten. Full precision används bland annat i 8.128, 8.396, 8.454, 8.459, 8.461, 8.600, 8.605 och 8.659.
- **Missriktade ledtrådar:** Uppgifter med redan given effekt ska inte be eleven först beräkna P=UI. Rättat i 8.194, 8.202, 8.205, 8.185, 8.186, 8.187 och delkort i 8.39, 8.97, 8.446, 8.449 och 8.461. 8.603 hänvisade till två effekter trots att bara en var given. 8.89:s fyra delar får olika relevanta ledtrådar.
- **Rättningsmål med full precision:** 8.659 ändras från 17,7 till 500·√(0,50/400) ≈ 17,67766953 V. Fem jämförelser 8.396, 8.596, 8.600, 8.605 och 8.463 hade redan korrekta oavrundade mål, som bevaras. Rättningsfunktionen verifierar 20, 18, 17,7, 17,68 och 17,678, och avvisar felaktiga 17,70/17,700/17,6/17,679 samt fel enhet.
- **Egna delkortsvärden:** 8.3 b, 8.5 b, 8.15 c, 8.92 c, 8.94 b/c, 8.445 b, 8.446 c, 8.452 b och 8.461 b behåller sina egna givna data. De får inte ersättas med huvuduppgiftens fullprecisionsresultat. 8.89 och 8.128 använder befintligt `spelIntro` och ärver respektive delnyckel.
- **Modellförståelse:** 8.5 förklarar varför ett öppet kylskåp värmer rummet; 8.37 skiljer avrundade märkdata från energibevarande; 8.46 lovar inte ofarlighet utifrån spänning; 8.96 lovar ingen viss utlösningstid; 8.98 behåller sitt avsiktligt orimliga driftfall. Inga senare delars svar läggs in i tidigare delfacit.
- **Nivå och verktyg:** 15 uppgifter på nivå 1, 56 på nivå 2, 7 på nivå 3 och 2 på nivå 4. Tidigare nivåbeslut från kopplingsgranskningen bevaras efter individuell läsning: direkta samband, rutinkedjor respektive mer krävande krets-/energiresonemang. Alla huvuduppgifter tillåter miniräknare och inget delkort förbjuder den. Uppgifterna kräver inte digital grafanalys. Kvadratrötterna för strömmens/spänningens storlek är direkta formelomskrivningar, inte grafiska ekvationsproblem.

## Kontroller

- `tools/fysik1-eleffekt-facit-2026-11-04.test.js`: oberoende fysikmodeller för **alla 80 huvudnycklar**, delkortens egna data, strukturen i alla 158 facit, dubbelsvar, ledtrådar och verktyg.
- Tidigare kopplingsprov, de 40 enkla kopplingsuppgifterna och nivå 3-omgång 11 passerar. Det äldre förbudet mot `facit-stegvis` i testet för enkla kopplingar ersätts av det senare användarbeslutet i FACITMALL.md. Förbud mot generiska ”Steg 1”-rubriker och samtliga numeriska/figur-/nivåkontroller behålls.
- Kunskapsgymmets verkliga `fysikVardesiffrorRatt` testas för 8.659 i `tools/fysik1-eleffekt-rattning-2026-11-04.test.js`.
- Alla **158 facit med ledtrådar** renderas med KaTeX vid 390 px med **båda apparnas CSS**: inga formelfel eller överflödande rader efter mobilanpassningen av 8.446. Browserharness: `tools/fysik1-eleffekt-facit-2026-11-04.browser.py`.
- Alla **25 befintliga frågefigurer** kontrolleras visuellt: rätt mätarkoppling, topologi och komponentnamn. Utvalda långa facit läses även som fullständiga mobilbilder, bland annat 8.5, 8.77, 8.98, 8.128, 8.454, 8.461 och 8.659.
- Strukturerad bankdiff säkerställer exakt 80 ändrade objekt och endast avsedda fält. Syntax och `git diff --check` kontrolleras före leverans.

## Alla granskade och åtgärdade – kommentarsförslag

Kommentarerna är förslag, inte skickade elevmeddelanden. Bankpushen ändrar inga rapportstatusar i Supabase.

| Uppgift | Status | Kommentar |
|---|---|---|
| 8.3 | Åtgärdad | Ohms lag och effektval förklaras. Kort b använder sin egen givna ström 0,0182 A. |
| 8.5 | Åtgärdad | Kompressorns faktiska arbetstid visas. Kylskåpets energiflöde förklaras och kort b använder 315,4 kWh. |
| 8.6 | Åtgärdad | Omvandlingen från kΩ och mA visas. Strömmens storlek fås med den positiva roten. |
| 8.14 | Åtgärdad | Omvandlingarna mA till A och W till mW förklaras. |
| 8.15 | Åtgärdad | Mottagen effekt, elektrisk effekt och verkningsgrad skiljs åt. Kort c använder sitt givna 203 W. |
| 8.27 | Åtgärdad | Ah, C, kJ och drifttid förklaras med tydliga enheter. |
| 8.36 | Åtgärdad | Strömmen skrivs i ampere och sambanden för spänning och effekt visas. |
| 8.37 | Åtgärdad | Wh och Ah förklaras. Facit skiljer avrundade märkdata från verklig energibalans. |
| 8.39 | Åtgärdad | Dygnsenergi, månadsenergi, kostnad och ström får egna lösningssteg. Energi-ledtråden kräver inte längre en onödig effektberäkning. |
| 8.46 | Åtgärdad | Medeleffekt skiljs från pulseffekt. Spänningen ensam ger ingen säker riskbedömning. |
| 8.63 | Åtgärdad | Facit förklarar att märkdata gäller när lampan ansluts till märkspänningen. |
| 8.75 | Åtgärdad | Effekten räknas direkt från spänning och resistans utan avrundad mellanström. |
| 8.193 | Åtgärdad | Effektsambandet visas med insättning och tydlig svarsrad. |
| 8.77 | Åtgärdad | Förklaringen visar varför halverad spänning ger en fjärdedel av effekten vid konstant resistans. |
| 8.194 | Åtgärdad | Energi räknas direkt från given effekt och tid. Missvisande ledtråd om P=UI borttagen. |
| 8.89 | Åtgärdad | Alla fyra delar har nu kompletta svarsrader och egna relevanta ledtrådar. Dubbla delbokstäver i facit borttagna. |
| 8.92 | Åtgärdad | Tillförd elenergi skiljs från nyttigt lyftarbete. Kort c använder 3,44 J enligt sin egen text. |
| 8.94 | Åtgärdad | Effektbesparing, användningstid, kronor och återbetalningstid förklaras. Kortens egna värden bevaras. |
| 8.96 | Åtgärdad | Total effekt och ström jämförs med säkringens märkström utan att lova en exakt utlösningstid. |
| 8.97 | Åtgärdad | Räckvidd och kupévärmarens energi förklaras. Ledtråden till b utgår nu från restiden och given effekt. |
| 8.98 | Åtgärdad | Båda svaren finns i b/c. W till MW visas korrekt i mellanleden. Orimligt driftfall förklaras med energibevarande. |
| 8.109 | Åtgärdad | Laddningen skrivs i coulomb före energiberäkningen och svaret omvandlas till kJ. |
| 8.111 | Åtgärdad | Resistans och effekt får var sin namngiven formel och svarsrad. |
| 8.112 | Åtgärdad | Medelspänning och batteritid förklaras med separata omvandlingar av kJ, kC, mA och timmar. |
| 8.128 | Åtgärdad | Lampornas spänningsdelning förklaras. Resistansen räknas med full precision och kortslutningens effekt förklaras. |
| 8.156 | Åtgärdad | Batteriets laddning, energi och drifttid förklaras med tydliga enhetsbyten. |
| 8.202 | Åtgärdad | W omvandlas till kW före energiberäkningen. Ledtråden utgår från den redan givna effekten. |
| 8.203 | Åtgärdad | Facit namnger det effektsamband som använder spänning och resistans. |
| 8.183 | Åtgärdad | Effektberäkningen har namngiven formel, insättning och svarsrad. |
| 8.184 | Åtgärdad | Effektberäkningen har namngiven formel, insättning och svarsrad. |
| 8.205 | Åtgärdad | Energiberäkningen visar W till kW och varför svaret blir kWh. |
| 8.185 | Åtgärdad | Facit förklarar varför kW gånger timmar ger kWh. |
| 8.186 | Åtgärdad | Effekten skrivs i kW innan tiden löses ut ur energisambandet. |
| 8.206 | Åtgärdad | Spänningens storlek beräknas som den positiva roten ur effekt gånger resistans. |
| 8.187 | Åtgärdad | Energianvändningen ger först effekten; därefter beräknas strömmen. Ledtråden följer samma väg. |
| 8.396 | Åtgärdad | Kortslutningen och antalet återstående lampor förklaras. Full precision behålls i effektberäkningen. |
| 8.445 | Åtgärdad | Datorns drifttid beräknas med dess egen effekt. Delkort b använder sina givna 9,9 MJ. |
| 8.446 | Åtgärdad | Enhetsbyten, årsmodell och antal blixtar visas. Kort c använder 4,7 GJ; långa formler är radbrutna. |
| 8.447 | Åtgärdad | Mekanisk effekt omvandlas till watt, sedan till elektrisk effekt med verkningsgraden före strömberäkningen. |
| 8.448 | Åtgärdad | Effekt, energi i kWh och elkostnad förklaras i separata steg. |
| 8.449 | Åtgärdad | Batteriets energi i Wh/kWh förklaras. Drifttiden använder båda lampornas sammanlagda effekt. |
| 8.450 | Åtgärdad | Facit skiljer glödlampans effekt från minskningen i effekt och beräknar därefter den sparade kostnaden. |
| 8.451 | Åtgärdad | Temperaturökning, värmebehov, elektrisk effekt och uppvärmningstid förklaras. |
| 8.452 | Åtgärdad | In- och utenergi skiljs åt. Temperaturändring i K och °C förklaras; kort b använder 221 J. |
| 8.453 | Åtgärdad | Omvandlingen från kWh till J visas före beräkningen av batteriets laddning. |
| 8.454 | Åtgärdad | Energins väg från el till smält massa, volym och istjocklek visas utan för tidig avrundning. |
| 8.455 | Åtgärdad | Facit räknar värmen under en minut och förklarar hur den bestämmer vattenmängden per minut. |
| 8.456 | Åtgärdad | Ström och ledningens värmeeffekt skiljs åt vid båda spänningarna. Ledtrådarnas felaktiga TeX-tecken ersatta. |
| 8.457 | Åtgärdad | Verkningsgraden används åt rätt håll: elenergin är större än värmen som vattnet tar upp. |
| 8.458 | Åtgärdad | Värmarens effekt och vattnets energibehov beräknas före tiden. |
| 8.459 | Åtgärdad | Full precision behålls när värmeenergi omvandlas till effekt och därefter till resistans. |
| 8.460 | Åtgärdad | Massan omvandlas till kg. Värmebehov och värmareffekt förklaras före tidsberäkningen. |
| 8.461 | Åtgärdad | Både fram- och återledare räknas med. Radie och area förklaras. Kostnadskortet använder sina givna 18,5 W. |
| 8.462 | Åtgärdad | Uppvärmning till 0 °C och smältning är två separata energibidrag. Ledtråden till b beskriver dessa steg. |
| 8.463 | Åtgärdad | Facit visar hur önskad effekt bestämmer resistansen och hur trådens area sedan ger längden. |
| 8.528 | Åtgärdad | Märkeffekter skiljs från faktiska effekter. Båda lampornas resistanser och gemensamma ström visas. |
| 8.581 | Åtgärdad | Facit kopplar instrumentens mätvärden till rätt storheter i effektsambandet. |
| 8.583 | Åtgärdad | Lampans ström löses ut ur effekten och den uppmätta spänningen. |
| 8.585 | Åtgärdad | Spänningen över och strömmen genom lampan används i en tydlig effektberäkning. |
| 8.586 | Åtgärdad | Facit väljer effektsambandet med spänning och resistans direkt. |
| 8.587 | Åtgärdad | Strömmen omvandlas till ampere innan den kvadreras. |
| 8.588 | Åtgärdad | Resistansen omvandlas till ohm och slutsvaret från W till mW. |
| 8.589 | Åtgärdad | Strömmen skrivs i ampere före effektberäkningen och slutsvaret avrundas. |
| 8.591 | Åtgärdad | Milliampere omvandlas före insättningen i effektsambandet. |
| 8.592 | Åtgärdad | Lampans märkdata ger strömmen genom båda seriekomponenterna; därefter beräknas resistorns spänning. |
| 8.594 | Åtgärdad | Båda lampornas effekter finns nu i en tydlig, namngiven svarsrad. |
| 8.595 | Åtgärdad | Samma serieström används i lampans effektberäkning utan avrundade mellanled. |
| 8.596 | Åtgärdad | Facit motiverar vilken resistor som begränsar strömmen och kontrollerar även den andra. |
| 8.597 | Åtgärdad | Delspänningarna adderas innan strömmen beräknas från den sammanlagda effekten. |
| 8.598 | Åtgärdad | Två olika samband ger delspänningarna; de adderas med full precision. |
| 8.600 | Åtgärdad | Den komponent som har känd effekt och resistans ger strömmen. Båda efterfrågade spänningarna sammanfattas. |
| 8.601 | Åtgärdad | L₁ ger den gemensamma strömmen, som används för L₂:s effekt. |
| 8.602 | Åtgärdad | Lampans effekt och spänning ger strömmen genom resistorn. |
| 8.603 | Åtgärdad | Ledtråden hänvisar inte längre till två effekter när bara en är given. Resistorns effekt används med serieströmmen. |
| 8.605 | Åtgärdad | R₂ ger den gemensamma strömmen. Båda spänningarna finns i en namngiven svarsrad. |
| 8.606 | Åtgärdad | L₂ ger strömmen som används för att beräkna L₁:s effekt. |
| 8.607 | Åtgärdad | Facit förklarar att resistorns egna spännings- och effektvärden räcker. |
| 8.618 | Åtgärdad | Lampans märkström och resistorns återstående spänning bestäms före resistansen. |
| 8.658 | Åtgärdad | Båda effektlägena förklaras och sammanfattas. Större serieresistans ger lägre effekt vid samma spänning. |
| 8.659 | Åtgärdad | Rättningsmålet är nu oavrundat: 17,6776695… V. Både 17,7 och korrekt avrundade 17,68/17,678 godtas. Facit motiverar den begränsande resistorn. |
