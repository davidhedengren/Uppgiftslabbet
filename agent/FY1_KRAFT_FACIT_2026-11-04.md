# Fy1 kapitel 4 (Kraft och rörelse): facit enligt facitmallen (från 2026-11-04)

Fortsättning på kapitel 3 (`agent/FY1_RORELSE_FACIT_2026-11-04.md`). Samma arbetssätt
gäller: handskrivna formelrubriker, avlästa värden i ett eget steg, återanvända figurer,
automatisk kontroll av svarsraderna mot `rättSvar`, `tolerans` och `svarVardesiffror`
(±2 värdesiffror), och kurvor kontrollerade mot figurernas koordinater. Testet är
`tools/fysik1-rorelse-facit-2026-11-04.test.js` (listan `FÄRDIGA`).

## Inventering 2026-11-04 (alla uppgifter, även `spel:false`)

| Område | Uppgifter | Bara i UL |
|---|---|---|
| newton1 | 95 | 35 |
| newton2 | 159 | 24 |
| newton3 | 53 | 8 |
| tyngdkraft | 46 | 2 |
| normalkraft | 59 | 14 |
| gravitation | 53 | 8 |
| fjadrar | 55 | 16 |
| friktion | 96 | 18 |
| lutande_plan | 103 | 21 |
| moment | 88 | 29 |
| blandat_kraft | 53 | 17 |

Ingen av de 860 uppgifterna följde mallen före arbetet.

## Omgång 1: tyngdkraft (46 uppgifter, 14 delfacit)

- Formelrubriker: ”Tyngdkraft: \(F_g=mg\)”, ”lös ut massan: \(m=F_g/g\)”, ”lös ut
  tyngdaccelerationen”, ”Massan är densamma överallt” och ”Jämvikt: \(F_{\text{upp}}=F_g\)”.
- Inga räknefel.
- Frågetexter med genererade fraser är rättade: 4.187 och 4.208 (”Föremålet flyttas” om en
  astronaut), 4.190 och 4.503 (”Föremålet befinner sig på Mars”) samt 4.470, där
  ”(Svara i kN.)” stod två gånger.

## Omgång 2: newton1 (95 uppgifter, 133 delfacit)

- Formelrubriker: ”Newtons första lag: \(\sum\vec F=\vec 0\Leftrightarrow\vec v\) konstant”,
  ”Jämvikt: \(\sum F_x=0\) och \(\sum F_y=0\)”, ”Lodrät/vågrät jämvikt”, ”Frilägg kroppen”,
  ”Ideal trissa: samma spännkraft i hela snöret”, ”Komposanter”, ”Pythagoras sats”,
  ”Riktning: \(\tan\alpha\)” följt av ett steg som bestämmer kvadranten, och ”Vektoraddition komposantvis”.
- Friläggningsfigurer från de gamla faciten ligger kvar i steget ”Frilägg kroppen”, och den
  grafiska kontrollen i 3.302–3.308 ligger kvar som eget steg.
- Inga räknefel. Alla 95 svar är omräknade, och inga `rättSvar` eller frågetexter är ändrade.

## Omgång 3: newton2 (159 uppgifter, 336 delfacit)

- Formelrubriker: ”Newtons andra lag: \(F_{\text{res}}=ma\)” (lös ut a respektive m),
  ”Kraftresultant med tecken”, ”Hela systemet: \(F_{\text{res}}=m_{\text{tot}}a\)”,
  friläggning av en del av systemet (snörkraft och kontaktkraft), ”Friktion: \(F_{\text{fr}}=\mu F_N\)”,
  ”Tyngdkraftens komposant längs planet”, ”Ideal trissa” samt rörelseformlerna
  (hastighetsformeln, tidlösa formeln, sträckformeln) där kraft kombineras med kinematik.
- Delkort med egen inledning, som ”En vikt på 25 kg accelererar nedåt med 0,598 m/s²”,
  får facit som bara använder värdena i det egna kortet.
- 4.704: frågetexten innehöll ”Hur stor blir accelerationen om” inklistrat mitt i
  deluppgifterna a–c, och delkort a och b upprepade frasen. Det är rättat.
- Inga räknefel. Alla 159 svar är omräknade, bland annat alla trissystem, kopplingar och
  system med två rörelsefaser (4.650, 4.656, 4.659, 4.662, 4.664, 4.667, 4.670).
