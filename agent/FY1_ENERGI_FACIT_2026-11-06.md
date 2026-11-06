# Fy1 kapitel 5 (Energi): facit enligt facitmallen (från 2026-11-06)

Fortsättning på kapitel 3 och 4 (`agent/FY1_RORELSE_FACIT_2026-11-04.md`,
`agent/FY1_KRAFT_FACIT_2026-11-04.md`). Samma arbetssätt gäller:

- facit skrivs för hand per uppgift, med formeln i rubriken;
- ”Givet och sökt” används när värden måste omvandlas eller när det finns många givna värden;
- svarsraderna kontrolleras automatiskt mot `rättSvar`, `tolerans` och `svarVardesiffror`;
- faciten renderas i 380 px bredd utan KaTeX-fel eller för breda formler.

Regressionstest: `tools/fysik1-rorelse-facit-2026-11-04.test.js` (listan `FÄRDIGA`).
`tools/fysik1-prosa.test.js` undantar områdena i listan `MALL`.

## Inventering 2026-11-06 (alla uppgifter, även `spel:false`)

| Område | Uppgifter | Utan steglista före arbetet |
|---|---|---|
| arbete | 108 | 108 |
| effekt | 116 | 116 |
| rorelseenergi | 113 | 113 |
| blandat_energi | 72 | 72 |

## Omgång 1: arbete (108 uppgifter, 145 delfacit)

- Formelrubriker:
  - ”Arbete: \(W=Fs\)” (lös ut F respektive s) och ”Arbete med sned kraft: \(W=Fs\cos\alpha\)”. Med α = 180° visas tecknet för bromsande krafter och med α = 90° att en vinkelrät kraft inte gör något arbete.
  - ”Lägesenergi: \(E_p=mgh\)”, ”Lyftarbete från vila till vila: \(W=mgh\)” och ”Fjäderenergi: \(E_f=\dfrac{kx^2}{2}\)”.
  - ”Hookes lag: \(F=kx\)” och ”Friktion på vågrätt underlag: \(f=\mu mg\)”.
  - ”Höjdökning längs rampen: \(h=s\sin\alpha\)”, ”Höjdökning i en pendel: \(h=l(1-\cos\theta)\)” och ”Energiprincipen …”.
- Grafuppgifter: ”Läs av grafen” som eget steg, följt av ”Arbetet är arean under grafen”. Rubriken visar formeln för triangel, rektangel eller trapets. Avläsningarna är kontrollerade mot SVG-koordinaterna (5.38, 5.70, 5.230 och 5.232: 30, 38, 40, 30, 16 och 10 N).
- Facitfiguren i 5.58 ligger kvar i steget ”Rita grafen”.
- 4.40 och 4.345 har tre delfrågor i frågetexten, och faciten har nu också tre delar.
- 5.23 a och 5.234 har fått en uträkningsrad som leder fram till svaret.
- Inga räknefel. Alla 108 svar är omräknade. Inga `rättSvar`, toleranser eller frågetexter är ändrade.
