# AI: minimax och beskärning på E- och C-nivå, 11 november 2026

Användarens önskemål: fler minimax- och beskärningsuppgifter på E–C-nivå.

## Nivåbeslut

Fullständig alfa–beta-spårning är fortfarande A, och de äldre
beskärningsuppgifterna 3.03–3.42 är oförändrade. Nytt tillägg i
AI_NIVAINDELNING.md: **beskärning med stöd är C**. Det betyder träd i två nivåer,
ett givet mellanvärde och ett enda beslut. **Begreppsfrågor om beskärning är E.**
Minimaxfrågor där eleven tolkar eller jämför värden är C.

## Minimax (3.50–3.55)

| ID | Innehåll | Nivåer |
|---|---|---|
| 3.50 | Stickspelet: 3 stickor, ta 1 eller 2, +1/−1 som vinst och förlust; A = −1, rot −1, ”MIN vinner vid bästa spel” | E, E, C |
| 3.51 | Fyra drag för MAX: hur många MIN-noder är minst 5, rot 6, drag B | E |
| 3.52 | Ett löv byter värde: rot 5; L1 = 8 ger drag A och rot 6 | E |
| 3.53 | Läs spelträdet: vilken spelare väljer i A, antal drag i roten, rot 3 | E |
| 3.54 | Två lika bra drag: A = 4; båda dragen garanterar 4 | E, C |
| 3.55 | MIN i roten, tre nivåer: D = 3, B = 5, rot 3 | E |

## Beskärning med stöd (3.56–3.61)

| ID | Innehåll | Nivåer |
|---|---|---|
| 3.56 | Vad beskärning betyder; att rotvärdet inte ändras | E, E |
| 3.57 | A = 5, B:s första löv 3: kan B bli större än 3? behövs L4? rot 5 | C, C, E |
| 3.58 | MIN i roten, A = 4, B:s första löv 6: B minst 6, L4 behövs inte, rot 4 | C, C, E |
| 3.59 | Vilket löv kan hoppas över (L4) | E, C |
| 3.60 | Samma löv i olika ordning: 1 respektive 2 av B:s löv undersöks | C, C, C |
| 3.61 | Tre MIN-noder: 4 av 6 löv behöver undersökas | E, C |

Facitrubrikerna beskriver vad som händer i steget, till exempel ”B är en MIN-nod och
blir högst 3”, i stället för ”Ja” eller ”Nej”. Samma rättelse är gjord i
teorifrågorna från förra omgången (1.56b, 1.60a/b, 2.71b). Stickspelets träd
ritas med större avstånd mellan löven, så att beteckningen C inte krockar med ett löv.

## Kontroll

Banken har nu 202 uppgifter och 536 delkort (385 E, 97 C och 54 A).
Byggskript: `tools/bygg-ai-pafyllnad6-2026-11-11.py`. Det körs före nivåskriptet.
Test: `tools/ai-pafyllnad6-2026-11-11.test.js` räknar om svaren med egen
minimax och alfa–beta och kontrollerar att de nya uppgifterna är E–C medan de
äldre beskärningsuppgifterna är A. Nivåtestet tillåter beskärning med stöd för
3.56–3.61. 84/84 AI-tester godkända. Validatorn hittar inga nya fynd. Webbläsarprov
gjort. Facit och ledtrådar har lästs igenom. Granskningen är gjord.
