# AI-banken: mängdträning (2026-11-12)

Användarbeslut 2026-11-12: ”Fortsätt fylla på banken med bra uppgifter. Det är bra med lite
mängdträning också, så det behöver inte vara helt olika, utan variera labyrinter/träd och
siffror.”

## 44 nya uppgifter (`tools/bygg-ai-mangdtraning-2026-11-12.py`)

| Delmoment | Uppgifter | Mall |
|---|---|---|
| Kö och stack steg för steg | 1.77–1.82 | kö eller stack i en bild och 5–6 steg; uttagsordning och vad som ligger först/överst |
| BFS i labyrinter | 1.83–1.86 | `bfs_task`: k:e uttaget, rutor på avstånd n, vägens längd, antal uttag |
| DFS i labyrinter | 1.87–1.90 | `dfs_task`: k:e besöket, antal besök, vägens längd, kortaste väg? |
| BFS i träd och grafer | 1.91–1.93 | uttagsordning, noder som aldrig tas ut, vägen |
| DFS i träd och grafer | 1.94–1.96 | besöksordning, noder som aldrig besöks, vägen |
| Uttag ur en prioritetskö | 2.88–2.91 | tvätteri, tandläkare, laddrobot och vårdcentral |
| g, h och f för en ruta | 2.92–2.95 | `ghf_task` med en ruta P som nås längs en rak väg (E-nivå) |
| A* steg för steg | 2.96–2.99 | f för grannarna till start, A*:s första uttag, vägens längd |
| Vägkostnad i labyrinter | 2.100–2.103 | kostnad för en given väg, billigaste vägen, är en kortaste väg också billigast? |
| Minimaxvärden och bästa drag | 3.62–3.65 | `mm_kg` i 3 × 2, 2 × 3 och tre nivåer, med negativa värden |
| Beskärningens idé | 3.66–3.69 | beskärning med stöd: A känd, L3 känt, behöver L4 undersökas? (C) |

- Labyrinter, träd och tal slumpas med fasta frön. Varje uppgift måste uppfylla villkor:
  nåbart mål, lagom lång väg, entydigt svar, unika lövvärden och inga lika värden utan regel.
  Om ett villkor inte är uppfyllt byts labyrinten eller trädet ut.
- Texterna skiljer sig genom sammanhang (robotdammsugare, mus, lager, drönare, mappar,
  brädspel, schackdator, fyra i rad …) och genom uppgiftens egna rutor, noder och tal. Utan
  sammanhang fick minimaxövningarna exakt samma text som 3.32, 3.33 och 3.37.
- Rubrikerna i facit beskriver vad som händer i just den uppgiften, med dess rutor och tal,
  till exempel ”Den översta noden tas ut vid varje uttag” med en tabell över stacken, eller
  ”Den billigaste vägen totalt kostar 7”.
- Pappersversionen (`t`) har inga svarsinstruktioner. Alternativ är aldrig en ensam bokstav.
- Nivåer: 122 av 130 delkort är E. C: 1.87d–1.90d (är DFS-vägen en kortaste väg? kräver jämförelse
  med BFS) och 3.66b–3.69b (beskärning med stöd, `OVERRIDE`).
- Facit, ledtrådar och figurer har lästs igenom i Kunskapsgymmet (390 px) för 1.78, 1.92,
  2.101 och 3.67. Rubrikerna i kostnadsuppgifterna gjordes mer specifika.

## Kort på träningsnivå 1–2 efter omgången (mål 50–100 per område)

| Område | Uppgifter | Nivå 1–2 | Nivå 3 | Nivå 4–5 |
|---|---|---|---|---|
| bfs | 40 | 97 | 13 | 0 |
| dfs | 33 | 82 | 21 | 0 |
| ko_stack | 23 | 50 | 1 | 0 |
| prioritetsko | 24 | 61 | 1 | 0 |
| astar_varden | 29 | 55 | 13 | 3 |
| astar_sokning | 27 | 47 | 25 | 0 |
| viktade_vagar | 23 | 48 | 13 | 0 |
| minimax | 34 | 90 | 5 | 1 |
| alfa_beta | 35 | 32 | 20 | 50 |

Nästa påfyllnad: A*-sökning och viktade vägar (under 50 på nivå 1–2), och alfa–beta på
E–C-nivå (rotvärden och beskärning med stöd).

## Kontroller

- `tools/ai-mangdtraning-2026-11-12.test.js` räknar om alla svar oberoende. Labyrinter
  (via `data-cell` och färg), sökträd (cirklar och linjer) och spelträd (trianglar, löv och
  linjer) läses ur figurerna som eleven ser. Köer och prioritetsköer läses ur texten. BFS,
  DFS, A*, billigaste väg, minimax och beskärningsbeslut räknas med egen kod.
- Nivåtestet räknar 3.66–3.69 som beskärning med stöd.
- Byggkedjan (med det nya skriptet före omgrupperingen) ger samma fil vid omkörning.
- Kunskapsgymmet: 728 delkort, 2 282 rättningskontroller, inga fel.
