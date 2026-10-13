# Ma1 – onödiga avrundningsledningar

Datum: 2026-10-13. Rapport #0.189 önskar bort ledningen om hur man avrundar, även i liknande uppgifter.

**Fem frågetexter ändrade. Åtta uppgifter granskade inklusive matematik och facit.** Endast fältet `t` ändras i banken; övriga uppgifter och alla svar, toleranser, nivåer, facit och separata ledtrådar är identiska med föreversionen. #0.189 är fortsatt nivå 1. De fyra svårare resonemangsuppgifterna behåller nivåerna 4/5 och manuell bedömning i Uppgiftslabbet.

Den vanliga skolregeln för positiva tal förutsätts nu utan påminnelse i frågan. Detta ändrar inte avrundningsmodell eller gränser i facit. Noggrannhet och situationsvillkor står kvar. Frågor där eleven ska granska själva metoden behåller sina alternativ.

## Samtliga granskade uppgifter och utfall

Alla rader gäller hela uppgiften, inga separat märkta delkort. Alla gäller Ma1a/b/c utom #7.500, som gäller Ma1a. Ursprungsrapporten gäller Ma1a; ändringen görs i det gemensamma objektet.

### #0.189 — Åtgärdad – formulering

2,675 ligger mitt mellan 2,67 och 2,68; vanlig skolavrundning ger 2,68.

**Kommentarsförslag:** Ledningen om avrundningsregeln är borttagen. Uppgiften lyder nu: Avrunda 2,675 till två decimaler. Svaret är fortfarande 2,68.

### #0.193 — Åtgärdad – formulering

Varje avrundningsfel har belopp högst 0,05 m. Två fel i samma riktning kan ge 0,10 m. Exemplet 1,25 + 2,35 ger 3,60 före och 3,70 efter avrundning.

**Kommentarsförslag:** Påminnelsen om avrundning vid halva steg är borttagen ur frågan. Förklaringen och exemplet finns kvar i facit.

### #0.566 — Åtgärdad – formulering

19,5 ≤ x < 20,5 och 29,5 ≤ y < 30,5. Positiva mått och exakt höjd ger 5,7525 ≤ V < 6,2525 liter. Sex liter ryms inte säkert.

**Kommentarsförslag:** Påminnelsen om halvcentimeter är borttagen. Frågan behåller måttens noggrannhet; volymgränserna förklaras i facit.

### #0.587 — Åtgärdad – formulering

1150 ≤ s < 1250 m och 210 ≤ t < 270 s ger 115/27 < v < 125/21 m/s. Ändpunkterna uppnås inte. Övre gränsen är mindre än 6 m/s.

**Kommentarsförslag:** Påminnelsen om halva steg är borttagen. Sträckans och tidens noggrannhet finns kvar.

### #0.592 — Åtgärdad – formulering

Direkt avrundning byter heltal vid n+0,5; dubbelavrundning byter vid n+0,45. Skillnad precis på [n+0,45; n+0,5). Metod II ger aldrig lägre heltal.

**Kommentarsförslag:** Regelpåminnelsen är borttagen. De två metoder som ska jämföras finns kvar; gränserna motiveras i facit.

### #0.186 — Granskad – inget fel

15,049 avrundat direkt till en decimal är 15,0. Via 15,05 blir det 15,1. Endast C förklarar den direkta avrundningen korrekt.

**Kommentarsförslag:** Metoderna ingår i resonemangsfrågan och behöver stå kvar. Direkt avrundning ger 15,0; rätt alternativ är C.

### #0.203 — Granskad – inget fel

80 ≥ 74, 130 ≥ 128 och 210 ≥ 203. Summan 420 är under 500; inget pris underskattas. Övriga alternativ uppfyller inte villkoret för varje pris.

**Kommentarsförslag:** Avrundningsriktningarna är svarsalternativ som eleven ska bedöma. D ger en säker övre uppskattning på 420 kr.

### #7.500 — Granskad – inget fel

Ett helt antal personer får inte överstiga gränsen 8,4. Största möjliga heltal är 8.

**Kommentarsförslag:** Frågan prövar säker avrundning och alternativen behövs. Högst 8 hela personer är tillåtna; rätt alternativ är A.

## Sökning och avgränsning

Frågetexter, `spelIntro` och delarnas `t`/`fraga` genomsöktes efter påminnelser om halva steg, avslutande femmor, avrundningsregler och vilken siffra man ska titta på. Hela Ma1:s avrundningsområde inventerades språkligt. Samma riktade textsökning gjordes över bankfilerna i repot. Träffar bedömdes i sitt sammanhang; facit och separat ledtråd räknades inte som text i frågan.

Sju jämförelser till ursprungsrapporten ingår i fullgranskningen: #0.193/#0.566/#0.587/#0.592/#0.186/#0.203/#7.500. Därmed är kravet på minst fem analoga uppgifter uppfyllt. Övriga inventerade texter räknas inte som en fullständig facitgranskning. Inga nya figurer eller delkort skapas.

## Verifiering

- Oberoende decimalräkning med ROUND_HALF_UP: 2,675→2,68; summans maximala fel 0,10 m; volymgränser 5,7525/6,2525 liter; hastighetsgränser 115/27 och 125/21 m/s.
- Dubbelavrundningen stöds av algebraiska gränsargumentet ovan och en kontroll av 10 000 decimalvärden på [7;8). Metod II ger aldrig mindre svar.
- 12 svar i Kunskapsgymmets riktiga fält: 2,68/2.68/2,680 godtas; 2,67/2,7/2,675 underkänns i #0.189. Korrekta och felaktiga alternativ provas i de tre oförändrade uppgifterna.
- 24 elev-/lärarvyer vid 390 och 1280 pixlar utan upptäckta KaTeX-fel, JavaScript-fel eller horisontella överflöden. Fyra manuella uppgifter provas i lärarvyn; fyra självrättande i båda apparna.
- 29 regressionstester passerar: `tools/sparskydd.test.js`, `tools/felrapporter-2026-10-12-0958.test.js`, `tools/felrapporter-2026-10-13.test.js`.
- Bankvalidatorn har fortsatt 198 fynd. Inga nya ERROR/WARNING. En befintlig INFO om liknande korta avrundningsfrågor inkluderar nu även #0.189; det är den avsiktliga textförkortningen, inte ett nytt matematiskt fel.
- Syntax och diff kontrollerade. Exakt fem `t`-fält ändras och Ma1-bankerna är byteidentiska. Konsumentens `BANK_VERSION` är `2026-10-13-avrundning`.

Inga nya implementationstrogna tester har lagts till för dessa fem rena textförkortningar. Beslutet skyddas redaktionellt i `PEDAGOGISKA_REGLER.md` och FP41. De befintliga regressionstesterna och den riktade verifieringen ovan skyddar matematiken och självrättningen.

[Maskinläsbar lista med före/eftertexter och kommentarer](MA1_AVRUNDNINGSLEDNINGAR_2026-10-13.json). Git-historiken visar ändringarna. Utgångspunkt: Uppgiftslabbet 3430579 och Kunskapsgymmet abb2c01. Redan ospårade `tools/__pycache__/` i konsumenten lämnas utanför commit.

**Rapportstatus:** kommentarerna är förslag. Ingen rapport har markerats åtgärdad och ingen kommentar har skickats i appen. Webbläsarkontrollen blockerar Supabase och ersätter sparandet av resultat/XP med en lokal testfunktion.
