# AI: varierade labyrinter och genomtänkta alternativ

## Uppdrag och omfattning

Tolv nya uppgifter med 25 deluppgifter. Användarens bilder inspirerar nästa
ruta från ett sökläge, markerade f-värden, två mål i sökträd, varierade spelträd
och terrängkostnader. Totalt finns nu 25 huvuduppgifter och 64 delar.

| ID | Innehåll | Verifierat resultat |
|---|---|---|
| 1.06 | BFS, 3 × 4 | 5 steg, 9 utforskade rutor |
| 1.07 | DFS, 5 × 6 | DFS 13 steg; kortaste vägen 9 |
| 1.08 | Onåbart mål, 4 × 6 | 11 besök; tom kö och ingen väg |
| 1.09 | Sökträd med två mål | BFS når D; stack-DFS når K |
| 2.06 | Markerat f, 5 × 6 | g=6, h=3, f=9 |
| 2.07 | Markerat f, 7 × 9, öppet svar | g=6, h=8, f=14 |
| 2.08 | Markerat f, 9 × 13 | g=13, h=9, f=22 |
| 2.09 | Utforskat sökläge, 7 × 9 | Girig väljer Q; A* väljer P |
| 2.10 | Is, backe och vanlig väg, 7 × 9 | Kostnader 19, 16 och 10 |
| 2.11 | Isväg som faktiskt lönar sig, 4 × 7 | Isväg 9; omväg 10 |
| 3.04 | MAX-rot, åtta löv | Rot 3; L7–L8 beskärs |
| 3.05 | MIN-rot, sexton löv | Rot 6; L8, L12, L13–L16 beskärs |

## Alternativ och självständiga delar

Blandning av öppna frågor, ett rätt alternativ och flera rätta alternativ.
Flersvarsfrågor säger uttryckligen ”Välj alla som stämmer”. Varje alternativ
har kommentar. Distraktorer prövar bland annat:

- antal rutor kontra antal steg,
- DFS-väg kontra kortaste väg,
- g kontra h kontra g+h och att start felaktigt räknas som ett steg,
- lägst h eller lägst g i stället för A*:s f,
- tom kö kontra evig sökning och nåbara kontra alla vita rutor,
- besöksordning kontra returnerad väg,
- bokstavsordning vid inläggning kontra uttagsordningen ur stack,
- kortast väg kontra billigast väg, och felregeln ”undvik alltid is”.

Main-texten innehåller synliga alternativlistor för lärarvy och export.
Delkort har strukturerade `alternativ` och `visaAlternativ`, medan `spelIntro`
bär alla gemensamma figurer/tabeller. Självrättning är fortsatt avstängd:
framtida integration med Kunskapsgymmet ska testa dess faktiska konsument.
Alla delar har egna facit, ledtrådar och verktygsmetadata. Räknare tillåts;
GeoGebra behövs inte. Inga tidigare uppgifter har fått ändrade svar.

## Viktiga tolkningsbeslut

2.09 är ett givet sökläge, inte ett påstående att både A* och girig sökning
skulle ha skapat samma tidigare sökordning. Hela öppna listan och dess kända
g/h-värden visas. Det är ett möjligt sökläge, verifierat genom att spela upp
en girig sökning. Starten ligger i den utforskade mängden men visas grön.

2.06–2.08 anger kortaste vägkostnad g för att markeringen ensam inte ska
behöva beskriva en tidigare sökning. Alla rörelsekostnader där är 1.
Terränguppgifterna anger kostnad per inträdd ruta, start 0 och mål 1.

3.04–3.05 har unika löv-ID:n så att upprepade lövvärden inte gör beskärningen
tvetydig. α och β avser noden där avbrottet sker, efter gränsuppdateringen.

## Verifiering

33/33 tester godkända: befintlig AI-regression, nya oberoende BFS/DFS/UCS-,
prioritets- och alfa–beta-beräkningar samt bankvalidatorns egna regressioner.
Modeller och förväntade värden: `tools/ai-expansion-2026-11-11.cases.json`.
Browserprov: alla 25 kort, 64 delfacit och 22 figurer renderade; inga JS- eller
KaTeX-fel. Alternativlistor och fyra representativa nya figurer visuellt
kontrollerade. Mobilkontroll: den breda figuren rullar inom sin behållare.

AI-validator: inga ERROR. Två manuellt bedömda likhetsfynd är avsiktliga:
WARNING EXACT_TEXT_DUPLICATE för 3.04/3.05 (olika figurer, antal nivåer och
rotspelare); INFO VERY_SIMILAR_TEXT för 2.06/2.08 (olika labyrinter och storlek).
De godkänns specifikt i testet; inga andra fynd undantas.

Ändrade filer: uppgifterai.js, befintligt AI-test (avgränsat till ursprungliga
13 uppgifter), nytt expansionstest och cases.json, denna rapport och loggar.
