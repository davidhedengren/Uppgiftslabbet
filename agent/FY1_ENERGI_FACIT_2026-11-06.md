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

## Omgång 1: arbete (108 uppgifter, 104 delfacit)

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

## Omgång 2: effekt (116 uppgifter, 129 delfacit)

- Formelrubriker:
  - ”Effekt: \(P=\dfrac{W}{t}\)” och ”Energi: \(E=Pt\)”, där tiden löses ut när den söks;
  - ”Effekt vid konstant fart: \(P=Fv\)” och ”Drivkraft: \(F=\dfrac{P}{v}\)”;
  - ”Verkningsgrad: \(\eta=\dfrac{P_{\text{nyttig}}}{P_{\text{tillförd}}}\)” och motsvarande för energi;
  - ”Massa per sekund: \(\dfrac{m}{t}=\rho\cdot\dfrac{V}{t}\)” för pumpar, vattenkraft och vind;
  - enhetsbyten som egna steg: kWh, hk = 735,5 W, kcal = 4186 J och km/h;
  - backar med ”Tyngdkraftens komposant längs backen” och ”Newtons andra lag”.
- Andragradsekvationer löses grafiskt enligt FACITMALL 4. Uppgifterna 5.582 b och 5.585 har en SVG-graf med avläst skärningspunkt, och lösningsformeln står som alternativ. Båda har nu `geogebra: true`.
- Svar i hela tal, alltså antal steg, lyft, verk och personer samt lastmassan i 5.272, slutar med en rad som visar det avrundade värdet och åt vilket håll det avrundas.
- GY25-FY1-EN-02 har två delfrågor i frågetexten, och facit har nu också två delar.
- Inga räknefel. Alla 116 svar är omräknade. Inga `rättSvar`, toleranser eller frågetexter är ändrade.
- `tools/fysik1-effekt-variation-2026-10-21.test.js` kräver nu steglistan i stället för att förbjuda den.
- 5.575 a: svarsraden visar 30,0 N (tre värdesiffror), som `tools/felrapporter-2026-10-11-1749.test.js` kräver.
