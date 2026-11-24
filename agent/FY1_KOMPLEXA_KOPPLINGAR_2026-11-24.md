# Fy1: mängdträning på komplexa kopplingar, 8.740–8.781 (2026-11-24)

Användaren: ”skapa fler mängdträningsuppgifter på komplexa kopplingar i fysik 1. Här har eleverna svårt, så här behövs
många olika, varierade kretsar på olika svårighetsnivåer.”

Området `kopplingar` (”Komplexa kopplingar och effektutveckling”) hade 184 uppgifter, men bara 30 om blandade
kopplingar, och nästan inga av dem på nivå 1 eller över nivå 3. Nu finns 42 nya, var och en med en egen kretsfigur.

## Delmoment och nivåer

| Delmoment | Uppgifter |
|---|---:|
| Blandade kopplingar (befintligt): ersättningsresistans | 10 |
| Ström och spänning i blandade kopplingar (nytt): grenström, spänningsfördelning, mätare, brytare, effekt | 32 |

| Träningsnivå | Antal | Vad som tränas |
|---|---:|---|
| 1 | 10 | ett steg i en blandad krets: knutpunktsregeln, spänningslagen, samma spänning i parallella grenar, Ohms lag för en komponent, ersättning av en del |
| 2 | 13 | två steg: ersättningsresistans, totalström, grenström, en okänd resistor ur ström och spänning, kΩ och mA, vilken lampa som lyser starkast |
| 3 | 12 | hela analysen: ström eller spänning i en gren, effekt, en brytare som sluts eller kortsluter en lampa, vilken resistor som utvecklar mest effekt, en okänd resistor för given ersättningsresistans, en tvådelad uppgift |
| 4 | 5 | nästlade kopplingar, en okänd resistor ur amperemeter och batteri, voltmeterns ändring när en brytare sluts, dimensionering av en förkopplingsresistor, en lampa som går sönder |
| 5 | 2 | en okänd resistor i en nästlad gren ur voltmeterns värde, största antal parallellkopplade lampor |

Variation: 20 olika topologier (bland annat serie–parallell–serie, parallell före serie, tre grenar, gren med en egen
parallelldel, två parallellkopplingar i serie, A–B utan batteri, brytare parallellt med en lampa), lampor och resistorer,
amperemetrar och voltmetrar i olika lägen, sammanhang (leksaksbil, billampor med säkring, dockskåp, cykellampa,
värmeelement, sensorkrets, kretskort) och svarsformer (tal med enhet, kΩ, mA, antal, flerval med kommentarer, två delar).
Validatorn har inga fynd för de nya ID:na; två textmallar som var för lika skrevs om (8.755, 8.759, 8.764, 8.765, 8.775).

## Figurer

Nytt ritbibliotek `tools/kretsrit.py`: kretsen byggs av `Ser` och `Par` med resistorer, lampor, mätare, brytare och
säkring, och läggs ut automatiskt. Namnet står ovanför komponenten och värdet under, noder med tre ledningar har
prickar, och ingen ledning går förbi en komponent. Batteriet ritas på den nedre ledningen med pluspolen till vänster.
Ramen är högst cirka 420 enheter bred, så att texten blir minst cirka 11 px i ett mobilkort. SVG-granskningen har
0 fynd i de 42 figurerna.

## Facit, ledtråd och kontroll

- Facit följer FACITMALL: Givet och sökt, formeln i rubriken (för ersättningsresistans står kopplingens egen formel,
  till exempel \(R=R_1+(1/R_2+1/R_3)^{-1}\)), insättning med enheter och svarsrad. Rubrikerna är skrivna för varje uppgift.
- Ledtrådarna pekar mot nästa tanke utan att ge svaret.
- Flervalsuppgifterna (8.762, 8.763, 8.769, 8.779) har en kommentar till varje felaktigt alternativ. 8.769 är vald så
  att en parallellkopplad resistor utvecklar mest effekt, inte serieresistorn med hela strömmen.
- Svaren räknas i byggskriptet och räknas om oberoende i `tools/fysik1-komplexa-kopplingar-2026-11-24.test.js`.
- Alla facit och ledtrådar har renderats vid 390 px och lästs (inga KaTeX-fel eller överflöden).
- Självrättningen i Kunskapsgymmet är provad: 0,55 A godtas som 0,55, 0,55 A och 550 mA; 4,5 mA som 0,0045 A;
  5,0 kΩ som 5000 Ω; 13 Ω som 13,3; antalet 2 exakt. Bråksvar som 1/3 godtas inte (svarsformatet är numeriskt).
- Uppgiftstexterna har inga svarsinstruktioner (beslut 2026-11-23); enheten står bara när den inte är underförstådd
  (”i kΩ”, ”i mA”).

Byggskript: `tools/bygg-fy1-komplexa-kopplingar-2026-11-24.py`.
