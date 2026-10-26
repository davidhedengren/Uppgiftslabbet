# Integraler, areor och funktionsmedelvärden – 2026-10-26

**29 huvuduppgifter manuellt granskade, samtliga förbättrade. Granskad – inget fel: inga.** 3.84 har nu två egna delkort. Alla uppgifter finns kvar i Uppgiftslabbet. De tre resonemangsuppgifterna 3.210/53/75 förblir manuella; övriga ger 27 spelbara kort. Ingen rapportstatus eller kommentar har skickats till elever.

## Matematik och pedagogik

Alla integralvärden har beräknats oberoende med SymPy. Tidigare korta lösningar saknade ofta insättning av undre gräns, uppdelning av negativa/positiva områden eller division med intervallängd. Samtliga har nu individuella rubriker, relevanta mellanled och en tydlig svarsrad. Ledtrådarna är skrivna för respektive problem. Exempel på felaktiga äldre råd: likformighet/volym i 3.12/51/53, absolutbelopp i 3.50/102/103 och optimering i 3.71/73. Motsvarande metodval har kontrollerats i alla 29, alltså fler än fem analoger per återkommande mönster.

3.49/51/103 och 3.84b saknar exakthetskrav och får numeriska referenser med full precision. Bråk och korrekta avrundningar ska godtas. 3.22/206/208/224/288 har uttryckliga exakthetskrav; dessa behålls. 3.288 hade felaktigt en decimaltolerans trots ordet exakt. 3.350:s referens är hela 20+8/π, inte redan avrundade 22,5; halv decimalenhets tolerans behålls.

3.50/102/103 kan bedömas automatiskt och har fått numerisk självrättning. 3.84:s nästlade skärningspunkter och area delas i två kort. Skärningspunkterna får skrivas i valfri ordning, men båda behövs. Delfacit läcker inte nästa svar. Gemensam inledning/figur och delarnas egna frågor finns för träningskedjan. Frågefigurens etikett (2,4), som gav bort svaret på a, har tagits bort.

## Nivåer, verktyg och figurer

Rutinuppgifterna 3.49/50/71/219/73/224/103/348 ligger på nivå 2. Parameteruppgifterna 3.104/285 blir nivå 3; 3.288 kräver skärningsanalys och en potensintegral och blir också nivå 3. 3.51 samordnas till C/nivå 3. Temperaturmodellen 3.350 behåller nivå 3 och får konsekvent C-metadata. 3.84:s huvuduppgift behåller C/nivå 3; de två vägledda delarna är nivå 2. Övriga nivåer bevaras efter granskning.

Miniräknare tillåts i alla 29: vanlig aritmetik tar inte bort integrationen eller tolkningen. GeoGebra krävs inte för dessa symboliska metoder. I 3.53 och 3.75 är det digitala resultatet redan givet och det är tolkningen som prövas.

Sju nya SVG: 3.51/70/80/53/103/288/350. Kurvor, skalor och skuggade områden är koordinatkontrollerade, och samtliga befintliga och nya figurer granskas i webbläsaren. Figuren hjälper läsaren se vilket område som avses utan att skriva ut arean.

## Alla granskade och åtgärdade med kommentarsförslag

| ID | Status | Kommentar |
|---|---|---|
| #3.12 | Åtgärdad | Facit härleder nollställena, areauttrycket a³/6 och parametern. Den irrelevanta geometriledtråden ersätts. |
| #3.22 | Åtgärdad | Facit visar båda gränsvärdena och varför den negativa integralen ger en positiv area. Exakt bråksvar behålls. |
| #3.28 | Åtgärdad | Facit visar trapetsens båda höjder och bredd samt en kontroll med integral. |
| #3.206 | Åtgärdad | Facit visar den primitiva funktionen och insättning av båda gränserna. Exakthetskravet behålls. |
| #3.208 | Åtgärdad | Integralen beräknas före division med intervallets längd. Det exakta svaret är 64/3. |
| #3.210 | Åtgärdad | Facit visar den positiva roten och bevisar unikheten med strikt positiv derivata. Motiveringen bedöms fortsatt manuellt. |
| #3.49 | Åtgärdad | Facit visar symmetrin och halva arean. Bråk och korrekta decimalavrundningar godtas eftersom frågan inte kräver exakt svar. Nivå 2. |
| #3.50 | Åtgärdad | Den felaktiga absolutbeloppsledtråden ersätts. Facit skiljer funktionsmedelvärde från mittpunktens värde. Numeriskt självrättande; nivå 2. |
| #3.51 | Åtgärdad | Ny figur och full beräkning av skärningsgränser och övre minus undre kurva. Både 9/2 och 4,5 godtas. C/nivå 3. |
| #3.70 | Åtgärdad | Ny figur. Facit beräknar axelskärningarna och triangelarean. |
| #3.71 | Åtgärdad | Felaktig optimeringsledtråd ersätts. Båda gränsvärdena och subtraktionen av ett negativt tal visas. Nivå 2. |
| #3.219 | Åtgärdad | Facit beräknar integralen och dividerar med rätt intervallängd. Rutinuppgift, nivå 2. |
| #3.73 | Åtgärdad | Den irrelevanta deriveringsledtråden ersätts. Villkoret a positivt används för att välja rot. E/nivå 2. |
| #3.80 | Åtgärdad | Ny figur visar de tre delområdena. Facit beräknar mittarean och de yttre areorna separat innan addition. |
| #3.224 | Åtgärdad | Facit visar integralekvationen och väljer den positiva exakta roten. E/nivå 2. |
| #3.53 | Åtgärdad | Ny figur och ett geometriskt tolkningsfacit. Det givna digitala integralvärdet behöver inte beräknas igen. |
| #3.75 | Åtgärdad | Facit förklarar tidpunkt, minustecken och °C/min och skiljer momentan hastighet från total temperaturändring. |
| #3.84 | Åtgärdad | Två delkort med egna facit och ledtrådar. Två skärningspunkter godtas i valfri ordning; arean får eget numeriskt fält. En koordinatetikett som avslöjade svaret är borttagen ur figuren. |
| #3.102 | Åtgärdad | Felaktig absolutbeloppsledtråd ersätts av linjär medelvärdesmetod och integralkontroll. Numeriskt självrättande. |
| #3.103 | Åtgärdad | Ny figur och relevant ledtråd. Facit integrerar övre minus undre funktion. Självrättningen godtar 1/6 och korrekt decimalavrundning; nivå 2. |
| #3.104 | Åtgärdad | Facit härleder gränserna och k³/6 före parameterekvationen. Nivå 3. |
| #3.285 | Åtgärdad | Facit visar att både integralgräns och intervallängd beror på a. Nivå 3. |
| #3.288 | Åtgärdad | Ny figur och full lösning med kontroll av kvadreringen. Exakt bråkformat ersätter decimaltolerans i en fråga som uttryckligen kräver exakt svar. Nivå 3. |
| #3.347 | Åtgärdad | Facit visar e^(ln 3) och e⁰ separat innan subtraktion. |
| #3.348 | Åtgärdad | Facit kopplar positiv hastighet till sträcka och visar integral, gränser och enhet. Nivå 2. |
| #3.349 | Åtgärdad | Facit visar varför integralen ger area och hanterar båda cosinusvärdenas tecken. |
| #3.350 | Åtgärdad | Ny temperaturgraf. Facit visar kedjefaktor, båda gränsvärdena och division med 12. Rättningen utgår från oavrundade 20+8/π. C/nivå 3. |
| #3.351 | Åtgärdad | Facit visar varje trapets från tabellen och deras summa. Resultatet betecknas approximation. |
| #3.352 | Åtgärdad | Facit visar den primitiva funktionen och de exakta logaritmvärdena. |

## Kontroll och reproduktion

- `tools/matf1-area-facit-2026-10-26.test.py`: oberoende integralberäkningar för alla 29, exakta/numeriska referenser, metadata och sju SVG-geometrier.
- Konsumentens `tools/matf1-area-facit-2026-10-26.cases.json` och befintlig browserharness: rätta/felaktiga uttryck, avrundningar, enheter och skärningspunkter i båda ordningarna.
- Chromium: 216 rättningsfall, 60 elevvyer och 62 lärarvyer godkända utan JavaScript-, LaTeX- eller breddfel. Mobil och dator, 390/1280 px. Alla 13 figurvisningar (inklusive delkortens gemensamma figur) kontrollerade. Långa matematikrader har delats efter första kontrollen.
- Helbanksvalidatorn: Matf1 har 0 ERROR. Befintliga 1479 ERROR i andra banker kvarstår och omfattas inte av denna områdesrunda.
- Byggare: `tools/revidera-matf1-area-facit-2026-10-26.py` och `tools/matf1-area-figurer-2026-10-26.py`. Revisionen är idempotent. Kör den efter äldre byggare så att tidigare generiska facit inte återinförs.
