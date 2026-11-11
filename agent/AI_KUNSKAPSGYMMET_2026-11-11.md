# AI: 30 självrättande uppgifter för Kunskapsgymmet, 11 november 2026

## Uppdrag

Användaren vill ha fler varierade uppgifter som kan användas i Kunskapsgymmet på
sikt. Användaren har också gett stående tillstånd att pusha till `main` när ett
arbete är klart.

## Format (samma som de självrättande fysik- och matematikbankerna)

- Huvuduppgift: `spel:true`, `självrättning:true`, `svarstyp:"flera_delar"`,
  `rättSvar` som lista i delarnas ordning, `tolerans`, `svarFormat`,
  `svarEnhet` (null), `svarsstruktur:"ordnad"` och `svarEtiketter`.
- Del med tal: `svarstyp:"numeriskt"`, heltal i `rättSvar`, `tolerans:0` och
  `svarFormat:"numeriskt"`. Används för antal rutor/noder/löv, steg, kostnader,
  g/h/f och nodvärden, även negativa.
- Del med flerval: `svarstyp:"alternativ"`, ett enda rätt alternativ,
  `rättSvar` = det rätta alternativets text och en kommentar till varje
  alternativ. Frågan slutar med ”Välj ett alternativ.”
- Ordningsföljder och vägar efterfrågas inte som fritext, eftersom de inte kan
  rättas säkert. De efterfrågas i stället som ”vilken ruta tas ut som femte”
  (flerval) eller som ett tal (antal steg, antal uttag).
- Varje del har egen ledtråd, facit och träningsnivå. Den gemensamma figuren
  och förutsättningarna ligger i `spelIntro`.

Kunskapsgymmet använder ännu inte AI-banken. Innan banken kopplas in behöver
konsumenten testas med dessa kort, till exempel så att negativa heltal och
alternativ som ”A2 och B1” rättas rätt.

## Nya uppgifter (3 per område)

| Område | ID | Delar och svar |
|---|---|---|
| Kö och stack | 1.32 | C först i kön; 3 kvar |
| | 1.33 | 3 uttag innan C; F överst |
| | 1.34 | Tredje uttaget: R (kö), Q (stack) |
| Kön under sökningen | 1.35 | Längsta kö 5; H före målet |
| | 1.36 | C överst; 7 uttag |
| | 1.37 | A2 och B1; längsta kö 3; C3 före målet |
| BFS | 1.38 | 7 steg; femte uttaget C1; 16 uttag |
| | 1.39 | 2 rutor på avstånd 2; 6 steg; fjärde uttaget C1 |
| | 1.40 | Sjätte uttaget C2; 11 uttag; 2 rutor på avstånd 3 |
| DFS | 1.41 | Femte besöket B4; 8 besök; 6 steg; kortaste: ja |
| | 1.42 | Femte noden G; 9 noder |
| | 1.43 | Sjätte besöket A4; 10 besök; 9 steg; kortaste: nej (7) |
| Prioritetsköer | 2.35 | Tredje uttaget K; kvar värde 6 |
| | 2.36 | A* tar Q; f = 9 |
| | 2.37 | 3 noder med lägst f; F (lägst h) |
| g, h och f | 2.38 | g 3, h 4, f 7 |
| | 2.39 | Med lera: g 5, h 2, f 7 |
| | 2.40 | g 2, h 2; verklig väg 8 steg längre än h |
| A*-sökning | 2.41 | Fjärde uttaget B3; 6 uttag; kostnad 5 |
| | 2.42 | Girig bäst först 12, A* 8 (lera) |
| | 2.43 | Femte uttaget A3; 6 uttag; kostnad 5 |
| Viktade vägar | 2.44 | Given väg 10; billigast 5 |
| | 2.45 | Billigast 6 via omväg; 4 kanter |
| | 2.46 | A* tar A efter S; 4 uttag; kostnad 7 |
| Minimax | 3.31 | B = 5; rot 5; drag B |
| | 3.32 | D = 2; rot 2; drag A |
| | 3.33 | A = 1; rot 3; drag B (negativa värden) |
| Alfa–beta | 3.34 | Rot 5; 1 löv beskärs; L4 |
| | 3.35 | Rot 6; 3 löv beskärs; 5 utvärderas |
| | 3.36 | Rot 6; 3 löv beskärs; första beskärningen i B |

Distraktorerna i frågorna om ”vilken ruta tas ut som k:e” är grannarna i
uttagsordningen och den ruta som den andra algoritmen (DFS respektive BFS)
skulle ha tagit som k:e. Kommentaren anger var rutan faktiskt hamnar och
pekar ut feltanken.

Entydighet: frågor om rotens drag förutsätter ett unikt bästa barn. A*-uppgifter
utan regel för lika värden kontrolleras så att lägsta f är unikt vid varje uttag.
2.46 fick därför kanten S–B = 3. Med S–B = 2 hade B och C fått samma f.

## Kontroll

- Byggskript: `tools/bygg-ai-kunskapsgymmet-2026-11-11.py`. Det körs efter
  `bygg-ai-pafyllnad-2026-11-11.py`, `bygg-ai-pafyllnad2-2026-11-11.py` och
  `bygg-ai-pafyllnad3-2026-11-11.py`. Hela kedjan ger en identisk fil från den
  committade versionen.
- Test: `tools/ai-kunskapsgymmet-2026-11-11.test.js` kontrollerar
  Kunskapsgymmets format och räknar om alla svar med egna simuleringar i
  JavaScript (BFS, DFS, girig bäst först, A*, billigaste väg, minimax och alfa–beta).
- Resultat: 65/65 tester i AI-banken godkända. Validatorn hittar inga nya fynd.
- Webbläsarprov med appens CSS i 900 px och delkort i 390 px. Inga JS-fel och
  inget horisontellt överflöd. Facit och ledtrådar har lästs igenom. Granskningen är gjord.

Banken har nu 125 uppgifter, varav 30 självrättande. Varje område har 10–22 uppgifter.
