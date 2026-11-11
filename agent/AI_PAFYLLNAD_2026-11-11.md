# AI: lärarkommentarer och 26 nya uppgifter, 11 november 2026

Uppdrag: åtgärda lärarkommentarerna i felrapporten ”Uppgiftslabbet 2026-11-11
09:31” (AI 1.01, 1.03 och 1.04), gör samma ändring i alla liknande uppgifter
och fyll på banken med fler uppgifter i samma stil i alla områden.

## Lärarkommentarerna

| ID | Kommentar | Åtgärd |
|---|---|---|
| 1.01 | Skriv ”Labyrinten söks igenom med BFS (ordning …)”, enhetligt i alla. | Alla labyrinter inleds nu med ”Labyrinten söks igenom med BFS/DFS/A*/UCS …”. Sökträd: ”Trädet söks igenom med …”, spelträd: ”Spelträdet söks igenom med …”. Minimaxträden 3.01–3.02 saknade inledning och har fått en. |
| 1.03 | Skriv tydligare vad som händer, t.ex. ”Noder läggs in och tas ut …”. | ”in A · in B · ut …” är ersatt av ”Noder läggs in och tas ut enligt följande: lägg in A, B och C → ta ut en nod → …”. Delfrågorna säger att stegen görs med en FIFO-kö respektive en stack. Samma ändring i 2.04 (prioritetskö). |
| 1.04 | ”Trädet söks igenom med BFS”, grön startnod, röd målnod, gör som i labyrinterna. Tabell med Tas ut/kön snyggt. | Ny inledning. Startnoden är grön och målnoden röd, med vit bokstav och färgförklaring Start/Mål. Den dubbla ringen runt målet är borttagen. Samma ändring i 1.05 och 1.09 (där målen tidigare var ljusröda och starten vit). Tabellerna har bankens stil (`class="data"`) och vänsterställda celler, och en ifylld startrad ”– S” ersätter texten ”Startkö: S”. |

Följdändringar för enhetlighet:

- 1.05 använder en stack, så kolumnen heter nu ”Stacken efter uttaget” och b-frågan
  ”kvar i stacken”.
- Huvudledtrådarna i 1.03, 1.04, 1.05, 2.04 och 2.05 var kopierade från
  labyrintuppgifterna (”Spara vilken ruta som först upptäckte …”) och är ersatta
  av ledtrådar som passar respektive uppgift.
- Alternativlistor i huvudtexten skrevs som `<ol type="A">`. Appen visar alla `<ol>`
  som a), b), c), vilket krockade med deluppgifternas bokstäver. De visas nu som
  **A.**, **B.**, … (`<p class="ul-alt">`), samma form som appens egen
  alternativvisning och som facitkommentarerna ”A:”, ”B:”.
  Det gäller 1.06–1.09 och 2.06–2.11.
- Alla tabeller i AI-banken har nu bankens tabellstil.

Inga svar har ändrats i de 25 tidigare uppgifterna.

## Nya uppgifter (26 st, 75 deluppgifter)

| Område | ID | Innehåll | Verifierat svar |
|---|---|---|---|
| FIFO-kö och stack | 1.10 | FIFO-kö som bild, fyra steg | K tas ut först; kvar P, R, S |
| | 1.11 | Stack som bild, flerval om stack/kö | B, Y, X; H överst; A och B stämmer |
| | 1.12 | Vilken struktur gav uttagen B, D, C, A? | Stack; FIFO hade gett A, B, C, D |
| Kön under sökningen | 1.13 | BFS-kö i en 3 × 3-labyrint, tabell | A1, A2, B1, A3, C1, B3, C2, C3; väg via A3 |
| | 1.14 | Fortsätt en påbörjad BFS-tabell | B härnäst; G och H kvar |
| BFS | 1.15 | Avstånd från start | C3 och D2 på 4 steg; 6 steg; A4 tas aldrig ut |
| | 1.16 | Två lika korta vägar, grannordningen | Övre vägen; 10 uttag; nedre vägen med ← ↓ → ↑ |
| DFS | 1.17 | Besökta rutor utanför vägen | B4 och A4 |
| | 1.18 | Två grannordningar | 8 respektive 6 steg |
| | 1.19 | Första återvändsgränden | A5; sedan C5; 6 rutor besöks aldrig |
| Prioritetsköer | 2.12 | Lika värden, alfabetisk ordning | L, N, K, M |
| | 2.13 | Bättre väg hittas (f sänks) | f = 6; B; sedan D |
| | 2.14 | UCS, girig bäst först och A* väljer olika | P, T, Q |
| g-, h- och f-värden | 2.15 | h för tre markerade rutor | 5, 3, 2; R lägst |
| | 2.16 | Lågt h men lång väg | h = 2, f = 4; 8 steg; B och D stämmer |
| A*-sökning | 2.17 | A* med lika f och en återvändsgränd | 11 besök; B2, A2, A3 utanför vägen |
| | 2.18 | Nästa uttag ur öppna listan | f 10, 9, 11, 9; L; sedan P |
| | 2.19 | A* jämfört med BFS | BFS 18, A* 8 uttag |
| Viktade vägar och UCS | 2.20 | Billigaste väg i en viktad graf | 8 via S, A, B, C, M |
| | 2.21 | UCS steg för steg med sänkt kostnad | S0, A1, B3, C3, D4, M6 |
| | 2.22 | Kostnaden för tre givna vägar | 10, 14; väg 2 (8) billigast |
| Minimax | 3.06 | MIN i roten | B = 5, R = 5, draget till B |
| | 3.07 | Ett okänt lövvärde x | A = 4; R = 7 vid x = 10; x ≥ 5 |
| | 3.08 | Ojämnt träd, negativa värden | C 4, D 3, E 2; A 1, B 2, R 2 |
| Alfa–beta | 3.09 | Tre MIN-noder | R = 5; L5, L6, L9 beskärs; 6 löv |
| | 3.10 | Ordningen avgör beskärningen | α = 6; omvänd ordning: 3 löv, ingen beskärning |

Träningsnivåer: 5 uppgifter på nivå 1, 10 på nivå 2 och 11 på nivå 3 (huvuduppgiftens
nivå är den högsta delens). Varje område har nu 4–6 uppgifter.

Variation: bilder av kö och stack, labyrinter i olika storlekar, sökträd,
viktade grafer, terräng med lera och spelträd med löv på olika djup. Frågetyperna är
tabeller att fylla i, öppna svar, ett rätt alternativ och flera rätta alternativ
(”Välj alla som stämmer”). Varje fel alternativ har en kommentar om den feltanke
det prövar, till exempel stack i stället för kö, DFS-tanke i BFS, lägst g eller h i
stället för f, antal kanter i stället för kostnad, MAX-val i en MIN-nod och
väntetid i stället för prioritet.

Delkort: alla delar har egen fråga, ledtråd, facit med specifika rubriker,
nivå och verktygsmetadata. När en senare del behöver ett tidigare delsvar står
det i delens fråga (2.13 b, 1.18 c, 2.16 c, 2.19 c). Delfacit avslöjar inte
senare delars svar. Miniräknare är tillåten och GeoGebra behövs inte, som i
resten av AI-banken. Självrättningen är avstängd (`spel:false`, `rättSvar:null`).

## Verktyg och kontroll

- `tools/bygg-ai-pafyllnad-2026-11-11.py` gör alla ändringar och är idempotent.
  Svaren räknas fram med `tools/ai_sokalgoritmer.py`. Figurerna byggs med
  `tools/ai_figurer.py`, som följer bankens figurformat.
- `tools/ai-pafyllnad-2026-11-11.test.js` kontrollerar alla nya svar med egna
  simuleringar i JavaScript (BFS, DFS, A* med lika-värde-regler, UCS, minimax och
  alfa–beta). Testet skyddar också lärarkommentarerna: inledningar, färgade
  start- och målnoder, tabellstil och att inga `<ol type="A">` eller ledtrådar om
  ”upptäckta rutor” finns kvar i köuppgifterna.
- `tools/ai-expansion-2026-11-11.test.js` är avgränsat till de 25 tidigare
  uppgifterna. Alternativkontrollen följer det nya A.-formatet.
- Resultat: 42/42 tester godkända (AI-testerna och `granska-uppgifter.test.js`).
  Validatorn hittar inga nya fynd i AI-banken. Kvar finns bara de två redan
  godkända likhetsfynden (3.04/3.05 och 2.06/2.08).
- Webbläsarprov: alla 26 nya och de reviderade uppgifterna har renderats med
  appens CSS, med facit och ledtrådar i 900 px och utvalda i 390 px (mobil).
  Det gav inga JS-fel och inget horisontellt överflöd utanför figurernas egna
  rullningsytor. Delkortsvy har kontrollerats för 1.04 och 2.13.
  Facit och ledtrådar har lästs igenom. Granskningen är gjord.

## Ma1 0.167 i samma logg

Rapporten (2026-11-10 09:56, ingen kommentar) åtgärdades redan 2026-11-10. Se
[MA1_0_167_2026-11-10.md](MA1_0_167_2026-11-10.md). Frågan är medvetet öppen i
Uppgiftslabbet, och `saknat-underlag-2026-11-06.test.js` kräver att alternativen
inte visas i lärarvyn. Ingen ändring har gjorts. Rapportstatusen i appen är inte
ändrad.
