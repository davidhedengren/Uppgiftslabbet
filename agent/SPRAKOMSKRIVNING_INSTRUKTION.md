# Språkomskrivning av uppgiftstexterna: instruktion och läge

Detta dokument räcker för att en annan AI ska kunna ta över. Läs det helt innan du ändrar något. Bakgrund och
mätningar finns i `agent/SPRAKGRANSKNING_2026-11-17.md`.

## Uppdraget (användarbeslut 2026-11-17)

Många uppgifter låter AI-genererade. Alla uppgiftstexter i de sju bankerna ska skrivas om så att de låter som
lärarens egna prov och uppgiftsblad i OneDrive (`Fysik\`, `Matematik\`).

- **För hand.** Läs varje uppgift och skriv den nya texten själv. Gör inga sök och ersätt över banken och generera
  ingen text automatiskt. Heuristiska fynd får aldrig massändras.
- **Ett område (`omr`) i taget.** Skriv om, kontrollera, synka och committa varje område för sig.
- **Rättningsinstruktioner syns bara i Kunskapsgymmet.** Uppgiftslabbet visar `t` för papper. Allt som bara behövs
  för automaträttningen läggs i fältet `kgInstruktion`, på uppgiften eller på ett delkort. Kunskapsgymmet lägger det
  sist i texten (`kgInstruktionerIn` i Kunskapsgymmets `index.html`), och Uppgiftslabbet ignorerar fältet.
- **Enheten skrivs inte i frågan.** Kunskapsgymmet visar redan ”Svara i …” vid svarsrutan utifrån `svarEnhet`.
  Kontrollera att `svarEnhet` stämmer, och skriv varken ”(Svara i …)” i `t` eller i `kgInstruktion`.
- **Skriv aldrig ”svara med tecken”.** Det får eleverna förstå själva. Om svaret har tecken skriver du bara
  riktningen i `kgInstruktion`, till exempel ”Höger räknas som positiv riktning.” eller ”Riktningen mot väggen
  räknas som positiv.”
- **Ändra inte svar, ID:n, nivåer eller facit utan skäl.** Facit ändras bara när pappersfrågan nu ger ett annat
  svarsformat (se `sbyt` nedan).

## Stilguide: så skriver läraren

Läraren beskriver en situation i en eller två meningar och ställer sedan en direkt fråga. Dessa exempel kommer ur
lärarens egna prov:

> En bil som väger 900 kg kör med hastigheten 20 m/s. Hur stor rörelseenergi har bilen?
> En sten släpps ned från ett 35 m högt torn. Hur lång tid tar fallet? Bortse från luftmotstånd.
> Helmut ska rulla en tunna med massan 100 kg upp för ett lutande plan. …
> Är linjerna parallella? Motivera ditt svar.

Gör så här:

- Skriv ”med massan 2,0 kg” eller ”som väger 2,0 kg”, aldrig ”en kloss på 2,0 kg”.
- Skriv ”horisontell/vertikal” i stället för ”vågrät/lodrät”, och ”står stilla”, ”från stillastående” eller
  ”släpps” i stället för ”från vila”.
- Ställ frågan med ”Hur stor …?”, ”Vilken fart får …?”, ”Beräkna …” eller ”Hur lång tid …?”. Variera, och
  använd inte ”Bestäm” överallt.
- Använd högst ett förbehåll, och sätt det sist: ”Bortse från luftmotståndet.” Ta bort förbehåll som inte ändrar
  svaret.
- Beskriv riktningar i ord, som ”åt höger”, ”mot väggen”, ”bakåt” eller ”rakt tillbaka”. Skriv inte tecken som
  ”+4,0 m/s”, utom när tecknet är själva poängen i uppgiften.
- Använd verkliga saker och gärna namn: pråm och bogserbåt, golfboll, Olle, en hockeypuck. Undvik ”kropp”, ”objekt”
  och ”en uppsättning”.
- Skriv ”resulterande kraft” eller ”medelkraft”, inte ”sammanlagd kraft”. Skriv ”totala rörelsemängden” eller
  ”tillsammans”, inte ”sammanlagda”.
- Matematik: skriv ”För funktionen f gäller att f(x) = …” eller ”Funktionen f ges av …”, inte ”Funktionen är …”.
  Skriv ”räknare” eller ”GeoGebra”, inte ”digitalt verktyg”. Skriv hellre ett namn än ”En elev säger”, och skriv
  ”Motivera ditt svar.”
- Flerval: ställ frågan (”Vilken knuff ger störst impuls?”). Ta bort ”Välj ett alternativ.” och ”Markera det
  korrekta alternativet.”, eftersom Kunskapsgymmet visar knappar och papperet visar A–D.

Skriv aldrig följande:

- formler eller konstanter i frågan, som ”med p = mv” eller ”Stefan–Boltzmanns lag: …”;
- lösningen i frågan, som ”Kraft · stopptid måste därför vara samma”;
- definitioner, som ”Impuls är kraftens sammanlagda påverkan”;
- metatext, som ”Räkna på …”, ”Miniräknare får användas”, ”Behåll oavrundade värden” eller ”Fördjupning utanför …”;
- precisionskrav, som ”med tre värdesiffror”, eftersom precisionen ligger i `svarVardesiffror`.

Behåll det som avgör svaret, men i vardagligt språk:

- Ett förbehåll som ändrar svaret: ”Ta hänsyn till tyngdkraften.”, ”Under studsen verkar både golvets kraft och
  tyngdkraften på bollen.”, ”Räkna med konstant acceleration.”
- Tidigare regressionstester låser ofta just sådana villkor, till exempel `felrapporter-fy1-2026-10-21-2114.test.js`.
  Om ett test kräver ett villkor ska villkoret stå kvar, gärna omformulerat. Uppdatera ett test bara när det låste
  en ordalydelse och innebörden finns kvar. Skriv i så fall en kommentar i testet.

Delkort (`spelDelar`) ska vara självbärande. Behåll varje korts data och skriv om i samma stil. Delkort med en
gemensam inledning (`[I+F]` i utskriften) byggs automatiskt av `intro` och `f`.

## Arbetsgång för ett område

Kör alla kommandon från `C:\Users\Hedav\code\Uppgiftslabbet` med `PYTHONUTF8=1`. Verktygen fungerar också på Linux (molnsessioner), eftersom sökvägarna byggs med `os.path.join`.

1. **Förbered.** Kör `git status`, `git fetch` och jämför med upstream i båda repona. Kontrollera att
   Kunskapsgymmets bankkopia inte har egna ändringar. Ta bort CR innan jämförelsen, till exempel
   `cmp <(git show HEAD:uppgifter.js | tr -d '\r') <(tr -d '\r' < ../kunskapsgymmet/uppgifter.js)`.
2. **Skriv ut området.** Kör `python tools/sprak/dump.py fy1 kollisioner > %TEMP%\kol.txt` och läs filen.
   Utskriften visar:
   - `T:`, som är huvudtexten med `[F1]` i stället för figurer;
   - `INTRO:`, som är `spelIntro`;
   - `[I+F]`, som betyder att delkortet är `intro` plus fråga;
   - `T = INTRO + lista av fragor`, som betyder att huvudtexten byggs av intro och frågor;
   - svar, `svarEnhet` och flervalsalternativ.
3. **Skriv om.** Skapa `tools/sprak/omskr/<bank>_<omr>.py` med en ordlista `R`. Använd
   `omskr/fy1_rorelsemangd.py` som förebild. Följande nycklar finns per uppgifts-ID:
   - `t`: hela nya huvudtexten, där `[F1]`, `[F2]` … är originalets figurer i ordning.
   - `fore`, `li` och `efter`: ny text före listan, nya `<li>`-texter och text efter listan. Originalets
     `<ol …>`-tagg behålls. Antalet `li` måste stämma.
   - `intro`: ny `spelIntro`. Figurerna kommer ur originalets intro.
   - `kg`: `kgInstruktion` för huvuduppgiften. Den visas när Kunskapsgymmet visar huvudtexten, alltså för
     uppgifter utan delkort eller med ett enda delkort.
   - `d`: `{etikett: {t, f, kg}}` för delkort. Ett `[I+F]`-kort behöver bara `f`. Ett kort med egen `t` behöver
     `t`, och även `f` om frågan ändras.
   - `sbyt`: `[(gammal delsträng, ny delsträng)]` i huvudfacit `s`, när pappersfrågan nu ger ett annat svarsformat.
     Exempel: 5.16, där Kunskapsgymmet frågar efter talet a men papperet efter rörelsemängden.

   Uppgifter som redan låter naturliga lämnas utanför `R`.
4. **Torrkör.** Kör `python tools/sprak/apply.py fy1 tools/sprak/omskr/fy1_kollisioner.py`. Läs varje varning:
   - ”tal borta/nya” får bara bero på avsiktliga ändringar, till exempel att en instruktion flyttats till `kg` eller
     att ett tal nu bara står i intro;
   - ”mönster” betyder att en förbjuden fras finns kvar och ska åtgärdas.
5. **Skriv.** Kör samma kommando med `--skriv`. Verktyget ersätter bara strängliteralerna i de berörda objekten, så
   formatet behålls. Kör sedan `node --check uppgifter.js` och `git diff --check`, och läs `git diff`.
6. **Testa.**
   - Lägg till området i `KLARA` i `tools/sprak-2026-11-17.test.js`.
   - Kör det testet och alla `tools/*.test.js` som nämner områdets ID:n.
   - Jämför felen med läget före ändringen genom att köra samma test mot `git show HEAD:uppgifter.js`. Kända fel
     sedan tidigare är `fysik1-kap23-facit-2026-11-04` och ”Äldre fysikprosa …” i `fysik1-prosa.test.js`. I
     Kunskapsgymmet fallerade redan 12 test före ändringen, bland annat Ma2 GeoGebra och ”Fysikrapport 5.133”.
7. **Synka.** Kopiera banken till `../kunskapsgymmet/` med `cp` och kontrollera med `cmp`. Höj `BANK_VERSION` i
   Kunskapsgymmets `index.html`, till exempel `"2026-11-18-sprak-fy1-kol"`.
8. **Kontrollera visningen** (rekommenderas för nya typer av instruktioner):
   1. Starta förhandsvisningen `code-static`, port 8765.
   2. Öppna `/kunskapsgymmet/index.html` och kör `await selectCourse('fy1',{render:false})`.
   3. Sätt `state.currentTask` till en uppgift i banken och kör `renderTraining()`.
   4. Kontrollera att instruktionen står under frågan och att ”Svara i …” står vid svarsrutan.
9. **Logga och committa.**
   - Fyll i lägestabellen nedan med område, antal uppgifter och anmärkningar.
   - Committa och pusha Uppgiftslabbet först och sedan Kunskapsgymmet, utan att fråga. Avsluta meddelandet med
     `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Använd aldrig force push. Verifiera `0 0` mot upstream.

## Fallgropar

- Skriv aldrig Python med bash-heredoc, eftersom backslashes halveras. Använd filverktyget.
- Om verktyget säger att en literal eller ett ankare hittades två gånger, har två delkort fått identisk text. Ge dem
  olika text, eller ankra `kg` vid kortets `t`. Ankringen vid `t` sker automatiskt när kortet har `t`.
- Om du skriver om `t` men inte delkorten, kommer Kunskapsgymmet att visa den gamla texten. Gå igenom båda.
- Kontrollera att en uppgift med negativt `rättSvar` har en riktning i `kg` om frågan inte nämner någon. Skriv
  inte ”tecken”, eftersom testet stoppar det.
- Läs huvudfacit när frågans form ändras, till exempel när ”ange talet a” blir ”beräkna rörelsemängden”.
- Om du är osäker på om en uppgift låter naturlig, jämför med lärarens korpus. Kör
  `python tools/sprak/korpus.py ut.json`, som läser OneDrive, och sök i den.

## Läge och ordning

**Parallella sessioner (2026-11-17):** en session tar Fy1 område för område, en annan Ma1. Skriv in ditt område i tabellen när du är klar och hämta (`git pull --rebase`) före varje commit. Vid konflikt i `KLARA` i `tools/sprak-2026-11-17.test.js` slås listorna ihop, och vid konflikt i `BANK_VERSION` i Kunskapsgymmet väljs ett nytt namn.

**Användarbeslut 2026-11-17 (rättat samma dag): elläran, Fy1 kapitel 8 Elektricitet (ID 8.x), görs först, eftersom den undervisas nu. Användaren sa ”kapitel 9” men menade elläran, som är kapitel 9 i boken. Därefter resten av kärnfysiken (bankens kap 9), sedan resten av kapitel 4.** Läge 2026-11-17: kap 8 och kap 9 är helt klara, kap 4 har fått riktad omgång och genomläsning (utom Newtons andra lag 4.654–4.734). Hela Fy1 (kap 2–9) har fått riktad omgång och genomläsning 2026-11-18, och hela Fy2 samma dag. Nästa: Ma2 (uppgifterma2.js), därefter Ma3c, Ma4 och Ma5. Efter varje kapitel ska användaren få exempel på gjorda ändringar. Prioritet i övrigt efter täthet av AI-mönster: först resten av Fy1 område för område, sedan Fy2, Ma1, Ma2, Ma3c, Ma4 och Ma5.
Inom Fy1 kommer kollisioner (kap 5) först, sedan resten av kapitel 5, därefter 4, 3, 6–9 och sist 2.

| Datum | Bank | Område | Uppgifter | Anmärkning |
|---|---|---|---:|---|
| 2026-11-17 | fy1 | rorelsemangd | 92 av 93 | 5.605 lät redan naturlig. 5.16 fick facitjustering. Fyra test uppdaterades eftersom de låste gammal ordalydelse med oförändrad innebörd. 5.603 och 5.608 fick `visaAlternativ`. |
| 2026-11-17 | fy1 | kollisioner | 121 av 121 | Stöt-förbehållen är borttagna. Villkor som påverkar svaret står kvar, till exempel tyngdkraftens impuls i 5.448 och ”nytt försök … stilla före hoppet” i 5.432. Testerna `fysik1-kollisioner` och `fysik-felrapporter-2026-10-08` uppdaterades: teckenriktningen kontrolleras nu i `kgInstruktion`. |
| 2026-11-17 | ma1 | enhetsbyten | 107 av 149 | ”Skriv svaret som ett vanligt tal, inte i tiopotensform.” borttaget; kvar i `kgInstruktion` bara för 0.560 och 0.562 (formatet decimalform godtar inte tiopotens). 0.565 fick tolerans 0,05 när kravet på en decimal togs bort. 0.540 behåller ”kvadratcentimeter … kvadratmeter” (låst av `ma1-dolda-pastaenden`). 42 uppgifter lät redan naturliga. |
| 2026-11-17 | ma1 | prefix | 63 av 96 | Elva ”Två tunna skikt …” och tio ”tolkas det av misstag som …” fick egna sammanhang (förpackning, väggskiva, lysdiod …). ”Vanligt tal” kvar i `kgInstruktion` bara för 0.244 och 0.246. |
| 2026-11-17 | ma1 | tiopotenser_prefix | 38 av 76 | Definitionen 1 ≤ a < 10 och ”Ange a och n separat.” är borttagna; fälten förklaras i `kgInstruktion`. Elva ”En elev skriver … Vilken korrigering bevarar talets värde?” har namn och en direkt fråga. |
| 2026-11-17 | ma1 | proportionalitet_grunder | 35 av 81 | ”(Svara i …)” och avrundningskrav borttagna; ”Hur många kilometer …?” där enheten är poängen. Ja/nej-frågor har ”Motivera ditt svar.” och ”Börja svaret med ja eller nej.” i `kgInstruktion`. 0.990 har ”Avrunda till hela gram.” i `kgInstruktion`, eftersom facit är avrundat. 0.991 och 0.992 behåller avrundningen i frågan (”Avrunda till …”), eftersom `felrapporter-2026-10-11-1902` låser den. |
| 2026-11-17 | ma1 | brakform | 18 av 54 | ”Ange a och b.” och ”Välj ett alternativ.” borttagna. |
| 2026-11-17 | ma1 | forhallanden | 13 av 63 | ”(Svara i …)” borttaget, ”sammanlagt” heter ”totalt”, 0.829 skrivet om (päron byts mot äpplen). |
| 2026-11-17 | ma1 | brakrakning | 45 av 135 | ”Ange ett exakt värde.” ersatt av `kgInstruktion` ”Svara exakt med ett bråk eller ett heltal.” Drillserierna 0.1266–0.1289 är oförändrade. |
| 2026-11-17 | ma1 | negativa_tal | 13 av 120 | 0.62 behåller ”och skriver −7 · (−5) = 35” (låst av `ma1-kap0-mangdtraning`). |
| 2026-11-17 | ma1 | tal_rakneordning | 10 av 108 | Namn i stället för ”en elev”, inga ”Välj ett alternativ.”. |
| 2026-11-17 | ma1 | decimaltal_positionssystem, avrundning, overslag_grunder, andelar | 5 av 100, 7 av 71, 12 av 65, 13 av 78 | Avrundningskrav som rättningen behöver (facit avrundat) står i `kgInstruktion`. ”Anta” heter ”Antag”. |
| 2026-11-17 | ma1 | kapitel 1: algebraiska_uttryck, ekv_brak, ekv_flera_variabeltermer, ekv_parenteser, ekv_problemlosning, faktorisering, forenkla_uttryck, formler, intervall, linjara_ekvationer, linjara_olikheter, monster_samband, multiplicera_uttryck | 121 uppgifter (2, 2, 0, 4, 22, 7, 9, 12+, 12, 13, 9, 13, 10) | Skript `ma1_kap1.py` och `ma1_kap1_tillagg.py`. ”(Svara med ett heltal.)”, ”Välj ett alternativ.” och definitioner borttagna. ”Svara med en decimal.” ligger i `kgInstruktion` för 1.99, 1.103a, 1.443, 1.444, 1.1025 och 1.1029 (facit avrundat). Testerna `ma1-ekvationsproblem-2026-11-06` (tre ordalydelser, samma villkor) och `ma1-geometri-variation-2026-10-24` (svarsform krävs inte i omskrivna områden) uppdaterades. |
| 2026-11-17 | ma1 | kapitel 2: funktionsbegreppet, definitionsmangd_vardemangd, representationer, grafisk_ekvationslosning, jamfora_modeller, linjara_funktioner, rata_linjens_ekvation, bestamma_linjar_funktion, exponentialfunktioner, potensfunktioner | 171 uppgifter (skripten `ma1_kap2a.py`, `ma1_kap2b.py`, `ma1_kap2c.py`) | ”Funktionen är …” heter ”Funktionen f ges av …”. ”Digitalt verktyg” heter GeoGebra eller räknare. Metatexten ”Grafen visar hela det område som ska användas i uppgiften.” är borttagen i 26 uppgifter. Den står kvar som ”Figuren visar hela grafen.” där antalet lösningar beror på det (2.52, 2.97, 2.101, 2.137, 2.139, 2.141, 2.144, 2.145). Formler som bara upprepar texten är borttagna (2.455, 2.545, 2.634). Avrundning ligger i `kgInstruktion` där toleransen är tät, och ”stigande ordning” heter ”Skriv lösningarna i storleksordning, den minsta först.”. 2.29a saknade \(K(x)\) och är nu självbärande. Testet `ma1-digital-ekvationslosning-2026-10-25` kontrollerar nu avrundningen i `kgInstruktion`. Observera: 2.188b har facit 25,3 med toleransen 0,005, så det exakta värdet 25,3125 underkänns utan avrundning. Facit är inte ändrat. |
| 2026-11-17 | ma1 | kapitel 3: potensregler, potensekvationer, procent, index, forandringsfaktor, upprepade_forandringar, genomsnittlig_forandring, ranta, amortering | 175 uppgifter (`ma1_kap3a.py`, `ma1_kap3b.py`) | ”Ange n.”, ”Ange a och n separat.” och definitionen 1 ≤ a < 10 är borttagna; fälten förklaras i `kgInstruktion` (”Svara med exponenten.”, ”Skriv resultatet som k·xⁿ …”). Negativa procentsvar har ”En minskning skrivs som ett negativt tal.” i `kgInstruktion`. 3.28 gav lösningen (”multiplicera med förändringsfaktorn 1,25”), och 3.19 hade volymformeln; båda är borttagna. Kunskapsgymmet godtar alla korrekt avrundade svar när toleransen är mycket liten (provat: ”8” för 8,447 i 3.65), så avrundning står i `kgInstruktion` bara där toleransen kräver en viss precision. `felrapporter-2026-10-12-0958` låser att eleven får veta precisionen i 3.40c, 3.88b–c och ”hela kronor” i 3.39, 3.203, 3.217, 3.223 och 3.518–3.520. Det står nu i `kgInstruktion`, och testet läser både frågan och `kgInstruktion`. |

| 2026-11-17 | fy1 | rorelseenergi | 115 av 115 | Formler är borttagna ur frågorna (”med Eₖ = mv²/2”, ”med F = E/s”, definitionen av mekanisk energi). 5.609 avslöjade svaret i frågan. 5.537 hade förbehållet ”Bortse från luftmotståndet” fast uppgiften handlar om luftmotstånd. Villkor som påverkar svaret står kvar, till exempel ”konstant retardation” (5.488) och ”Bromskraften F är oförändrad” (5.224). |
| 2026-11-17 | fy1 | arbete | 106 av 109 | ”gör arbete” är bytt mot ”uträttar arbete”. Formeln är borttagen ur intro (5.535) och meningen ”Här är två frågor …” likaså. Arbetets tecken anges inte. 5.499 har fått de verkliga platserna Death Valley och Mount Whitney. Testerna `fy1-svarsinstruktioner` (5.184) och `fysik1-arbete` (”andel”) är uppdaterade. |
| 2026-11-17 | fy1 | effekt | 117 av 120 | Svarsinstruktioner som ”(Svara i kW.)” och ”Svara med ett positivt värde” är borttagna. ”Verkningsgrad är …” och ”Räkna på …” likaså. ”En elev” har fått namn. ”Svara i decimalform.” står bara i `kgInstruktion` (5.327, 5.588 b). Testerna `fysik1-effekt`, `fysik1-effekt-variation` och `a-uppgifter` (5.640) är uppdaterade. |
| 2026-11-17 | fy1 | blandat_energi | 74 av 76 | Uppgifterna på A-nivå behåller nödvändiga modellvillkor men har fått kortare och vardagligare text. 5.117 behåller ”på passageraren under inbromsningen”, som är låst av två felrapporttester. Teckenriktning står i `kgInstruktion` (5.110, 5.132, 5.166). |
| 2026-11-17 | fy1 | tyngdkraft | 40 av 46 | ”modellplanet” heter nu ”främmande planet”. ”I denna uppgift används …” har blivit en vanlig mening, till exempel ”Tyngdaccelerationen är 1,62 m/s² på månen.”, eftersom testerna låser formen ”… m/s² på månen/Mars”. ”Kraftmätare” behålls, eftersom läraren använder ordet. |
| 2026-11-17 | fy1 | hela kapitel 9 (12 områden) | 291 av cirka 610 | Riktad omgång: varje träff i listan (”(Svara i …)”, ”Markera det korrekta alternativet”, ”Välj ett alternativ”, ”sammanlagd”, ”från vila”, ”en elev”, ”på X kg”, ”Räkna bara med radioaktivt sönderfall”) är beslutad per uppgift i `omskr/fy1_kap9.py`. Fyra rättningsinstruktioner har flyttats till `kgInstruktion` (9.49 c, 9.337, 9.340, 9.582). `ers` i `apply.py` gör delsträngsbyten per uppgift. Genomläsningen av hela meningsbyggnaden är gjord för alla tolv områden (skripten `fy1_k9_*.py`). I nuklider är proton-, neutron- och väteatommassorna borttagna ur frågorna om massdefekt och bindningsenergi (konstanter slås upp i formelsamlingen). I fusion och fission står de kvar, eftersom de där ingår i samma lista som reaktionens övriga atommassor. Aktivitet och stråldoser: ”Räkna med …” heter ”Antag att …” eller ”Viktfaktorn är …”, ”I en modell” är omskrivet, ”den” är utskrivet som ”dosen per timme” och enhetsprefix (kBq, GBq, µSv/h) är borttagna ur frågan. |
| 2026-11-17 | fy1 | hela kapitel 8 Elektricitet (10 områden) | 356 av 739 (laddning 36, coulomb 45, strom 20, kretsar 30, multimeter 45, seriekoppling 15, parallellkoppling 9, kopplingar 88, falt 26, potential 42) | Två steg: `omskr/fy1_kap8.py` (riktad omgång) och `omskr/fy1_k8_genomlasning.py` (genomläsning). Lärarens prov skriver ”en lampa på 10 Ω”, ”ett batteri på 9 V” och ”ersättningsresistansen”, så ”på X Ω/V/W” står kvar (bara ”på X g/kg” ändras). ”(Svara i …)” är borttaget där enheten är en svarsenhet, ”Markera det korrekta alternativet”/”Välj ett alternativ” likaså. ”sammanlagd kraft/fält” heter ”resulterande”, ”sammanlagd resistans” heter ”ersättningsresistans”. Svarsordning (8.40, 8.49, 8.76, 8.84, 8.141, 8.166), riktning (8.104, 8.338, 8.342, 8.346), ”Svara med ett ord” (8.124) och flerval med flera rätt (8.82 c, 8.100, 8.530, 8.532, 8.533) står i `kgInstruktion`. Precisionskrav är borttagna. Laddningens tecken och energiändringens tecken anges inte. Protonens massa är borttagen ur 8.22 b och 8.491 b, I = Q/t ur 8.464 och definitionen av Ah ur 8.79 och 8.465. 8.108 hade trasig HTML och 8.159 c e-notation. Fördjupningarna 8.294 och 8.439–8.444 behåller sina formler (de ingår inte i kursen). Testerna `fysik1-omgang-11-niva3` och `fysik1-strom-variation` godtar nu `visaAlternativ`/`alternativ` i stället för ”Välj …” i texten. `apply.py`: ett delkort med egen t som inte innehöll den bytta frasen behåller sin t. |
| 2026-11-17 | fy1 | hela kapitel 4 Kraft (11 områden + kraftvektorer 3.3xx) | 648 av 929 (newton2 132, friktion 92, kraftvektorer 87, lutande_plan 67, moment 66, blandat_kraft 52, newton1 39, fjadrar 37, gravitation 29, newton3 24, normalkraft 23) | Fyra skript i ordning: `omskr/fy1_kap4.py` (regelmässiga byten, görs på platshållartexten så att figurer aldrig ändras), `fy1_k4_newton2.py`, `fy1_k4_hand.py`, `fy1_k4_rest.py` och `fy1_k4_rest2.py` (handbeslut). Standardmeningarna om snören och trissor (”Snöret är masslöst och sträckt. Trissan är masslös och friktionsfri.”) heter nu som i lärarens 4.106: ”Bortse från snörets och trissans massa och från friktionen.” ”Bara tyngdkraften och snörkraften verkar” och liknande är borttagna eller blev ”Bortse från luftmotstånd.” vågrät/lodrät heter horisontell/vertikal, ”en låda på 30 kg” heter ”en låda med massan 30 kg” (personer: ”som väger”), ”från vila” heter ”från stillastående” (”släpps från vila” heter ”släpps”), ”sammanlagd kraft” heter ”resulterande kraft” och i övrigt ”total”. Riktningar och teckenkonventioner står i `kgInstruktion` (till exempel ”Höger och uppåt räknas som positiva riktningar.” i kraftvektorer, kopplingskraftens tecken i 4.654 och 4.660, vinkel moturs från positiva x-axeln). Bestämd form som ”lådan på 20 kg” står kvar, eftersom den pekar ut ett föremål. Mönstret i `sprak-2026-11-17.test.js` och `apply.py` gäller därför bara obestämd form, och ”Bortse från andra” gäller bara ”Bortse från andra krafters …”. 4.368 behåller ”En elev skriver g = 9,82 …” (låst av `fysik-formelsamling`). Parentesmassor som ”En bil (1,4 ton)” står kvar. Genomläsning gjord samma dag med `fy1_k4_las_*.py` (newton13, normal_grav, fjadrar, friktion, moment, blandat, vektorer; cirka 170 uppgifter till): förbehåll före själva situationen är flyttade sist eller borttagna, standardmeningen ”Rita av figuren och sätt ut alla krafter som verkar på den markerade kroppen. Märk ut varje kraft med namn och rita pilen från rätt angreppspunkt.” heter ”Rita av figuren och sätt ut alla krafter med namn.”, ”Behandla kropparna som punktmassor. Avståndet mäts mellan deras masscentrum.” och ”I en sfäriskt symmetrisk jordmodell” är borttagna, ”som väger nästan ingenting” heter ”lätt”, ”komponent” heter komposant, ”Glidfriktionen är den enda bromsande kraften och är konstant.” heter ”Bortse från luftmotstånd.”. 4.105 rättades (en tidigare regel skrev ”Bortse från friktion” i en friktionsuppgift). 4.969–4.972 frågar efter komposanternas tecken och har därför axlarnas riktning i texten: ”Den positiva x-axeln pekar åt höger och den positiva y-axeln uppåt.” Newtons andra lag 4.654–4.734 och 4.910 är bara kontrollerade mot mönstren, inte genomlästa mening för mening. |
| 2026-11-18 | fy1 | hela kapitel 3 Rörelse (6 områden) | 289 av 524 (vektorer 91, konstacc 75, vt_diagram 37, acceleration 29, st_diagram 28, at_diagram 26) | Skript i ordning: `fy1_kap3.py` (kopia av kap 4-generatorn), `fy1_k3_riktning.py`, `fy1_k3_fix.py`, `fy1_k3_las_konstacc.py`, `fy1_k3_las_diagram.py`, `fy1_k3_las_acc_vektorer.py`, `fy1_k3_namn.py`. Lärarens prov skriver aldrig ”positiv riktning” eller ”med tecken” (kontrollerat i korpusen), så alla riktningsval (”Välj nedåt som positiv riktning.”, ”med färdriktningen positiv”, ”Uppför är positivt.”) står i `kgInstruktion`, till exempel ”Nedåt räknas som positiv riktning.” eller ”Färdriktningen räknas som positiv.”. Teckenuppmaningar (”med tecken”, ”Ange tecknet.”, ”med rätt tecken”) och precisionskrav (”med en decimal”, ”med tre värdesiffror”) är borttagna. Där tecknen står i själva datan är riktningen kvar på papperet utan ”positiv riktning”: 3.226 har ”2,0 m/s² österut och 4,0 m/s² västerut”, 3.423 och 3.435 har ”Hastigheten räknas positiv åt höger/mot väggen.”, 3.439 har ”Läget räknas positivt åt höger.”. Ett ensamt inledningsstycke ”<p>Bestäm.</p>” är borttaget (finns också i kap 2, medelhastighet). Läraren skriver lika ofta ”från vila” som ”från stillastående”; omskrivningen har ”från stillastående”. Testerna `fysik1-komposanter-2026-10-24` (precisionskrav) och `felrapporter-2026-10-26-1531` (delkortets fråga får sluta med ”Bestäm … .”) är uppdaterade. `tools/sprak/kvar.py fy1 <kap>` listar kvarvarande förbjudna mönster. |
| 2026-11-18 | fy1 | hela kapitel 2 Fysikens grunder (4 områden) | 176 av 401 (densitet 84, medelhastighet 45, matnogg 29, enheter 18) | Skript i ordning: `fy1_k2_forst.py` (före generatorn: målenheten flyttas in i frågan i enhetsuppgifter, tomt ”<p>Bestäm.</p>” bort), `fy1_kap2.py`, `fy1_k2_rest.py`, `fy1_k2_rest2.py`, `fy1_k2_las_mat_medel.py`, `fy1_k2_las_densitet.py`, `fy1_k2_namn.py`. I enheter är målenheten själva uppgiften, så där står den i frågan (”Hur stor är tvärsnittsarean i mm²?”). I matnogg är värdesiffror och avrundning själva uppgiften och står kvar; ”… och ange svaret.” (2.248, 2.249, 2.267) betydde ”med rätt antal värdesiffror” och skrivs nu ut. ”Avrunda till hela gram/kilogram” står i `kgInstruktion`. 2.55 b hade förlorat sin målenhet när parentesen togs bort och har nu ”Ange samma densitet i kg/m³.”. Formler i frågan (klotets och cylinderns volym) är borttagna. Testerna `fysik1-densitet-2026-10-21` och `fy1-svarsinstruktioner-2026-10-26` (2.321) godtar nu enheten via `svarEnhet` eller i frågan. **Lärdom:** när generatorn tar bort ”(Svara i X.)” måste frågan fortfarande gå att besvara på papper; kontrollera omvandlingsuppgifter och ”Ange samma …”. |
| 2026-11-18 | fy1 | kapitel 6 Tryck och 7 Värme (6 områden) | 486 av 751 (gaslagen 107, varme 92, arkimedes 74, fasandring 74, tryck 72, vatsketryck 67) | Skript: `fy1_kap67.py` (generatorn), `fy1_k67_rest.py`, `fy1_k67_rest2.py`, `fy1_k67_las.py`. ”(Svara i J/(kg·K).)” togs bort med ett mönster som klarar parentes i enheten. Två efterfrågade enheter står i frågan (”i kPa och i mmHg?”). ”Räkna med att ingen energi går till kärlet eller omgivningen.” heter ”Bortse från energi som går till kärlet och omgivningen.”, övriga ”Räkna med att …” heter ”Antag att …”. ”Räkna bara med tyngdkraften och lyftkraften.” heter ”Bortse från vatten-/luftmotståndet.”. ”enligt modellen” är struket i beräkningsfrågor, men frågor om modellens begränsningar står kvar. Testerna `a-uppgifter-2026-11-11` (7.232), `fy1-svarsinstruktioner` (6.112) och `fysik1-varmeoverforing-variation` är uppdaterade. |
| 2026-11-18 | fy2 | hela banken (37 områden) | 490 av 1765 (magnituder 45, interferens 36, kast 32, jordens_magnetfalt 30, avstandsmatning 29, farg_ljusstyrka 28, exoplaneter 28, kosmologi 24, kast_elfalt 22 …) | Skript i ordning: `fy2_alla.py` (kap 4-generatorn för hela banken), `fy2_parenteser.py` (parenteser: enhet/precision bort, svarsformat som rättningen behöver till `kgInstruktion`, ”både i joule och i elektronvolt” som vanlig mening), `fy2_rest.py` (positiv riktning till kg i 1.119 och 2.304, sammanlagd → total/resulterande), `fy2_las.py` (”Hubblekonstanten i modellen är” → ”Hubblekonstanten är”, Anta → Antag, ”En elev” får namn). Bohrs modell och kosmologiska modeller står kvar som fysikbegrepp. Fy2 ligger i `KLARA` i `sprak-2026-11-17.test.js`. |
| 2026-11-18 | fy2 | handgenomläsning av hela banken, kap 1–6 | 411 uppgifter (skript `fy2_hand_*.py`, `fy2_formelstycken.py`) | Varje område lästes med `las2.js` (synlig text, delkort visar bara det som skiljer). Inledande formelrader är borttagna: gitterekvationen, fotonens energi, Wien, Stefan–Boltzmann med σ, Hookes lag, harmonisk svängning, pendel- och fjäderperiod, pipor och strängar, ljudnivå, generator, plattfält, tidsdilatation. Kvar står samband som inte står i formelsamlingen eller definierar en beteckning: platta spolens fält, ljudhastighetens temperaturberoende, Bohrs radier och farter, Keplers lag i solenheter, Schwarzschildradien. Konstanter i frågan borttagna: proton- och elektronmassa, viloenergier, I₀, Wiens konstant, AU i meter. Svarsrader under frågan (”medurs eller moturs”, ”nordpol eller sydpol”) och ”Välj rätt riktning …” är borttagna eller flyttade till `kgInstruktion`. ”En 0,60 kg kloss” och ”(400 g) i en fjäder (46,0 N/m)” skrivs ”med massan” och ”med fjäderkonstanten”. Språktestet och `kvar.py` fångar nu också ”Positiv riktning”, ”Från vila” och ”Med tecken” med stor bokstav; fyra sådana missar i Fy1 är rättade (`fy1_versaler.py`). |
| 2026-11-18 | ma1 | omkrets_area | 30 av 39 | Kontrollerat alla 39 uppgifter. 4.568 frågar efter både cirkelns area och ökningen i procent. I 4.588 avser de extra 10 procenten uttryckligen golvarean. 4.732 efterfrågar fortfarande kvadratmeter vid bytet av enhet. |
| 2026-11-18 | ma1 | volym | 34 av 39 | Invändiga mått anges där frågan gäller hur mycket som ryms. 4.550 visar fortfarande alla fyra alternativ även på papper. Avrundningen till tiotal liter i 4.595 ligger i kgInstruktion. Testet för 4.550 läser nu också in bildhjälpfunktionen som utskriftsvyn använder. |
| 2026-11-18 | ma1 | kvadratrotter | 26 av 33 | I 4.557, 4.559, 4.561 och 4.754 efterfrågas den positiva lösningen direkt. I 4.601 står nockens läge i frågan. 4.761 visar alla fyra uttrycken på papper. |
| 2026-11-18 | ma1 | pythagoras | 26 av 48 | I 4.165 anges vilken garderobsdiagonal som behövs. Båda plåtarnas mått och beteckningar följer med till varje delkort i 4.401. I 4.402 visas påståendena även på papper. Utskriftstestet läser in bildhjälpfunktionen. |
| 2026-11-18 | ma1 | sinus_cosinus_tangens | 39 av 58 | I 4.38b anges kateternas längder 8 och 15 så att hypotenusan går att bestämma även på det fristående kortet. I 4.218 framgår vilken katet som ligger mitt emot vinkeln. 4.47 och 4.226 visar alternativen på papper. |
| 2026-11-18 | ma1 | arcusfunktioner | 38 av 46 | I 4.800 och 4.801 får eleven själv välja sambandet från linjens lutning respektive katetens andel av hypotenusan. I 4.804 anges höjdskillnaden från handen. Flervalet i 4.116 visar fortsatt samtliga uttryck. |
| 2026-11-18 | ma1 | strackor_vinklar | 37 av 45 | Även provuppgiften 8.12 tillhör området. I 4.33 är det vägen som lutar, i 4.62 framgår vilken lina som har vilken vinkel, och 4.167 har två fullständiga delkort med mätpunkter och frågor. |
| 2026-11-18 | ma1 | koordinatgeometri | 15 av 46 | 4.811 anger kartans skala per steg längs en axel. Triangelpåståendena i 4.85 och 4.815 visas också på uppgiftsbladet. Decimalkrav ligger vid träningens svar i 4.460–4.462 och 4.816. |
| 2026-11-18 | ma1 | vektorer | 16 av 50 | I 4.92 anges hur kartans axlar ligger. 4.773 frågar efter en annan vektor än den givna. Alternativen visas i 4.481 och 4.776. |
| 2026-11-18 | ma1 | vektor_addition_subtraktion | 13 av 42 | 4.129 frågar efter robotens körsträcka och 4.194 efter vektorn från start till mål. Pappersfrågorna och motsvarande delkort använder samma formulering. |
| 2026-11-18 | ma1 | vektor_absolutbelopp | 17 av 47 | Även provuppgiften 8.13 tillhör området. I 4.508 och 4.798 ser eleven vilka vektorer som ska jämföras. I 4.799 efterfrågas avståndet fågelvägen. |

### Tecken: riktning eller fysik

- **Riktningstecken** (hastighet, rörelsemängd, impuls och kraft längs en linje) beror på vald riktning. Om svaret har
  tecken ska `kgInstruktion` säga vilken riktning som är positiv, till exempel ”Höger räknas som positiv riktning.”
- **Arbetets tecken** (friktionens eller bromsande krafters arbete) är fysik och ingen överenskommelse. Där behövs
  ingen instruktion, eftersom eleven ska inse att arbetet är negativt (användarbeslut: ”det får de förstå själva”).
- **Fältkontroll:** kör `python tools/sprak/faltkoll.py <bank före omskrivningen> uppgifter.js [id med avsiktligt
  ändrat facit …]`. Kontrollen visar om något annat än `t`, `spelIntro`, `kgInstruktion`, `visaAlternativ` eller
  delkortens `t`, `fraga` och `kgInstruktion` har ändrats. Ta fram banken före omskrivningen med
  `git show 075bc77~1:uppgifter.js`. Verktyget ankrar varje ersättning vid fältnamnet, så att en ledtråd med
  samma text inte ändras.

### Fler lärdomar från kollisioner

- **Flerval:** Uppgiftslabbet skriver bara ut A–D när texten innehåller ”alternativ”, ”markera”, ”kryssa” eller ”ringa
  in”, eller när `visaAlternativ` är `true` (`altVisas` i `index.html`). `apply.py` sätter `visaAlternativ: true`
  automatiskt när ordet försvinner ur `t`.
- **Omkörning är säker.** `apply.py` kan köras igen på ett område som redan är omskrivet. Nycklar som redan finns får
  nytt värde i stället för att dubbleras, och `sbyt` hoppar över byten som redan är gjorda.
- **Lika delkort:** när flera delkort har identisk gammal fråga, ersätts förekomsterna i dokumentordning, och
  verktyget varnar för det. Kontrollera dem efteråt.
- **Hela testsviten:** kör `node --test tools/*.test.js` med den nya banken och med `git show HEAD:<bank>`. Jämför
  felnamnen med `comm`. Före ändringen fallerade 47 test i Uppgiftslabbet, bland annat tre i `granska-svg`. Testet
  ”clean figure has no findings” fallerar ibland av sig självt.
