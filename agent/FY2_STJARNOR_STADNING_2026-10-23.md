# Fy2 kap 5: städning av stjärnkort – felrapport 2026-10-23 10:33

Lärarens önskemål: stjärnuppgifterna såg nästan likadana ut och innehöll mycket som finns i formelsamlingen. De skulle bli tydligare, och liknande uppgifter skulle letas upp. Två tillägg under arbetet: begreppet ”bolometrisk” används inte, och enheten heter AU, inte AE.

## Rapporterna

| Kort | Åtgärd |
|---|---|
| 5.361 a | Omskrivet. Bellatrix (M = −2,8, 22 000 K): luminositet och radie i solenheter. Inga formelsamlingsvärden i texten. |
| 5.360 a | Omskrivet. Alkaid: luminositet i W ur radie och temperatur, därefter absolut magnitud. Bara stjärnans data står i texten. |
| 5.324 | HR-diagram med verkliga stjärnor tillagt. |
| 5.314 | HR-diagram med områdena markerade (solen pekas inte ut, eftersom det är svaret). |
| 5.323 | Nivå 3 i stället för 2. Ledtråden förklarar att samma temperatur ger L ∝ R². |
| 2.498 b | Frågan lyder nu ”Hur lång ska pendeln vara för att få perioden 1,0 s på månen? (Svara i m.)”. Periodformlerna är borttagna ur texten och alla delar har svarsinstruktion. |
| Ma1 0.1121 | Ingen ändring. Facit och rättning är prövade i webbläsaren: alla negativa par med a − b = 6 godtas i flera skrivsätt. Omvänd ordning, (−8; −2), underkänns korrekt eftersom den ger −6. Rapporten saknar kommentar och beror troligen på ett elevfel. |

## Liknande kort

- **5.356–5.368 skrivs om.** Alla inleddes med samma block av formelsamlingsvärden (σ, R☉, P☉ och formeln P = P☉·10^(−0,4M + 1,932)), och flera var i praktiken kopior av äldre kort:
  - Procyon i både 5.365 och 5.39;
  - Betelgeuse i både 5.366 och 5.40;
  - Gamma Comae i både 5.368 och 5.42;
  - Spica i både 5.361 och 5.33;
  - Deneb i både 5.362 och 5.34;
  - samma röda dvärg i 5.357 och 5.31;
  - samma radie och temperatur i 5.363 och 5.37.

  De har nu egna stjärnor och korta texter: Altair, Wolf 359, Canopus, Alkaid, Bellatrix, Aldebaran, Vega, Antares, Sirius och Hamal. Delkorten har svarsinstruktion och mellanresultat.
- **5.30–5.43, 5.54 och 5.376:** solens magnitud, temperatur, luminositet och radie är borttagna ur texten. Det är också ”Använd Stefan–Boltzmanns lag”. Villkoret om magnituder är kortat till ”Magnituderna gäller all strålning från stjärnan.”
- **Toleranser:** svar som beror på solens värden godtas med alla vanliga formelsamlingsvärden: M☉ 4,74 eller 4,83, T☉ 5 772, 5 778 eller 5 800 K och L☉ 3,828–3,85·10²⁶ W. Testet kontrollerar alla kombinationer.
- **Exoplaneter och kosmologi:**
  - 11 självrättade kort rättas nu automatiskt med tal, flerval eller delkort;
  - omkring 35 kort fick träningsnivå;
  - solradie, solmassa, jordradie och Jupiters massa är borttagna ur texten;
  - Hubblekonstanten 70 står kvar som valt modellvärde;
  - Hubblekort som var nästan identiska (5.332 var en exakt kopia av 5.316) fick egna sammanhang: Virgohopen, Komahopen och spektrallinjer;
  - svarsinstruktioner är tillagda.
- **”Bolometrisk”** är borttaget överallt. Det fanns bara kvar i facit till 5.40 och 5.43.
- **AU:** enheten heter AU i alla kort i kapitel 5. Mina tidigare kort hade AE, och det är ändrat. I Kunskapsgymmet är AU nu en egen enhet, och AE finns kvar som alias.

## Verifiering

- **Test:** `tools/fy2-stjarnor-stadning-2026-10-23.test.js` kontrollerar:
  - att inga formelsamlingsvärden, ingen ”bolometrisk” och ingen ”AE” finns kvar;
  - att inga självrättade kort finns och att alla kort har nivå;
  - att de nya stjärnorna inte är dubbletter;
  - att facit räknas om och att toleranserna klarar alla formelsamlingskombinationer.
- **Validator:** inga nya fynd. Antalet ERROR minskade från 1518 till 1516.
- **SVG-granskningen:** 0 fynd för de nya HR-diagrammen och de ändrade figurerna. 5.6 och 5.14 har kvar äldre varningar i figurer som inte är ändrade.
- **Konflikt:** en annan session ändrade `uppgifter2.js` under arbetet. Alla steg var skriptade och kördes om på den nya versionen.
