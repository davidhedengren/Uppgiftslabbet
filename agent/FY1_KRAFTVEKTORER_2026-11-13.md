# Fy1: nytt område Vektorer i kraftkapitlet, 2026-11-13

## Uppdrag

Användaren gjorde om övningsbladet ”Vektorer – resulterande kraft” (Fysik 1, kap 4) och bad om att
uppgifterna också läggs in i Uppgiftslabbet och Kunskapsgymmet, med fler likadana uppgifter för
mängdträning och flerval där eleven annars skulle rita. Därefter: ”ha det som ett första område i
kraftkapitlet, alltså vektorer”, med en tydlig genomgång av hur man adderar vektorer och bestämmer
komposanter, i båda apparna.

## Struktur

- Nytt område `kraftvektorer` (”Vektorer”) först i `OMR["4"]`. Nyckeln är inte `vektorer`, eftersom
  `vektorer` redan är kap 3 (”Hastighet som vektor”) och Kunskapsgymmet sparar områdesresultat per `omr`.
- Användaren valde att flytta de två befintliga vektordelmomenten från `newton1`:
  ”Addera krafter som vektorer” (21) och ”Krafter i komposanter” (20). De 41 uppgifterna har fått
  `omr: "kraftvektorer"`, `"newton1"` tillagt i `omrTidigare`, nytt prefix `kraftvektorer__` i
  `familjNyckel` och det gamla i `familjNyckelTidigare`. Inget annat fält ändrades (kontrollerat per objekt).
- Delmoment i området: Resultant längs en linje (12), Addera krafter som vektorer (57), Krafter i komposanter (20).

## Nya uppgifter 4.913–4.960

| ID | Innehåll | Svarsform |
|---|---|---|
| 4.913–4.917 | Övningsbladets vagnar (sida 1), egna korta sammanhang | flerval (storlek + riktning) |
| 4.918–4.924 | Nya krafter längs en linje: låda, kälke, dragkamp, båt, boll, shoppingvagn, kartong | flerval / tal med tecken |
| 4.925–4.929 | ”Kraftresultanten – övningar”: storlek av F₁, F₂, F_R och riktning; 4.929 vinkeln α med tangens | a–c tal, d flerval eller tal |
| 4.930–4.935 | ”Kraftresultanten – stöd” | a F_Rx, b F_Ry, c F_R, d riktning (flerval) |
| 4.936–4.943 | ”Resultantbestämning II” (storlek utskriven vid pilen, avrundad som i originalet) | som ovan |
| 4.944–4.946 | ”Kraftresultanten – övningar 2”, uppgift 1–3 (4.945–4.946 ger F_R = 0) | som ovan |
| 4.947–4.960 | Nya rutnätsuppgifter med egna sammanhang (hundar, kälke, ring, lampa, fotboll, magneter, knut, puck, låda med friktion, hästar och pråm, båtlinor, drake, timmerflak, tvättlina) | som ovan |

Tiokraftspusslet från övningsbladet är inte inlagt: frågan ”Går det att använda alla tio …” är en
resonemangsuppgift och a-delen kräver att eleven prövar kombinationer på papper.

Alla krafter är hela tiotal (1 ruta = 10 N) och alla pilar börjar och slutar på rutnätets kryss,
som i det omarbetade övningsbladet. Därför skiljer sig några tal från originalbladet (se svar i
facit-PDF:en i `OneDrive\Fysik\Fysik 1\Extrauppgifter\Kap 4 – Kraft`).

## Pedagogiska beslut

- Riktningen ritas på papper (”Rita resultanten i figuren. Åt vilket håll pekar den?”). I Kunskapsgymmet
  är d-kortet ett flerval med fyra riktningar. Felalternativen bygger på teckenfel i x eller y,
  motsatt riktning och tanken att resultanten pekar som den största kraften. Varje fel har en kommentar.
- På papper är vagnuppgifterna öppna (”Hur stor är resultanten och åt vilket håll pekar den?”). I
  Kunskapsgymmet är de flerval med vanliga fel: fel riktning, alla krafter adderade utan tecken, 0 N
  och bara den största kraften.
- **Friktion ritas längs underlaget** (användarbeslut 2026-11-13): friktionskraften och vattnets
  motstånd mot båtskrovet utgår från kontaktytans mitt och ligger längs marken, aldrig mitt på föremålet.
- Resultanten är grön i alla facitfigurer (användarbeslut för övningsbladet, följt här).
- a-facit visar bara x-komposanterna och b-facit bara y (enligt FY1_VEKTORER_DELFACIT_2026-11-02).
  c-facit har ingen lösningsfigur, så att riktningen i d inte avslöjas.
- Nivå: E överallt. Träningsnivå 1 för en linje och för två krafter i rutnät (a, b), 2 för Pythagoras
  och tre–fyra krafter, 3 för vinkeln med tangens (4.929 d, `trigonometri: true`).
- Verktyg: miniräknare tillåten (fysik). GeoGebra behövs inte.
- Storlekar med decimaler: `svarVardesiffror: 3`, oavrundat `rättSvar`, tolerans 0,05. Hela tal: tolerans 0.

## Genomgångar i Kunskapsgymmet (`typuppgifter-fy1.js`)

Fyra nya genomgångar först i kapitel 4, med figurer i `dg`-klasser (följer ljust och mörkt läge):
Resultant längs en linje, Addera vektorer grafiskt, Komposanter i ett rutnät och Addera krafter med
komposanter. Den befintliga ”Dela upp en kraft i komposanter” (trigonometri) flyttades till området
och fick träningsfamiljen ”Krafter i komposanter” (tidigare felaktigt ”Kraftresultant och kraftjämvikt”).
Uppgiftslabbet har ingen genomgångsfunktion. Där syns det nya området och uppgifterna.

## Kontroller

- `node --check`, JSON-parsning och unika id (4569 uppgifter).
- `tools/granska-uppgifter.js`: 0 ERROR, 10 WARNING och 759 INFO för `uppgifter.js`, samma som före ändringen.
  De första exakta textdubbletterna rättades genom att ge varje originaluppgift ett eget sammanhang.
- SVG-granskningen körd på de nya uppgifternas 83 figurer: inga varningar (bara samma
  EDGE_CLIPPING-information om bakgrundsrutan som befintliga figurer har). Etiketter placeras mitt i rutor.
  Hela `granska-svg.js` gick inte att köra klart (Chrome-timeout).
- Förhandsvisning med KaTeX av uppgift, ledtråd, facit och alla delkort för ett urval, samt lokal
  Kunskapsgymmet: 4.955 a–d besvarad (40, 20, 44,7, flerval) och genomgångarna lästa i mörkt läge.
- Tester: nytt `tools/fy1-kraftvektorer-2026-11-13.test.js` (6 pass). `fysik1-kapitel4.test.js`
  räknar nu även de flyttade uppgifterna (urvalet utökat till `kraftvektorer` med `omrTidigare` newton1).
  `fysik1-prosa` och `verktygspolicy-2026-10-14` har samma fel som före ändringen (andra uppgifter).

## Tillägg samma dag: tre delmoment efter trigonometri

Användaren: delmomenten ska vara ungefär ”Resultantbestämning utan trigonometri”, ”med trigonometri” och
”Komposantuppdelning”, så att elever som ännu inte gått igenom trigonometri kan träna enklare vektoruppgifter.

| Delmoment | Antal | Innehåll |
|---|---:|---|
| Resultantbestämning utan trigonometri | 55 | Resultant längs en linje (4.913–4.924), alla rutnätsuppgifter utan trigonometri (3.301–3.308, 4.925–4.928, 4.930–4.960) |
| Resultantbestämning med trigonometri | 14 | 3.331–3.344, 3.366 (cosinus i facit) och 4.929 (vinkeln med tangens) |
| Komposantuppdelning | 20 | Tidigare ”Krafter i komposanter” (3.286–3.293 utan och 3.314–3.329 med trigonometri) |

Gamla delmomentsnamn ligger i `familjTidigare`, så Kunskapsgymmets `migreraFamiljer` för över elevernas
resultat. `familjNyckel` har nya nycklar; den tidigare står i `familjNyckelTidigare` när fältet saknades.
Genomgångarnas `traningsfamilj` i Kunskapsgymmet pekar på de nya namnen. Testet kontrollerar att inget kort
i delmomentet utan trigonometri har `trigonometri: true` eller sinus, cosinus eller tangens i facit.

## Textändringar (användarbeslut 2026-11-13)

Gjorda med `tools/fy1-kraftvektorer-text-2026-11-13.py` (bara `omr = kraftvektorer`, idempotent) och i
Kunskapsgymmets `typuppgifter-fy1.js`:

- Punkter och vektorer skrivs \((30,\,20)\) i stället för \((30;\ 20)\): 73 ställen i banken och 3 i genomgången.
- Facitrubriken ”Kraftresultant längs en linje” heter ”Resulterande kraft: \(F_R=F_1+F_2+\dots\)” (12 uppgifter).
- ”Addera sedan med tecken.” heter ”Sedan adderar du alla krafter (tänk på tecknen).” (12). Alternativkommentaren
  ”Resultanten är summan av alla krafter med tecken.” heter ”Resultanten får du genom att addera alla krafter
  (tänk på tecknen).” (3).

”Ange med tecken” i komposantfrågorna och ”(Svara med tecken.)” är kvar, eftersom de säger hur svaret ska
skrivas. Punkter med semikolon i andra områden (kap 2–3) är inte ändrade.

## Felrapporter 2026-11-13 10:49 och 18 nya komposantuppgifter

- **Fy1 4.940 a** (lärare: ”nivå 2”): att läsa av komposanter för två snea krafter är nivå 2. Samma ändring för a och b i
  4.933, 4.938, 4.939, 4.941, 4.947, 4.948, 4.951, 4.952 och 4.956. Krafter längs rutnätets linjer behåller nivå 1.
- **Fy1 4.948 b** (”ha dem som a), b), c)”): uppgiften är korrekt byggd som deluppgiftskedja (samma inledning och figur,
  sedan bara delens fråga). I elevernas träning visas a → b → c → d i följd. Kunskapsgymmets admin-bläddring
  (`state.adminBlad`) visar däremot varje delkort för sig. **Kvar att utreda:** om bläddringsläget också ska visa kedjan.
- **Fy2 2.179 c**: ”låter mörkast” och ”klang” krävde musikvana. Ny fråga: vilken pipa ger lägst ton, och finns någon
  frekvens som båda kan ge? Svar: den täppta (131 Hz); ingen gemensam frekvens (jämna mot udda multiplar av 131 Hz).
- **Fy2 2.135**: piplängderna står nu längs piporna med måttlinjer i uppgift och delkort.
- **Fy2 2.69**: pulsernas höjder (4,0 cm och 3,0 cm) står i figuren, frågan gäller punkten där de markerade punkterna
  möts (+1,0 cm) och en skiss. Facit har en figur med summan punkt för punkt; lägsta punkt ungefär −2,2 cm.

Nya uppgifter i Komposantuppdelning (4.961–4.978):

| ID | Innehåll | Nivå |
|---|---|---|
| 4.961–4.968 | Läs av \(F_x\), \(F_y\) och \(F\) i rutnät med olika skalor (2 N, 5 N, 10 N, 20 N, 50 N, 100 N, 1 kN per ruta) | a, b 1; c 2 |
| 4.969–4.972 | Flerval: vilka tecken har \(F_x\) och \(F_y\)? | 1 |
| 4.973–4.978 | \(F_x=F\cos v\), \(F_y=F\sin v\) ur given kraft och vinkel (resväska, kälke, gräsklippare, koppel, kran, båtlina) | 3, `trigonometri: true` |

Uppgifter med trigonometri har träningsnivå 3, så elever utan trigonometri möter dem senare. SVG-granskningen: en kvarvarande
heuristisk varning (4.978: vinkeletiketten 20° ligger inom den flacka pilens omslutande rektangel; bilden är tydlig).
Testet `tools/fy1-kraftvektorer-2026-11-13.test.js` kontrollerar komposanter, tecken och trigonometrivärden.
