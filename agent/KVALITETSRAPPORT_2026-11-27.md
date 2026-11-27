# Kvalitetsrapporten i Kunskapsgymmet, 2026-11-27

Användaren körde adminfunktionen ”Kvalitetsgranskning” i Kunskapsgymmet (Fy1) och fick en lång logg, men visste inte hur
granskningen fungerar.

Granskningen ligger i `index.html` (`kvKor`). Den går igenom alla kort som eleverna möter (efter `expandGameTask`), med
appens egen rättning och ritning, och har fyra kontroller:

- `facit`: godkänns facit som elevsvar?
- `figur`: krockar en etikett med en linje, en cirkel eller en annan etikett, eller hamnar den utanför bilden?
- `plural`: står kortets inledning i plural fast kortet bara visar en fråga?
- `raknare`: saknas miniräknare där den behövs?

Fynd som admin markerar som OK sparas i `kg_private.kvalitet_ok`.

## 1. ”Facit godkänns inte”: 1 643 falsklarm

Kontrollen skrev in det sparade `rättSvar` som elevsvar, till exempel 8.253850129198966 eller 122.75.

- Sedan beslutet 2026-10-26 lagras fysikens `rättSvar` oavrundat, och `svarVardesiffror` styr precisionen. Rättningen
  godtar n−2 till n+2 värdesiffror, så ett maskinvärde med 16 siffror underkänns med rätta.
- Kontrollen hade alltså inte följt med i beslutet. Alla 1 538 facitfynd i Fy1 och 97 i Fy2 var av den typen.
- I AI-banken (7 fynd) provades namnlistor i omvänd ordning med ”x = ”, och ”A|B”-alternativ som ett enda svar.

Ändrat i Kunskapsgymmets `kvFacit`:

- Med `svarVardesiffror` provas facit avrundat till det rekommenderade antalet värdesiffror, alltså som en elev skriver
  svaret (1,2·10² för 122,75 med två värdesiffror).
- Namnlistor i ordning (`namnordning`) och mängder (`namnmangd`) provas inte omkastade.
- För alternativ provas det första.

Efter ändringen har alla kurser **0 facitfynd**.

Ett verkligt fel kom fram: **Ma2 3.67** gick inte att rätta.

- `rättSvar` var LaTeX-strängen `\(y=45^\circ-\frac{x}{2}\)` utan `svarFormat`, så inget rimligt svar godtogs.
- Facit är matematiskt rätt: medelpunktsvinkeln är 2x, ∠MBA = 90° − x, ∠MBD = 90° + x och y = 45° − x/2.
- Nu är `rättSvar` `y=45-x/2` med formatet `uttryck`. Uttrycksrättningen i Kunskapsgymmet godtar nu också ett utskrivet
  gradtecken (45° − x/2) när facit saknar det, men inte i sin, cos och tan, där gradtecknet ändrar värdet. Fallen ligger
  i självtestet `KG_TEST_MA4_SVAR`.
- Provat: y=45−x/2, 45−x/2, y=45−0,5x, y=(90−x)/2, y=45°−x/2 och 45°−x/2 godtas. y=90−x/2, y=45+x/2, y=45−x och y=x/2
  underkänns.

## 2. Text utanför bilden: mitt fel från 2026-11-24

Textförstoringen i commit 1a7e7b1 (”läsbar figurtext i mobil”) mättes med `tools/granska-svg.js`. Den laddade inte
webbtypsnittet IBM Plex Mono, som Kunskapsgymmet använder i figurerna, utan mätte med ett smalare reservtypsnitt. Med
det riktiga typsnittet klipptes etiketter av, till exempel ”R₂ = 1000 Ω” i 8.16, ”ε₁ = 12 V” i 8.31 och ”240 m” i 3.131.

- `tools/svg-ram-plexmono-2026-11-27.cjs` mäter varje text i alla banker med IBM Plex Mono och vidgar `viewBox` där en
  text sticker ut. Det gjordes i 64 figurer: Fy1 46, Fy2 9, Ma2 7, Ma1 1 och Ma3c 1.
- Vidgningen följer textens utsträckning plus 4 enheters marginal. Bredd och höjd skalas i samma proportion, och ingenting
  flyttas.
- Bakgrundsrektanglar och kantlinjer som täckte den gamla ramen följer med, till exempel land- och vattenbanden i 3.131.
- Kontroll: bara `<svg>`-taggar, bakgrunder och kantlinjer har ändrats, ingen text och inget facit. En andra körning
  hittar inget mer att vidga. Ett urval är renderat före och efter, och Kunskapsgymmets granskning med typsnittet laddat
  har 0 fynd ”utanför bilden” i alla kurser.
- `tools/granska-svg.js` laddar nu IBM Plex Mono och Instrument Sans innan den mäter. Den varnar om typsnittet inte gick
  att ladda (ingen nätåtkomst), eftersom etiketter utanför bilden då kan missas. Med det hittar den felen i de gamla
  figurerna och godkänner de nya.

## 3. Övriga fynd i Fy1-rapporten

- **Krock med cirkel eller linje**, 8 figurer. Sju är falsklarm:
  - 4.739, 6.85, 3.203 och 9.301: kontrollen räknar en ellips som en cirkel med ellipsens bredaste radie.
  - 9.444 och 9.448: ”e−” står avsiktligt i elektronen.
  - 4.877: etiketterna har vit bakgrund.

  I **4.852** låg ”f = 20 N” på rampens lutande kant. Etiketten är flyttad ned i rampen, nära friktionspilen.
- **Inledning i plural**, 6 uppgifter. Inledningarna är omskrivna så att de fungerar både på papper och på ett kort med
  en fråga. Frågor och facit är oförändrade.
  - 4.747: ”Utgå hela tiden från de ursprungliga värdena.”
  - 4.647: ”Vikten är stilla i förhållande till hissen.”
  - 6.88: ”En instängd gas förändras.”
  - 6.530: ”En instängd gas byter tillstånd.”
  - 6.538: ”Temperaturen och gasmängden är konstanta.”, som delkorten redan sa.
  - 7.139: ”Tre olika metallbitar värms upp.”

## Kvar i andra kurser, inte åtgärdat

En körning med typsnittet laddat ger i alla kurser 449 fynd ”linje”, 115 ”cirkel”, 341 ”annan etikett” (339 i Ma4), 26
”plural” och 43 ”miniräknare”. Krockkontrollen är grov, som falsklarmen i Fy1 visar, så fynden behöver bedömas figur
för figur och massändras inte.

Skript och test:

- `tools/kvalitetsrapport-2026-11-27.py` (Ma2 3.67, Fy1 4.852 och inledningarna)
- `tools/svg-ram-plexmono-2026-11-27.cjs`
- `tools/kvalitetsrapport-2026-11-27.test.js`
- i Kunskapsgymmet: `tools/kvalitet-facit-2026-11-27.test.js`
