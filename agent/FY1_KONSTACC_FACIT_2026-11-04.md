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

## Omgång 3: Reaktions- och bromssträcka (21 uppgifter, 19 delfacit)

3.5, 3.63, 3.77, 3.81, 3.84, 3.91, 3.157, 3.159, 3.162, 3.164, 3.172, 3.185,
3.186, 3.187, 3.188, 3.189, 3.276, 3.278, 3.372, 3.376, 3.378.

- Formelrubriker som återkommer: "Konstant fart under reaktionstiden: \(s_r=v_0t_r\)",
  "Bromssträcka till stillastående (tidlösa formeln med \(v=0\)): \(s_b=\dfrac{v_0^2}{2b}\)",
  "Stoppsträcka: \(s_{\text{stopp}}=s_r+s_b\)" och för v-t-diagram
  "Accelerationen är lutningen …: \(a=\dfrac{\Delta v}{\Delta t}\)" och "Sträckan är arean under v-t-grafen".
- 3.188: andragradsekvationen i farten löses grafiskt (stoppsträckan som funktion av
  farten och linjen s = 45). `geogebra: true`.
- 3.189 är helt symbolisk (L, τ, b). Facit visar lösningsformeln steg för steg och
  förklarar varför en graf kräver givna värden.
- 3.172 behåller de delsträngar som `fysik1-prosa` kräver.
- Odelade uppgifter med flera delfrågor (3.5, 3.63, 3.157, 3.162, 3.164, 3.172) får
  ett facit per delfråga med a), b) …

## Omgång 4: Sträcka vid konstant acceleration (44 uppgifter, 98 delfacit)

Hela delmomentet, 3.4–3.388.

- Andragradsekvationer med graf: 3.383 b (\(59{,}5=23t+2t^2\)) och 3.388 b
  (tid till mittpunkten). `geogebra: true`.
- Delfacit som inte går via svaret i en senare del: 3.80 b (slutfarten med
  medelhastighet, inte via medelfarten i c), 3.369 b och 3.373 c (tidlösa
  formeln i stället för tiden från a/b).
- 3.166: medelhastigheten under en sekund är hastigheten mitt i sekunden, och
  därefter används \(a=\Delta v/\Delta t\) och hastighetsformeln.
- 3.385: tidlösa formeln ger \(v_A=\pm\sqrt{21}\). Facit förklarar varför den
  positiva roten ger kortast tid.
- Symboliska uppgifter (3.254, 3.255) visar arean under v-t-grafen och
  medelhastighetens formel steg för steg.
- Testet `fysik1-konstacc-facit-2026-11-04` kontrollerar nu hela delmomenten
  reaktions- och bromssträcka samt sträcka vid konstant acceleration.

## Omgång 5: Fritt fall och lodrät kast (46 uppgifter, 72 delfacit)

Därmed har alla 135 uppgifter i `konstacc` nya facit.

- Grafisk lösning: 3.17 och 3.407 b (villkoret \((T-1)^2=k\,T^2\) med två kurvor),
  3.27 b–c, 3.30 b, 3.79 a (två bollars höjd), 3.123 (två skärningar, båda tolkade),
  3.400 b och 3.404 a. `geogebra: true`.
- 3.120 c: svarsraden "1,66 None" är rättad till "1,66".
- 3.30 b löser tiden med sträckformeln och grafen, utan att gå via farten i a.
- Tyngdaccelerationens tecken har en egen rubrik, "Tyngdacceleration med tecken:
  \(a=\pm g\)", som förklarar riktningsvalet.

## Facitmall för hela Uppgiftslabbet

Användaren vill att formatet ska vara standard i hela Uppgiftslabbet. Mallen
står i `agent/FACITMALL.md` och refereras från `CLAUDE.md` (läsordningen och
avsnittet "Facitmall") och från `INNEHALLSREGLER.md` 3.6. Den ersätter den
äldre regeln om löpande fysiklösning utan steglista.
