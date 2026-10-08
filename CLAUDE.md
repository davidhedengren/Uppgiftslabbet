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

## Kurser och planeringar

Bankernas kursnamn → skolkurs: mato1 = Matematik 3c, mato2 = Matematik 4, matf1 = Matematik 5, fy1 = Fysik 1, fy2 = Fysik 2, ma1 = Ma1a/b/c, ma2 = Ma2a/b/c.

Lärarens planeringar ligger i OneDrive: `C:\Users\Hedav\OneDrive - Jönköpings kommun\Fysik\` och `...\Matematik\` (undermappar per kurs, ofta `Planeringar/`). Prioritera nyaste (t.ex. "2627"). `.doc`-filerna från 2026 är egentligen HTML; `Sparade planeringsfiler/Lektioner - *.json` har lektionslistor. Ma1b/1c och Ma2a/2b utgår från närmaste nya planering (Ma1a resp. Ma2c). Ma3c = vårdelen av "Planering Ma2c-3c 2627"; Ma4 = "Planering Ma4 25-26"; Ma5 = gamla Ma5-planeringar (VT22).

## Pågående omstrukturering: moment och delmoment

Mål (beslutat 2026-10-01): *moment* = en lektion i planeringen (= `omr`, ett kort i Kunskapsgymmet), *delmoment* = `familj` (2–5 per moment, minst 8 uppgifter var). Ordning: Fysik 1 → Ma1 → Ma2c → övriga. Gamla namn sparas i `omrTidigare`/`familjTidigare`; Kunskapsgymmets `migreraFamiljer()` flyttar elevresultat och räknar om historiken. Vid synk av `struktur*.js` måste Kunskapsgymmets avslutande `window.GRUPP… = {};` finnas kvar (saknas i master för ma2). Alla sju banker är klara och pushade 2026-10-01 (sist Ma4/mato2 och Ma5/matf1). Ma5 följer Planering Ma5 VT22 (kap 1, 2, 4) och NA16D 2018/19 (kap 3); Grafteori ingår inte längre i matf1 enligt lärarens kursavgränsning 2026-10-08 och ska inte läggas till. Ma4 följer Planering Ma4 24-25/25-26; trigonometriska kurvor i radianer ligger i ett eget moment efter Cirkelsektorn. Vid omstrukturering: peka också om genomgångarna i Kunskapsgymmets `typuppgifter-<bank>.js` (block sist i filen) och höj `BANK_VERSION`. Översikter: `C:\Users\Hedav\code\struktur-forslag\` (`fysik1.md`, `ma1.md`, `fy2.md`, `mato1.md`, `mato2.md`, `matf1.md`).

## Arbetssätt med användaren

- Svara på svenska, kortfattat; rapportera per uppgift vad som ändrats och vad som inte gjorts.
- Fråga innan commit/push, men när användaren sagt ja: gör båda repona i ett svep och verifiera mot remote.
- Verktyg på `Hedav`: Python, Bash och Node fungerar (skriv hjälpskript i sessionens scratchpad/`$TEMP`). Skriv Python-skript med filverktyget, inte via bash-heredoc, eftersom backslashes i LaTeX annars kan halveras. Läs/skriv bankfiler som utf-8; konsolutskrift av å/ä/ö kan se trasig ut utan att filen är det.
- Instruktionerna ovan ersätter inte kontrollen mot `agent/*.md`; läs dem vid innehållsändringar.
