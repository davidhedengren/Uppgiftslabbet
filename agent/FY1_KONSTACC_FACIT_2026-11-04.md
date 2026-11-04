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

## Omgång 2: Möte och ikapp + Konstant acceleration (11 uppgifter, 14 delfacit)

3.39, 3.169, 3.170, 3.176, 3.177, 3.371, 3.389, 3.390, 3.391, 3.446, 3.448.

- Mötesuppgifter ställer upp båda lägena med formel (konstant fart \(s=s_0+vt\),
  sträckformeln med startläge) och sätter dem lika.
- Andragradsekvationerna (3.39 b, 3.169 c, 3.176, 3.177, 3.389 a–c, 3.391 a,
  3.448) löses grafiskt med **två kurvor i samma diagram**, där mötet är
  skärningspunkten. Faktorisering eller lösningsformeln står som alternativ.
  `geogebra: true`. Testet `fysik1-acceleration-2026-10-21` tillåter nu
  GeoGebra för 3.448.
- 3.389 c: grafen visar båda skärningarna, och facit förklarar varför den
  första är omkörningen (bilen bromsar och blir senare omkörd av cyklisten).
- 3.391 a: steget "Har den bakre bilen kört 43 m efter 3,0 s?" visar varför
  krocken sker efter att den främre bilen stannat.
- 3.170: \(4{,}91t^2\) tar ut varandra. Facit förklarar att båda bollarna faller
  lika snabbt, så ekvationen blir linjär (ingen graf).

## Sparade övningsblad i Uppgiftslabbet

Sparade prov och övningsblad lagrar en ögonblicksbild av uppgifterna. Därför
når nya facit inte äldre blad av sig själva. Sedan 2026-11-04 (UL 6ebc154)
visar bladet "N uppgifter i bladet har nytt facit i banken" med knappen
**Uppdatera facit**. Den byter bara facit i uppgifter som inte redigerats i
bladet och går via skyddet för sparade dokument. Läraren väljer sedan Spara.
