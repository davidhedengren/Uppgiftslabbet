# Innehållsregler för uppgifter, facit, ledtrådar och figurer

Detta dokument kompletterar [ARBETSINSTRUKTION.md](ARBETSINSTRUKTION.md), [PEDAGOGISKA_REGLER.md](PEDAGOGISKA_REGLER.md) och [KVALITETSKONTROLL.md](KVALITETSKONTROLL.md). Det gäller all granskning och ändring av uppgiftsbankerna, oavsett vilken agent som utför arbetet.

## 1. Grundregler

1. Bevara befintliga uppgifts-ID:n.
2. Radera aldrig uppgifter eller filer utan uttryckligt godkännande.
3. Befintlig metadata är information att granska, inte automatiskt korrekt. Anta aldrig att gammal metadata stämmer bara för att den redan finns.
4. Använd inte kryssprodukter i uppgifter eller facit.
5. Lämna aldrig interna redigeringskommentarer eller teknisk text riktad till utvecklaren i elevtext, facit eller ledtrådar.

## 2. Fält som ska granskas

Varje berörd uppgift ska kontrolleras mot själva uppgiften, inte bara syntaktiskt:

- matematik/fysik, facit och `rättSvar`
- `kurs`/spår, `kap`, `omr`, `familj`, `formaga`
- E/C/A (`niva`) och `poang`
- `traningsniva` (1–5) och `arbetsinsats`
- `miniräknare`, `geogebra`
- `spel`, `självrättning`, `svarstyp`, `svarFormat`, `tolerans`, `svarEnhet`, `svarEtiketter`, `svarsstruktur`
- `spelDelning`, `spelIntro`, `spelDelar` (inklusive varje dels `t`, `s`, `ledtrad`)

## 3. Kontrollkedja

### 3.1 Matematisk/fysikalisk korrekthet

Räkna själv igenom uppgiften och lita inte på befintligt facit. Kontrollera alla delresultat, tecken, enheter, avrundningar och signifikanta siffror, och att lagrat `rättSvar` verkligen motsvarar facit.

Jämför alltid fyra led:

1. uppgiftstexten,
2. det matematiskt/fysikaliskt korrekta svaret,
3. det lagrade facit,
4. det svar som Kunskapsgymmets självrättning faktiskt accepterar.

Då går det att skilja mellan fel facit och korrekt facit med felaktig parser eller självrättning. Matematiskt ekvivalenta svar ska godtas. Ett korrekt svar som `3*(sin(x))^2*cos(x)` får till exempel inte underkännas för att facit är skrivet som \(3\sin^2x\cos x\).

### 3.2 Varje Kunskapsgymmet-kort ska vara självbärande

Detta är en av de viktigaste reglerna. När en uppgift med a), b), c) delas med `spelDelning:"deluppgifter"` ska varje `spelDelar[i]` kunna lösas utan att eleven har sett eller löst någon annan del.

- Leta efter formuleringar som ”använd svaret från a)”, ”samma vinkel”, ”detta värde”, ”motsvarande”, ”denna funktion” och ”ditt svar”.
- Om b) behöver ett resultat från a) ska resultatet eller den bakomliggande informationen skrivas in i b-kortet. Eleven ska inte behöva göra om a) i smyg för att förstå b).
- Uppgiftslabbet ska samtidigt kunna behålla hela a–b–c-uppgiften i huvudtexten.

### 3.3 Gemensam information ska följa med

Funktioner, modeller, tabeller, diagram, SVG-figurer, givna konstanter, koordinater och villkor måste finnas i `spelIntro` eller på själva delkortet. Kontrollera bland annat:

- att delkortet har figuren när huvuduppgiften innehåller en SVG,
- att svarsalternativ A–D inte försvinner när uppgiften delas.

### 3.4 Ingen facitläcka mellan delar

- Facit till en del får aldrig visa svaret på en annan del. Varje `spelDelar[i].s` ska bara innehålla den aktuella delens lösning.
- Jämför huvudfacit med varje separat spelfacit och leta efter överflödiga svar till senare delar. Ett känt exempel är Ma1 2.63, där a-kortets facit avslöjade svaret på b.
- Huvudfacit i Uppgiftslabbet (`s`) får fortfarande visa hela lösningen till a–b–c.

### 3.5 Ledtrådar

- Ledtråden ska vara specifik för uppgiften och hjälpa eleven vidare utan att ge lösningen.
- Den ska helst peka mot nästa tanke eller metodval, till exempel ”Vilken formel kopplar ihop kraft, massa och acceleration?”, snarare än att skriva hela ekvationen med insatta värden.
- Generiska ledtrådar som ”Tänk noga” eller sådana som bara upprepar frågan ska bort.
- Om utmaningen är att identifiera vilken ekvation eller modell som ska användas får ledtråden inte servera den färdiga ekvationen. Om uppgiften tränar själva proceduren kan det vara rimligt att påminna om formeln.
- En b-ledtråd får inte säga något som bara är begripligt efter a), och den får inte ge bort svaret på en annan del. En generisk ledtråd från huvuduppgiften ska ersättas när ett separat kort behöver något mer specifikt.

### 3.6 Facit

- Facit ska vara uppgiftsspecifikt och pedagogiskt, inte bara ange slutsvaret. Det ska visa den centrala idén, relevanta lösningssteg med mellanled och det slutliga svaret.
- För enkla rutinuppgifter kan facit vara kort. För resonemang, modellering och högre träningsnivåer ska lösningen vara så fullständig att eleven förstår varför metoden fungerar.
- Inga generiska malltexter som bara halvdåligt passar många uppgifter.
- Facit och ledtråd på ett Kunskapsgymmet-kort får inte referera till osynliga tidigare delar.

### 3.7 Självrättningen måste fungera

- Kontrollera sambandet mellan `rättSvar`, `självrättning`, `svarFormat`, `svarstyp`, `tolerans`, `svarEnhet`, `svarEtiketter` och antalet deluppgifter.
- Arraylängderna måste stämma.
- `rättSvar:null` får inte kombineras med `självrättning:true`.
- Om ett korrekt uttryck kan skrivas på flera naturliga sätt måste svarstypen och parsern stödja dem. Eleven ska aldrig behöva imitera typografin i facit.

### 3.8 LaTeX/MathJax ska vara renderingssäkert

Det räcker inte att strängen ser ut som LaTeX. Kontrollera:

- obalanserade `\(` `\)` och `\[` `\]`,
- saknade klamrar och trasiga kommandon,
- rå HTML inne i matteblock, till exempel `<br>` mellan `\[` och `\]`,
- råa `<` och `>` inne i matte. Ersätt dem med `\lt` och `\gt`, annars kan de tolkas som HTML.

### 3.9 HTML och SVG

Kontrollera mer än XML-syntax:

- giltig XML och fungerande interna `id`/referenser,
- rimlig `viewBox`,
- att text inte hamnar utanför figuren,
- att etiketter inte överlappar linjer, vinkelbågar eller andra värden,
- att grader och vinkelbågar stämmer geometriskt, inte bara ser ungefär rätt ut,
- att figuren fungerar i både Uppgiftslabbet och Kunskapsgymmet, också när den flyttas från hela uppgiften till ett separat kort.

SVG-validatorn (`tools/granska-svg.js`) är en prioriterad del av arbetet.

### 3.10 Metadata bedöms pedagogiskt

`kurs`, `kap`, `omr`, `familj`, `formaga`, E/C/A, `poang`, `traningsniva`, `arbetsinsats`, `miniräknare`, `geogebra` och `spel` ska bedömas mot själva uppgiften.

Träningsnivå 1–5 hålls isär från E/C/A:

| Träningsnivå | Innebörd |
|---|---|
| 1 | Enkel E-uppgift |
| 2 | Mer krävande E-uppgift, ännu inte C |
| 3 | Börjar bli C |
| 4–5 | Tydligt svårare |

A-uppgifter ska vara korrekt kalibrerade.

Fler räknesteg gör inte i sig en uppgift till C. En mer krävande rutinuppgift kan
fortfarande vara E och ska då få träningsnivå 2, inte höjas till C enbart för att
skiljas från de enklaste uppgifterna. Arbetsinsats bedöms separat från nivån.

### 3.11 Progression och variation

- Inom en familj ska det finnas en rimlig väg från grundläggande procedur och begrepp till mer sammansatta problem.
- Leta efter klonuppgifter, onödigt många nästan identiska talbyten, luckor på nivå 1–2 och uppgifter som är märkta för högt.
- Sträva efter progression i stället för klonspam.

### 3.12 Olämpliga speluppgifter

Skissuppgifter, fri resonemangstext, grafritning, regressions- och linjeanpassningsuppgifter och annat som inte kan självrättas robust kan finnas kvar i Uppgiftslabbet men ska få `spel:false`. En bra läraruppgift ska inte försämras för att den ska bli spelbar.

## 4. Arbetssätt: iterera tills inga säkra fel återstår

1. Kör först automatisk, deterministisk scanning.
2. Kontrollera därefter flaggade kandidater manuellt i sitt sammanhang.
3. Ändra endast när felet är bekräftat. Osäkra heuristiska träffar får aldrig massändras: flagga, kontrollera sammanhanget och ändra bara det som är bekräftat.
4. Kör en ny full kontroll på den korrigerade filen.
5. Fortsätt tills en hel körning ger noll nya bekräftade fel.

Vid en andra kvalitetskontroll av en grupp ska särskilt kontrolleras:

- att facit är uppgiftsspecifikt, korrekt och tillräckligt pedagogiskt,
- att ledtråden hjälper utan att avslöja,
- att facit och ledtråd på ett Kunskapsgymmet-kort inte refererar till osynliga tidigare delar,
- att elevtexterna saknar interna redigeringskommentarer och teknisk text.

## 5. Tekniska slutkontroller

- Filen ska kunna parsas (`node --check` eller motsvarande parsning när Node saknas).
- Inga dubbla ID:n.
- Antalet uppgifter får inte ändras oavsiktligt. Jämför före och efter.
- Relevanta metadata-arrayer ska ha rätt längd.

## 6. Backup utanför Git

Både Uppgiftslabbet och Kunskapsgymmet ska ha en separat veckovis lokal backup: tidsstämplade ZIP-filer utanför repona, verifiering efter skapandet och retention på minst 12 backuper. Den körs deterministiskt via Windows schemaläggning och är inte beroende av AI. Se [GIT_OCH_BACKUP.md](GIT_OCH_BACKUP.md).
