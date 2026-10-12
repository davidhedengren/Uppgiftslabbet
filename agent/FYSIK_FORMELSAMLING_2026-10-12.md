# Fysikbankerna – formelsamling i stället för ledningar i frågan

2026-10-12. Användarbeslut: eleven ska själv hitta standardkonstanter och välja formel. Den fullständiga inventeringen omfattar **3 768 Fysik 1-uppgifter och 1 412 Fysik 2-uppgifter**, totalt 5 180. **1 341 respektive 363 uppgifter** har reviderade frågor/intron/delkort. Kontrollen gäller denna feltyp och ska inte beskrivas som en ny fullständig manuell omräkning av alla fysikuppgifter.

## Beslut

- Standardkonstanter g på jorden, G, Coulombs konstant, elementarladdning, elektron-/protonmassa, c, h, R, N_A, Boltzmanns konstant, μ₀, ε₀, Wiens konstant, Stefan–Boltzmanns konstant och standardomvandlingar ska sökas i formelsamlingen. Färdiga uppmaningar som ”Använd F = ma” eller ”Använd g = 9,82” är borttagna från frågorna.
- Rensningen gäller `t`, `spelIntro` och alla delkorts `t`/`fraga`; eleven får inte samma ledning igen i ett separat kort. Lösningsförslag och ledtrådar bakom separata knappar är inte uppgiftstext. Förklaringar och insatta konstanter finns kvar i facit.
- Behåll uppmätta tal, fjäderkonstanter, experimentella referensvärden, friktionstal, lokala g-värden i jämförelseexperiment, modellplaneters g samt nödvändiga material-/isotopdata. Dessa är situationsdata och får inte försvinna för att ordet ”konstant” eller tecknet ”=” förekommer. Modellvärden utan en allmängiltig tabellkälla skrivs som givna fakta i stället för ”Använd ...”. Hubbleparametern 70 och solens bolometriska magnitud +4,74 behålls som valda modellvärden.
- Behåll riktning, nollnivå, och antaganden som påverkar svaret. ”Använd g ... och uppåt som positivt” blev ”Uppåt är positiv riktning”; energiförluster, friktion, luftmotstånd och modellradier behålls där de behövs. 4.378 behåller 6370 km för sitt tvådecimalssvar.
- Formler som är själva föremålet för en felsökning, jämförelse eller härledning är kvar. 4.368:s felaktiga beräkning och 2.503/2.504:s lokala g-värden är uppgiftens data, inte en extra ledning.
- Nivåer, ID, ordning, fysikmodeller, givna mellanresultat, ordinarie `rättSvar`, toleranser, enheter och SVG-geometri är bevarade. Att leta efter en formel är inte i sig skäl att höja träningsnivån.

## Självrättning och tabellvärden

283 kontroller av svarsfält har gjorts mot oberoende beräkningsmodeller från befintliga fysiktester, med alternativa tabellvärden och efterfrågad avrundning. Åtta uppgifter behöver uttryckliga kompletterande mål, som lagras i `svarTabell`. Varje mål använder samma format, enhet och tolerans som originalsvaret. Ingen generell procenttolerans införs. En elev ska inte behöva skriva tabellvärdet i själva frågan.

| Uppgift | Alternativt tabellvärde | Kompletterande svar | Kommentarsförslag |
|---|---|---|---|
| fy1 2.29 a/b/e | 4186 J/kcal; e = 1,60·10⁻¹⁹ C | 8 372 000 J; cirka 2,33 kWh; 0,800 J | Rättningen godtar båda vanliga kaloriomvandlingarna och den avrundade elementarladdningen. |
| fy1 2.32 d | 735,5 W/hk | 1103,25 W | Både 735 och 735,5 W per hk fungerar. |
| fy1 2.33 f | 4186 J/kcal | 2 093 000 J | Båda vanliga kaloriomvandlingarna godtas. |
| fy1 4.74 b/c | G = 6,67·10⁻¹¹ | cirka 10,42 och 11,77 kN | Kraften kan skilja i sista siffran när tabellvärdet för G avrundas. |
| fy1 4.740 | G = 6,674·10⁻¹¹ | cirka 686 N | Både 685 och 686 N är rimliga med de två vanliga G-värdena. |
| fy1 4.742 a/d | G = 6,674·10⁻¹¹ | cirka 1,63 och 25,95 N/kg | Båda vanliga G-värdena fungerar även när sista decimalen ändras. |
| fy1 5.498 c | 4184 J/kcal | 26 034 hela lyft | Med 4184 respektive 4186 J/kcal blir minsta antalet 26 034 respektive 26 047; båda godtas. |
| fy1 5.562 b | 735 W/hk | cirka 501 N | Både 501 och 502 N godtas med de två vanliga hk-omvandlingarna. |

Facit har korta kommentarer om dessa alternativ, även i rätt delkort. En kommentar till b får inte visa c:s svar. Ett delkort med egna mellanresultat ärver inte ett alternativt föräldrasvar: då krävs egen `svarTabell`. Hela uppgifter, uppdelade kort och riktiga svarsfält har provats. Tidigare FP26/FP30 gäller fortsatt: exakt fysik och enheter ska inte blandas ihop med avrundning, och inga generella toleranser vidgas. Här kompletteras tidigare beslut eftersom frågan inte längre låser vilket tabellvärde eleven ska använda.

## Granskade, åtgärdade och utan rensningsbehov

Den maskinläsbara JSON-loggen innehåller samtliga 5 180 granskade ID:n, alla 1 704 ändrade ID:n med exakta fältsökvägar och kommentarsförslag, samt samtliga 3 476 uppgifter utan rensningsbehov. ”Granskad – inget fel” avser endast den här avgränsade kontrollen, inte en garanti om varje äldre facit eller metadatafält. Inga elevrapporter har handlagts eller avslutats och inga kommentarer har skickats.

## Verifiering

- Master: 185 godkända regressionstestfall, inklusive den nya helbankskontrollen och oberoende modeller för de kompletterande svaren. `node --check` på båda bankfilerna.
- Konsument: 48 godkända kontraktstester för delning, aliasens fältkoppling, tal och enheter. Rättningen för uppgifter utan `svarTabell` är oförändrad.
- Före/efter i Chromium: 5 282 fy1-kort och 1 986 fy2-kort, totalt 19 197 kontroller av facitsvar, enheter och avsiktliga felsvar. 0 rättningsfel och 0 KaTeX-fel, både före och efter rensningen.
- Riktat browsertest: 74 kontroller i riktiga svarsfält (heluppgift/delkort), inklusive de nya tabellsvaren, alternativa enheter och felaktiga grannvärden; 10 mobil-/datorvisningar. 0 JavaScript-fel. Två extra kalori-/hk-analoger har oberoende direktmodeller även när de inte finns i den äldre modellinventeringen.
- Bankvalidatorns före/efter-resultat är oförändrat: fy1 0 ERROR, 8 WARNING, 833 INFO; fy2 1 587 äldre ERROR och 40 INFO, huvudsakligen saknade hjälpmedelsflaggor. Dessa metadatafynd fanns före denna ändring och innebär inte nya rättningsfel. Inga nya validatorfynd. Befintliga metadatafynd ska inte tyst märkas som lösta i denna textomgång.
- Strukturerad diff: oförändrat antal/ordning/ID; endast frågetext/introt/delkort och de åtta uppgifternas facittillägg/`svarTabell` ändras. Alla SVG-strängar är bevarade. `uppgifter.js` och `uppgifter2.js` är byteidentiska mellan repona. Konsumentens `BANK_VERSION` höjs till `2026-10-12-fysik-formelsamling`.

Skydd: master `tools/fysik-formelsamling.test.js`; konsument `tools/tabellkonstanter.test.js`, `tools/fysik-formelsamling.browser.py`, befintliga delkort-/enhetstester och `tools/fysik1-hela-banken.browser.py`. Vid nya uppgifter ska regelns syfte kontrolleras mot elevens faktiska kort, inte bara läraruppgiftens huvudtext.

## Samtliga ändrade ID och fält

| Kurs | ID | Ändrade fält |
|---|---|---|
| fy1 | 2.10 | t |
| fy1 | 2.12 | t |
| fy1 | 2.29 | s, spelDelar.0.fraga, spelDelar.0.s, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.s, spelDelar.1.t, spelDelar.4.fraga, spelDelar.4.s, spelDelar.4.t, svarTabell, t |
| fy1 | 2.32 | s, spelDelar.3.s, spelDelar.3.t, svarTabell, t |
| fy1 | 2.33 | s, spelDelar.2.t, spelDelar.3.t, spelDelar.5.s, spelDelar.5.t, svarTabell, t |
| fy1 | 2.57 | spelDelar.4.t, t |
| fy1 | 2.59 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 2.60 | spelDelar.5.t, t |
| fy1 | 2.61 | spelDelar.4.t, t |
| fy1 | 2.63 | t |
| fy1 | 3.6 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.17 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.27 | t |
| fy1 | 3.30 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.45 | t |
| fy1 | 3.71 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.72 | t |
| fy1 | 3.79 | t |
| fy1 | 3.86 | t |
| fy1 | 3.87 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.88 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.89 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.92 | t |
| fy1 | 3.117 | t |
| fy1 | 3.118 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.120 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 3.121 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.123 | t |
| fy1 | 3.132 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.146 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.150 | t |
| fy1 | 3.161 | t |
| fy1 | 3.162 | t |
| fy1 | 3.165 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.170 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.171 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.1 | t |
| fy1 | 4.3 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.4 | spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.6 | t |
| fy1 | 4.323 | t |
| fy1 | 4.9 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.346 | t |
| fy1 | 4.347 | t |
| fy1 | 4.10 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.11 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.13 | t |
| fy1 | 4.16 | t |
| fy1 | 4.19 | t |
| fy1 | 4.20 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.21 | t |
| fy1 | 4.22 | t |
| fy1 | 4.24 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.26 | t |
| fy1 | 4.387 | t |
| fy1 | 4.27 | t |
| fy1 | 4.29 | spelDelar.1.t, spelIntro, t |
| fy1 | 4.30 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.388 | t |
| fy1 | 4.447 | t |
| fy1 | 4.36 | t |
| fy1 | 4.37 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.362 | t |
| fy1 | 4.38 | t |
| fy1 | 4.363 | t |
| fy1 | 4.364 | t |
| fy1 | 4.39 | t |
| fy1 | 4.367 | t |
| fy1 | 4.42 | t |
| fy1 | 4.43 | t |
| fy1 | 4.44 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.45 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.46 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.47 | t |
| fy1 | 4.51 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.52 | t |
| fy1 | 4.53 | spelDelar.0.t, spelDelar.1.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.54 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.55 | t |
| fy1 | 4.56 | t |
| fy1 | 4.57 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.58 | t |
| fy1 | 4.59 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.390 | t |
| fy1 | 4.61 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.63 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.64 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.65 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.66 | t |
| fy1 | 4.67 | t |
| fy1 | 4.71 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.72 | t |
| fy1 | 4.73 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.74 | s, spelDelar.1.s, spelDelar.1.t, spelDelar.2.s, spelDelar.2.t, spelIntro, svarTabell, t |
| fy1 | 4.368 | t |
| fy1 | 4.75 | t |
| fy1 | 4.79 | t |
| fy1 | 4.85 | spelDelar.2.t, spelDelar.3.t, spelDelar.4.t, spelIntro, t |
| fy1 | 4.86 | t |
| fy1 | 4.90 | t |
| fy1 | 4.91 | t |
| fy1 | 4.94 | t |
| fy1 | 4.96 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.97 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.98 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.100 | t |
| fy1 | 4.103 | t |
| fy1 | 4.104 | spelIntro, t |
| fy1 | 4.391 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.105 | t |
| fy1 | 4.106 | t |
| fy1 | 4.108 | t |
| fy1 | 4.109 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.392 | t |
| fy1 | 4.111 | t |
| fy1 | 4.113 | t |
| fy1 | 4.114 | t |
| fy1 | 4.115 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.116 | t |
| fy1 | 4.117 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.393 | t |
| fy1 | 4.118 | t |
| fy1 | 4.119 | t |
| fy1 | 4.120 | t |
| fy1 | 4.121 | t |
| fy1 | 4.394 | t |
| fy1 | 4.122 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.123 | t |
| fy1 | 4.124 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.395 | t |
| fy1 | 4.125 | t |
| fy1 | 4.126 | t |
| fy1 | 4.127 | spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.130 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.132 | t |
| fy1 | 4.133 | t |
| fy1 | 4.138 | t |
| fy1 | 4.140 | t |
| fy1 | 4.146 | t |
| fy1 | 4.151 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.152 | t |
| fy1 | 4.153 | spelDelar.1.t, spelIntro, t |
| fy1 | 4.154 | t |
| fy1 | 4.155 | spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 4.157 | t |
| fy1 | 4.160 | spelDelar.2.t |
| fy1 | 4.166 | spelDelar.1.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.167 | spelDelar.2.t, spelIntro, t |
| fy1 | 4.434 | t |
| fy1 | 4.168 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.169 | spelDelar.0.t, spelDelar.1.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.435 | t |
| fy1 | 4.436 | t |
| fy1 | 4.171 | t |
| fy1 | 4.172 | t |
| fy1 | 4.173 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.174 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.449 | t |
| fy1 | 4.176 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.396 | t |
| fy1 | 4.177 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.178 | t |
| fy1 | 4.179 | t |
| fy1 | 4.397 | t |
| fy1 | 4.180 | t |
| fy1 | 4.181 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.333 | t |
| fy1 | 4.184 | t |
| fy1 | 4.185 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.186 | t |
| fy1 | 4.187 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.372 | t |
| fy1 | 4.188 | t |
| fy1 | 4.374 | t |
| fy1 | 4.375 | t |
| fy1 | 4.190 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.378 | t |
| fy1 | 4.191 | t |
| fy1 | 4.194 | t |
| fy1 | 4.196 | t |
| fy1 | 4.201 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.202 | t |
| fy1 | 4.437 | t |
| fy1 | 4.203 | t |
| fy1 | 4.204 | t |
| fy1 | 4.205 | t |
| fy1 | 4.206 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.207 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.208 | spelDelar.0.t, spelDelar.1.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.209 | t |
| fy1 | 4.210 | t |
| fy1 | 4.398 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.212 | t |
| fy1 | 4.213 | t |
| fy1 | 4.214 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.215 | t |
| fy1 | 4.216 | t |
| fy1 | 4.217 | t |
| fy1 | 4.735 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.736 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.737 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.738 | t |
| fy1 | 4.739 | t |
| fy1 | 4.740 | s, svarTabell, t |
| fy1 | 4.741 | t |
| fy1 | 4.742 | s, spelDelar.0.s, spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.s, spelDelar.3.t, spelIntro, svarTabell, t |
| fy1 | 4.743 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.744 | t |
| fy1 | 4.745 | t |
| fy1 | 4.748 | t |
| fy1 | 4.749 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.750 | t |
| fy1 | 4.751 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelDelar.4.t, t |
| fy1 | 4.752 | t |
| fy1 | 4.753 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.218 | t |
| fy1 | 4.220 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.224 | t |
| fy1 | 4.225 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.226 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.227 | t |
| fy1 | 4.228 | t |
| fy1 | 4.229 | t |
| fy1 | 4.231 | t |
| fy1 | 4.232 | t |
| fy1 | 4.233 | t |
| fy1 | 4.236 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.237 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.238 | t |
| fy1 | 4.240 | spelDelar.3.t, spelDelar.4.t, spelDelar.5.t, spelIntro, t |
| fy1 | 4.241 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.242 | t |
| fy1 | 4.245 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.249 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.254 | t |
| fy1 | 4.256 | t |
| fy1 | 4.262 | t |
| fy1 | 4.267 | t |
| fy1 | 4.268 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.269 | t |
| fy1 | 4.339 | t |
| fy1 | 4.271 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.272 | t |
| fy1 | 4.273 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.341 | t |
| fy1 | 4.275 | t |
| fy1 | 4.342 | t |
| fy1 | 4.276 | t |
| fy1 | 4.277 | t |
| fy1 | 4.441 | t |
| fy1 | 4.279 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.442 | t |
| fy1 | 4.280 | t |
| fy1 | 4.443 | t |
| fy1 | 4.281 | spelDelar.3.t |
| fy1 | 4.282 | t |
| fy1 | 4.444 | t |
| fy1 | 4.284 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.285 | t |
| fy1 | 4.446 | t |
| fy1 | 4.288 | t |
| fy1 | 4.450 | t |
| fy1 | 4.499 | t |
| fy1 | 4.516 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.517 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.518 | t |
| fy1 | 4.519 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.520 | t |
| fy1 | 4.521 | t |
| fy1 | 4.523 | t |
| fy1 | 4.524 | t |
| fy1 | 4.525 | t |
| fy1 | 4.526 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.527 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.528 | t |
| fy1 | 4.529 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.530 | spelDelar.1.t, spelIntro, t |
| fy1 | 4.531 | t |
| fy1 | 4.532 | t |
| fy1 | 4.533 | t |
| fy1 | 4.534 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.536 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.537 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.538 | t |
| fy1 | 4.539 | t |
| fy1 | 4.540 | t |
| fy1 | 4.541 | t |
| fy1 | 4.542 | t |
| fy1 | 4.543 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.545 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.546 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.547 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.548 | t |
| fy1 | 4.549 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.550 | t |
| fy1 | 4.551 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.552 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.553 | t |
| fy1 | 4.554 | t |
| fy1 | 4.555 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.556 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.563 | t |
| fy1 | 4.576 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.291 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.292 | t |
| fy1 | 4.293 | t |
| fy1 | 4.295 | t |
| fy1 | 4.298 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.557 | spelIntro, t |
| fy1 | 4.559 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.560 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.561 | t |
| fy1 | 4.562 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.564 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.566 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.567 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.568 | t |
| fy1 | 4.569 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.570 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.571 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.572 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.573 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.574 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.575 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.596 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.597 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.598 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.599 | t |
| fy1 | 4.630 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.632 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.643 | t |
| fy1 | 4.648 | spelDelar.0.t, spelIntro, t |
| fy1 | 4.650 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.651 | t |
| fy1 | 4.652 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.653 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.656 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.657 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.659 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.660 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.661 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.662 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.663 | t |
| fy1 | 4.664 | t |
| fy1 | 4.666 | t |
| fy1 | 4.667 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.668 | t |
| fy1 | 4.669 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.670 | t |
| fy1 | 4.700 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.714 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.715 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.718 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.719 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.721 | t |
| fy1 | 4.722 | t |
| fy1 | 4.723 | t |
| fy1 | 4.724 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 4.299 | t |
| fy1 | 4.302 | t |
| fy1 | 4.304 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.251 | t |
| fy1 | 5.322 | t |
| fy1 | 5.4 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.8 | t |
| fy1 | 5.9 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.10 | t |
| fy1 | 5.11 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.277 | t |
| fy1 | 5.298 | t |
| fy1 | 5.299 | t |
| fy1 | 5.300 | t |
| fy1 | 5.14 | spelDelar.0.t |
| fy1 | 5.16 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.17 | t |
| fy1 | 5.279 | t |
| fy1 | 5.301 | t |
| fy1 | 5.312 | t |
| fy1 | 5.20 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.21 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t |
| fy1 | 5.23 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.24 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.25 | t |
| fy1 | 5.28 | t |
| fy1 | 5.29 | t |
| fy1 | 5.30 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.280 | t |
| fy1 | 5.302 | t |
| fy1 | 5.35 | t |
| fy1 | 5.294 | t |
| fy1 | 5.36 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.42 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.45 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.46 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.47 | t |
| fy1 | 5.261 | t |
| fy1 | 5.309 | t |
| fy1 | 5.50 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.52 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.53 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.56 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.57 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.59 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.60 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.62 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.63 | t |
| fy1 | 5.64 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.66 | spelDelar.1.t |
| fy1 | 5.67 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.68 | t |
| fy1 | 5.69 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.71 | spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.72 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.262 | t |
| fy1 | 5.325 | t |
| fy1 | 5.331 | t |
| fy1 | 5.74 | t |
| fy1 | 5.76 | t |
| fy1 | 5.78 | t |
| fy1 | 5.80 | t |
| fy1 | 5.81 | spelDelar.0.t, spelDelar.2.t |
| fy1 | 5.82 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 5.84 | spelDelar.0.t |
| fy1 | 5.89 | t |
| fy1 | 5.95 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.96 | t |
| fy1 | 5.97 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.98 | spelDelar.1.t, spelIntro, t |
| fy1 | 5.99 | spelDelar.2.t, spelIntro, t |
| fy1 | 5.101 | t |
| fy1 | 5.102 | t |
| fy1 | 5.103 | t |
| fy1 | 5.106 | t |
| fy1 | 5.107 | t |
| fy1 | 5.108 | spelDelar.2.t, spelIntro, t |
| fy1 | 5.110 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.111 | t |
| fy1 | 5.112 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.114 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.115 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.116 | t |
| fy1 | 5.118 | spelDelar.0.t |
| fy1 | 5.120 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.122 | t |
| fy1 | 5.123 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.127 | t |
| fy1 | 5.128 | t |
| fy1 | 5.131 | spelDelar.0.t |
| fy1 | 5.132 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.134 | t |
| fy1 | 5.135 | t |
| fy1 | 5.137 | t |
| fy1 | 5.138 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.140 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.145 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.147 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t |
| fy1 | 5.150 | t |
| fy1 | 5.151 | t |
| fy1 | 5.272 | t |
| fy1 | 5.152 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.153 | t |
| fy1 | 5.154 | t |
| fy1 | 5.156 | t |
| fy1 | 5.157 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 5.160 | spelDelar.0.t |
| fy1 | 5.161 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t |
| fy1 | 5.162 | spelDelar.0.t |
| fy1 | 5.165 | t |
| fy1 | 5.168 | t |
| fy1 | 5.169 | t |
| fy1 | 5.170 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.171 | t |
| fy1 | 5.172 | t |
| fy1 | 5.173 | t |
| fy1 | 5.174 | t |
| fy1 | 6.2 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.222 | t |
| fy1 | 6.3 | t |
| fy1 | 6.251 | t |
| fy1 | 6.4 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.5 | t |
| fy1 | 6.6 | spelDelar.2.t, spelIntro, t |
| fy1 | 6.269 | t |
| fy1 | 6.7 | t |
| fy1 | 6.223 | t |
| fy1 | 6.8 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.252 | t |
| fy1 | 6.300 | t |
| fy1 | 6.301 | t |
| fy1 | 6.304 | t |
| fy1 | 6.253 | t |
| fy1 | 6.306 | t |
| fy1 | 6.11 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 6.14 | t |
| fy1 | 6.270 | t |
| fy1 | 6.17 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.271 | t |
| fy1 | 6.321 | t |
| fy1 | 6.18 | t |
| fy1 | 6.23 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.24 | t |
| fy1 | 6.25 | t |
| fy1 | 6.26 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.27 | t |
| fy1 | 6.228 | t |
| fy1 | 6.28 | t |
| fy1 | 6.29 | t |
| fy1 | 6.229 | t |
| fy1 | 6.30 | t |
| fy1 | 6.254 | t |
| fy1 | 6.305 | t |
| fy1 | 6.31 | t |
| fy1 | 6.32 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.255 | t |
| fy1 | 6.309 | t |
| fy1 | 6.33 | t |
| fy1 | 6.272 | t |
| fy1 | 6.327 | t |
| fy1 | 6.37 | t |
| fy1 | 6.273 | t |
| fy1 | 6.39 | t |
| fy1 | 6.43 | t |
| fy1 | 6.256 | t |
| fy1 | 6.308 | t |
| fy1 | 6.44 | t |
| fy1 | 6.152 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.45 | t |
| fy1 | 6.46 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 6.274 | t |
| fy1 | 6.47 | t |
| fy1 | 6.48 | t |
| fy1 | 6.51 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 6.290 | t |
| fy1 | 6.292 | t |
| fy1 | 6.52 | spelDelar.0.t, spelDelar.2.t, t |
| fy1 | 6.257 | t |
| fy1 | 6.53 | spelDelar.1.t, spelIntro, t |
| fy1 | 6.54 | spelDelar.0.t, spelDelar.1.t |
| fy1 | 6.55 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.56 | t |
| fy1 | 6.235 | t |
| fy1 | 6.57 | t |
| fy1 | 6.237 | t |
| fy1 | 6.59 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.60 | t |
| fy1 | 6.239 | t |
| fy1 | 6.61 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.258 | t |
| fy1 | 6.63 | t |
| fy1 | 6.259 | t |
| fy1 | 6.65 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 6.153 | t |
| fy1 | 6.66 | t |
| fy1 | 6.260 | t |
| fy1 | 6.67 | t |
| fy1 | 6.157 | t |
| fy1 | 6.261 | t |
| fy1 | 6.68 | t |
| fy1 | 6.69 | t |
| fy1 | 6.70 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.154 | t |
| fy1 | 6.275 | t |
| fy1 | 6.72 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.74 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.76 | spelDelar.4.t, spelIntro, t |
| fy1 | 6.77 | spelDelar.0.t, spelIntro, t |
| fy1 | 6.79 | t |
| fy1 | 6.85 | t |
| fy1 | 6.91 | t |
| fy1 | 6.241 | t |
| fy1 | 6.93 | t |
| fy1 | 6.95 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.96 | t |
| fy1 | 6.98 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.246 | t |
| fy1 | 6.99 | t |
| fy1 | 6.101 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.263 | t |
| fy1 | 6.102 | t |
| fy1 | 6.264 | t |
| fy1 | 6.104 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy1 | 6.105 | t |
| fy1 | 6.265 | t |
| fy1 | 6.106 | t |
| fy1 | 6.155 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 6.107 | spelDelar.0.t, t |
| fy1 | 6.266 | t |
| fy1 | 6.109 | spelDelar.0.t, spelDelar.2.t, t |
| fy1 | 6.267 | t |
| fy1 | 6.110 | t |
| fy1 | 6.111 | t |
| fy1 | 6.112 | t |
| fy1 | 6.113 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.280 | t |
| fy1 | 6.114 | spelIntro, t |
| fy1 | 6.118 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.119 | spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 6.283 | t |
| fy1 | 6.125 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.126 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.128 | t |
| fy1 | 6.268 | t |
| fy1 | 6.131 | t |
| fy1 | 6.132 | t |
| fy1 | 6.133 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy1 | 6.307 | t |
| fy1 | 6.249 | t |
| fy1 | 7.2 | t |
| fy1 | 7.3 | t |
| fy1 | 7.8 | t |
| fy1 | 7.12 | t |
| fy1 | 7.13 | spelIntro, t |
| fy1 | 7.18 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 7.42 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.5 | spelIntro, t |
| fy1 | 8.9 | t |
| fy1 | 8.15 | spelDelar.2.t |
| fy1 | 8.21 | spelIntro, t |
| fy1 | 8.22 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 8.23 | spelIntro, t |
| fy1 | 8.297 | t |
| fy1 | 8.24 | spelIntro, t |
| fy1 | 8.298 | t |
| fy1 | 8.25 | spelIntro, t |
| fy1 | 8.33 | spelIntro, t |
| fy1 | 8.35 | spelIntro, t |
| fy1 | 8.302 | t |
| fy1 | 8.47 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.327 | t |
| fy1 | 8.48 | t |
| fy1 | 8.330 | t |
| fy1 | 8.57 | spelIntro, t |
| fy1 | 8.58 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.304 | t |
| fy1 | 8.59 | spelIntro, t |
| fy1 | 8.305 | t |
| fy1 | 8.68 | spelIntro, t |
| fy1 | 8.69 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.306 | t |
| fy1 | 8.70 | t |
| fy1 | 8.72 | spelIntro, t |
| fy1 | 8.74 | spelIntro, t |
| fy1 | 8.310 | t |
| fy1 | 8.78 | spelIntro, t |
| fy1 | 8.83 | spelIntro, t |
| fy1 | 8.92 | spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 8.337 | t |
| fy1 | 8.101 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.339 | t |
| fy1 | 8.341 | t |
| fy1 | 8.104 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.343 | t |
| fy1 | 8.345 | t |
| fy1 | 8.106 | spelIntro, t |
| fy1 | 8.347 | t |
| fy1 | 8.348 | t |
| fy1 | 8.349 | t |
| fy1 | 8.110 | spelIntro, t |
| fy1 | 8.114 | t |
| fy1 | 8.351 | t |
| fy1 | 8.352 | t |
| fy1 | 8.115 | spelDelar.2.t, spelIntro, t |
| fy1 | 8.119 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.311 | t |
| fy1 | 8.312 | t |
| fy1 | 8.121 | spelIntro, t |
| fy1 | 8.143 | spelIntro, t |
| fy1 | 8.146 | spelIntro, t |
| fy1 | 8.159 | spelIntro, t |
| fy1 | 8.160 | spelIntro, t |
| fy1 | 8.161 | spelDelar.2.t, spelIntro, t |
| fy1 | 8.239 | t |
| fy1 | 8.163 | spelIntro, t |
| fy1 | 8.294 | t |
| fy1 | 8.355 | t |
| fy1 | 8.358 | t |
| fy1 | 8.170 | spelDelar.1.t, spelIntro, t |
| fy1 | 8.360 | t |
| fy1 | 9.5 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.8 | spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.9 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.10 | spelDelar.3.fraga, spelDelar.3.t, spelIntro, t |
| fy1 | 9.12 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.19 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.20 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.21 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.22 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.26 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.31 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.32 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.35 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.45 | t |
| fy1 | 9.46 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.48 | spelIntro |
| fy1 | 9.49 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.53 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.59 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.224 | t |
| fy1 | 9.61 | spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.62 | spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.228 | t |
| fy1 | 9.232 | t |
| fy1 | 9.233 | t |
| fy1 | 9.234 | t |
| fy1 | 9.66 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.235 | t |
| fy1 | 9.236 | t |
| fy1 | 9.68 | t |
| fy1 | 9.239 | t |
| fy1 | 9.240 | t |
| fy1 | 9.69 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.71 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.72 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.198 | t |
| fy1 | 9.76 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.148 | t |
| fy1 | 4.305 | t |
| fy1 | 4.307 | t |
| fy1 | 4.345 | t |
| fy1 | 8.316 | t |
| fy1 | 8.172 | t |
| fy1 | 8.173 | t |
| fy1 | 8.318 | t |
| fy1 | 8.174 | t |
| fy1 | 4.309 | t |
| fy1 | 4.506 | t |
| fy1 | 4.508 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.510 | t |
| fy1 | 4.511 | t |
| fy1 | 4.512 | t |
| fy1 | 4.515 | t |
| fy1 | 6.336 | t |
| fy1 | 5.176 | t |
| fy1 | 5.323 | t |
| fy1 | 5.324 | t |
| fy1 | 5.326 | t |
| fy1 | 5.327 | t |
| fy1 | 5.332 | t |
| fy1 | 9.99 | t |
| fy1 | 5.177 | t |
| fy1 | 8.439 | t |
| fy1 | 8.440 | t |
| fy1 | 8.441 | t |
| fy1 | 8.442 | t |
| fy1 | 8.443 | t |
| fy1 | 8.444 | t |
| fy1 | 8.473 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 8.181 | t |
| fy1 | 9.100 | t |
| fy1 | 9.101 | t |
| fy1 | 9.199 | t |
| fy1 | 9.102 | t |
| fy1 | 9.104 | t |
| fy1 | 4.316 | t |
| fy1 | 4.317 | t |
| fy1 | 4.500 | t |
| fy1 | 4.671 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.672 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.673 | t |
| fy1 | 4.674 | t |
| fy1 | 4.318 | t |
| fy1 | 4.319 | t |
| fy1 | 4.320 | t |
| fy1 | 4.321 | t |
| fy1 | 4.322 | t |
| fy1 | 5.303 | t |
| fy1 | 5.304 | t |
| fy1 | 5.305 | t |
| fy1 | 5.306 | t |
| fy1 | 5.307 | t |
| fy1 | 5.308 | t |
| fy1 | 5.367 | t |
| fy1 | 5.368 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, t |
| fy1 | 5.370 | spelDelar.0.t, spelDelar.1.t |
| fy1 | 5.371 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t |
| fy1 | 5.373 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.374 | t |
| fy1 | 5.381 | spelDelar.0.t, spelDelar.1.t |
| fy1 | 5.384 | spelDelar.0.t, spelDelar.1.t |
| fy1 | 5.386 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 5.394 | t |
| fy1 | 5.395 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.396 | t |
| fy1 | 5.397 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, t |
| fy1 | 5.398 | spelDelar.0.t, spelDelar.1.t |
| fy1 | 5.399 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.400 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, t |
| fy1 | 7.63 | t |
| fy1 | 7.137 | spelDelar.2.t, spelIntro, t |
| fy1 | 7.140 | spelIntro, t |
| fy1 | 7.146 | t |
| fy1 | 7.150 | spelDelar.0.t, spelIntro, t |
| fy1 | 7.151 | t |
| fy1 | 7.152 | t |
| fy1 | 7.157 | t |
| fy1 | 7.162 | t |
| fy1 | 7.207 | t |
| fy1 | 7.210 | t |
| fy1 | 7.214 | t |
| fy1 | 7.217 | t |
| fy1 | 7.218 | spelIntro, t |
| fy1 | 7.220 | t |
| fy1 | 7.221 | spelDelar.0.t, spelIntro, t |
| fy1 | 8.446 | spelIntro, t |
| fy1 | 3.202 | spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 3.219 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 3.220 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy1 | 3.221 | spelDelar.0.t, spelDelar.1.t, t |
| fy1 | 3.222 | t |
| fy1 | 5.183 | t |
| fy1 | 5.187 | t |
| fy1 | 5.189 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.192 | t |
| fy1 | 5.193 | t |
| fy1 | 5.194 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.195 | t |
| fy1 | 5.197 | t |
| fy1 | 5.198 | t |
| fy1 | 5.200 | t |
| fy1 | 5.201 | t |
| fy1 | 5.204 | t |
| fy1 | 5.209 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.211 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.212 | t |
| fy1 | 5.213 | t |
| fy1 | 5.214 | spelDelar.1.t, spelIntro, t |
| fy1 | 5.219 | t |
| fy1 | 5.220 | t |
| fy1 | 5.216 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.217 | t |
| fy1 | 5.218 | t |
| fy1 | 5.221 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.222 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.223 | t |
| fy1 | 5.224 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.225 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.182 | t |
| fy1 | 6.183 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.185 | t |
| fy1 | 6.191 | t |
| fy1 | 6.192 | t |
| fy1 | 6.193 | t |
| fy1 | 6.194 | t |
| fy1 | 6.195 | t |
| fy1 | 6.196 | t |
| fy1 | 6.173 | t |
| fy1 | 6.197 | t |
| fy1 | 9.200 | t |
| fy1 | 9.109 | t |
| fy1 | 9.110 | spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.111 | spelDelar.1.fraga, spelDelar.1.t, spelDelar.4.fraga, spelDelar.4.t, spelIntro, t |
| fy1 | 9.115 | t |
| fy1 | 9.116 | t |
| fy1 | 6.200 | t |
| fy1 | 6.201 | spelDelar.0.t, spelIntro, t |
| fy1 | 6.202 | spelDelar.1.t, spelIntro, t |
| fy1 | 6.203 | t |
| fy1 | 6.204 | t |
| fy1 | 6.205 | t |
| fy1 | 6.207 | t |
| fy1 | 6.208 | t |
| fy1 | 6.209 | t |
| fy1 | 6.210 | t |
| fy1 | 9.117 | t |
| fy1 | 6.212 | t |
| fy1 | 9.118 | t |
| fy1 | 9.119 | spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 3.228 | t |
| fy1 | 3.273 | t |
| fy1 | 3.274 | t |
| fy1 | 3.275 | t |
| fy1 | 3.392 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.393 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 3.394 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.395 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.396 | t |
| fy1 | 3.397 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.398 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 3.399 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.400 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.401 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 3.402 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.403 | t |
| fy1 | 3.404 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.405 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.406 | t |
| fy1 | 3.407 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 3.408 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 3.409 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.227 | t |
| fy1 | 5.228 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.229 | t |
| fy1 | 5.233 | t |
| fy1 | 5.238 | t |
| fy1 | 5.239 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.240 | t |
| fy1 | 5.241 | t |
| fy1 | 5.242 | t |
| fy1 | 5.243 | t |
| fy1 | 5.244 | t |
| fy1 | 5.245 | t |
| fy1 | 5.246 | t |
| fy1 | 5.247 | t |
| fy1 | 5.248 | t |
| fy1 | 5.249 | t |
| fy1 | 5.250 | t |
| fy1 | GY25-FY1-EM-02 | t |
| fy1 | GY25-FY1-EN-01 | t |
| fy1 | 5.551 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.552 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.555 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.556 | spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.559 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.561 | t |
| fy1 | 5.562 | s, spelDelar.1.s, spelDelar.1.t, spelDelar.3.t, spelIntro, svarTabell, t |
| fy1 | 5.564 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.565 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.566 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.567 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.568 | t |
| fy1 | 5.569 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.570 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.571 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.572 | t |
| fy1 | 5.574 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.575 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.578 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.579 | t |
| fy1 | 5.580 | t |
| fy1 | 5.581 | t |
| fy1 | 5.582 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.583 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.584 | t |
| fy1 | 5.585 | t |
| fy1 | 5.586 | t |
| fy1 | 5.587 | t |
| fy1 | 5.592 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.593 | t |
| fy1 | 5.594 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.595 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.596 | t |
| fy1 | 5.599 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.334 | t |
| fy1 | 5.335 | t |
| fy1 | 5.336 | t |
| fy1 | 5.337 | t |
| fy1 | 5.338 | t |
| fy1 | 5.339 | t |
| fy1 | 5.340 | t |
| fy1 | 5.341 | t |
| fy1 | 5.345 | t |
| fy1 | 5.346 | t |
| fy1 | 5.347 | t |
| fy1 | 5.348 | t |
| fy1 | 5.349 | t |
| fy1 | 5.357 | t |
| fy1 | 5.473 | spelDelar.0.t, spelDelar.1.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.474 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.475 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.476 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.477 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.478 | t |
| fy1 | 5.479 | t |
| fy1 | 5.480 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.481 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.482 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.483 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.484 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.485 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.486 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.487 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.488 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.489 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.491 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.492 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.493 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.494 | t |
| fy1 | 5.495 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.496 | t |
| fy1 | 5.503 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t |
| fy1 | 5.508 | t |
| fy1 | 5.511 | spelDelar.3.t, spelIntro, t |
| fy1 | 5.514 | spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.517 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.518 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.519 | t |
| fy1 | 5.536 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.537 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.539 | t |
| fy1 | 5.540 | t |
| fy1 | 5.541 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.542 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.543 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.544 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.545 | t |
| fy1 | 5.546 | spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 5.547 | t |
| fy1 | 5.548 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.549 | t |
| fy1 | 5.550 | t |
| fy1 | KG-FY1-ALFA-03 | t |
| fy1 | KG-FY1-BP-04 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.388 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.389 | spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.390 | t |
| fy1 | 9.391 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.392 | t |
| fy1 | 9.393 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.394 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.395 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.396 | t |
| fy1 | 9.397 | t |
| fy1 | 9.398 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.399 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.400 | t |
| fy1 | 9.401 | t |
| fy1 | 9.402 | spelDelar.0.fraga, spelDelar.0.t, t |
| fy1 | 9.403 | t |
| fy1 | 9.407 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.408 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.409 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.410 | spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.411 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.341 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.342 | t |
| fy1 | 9.344 | t |
| fy1 | 9.345 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.350 | t |
| fy1 | 9.351 | t |
| fy1 | 9.353 | t |
| fy1 | 9.354 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.355 | t |
| fy1 | 9.358 | t |
| fy1 | 9.359 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.360 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.365 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.366 | t |
| fy1 | 9.367 | t |
| fy1 | 9.368 | t |
| fy1 | 9.369 | t |
| fy1 | 9.371 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.373 | spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.375 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.376 | t |
| fy1 | 9.378 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.379 | t |
| fy1 | 9.382 | t |
| fy1 | 9.384 | t |
| fy1 | 9.385 | spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.386 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.387 | t |
| fy1 | 6.310 | t |
| fy1 | 6.311 | t |
| fy1 | 6.320 | t |
| fy1 | 6.313 | t |
| fy1 | 6.324 | t |
| fy1 | 6.312 | t |
| fy1 | 6.323 | t |
| fy1 | 6.334 | t |
| fy1 | 6.337 | t |
| fy1 | 6.338 | t |
| fy1 | 6.347 | t |
| fy1 | 6.330 | t |
| fy1 | 6.346 | t |
| fy1 | 6.348 | t |
| fy1 | 6.349 | t |
| fy1 | 6.350 | t |
| fy1 | 6.352 | t |
| fy1 | 6.367 | spelDelar.0.t, spelIntro, t |
| fy1 | 6.368 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.419 | spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 6.420 | t |
| fy1 | 6.422 | spelDelar.1.t, spelIntro, t |
| fy1 | 6.423 | spelDelar.1.t, spelIntro, t |
| fy1 | 6.426 | t |
| fy1 | 6.430 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.431 | t |
| fy1 | 6.434 | t |
| fy1 | 6.447 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.448 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 6.449 | t |
| fy1 | 6.451 | t |
| fy1 | 6.356 | t |
| fy1 | 6.357 | t |
| fy1 | 6.436 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.437 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.438 | t |
| fy1 | 6.439 | spelDelar.1.t, t |
| fy1 | 6.440 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.441 | t |
| fy1 | 6.442 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.443 | spelDelar.0.t, spelIntro, t |
| fy1 | 6.444 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.445 | spelDelar.0.t, spelIntro, t |
| fy1 | 6.446 | t |
| fy1 | 6.452 | t |
| fy1 | 6.453 | t |
| fy1 | 6.454 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.455 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.456 | t |
| fy1 | 6.457 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.458 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.459 | t |
| fy1 | 6.460 | t |
| fy1 | 6.461 | t |
| fy1 | 6.462 | t |
| fy1 | 6.463 | spelDelar.1.t, spelIntro, t |
| fy1 | 6.464 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.465 | t |
| fy1 | 6.358 | t |
| fy1 | 6.359 | t |
| fy1 | 6.466 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.468 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.470 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.471 | t |
| fy1 | 6.472 | t |
| fy1 | 6.473 | t |
| fy1 | 6.474 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.476 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.477 | t |
| fy1 | 6.478 | t |
| fy1 | 6.479 | t |
| fy1 | 6.481 | t |
| fy1 | 6.483 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.484 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.485 | t |
| fy1 | 6.487 | spelIntro, t |
| fy1 | 6.488 | t |
| fy1 | 6.489 | t |
| fy1 | 6.490 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.492 | t |
| fy1 | 6.493 | t |
| fy1 | 6.494 | t |
| fy1 | 6.495 | t |
| fy1 | 6.496 | spelDelar.2.t, spelIntro, t |
| fy1 | 6.497 | t |
| fy1 | 6.498 | t |
| fy1 | 6.499 | t |
| fy1 | 6.500 | t |
| fy1 | 6.501 | t |
| fy1 | 6.502 | t |
| fy1 | 6.503 | t |
| fy1 | 6.504 | t |
| fy1 | 6.505 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.507 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.508 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.509 | t |
| fy1 | 6.510 | t |
| fy1 | 6.511 | t |
| fy1 | 6.512 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.529 | t |
| fy1 | 6.536 | t |
| fy1 | 6.537 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 6.538 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.539 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.540 | t |
| fy1 | 6.543 | spelDelar.0.t, spelIntro, t |
| fy1 | 6.544 | spelDelar.1.t, spelIntro, t |
| fy1 | 6.545 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.546 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 6.547 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 4.467 | t |
| fy1 | 4.468 | t |
| fy1 | 4.470 | t |
| fy1 | 4.471 | t |
| fy1 | 4.472 | t |
| fy1 | 4.498 | t |
| fy1 | 4.503 | t |
| fy1 | 4.504 | t |
| fy1 | 4.475 | t |
| fy1 | 4.476 | t |
| fy1 | 4.477 | t |
| fy1 | 4.478 | t |
| fy1 | 4.480 | t |
| fy1 | 4.481 | t |
| fy1 | 4.482 | t |
| fy1 | 4.484 | t |
| fy1 | 4.497 | t |
| fy1 | 4.502 | t |
| fy1 | 4.636 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.637 | t |
| fy1 | 4.638 | t |
| fy1 | 4.639 | t |
| fy1 | 4.640 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.641 | t |
| fy1 | 4.642 | t |
| fy1 | 4.644 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.645 | t |
| fy1 | 4.646 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.647 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.485 | t |
| fy1 | 4.486 | t |
| fy1 | 4.487 | t |
| fy1 | 4.489 | t |
| fy1 | 4.490 | t |
| fy1 | 4.492 | t |
| fy1 | 4.578 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.579 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.580 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.582 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.583 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.584 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.585 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.586 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.587 | t |
| fy1 | 4.589 | t |
| fy1 | 4.590 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.591 | t |
| fy1 | 4.592 | t |
| fy1 | 4.593 | spelDelar.0.t, spelIntro, t |
| fy1 | 4.594 | t |
| fy1 | 4.600 | t |
| fy1 | 4.601 | t |
| fy1 | 4.602 | t |
| fy1 | 4.603 | t |
| fy1 | 4.604 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.605 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.606 | t |
| fy1 | 4.607 | t |
| fy1 | 4.608 | t |
| fy1 | 4.609 | t |
| fy1 | 4.610 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.611 | t |
| fy1 | 4.612 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.613 | t |
| fy1 | 4.614 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.615 | t |
| fy1 | 4.616 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.617 | t |
| fy1 | 4.618 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.619 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.620 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.621 | t |
| fy1 | 4.622 | t |
| fy1 | 4.623 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 4.624 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.625 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.626 | t |
| fy1 | 4.628 | t |
| fy1 | 4.629 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.631 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.633 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 4.634 | t |
| fy1 | 4.635 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 8.373 | t |
| fy1 | 8.374 | t |
| fy1 | 8.375 | t |
| fy1 | 8.391 | spelIntro, t |
| fy1 | 8.394 | t |
| fy1 | 8.475 | t |
| fy1 | 8.464 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 8.468 | t |
| fy1 | 8.469 | t |
| fy1 | 8.470 | spelDelar.0.t, spelIntro, t |
| fy1 | 8.471 | t |
| fy1 | 9.326 | t |
| fy1 | 9.328 | t |
| fy1 | 9.289 | t |
| fy1 | 9.291 | t |
| fy1 | 9.292 | t |
| fy1 | 9.294 | t |
| fy1 | 9.414 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, t |
| fy1 | 9.415 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.416 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelDelar.3.fraga, spelDelar.3.t, spelIntro, t |
| fy1 | 9.417 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelDelar.2.fraga, spelDelar.2.t, spelIntro, t |
| fy1 | 9.418 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.419 | spelDelar.0.fraga, spelDelar.0.t, spelDelar.1.fraga, spelDelar.1.t, spelIntro, t |
| fy1 | 9.420 | spelDelar.0.fraga, spelDelar.0.t, spelIntro, t |
| fy1 | 9.304 | t |
| fy1 | 9.305 | t |
| fy1 | 9.306 | t |
| fy1 | 9.310 | t |
| fy1 | 9.311 | t |
| fy1 | 5.497 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.498 | s, spelDelar.0.t, spelDelar.1.t, spelDelar.2.s, spelDelar.2.t, spelIntro, svarTabell, t |
| fy1 | 5.499 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.500 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.501 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.502 | t |
| fy1 | 5.520 | spelDelar.0.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.522 | t |
| fy1 | 5.523 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.525 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.526 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.527 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.528 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.530 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy1 | 5.531 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.532 | spelDelar.0.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy1 | 5.533 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.534 | spelDelar.1.t, spelIntro, t |
| fy1 | 5.362 | t |
| fy1 | 5.404 | t |
| fy1 | 5.420 | spelDelar.2.t, t |
| fy1 | 5.421 | t |
| fy1 | 5.426 | spelDelar.1.t, spelIntro, t |
| fy1 | 5.429 | t |
| fy1 | 5.431 | spelDelar.0.t, spelDelar.1.t |
| fy1 | 5.437 | t |
| fy1 | 5.445 | t |
| fy1 | 5.447 | spelDelar.0.t, t |
| fy1 | 5.448 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 5.449 | t |
| fy1 | 5.450 | t |
| fy1 | 5.451 | t |
| fy1 | 5.458 | t |
| fy1 | 5.459 | t |
| fy1 | 5.460 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.461 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.462 | t |
| fy1 | 5.464 | spelDelar.0.t, spelIntro, t |
| fy1 | 5.465 | t |
| fy1 | 5.466 | t |
| fy1 | 5.469 | t |
| fy1 | 5.470 | spelDelar.1.t |
| fy1 | 5.472 | t |
| fy1 | 8.476 | t |
| fy1 | 8.477 | t |
| fy1 | 8.478 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 8.479 | spelIntro, t |
| fy1 | 8.480 | t |
| fy1 | 8.481 | t |
| fy1 | 8.482 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 8.483 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 8.485 | spelDelar.0.t, spelIntro, t |
| fy1 | 8.486 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy1 | 8.487 | t |
| fy1 | 8.488 | spelIntro, t |
| fy1 | 8.489 | t |
| fy1 | 8.490 | t |
| fy1 | 8.491 | spelDelar.0.t, spelIntro, t |
| fy1 | 8.492 | t |
| fy1 | 8.493 | spelIntro, t |
| fy1 | 8.494 | t |
| fy1 | 9.323 | t |
| fy1 | 9.324 | t |
| fy1 | 9.325 | t |
| fy1 | 9.327 | t |
| fy1 | 6.550 | t |
| fy1 | 6.551 | t |
| fy1 | 6.555 | t |
| fy2 | 1.13 | t |
| fy2 | 1.39 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy2 | 1.69 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy2 | 1.79 | t |
| fy2 | 1.113 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 1.114 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 1.115 | t |
| fy2 | 1.116 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 1.117 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 1.118 | t |
| fy2 | 1.119 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 1.120 | t |
| fy2 | 1.121 | t |
| fy2 | 1.122 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 1.123 | t |
| fy2 | 1.124 | t |
| fy2 | 1.125 | t |
| fy2 | 1.126 | t |
| fy2 | 1.127 | t |
| fy2 | 1.128 | t |
| fy2 | 1.129 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 1.130 | t |
| fy2 | 1.131 | t |
| fy2 | 1.132 | t |
| fy2 | 1.133 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 1.134 | t |
| fy2 | 1.135 | t |
| fy2 | 1.136 | t |
| fy2 | 1.137 | t |
| fy2 | 2.310 | t |
| fy2 | 2.471 | t |
| fy2 | 2.476 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.483 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.484 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.485 | t |
| fy2 | 2.507 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelDelar.4.t, spelIntro, t |
| fy2 | 2.508 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 2.509 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 2.515 | t |
| fy2 | 2.518 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.521 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.522 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.523 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.526 | t |
| fy2 | 2.528 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.530 | t |
| fy2 | 2.531 | t |
| fy2 | 2.533 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.535 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.536 | t |
| fy2 | 2.537 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.36 | t |
| fy2 | 2.71 | t |
| fy2 | 2.72 | t |
| fy2 | 2.73 | t |
| fy2 | 2.79 | t |
| fy2 | 2.84 | t |
| fy2 | 2.85 | t |
| fy2 | 2.92 | t |
| fy2 | 2.93 | t |
| fy2 | 2.95 | t |
| fy2 | 2.96 | t |
| fy2 | 2.112 | t |
| fy2 | 2.115 | t |
| fy2 | 2.122 | t |
| fy2 | 2.141 | t |
| fy2 | 2.142 | t |
| fy2 | 2.143 | t |
| fy2 | 2.149 | t |
| fy2 | 2.150 | t |
| fy2 | 2.157 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 2.165 | t |
| fy2 | 2.166 | t |
| fy2 | 2.167 | t |
| fy2 | 2.168 | t |
| fy2 | 2.169 | t |
| fy2 | 2.170 | t |
| fy2 | 2.171 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 3.3 | spelDelar.1.t |
| fy2 | 3.12 | t |
| fy2 | 3.33 | t |
| fy2 | 3.51 | t |
| fy2 | 3.53 | t |
| fy2 | 3.55 | t |
| fy2 | 3.72 | t |
| fy2 | 3.366 | t |
| fy2 | 3.367 | t |
| fy2 | 3.368 | t |
| fy2 | 3.369 | t |
| fy2 | 3.370 | t |
| fy2 | 3.371 | t |
| fy2 | 3.372 | t |
| fy2 | 3.373 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.374 | t |
| fy2 | 3.375 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 3.376 | t |
| fy2 | 3.377 | t |
| fy2 | 3.364 | t |
| fy2 | 3.365 | t |
| fy2 | 4.3 | t |
| fy2 | 4.7 | t |
| fy2 | 4.9 | t |
| fy2 | 4.18 | spelDelar.1.t, t |
| fy2 | 4.24 | t |
| fy2 | 4.31 | spelDelar.1.t |
| fy2 | 4.36 | spelDelar.1.t |
| fy2 | 3.336 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 3.337 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.338 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.339 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.340 | t |
| fy2 | 3.341 | t |
| fy2 | 3.342 | t |
| fy2 | 3.343 | t |
| fy2 | 3.344 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.345 | t |
| fy2 | 5.5 | t |
| fy2 | 5.6 | t |
| fy2 | 5.9 | t |
| fy2 | 5.11 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 5.12 | t |
| fy2 | 5.16 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy2 | 5.19 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 5.20 | spelDelar.1.t, t |
| fy2 | 5.21 | t |
| fy2 | 5.22 | t |
| fy2 | 5.23 | t |
| fy2 | 5.29 | t |
| fy2 | 5.30 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 5.31 | t |
| fy2 | 5.32 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 5.33 | t |
| fy2 | 5.34 | t |
| fy2 | 5.35 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy2 | 5.38 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelDelar.4.t, t |
| fy2 | 5.39 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 5.40 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, t |
| fy2 | 5.42 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelDelar.4.t, spelDelar.5.t, t |
| fy2 | 5.43 | t |
| fy2 | 4.51 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy2 | 5.44 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 4.53 | t |
| fy2 | 4.54 | t |
| fy2 | 5.45 | t |
| fy2 | 2.438 | t |
| fy2 | 2.439 | t |
| fy2 | 2.440 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.443 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 2.445 | t |
| fy2 | 2.446 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.447 | t |
| fy2 | 2.449 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.450 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.456 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.457 | t |
| fy2 | 2.459 | t |
| fy2 | 2.462 | t |
| fy2 | 2.463 | t |
| fy2 | 2.354 | t |
| fy2 | 2.355 | t |
| fy2 | 2.356 | t |
| fy2 | 2.358 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.359 | t |
| fy2 | 2.361 | t |
| fy2 | 3.111 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 3.353 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.354 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.355 | t |
| fy2 | 3.356 | t |
| fy2 | 4.57 | t |
| fy2 | 3.312 | t |
| fy2 | 3.313 | t |
| fy2 | 3.314 | t |
| fy2 | 3.315 | t |
| fy2 | 3.316 | t |
| fy2 | 3.317 | t |
| fy2 | 3.319 | t |
| fy2 | 3.320 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.321 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.322 | t |
| fy2 | 3.323 | t |
| fy2 | 3.324 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.325 | t |
| fy2 | 3.326 | t |
| fy2 | 3.327 | t |
| fy2 | 3.328 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.329 | t |
| fy2 | 3.330 | t |
| fy2 | 3.332 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.333 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.334 | t |
| fy2 | 3.335 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.58 | spelDelar.0.t, spelDelar.1.t, t |
| fy2 | 4.70 | t |
| fy2 | 5.52 | spelDelar.0.t, t |
| fy2 | 5.58 | t |
| fy2 | 5.59 | t |
| fy2 | 5.60 | t |
| fy2 | 5.53 | spelDelar.2.t, t |
| fy2 | 5.343 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.344 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.345 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.346 | t |
| fy2 | 5.347 | t |
| fy2 | 5.348 | t |
| fy2 | 5.61 | t |
| fy2 | 5.62 | t |
| fy2 | 5.63 | t |
| fy2 | 5.349 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.350 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.351 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.352 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 5.354 | t |
| fy2 | 2.408 | t |
| fy2 | 2.410 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.412 | t |
| fy2 | 2.413 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.417 | t |
| fy2 | 2.362 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.363 | t |
| fy2 | 2.364 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.369 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.370 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.371 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.372 | t |
| fy2 | 2.373 | t |
| fy2 | 2.375 | t |
| fy2 | 2.376 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.378 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.381 | t |
| fy2 | 2.382 | t |
| fy2 | 2.384 | t |
| fy2 | 2.385 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.386 | t |
| fy2 | 6.56 | spelDelar.1.t, t |
| fy2 | 6.58 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, t |
| fy2 | 4.321 | t |
| fy2 | 3.301 | t |
| fy2 | 2.340 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 5.316 | t |
| fy2 | 5.317 | t |
| fy2 | 5.318 | t |
| fy2 | 5.322 | t |
| fy2 | 3.304 | t |
| fy2 | 3.305 | t |
| fy2 | 3.378 | t |
| fy2 | 3.379 | t |
| fy2 | 3.380 | t |
| fy2 | 3.381 | t |
| fy2 | 3.382 | t |
| fy2 | 3.383 | t |
| fy2 | 3.384 | t |
| fy2 | 3.385 | t |
| fy2 | 3.386 | t |
| fy2 | 3.387 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 3.388 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.389 | t |
| fy2 | 3.390 | t |
| fy2 | 3.391 | t |
| fy2 | 3.392 | t |
| fy2 | 3.393 | t |
| fy2 | 3.394 | t |
| fy2 | 3.395 | t |
| fy2 | 3.396 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 3.397 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 3.398 | t |
| fy2 | 3.399 | t |
| fy2 | 5.323 | t |
| fy2 | 5.366 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 5.367 | t |
| fy2 | 5.368 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.326 | t |
| fy2 | 4.327 | t |
| fy2 | 4.366 | t |
| fy2 | 4.367 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 4.507 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.508 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.509 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.510 | t |
| fy2 | 4.511 | t |
| fy2 | 4.329 | t |
| fy2 | 4.330 | t |
| fy2 | 4.331 | t |
| fy2 | 5.335 | t |
| fy2 | 5.336 | t |
| fy2 | 4.349 | t |
| fy2 | 4.350 | t |
| fy2 | 4.351 | t |
| fy2 | 4.352 | t |
| fy2 | 4.353 | t |
| fy2 | GY25-FY2-FOTO-04 | t |
| fy2 | 4.500 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.501 | t |
| fy2 | 4.502 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.503 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.504 | t |
| fy2 | 4.505 | t |
| fy2 | 4.506 | t |
| fy2 | 4.447 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.448 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.449 | t |
| fy2 | 4.496 | t |
| fy2 | 4.497 | t |
| fy2 | 4.499 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.368 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.369 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.370 | t |
| fy2 | 4.371 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.372 | t |
| fy2 | 4.373 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.375 | t |
| fy2 | 4.376 | t |
| fy2 | 4.377 | t |
| fy2 | 4.378 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.379 | t |
| fy2 | 4.380 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 4.381 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.382 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.384 | t |
| fy2 | 4.385 | t |
| fy2 | 4.390 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.398 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelDelar.4.t, spelIntro, t |
| fy2 | 4.413 | t |
| fy2 | GY25-FY2-EXP-02 | t |
| fy2 | 2.488 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.489 | t |
| fy2 | 2.490 | t |
| fy2 | 2.492 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 2.493 | t |
| fy2 | 2.497 | t |
| fy2 | 2.498 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 2.499 | t |
| fy2 | 2.505 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelDelar.3.t, spelIntro, t |
| fy2 | 2.506 | t |
| fy2 | 4.355 | t |
| fy2 | 4.356 | t |
| fy2 | 4.357 | t |
| fy2 | 4.358 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.359 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.360 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.361 | t |
| fy2 | 4.362 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.363 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.364 | t |
| fy2 | 4.365 | t |
| fy2 | 4.478 | t |
| fy2 | 4.479 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.480 | t |
| fy2 | 4.481 | t |
| fy2 | 4.482 | t |
| fy2 | 4.483 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.484 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.485 | t |
| fy2 | 4.486 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.487 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.488 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.489 | spelDelar.0.t, spelDelar.1.t, spelIntro, t |
| fy2 | 4.490 | t |
| fy2 | 4.491 | t |
| fy2 | 4.492 | t |
| fy2 | 4.493 | t |
| fy2 | 4.494 | spelDelar.0.t, spelDelar.1.t, spelDelar.2.t, spelIntro, t |
| fy2 | 4.495 | t |
