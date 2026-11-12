# AI-banken: granskning och åtgärder (2026-11-12)

Användaren frågade hur banken ser ut för mängdträning och för övningsblad, och bad sedan att
fem förbättringar görs i den föreslagna ordningen. Banken byggs ut till fler delar av ämnet
senare; just nu gäller arbetet sökning.

## 1. Facit i Kunskapsgymmet nämnde alternativen med fel bokstav

Delkortens facit listade kommentarerna som ”A: …, B: …”, men Kunskapsgymmet blandar
alternativen. I 270 delkort står nu själva alternativet i stället för bokstaven. Huvudfacit `s`,
som Uppgiftslabbet visar på papper, behåller bokstäverna, eftersom de där stämmer med A–D i `t`.
Görs i `tools/bygg-ai-efterbearbetning-2026-11-12.py`, som kontrollerar att varje kommentar hör
till rätt alternativ.

## 2. C- och A-uppgifter för prov, E-uppgifter i alfa–beta (`bygg-ai-pafyllnad9-2026-11-12.py`)

| Uppgift | Område | Nivå | Innehåll |
|---|---|---|---|
| 1.97 | Köer och stackar | C | vilka uttagsordningar en stack kan ge (C, A, B, D är omöjlig) |
| 1.98 | Köer och stackar | C | vilken struktur och barnordning som gav en viss sökordning |
| 1.99 | DFS | E/C + A | DFS-vägar med två grannordningar; vad gäller i alla labyrinter |
| 2.104 | Prioritetsköer | C | A*:s öppna lista när målet först får f = 8 och sedan f = 4 |
| 2.105 | Prioritetsköer | C | varför A* behöver en prioritetskö och kan behöva sänka f |
| 2.106 | Heuristik | E + A | tre heuristiker: vilken överskattar, vilken hjälper A* mest |
| 2.107 | Viktade vägar | E + A | för vilka heltal k vägen med kostnaden 2k är billigast (k ≤ 2) |
| 2.108 | Girig bäst först och A* | E + A | vad som gäller för girig bäst först i alla labyrinter |
| 3.70–3.72 | Alfa–beta | E | nodvärde, rotvärde och en begreppsfråga i små träd med beskärning |

A-delarna och begreppsfrågorna har motiverade undantag i nivåskriptets `OVERRIDE`.

## 3. Träningsnivå 1 i DFS och A*-sökning

Fyra uppgifter vardera på träningsnivå 1 (`bygg-ai-mangdtraning-2026-11-12.py`):

- DFS (1.100–1.103): antal grannar till start, första besöket och nästa besök från en given ruta.
  Rutan väljs så att nästa besök är en granne, inte ett steg efter backning.
- A* (2.109–2.112): h för start, f för en granne och vilken granne som har lägst f.
  Lägst f är alltid entydigt.

## 4. Ensamma bokstäver som alternativ

132 alternativ som bara var ett namn (”B”) skrivs nu ”Noden B”, eller ”Rutan P” när uppgiften
handlar om rutor (1.22a: ”Efter uttaget av A”). Ändringen görs i alternativ, rättSvar,
uppgiftstextens A–D-lista och svarsraderna, och i huvudfacit bara inom delens eget avsnitt.
Äldre tester tar bort prefixet innan de jämför med sina egna beräkningar. Prefixen
kontrolleras i det nya testet.

## 5. Fler terrängtyper i mängdträningen

2.113–2.116 kombinerar lera (3), is (4) och backe (5). Varje uppgift har en given väg med minst
två terrängtyper, den billigaste vägen och hur mycket den sparar.

## Läget efter åtgärderna (delkort)

| Område | Uppgifter | Nivå 1 | Nivå 1–2 | E | C | A |
|---|---|---|---|---|---|---|
| bfs | 40 | 23 | 97 | 97 | 13 | 0 |
| dfs | 38 | 20 | 94 | 94 | 23 | 1 |
| ko_stack | 25 | 44 | 50 | 50 | 7 | 0 |
| prioritetsko | 26 | 42 | 61 | 61 | 6 | 0 |
| astar_varden | 30 | 39 | 57 | 57 | 13 | 5 |
| astar_sokning | 32 | 28 | 61 | 61 | 25 | 1 |
| viktade_vagar | 28 | 30 | 62 | 62 | 13 | 1 |
| minimax | 34 | 28 | 90 | 90 | 5 | 1 |
| alfa_beta | 38 | 31 | 41 | 41 | 20 | 50 |

Totalt 291 uppgifter och 797 delkort: 613 E, 125 C och 59 A.

## Kontroller

- `tools/ai-granskning-2026-11-12.test.js`: punkt 1 och 4 i hela banken, oberoende omräkning
  av alla nya C-, A- och E-uppgifter samt nivåbalansen.
- `tools/ai-mangdtraning-2026-11-12.test.js` räknar om 1.100–1.103, 2.109–2.116 ur figurerna.
- Byggkedjan ger samma fil två gånger i rad. Validatorn hittar bara de två godkända fynden.
- Kunskapsgymmet: 797 delkort, 2 462 rättningskontroller, inga fel. Facit och figurer har
  lästs igenom i 390 px (bland annat 1.97b, 1.100c, 2.104b, 2.106d och 3.70c).
