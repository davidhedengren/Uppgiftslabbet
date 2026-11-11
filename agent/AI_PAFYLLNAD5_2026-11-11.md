# AI: teorifrågor och beräkningar i minimax och sökning, 11 november 2026

Användarens önskemål: fler uppgifter inom minimax, oinformerad sökning och
informerad sökning, gärna teorifrågor med flerval. Alfa–beta ingår inte i
den här omgången.

## Teoriuppgifter (16 st, 38 flervalsfrågor)

| Område | ID | Innehåll |
|---|---|---|
| BFS | 1.55 | Datastruktur, vilken väg BFS hittar, i vilken ordning rutorna tas ut |
| DFS | 1.56, 1.60 | Stack, kortaste väg?, återvändsgränder; grannordningens betydelse för DFS och BFS |
| Kön under sökningen | 1.57, 1.58 | Varför upptäckta rutor inte läggs in igen, onåbart mål; oinformerad sökning |
| Kö och stack | 1.59 | Stack i stället för kö ger DFS |
| g, h och f | 2.67, 2.68, 2.71 | g, h och f i ord; Manhattanavståndet (med figur); när h är en bra heuristik |
| A*-sökning | 2.69, 2.70 | Girig bäst först eller A*; vad som gör en sökning informerad |
| Prioritetsköer | 2.72 | Prioritetskön i A* |
| Viktade vägar | 2.73 | Kortaste eller billigaste väg, BFS och kostnader |
| Minimax | 3.43–3.46 | MAX, MIN och lövens tal (med träd); noder, kanter och trädets storlek; rotvärdet som garanti; varför inte det högsta lövet |

Varje fel alternativ är en vanlig feltanke, till exempel att stack ger BFS, att
h räknar väggar, att girig bäst först använder f eller att MAX kan räkna med det
högsta lövet. Kommentaren förklarar felet. Teorifrågor om definitioner och
datastrukturer saknar figur, eftersom en figur inte tillför något där.
Manhattanavståndet och minimaxfrågorna har figur.

Nivåer enligt AI_NIVAINDELNING.md: att känna igen begrepp är E.
Förklaringar av varför är C (1.57a, 1.60b, 2.68c, 2.69c, 3.45a, 3.46b). Att
värdera heuristiken, alltså att h inte får överskatta och att Manhattanavståndet
inte gör det, är A (2.71). Undantagen står i `OVERRIDE` i nivåskriptet.

## Beräkningsuppgifter (12 st)

1.61 (BFS 4 × 6), 1.62 och 1.63 (DFS, kortaste väg ja respektive nej), 1.64
(vem lägger in målet), 2.74 (A*, sjätte uttaget), 2.75 (girig bäst först bland
fyra grannar), 2.76 (samma h, olika g), 2.77 (direkt kant eller omväg), 3.47 och
3.48 (minimax i tre nivåer, negativa värden), 3.49 (vägen till lövet).

## Fördelning och kontroll

Banken har nu 190 uppgifter och 504 delkort: 364 E, 86 C och 54 A.

- Byggskript: `tools/bygg-ai-pafyllnad5-2026-11-11.py`. Det körs efter
  `…pafyllnad4…` och före nivåskriptet. Hela kedjan med åtta skript ger en identisk fil.
- Test: `tools/ai-pafyllnad5-2026-11-11.test.js` kontrollerar teorisvaren, nivåerna
  och omräknade beräkningssvar. 80/80 AI-tester godkända. Validatorn hittar inga
  nya fynd. 3.49 omformulerades för att inte likna 3.39.
- Webbläsarprov med appens CSS. Facit och ledtrådar har lästs igenom. Granskningen är gjord.
