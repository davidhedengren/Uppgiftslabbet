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

Prioritet efter täthet av AI-mönster: först resten av Fy1 område för område, sedan Fy2, Ma1, Ma2, Ma3c, Ma4 och Ma5.
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

| 2026-11-17 | fy1 | rorelseenergi | 115 av 115 | Formler är borttagna ur frågorna (”med Eₖ = mv²/2”, ”med F = E/s”, definitionen av mekanisk energi). 5.609 avslöjade svaret i frågan. 5.537 hade förbehållet ”Bortse från luftmotståndet” fast uppgiften handlar om luftmotstånd. Villkor som påverkar svaret står kvar, till exempel ”konstant retardation” (5.488) och ”Bromskraften F är oförändrad” (5.224). |

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
