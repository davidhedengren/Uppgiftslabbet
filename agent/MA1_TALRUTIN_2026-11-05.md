# Ma1: vanlig bråkräkning och enkel procent, 5 november 2026

Användaren vill uttryckligen ha mängdträning utan problemlösningstwister:
vanliga a), b), c) med bråktal samt delen, andelen och det hela.

## Levererat innehåll

36 nya huvuduppgifter med tre delar vardera = **108 självständiga träningskort**.
Samtliga finns på spåren 1a, 1b och 1c. Inga befintliga uppgifter ändras.

| ID (alla inkluderade) | Område och innehåll | Antal kort |
|---|---|---:|
| 0.1266, 0.1267, 0.1268, 0.1269, 0.1270, 0.1271 | Bråkräkning: addition, lika/olika nämnare, heltal och bråk | 18 |
| 0.1272, 0.1273, 0.1274, 0.1275, 0.1276, 0.1277 | Bråkräkning: subtraktion, lika/olika nämnare, heltal och bråk | 18 |
| 0.1278, 0.1279, 0.1280, 0.1281, 0.1282, 0.1283 | Bråkräkning: multiplikation, förkortning, heltal och bråk | 18 |
| 0.1284, 0.1285, 0.1286, 0.1287, 0.1288, 0.1289 | Bråkräkning: division med bråk eller heltal | 18 |
| 0.1290, 0.1291, 0.1292, 0.1293 | Andelar: beräkna delen när procentsatsen och det hela är kända | 12 |
| 0.1294, 0.1295, 0.1296, 0.1297 | Andelar: beräkna andelen i procent | 12 |
| 0.1298, 0.1299, 0.1300, 0.1301 | Andelar: beräkna det hela när delen och procentsatsen är kända | 12 |

## Pedagogiska beslut

- Alla är E/procedur. 36 kort är nivå 1, 72 kort nivå 2. Flera räknesteg
  gör inte en vanlig beräkning till C-nivå.
- Samma metod får avsiktligt återkomma: denna beställning gäller uttryckligen
  mängdträning. Variation finns i operation, nämnare, behov av förlängning/
  förkortning, heltal tillsammans med bråk och vad som söks i procentuppgiften.
  Lägg inte till textproblem eller extra villkor för att tysta likhetsheuristik.
- Bråkkorten tränar just räknesätten med bråk; miniräknare och GeoGebra är
  därför avstängda på både huvuduppgift och delkort. Detta är ett motiverat
  undantag från den generella räknarpolicyn. Procentsatserna tränar sambandet
  mellan del/andel/helhet och tillåter miniräknare. Inga digitala funktioner behövs.
- Inga dekorativa figurer: en bild behövs inte för att förstå dessa rena
  talberäkningar. Frågor och facit har i stället tydliga matematiska uttryck.
- Bråkfrågorna anger exakt svar. Likvärdiga bråk och exakta decimaler godtas;
  det finns inget dolt krav på en viss typografisk bråkform. Facit förkortar.
- Procentandelar använder numeriskt svar med enheten `%`, vilket godtar
  exempelvis både `25` och `25%`, men inte `2500%`. Nya kort använder inte
  det äldre breda procentformatets automatiska faktor-100-jämförelse.
- Varje del har egen fråga, ledtråd, regel, beräkning och svarsrad enligt
  FACITMALL. Huvudfacit visar a), b), c); delkortets facit visar bara sin del.
- Befintliga områden/familjer används: `brakrakning`/Räkna med bråk och
  `andelar`/Andel i procent respektive Beräkningar när procentsatsen är känd.

## Verifiering

- `tools/ma1-talrutin-2026-11-05.test.py` läser bankens faktiska frågor och
  verifierar svaren oberoende av byggaren med exakt Sympy-aritmetik.
  Alla **248 numeriska likhetskedjor i delfaciten** kontrolleras separat.
- Kunskapsgymmets `tools/ma1-talrutin-2026-11-05.test.js` använder verkliga
  `expandGameTask`, `svarsPlan` och rättningsfunktioner. Alla 108 kort har
  ett automatiskt rättat fält. Rätt svar, alternativa bråknotationer,
  procent med/utan tecken, felaktiga värden och fel enhet är provade.
- 144 presentationer (36 huvuduppgifter + 108 delkort), inklusive fråga,
  ledtråd och facit, renderade med KaTeX och båda apparnas CSS i mobilbredd
  390 px och datorbredd 1200 px. Inga KaTeX-fel eller överflödande
  facitrader. Representativa skärmbilder har även inspekterats visuellt.
- Riktad bankvalidator: 0 ERROR, 0 WARNING, 6 INFO om liknande textmallar.
  Likheten är avsiktlig och pedagogiskt motiverad av beställningen ovan.
- Syntax, diffkontroll, unika ID:n, befintliga uppgifter oförändrade och
  identiska bankkopior kontrolleras inför leverans.

## Granskningsutfall

Alla granskade nya uppgifter är listade ovan. Åtgärdade rapporterade fel:
inga i denna omgång. Granskad – inget fel av äldre rapporter: inga.
Ingen rapportstatus ändras i appen.

Förslag på återkoppling till önskemålet:
”Nu finns 36 nya rutinuppgifter med a), b), c), totalt 108 beräkningar,
inom vanlig bråkräkning och enkel procent. Varje del har ledtråd,
stegvis facit och självrättning.”
