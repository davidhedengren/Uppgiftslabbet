# Tunna områden – omgång 1 (2026-10-21)

Användaren bad om en genomgång av vilka områden som har få uppgifter, och om fler varierade uppgifter i dem, gärna med figurer.

## Kartläggning

Alla sju banker har räknats per område (`omr`), delmoment, kursspår och träningsnivå. Totalt finns 367 områden. 95 flaggades med färre än 20 uppgifter eller ett delmoment under 8. Många av dem har bara små restdelmoment på 1–3 uppgifter. Det är en taggningsfråga och inte brist på uppgifter.

De 15 verkligt tunna områdena, med färre än 15 uppgifter, var:

| Bank | Område | Före | Omgång 1 |
|---|---|---:|---|
| fy2 | induktion_ledare | 6 | **+8 → 14** |
| fy2 | stjarnornas_utveckling | 7 | **+8 → 15** |
| ma2 | tabeller_diagram | 8 | – (fylldes på 2026-10-13) |
| mato1 | derivata_exponential | 10 | **+8 → 18** |
| mato2 | asinx_bcosx | 11 | **+8 → 19** |
| mato2 | sinusformad_kurva | 11 | **+8 → 19** |
| fy1 | fyra_krafterna | 12 | **+8 → 20** |
| fy2 | de_broglie | 12 | återstår |
| mato2 | tan_kurvan | 12 | återstår |
| mato2 | andragradsekv_komplexa | 12 | återstår |
| fy1 | medicinska_metoder | 13 | återstår |
| fy2 | vaxelstrom_spole_kondensator | 13 | återstår |
| mato1 | derivatans_definition | 13 | återstår |
| mato2 | forskjutna_kurvor | 13 | återstår |
| mato1 | faktorisera_polynom | 14 | återstår |

Övriga iakttagelser, inte åtgärdade:
- ma2 `mer_om_andragradsekvationer` har bara 2 uppgifter i ett av spåren.
- ma1 `potensregler` har 7 i ett spår.
- Många fy2-uppgifter saknar `traningsniva`, `spel` och `självrättning`. Det är orsaken till fy2-bankens 1 587 kända ERROR i validatorn.

## Nya uppgifter (48)

**Fysik 1, De fyra krafterna (9.428–9.435):**
- Flervalsuppgifter: månens bana, normalkraft, proton till neutron i solen och friktion.
- Ett stapeldiagram med logaritmisk skala över krafternas styrka.
- Beräkningar: kvoten F_e/F_g i väteatomen (2,3·10³⁹), repulsion mellan protoner på 2,0 fm (58 N) och antalet extra elektroner som behövs för att balansera gravitationen mellan två blykulor (5,4·10⁸).

**Fysik 2, Induktion i ledare (3.415–3.422):** stav på skenor, med figur, från e = Blv (nivå 1) till ström genom motstånd och nödvändig fart. Vidare flygplanets vingar i jordens magnetfält (figur), Lenz lag med strömriktning (figur), bromskraft, snett rörelse och sluthastighet vid konstant dragkraft (A).

**Fysik 2, Stjärnors utveckling (5.369–5.376):** energikällan på huvudserien, ett HR-diagram (figur), L ∝ M^3,5, huvudserietid för en röd dvärg (57 miljarder år), slutstadium utifrån Chandrasekhargränsen, neutronstjärnans densitet, Schwarzschildradien och den röda jättens radie ur Stefan–Boltzmanns lag.

**Ma3c, Derivatan av exponentialfunktioner (2.1116–2.1123):** kvoten f′/f, lutning ur graf (figur) och modell ur f′ = kf. Vidare att bestämma k, avsvalning där T′ = −0,05(T − 20) (figur), flerval, halveringstid ur sönderfallstakten och lutning −0,3, med svaret x = 2 ln 5 (A).

**Ma4, a sin x + b cos x (2.589–2.596):**
- Begreppsfråga om det största värdet.
- Vattennivå med högsta och lägsta värde.
- R sin(x + v) med exakta värden.
- Bestämma a och b ur en graf (figur).
- Ekvationslösning med valfri ordning på lösningarna.
- Mekanisk arm.
- Flerval.
- Bestämma a och b ur maximum (A).

**Ma4, Sinusformad kurva (2.597–2.604):** tre grafuppgifter (figurer), egenskaper ur max- och minimipunkter, ett pariserhjul (figur), egenskaper ur formeln, en dygnstemperaturmodell och parametrar ur villkor.

Fysikuppgifterna ger inte standardkonstanter. Svarsinstruktionen står i parentes efter frågan, och miniräknare är alltid tillåten. Matematikuppgifterna har räknarspärr där talen är enkla och det är begreppet som prövas.

## Variation och kvalitet

- **Validatorn:** fynden i de fyra bankerna är identiska före och efter. Validatorn flaggade först tre av mina uppgifter som för lika befintliga: 2.589 liknade 1.669, 2.590 liknade 1.119 och 2.599 hade samma text som 1.625. De skrevs om till en begreppsfråga, en uppgift med sammanhang och en egen formulering.
- **Facit:** alla facit är omräknade i byggskripten och i det nya testet `tools/tunna-omraden-2026-10-21.test.js`.
- **Rättningen:** testad i Kunskapsgymmets riktiga kod för alla 48 kort. Rätt svar godkändes med enhet och med den precision frågan anger, och felaktiga svar underkändes. Mängdsvaret i 2.593 kräver `svarsstruktur:"mängd"` och godtar valfri ordning, men inte samma lösning två gånger.
- **Visning:** alla kort på 375 px har inga KaTeX-fel och ingen överbredd. Korten syns i rätt spår.
- **Figurer:** 14 figurer, kontrollerade med getBBox och granskade visuellt. Text över fältsymboler har vit kontur.
