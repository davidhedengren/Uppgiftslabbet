# Fy2 tidsdilatation: hela området 10 november

## Omfattning

Alla 34 ID:n granskade och facit omskrivna:
6.1–6.8, 6.10, 6.23, 6.25, 6.26, 6.55, 6.59–6.61, 6.301–6.308, 6.320–6.329.
6.55:s två explicita delkort har var sitt komplett facit. Totalt 36 kontrollerade lösningsvyer. Författarkälla: `tools/fy2-tidsdilatation-facit-2026-11-10.py`.

Varje facit har en numrerad steglista med specifika rubriker, formel/regeln där den används, insättning och en svarsrad. Begreppsfrågor förklarar den relevanta principen. Inga ”Tänk så här” eller ”Kontroll och insikt” från allmänna mallar finns kvar. Formler radbryts efter faktisk mobilkontroll.

## Vad som förklaras

- 6.1/6.2/6.301/6.320–6.322: fartkvot, megaprefix och dimensionslös gammafaktor; inget slentrianmässigt råd om egentid när frågan inte söker en tid.
- 6.3/6.4/6.7/6.61/6.307: farten isoleras från Lorentzfaktorn/tidskvoten. Ingen gissad fart eller gömt algebraiskt steg.
- 6.5/6.8/6.23/6.26/6.59/6.60/6.323/6.324/6.328/6.329: klockan ombord följer händelserna och mäter egentiden; jordtiden är längre. När gamma redan ges, som i 6.328, behövs ingen fartberäkning.
- 6.6/6.25: laboratoriets eller jordens tid är given; vilotiden/egentiden blir kortare. Riktningen i omräkningen förklaras uttryckligen.
- 6.10: händelserna sker på samma plats på jorden, så jordtiden är egentiden; de båda rymdskeppens tider jämförs via denna gemensamma tid.
- 6.302: överlevnadsandelen använder halveringstiden 1,56 μs och myonens egentid. Klassisk andel cirka 2·10⁻¹⁰ motsvarar cirka 2·10⁻⁸ %, inte samma tal uttryckt i procent. 6.324 söker i stället medellivslängden: ingen halveringslag ska användas där.
- 6.303/6.327: beskriver hur man läser den redan givna kurvan och visar sedan formelkontroll.
- 6.304/6.325: sömn/blinkningar sker på samma plats i astronautens system, som därför mäter egentiden.
- 6.305: jordens åtta år gäller redan hela tur- och returresan. Resenärens tid 6,4 år jämförs med åtta för att få åldersskillnaden 1,6 år.
- 6.306: liten fartkvot ger gamma nära 1. Den konkreta storleksordningen för en veckas flygning förklaras.
- 6.308/6.326: nämnaren närmar sig noll från positiv sida och gamma växer obegränsat; ingen ändlig maxfaktor.
- 6.55 a: härleder tidsförlusten t−τ ≈ t(γ−1) i approximationen för liten fart. Gravitationsbidraget och markklockans rörelse förblir uttryckligen uteslutna enligt uppgiften.
- 6.55 b: räknar signalavståndsfelet c·δt ≈ 2,2 km. Detta är inte ensamt en exakt positionsavvikelse för en riktig GPS-mottagare. Ledtråden handlade tidigare om att identifiera egentid, vilket inte hjälpte på b; den frågar nu hur långt signalen färdas under tidsfelet.

14 huvudledtrådar och båda GPS-delarnas ledtrådar är specifikt omskrivna där den tidigare texten inte passade frågan. Jämförelser omfattar fler än fem gamma-/tidskort inom samma område.

## Granskad – inget matematiskt fel

Alla 34 uppgifters svar stämmer med självständigt uppställda samband, inom äldre lagrade avrundningar. Samtliga `rättSvar`, enheter, toleranser, nivåer, poäng, alternativ och frågor bevaras. Faciten ändras av pedagogiska skäl även när svaret var korrekt. Inga felrapporter eller rapportstatusar behandlas i denna omgång.

Miniräknare tillåts på alla 34. GeoGebra behövs inte: gamma, isolerbar fart/tid och givna grafavläsningar kräver inget digitalt verktyg. Befintliga figurer och konstantskillnader bevaras. Inga nya figurer tillförs när det inte förbättrar den aktuella förklaringen.

## Verifiering

- 62 faktiska rättningsförsök i Kunskapsgymmet: 52 numeriska plus 10 flervalsförsök med korrekta och felaktiga val. Testet använder renderTraining/checkAnswer/kollaAlt, utan riktig XP-/databasskrivning.
- 72 lösningsvyer per app, för 34 huvuduppgifter och två GPS-delar vid 390/1280 px. KaTeX, bildladdning och formelbredd kontrollerade.
- Tre nya regressionstester: struktur för hela området, självständigt beräknade numeriska samband och GPS-tolkningen. Sju befintliga relativitets-/figurtester passerar.
- Strukturell diff kontrolleras: endast de 34 avsedda objekten och fälten s, ledtrad, miniräknare, geogebra och relevanta GPS-delfält. Uppgiftslabbet är master; konsumentkopian jämförd före synk och identisk efteråt.

Detta slutför tidsdilatation. Längdkontraktion var färdig i föregående omgång. Relativistisk energi samt övriga områden och banker återstår i den övergripande genomgången.
