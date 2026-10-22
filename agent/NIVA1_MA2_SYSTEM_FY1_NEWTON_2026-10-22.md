# Nivå 1-påfyllnad: Ma2 ekvationssystem och Fy1 Newtons lagar – 2026-10-22

Påfyllnaden följer målet om 50–100 varierade kort på nivå 1 per område (se `CLAUDE.md`). Här valdes områdena med minst antal kort.

## Ma2 1.900–1.992 (93 kort)

Ekvationssystem hade 0–7 kort på nivå 1 per område. Området ingår i nationella provet i Ma2c den 11 december.

| Område | Före | Efter | Innehåll |
|---|---|---|---|
| substitutionsmetoden | 0 | 18 | y redan utlöst, x eller y känt, ekvationen efter substitution, parentes vid substitution, välja och lösa ut variabel, parameter ur känd lösning |
| additionsmetoden | 0 | 18 | addera eller subtrahera direkt, vad summan eller differensen blir, välja multiplikator (−2 respektive 2), variablerna a och b, hitta felet, negativ lösning |
| linjara_ekvationssystem | 5 | 20 | kontrollera lösning (ja och nej), vilken punkt, välja system till en text, ingen eller oändligt många lösningar, åldrar, rektangel, apelsin och banan |
| ekvationssystem_tillampningar | 1 | 19 | välja och tolka system, kaffe och bulle, pennor och sudd, glass, taxa, gym, saft, lådor, hotell, rep, kulor, arbetstimmar, abonnemang (graf) |
| ekvationssystem_tre_obekanta | 0 | 14 | trappstegsform, kontrollera lösning, tre lika stora tal, bestäm bara z, fruktkorg, antal ekvationer. Kursen är 2c, enligt testet från 2026-10-18 |
| grafisk_losning_ekvationssystem | 7 | 17 | skärning i olika kvadranter, lodrät och vågrät linje, parallella linjer, värdetabell, välja rätt par av tre linjer, kontrollera en avläsning |

- **Kontroll:** sympy kontrollerar varje system när korten byggs.
- **Figurer:** linjeetiketterna står bredvid linjerna, till höger om branta linjer. Axelsiffrorna har vit bakgrund och ritas sist.
- **Omformuleringar:** validatorn hittade nio kort med samma textmall (”Lös ekvationssystemet.”) som befintliga kort, och de är omformulerade.

## Fy1 4.800–4.836 (37 kort)

| Område | Före | Efter | Innehåll |
|---|---|---|---|
| normalkraft | 6 | 25 | bok, dator, katt, bil och astronaut på månen; riktning och ramp (fyra pilar); hiss med konstant fart, med acceleration uppåt och nedåt, vid inbromsning och i fritt fall; vågens utslag; massa ur normalkraften; bok mot vägg |
| newton3 | 7 | 25 | låda, spark, satellit, boxare, dragkamp, studsboll; raket, att gå, fluga mot vindruta, båt, astronaut, skateboard mot vägg; kraft och motkraft verkar på olika föremål och är av samma slag; välja motkraft i figur |

- **Kapitel 4-testet:** de nya numeriska korten är tillagda i `tools/fysik1-kapitel4.test.js`, och facit räknas om oberoende med g = 9,82.
- **Formattest:** `tools/fysik1-niva1-newton-2026-10-22.test.js`.
- **Granskning:** validatorn ger inga nya fynd och SVG-granskningen 0 fynd.
