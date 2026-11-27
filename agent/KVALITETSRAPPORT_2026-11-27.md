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

## Omgång 2 (samma dag, ”Fortsätt”): övriga kurser

**Inledningar i plural.** Kortet visar hela uppgiften med alla deluppgifter i följd, eftersom deluppgiftskedjan
(2026-10-24) gäller allt utom `kgFristaendeDelar`. Därför är ”Lös ekvationerna.” följt av a)–d) rätt, vilket en
rendering av Ma3c 1.1038 visar. Pluralkontrollen var föråldrad. Den letar nu bara bland fristående delkort, och de 20
fynden i Ma3c, Ma4 och Ma5 försvann. Även de sex Fy1-inledningarna i omgång 1 var alltså rätt från början. De nya
formuleringarna fungerar lika bra och står kvar.

**Miniräknare (43 fynd).**

- 42 är rätt bedömda som `miniräknare: false`: avrundning, positionssystem, grundpotensform, prefix och procentform, där
  räknaren tar bort det som prövas, eller enkel huvudräkning som 12·5/8 och −1/4. De är förda in i Kunskapsgymmets
  `KV_RAKNARE_GRANSKADE`.
- Ma3c 1.980 har fått miniräknare, eftersom parabelmodellen ger 175/40 = 4,375 m
  (`tools/kvalitetsrapport-2026-11-27b.py`).

**Figurkrockar.** Krockkontrollen i Kunskapsgymmet (`kvFigur`) är förbättrad på fyra punkter:

- En vit kantkopia under en etikett, som många figurer ritar, är ingen egen etikett. Det var de flesta ”annan
  etikett”-fynden i Ma4.
- En etikett med vit kant (kopia eller `paint-order="stroke"`) räknas som läsbar över linjer och cirklar.
- En ellips mäts med båda radierna.
- En nodetikett inuti en liten cirkel, en etikett med en fylld ruta bakom sig och en kontur som döljs av en fylld form
  ovanpå räknas inte.

Därefter granskades varje kvarvarande figur visuellt, 156 kort och 119 unika figurer, och åtgärdades
(`tools/svg-etikettkant-2026-11-27.py`):

- **Vit kant** på 172 etiketter i 119 uppgifter som avsiktligt står på en linje eller cirkel. Exempel: hastighet längs
  kastbanan, mått på måttlinjer, r₂ på streckad sträcka, −1 på enhetscirkeln, mängdnamn på Venndiagrammens cirklar och
  gradtal på asymptoter. Linjen bryts bakom texten, och ingenting flyttas. Listan finns i
  `tools/svg-etikettkant-2026-11-27.json`.
- **Flyttade etiketter:**
  - ”f” i Ma1 2.56 och 2.58 samt Ma2 2.210 och 2.413 stod där kurvan korsar x-axeln och står nu på kurvans övre högra gren.
  - ”2x+1” i Ma3c 3.501 låg på gränsetiketten ”3”.
  - Punktetiketten ”−3” i Ma4 4.589 låg på axelns ”−3” och står nu ovanför punkten.
- Kontroll: bara `<text>`-taggar har ändrats. Ett urval är renderat före och efter, och Kunskapsgymmets granskning med
  typsnittet laddat har **0 synliga fynd i alla kurser**. Kvar är bara de små fynden som rapporten döljer som standard,
  till exempel axeltal som en rutnätslinje går igenom.

Skript och test:

- `tools/kvalitetsrapport-2026-11-27.py` (Ma2 3.67, Fy1 4.852 och inledningarna)
- `tools/kvalitetsrapport-2026-11-27b.py` och `tools/svg-etikettkant-2026-11-27.py` (omgång 2)
- `tools/kvalitetsrapport-2026-11-27b.test.js`
- `tools/svg-ram-plexmono-2026-11-27.cjs`
- `tools/kvalitetsrapport-2026-11-27.test.js`
- i Kunskapsgymmet: `tools/kvalitet-facit-2026-11-27.test.js`
