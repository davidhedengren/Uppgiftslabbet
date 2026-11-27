# Fy1: manuell granskning av densitet, rörelse och krafter, 2026-11-27

I en tidigare chatt föreslogs och gjordes ändringar i Fy1 (lokala commits d4bd27e och 4f62f87). De nådde aldrig GitHub,
eftersom pushen misslyckades i den miljön, och patcharna följde inte med. Ändringarna är gjorda om här, varje uppgift är
kontrollerad mot banken, och de fem rörelseuppgifter som chatten inte namngav är identifierade på nytt. Skriptet är
`tools/fy1-granskning-2026-11-27.py`.

| Uppgift | Fynd | Ändring |
|---|---|---|
| 2.17 c | ”Bestäm densiteten.” efter ”Bestäm densiteten i g/cm³”. Facit begär kg/m³ (288/240 = 1,2 g/cm³ = 1 200 kg/m³). | ”Ange rätblockets densitet i kg/m³.” |
| 2.26 d | Som ovan (1 050/125 = 8,4 g/cm³ = 8 400 kg/m³). | ”Ange kubens densitet i kg/m³.” |
| 2.161 b | Som ovan (5 600/5 000 = 1,12 g/cm³ = 1 120 kg/m³). | ”Ange glykolens densitet i kg/m³.” |
| 2.379 | ”vågrätt” i stället för stilguidens ”horisontellt”. | ”flyter/ligger horisontellt”. `sprak-2026-11-17` går nu igenom. |
| 3.14 | ”Sedan har den den konstanta accelerationen …” | ”Den accelererar sedan konstant med 3,0 m/s² i 4,0 s.” |
| 3.158 | ”Därefter håller den den farten.” | ”Därefter fortsätter bilen med samma fart.” |
| 3.64, 3.120, 3.124, 3.155 | Facit använder tidlösa formeln eller medelfart gånger tid, alltså konstant acceleration, men frågan sa det inte. Utan villkoret går bara en medelacceleration att bestämma. | ”Räkna med att accelerationen är konstant (under inbromsningen).” Tomma `<p></p>` och inledande mellanslag i styckena är borta. |
| 4.368 | ”En satellit är 400 km över ytan.” Tyngdlösheten beror på att satelliten faller fritt. | ”En satellit kretsar runt jorden på 400 km höjd.” |

Andra rörelseuppgifter där facit förutsätter konstant acceleration är redan tydliga. Det gäller till exempel
”accelererar med …”, ”bromsar med …”, ”bromsar jämnt” (3.278), ”samma retardation” (3.206), fritt fall och diagram. I
3.253 är antagandet självt det som prövas.

Svar, facit och rättning är oförändrade. Kontroll:

- Kedjornas delkort börjar fortfarande med inledningen.
- 3.120 och 2.17 är renderade i Kunskapsgymmet.
- `sprak-2026-11-17` går igenom. Densitetstesterna och `fysik1-kapitel3` har samma kända fel som före ändringen.

Granskningen av hela urvalet (193 densitets-, 460 rörelse- och 1 020 kraftuppgifter) är inte slutförd. Det här är
de fynd som hittills är bekräftade.

## Omgång 2: manuell genomläsning område för område

Varje uppgift läses i en kompakt utskrift (text, delkort, svar, enhet, kgInstruktion) och kontrollräknas. Bygger på den
andra sessionens Fy1-revision samma dag (`agent/FY1_REVISION_2026-11-27.md`), som flyttade tabellvärden ur
`spelIntro` och delkort men inte ur huvudtexten `t`.

### Densitet (193 uppgifter, klart) – `tools/fy1-granskning-densitet-2026-11-27.py`

Alla beräkningar stämmer, även A-uppgifterna (2.200, 2.201, 2.290, 2.365–2.377). Ändringar:

- **Tabelldensiteter ur `t` till `kgInstruktion`** (beslutet 2026-11-27 gäller även `t`). 21 uppgifter: 2.117,
  2.122, 2.125, 2.132, 2.143, 2.147, 2.149, 2.150, 2.157, 2.158, 2.162, 2.198, 2.201, 2.202, 2.203, 2.274, 2.277, 2.367,
  2.368, 2.373, 2.375. I 2.367 saknades vattnets och glykolens densitet helt i delkortens instruktion.
- **Står kvar enligt undantagen:** omvandlingsuppgifter där densiteten är uppgiftens tal (2.6, 2.107, 2.108, 2.111,
  2.113), identifiera eller jämföra ämnen (2.24, 2.40, 2.88, 2.92, 2.100, 2.101, 2.104, 2.106, 2.165, 2.169, 2.188),
  värden i en formel eller ett påstående (2.51, 2.116) och uppgiftens egna material (trä, plast, granit, saltvatten,
  ägg, sten, spolarvätska, saft, palladium).
- **”Antag” → ”Anta”:** 2.142, 2.184, 2.195.
- **Tester:** `fysik1-densitet-a-2026-11-18` väntade 36,4 % i 2.200. Facit är 36,1 % med zinkens 7,13 g/cm³
  (formelsamlingen, beslut 2026-11-25), och testet går nu igenom. `felrapporter-2026-11-22-1935` godtar nu
  aluminiumets densitet i `kgInstruktion`.
- 2.85 a (luftens densitet saknades i delkortets instruktion) hade redan rättats av revisionen.

### Medelhastighet (93 uppgifter, klart) – `tools/fy1-granskning-rorelse-2026-11-27.py`

Alla beräkningar stämmer, även ekvationsuppgifterna (2.301, 2.303, 2.315, 2.316) och 2.307, 2.310, 2.317, 2.318,
2.320 och 2.380. Ändringar:

- **Konstanter och tabellvärden till `kgInstruktion`:** ljudets och ljusets fart (3.103), ljusets fart (3.127,
  2.308 b) och jordens radie (3.101).
- **Avrundnings- och svarsinstruktioner** till `kgInstruktion` eller bort: 3.101 a, 2.308 b (”Ange antalet varv.”) och
  3.21 b (”i m”).
- **Lösningsanvisningar och metatext bort:**
  - 3.103: ”Börja med att anta att ljuset inte tar någon tid …”
  - 3.104: ”Antag att s > 0 och v > 0.”
  - 3.229: ”Antag att alla sträckor och farter är positiva …” blir ”Bilen gör inga stopp.”
  - 3.127: ”Antag att signalen går rakt …”
  - 2.297, 2.303, 2.310, 2.315, 2.316, 2.319: ”Ställ upp ett uttryck …” eller ”Ställ upp en ekvation …”
- **2.295, 2.299:** pappersbladets b upprepade situationen med nya ord, och 2.295 sa både ”åker” och ”cyklar”. De har
  fått en ny gemensam inledning, och delkorten är inledning + fråga. I 2.299 b står mellanresultatet 11 934 m i frågan.
- **3.96:** ”Antag” → ”Anta”.

### Kapitel 3 utom medelhastighet (klart) – `tools/fy1-granskning-kap3-2026-11-27.py`

Områdena acceleration, at-diagram, konstant acceleration, st-diagram, vektorer och vt-diagram är lästa och
kontrollräknade (svar som bara kan läsas av i en figur är inte omräknade). Alla beräknade svar stämmer. Ändringar i
53 uppgifter:

- **Sakfel i texten:**
  - 3.231 c frågade efter tunneln, men den fanns bara i delkortet. Den står nu i frågan, och delkorten är kedjade
    med omkörningstiden 24 s som mellanresultat.
  - 3.46 c frågade efter ”personens hastighet” utan att det stod att personen går nedåt.
  - 3.44 b: ”tåget” → ”det snabbare tåget”.
  - 3.386: delkorten upprepade inledningen med nya ord, och d hänvisade till ”bilen i c”. Nu är de inledning +
    fråga, b får accelerationen 1,887 m/s² och d sina egna värden. Delfacit b: ”Från a):” → ”Accelerationen är given:”.
  - 3.387 a saknade A och B och får nu inledningen med figuren (tidigare beslut 2026-11-19 ersatt av kedjeregeln).
  - 3.388: ”Partikeln … En bil passerar” → en bil. b får farten i A som mellanresultat.
  - 3.380–3.384: ”Partikeln rör sig … En partikel passerar” → en mening. 3.389: inledningen ”Partikeln …” passade
    inte bilarna och cyklisten.
  - 3.407 b: ”Bestäm h” utan h i delen → ”Från vilken höjd faller partikeln?”
- **Avrundning och underförstådda enheter bort:** 3.88, 3.403, 3.407 b (värdesiffror finns i `svarVardesiffror`),
  3.388 b (två decimaler, till `kgInstruktion`), samt ”i m/i s/i m/s²/i km/h” i 3.43, 3.47 b, 3.106 d, 3.140 a,
  3.151 c, 3.163 c och 3.175.
- **Metatext bort:** 3.39, 3.73, 3.94, 3.95, 3.230, 3.362 (”Bestäm tangentens lutning.”), 3.47 (förenklad modell,
  till `kgInstruktion` som ”Använd värdena i diagrammet.”), 3.75, 3.76 och 3.144.
- 3.618: ”På vilken höjd ligger den?” → ”Vilken acceleration har bilen?”
- **Namn i stället för ”eleven”:** 3.38, 3.253, 3.439. **Minustecken:** 3.197, 3.198. **”Antag” → ”Anta”:** 18 uppgifter.
- **Tester:** `fysik1-kap3-figurer-2026-11-19` väntar nu figuren på alla delkort i 3.387. `felrapporter-2026-10-14-1634`
  går igenom ("Den andra bilen" i stället för "En annan bil").

### Kapitel 4 Krafter (klart) – `tools/fy1-granskning-kap4-2026-11-27.py`

Alla tolv områden är lästa: tyngdkraft, newton1, normalkraft, newton3, fjädrar, friktion, gravitation, blandat_kraft,
lutande_plan, moment, kraftvektorer och newton2. Alla svar som går att räkna fram utan figur är kontrollräknade, i
lutande plan, moment och newton2 med skript. Alla stämmer. Ändringar i 83 uppgifter:

- **Data saknades i huvudtexten:**
  - 4.207 c: fjäderkonstanten 25 N/m fanns bara i delkortet.
  - 4.749 b: stenen 1,0 m över marken fanns bara i delkortet.
- **Felaktiga eller otydliga delkort:**
  - 4.102 b hade 82 N i stället för 75 N och är nu en kedja.
  - 4.206 c upprepade en mening.
  - 4.635 skrev ”backen” om två backar. Nu står ”den första backen” och ”backen som lutar 20°”. Testet från
    2026-10-08 förbjuder ”andra backen” i b.
  - 4.149 sa både ”ger glidfriktion” och ”bortse från friktionen”. Nu står ”friktionen i trissan”.
- **Tabellvärden och konstanter till `kgInstruktion`:**
  - jordens radie och massa: 4.74, 4.186, 4.362, 4.374, 4.378, 4.739–4.741, 4.743, 4.748
  - g på månen och Mars: 4.840, 4.883, 4.885, 4.886, 4.888, 4.890
  - jordradien i 4.882 och himlakropparnas data i 4.22
  - protonens och elektronens massa: 4.736 b, 4.689 a
  - densiteterna i 4.523 och 4.524
  - Saknade tabellvärden har lagts till i `kgInstruktion`: Venus g (4.24), månens g (4.273, 4.812) och vattnets
    densitet (4.899).
  - 4.368 behåller 6370 km, eftersom elevens felräkning använder talet.
  - 4.378 hade enligt beslutet 2026-10-12 radien kvar för sitt tvådecimalssvar. Nu står radien i `kgInstruktion`
    (beslut 2026-11-27), så Kunskapsgymmet rättar fortfarande mot samma radie. Testet `fysik-formelsamling` är
    uppdaterat.
- **Modelljargong och metatext bort:**
  - ”Himlakroppen modelleras som sfäriskt symmetrisk.” och liknande. Kvar står ”Bortse från jordens rotation.” eller
    motsvarande.
  - ”Samma jordmodell gäller i alla delar.”, ”De behåller sin form.”, ”Bortse från luftens lyftkraft.” och ”Bortse
    från variationen i g med höjden.”
  - Metodtipset ”Skriv krafterna på vektorform och addera dem. Tänk på tecknen.” i 3.334–3.337 och 3.341–3.344.
  - Det allmänna villkoret i 4.297 och ”Bestäm värdena på grafens raka delar.” i 4.157.
- **Underförstådda enheter bort:** ”i N” och ”i m/s²” i 4.245, 4.281, 4.578–4.580, 4.585 och 4.594.
- **”krafterna på föremålet” → det namngivna föremålet:** 4.400–4.402, 4.404, 4.406, 4.408 och 4.421.
- **”elevens påstående” → ”Ines påstående”:** 4.21.
- **”Antag” → ”Anta”:** 20 uppgifter.

### Kapitel 5 Energi och rörelsemängd (klart) – `tools/fy1-granskning-kap5-2026-11-27.py`

Arbete, rörelseenergi, effekt, rörelsemängd, kollisioner och blandat energi är lästa. Alla svar som går att räkna fram
utan figur är kontrollräknade med skript, och alla stämmer. Ändringar i 37 uppgifter:

- **Rättningsfel: avrundat `rättSvar` underkände det exakta svaret.** I Kunskapsgymmet prövat med
  `kg-sjalvrattning-kontroll.cjs`: 736,5 J, 82,2 kg, 4805 N och 76,25 J underkändes.
  - Orsaken är tvådelad. Ett heltal i `rättSvar` (737, 82, 371, 4810, 402, 563, 246, 213, 3530, 12 200 000)
    behandlas som exakt. Ett decimaltal som ligger exakt ett halvt steg från fullvärdet (76,3, 17,6, 41,3, −2,84,
    1,13, 0,00228, 0,788, 0,0737, 0,563) jämförs strikt.
  - Nu lagras fullvärdet: 3.370 a, 5.142, 5.160 d, 5.209 c, 5.270, 5.272, 5.370 a, 5.375, 5.381 a, 5.418 b,
    5.440 c, 5.505 c, 5.509 b, 5.514 d, 5.72 a, 5.529 b, 5.533 a, 5.578 a, 6.457 b och 8.523.
  - Kontrollen visar att fullvärdet, båda grannarna vid halvsteg och det rekommenderade antalet siffror godtas. Fel
    grannvärden underkänns fortfarande. Facit (`s`) är oförändrade.
- **Beslutsändring (FP30, 2026-10-11):** FP30 lagrade vid exakta halvsteg det rätt avrundade grannvärdet med en
  tolerans som godtog fullvärdet och avvisade den andra grannen.
  - Sedan dess rättar Kunskapsgymmet fysik med `svarVardesiffror` utan toleransen. Användarbeslutet 2026-11-24 säger
    dessutom att ett exakt halvsteg får avrundas åt båda hållen.
  - Med FP30:s lagring underkändes därför fullvärdet, vilket är tvärtemot FP30:s eget syfte.
  - FP30:s 16 fall och 8.523 lagras nu oavrundat. Testerna `felrapporter-2026-10-11-1902`,
    `fysik-felrapporter-2026-10-08`, `fysik1-kollisioner`, `fysik1-rorelsemangd`, `fysik1-vatsketryck` och
    `fysik1-elektricitet-fordjupning` är uppdaterade med denna motivering.
- **Text:**
  - 2.29 e: ”Ange energin i joule.” bort.
  - 5.150: ”Moa använder sin θ = 0,060” kunde läsas som ett possessivt ”sin”. Nu står ”Moa räknar med att
    \(\sin\theta=0{,}060\)”.
  - 5.16 b: protonens massa flyttad till `kgInstruktion`.
  - ”Antag” → ”Anta” i 14 uppgifter.
- **Står kvar:** luftens densitet i 5.22 och 5.554 (gas), avloppsvattnets densitet i 5.594 och bensinens data i
  5.599 (uppgiftens egna material).
