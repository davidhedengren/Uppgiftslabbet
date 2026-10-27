# Fy1: svarsinstruktioner bara där de behövs (2026-10-26)

Användarbeslut: ta bara bort enhet och avrundning där det är underförstått. Annars kan toleransen vara ganska generös. Den som svarar med 2 fler eller färre värdesiffror ska ändå få rätt.

## Regler som tillämpats på uppgifter.js

**Avrundningskrav**

- Formuleringar som ”(Svara med tre värdesiffror.)”, ”med två decimaler”, ”Avrunda vid behov till 1 decimal.” och ”(Svara med ett heltal.)” är borttagna.
- `svarVardesiffror` för svaret tar över. Värdet är kravets värdesiffror, eller antalet värdesiffror i facit avrundat enligt kravet.
- Appen godkänner korrekt avrundade svar med n−2 till n+2 värdesiffror (minst 1) och visar ”Rekommenderat: n värdesiffror”.
- Handkalibrerade värden skrivs aldrig över. Det gäller även null, som betyder exakt svar.
- Antal utan enhet, som ”Hur många …”, rättas exakt och får inget `svarVardesiffror`.

**Enhetsangivelser**

- ”(Svara i U.)” och ”Bestäm … i U.” är borttagna bara när U är en naturlig SI-enhet utan prefix (s, m, kg, N, J, W, Pa, V, A, Ω, Hz, K, °C, m/s, m/s², kg/m³ och liknande).
- U måste också vara svarets `svarEnhet`.
- Inget givet värde i texten får ha en annan enhet av samma slag. Till exempel står ”(Svara i m.)” kvar när tjockleken är given i µm, och ”i m/s” står kvar när farten är given i km/h.
- Enheter som kJ, mN, cm, kWh, MeV, % och timmar står kvar.

**Specialformuleringar lämnas orörda**

197 formuleringar, till exempel ”Svara i hela N”, ”med tecken”, ”Svara med ett positivt värde i J” och ”Avrunda till hela gram”.

## Omfattning

| Mått | Antal |
|---|---|
| Kort | 4 444 |
| Ändrade kort | 2 522 |
| Borttagna avrundningskrav | 6 633 |
| Borttagna enhetsangivelser | 6 176 |
| Enhetsangivelser kvar | 1 829 |

Skripten finns i scratchpad: `rensa_svarsinstr.js`, med appens `tolkaEnhet`, och `lagg_in_kort.py`.

Två slumpurval på sammanlagt 34 kort är genomlästa. Mekaniska fel som hittades och rättades i skriptet:

- ”… och svara.”
- ”(Svara i m,.)”
- ”s,.”
- ”?.”

Inga kort med heltalsfacit förlorade avrundningskravet utan att få `svarVardesiffror`.

## Kunskapsgymmet

`fysikVardesiffrorRatt` jämför nu på facits egen precision när eleven skriver fler siffror än det avrundade facit. Med facit 1,43 godkänns både 1,426 och 1,4257. Heltalsfacit behandlas som tidigare, eftersom de kan vara exakta.

Provat i appen:

| Kort | Godkänt | Underkänt |
|---|---|---|
| 4.447 | 3,3; 3,32; 3,317; 3,3 m/s² | 3,4 |
| 6.300 | 7856; 7,86 kPa; 7900 | 7800 |
| 2.324 | 800 | 799 |
| 5.209 b | 433 | 432 |

Delkorten 3.155 c, 6.445 b och 3.368 a är också provade.

## Tester

- Nytt test: `tools/fy1-svarsinstruktioner-2026-10-26.test.js`.
- 25 äldre testfiler krävde ”(Svara …” eller precisionstext i frågan. De godtar nu en angiven enhet (`svarEnhet`) eller `svarVardesiffror` i stället. Där de krävde precisionstexten kontrollerar de nu värdet i `svarVardesiffror`.

## Tillägg 2026-10-27: Fy2 (uppgifter2.js)

Användaren: ”gör samma sak där”. Samma skript och regler användes.

Fy2 hade redan få avrundningskrav. De flesta Fy2-kort har `svarVardesiffror` sedan tidigare, och inga handkalibrerade värden skrevs över.

| Mått | Antal |
|---|---|
| Kort | 1 765 |
| Ändrade kort | 173 |
| Borttagna avrundningskrav | 28 |
| Borttagna enhetsangivelser | 174 |
| Enhetsangivelser kvar | 211 (bland annat nm, pc, km/s, procent, µT och år) |

”(Svara med ett tal.)”, 111 gånger, står kvar. Det talar om att svaret ska vara ett tal och inte text, vilket gör det till ett svarsformat och inte ett avrundningskrav. Specialformuleringar som ”Svara i miljoner år”, ”Svara med maximum eller minimum” och ”Svara i varv per sekund” är orörda.

Urval genomläst (16 kort). Provat i appen:

| Kort | Godkänt | Underkänt |
|---|---|---|
| 3.556 | 2,5·10⁻⁹; 2,5 ns; 3·10⁻⁹ | 2,6·10⁻⁹ |
| 3.472 | 10; 10 A | 11 |
| 3.529 (antal varv) | 100 | 99 |
| 2.608 | 0,68; 0,7 | 0,69 |
| 4.519 | 3,3·10⁻¹⁰; 3,31·10⁻¹⁰ | 3,4·10⁻¹⁰ |

Sex Fy2-testfiler godtar nu en angiven enhet (`svarEnhet`) i stället för en svarsinstruktion i frågan. Antalsfrågor (”Hur många …”) godtas utan heltalsinstruktion. Hela testsviten är grön (1 060 tester).
