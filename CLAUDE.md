# Uppgiftslabbet – instruktioner för Claude

Claude är agenten som underhåller Uppgiftslabbet och Kunskapsgymmet. Innan du granskar, ändrar, synkroniserar eller levererar något i detta repo **ska** du läsa och följa:

1. `agent/ARBETSINSTRUKTION.md` – övergripande arbetsgång och modellbudget
2. `agent/INNEHALLSREGLER.md` – kontrollkedja för uppgifter, facit, ledtrådar, Kunskapsgymmet-kort och SVG
3. `agent/PEDAGOGISKA_REGLER.md` – förmåga, nivå, självrättning och svarsformat
4. `agent/KVALITETSKONTROLL.md` – checklistor före och efter ändring
5. `agent/GIT_OCH_BACKUP.md` – Git från flera datorer, banksynkronisering och backup

Reglerna i `agent/` gäller Claude på samma sätt som de gällde Hermes.

## Kärnregler (gäller även innan dokumenten ovan har lästs)

- Kör `git status`, `git fetch origin --prune` och jämför med upstream före redigering. Användaren laddar ofta upp filer via GitHubs webb och arbetar från flera datorer.
- Använd aldrig force push. Gör ingen commit eller push utan användarens godkännande.
- Uppgiftslabbet är master för de sju gemensamma bankerna. Kunskapsgymmet får bara synkade kopior, aldrig egna manuella ändringar.
- Bevara ID:n och radera aldrig uppgifter eller filer utan uttryckligt godkännande.
- Befintlig metadata och facit är referensmaterial, inte facit. Räkna själv.
- Heuristiska fynd får aldrig massändras.
- Ändra bara det användaren har bett om.

## Modellbudget för Claude

Inled varje nytt arbete med ”För det här jobbet föreslår jag …” (Sonnet eller Opus) med en kort motivering. Byt inte modell mitt i en lång session, eftersom det kräver en dyr omläsning utan cache. Föreslå i stället att användaren startar en ny session med rätt modell för jobbet. Sonnet räcker för mekaniskt och deterministiskt arbete. Opus behövs för svår matematik- och fysikgranskning, pedagogiska bedömningar, geometriskt SVG-arbete och komplex kod.

Avsnitt 7 i ARBETSINSTRUKTION (Luna/Sol/Astra) översätts så här: använd deterministiska verktyg först, starta inga subagenter för rutinkontroller, och fråga användaren innan en bred AI-granskning av många uppgifter.

## Miljö på datorn `Hedav`

- Repona ligger i `C:\Users\Hedav\code\Uppgiftslabbet` och `C:\Users\Hedav\code\kunskapsgymmet`.
- Node.js v24 finns (`C:\Program Files\nodejs\node.exe`, på PATH). Kör `node --check`, `node tools/granska-uppgifter.js` och `node tools/granska-svg.js` (använder Chrome i `C:\Program Files\Google\Chrome\Application\`, tar ca 3 min, skriver `SVG_GRANSKNING.html/.json` som är gitignorerade). Testerna: `node tools/granska-uppgifter.test.js` och `node tools/granska-svg.test.js`.
- Backupsystemet i `GIT_OCH_BACKUP.md` finns på den andra datorn (`C:\Users\david\...`), inte här.

## Felrapporter från Kunskapsgymmet

Användaren klistrar in en logg ("Felrapporterade uppgifter · Kunskapsgymmet · datum", sparas även i `C:\Users\Hedav\code\felrapporter\`) med bank, uppgifts-ID, ev. del/spår, taggar och elevkommentarer. Uppdraget "lös felen i loggen" betyder: åtgärda varje rapport i master, synka till Kunskapsgymmet och rapportera per uppgift. Rutin:

1. Hitta uppgiften: bankkoden i hakparentes ger filen (fy1 → `uppgifter.js`, fy2 → `uppgifter2.js`, ma1 → `uppgifterma1.js`, ma2 → `uppgifterma2.js`, matf1 → `uppgiftermatf1.js`, mato1 → `uppgiftermato1.js`, mato2 → `uppgiftermato2.js`). Sök på `"id": "5.81"`. Filerna är stora (5–11 MB): använd `grep -n` + `sed -n` med `cut -c1-1500`, aldrig hela filen.
2. Räkna själv. Verifiera facit och `rättSvar` innan du bedömer om rapporten stämmer. Är facit rätt och rapporten saknar elevens svar: ändra inte facit, men kontrollera självrättningen (`enhetsJamforelse` i Kunskapsgymmets `index.html`) och rapportera att orsaken är okänd.
3. Åtgärda efter tagg:
   - *Frågan är otydlig*: skriv om uppgiftstexten (`t`) enklare och mer konkret. Behåll facit om matematiken inte ändras.
   - *Fel svar i facit*: räkna om; ändra `s`, `rättSvar`, `tolerans`, `svarEnhet` vid behov.
   - *Något annat* / kommentar om svårighet: bedöm kommentaren mot uppgiften (t.ex. `miniräknare`-flaggan, svarsformat, bildfel i SVG).
   - Elevens kommentar om en formulering gäller ofta **fler uppgifter**. Användaren vill då att liknande formuleringar tas bort i alla banker/uppgifter ("och ta bort liknande i andra uppgifter"). Sök brett med regex, räkna förekomster, ändra deterministiskt med ett Python-skript (utf-8, `newline=''`), ändra bara `t` (aldrig facit `s` utan skäl) och kontrollera diffen.
4. Redigera bara master i Uppgiftslabbet, kopiera därefter de ändrade bankfilerna till `kunskapsgymmet` (`cp`) och kontrollera med `cmp` att de är identiska.
5. Kontrollera att filen fortfarande är giltig JSON (Python: `json.loads` på `[`…`]`), `git diff --check`, `node --check` på bankfilen och att ingen tom `<p></p>` uppstått.
6. Fråga användaren innan commit/push. Efter ja: `git fetch`, jämför mot upstream, commit i båda repona (Uppgiftslabbet först), `git pull --rebase` i Kunskapsgymmet om remote ligger före (den får ofta ändringar i `index.html`/`sql/` från andra sessioner), push, hämta och verifiera `0 0` mot upstream.
7. Avsluta med en kort lista per uppgift: vad som ändrades, vad som lämnades orört och varför.

### Formuleringar och mönster att undvika i uppgifter

- Fysikkort på träningsnivå 1–2 ska bara visa de givna tal och materialdata som behövs för just den frågan. Ange nödvändiga mellanresultat direkt, med tillräcklig precision, och låt delens facit använda dem. Behåll nödvändiga villkor, riktning och nollnivå. Kontrollera frågans svarsenhet mot `svarEnhet` i det faktiskt visade delkortet.

Eleverna är gymnasieelever; texten ska vara enkel och konkret.

- Onödig modelljargong i uppgiftstexten, t.ex. "Försumma yttre horisontell impuls", "försumma yttre impuls", "masslösa kolvar och inkompressibel vätska", "samma lufttryck verkar ovanpå båda kolvarna". Det krånglar till uppgiften utan att hjälpa. Behåll bara förenklingar som verkligen behövs (luftmotstånd, friktion, hjulens rotationsenergi) och skriv dem i vardagligt språk. Impuls- och rörelsemängdsresonemang hör hemma i lösningen/ledtråden, inte som förbehåll i frågan. Ett bortstruket förbehåll ska inte ändra svaret.
- Otydlig fråga: skriv vad som söks och vem som gör vad ("Hur stor kraft måste du trycka med på pumpkolven…") i stället för passiva eller abstrakta formuleringar ("pumpkraften som balanserar bilens tyngd"). Förklara vad fackord avser (t.ex. "den stora kolven (lyftkolven)").
- Fråga som kräver ett ord eller en enhet: säg uttryckligen vad som ska skrivas ("Svara med ett ord", "Svara i m/s"), annars skriver eleven en hel mening och blir underkänd. Se till att `svarEnhet`/`svarFormat` låter eleven svara både med och utan enhet.
- Uppgifter markerade `miniräknare: false` som i praktiken kräver räknare (decimala radianer/grader, rötter, π numeriskt). Antingen byt siffror till exakta värden eller sätt `miniräknare: true`. Bedöm mot själva uppgiften.
- Facit där `rättSvar` bara godkänner ett format som eleven inte kan gissa (t.ex. bara "5" men inte "5 m/s").
- Figurer där text/beteckningar hamnar utanför bilden (SVG); se `agent/INNEHALLSREGLER.md` och `tools/granska-svg.js`.
- Allmänt: internt utvecklarspråk i elevtext, kryssprodukter, och nya uppgifter som är massproducerade. Användaren vill ha relativt unika uppgifter med egna sammanhang.
- Begreppen interpolation och extrapolation används inte i uppgifter, facit eller ledtrådar (användarbeslut 2026-10-22, begreppen tas inte upp på gymnasiet). Skriv i stället vardagligt, till exempel ”inom det undersökta intervallet” och ”långt utanför mätvärdena”. Ma2 4.142 och 4.224 togs bort av detta skäl.

## Kurser och planeringar

Bankernas kursnamn → skolkurs: mato1 = Matematik 3c, mato2 = Matematik 4, matf1 = Matematik 5, fy1 = Fysik 1, fy2 = Fysik 2, ma1 = Ma1a/b/c, ma2 = Ma2a/b/c.

Lärarens planeringar ligger i OneDrive: `C:\Users\Hedav\OneDrive - Jönköpings kommun\Fysik\` och `...\Matematik\` (undermappar per kurs, ofta `Planeringar/`). Prioritera nyaste (t.ex. "2627"). `.doc`-filerna från 2026 är egentligen HTML; `Sparade planeringsfiler/Lektioner - *.json` har lektionslistor. Ma1b/1c och Ma2a/2b utgår från närmaste nya planering (Ma1a resp. Ma2c). Ma3c = vårdelen av "Planering Ma2c-3c 2627"; Ma4 = "Planering Ma4 25-26"; Ma5 = gamla Ma5-planeringar (VT22).

## Pågående omstrukturering: moment och delmoment

Mål (beslutat 2026-10-01): *moment* = en lektion i planeringen (= `omr`, ett kort i Kunskapsgymmet), *delmoment* = `familj` (2–5 per moment, minst 8 uppgifter var). Ordning: Fysik 1 → Ma1 → Ma2c → övriga. Gamla namn sparas i `omrTidigare`/`familjTidigare`; Kunskapsgymmets `migreraFamiljer()` flyttar elevresultat och räknar om historiken. Vid synk av `struktur*.js` måste Kunskapsgymmets avslutande `window.GRUPP… = {};` finnas kvar för kurserna som använder det. Ma2 använder sedan 2026-10-14 lektionskort med begränsade gemensamma moment; gamla samlingsgrupper har `historisk:true` för sparade uppdrag och får inte visas som nya kort (se ST02). Ma2c har sedan ST03 (2026-10-14) ett kort per planeringsavsnitt: 27 kort med 4–8 delmoment, där närliggande lektioner är samlade så att varje område får tillräckligt många uppgifter. Alla sju banker är klara och pushade 2026-10-01 (sist Ma4/mato2 och Ma5/matf1). Ma5 följer Planering Ma5 VT22 (kap 1, 2, 4) och NA16D 2018/19 (kap 3); Grafteori ingår inte längre i matf1 enligt lärarens kursavgränsning 2026-10-08 och ska inte läggas till. Ma4 följer Planering Ma4 24-25/25-26; trigonometriska kurvor i radianer ligger i ett eget moment efter Cirkelsektorn. Vid omstrukturering: peka också om genomgångarna i Kunskapsgymmets `typuppgifter-<bank>.js` (block sist i filen) och höj `BANK_VERSION`. Översikter: `C:\Users\Hedav\code\struktur-forslag\` (`fysik1.md`, `ma1.md`, `fy2.md`, `mato1.md`, `mato2.md`, `matf1.md`).

## Arbetssätt med användaren

- Svara på svenska, kortfattat; rapportera per uppgift vad som ändrats och vad som inte gjorts.
- Fråga innan commit/push, men när användaren sagt ja: gör båda repona i ett svep och verifiera mot remote.
- Verktyg på `Hedav`: Python, Bash och Node fungerar (skriv hjälpskript i sessionens scratchpad/`$TEMP`). Skriv Python-skript med filverktyget, inte via bash-heredoc, eftersom backslashes i LaTeX annars kan halveras. Läs/skriv bankfiler som utf-8; konsolutskrift av å/ä/ö kan se trasig ut utan att filen är det.
- Instruktionerna ovan ersätter inte kontrollen mot `agent/*.md`; läs dem vid innehållsändringar.

## Tidigare granskningar och skydd mot återkommande fel

### Referens för tydliga matematiklösningar (2026-10-23)

Användaren har pekat ut **Ma1 #1.116** som förebild: tydliga, matematiskt
motiverade steg, relevanta mellanled och ett tydligt slutsvar. Använd dess
struktur vid nya och reviderade matematikfacit. Rubriker ska förklara vad
man gör (t.ex. ”Ta bort samma kvadratterm från båda leden”), inte bara heta
”Steg 1”. Visa beräkningen som leder till nästa rad och kontrollera svaret
när det tillför förståelse. Anpassa längden till uppgiften och radbryt långa
uttryck för mobilvisning. Detta ändrar inte regeln om sammanhängande
fysiklösningar utan generiska numrerade steglistor.

### Facit, ledtråd och svar ska alltid granskas noggrant (användarbeslut 2026-10-25)

Varje ny eller omarbetad uppgift ska ha ett tydligt facit, en bra ledtråd och
genomtänkta svarsalternativ. Det gäller även vid stora påfyllnadsomgångar.
Detta är ett krav, inte något man gör om tid finns.

- **Facit i matematik** följer 1.116. Varje steg har en rubrik som förklarar
  vad man gör (`facit-rubrik`), och beräkningen står i samma steg. Visa
  mellanled och avsluta med en svarsrad. Vid resonemang ska facit förklara
  varför, inte bara konstatera.
- **Rubrikerna skrivs för just den uppgiften.** Läraren vill ha det exakt
  så (2026-10-25). En rubrik ska beskriva det som faktiskt händer i steget,
  till exempel ”\(x^2\) finns i båda leden och tar ut varandra” eller
  ”Gången finns på båda sidor, så hela ytan är \(8+2x\) lång”. Den får
  inte vara en allmän mallfras som ”Steg 2”, ”Förenkla” eller ”Lös
  ekvationen” som skulle passa på vilken uppgift som helst. Generera
  aldrig rubriker automatiskt. Lägg till en kontroll när den tillför
  förståelse.
- **Facit i fysik** är en sammanhängande lösning: först modell och samband
  i ord, sedan beräkning med enheter och till sist en svarsrad med enhet
  och rimlig precision.
- **Ledtråden** är specifik för uppgiften och pekar mot nästa tanke eller
  metodval. Den får inte innehålla svaret, de insatta värdena eller den
  färdiga ekvationen när det är just modellvalet som tränas.
- **Flerval:** varje felaktigt alternativ har en kommentar som förklarar
  felet, och facit förklarar varför det rätta alternativet stämmer.
- **Före leverans:** rendera facit och ledtråd för varje nytt kort, inte
  bara frågan och figuren, och läs igenom dem. Bygg ut för tunna facit.
  Kontrollera att facit, svarsrad och `rättSvar` stämmer överens. Skriv i
  loggen att granskningen är gjord.

Läs `AGENTS.md` och `agent/FELMONSTER_OCH_BESLUT.md`. Sök tidigare beslut för
berörda uppgifts-ID:n och kör deras regressionstester före ändring och leverans.

## Långsiktigt mål: många och varierade uppgifter på nivå 1–3

Användarbeslut 2026-10-22: varje område (`omr`, ett kort i Kunskapsgymmet) ska på sikt ha **50–100 kort på träningsnivå 1 och 2 tillsammans** (preciserat 2026-10-25). Nivå 3 ska också fyllas på, så att det finns varierad träning även där. Korten ska vara **mycket varierade**, så att eleverna kan mängdträna utan att känna att de får samma uppgift om och om igen. Fortsätt fylla på löpande när tillfälle ges, och prioritera de områden som har minst antal kort på nivå 1–2 (eller nivå 3) och som undervisas nu. Fyll inte bara på nivå 1.

Variation betyder mer än nya tal:

- olika sammanhang, frågeformer och representationer, till exempel text, figur, tabell, graf och flerval;
- olika svarsformer;
- olika delmoment (`familj`) inom området.

Det räcker inte att byta tal i samma mall, eftersom validatorns `VERY_SIMILAR_TEXT` och `EXACT_TEXT_DUPLICATE` fångar kloner. Undvik också identiska facit inom ett område. Nivå 1 betyder ett steg eller ett tydligt grundsamband, utan fällor. Kunskapsgymmet räknar ett kort som nivå 1 bara när `traningsniva` är 1 på uppgiften eller delkortet, så ange den uttryckligen.

Räkna själv, sträva efter figurer och följ verktygs- och avrundningsreglerna nedan. Logga varje påfyllnad i `agent/` och lägg till ett regressionstest.

## Figurer vid konstruktion och omarbetning

Användarbeslut 2026-10-13: när du konstruerar nya uppgifter eller gör om befintliga uppgifter ska du **alltid sträva efter att ha med en figur, om det är möjligt**. Bedöm för varje uppgift hur en figur kan hjälpa eleven att förstå situationen, tolka samband eller välja metod. Kretsar, laddningars placeringar, rörelser, krafter och geometri lämpar sig särskilt väl för egna SVG-figurer. Figuren ska bidra till förståelsen och kan vara schematisk; ange skala när skalenlig avläsning behövs.

Placera alla beteckningar, sträckor, vinklar, enheter och pilar tydligt och på rätt plats. Kontrollera modellen, geometrin och faktisk mobil-/datorvisning. Om uppgiften delas i Kunskapsgymmet ska varje kort få den figur och de givna värden som behövs för just det kortet. Förklarande figurer kan också användas i facit. Dokumentera kort om en figur inte hjälper eller inte är meningsfull för uppgiften.

## Statistik: standardavvikelse

Användarbeslut 2026-10-14: databeräkningar från listor, frekvenstabeller och histogram ska använda **Sx och n−1**, inte σx. Följ `agent/PEDAGOGISKA_REGLER.md`, avsnittet ”Statistik: Sx som räkningsstandard”. Fråga, facit, alla delkort och självrättning måste räknas om tillsammans. σ som given normalfördelningsparameter behålls. Det nya beslutet ersätter FP28–29:s tidigare val av beskrivande σx i rådatauppgifter; återställ inte gamla facit från den historiska granskningsloggen.

## Verktyg: senaste användarbeslutet 2026-10-14

Vid alla analyser, rättningar och nya/omarbetade uppgifter ska miniräknare och GeoGebra kontrolleras. Läs masterrepots `agent/PEDAGOGISKA_REGLER.md`, ”Verktygsval i varje granskning”. Tillåt miniräknare för beräkningar som inte görs snabbt i huvudet, såsom stora multiplikationer och numerisk trigonometri; neka bara när verktyget tar bort det som faktiskt prövas. Vi testar normalt inte huvudräkning eller aritmetiska handalgoritmer. Tillåt GeoGebra för digital grafanalys/ritning, statistik, regression och avancerade numeriska/symboliska beräkningar när digitala verktyg behövs. **GeoGebra innebär alltid också tillåten miniräknare.** Detta ersätter den tidigare miniräknarspärren för Sx-kort. Kontrollera huvuduppgift och delkort separat, och dokumentera beslut/undantag tillsammans med nivå, facit och självrättning.

## Avrundning utan uttalad precision (användarbeslut 2026-10-19)

Om frågan inte anger avrundning ska exakta, mer noggranna och korrekt avrundade
svar godkännas. Kräv inte ett dolt antal decimaler eller värdesiffror. Jämför
med facit avrundat till elevens precision, inte med en godtyckligt stor felmarginal.
Bevara krav på exakt form och angiven precision när frågan faktiskt ställer dem.
Antal och andra exakta heltal ska fortfarande vara korrekta; fel enhet eller
felaktigt avrundade tal ska inte godtas. Kontrollera detta i verkliga svarsfält.

## Fysik: konstanter slås upp i formelsamlingen (användarbeslut 2026-10-25)

Skriv inte naturkonstanter i fysikuppgifternas frågor eller ledtrådar. Det gäller
c, h, e, elektronens, protonens och neutronens massa, k, G, \(\mu_0\), Avogadros
tal, atommassenheten och viloenergier. Det gäller också omvandlingar som
”1 eV = 1,602·10⁻¹⁹ J”. Eleverna slår upp dem i formelsamlingen. Data som hör
till själva situationen, som mätvärden och atommassor för en viss nuklid, får stå
kvar. Självrättningen ska godkänna svar som räknats med vanliga värden, till
exempel både \(c=2{,}998\cdot10^8\) och \(3{,}00\cdot10^8\) m/s. Kontrollera
facit och tolerans med båda varianterna.

## Fysik: placering av svarsinstruktioner

Skriv enhet, avrundning och särskilda krav på svaret i parentes efter själva
frågan, även på fristående delkort: ”Hur lång tid är pilen i luften?
(Svara i s med två decimaler.)” Behåll nödvändiga förutsättningar och vald
positiv riktning. Kontrollera att enhet och precision stämmer med facit och
självrättning. Lägg inte till avrundningskrav som eleven inte behöver.

**Ändrat 2026-10-26 (lärarens felrapporter, Fy1):** skriv inte ut svarsenhet
eller avrundningskrav när de är underförstådda ("Svara i m", "med två decimaler").
Precisionen sköts av `svarVardesiffror` med oavrundat `rättSvar`. Skriv inte
"likformig" om acceleration och skriv "fart", inte "fartbelopp". Delkort ska vara
fristående med egna givna värden och inte upprepa samma inledning ordagrant
(se `agent/FELRAPPORTER_2026-10-26_1531.md`). Behåll nödvändig positiv riktning.
