# Fy1 konstacc: tydligare facit med formler och grafisk lösning (2026-11-04)

Användarbeslut: facit i kapitlet ”Rörelse med konstant acceleration” ska vara
tydligare och ha fler steg. Det ska **alltid stå vilken formel som används**.
Andragradsekvationer löses grafiskt i kursen, och facit ska då alltid visa en
grafisk lösning. Regeln står i `CLAUDE.md` (”Fysikfacit: formeln ska alltid stå”).

## Format

Numrerad steglista (`facit-v2 facit-stegvis`, `facit-steglista`) med specifika rubriker:

1. **Givet och sökt.** Storheter med tecken och enheter, en per rad, vald
   positiv riktning och nollnivå, omvandlingar (km/h → m/s, cm → m).
2. **Formelsteg.** Rubriken namnger och visar formeln, t.ex. ”Hastighetsformeln: \(v=v_0+at\)”,
   ”Sträckformeln: \(s=v_0t+\tfrac{at^2}{2}\)”, ”Tidlösa formeln: \(v^2=v_0^2+2as\)”
   eller ”Sträcka med medelhastighet: \(s=\tfrac{v_0+v}{2}\cdot t\)”. En rad
   motiverar valet (vilken storhet som saknas).
3. **Lös ut och sätt in** med enheter.
4. **Andragradsekvation:** ”Lös ekvationen grafiskt” med SVG-graf av \(s(t)\)
   eller \(h(t)\), den vågräta linjen eller t-axeln, markerad skärningspunkt och
   avläst värde. Därefter ”Alternativ: lösningsformeln”. `geogebra: true`.
5. Svarsrad.

Långa rader bryts för mobil: givna värden står på egna rader (aligned) och
⇒/⇔ ger ny rad. Huvudfacit för uppdelade uppgifter är delarnas facit efter
varandra (`facit-del` med a), b) …).

## Omgång 1 (pilot): 13 uppgifter, 29 delfacit

Tidlösa formeln: 3.48, 3.64, 3.74, 3.88, 3.93, 3.124, 3.152, 3.370, 3.377, 3.379.
Andragradsekvationer: 3.118, 3.171, 3.399.

Särskilda ändringar:

- **3.74 a och 3.171 a:** tiden löses nu med sträckformeln och grafiskt. Det
  tidigare delfacitet räknade först ut slutfarten, som är svaret på b.
- **3.88 b:** svarsraden ”257 None” är rättad till ”257”.
- **3.399 a/b:** grafen visar naturligt båda skärningarna. Bara den efterfrågade
  är markerad och avläst.
- **3.74, 3.118, 3.171, 3.399:** `geogebra: true` (grafisk lösning).

Alla värden är omräknade i byggskriptet med asserts mot `rättSvar`, och inga
`rättSvar`, toleranser eller frågetexter är ändrade. Faciten har renderats i
Kunskapsgymmet (KaTeX, mobilbredd) och lästs.

Bygghjälp i sessionens scratchpad: `fysfacit.py` (steg, facit, helfacit,
graf, bryt), `konstacc_pilot.py` (facit per uppgift, handskrivna rubriker) och
`lagg_in_facit.py` (byter bara `s` och `geogebra` på plats).
