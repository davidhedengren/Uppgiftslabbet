# AI-banken som kurs i Kunskapsgymmet (2026-11-11)

Användarbeslut 2026-11-11: AI-banken läggs in i Kunskapsgymmet som ämnet
**”Artificiell intelligens nivå 1”** och placeras ovanför Historia på startsidan.

## Kompatibilitet

Kunskapsgymmet visar bara uppgifter med `spel:true` och delkort som inte är
`spel:false` (`availableTasks` och `expandGameTask` i `index.html`).

| Område | Uppgifter | Delkort | E | C | A | Träningsnivå 1–2 |
|---|---|---|---|---|---|---|
| FIFO-kö och stack | 6 | 12 | 12 | 0 | 0 | 12 |
| Kön under sökningen | 9 | 19 | 18 | 1 | 0 | 18 |
| Bredden först (BFS) | 8 | 23 | 23 | 0 | 0 | 23 |
| Djupet först (DFS) | 10 | 33 | 26 | 7 | 0 | 26 |
| Prioritetsköer | 6 | 12 | 12 | 0 | 0 | 12 |
| g-, h- och f-värden | 12 | 30 | 22 | 6 | 2 | 22 |
| A*-sökning | 15 | 36 | 25 | 11 | 0 | 25 |
| Viktade vägar | 10 | 24 | 21 | 3 | 0 | 21 |
| Minimax | 19 | 52 | 48 | 4 | 0 | 48 |
| Alfa–beta-beskärning | 12 | 33 | 11 | 10 | 12 | 11 |
| **Totalt** | **107** | **274** | **218** | **42** | **14** | |

- Alla 107 spelbara uppgifter har formatet `flera_delar` med delkort som är
  antingen heltal (`numeriskt`, tolerans 0) eller flerval med ett rätt alternativ
  och en kommentar per alternativ. Ingen KaTeX och inga bildfiler; figurerna är inbäddad SVG.
- **95 äldre uppgifter (1.01–1.31, 2.01–2.34, 3.01–3.30) är manuella** (`spel:false`,
  `svarstyp: "manuell"`, `rättSvar: null`) och syns inte i Kunskapsgymmet. De finns
  kvar i Uppgiftslabbet för övningsblad. Att göra dem självrättande kräver ett
  omräknat facit per delkort och är ett eget arbete. Ändra inte `spel` utan att
  rättSvar har räknats fram och kontrollerats.

## Ändringar i Kunskapsgymmet

- `uppgifterai.js` och `strukturai.js` kopieras **oförändrade** från Uppgiftslabbet
  (master). `selectCourse` använder tomma standardvärden för `KAPNAMNAISPAR` och
  `GRUPPAI`, så strukturfilen behöver inga egna rader.
- `index.html`:
  - kursen `ai` (`code:"AI1"`, `subject:"Artificiell intelligens"`, plommonfärgat tema
    `#A63D80`/`#E58AC6`);
  - `COURSE_ORDER` med `"ai"` före `"hist"`;
  - `UTAN_LARARVY = {hist, ai}` ersätter fyra jämförelser `id!=="hist"` i lärarvyn,
    eftersom gruppkursfunktionerna i databasen bara godtar matematik och fysik;
  - symbolraden visar bara minustecken för AI;
  - titel, metatexter och noscript nämner AI. `BANK_VERSION` = `2026-11-11-ai1`.
- `sql/2026-11-11-ai1.sql`: lägger till `'ai'` i kurslistorna i
  `kg_private.uppdragsbok_delta` och `public.kg_skicka_onskemal`. **Den ska köras i
  Supabase innan index.html publiceras.** Annars avvisas profilsparningar
  (`uppdragsbok_delta`) i upp till en vecka efter ett dagsuppdrag i AI.

## Kontroller

- `tools/ai1-kurs-2026-11-11.browser.cjs` (Kunskapsgymmet, i Playwright mot en lokal server):
  startsidans ordning (Matematik, Fysik, Artificiell intelligens, Historia), att
  alla 107 uppgifter syns i kursens tio kort, och 760 rättningar på 274 delkort.
  Rätt svar godkänns och fel svar underkänns. Negativa svar godkänns med både −
  och -, och varje felaktigt alternativ underkänns. Ledtråd och facit visas utan
  sidledsrullning i 390 och 1280 px. Inga sidfel.
- `tools/kapitel-blandat.browser.cjs` med `REVIEW_COURSE=ai`: blandade
  kapitelpass för alla tre kapitel utan fynd.
- Kunskapsgymmets enhetstester: 491 godkända och 16 underkända, samma 16 som före ändringen.
