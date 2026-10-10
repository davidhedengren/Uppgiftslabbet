# Fysik 1 – aktuell granskningsstatus 2026-10-10

Banken har 3 738 uppgifter. Den här fortsättningen omfattar 151 manuellt granskade uppgifter: fission 26, fusion 19, kärnreaktioner 47 och enheter 59. Alla ID, åtgärdade uppgifter, granskad–inget fel och föreslagna kommentarer finns i respektive JSON/Markdown.

- [Fission](FISSION_FYSIK1_2026-10-10.md)
- [Fusion](FUSION_FYSIK1_2026-10-10.md)
- [Kärnreaktioner](KARNREAKTIONER_FYSIK1_2026-10-10.md)
- [Enheter](ENHETER_FYSIK1_2026-10-10.md)

Kapitel 9:s första manuella genomgång är klar: 450 av 450 uppgifter. Tidigare delområden och samtliga ID finns i KARNFYSIK_GRANSKNINGSSTATUS.json. Kapitel 8:s första genomgång finns i ELEKTRICITET_GRANSKNINGSSTATUS.json. Hela bankens andra manuella genomgång är inte slutmarkerad. Äldre områdesgranskningar av kapitel 2–7 finns i agent/; deras täckning varierar och får inte ersättas med ett påstående att varje uppgift nyligen räknats igenom.

Den senaste tekniska helbankskontrollen omfattar 5 271 aktiva kort och 14 979 rättningsfall, utan fel. Både lärar- och elevappens samtliga 3 738 uppgifter har matematikvisningskontrollerats utan KaTeX-fel. Mastertester 289/289 och konsumenttester 106/106. Exakta siffror finns i FYSIK1_HELBANK_TEKNISK_2026-10-10.json. Kontrollen testar facitsvar, svar med enheter och avsiktliga felsvar; den bevisar inte att den lagrade fysikmodellen alltid är korrekt.

Nästa manuella fortsättning: kapitel 2:s mätning/noggrannhet (60 uppgifter), medelhastighet (76) och densitet (170), jämför med tidigare granskning och regressionstester. Enheter har nu genomlästs igen med tydligt ID-register. Därefter fortsatta manuella varv i övriga kapitel. Kör relevanta fysikmodeller, faktiska kort och mobil-/datorvisning; registrera minst fem liknande uppgifter per felmönster.

Bevara särskilt egna givna mellanvärden på fristående kort; lärarfacit använder ofta full precision och kan därför ha ett annat svar. Atommassetolerans får inte dölja massdefekten. Två sökta värden kräver två tydliga svarsfält. Alfaenergi är inte hela sönderfallsenergin: dotterkärnan har rekylenergi. SVG-ändringar ska granskas visuellt, inte bara med heuristik. Se FP20–FP23 i FELMONSTER_OCH_BESLUT.md.

Inga Supabase-rapporter har avslutats eller elevkommentarer skickats under denna fortsättning.
