# MatO1: kalibrering och självrättning 2026-10-08

Banken har gått från 2700 huvuduppgifter och 2156 aktiva kort till 2727 huvuduppgifter och 2184 aktiva kort. 794 befintliga huvuduppgifter ändras; inga ID:n tas bort. 191 befintliga kort får ändrad träningsnivå. 27 nya uppgifter ger enklare ingångar och metodval.

## Omfattning

Hela banken inventerad och maskinellt granskad. Alla aktiva nivå 1-texter lästa, nivå 1-2 kontrollerade för långa/osjälvständiga formuleringar och utvalda nivå 2-lösningar granskade. 332 oberoende omräkningar plus direkt kontroll av nya och korrigerade uppgifter. Detta är inte en redovisning av att samtliga 2727 uppgifter har räknats om för hand.

Nivå 1 betyder ett grundbegrepp eller ett direkt samband med enkla tal. Derivera och därefter sätta in ett värde, beräkna en tangentekvation, bestämma extremvärden eller genomföra flera beroende steg hör normalt till nivå 2 eller högre. Delkort bedöms utifrån den information som faktiskt är given.

Alla 50 områden har nu aktiva nivå 1-kort för varje spår som områdesstrukturen anger. Fem områden saknade nivå 1 före revideringen: faktorisera polynom, räkna med rationella uttryck, andraderivatan, extremvärdesmodellering och derivatans graf.

## Korrigerade innehålls- och rättningsfel

- **1.129:** rationella ekvationen har lösningen x = 2; tidigare maskinsvar var −2. Definitionsvillkoret anges.
- **1.113:** facit ger (x−3)(x+3) i stället för att återge det ofaktoriserade uttrycket.
- **2.254 a/b:** funktion, derivata och maskinsvar hör ihop. Det enklare b-kortet får derivatan given och frågar efter f′(0) = 11.
- **2.309:** lutningen och tangentekvationen får egna svarsfält och självbärande kort.
- **3.481:** övre integrationsgränsen och sträckan får varsitt svar. Gamla flaggan för manuell komplettering tas bort.
- **4.448:** frågan tillhör nu två möjliga sinusvinklar; 30° ger andra vinkeln 150°. Ny enhetscirkelfigur.
- **4.446, 4.447, 4.461, 4.464:** trianglarna har faktiskt räta vinklar och korrekta sidproportioner. Två tidigare dubbletter får andra sidlängder.
- **2.745, 3.1074, 3.1049:** dolda dubbletter får faktisk beräkningsvariation.
- **2.99 och 1.290:** uppgifterna flyttas till rätt moment.

## Facit och språk

629 huvuduppgifter får allmänna metodförord eller upprepade kontrollmallar borttagna. De konkreta beräkningsstegen behålls. Tillsammans med de särskilt omskrivna lösningarna ändras huvudfacit i 640 befintliga uppgifter. Interna etiketten ”Kort rutinövning” tas bort; en upprepad inledning i 4.231 rensas. De nya faciten förklarar den centrala idén, visar en kort beräkning när den behövs och avslutar med ett tydligt svar. Ledtrådar hålls skilda från lösningen.

## Rättningsformat

- `faktoriserat` jämför matematiken och produktformen. Omordnade faktorer och alternativa minustecken godtas. Utvecklade summor och kvarvarande faktorer av för hög grad underkänns.
- `primitiv` godtar en extra konstant var som helst i uttrycket. Villkorsbestämda funktioner behåller formatet `uttryck` och kräver rätt konstant.
- `primitiva` godtar hela familjer som K + x³ eller x³ + 2K + 7 och kräver en fri konstant. Ett ensamt x³ eller x³ + sin(K) är inte hela familjen.
- `funktionsuttryck` skiljer funktionsvärdet f(a+h) från multiplikation med f.

## Verifiering

- Faktisk Chromium-rättning: 4931 godkända kontroller över alla 2184 aktiva kort, inklusive alternativa korrekta svar och felaktiga kontrollsvar.
- 13239 matematikrenderingar, inga KaTeX-fel. Svarsfältskontrakten kontrollerade över hela träningsbanken.
- 38 kort testas även genom appens Kontrolleraknapp/flervalsmotor, med både rätt och fel svar.
- 14 känsliga kort visas på 390 och 1280 px: inga sidöverflöden eller renderingsfel. Mobilfacit inspekterat; en onödigt lång formel i 4.493 kortas.
- 332 oberoende symboliska/numeriska omräkningar utan kvarvarande avvikelse. Nya kort och särskilt rättade uppgifter kontrolleras även direkt.
- Alla tio nya eller omritade SVG-figurer kontrollerade med faktisk DOM-geometri och visuellt: inga fynd.
- 81 övriga mastertester, 47 SVG-tester och 63 konsumenttester godkända. SVG-testerna använder `CHROME_PATH=/workspace/.environment/chromium-svg` i molnmiljön.
- MatO1-validator: 0 ERROR, 54 WARNING, 182 INFO. Före: 0/54/184. Tre kända varningar gäller lärarbladets manuella c-del i 1.02, 1.19 och 1.32; 51 gäller äldre dubbletter. Inga nya varningar.

Hela projektets validator har även körts. Befintliga fel i andra banker ligger utanför denna MatO1-leverans och redovisas i nästa banks genomgång; ingen av dessa banker ändras i denna commit.

## Nivå 1 per område

| Område | Före | Efter | Nivå 1-kort efter |
|---|---:|---:|---|
| Algebra och polynom | 4 | 3 | 1.444, 1.528, 1.555 |
| Polynom | 3 | 3 | 1.449, 1.463, 1.471 |
| Faktorisera polynom | 0 | 2 | 1.818, 1.819 |
| Polynomekvationer | 5 | 3 | 1.476, 1.540, 1.564 |
| Absolutbelopp | 20 | 13 | 1.20, 1.30, 1.65, 1.95, 1.100, 1.168, 1.180, 1.237, 1.238, 1.451, 1.475, 1.479, 1.481 |
| Funktioner | 8 | 8 | 1.434, 1.453, 1.461, 1.472, 1.477, 1.511, 1.545, 1.551 |
| Polynomfunktioner | 3 | 2 | 1.486, 1.493 |
| Rationella uttryck | 9 | 7 | 1.290, 1.406, 1.407, 1.424, 1.448, 1.466, 1.473 |
| Förkorta rationella uttryck | 3 | 4 | 1.478, 1.538, 1.822, 1.823 |
| Ekvationer och rationella uttryck | 7 | 4 | 1.507, 1.509, 1.532, 1.557 |
| Multiplicera och dividera rationella uttryck | 0 | 2 | 1.824, 1.825 |
| Tangent, sekant och gränsvärde | 4 | 1 | 1.570 |
| Gränsvärde | 12 | 6 | 1.454, 1.474, 1.483, 1.505, 1.513, 1.524 |
| Kontinuerliga funktioner | 3 | 2 | 1.820, 1.821 |
| Ändringskvoter och derivata | 7 | 2 | 2.518, 2.762 |
| Begreppet derivata | 18 | 6 | 2.584, 2.636, 2.637, 2.640, 2.657, 2.698 |
| Numerisk derivering och derivering med digitalt verktyg | 3 | 2 | 2.587, 2.750 |
| Derivatans definition | 2 | 2 | 2.25a, 2.800 |
| Deriveringsregler | 15 | 1 | 2.1115 |
| Mer om derivatan av polynomfunktioner | 5 | 2 | 2.1109, 2.1110 |
| Derivatan av potensfunktioner | 9 | 2 | 2.1107, 2.1108 |
| Tangenter och derivata | 30 | 3 | 3.1066, 2.1113, 2.1114 |
| Derivatan av exponentialfunktioner | 1 | 1 | 2.729 |
| Talet e och derivatan av e^kx | 10 | 2 | 2.104, 2.254b |
| Naturliga logaritmer | 8 | 6 | 2.114, 2.119, 2.139, 2.751, 2.1111, 2.1112 |
| Derivatan av f(x) = a^x | 9 | 6 | 2.84, 2.89, 2.94, 2.99, 2.109, 2.704 |
| Exponentialfunktioner – tillämpningar och problemlösning | 2 | 1 | 2.570 |
| Vad säger derivatan om funktionens graf? | 0 | 2 | 3.1154, 3.1155 |
| Andraderivatan och funktionens graf | 0 | 2 | 3.1150, 3.1151 |
| Extrempunkter och terrasspunkter | 13 | 13 | 3.707, 3.708, 2.674, 2.679, 2.731, 3.828, 3.834, 3.836, 3.880, 3.970, 3.974, 3.1038, 3.1086 |
| Största och minsta värde | 13 | 11 | 2.688, 3.845, 3.848, 3.867, 3.878, 3.893, 3.905, 3.919, 3.932, 3.936, 3.1053 |
| Problemlösning med derivata | 2 | 2 | 3.459, 2.776 |
| Extremvärdesproblem med modellering | 0 | 2 | 3.1152, 3.1153 |
| Fler extremvärdesproblem | 1 | 1 | 3.797 |
| Deriverbarhet | 1 | 1 | 2.673 |
| Från derivata till funktion | 12 | 9 | 3.46, 3.283, 3.551, 3.617, 3.727, 3.792, 3.923, 3.1015, 3.1057 |
| Primitiva funktioner med villkor | 10 | 2 | 3.825, 3.1156 |
| Integral och area | 15 | 15 | 3.429, 3.504, 3.702, 3.830, 3.1068, 3.1119, 3.1120, 3.1121, 3.1125, 3.1128, 3.1129, 3.1132, 3.1136, 3.1137, 3.1142 |
| Integralberäkning med primitiv funktion | 32 | 10 | 3.41, 3.47, 3.631, 3.714, 3.793, 3.827, 3.833, 3.958, 3.991, 3.993 |
| Integraler – tillämpningar och problemlösning | 13 | 9 | 3.481a, 3.599, 3.902, 3.903, 3.1023, 3.1046, 3.1050, 3.1062, 3.1117 |
| Trigonometri i rätvinkliga trianglar och exakta värden | 5 | 5 | 4.431, 4.434, 4.466, 4.469, 4.470 |
| Trigonometri och enhetscirkeln | 18 | 8 | 4.209a, 4.210a, 4.211a, 4.411, 4.414, 4.422, 4.445, 4.472 |
| Trigonometriska ekvationer | 5 | 6 | 4.31, 4.36, 4.41, 4.46, 4.409, 4.495 |
| Areasatsen | 5 | 5 | 4.436, 4.438, 4.450, 4.462, 4.467 |
| Sinussatsen | 5 | 2 | 4.493, 4.494 |
| När ger sinussatsen två fall? | 1 | 1 | 4.448 |
| Cosinussatsen | 5 | 4 | 4.430, 4.446, 4.461, 4.463 |
| Trigonometri – tillämpningar och problemlösning | 5 | 5 | 4.82, 4.404, 4.405, 4.406, 4.435 |
| Linjär optimering | 9 | 7 | 4.157, 4.432, 4.437, 4.444, 4.452, 4.454, 4.458 |
| Geometriska summor | 10 | 5 | 4.295, 4.433, 4.440, 4.441, 4.456 |

## Filer och reproduktion

Master: `uppgiftermato1.js`, `agent/INNEHALLSREGLER.md`, `tools/mato1-kalibrering.test.js` och denna rapport med JSON. Konsument: identisk `uppgiftermato1.js`, rättningsfunktioner och cacheversion i `index.html`, kontraktstest i `tools/delkort.test.js` samt `tools/mato1-sjalvrattning.browser.py`.

Starta Kunskapsgymmet med `python -m http.server 8062` och kör `python tools/mato1-sjalvrattning.browser.py --url http://127.0.0.1:8062`. Verktyget använder appens riktiga funktioner och sparar resultat och skärmbilder i `/tmp`. Python Playwright och Chromium krävs.

Exakta ändrade ID:n/fält, alla nivåändringar, nyuppgifter och omräkningsresultat finns i [JSON-rapporten](MATO1_KALIBRERING_2026-10-08.json).
