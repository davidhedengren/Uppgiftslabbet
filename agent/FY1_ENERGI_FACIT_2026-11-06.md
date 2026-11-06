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
- Andragradsekvationer löses grafiskt enligt FACITMALL 4. Uppgifterna 5.582 b och 5.585 har en SVG-graf med avläst skärningspunkt, och pq-formeln står som alternativ, efter division till normalform. Båda har nu `geogebra: true`. Första versionen hade abc-formeln, vilket ändrades samma dag efter lärarens beslut att pq-formeln ska användas i alla kurser.
- Svar i hela tal, alltså antal steg, lyft, verk och personer samt lastmassan i 5.272, slutar med en rad som visar det avrundade värdet och åt vilket håll det avrundas.
- GY25-FY1-EN-02 har två delfrågor i frågetexten, och facit har nu också två delar.
- Inga räknefel. Alla 116 svar är omräknade. Inga `rättSvar`, toleranser eller frågetexter är ändrade.
- `tools/fysik1-effekt-variation-2026-10-21.test.js` kräver nu steglistan i stället för att förbjuda den.
- 5.575 a: svarsraden visar 30,0 N (tre värdesiffror), som `tools/felrapporter-2026-10-11-1749.test.js` kräver.

## Omgång 3: rorelseenergi (113 uppgifter, 167 delfacit)

- Formelrubriker:
  - ”Rörelseenergi: \(E_k=\dfrac{mv^2}{2}\)” och samma formel med \(v=\sqrt{2E_k/m}\) utlöst;
  - ”Energiprincipen utan förluster: \(v=\sqrt{2gh}\)”, \(v^2=v_0^2+2gh\) och \(h=\dfrac{v_0^2}{2g}\);
  - ”Mekanisk energi bevaras: \(E_k+E_p=\text{konstant}\)”;
  - ”Arbete och rörelseenergi: \(W_{\text{netto}}=\Delta E_k\)” och ”Bromsarbete: \(F\cdot s=\Delta E_k\)”;
  - ”Energiprincipen med förluster: \(E_{\text{start}}=E_{\text{slut}}+E_{\text{förlust}}\)”;
  - lutande plan med friktion \(\mu mg\cos\alpha\), och ”Energiprincipen från start till stopp: \(F\cdot d=mg(h+d)\)” för inbromsningar efter fall.
- Avläsningen i 5.143 (20 N till 4 m, sedan 10 N till 10 m) är kontrollerad mot SVG-koordinaterna.
- 5.36 c och 5.68 har fått en slutrad med talet, som `tools/fysik1-rorelseenergi.test.js` kräver.
- Inga räknefel. Alla 113 svar är omräknade. Inga `rättSvar`, toleranser eller frågetexter är ändrade.

## Omgång 4: blandat_energi (72 uppgifter, 68 delfacit), kapitel 5 klart

- Området blandar energi med rörelsemängd och impuls. Formelrubriker utöver de ovan:
  - ”Rörelsemängd: \(p=mv\)”, ”Rörelsemängden bevaras: \(m_1u_1+m_2u_2=(m_1+m_2)v\)” och ”Impuls: \(F\Delta t=\Delta p\)”;
  - elastisk stöt med \(v_2=\dfrac{2m_1u}{m_1+m_2}\) och energikvoten \(\dfrac{4m_1m_2}{(m_1+m_2)^2}\);
  - ”Jämn retardation: \(t=\dfrac{s}{v_{\text{medel}}}\)”, raketformeln och centripetalkraft i pendeln (5.128).
- Andragradsekvationer löses grafiskt enligt FACITMALL 4, med SVG-graf och `geogebra: true`:
  - 5.134 (\(9{,}6V^2-24V=0\), fysisk rot V = 2,5 m/s);
  - 5.172 (bungyhopp, \(31x^2-638{,}3x-11\,489{,}4=0\), med pq-formeln som alternativ);
  - 5.247 (\(0{,}84x^2-0{,}40x=0\)).
- Frågetexternas delfrågor styr facitdelarna. 5.90, 5.107, 5.121 och 5.248 har två delfrågor, och 5.247 en.
- Ändrade äldre tester:
  - `tools/fysik1-blandat-energi.test.js` kräver nu steglistan.
  - Svarsraderna i 5.95 a och 5.120 a skrivs som 9427 J och 10 720 N, eftersom testet läser talet i svarsraden.
- Inga räknefel. Alla 72 svar är omräknade. Inga `rättSvar`, toleranser eller frågetexter är ändrade.
- **Kapitel 5 är klart:** alla 409 uppgifter i arbete, effekt, rorelseenergi och blandat_energi följer facitmallen och ingår i FÄRDIGA.

## pq-formeln (användarbeslut 2026-11-06)

Läraren: ”Vi använder PQ-formeln i alla kurser, inte ABC, ändra det i alla facit.” FACITMALL och CLAUDE.md säger nu ”Alternativ: pq-formeln” efter division till normalform. abc-formeln används aldrig. Ändringen i övriga banker loggas i `agent/PQ_FORMELN_2026-11-06.md`.
