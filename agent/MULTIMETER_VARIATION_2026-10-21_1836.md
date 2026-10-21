# Multimeter: valfri placering och åtta nya kretsuppgifter

Fellogg 2026-10-21 18:36, fy1 #8.553, samt användarens följdönskemål om fler lämpliga alternativ och nya varierade kretsar.

## Rapport och kommentarsförslag

**#8.553 – önskemålet genomfört.** Inget svarsfel före ändringen: amperemetern ska fortfarande sitta i serie vid P för att mäta hela strömmen. Det nya felalternativet ersätter ett tidigare parallellalternativ. Det preciserar P/Q/R, så det inte kan tolkas som det korrekta påståendet att valfri punkt på den gemensamma huvudledningen fungerar.

**Kommentar:** Alternativet ”Det spelar ingen roll: bryt vid P, Q eller R” finns nu med. Facit förklarar att P mäter hela strömmen, medan Q och R mäter var sin grenström.

## Samtliga manuellt granskade och konstruerade uppgifter

Befintliga: 8.542, 8.543, 8.545, 8.548, 8.550, 8.551, 8.552, 8.553, 8.561, 8.564. Nya: 8.566, 8.567, 8.568, 8.569, 8.570, 8.571, 8.572, 8.573. Totalt 18 uppgifter inom denna avgränsade innehållsgranskning. Hela områdets 44 kort är dessutom tekniskt kontrollerade i webbläsaren; det är inte ytterligare en full manuell innehållsgranskning av de övriga korten.

## Åtgärdade befintliga uppgifter

| Fy1 ID | Åtgärd |
|---|---|
| 8.542 | P mäter totalström, Q lampan L1 och R lampan L2. Nytt felalternativ om valfri punkt, med förklaring. |
| 8.545 | R mäter L2, Q L1 och P summan. Nytt felalternativ om valfri punkt, med förklaring. |
| 8.552 | P mäter strömmen genom R0 till båda grenarna. R mäter endast R2. Nytt felalternativ om valfri punkt. |
| 8.553 | Önskat alternativ: ”Det spelar ingen roll: bryt vid P, Q eller R.” Kommentar och facit förklarar att bara P mäter hela strömmen. |

Endast `alternativ` och `s` har ändrats i dessa fyra objekt. Figuren, den korrekta placeringen, nivå 2, miniräknare tillåten och GeoGebra av är bevarade.

## Nya uppgifter

| Fy1 ID | Innehåll och korrekt svar |
|---|---|
| 8.566 | Lampa och motor i serie. Brytpunkterna P/Q/R är likvärdiga för strömmätning; ”det spelar ingen roll” är rätt. Nivå 1. |
| 8.567 | Lampa och motor i olika grenar. Motorström mäts vid R; valfri punkt P/Q/R är fel. Nivå 2. |
| 8.568 | Parallellspänning: A–B, C–D och E–F är samma två noder och ger samma spänning. ”Det spelar ingen roll” är rätt för just dessa tre punktpar. Nivå 2. |
| 8.569 | Tre seriemotstånd runt kretsen. Spänningen över R2 och R3 tillsammans mäts B–D. Valfria två punkter är fel. Nivå 2. |
| 8.570 | Lampa gemensamt före två resistansgrenar. Totalström kan mätas vid P före förgrening eller S efter sammanslagning, men inte i valfri gren. Nivå 2. |
| 8.571 | Fyra kopplingsscheman med olika fel: V över båda motstånden, V i serie, V över R2 och A över R2. Bild C är rätt. Nivå 2. |
| 8.572 | Motorgrenen har en öppen brytare. Då är totalströmmen vid P lika med lampströmmen vid Q, medan R ger 0 A. Nivå 3. |
| 8.573 | Två multimetrar: amperemeter i serie vid P och voltmeter mellan A och B över R. C–D mäter hela seriekretsens spänning. Nivå 3. |

Varje uppgift har en egen SVG, fullständig fråga, egen ledtråd, kort förklarande facit och kommentarer till alla alternativ. Åtta olika scenarier: serie, motorgren, likvärdiga spänningspar, flera seriemotstånd, huvudledning/återledning, fyra bildalternativ, öppen gren och två mätare. Alla är självrättande med ett korrekt alternativ. Inga nya delkort hänvisar till tidigare uppgifter.

## Granskad – inget fel

| Fy1 ID | Motivering / kommentarsförslag |
|---|---|
| 8.543 | Granskad – inget fel: A–B mäter lampans spänning. B–C ligger på samma ledning. Den goda befintliga uppgiften behålls. |
| 8.548 | Granskad – inget fel: Rätt uttag och strömområde med fel seriepunkt P finns redan som distraktor; Q är L1-grenen. |
| 8.550 | Granskad – inget fel: B–C omsluter R2, medan B–F är samma nod och A–C omsluter båda seriemotstånden. |
| 8.551 | Granskad – inget fel: Båda seriemotståndens spänning mäts mellan A och C. Annat delspänningspar är inte likvärdigt. |
| 8.561 | Granskad – inget fel: B och F är samma elektriska nod; svaret 0 V är korrekt. |
| 8.564 | Granskad – inget fel: Rätt 400 mA-läge förekommer med fel parallellkoppling; i serie är rätt. 6/300 A = 20 mA. |

**Kvar att utreda:** inga inom denna avgränsning.

## Principer som kontrollerats

- Minst fem jämförelser till #8.553: 8.542, 8.545, 8.548, 8.552 och 8.564. Tre fick samma slags rimliga felalternativ, två hade redan alternativa placeringar som prövar rätt strömväg. Spänningsjämförelser 8.543/8.550/8.551/8.561 skyddar skillnaden mellan samma nod, delspänning och totalspänning.
- **”Det spelar ingen roll” kan vara rätt.** I 8.566 finns ingen förgrening. I 8.568 är det bara de uttryckligt angivna tre punktparen som är likvärdiga. En voltmeter mellan *vilka punkter som helst* skulle inte vara korrekt. De två rätta fallen motverkar att elever lär sig att alltid välja bort formuleringen.
- **Det kan också vara fel.** För P/Q/R i olika strömgrenar är det inte likvärdigt. Parallellgrenarna kan ha lika stora strömmar men huvudledningens ström är ändå summan; facit påstår därför inte att alla grenströmmar alltid är olika.
- **Före och efter:** 8.570 ger samma totalström vid P och S. 8.572 har ingen motorström när brytaren är öppen, så P och Q ger lampans ström medan R ger noll.
- **Nivå:** en ny nivå 1, fem på nivå 2 och två på nivå 3. De svårare kräver villkorad strömfördelning respektive två oberoende mätarkopplingar. Nivå bedöms efter resonemanget, inte ordmängd eller miniräknare.
- **Verktyg:** miniräknare är tillåten i alla granskade fysikkort. GeoGebra behövs inte för begrepp och kopplingsval och är av. Inga standardkonstanter eller lösningsformler ges i frågorna.
- **Figurer:** positiva/negativa anslutningar, knutpunkter, komponenter och mätpunkter stämmer med alternativen. R2 i 8.569/8.573 är vertikalt ritat. Den öppna brytaren i 8.572 har ett synligt avbrott. I 8.571 följer Bild C med sin voltmeter även när knappordningen blandas.
- **Ordning:** de fyra gamla uppgifternas korrekta alternativ och grundposition bevaras. Nya alternativ placeras så att råbankens fördelning förblir balanserad. Konsumenten blandar vid visning enligt FP84.

## Verifiering

- Befintliga multimetertester, riktade inkopplingstester, FP84/fellogg 17:41 och SVG-bredd passerar. Inkopplingstestet har nu 44 kort och konkreta skydd för både sanna och falska ”det spelar ingen roll”-alternativ.
- Kunskapsgymmets riktiga alternativknappar: **334 svarskontroller, 88 vyer, 44 kort på 390/1280 px**. Alla rätta alternativ, varje felalternativ och ofullständiga flerval prövade. Inga JavaScript-fel, KaTeX-fel, sidöverflöden eller klippta SVG-etiketter.
- De åtta nya figurerna är även manuellt granskade i renderad bild. Validatorn reagerade först på en normaliserad textlikhet mellan 8.551 och 8.569. 8.569 förtydligades utifrån sitt faktiska innehåll: tre motstånd, mätning över två av dem. Slutlig validator: ERROR 1577, WARNING 227 och INFO 1452 före och efter. Inga nya fynd. Kvarvarande äldre fynd i banken ingår inte i denna omgång.
- Uppgiftslabbet är master; `uppgifter.js` jämförs med konsumentens original före identisk synk. Bara bank, tester, cacheversioner, felmönster och granskningsloggar ingår i leveransen.
- Orelaterade prototyper och `__pycache__` lämnas orörda. Git-pushen ändrar inte rapportstatus i Supabase och skickar inte kommentarer till eleverna.
