# Granskning av delkedjor och facit 1 november 2026

## Generella fel och åtgärder

Kunskapsgymmets `kedjaLararversion` kunde välja gemensam inledning plus
`fraga` även när delkortet hade en egen `t` med andra givna värden. Därmed
försvann information eller ersattes med data från ett annat fall. Nu används
enbart den korta lärarversionen när korten faktiskt skapats av gemensam
inledning och fråga. Annars delas de verkliga korttexterna upp med bevarat
underlag. Dolda delar får inte ersättas av hela ursprungsuppgiften. Saknas
ett separat delfacit får huvudfacit inte visas som reserv för delkortet.

Visade bokstäver i en kedja är nu a), b), … för de delar som faktiskt är med.
Ursprungliga del-ID:n och etiketter för historik, resultat och felrapporter
behålls. Exempel: Fy1 8.58 c/d blir synligt a/b men lagras fortfarande som
8.58c/8.58d. Enstaka synliga kort behandlas som tidigare som fristående.

## Manuellt granskade exempel på tappad delinformation

Fy1 **3.197, 3.218, 5.66, 5.117, 5.405, 5.489, 5.513, 5.515, 6.469,
6.470, 7.139, 7.166, 7.167, 7.176 och 7.177**. Samtliga hade korta
likalydande frågor men olika givna situationer eller mätvärden i deltexterna.
Exempelvis måste 3.197 b innehålla 27,0→29,0 m/s på 5,0 s och c innehålla
27,0→23,0 m/s på 5,0 s. I 5.66 b verkar kraften i rörelseriktningen, inte
35° uppåt som i a. Dessa data bevaras nu genom appens allmänna rättning;
bankdata ändrades inte för dessa exempel.

## Individuellt rättade delfacit

| Uppgift | Ändring och matematisk kontroll |
|---|---|
| Ma4 2.117 a | \(a=f'(0)-f(0)=5-2=3\); facit räknar inte uttryckligen ut b. |
| Ma4 2.229 a | Addera \(a+b=8\) och \(a-b=12\): \(a=10\). Svaret b=−2 visas inte i a. |
| Ma4 2.101 a | Den korrekta derivatan härleds utan den tidigare separata meningen som direkt besvarade felanalysen i b. Faktorn \(2x\) syns ändå i den nödvändiga kedjeregeln. |
| Ma4 2.42 a och 2.77 a | Enbart derivatans tecken och efterfrågade växande/avtagande intervall. Det står inte längre vilka punkter som är max/min. |
| Ma4 2.158 a/b | a visar endast andraderivatan \(12x²-8\); b visar efterfrågade teckenintervall. Gränserna för intervallen är naturligtvis samma värden som efterfrågas i c. |
| Ma4 2.253 a/b | a visar endast växande intervall; b beräknar extrempunkternas x-värden 1 och 4 men namnger inte max/min. |
| Ma4 3.113 a | Visar skivornas area och integralen \(\pi\int_0^3x^4dx\), inte den färdigberäknade volymen i b. |
| Ma4 4.04 a | Visar produkten i polär form, inte kvoten från b. |
| Ma4 4.327 a | Identifierar regelbunden sexhörning utan arean från b. |
| Ma2 1.313 a | Två exempel på möjliga vikter är (1,8; 0,4) och (2,6; 0,3). Båda uppfyller \(l+8b=5\) och är inte b-delens entydiga par (1; 0,5). |
| Ma2 3.462 b | Hypotenusan beräknas som \(5\cdot36/12=15\) cm utan att i förväg räkna ut arean i c. |
| Fy1 3.80 b | Slutfarten \(v=2s/t=12\) m/s visas utan att först ange medelfarten som efterfrågas i c. |

Huvudfacit i Uppgiftslabbet och matematiska slutsvar är oförändrade. Ingen
miniräknar- eller GeoGebraflagga ändrades; verktygsvalen kontrollerades mot
respektive uppgift, med miniräknare tillåten där den redan behövs. I Ma4
4.04 är exakt polär beräkning med enkla givna vinklar möjlig utan digitalt
verktyg; befintliga flaggor behålls.

## Jämförelser och kvarstående avgränsning

Samtliga sju bankfiler inventerades maskinellt efter saknade delfacit,
identiska delfacit, delmarkörer, misstänkta svarsöverensstämmelser och
deltexter som ersätts av korta frågor. Genomlästa jämförelser utan ny ändring
omfattar bland annat Ma2 2.407, 2.714, 2.397, 2.414 och 2.425; Ma4 1.51,
1.70, 1.150, 2.76 och 4.133; Fy1 2.1, 3.148, 4.187, 4.208 och 5.91;
Ma3 1.02, 1.14 och 2.782. En siffra som även förekommer i en annan del är
inte i sig en felaktig facitläcka: den kan vara given information, ett
nödvändigt mellanled eller ett sammanfallande korrekt svar.

Vissa delar bygger matematiskt på varandra. I Ma4 2.158 identifierar b
gränserna för teckenintervallen som c frågar efter; i 2.101 innehåller en
tydlig kedjeregelberäkning den faktor eleven ska identifiera i b. Vidare kan
två separata frågor ha samma korrekta numeriska svar, exempelvis Fy1 3.148
och Ma2 4.322. Detta är inte löst genom att dölja nödvändiga mellanled eller
ändra talen utan vidare granskning. Fortsatt pedagogisk granskning behövs;
den maskinella inventeringen bevisar inte att varje delfacit är felfritt.

## Tester

- `kedjor-allabanker-2026-11-01.browser.cjs` kontrollerar att text och
  SVG/bilder från **8 659 synliga delkort i 3 144 kedjor** bevaras, både när
  en del är först och med tidigare visade delar. Detta är en strukturell
  kontroll, inte en matematisk granskning av alla kort.
- `delfacitkedjor-2026-11-01.browser.cjs` provar riktiga elevflöden i 390 och
  1 280 px, 15 särskilt undersökta uppgifter, facit efter a, saknade facit,
  dolda delar och visade respektive lagrade etiketter.
- Äldre `felrapporter-2026-10-26-flow.browser.cjs` passerar för tidigare
  kedjor, överhoppning/sparning, återupptagning, XP och självrättning.
- `delfacitgranskning-2026-11-01.test.js` kontrollerar matematiska värden och
  att de ändrade delfaciten inte innehåller de konstaterade facitläckorna.
- Vid fullständig körning har mastersviten 1 056 godkända av 1 099; 43
  SVG-tester kan inte köras med verktygets Windows-Chrome-inställning i denna
  miljö. Konsumentsviten har 304 godkända av 314; samma tio fall misslyckas på
  oförändrad basversion enligt föregående rapport.

Ingen rapportstatus eller kommentar har ändrats i produktionsdatabasen.
