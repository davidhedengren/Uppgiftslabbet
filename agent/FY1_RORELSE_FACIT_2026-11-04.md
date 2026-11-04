# Fy1 kapitel 3 (Rörelse): facit enligt facitmallen (från 2026-11-04)

Användaren vill att faciten runt ”Rörelse med konstant acceleration” ska vara
enhetliga. Exemplet var 3.437, ett s-t-diagramkort som bara visas i
Uppgiftslabbet och som hade den gamla mallen. Arbetet fortsätter därför i
övriga områden i kapitel 3 med samma format som `konstacc`, se
`agent/FACITMALL.md` och `agent/FY1_KONSTACC_FACIT_2026-11-04.md`.

## Inventering 2026-11-04 (alla uppgifter, även `spel:false`)

| Område | Uppgifter | Följde mallen före |
|---|---|---|
| konstacc | 135 | 135 |
| st_diagram | 54 (22 bara i UL) | 0 |
| acceleration | 48 | 0 |
| vt_diagram | 68 | 0 |
| at_diagram | 51 | 0 |
| vektorer | 166 | 0 |

## Arbetssätt

- Facit skrivs för hand per uppgift i ett byggskript. Rubrikerna namnger formeln:
  ”Hastigheten är grafens lutning: \(v=\Delta s/\Delta t\)”, ”Momentanhastigheten
  är tangentens lutning”, ”Medelhastighet”, ”Medelfart”, ”Konstant hastighet:
  \(s=s_0+vt\)” och ”Vågrät graf: \(\Delta s=0\Rightarrow v=0\)”.
- Avlästa punkter står i ett eget steg innan formeln används.
- Figurer i gamla facit, till exempel ritade tangenter och diagram som eleven ska
  rita, återanvänds oförändrade i rätt steg.
- Uppgifter med flera delfrågor i samma kort får `facit-del` med a), b) …
- Svarsraderna kontrolleras automatiskt mot `rättSvar` och `tolerans`.
- Kurvorna i figurerna har räknats om från SVG-koordinaterna
  (`kurvdata.js` i sessionens scratchpad). Facitvärdena är kontrollerade mot
  dem, till exempel 3.437 \(x=2t+t^3/12\) och 3.439 \(x=4\sin(\pi t/4)\).
- Regressionstest: `tools/fysik1-rorelse-facit-2026-11-04.test.js` (listan `FÄRDIGA`).

## Omgång 1: st_diagram (54 uppgifter, 25 delfacit)

Inga räknefel hittades, och inga `rättSvar`, frågetexter eller toleranser är
ändrade. Delfacit i 3.13 d, 3.36 b och 3.138 c avslöjar inte svaret på en senare del.
Faciten är renderade i mobilbredd utan KaTeX-fel eller för breda formler.

## Omgång 2: acceleration (48 uppgifter, 70 delfacit)

- Formelrubriker: ”Hastighetsformeln: \(v=v_0+at\)”, ”Acceleration: \(a=\Delta v/\Delta t\)”,
  ”Medelacceleration”, ”Retardation: \(b=|\Delta v|/\Delta t\)” och ”Gör om till m/s”.
  Tecken och positiv riktning står i ett eget steg, ”Givet med tecken”.
- 3.360 (omkörning) löses grafiskt med två kurvor, och lösningsformeln står som
  alternativ. `geogebra: true`.
- 3.207: det tidsvägda medelvärdet visas som formel.
- Inga räknefel. Alla 48 svar är omräknade, och inga `rättSvar` eller frågetexter är ändrade.
