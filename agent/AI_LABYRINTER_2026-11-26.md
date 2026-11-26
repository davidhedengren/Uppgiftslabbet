# AI-banken: labyrinter med riktiga väggar (2026-11-26)

Användaren: ”Det är lite för många labyrinter där som inte är labyrinter, alltså det är inga väggar. Gör om dessa
och lägg till fler uppgifter av typen 'Bestäm g(n) för rutan P', 'bestäm h(n) för rutan …' och 'bestäm f(n) för
rutan …'. Jag vill ha varierade labyrinter men liknande uppgifter.”

Byggskript: `tools/bygg-ai-labyrinter-2026-11-26.py` (torrkörning utan `--skriv`; kan köras om, och ersätter då uppgifterna på plats). Därefter körs som vanligt
`bygg-ai-omgruppering-2026-11-11.py`, `bygg-ai-efterbearbetning-2026-11-12.py` och `bygg-ai-nivaer-2026-11-11.py`.
Regressionstest: `tools/ai-labyrinter-2026-11-26.test.js`.

## 1. Ombyggda uppgifter (15)

Labyrinten saknade väggar (2.27, 2.29, 2.42, 2.44, 2.51, 2.53, 2.63, 2.108) eller hade en enda vägg i ett större
rutnät (1.104, 2.25, 2.28, 2.48, 2.55, 2.57, 2.75). De har fått nya labyrinter (4 × 4 till 6 × 7) med 4–10 väggar som tvingar fram
omvägar. Samma id, område, delmoment, förmågor, antal delkort, nivå, träningsnivå och poäng per delkort; frågorna är
desamma i sak, med nytt innehåll, facit, ledtrådar och flervalskommentarer. De två begreppsfrågorna (2.108c, 1.104c)
står kvar, med siffrorna i kommentarerna utbytta mot den nya labyrintens.

Kvar som förut: 1.105 och 1.106 (handlar om öppna rutnät, R · C uttag) och 3 × 3-rutnäten i 1.13 och 1.48.

## 2. Nya uppgifter 2.123–2.152 (30)

g(n), h(n) och f(n) för en markerad ruta: ”Bestäm g(n) för rutan P.”, ”Bestäm h(n) för rutan P.”, ”Bestäm f(n) för
rutan P.” (bokstaven varierar: P, Q, R, X). E-nivå, poäng 3/0/0, träningsnivå 2/1/1, delmoment ”g, h och f för en
ruta” i kortet Heuristik och f-värden. Labyrinterna är 4 × 4 till 6 × 7; 11 av dem har lera eller is, så att g(n)
blir en kostnad och inte bara ett antal steg. I nästan alla går den billigaste vägen till rutan runt väggar
eller genom terräng, så att g(n) skiljer sig från Manhattanavståndet från start. Varje uppgift har ett eget
sammanhang (lagerrobot, mus och ost, robotdammsugare, räddningsrobot …), så att ingen text upprepas (validatorns
EXACT_TEXT_DUPLICATE).

## 3. Övrigt

- 2.61 ”Bestäm f(n) = g(n) + h(P).” → ”Bestäm f(P) = g(P) + h(P).” och 2.120:s ledtråd ”Jämför f(n) = g(n) + h(M) …”
  → ”Jämför f(M) = g(M) + h(M) …” (nodens namn på båda sidor, enligt notationsbeslutet 2026-11-24).
- Kostnadstexten skrivs nu ”Det kostar 3 att gå in i en lerruta, 4 att gå in i en isruta och 1 att gå in i en vit
  ruta eller målet. Startrutan kostar inget.”
- Facitrubriken för den billigaste vägen säger vilka dyra rutor vägen går runt (”Den billigaste vägen går runt
  lerrutorna C6 och D7”).

## Kontroll

- `tools/ai-labyrinter-2026-11-26.test.js` läser varje labyrint ur figuren (väggar, terräng, start, mål och markerad
  ruta) och räknar om alla 127 delsvar oberoende av byggskriptet: billigaste väg (Dijkstra), BFS, girig bäst först
  och A* med regeln för lika värden, öppna listan och antal grannar. Testet kräver också minst tre väggar och en
  omväg i varje labyrint, varierade storlekar och unika texter.
- Äldre tester med de gamla labyrinterna inskrivna hänvisar nu till det nya testet (kommentar i varje test).
- Alla 20 AI-tester, `granska-uppgifter.js` (AI: 0 fel, 1 varning, 1 info som förut), `node --check`.
- Renderat och läst: 2.123, 2.126, 2.128, 2.29, 2.63, 2.27, 2.28, 2.57, 2.75, 1.104, 2.55, 2.48 och 2.42, med figur,
  facit och ledtråd.
