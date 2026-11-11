# AI-banken: oinformerad och informerad sökning (2026-11-11)

Användarbeslut 2026-11-11: dela in sökavsnittet i **oinformerad sökning** (köer,
labyrinter och träd med BFS och DFS) och **informerad sökning** (heuristik, A*, girig
bäst först, f, g och h). Det fanns för få uppgifter om BFS och DFS i träd.

## Ny struktur (`strukturai.js`, skrivs av `tools/bygg-ai-omgruppering-2026-11-11.py`)

| Kapitel | Område (kort) | Delmoment | Uppgifter |
|---|---|---|---|
| 1 Oinformerad sökning | Köer och stackar (`ko_stack`) | Kö och stack steg för steg | 9 |
| | | Kö, stack och sökning i teorin | 8 |
| | Bredden först (BFS) (`bfs`) | BFS i labyrinter | 19 |
| | | BFS i träd och grafer | 14 |
| | Djupet först (DFS) (`dfs`) | DFS i labyrinter | 13 |
| | | DFS i träd och grafer | 13 |
| 2 Informerad sökning | Prioritetsköer (`prioritetsko`) | Uttag ur en prioritetskö | 7 |
| | | Prioritetskön i girig bäst först och A* | 7 |
| | Heuristik och f-värden (`astar_varden`) | Heuristiken h | 6 |
| | | g, h och f för en ruta | 15 |
| | Girig bäst först och A* (`astar_sokning`) | A* steg för steg | 14 |
| | | Girig bäst först jämfört med A* | 9 |
| | Viktade vägar (`viktade_vagar`) | Vägkostnad i labyrinter | 10 |
| | | Billigaste väg i grafer | 9 |
| 3 Spelträd och beskärning | Minimax, Alfa–beta-beskärning | oförändrat | |

- Kortet ”Kön under sökningen” (`ko_sokning`) är borttaget. Dess 17 uppgifter hör nu till
  BFS eller DFS efter algoritm (1.58 om oinformerad sökning till Köer och stackar).
  Teorifrågorna 1.55, 1.56 och 1.60 flyttades från BFS/DFS till Köer och stackar.
- Tidigare hade varje uppgift ett eget delmoment. Nu har varje kort två delmoment
  (strukturregeln: 2–5 delmoment per kort). Delmomenten med 6–7 uppgifter fylls på senare.
- Område-ID:n för kapitel 2 är oförändrade; bara namnen ändrades. Gamla värden finns i
  `omrTidigare` (20 uppgifter) och `familjTidigare`, så att Kunskapsgymmets
  `migreraFamiljer()` flyttar elevernas resultat.
- Kapitel 3 har fortfarande ett delmoment per uppgift. Det ingick inte i beslutet.

## Tolv nya uppgifter (1.65–1.76, `tools/bygg-ai-pafyllnad7-2026-11-11.py`)

BFS i träd och grafer: 1.65 nivåer och väg i ett sökträd, 1.66 kön när målet läggs in,
1.67 graf med slingor, 1.68 tunnelbanekarta (färst hållplatser är inte kortast tid),
1.69 två mål på olika djup (BFS och DFS hittar olika mål), 1.70 mappar på en dator.

DFS i träd och grafer: 1.71 djupt träd med backning, 1.72 stacken steg för steg,
1.73 graf med slingor (DFS hittar en omväg), 1.74 robotens beslutsträd, 1.75 DFS går
snabbare än BFS när målet ligger djupt i första grenen, 1.76 barnens ordning avgör.

- Svarsformer: antal, ordningsföljd och väg (`namnordning`) samt flerval med en
  kommentar per alternativ. Uppgiftstexten `t` saknar svarsinstruktioner; parentesen
  står bara i delkortet. Alternativ är aldrig ett ensamt nodnamn (”Noden B”, inte ”B”),
  eftersom det krockar med A–D på papper.
- Nivåer: 33 delkort, 27 E och 6 C: resonemang i 1.68c, 1.73c, 1.75c och 1.76c, den
  långa BFS-ordningen i 1.65b (11 uttag) och BFS över hela nivå 2 i 1.75b.
- Facit och ledtrådar har renderats och lästs igenom i Kunskapsgymmet (390 px).
  Två dubbla svarsinstruktioner (1.66a, 1.72a) rättades.

## Kontroller

- `tools/ai-pafyllnad7-2026-11-11.test.js`: strukturen, egna BFS- och DFS-simuleringar
  för alla nya svar, figurernas kanter och noder samt validatorn.
- Äldre tester räknar områden med `omrTidigare || omr`. Nivåtestet räknar inte längre
  `ko_sokning`.
- Byggkedjan ger identiska filer från den committade versionen. De äldre skripten
  `bygg-ai-pafyllnad` och `bygg-ai-pafyllnad3` tål nu Kunskapsgymmets svarsinstruktion
  i delkortens frågor vid omkörning.
- Kunskapsgymmet: `tools/ai1-kurs-2026-11-11.browser.cjs` (569 delkort, 1 809
  rättningskontroller, inga fel) och `tools/kapitel-blandat.browser.cjs` med
  `REVIEW_COURSE=ai` (inga fynd).
