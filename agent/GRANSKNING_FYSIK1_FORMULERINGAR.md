# Fysik 1: formuleringar, facit och rapporterade fel

Granskad 2026-10-08. Master: Uppgiftslabbet. De två ändrade bankerna är synkade byte för byte till Kunskapsgymmet. Fysikändringarna godkändes för commit och push av användaren 2026-10-08. Den separat godkända Ma2-geometrin är pushad i båda repona (`ced7d7b`, `67f4114`).

## Omfattning och metod

Inventerat hela Fysik 1-banken: 3681 uppgifter och 5 847 faktiska träningskort, varav 2498 på träningsnivå 1–2. Sökningen gick kapitelvis genom långa kort, gemensamma inledningar, hänvisningar, modelljargong, ovidkommande givna värden och otydliga frågor. Fördjupad innehållsgranskning av arbete/effekt, rörelsemängd/kollisioner och tryck/vätsketryck.

Ändrat 155 fysikuppgifter i kapitel 2–9. Frågetexten ändras i 223 faktiskt visade kort, varav 188 på nivå 1–2. Dessa enklare kort har sammanlagt 43 % mindre löptext (figurer och HTML räknas inte). Alla kort ändras inte: korta och entydiga formuleringar behålls. Detta är en formulerings- och facitgranskning av de berörda uppgifterna, inte en ny matematisk verifiering av alla avancerade fysiklösningar.

Fysikens uppgifts-ID:n, rättSvar, toleranser, poäng, träningsnivåer och övrig bedömningsmetadata är oförändrade. Mellanresultat i fristående kort ges med tillräcklig precision och kontrolleras mot befintliga svar/toleranser. Nödvändiga fysikaliska villkor, teckenriktningar och nollnivåer behålls. Befintliga figurer följer med berörda delkort.

## Felrapporter

| Bank / uppgift | Åtgärd | Verifiering |
|---|---|---|
| fy1 5.133 a | Endast bilen 1500 kg, släpet 800 kg och farten 25 m/s visas. Motoreffekt och bromssträcka hör till separata kort. Facit skiljer konstant fart från inbromsning. | p = (1500 + 800) · 25 = 57 500 kg·m/s. |
| fy1 5.575 a | Tydlig fråga efter luftens och däckens motståndskraft. Del a får fart och nyttig effekt; senare kort får egna givna data. Kortare facit förklarar kraftbalansen. | F = 120/4 = 30 N; senare effekter 213,30 W respektive 173,93 W. |
| fy1 6.506 d | Anger klotform, last 7,70 ton och att hölje, korg och nät tillsammans väger 196 kg. | r = (3 · 7896 / (4π · (1,29 − 0,179)))^(1/3) ≈ 11,93 m. |
| mato2 2.562, spår 2c | Tydlig ordning: största värdet först, x sedan. Båda tillåter exakta svar. Numeriskt svarsformat och lokal parser gör pi/4 robust även utan algebrafilen. | Maxvärde √2 vid x = π/4. pi/4 och π/4 godkänns med och utan Nerdamer; pi/3 och felaktiga parenteser underkänns. |

Den rapporterade avvisningen av pi/4 kunde inte reproduceras när algebrafilen var laddad. Facit är matematiskt korrekt; orsaken till den enskilda rapporten är därför inte säkert fastställd. Åtgärden skyddar mot utebliven extern algebrafil och minskar risken att svaret skrivs i fel fält.

## Återkommande förbättringar

- Arbete och effekt: kort om medeleffekt får arbete och tid direkt. Facit visar P = W/t utan att räkna om en osynlig tidigare del. Nyttig och tillförd effekt skiljs åt.
- Rörelsemängd och impuls: relevant massa, hastighet eller impuls visas separat. Rättat felplacerade nämnare i impulssamband i 5.44, 5.125, 5.130 och 5.164.
- Tryck: övertryck förklaras som tryckskillnad jämfört med ytan/luften. Kolv-, area- och gaskort får bara de givna data som används.
- Krafter: dubblerade ritinstruktioner kortas, kroppen som studeras anges före frågorna. Standardvillkor om trissor tas bort från biluppgifter.
- Värme: varje steg får bara relevant värmekapacitet eller smältvärme. Kortets svarsenhet matchar rättaren.
- El och kärnfysik: mellanresultat gör senare kort självständiga. Rättat kvadreringen av radien i 8.461 och synliga TeX-klamrar i atommassor.
- Reporutiner: konkreta regler för korta, självständiga fysikkort på nivå 1–2 tillagda i masterreglerna och båda CLAUDE.md.

## Exakta matematiska svar

Utöver 2.562 har åtta liknande mato2-uppgifter fått numeriskt svarsformat för exakta tal: 1.672, 2.560, 2.571, 2.580, 2.582, 3.519, 3.520 och 3.521. Förtydligat svarens ordning i 2.571 och 2.582 samt den tillåtna noggrannheten i 1.672. Inga matematiska rättSvar eller toleranser ändras.

Kunskapsgymmets rättare använder den befintliga kalkylatorns parser om Nerdamer saknas. Självrättningen kräver slutparenteser och använder radianer, oberoende av kalkylatorns gradläge. Naturlig logaritm och tiologaritm mappas rätt. Kalkylatorns befintliga gradläge, Ans och automatiska slutparentes påverkas inte. Ingen eval används. BANK_VERSION är höjd till 2026-10-08-fy1-formuleringar.

## Kontroller

- Master: 58 innehålls-, geometri-, deluppgifts-, formatterings- och skyddstester godkända. SVG-verktygets 47 tester godkända med molnmiljöns Chromium-wrapper.
- Kunskapsgymmet: 50 tester godkända, inklusive nya regressioner för de tre fysikrapporterna, värmekortens svarsenheter och exakta talsvar utan Nerdamer.
- Bankvalidator före/efter: fy1 0 ERROR, 8 WARNING, 655 INFO; mato2 0 ERROR, 14 WARNING, 57 INFO. Inga nya fynd i jämförbara kontroller.
- Appens egen kvFacit-kontroll: samtliga 2498 nivå 1–2-kort och alla 374 kort i de ändrade uppgifterna godkänner sina lagrade svar med/utan enhet. Kontrollen verifierar rättaren, inte ensam fysikens riktighet.
- Chromium i båda apparna: 758 matematikfält med 1908 renderade formler i de ändrade fysikuppgifterna, utan KaTeX-fel eller JavaScript-fel.
- Faktisk träningsvy visuellt kontrollerad på 390 px och 1280 px för 5.133 a, 5.575 a, 6.506 d och 7.36 c.
- Giltiga bankfiler, bevarade ID:n och bedömningsmetadata, inga nya tomma stycken, byte-identisk synk och git diff --check.

## Ändringslogg per fysikuppgift

| ID | Område | Ändrade fält | Motivering |
|---|---|---|---|
| 2.260 | matnogg | t | Tagit bort överflödiga tidsvärden och dubblerat villkor; jämförelsen gäller fortfarande relativ osäkerhet. |
| 3.73 | konstacc | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.11 | moment | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.53 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.57 | friktion | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.63 | fjadrar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.74 | gravitation | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.136 | newton1 | t | Samlat systemavgränsning och villkor före tre tydliga frågor; borttaget dubblerade ritinstruktioner och modelljargong. |
| 4.143 | newton1 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.147 | newton1 | t | Samlat systemavgränsning och villkor före tre tydliga frågor; borttaget dubblerade ritinstruktioner och modelljargong. |
| 4.151 | blandat_kraft | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.160 | blandat_kraft | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.169 | blandat_kraft | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.173 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.197 | newton2 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.198 | newton1 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.200 | newton1 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.207 | normalkraft | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.220 | moment | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.223 | normalkraft | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.237 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.257 | newton1 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.261 | newton3 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.264 | friktion | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.265 | newton2 | t | Kortat dubblerade kraft- och ritinstruktioner; kropp, rörelse och nödvändiga antaganden står före frågorna. |
| 4.527 | friktion | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.648 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.650 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.653 | newton2 | spelDelar, spelIntro, t | Tagit bort ovidkommande standardvillkor om snören och trissor i biluppgift. |
| 4.656 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.660 | newton2 | spelDelar, spelIntro, t | Tagit bort ovidkommande standardvillkor om snören och trissor i biluppgift. |
| 4.661 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.667 | newton2 | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.4 | arbete | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.9 | effekt | spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.11 | arbete | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.20 | arbete | s, spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Facit förklarar det centrala sambandet före beräkningen; egna delkortsfacit visar endast den aktuella delens svar. |
| 5.23 | arbete | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.24 | rorelseenergi | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.30 | effekt | spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.42 | effekt | spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.43 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.44 | rorelsemangd | s | Rättat medelkraftens formel: hela kontakttiden Δt ligger i nämnaren. |
| 5.261 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.71 | arbete | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.73 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.75 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.264 | effekt | s, spelDelar | Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Facit förklarar det centrala sambandet före beräkningen; egna delkortsfacit visar endast den aktuella delens svar. |
| 5.267 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.82 | rorelsemangd | s, spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Facit förklarar det centrala sambandet före beräkningen; egna delkortsfacit visar endast den aktuella delens svar. |
| 5.97 | blandat_energi | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.108 | blandat_energi | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.125 | blandat_energi | s, spelDelar | Rättat medelkraftens formel: hela kontakttiden Δt ligger i nämnaren. |
| 5.130 | blandat_energi | s | Rättat medelkraftens formel: hela kontakttiden Δt ligger i nämnaren. |
| 5.132 | blandat_energi | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.133 | blandat_energi | s, spelDelar, spelIntro, t | Felrapport: del a får endast massa och fart. Motstånd vid konstant fart skiljs tydligt från inbromsning; facit förklarar metodvalet. |
| 5.138 | rorelseenergi | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.147 | effekt | s, spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Rättat felplacerade enheter och nämnare i två facitformler. Varje del får kort förklaring av den beräknade storheten. |
| 5.148 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.160 | kollisioner | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.161 | rorelsemangd | s, spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Facit förklarar det centrala sambandet före beräkningen; egna delkortsfacit visar endast den aktuella delens svar. |
| 5.162 | rorelsemangd | s, spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. Delkortet har endast relevant information och får nödvändigt mellanresultat i sin egen fråga. Facit förklarar det centrala sambandet före beräkningen; egna delkortsfacit visar endast den aktuella delens svar. |
| 5.164 | kollisioner | s | Rättat medelkraftens formel: hela kontakttiden Δt ligger i nämnaren. |
| 6.7 | tryck | t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. |
| 6.9 | vatsketryck | t | U-rörsfrågan kortas; lika tryck på samma nivå och varför lufttrycket försvinner förklaras i facit. |
| 6.150 | vatsketryck | t | U-rörsfrågan kortas; lika tryck på samma nivå och varför lufttrycket försvinner förklaras i facit. |
| 6.17 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.23 | tryck | spelDelar, spelIntro, t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. |
| 6.151 | vatsketryck | t | U-rörsfrågan kortas; lika tryck på samma nivå och varför lufttrycket försvinner förklaras i facit. |
| 6.42 | tryck | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.152 | vatsketryck | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.46 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.52 | vatsketryck | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.257 | vatsketryck | t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. |
| 6.262 | vatsketryck | t | U-rörsfrågan kortas; lika tryck på samma nivå och varför lufttrycket försvinner förklaras i facit. |
| 6.73 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.74 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.76 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.87 | gaslagen | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.95 | tryck | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.109 | vatsketryck | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.118 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.119 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.125 | gaslagen | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.6 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.16 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.22 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.25 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.26 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.102 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.36 | varme | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.40 | varme | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.42 | varme | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.45 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.310 | moment | t | Ersatt svårt formulerad lodlinjefråga med samma konkreta jämförelse av stabilitet. Svarsalternativ och korrekt svar oförändrade. |
| 5.176 | effekt | t | Kortare inledning; nödvändiga tal och fysikaliska villkor bevarade. |
| 8.436 | kretsar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 7.197 | fasandring | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.402 | kopplingar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.403 | kopplingar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.445 | kopplingar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.446 | kopplingar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.461 | kopplingar | s, spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. Rättat felaktig exponent: hela radien ska kvadreras i tvärsnittsarean. |
| 8.462 | kopplingar | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 3.218 | acceleration | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.220 | gaslagen | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 3.387 | konstacc | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 2.162 | densitet | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.562 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.563 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.566 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.567 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.568 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.569 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.570 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.571 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.572 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.573 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.574 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.575 | effekt | s, spelDelar, spelIntro, t | Felrapport: alla tre frågor får entydig situation och självständiga givna värden. Ersatt lång generell härledning med uppgiftsspecifika förklaringar. |
| 5.576 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.577 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.578 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.579 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.580 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.582 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.583 | effekt | s, spelDelar | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.584 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.585 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.586 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 5.587 | effekt | s | Kortat återkommande generell effekthärledning. Kraftens betydelse och skillnaden mellan momentan effekt och medeleffekt bevaras. |
| 9.408 | fission | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.409 | fission | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.410 | fission | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.411 | fission | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.373 | straldoser | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.385 | straldoser | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.422 | tryck | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.458 | vatsketryck | spelDelar, t | Vätsketryck definieras uttryckligen som övertryck; atmosfärstryck ska inte läggas till. |
| 6.470 | arkimedes | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 6.506 | arkimedes | s, spelDelar, spelIntro, t | Felrapport: formen och vad massan 196 kg omfattar är uttryckligt. Varje kort visar endast relevant gasdensitet; facit förklarar bärförmåga, volym och radie. |
| 4.625 | lutande_plan | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 4.635 | lutande_plan | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.415 | fusion | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.416 | fusion | spelDelar, spelIntro, t | Rättat synliga TeX-klamrar i atommassor utanför matematikmiljö. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.417 | fusion | spelDelar, spelIntro, t | Rättat synliga TeX-klamrar i atommassor utanför matematikmiljö. Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.418 | fusion | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 9.419 | fusion | spelDelar, spelIntro, t | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. Rättat synliga TeX-klamrar i atommassor utanför matematikmiljö. |
| 9.420 | fusion | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.501 | arbete | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.423 | kollisioner | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.426 | kollisioner | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 5.447 | kollisioner | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.485 | coulomb | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |
| 8.486 | coulomb | spelDelar | Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt. |

## Fortsatt granskning, omgång 2

Ytterligare sju uppgifter har förtydligats efter första pushen. Svar, toleranser och nivåer bevaras. Nya givna mellanresultat har räknats om och kontrollerats mot svarstoleransen.

- **4.593**: Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt.
- **4.574**: Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt.
- **4.632**: Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt.
- **5.110**: Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt.
- **5.209**: Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt.
- **4.630**: Delkort visar bara relevanta givna data; referensriktning, villkor, avrundning och befintliga figurer bevaras. Facit anpassat när ett mellanresultat ges direkt.
- **3.60**: Flyttat nollnivå och rörelsevillkor före tabell och frågor; undvikit upprepning och förtydligat lägesaxeln.

Omgång 2 verifierad: 26 mastertester och 18 delkortstester godkända. Chromium renderar 2013 formler i samtliga 162 ändrade uppgifter utan fel. Alla 2498 nivå 1–2-kort och de 391 korten i de ändrade uppgifterna godkänner facitsvaren med och utan enhet. Bankerna är byte-identiska; inga ändrade rättSvar, toleranser eller nivåer. Omgången pushas enligt användarens godkännande.
