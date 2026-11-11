# AI: UCS borttaget och 20 nya uppgifter, 11 november 2026

## Användarbeslut

UCS ingår inte i kursen. Informerad sökning tränas bara med **girig bäst först**
och **A\***. Det gäller uppgiftstext, alternativ, facit, ledtrådar och områdesnamn.

## UCS borttaget

| ID | Före | Efter |
|---|---|---|
| 2.03 | Girig bäst först jämfört med UCS | Girig bäst först jämfört med A* i samma labyrint. Girig bäst först tar den dyra övre vägen (11), A* den billiga vägen runt väggarna (7). Facit visar f = g + h. |
| 2.14 | UCS, girig bäst först och A* väljer | a) Bestäm f = g + h, b) girig bäst först väljer T, c) A* väljer Q. Ny familj: ”Girig bäst först och A* väljer olika”. |
| 2.20 | ”Grafen söks igenom med UCS” | Billigaste väg i en graf utan algoritmnamn. Påståendet om UCS är ersatt av ”Det billigaste sättet att komma till B går via A” (rätt). Svaret är nu B och D. |
| 2.21 | UCS steg för steg | A* steg för steg i en graf med h-värden vid noderna (konsekvent h). Tabell med g, h och f: S 5, A 5, B 6, D 6, M 6. Ny del d: C läggs in men tas aldrig ut (f = 8). |
| område | ”Viktade vägar och UCS” | ”Viktade vägar” (`strukturai.js`, nyckeln `viktade_vagar` oförändrad). |

Inga andra uppgifter nämnde UCS. Test: ingen uppgift och inget områdesnamn får
innehålla UCS eller Dijkstra.

## 20 nya uppgifter (56 deluppgifter)

| Område | ID | Innehåll | Verifierat svar |
|---|---|---|---|
| FIFO-kö och stack | 1.20 | Kö eller stack i vardagen (kassakö, ångra-knapp, skrivarkö, tallrikshög) | FIFO, stack, FIFO, stack |
| | 1.21 | Samma steg med kö och stack i en tabell | Ut: P, Q respektive Q, S |
| Kön under sökningen | 1.22 | Hitta felet i en BFS-kötabell (barnen lagda först) | Fel efter A; F som sjätte nod efter S |
| | 1.23 | BFS i en graf med slinga | S, A, B, C, G; C läggs in en gång, av A |
| BFS | 1.24 | BFS i 5 × 5 | A1, A2, B1, B2, C1, C2; 8 steg; 18 uttag |
| | 1.25 | Start mitt i labyrinten (nivå 1) | B3, C4, C2; B3; 4 steg |
| DFS | 1.26 | DFS och BFS i samma träd | DFS 8 noder, BFS 6 |
| | 1.27 | DFS i en liten labyrint (nivå 1) | B2 tredje; A1 → A2 → B2 → C2 → C3 |
| Prioritetsköer | 2.23 | Lika värden avgörs av inläggningsordningen | P, S, M, K; med alfabetet M först |
| | 2.24 | Kö, stack och prioritetskö med samma noder, och vilken A* använder | A, C, B; prioritetskö |
| g-, h- och f-värden | 2.25 | f med lera | g = 4, f = 7 |
| | 2.26 | Hitta felet i Elins f-tabell (h räknat runt väggen) | h för P; rätt f = 4 |
| A*-sökning | 2.27 | Girig bäst först och A* på is | Girig 13, A* 7; A* tar D2 före C1 |
| | 2.28 | Öppna listan när målet tas ut | B1 och B3 kvar med f = 5; målet har lägst h |
| Viktade vägar | 2.29 | Billigaste vägen genom leran | 6; övre vägen 8 |
| | 2.30 | Girig bäst först och A* i en graf med h | Girig S → A → M (11), A* S → B → C → M (7) |
| Minimax | 3.11 | Ett löv ändras | 5 via B; fortfarande B; 7 |
| | 3.12 | Vägen genom trädet vid bästa spel | R → B → E → lövet 5 (L6) |
| Alfa–beta | 3.13 | Beskärning med MIN i roten | β = 5; L4 och L5 beskärs; roten 5 |
| | 3.14 | Vad beskärning betyder | 3 löv; samma rotvärde, ordningen spelar roll |

Nivåer: 4 uppgifter på nivå 1, 8 på nivå 2 och 8 på nivå 3. Banken har nu 71
uppgifter, med 6–8 i varje område.

Nya frågeformer i denna omgång: hitta felet i en elevs tabell (1.22, 2.26),
graf med slinga (1.23), vardagsexempel (1.20), regeln för lika värden ändras
(2.23), öppna listan när målet tas ut (2.28), ett löv ändras (3.11) och vägen
genom trädet vid bästa spel (3.12).

Ett sökresultat som påverkade uppgiftsvalet: i små rutnät där varje steg
kostar 1 hittade girig bäst först nästan alltid en lika kort väg som A*
(slumpsökning bland 200 000 labyrinter). Skillnaden mellan girig bäst först
och A* visas därför med terräng och kantkostnader (2.03, 2.27, 2.30) i stället
för med väggar.

## Kontroll

- `tools/bygg-ai-pafyllnad-2026-11-11.py` (UCS-ändringarna) och
  `tools/bygg-ai-pafyllnad2-2026-11-11.py` (nya uppgifter). Båda är idempotenta
  och körs i den ordningen.
- `tools/ai_sokalgoritmer.py` har fått `greedy`, `astar_graph` och
  `greedy_graph`. `tools/ai_figurer.py` kan visa h-värden vid grafernas noder.
- `tools/ai-pafyllnad2-2026-11-11.test.js` kontrollerar alla nya svar med egna
  simuleringar i JavaScript, bland annat girig bäst först och A* i rutnät och
  grafer, och att h i 2.30 är konsekvent.
- Resultat: 49/49 tester godkända. Validatorn hittar inga nya fynd.
- Webbläsarprov med appens CSS: alla 20 nya och de fyra omskrivna uppgifterna
  med facit och ledtrådar (900 px), utvalda även i 390 px. Inga JS-fel och inget
  horisontellt överflöd. Facit och ledtrådar har lästs igenom. Granskningen är gjord.
