# Ma2 kap 3: revision efter lärarens granskning, etapp 1, 2026-10-25

## Lärarens synpunkter

- Många figurer var likadana och texterna nästan identiska. Exemplet var 3.185 och 3.186, med samma mallfigur oavsett mått.
- Texten ”Skiss. Mät inte i figuren.” ska inte finnas på någon uppgift.
- Vinkelmarkeringar överlappar ibland sidor. Alla figurer i kapitlet ska gås igenom och förbättras, och frågorna ska vara varierade.
- 3.72 var konstigt formulerad, och 3.106 och liknande kort också.
- Läraren gav exempeluppgifter (NP och andra) som förebilder och ville ha varianter av dem. Analysen finns i `NP_EXEMPEL_ANALYS_2026-10-25.md`.

## Gjort i etapp 1

1. **”Skiss. Mät inte i figuren.”** finns inte längre i någon bank. Texten fanns bara i Ma2: 51 kort och 90 förekomster, i frågetexter och deluppgifter.
2. **30 kort med mallfigurer har nya figurer:**
   - **Kort:** 3.08, 3.97, 3.101, 3.102, 3.110, 3.131, 3.163, 3.165, 3.185, 3.186, 3.260, 3.261, 3.262, 3.298, 3.313, 3.337, 3.338, 3.22, 3.26, 3.60, 3.148, 3.35, 3.48, 3.77, 3.81, 3.285, 3.297, 3.311, 3.150 och 3.153.
   - **Skalenliga:** sidlängderna är de angivna, och D och E ligger där delningsförhållandet säger.
   - **Beteckningar:** givna mått och den okända sträckan (”?” eller x) står utsatta. En hel sida får en måttlinje. Parallellitet markeras med pilar i stället för texten ”DE ∥ BC”.
   - **Variation:** formerna är vridna, och spetsen pekar ibland nedåt. Inga två figurer är lika.
   - **Texter:** texterna i de nästan identiska korten är formulerade olika.
   - **3.313:** var en exakt dubblett av 3.298 och fick nya tal (AD = 4, AB = 11, DE = 6, så BC = 16,5).
   - **Facit:** facit skrevs om där texten ändrades: 3.48, 3.77, 3.297, 3.311 och 3.313.
3. **13 kort i `sats_bevis` är omformulerade:**
   - **Tydligare frågor:** 3.72 handlar nu om \(n^2+n+41\), och 3.106, 3.104 och 3.40 har fått tydligare formuleringar.
   - **Dubbletter blev nya uppgifter:**
     - 3.348 blev en egen motexempeluppgift med \(2^n+1\) och numeriskt svar.
     - 3.250 blev ”vem har rätt?” med Noah och Lova.
     - 3.281 handlar om \(x^2=4x\) och \(x=4\), och 3.356 om \(x^3=8\Rightarrow x=2\).
     - 3.248 handlar om vertikalvinklar, 3.83 om rät vinkel ⇔ vinkelsumman 90°, 3.249 om romb och parallellogram, och 3.300 om tal som slutar på 0.
     - 3.329 är nu ”Lisa påstår …” med implikationen \(x\gt1\Rightarrow x\gt3\).
4. **12 varianter av lärarens exempeluppgifter (3.2162–3.2173):**

| ID | Förebild | Variant | Poäng |
|---|---|---|---|
| 3.2162 | ABM i cirkel, rät vinkel, 110° | Två radier, rät vinkel vid M och 115° vid P, så v = 40° | 1/1/0 |
| 3.2163 | AC lika lång som radien, 40° | AB lika lång som radien, 70° som distraktor, så v = 30° | 0/0/2 |
| 3.2164 | Liksidig triangel i koordinatsystem, arean i s | Regelbunden sexhörning, arean \(\frac{3\sqrt3}{2}s^2\) | 0/0/3 |
| 3.2165 | u, v och yttervinkeln 3v | Yttervinkeln 4v, så u = 3v | 1/0/0 |
| 3.2166 | Bevis av vinkelsumman i omvänd ordning | Fyrhörningens vinkelsumma, där kedjan börjar i slutsatsen | 0/1/0 |
| 3.2167 | Bubblorna med ⇒, ⇔ eller ⇐ | Sidorna 5, 12, 13 ⇒ rätvinklig | 0/1/0 |
| 3.2168 | Elin och Sanna | Omar och Ella, \(x^2=5x\) och \(x=5\) | 0/1/0 |
| 3.2169 | Huset och granen | Flaggstång, lyktstolpe och ögonhöjd, så h = 7,2 m | 0/4/0 |
| 3.2170 | Bestäm x | Rätvinkliga trianglar med gemensam vinkel, så x = 5 | 0/2/0 |
| 3.2171 | Area när höjden delar hypotenusan i 7 och 3 | Delarna 6 och 4, arean \(10\sqrt6\) | 0/0/3 |
| 3.2172 | a och b med 3x och 5x | 2x och 3x, så \(a=\frac53b\) | 0/0/2 |
| 3.2173 | AB/AQ med BP = a och PC = 3a | PC = 2a, så AB/AQ = 2/3 | 0/0/3 |

## Kontroll

- **Verktyg:** två nya verktyg byter enskilda textfält eller hela kortobjekt per ID. De klarar både kompakt och radbruten JSON. Efter varje ändring jämförs hela banken (3 332 kort) med förväntat resultat.
- **Validatorn:** 0 fynd för de ändrade och nya korten.
- **Figurgeometri:** vinkelbågarna i 3.2162, 3.2163 och 3.2165 mättes ur SVG-koordinaterna. Första versionen av 3.2165 visade u ≈ 82° och v ≈ 34°, vilket inte stämde med 4v, och rättades till v = 25°, u = 75° och yttervinkeln 100°.
- **Självrättning i Kunskapsgymmet:** rätt svar godtas i likvärdiga exakta former, till exempel 10√6, `sqrt(600)` och 4/6. Närmevärden avvisas när uppgiften kräver exakt svar. Alla flerval ger rätt och fel som väntat.
- **Test:**
  - `tools/ma2-kap3-revision-2026-10-25.test.js` ger 4/4.
  - Antalet i `ma2-problemlosning.test.js` är 66.
  - Alla Ma2-tester går igenom.

## Kvar till nästa etapp

- **Kapitlet:** genomgång av alla övriga figurer i kapitel 3 (omkring 540), med överlappande vinkelmarkeringar och etiketter, och variation i texter med nästan identiska mallar. Exempel är ”Bestäm vinklarna x och y.” på 13 randvinkelkort och ”Trianglarna är likformiga. Bestäm x.” på 6 kort.
- **Fler varianter:** av exemplen i kapitel 4 (standardavvikelse ur stapeldiagram, frekvenstabell med percentil) och kapitel 1–2 (faktorisering, symmetrilinje, raket, hage, vattenspridare, skärning, parameter). Kapitel 1–2 ska samordnas med den andra sessionen.

## Etapp 2: randvinklar och medelpunktsvinklar (`randvinkel_medelpunkt`)

**Utgångsläge**
- Serien 3.363–3.382 (20 kort) hade nästan samma figur: spetsen överst och två randvinklar från sidorna. 13 av korten hade dessutom samma text, ”Bestäm vinklarna x och y.”, och värdena fanns bara i figuren.
- Mallkorten 3.03, 3.42 och 3.132 var identiska i text och figur.
- 3.17, 3.157, 3.293 och 3.331 var nästan likadana. 3.331 hade samma tal som 3.293.

**Ändrat (33 kort)**
- **Figurer:**
  - Alla figurer är omritade med en egen cirkelmodul (`cirk`). Punkterna placeras med gradtal på cirkeln, och varje markerad vinkel mäts och jämförs med sitt värde innan figuren skapas.
  - Lägena varieras. Fria punkter söks fram så att:
    - inga etiketter korsar linjer eller överlappar varandra;
    - inga kordor går genom vinkelsektorn vid medelpunkten;
    - inga sträckor löper längs en radie;
    - punkterna ligger isär;
    - vinkelbenen inte är för korta.
  - Givna vinklar är blå, okända orange och distraktorer grå.
- **Texter:** formerna varieras:
  - sammanhang: fotografer vid en damm, park med fontän, hus runt en sjö, lampor på en ring, karusell, rund skiva;
  - felresonemang att kommentera: Lina tror att vinkeln växer närmare kordan, Kim halverar i stället för att dubbla;
  - distraktorer där alla uppgifter inte behövs (3.373, 3.374, 3.378);
  - inskriven fyrhörning med diagonaler;
  - Thales med tre punkter (3.361).
- **Facit:** varje steg har en rubrik, enligt Ma1 #1.116.
- **3.42:** delkorten var beroende av varandra (b behövde a:s svar). Nu frågar a efter medelpunktsvinkeln (124°) och b efter en annan randvinkel (62°). Kortet räknas som E 2/0/0.
- **3.331:** var en dubblett av 3.293 och har nu 154° och svaret 77°. 76° krockade med 3.2032.
- **Algebrakorten 3.376 och 3.377:** uttrycken för de smala randvinklarna står i texten och inte i figuren, eftersom långa etiketter inte får plats nära spetsen.
- **Endast ny figur:** 3.2029, 3.2134 och 3.2137. Där behålls text och facit.

**Kontroll**
- **Validator:** 0 fynd för de 33 korten.
- **Bågarna:** de har rätt storlek och sitter på vinkelbenen. Testet mäter dem ur SVG-koordinaterna.
- **Självrättning i Kunskapsgymmet:** 41 fall med rätt och fel svar, inklusive flerdelskort del för del, och alla ger väntat resultat.
- **Mobilvy:** kontrollerad för 3.378.
- **Skydd:** `tools/ma2-kap3-randvinklar-2026-10-25.test.js`.

## Etapp 3: yttervinkelsatsen (2026-10-26)

**Utgångsläge**
- 22 kort (3.127, 3.154, 3.156, 3.181, 3.182, 3.197, 3.198, 3.271, 3.274, 3.275, 3.306, 3.330 och 3.383–3.392) hade samma mallfigur. Bågarna var alltid 44°, 86° och 129° oavsett uppgiftens värden, och algebraiska etiketter korsade sidorna.
- Texterna visade ”Bestäm (x).”: avgränsarna `\(` och `\)` hade tappat sina backslash.
- Flera texter var identiska, till exempel ”Bestäm yttervinkeln (x).” på fyra kort.
- 3.383, 3.384, 3.385, 3.386 och 3.387 var märkta C men var direkta E-uppgifter på träningsnivå 1–2.

**Ändrat**
- **Ny figurmodul** (`vfig.js`) för trianglar med en förlängd sida:
  - triangeln byggs ur vinklarna, och varje båge mäts mot sitt värde;
  - läget varierar per kort (vridning och spegling);
  - etiketter placeras fria från sträckorna. Långa uttryck flyttas till utsidan av hörnet om de annars skulle hamna långt in i vinkeln.
- **Texter:**
  - sammanhang: segelbåt som svänger (3.384), tält (3.383);
  - Felix räknar i två steg (3.330);
  - beräkning utan att först räkna den tredje vinkeln (3.198);
  - begreppsformulering (3.387);
  - olika punktnamn (PQR, KLM, DEF, STU, GHI).
- **Facit:** varje steg har en rubrik. Algebrakorten har ett kontrollsteg.
- **3.181:** delningen togs först bort, men det var fel och den är återställd i etapp 4. Ett givet mellanresultat i b-frågan är tillåtet.
- **Nivåer:** 3.383–3.387 är E (1/0/0, och 2/0/0 för 3.386).
- **Ledtrådar i Ma2 kap 1–2** (1.261, 1.263, 1.271, 1.273, 1.274, 2.07, 2.22, 2.25, 2.31, 2.32, 2.33 och 2.40) hade samma fel och har fått tillbaka `\(` och `\)`. Även `\ge` i 2.31 var trasig.

**Kontroll**
- **Banken:** inga fler ”(x)” utan avgränsare i Ma2. Testet söker igenom hela banken.
- **Matf1:** har samma fel i 19 kort, i ledtrådar som 1.35, 1.102–1.109 och 1.127. Banken redigeras av en annan session och lämnas till en egen rättning.
- **Validator:** 0 fynd.
- **Självrättning:** 23 fall i Kunskapsgymmet, och alla ger väntat resultat.
- **Skydd:** `tools/ma2-kap3-yttervinkel-2026-10-26.test.js`.

### Geometriska begrepp (etapp 3b)

- **3.291:** var en dubblett av 3.212 (vad en bisektris gör). Nu visar figuren höjd, median och bisektris från samma hörn. Höjden har en markerad rät vinkel och medianen markerade lika delar, och eleven ska avgöra vilken sträcka som är bisektrisen.
- **3.303:** var en dubblett av 3.214 och 3.31 (transversal). Nu handlar kortet om tangent: en figur med tangeringspunkt och rät vinkel mot radien, och sekant och korda som distraktorer.
- **3.347:** var en dubblett av 3.215 (sidovinkel utan figur). Kortet har nu en figur med två skärande linjer och de uppmätta vinklarna 118° och 62°.
- **Övriga figurer i området:** 3.222, 6.07 och 3.2068–3.2081 är skalenliga och tydliga och behålls.
- **Kontroll:** självrättningen ger väntat resultat i Kunskapsgymmet, och testet är tillagt i `ma2-kap3-yttervinkel-2026-10-26.test.js`.

## Etapp 4: Pythagoras (2026-10-26)

**Utgångsläge**
- **Figurer som inte följde måtten:**
  - 3.142 (8 och 15), 3.310 (12 och 5), 3.624 (9 och 40) och 3.625: den långa kateten var ritad kortare än den korta.
  - 3.630 (drake): höjden 40 var ritad lägre än avståndet 30.
  - 3.632 (ramp): 0,5 m på 6 m var ritad brant.
  - 3.04: stegen hade fel proportioner och etiketter i typsnittet Courier.
  - 3.34: delsträckan 4 m var lika lång som 6 m.
  - 3.333: kateterna 6 och 8 hade fel proportioner.
- **Dubbletter:**
  - 3.240 = 3.129 (9, 12, 15) och 3.353 = 3.309 (6, 8, 10).
  - 3.302 = 3.241 (13, 5, 12), och 3.310 och 3.200 gav också svaret 12.
  - 3.632 = 3.2006 (rampen 0,5 m och 6 m).

**Ändrat (16 kort)**
- **Skalenliga figurer:** 3.04, 3.34, 3.142, 3.145, 3.187, 3.333, 3.624, 3.625 och 3.630.
- **Nya tal och sammanhang:**

  | Kort | Uppgift | Svar |
  |---|---|---|
  | 3.240 | Grind 2,0 × 1,5 m med diagonalstag | 2,5 m |
  | 3.353 | Triangeln ABC med AC = 20 mm och BC = 21 mm | 29 mm |
  | 3.302 | Längsta sidan 53 cm, kortaste 28 cm | 45 cm |
  | 3.310 | Hypotenusan 37 cm, kateten 12 cm | 35 cm |
  | 3.200 | Bordsskiva med diagonalen 2,6 m och bredden 1,0 m | 2,4 m |
  | 3.632 | Ramp till en lastkaj, 0,8 m på 9,6 m | 9,63 m |

- **Facit:** varje steg har en rubrik. 3.632 har dessutom ett rimlighetssteg.
- **3.145:** behåller sina delkort, och b får höjden 6 cm given i frågan.
- **3.181:** delningen från etapp 3 är återställd.

**Delkort**
- Sökningen efter delkort som innehåller ett tidigare delkorts svar gav 28 träffar. De flesta är avsiktliga mellanresultat som gör korten fristående, till exempel ”Med a = 5 …” och ”Modellen är m(s) = 2,25s³”. Det är tillåtet enligt principen att ge nödvändiga mellanresultat direkt.
- Det som inte får förekomma är att ett delkorts facit visar ett annat delkorts svar.

**Kontroll**
- **Figurer:** testet mäter kateternas kvot i figuren mot måtten i uppgiften.
- **Validator:** 0 fynd.
- **Självrättning:** 17 fall i Kunskapsgymmet, och alla ger väntat resultat.
- **Tester:** `ma2-niva1-geometri-2026-10-22.test.js` har uppdaterats med 3.632:s nya tal.
- **Skydd:** `tools/ma2-kap3-pythagoras-2026-10-26.test.js`.

## Etapp 5: likformighet och topptriangel (2026-10-26)

**Utgångsläge**
- **Topptriangelkort med samma triangel:**
  - 3.36, 3.69, 3.98, 3.99, 3.100, 3.162, 3.164, 3.176 och 3.323 använde samma likbenta triangel. I 3.99 och 3.259 låg D på fel ställe.
  - 3.600–3.611 använde samma liksidiga triangel (D låg rätt).
- **3.359:** var en exakt dubblett av 3.337 (AD = 4, AB = 10, AC = 15).
- **Fel skala mellan likformiga figurer:**
  - 3.43 (skala 2, ritad ungefär 1,2), 3.209, 3.335, 3.466–3.470, 3.639 och 3.642;
  - rektanglarna i 3.641 (skala 3, ritad 2).
- **Samma text:** 3.209, 3.335 och 3.466–3.470 hade texten ”Trianglarna är likformiga. Bestäm x.”.

**Ändrat (34 kort)**
- **Topptriangel:** 23 figurer är ritade med `topp()` från etapp 1, med varierad form och vridning. Spetsen pekar ibland nedåt eller åt sidan, och parallellitet markeras med pilar. Hela sidor har måttlinjer, och i figurer där toppen heter C (3.99, 3.164) är punkterna omdöpta.
- **Likformiga trianglar:** paren är ritade med `tva()` i rätt skala. Den stora triangeln är ofta vriden, så att eleven måste para ihop sidorna efter storlek.
- **Texter:** varierade sammanhang (segel, förminskning, olika lägen och samma vinklar). 3.359 har nya tal (AD = 6, AB = 15, AC = 20, så AE = 8).
- **Facit:** varje steg har en rubrik, även i delkorten för 3.43, 3.99 och 3.176.

**Kontroll**
- **Figurer:** testet mäter DE/BC mot längdskalan och omkretsarnas kvot mot skalan, och kontrollerar att inga två topptriangelfigurer är identiska.
- **Validator:** 0 fynd.
- **Självrättning:** 33 fall i Kunskapsgymmet, och alla ger väntat resultat.
- **Skydd:** `tools/ma2-kap3-likformighet-2026-10-26.test.js`.

## Etapp 6: kordasatsen och bevis med likformighet (2026-10-26)

**Kordasatsen**
- 3.79, 3.315 och 3.340 var nästan samma textuppgift som 3.44 (”Två kordor skär varandra. Den ena delas i …”).
- 3.79 handlar nu om en rund matta och 3.315 om ett runt fönster. I 3.340 adderar Sara delarna i stället för att multiplicera, och eleven ska rätta henne.
- Alla tre har fått en kordafigur. Cirkeln beräknas ur delarna, så att alla fyra ändpunkter ligger på cirkeln och delarna har rätt proportioner.
- Övriga kordafigurer och bisektrisfigurer är i stort sett skalenliga och behålls.

**Bevis med likformighet**
- 3.152, 3.177, 3.206, 3.254, 3.255 och 3.283 använde samma likbenta DE ∥ BC-triangel. De har nu varierade, skalenliga figurer ritade med `topp()`, som har fått stöd för vinkelmarkeringar.
- 3.283 var samma fråga som 3.254 och markerar nu vinkeln \(AED\) (rätt svar: \(\angle ACB\)).
- 3.254 hade alternativen \(\angle ACB\) och \(\angle BCA\), som är samma vinkel. Det ena är bytt mot \(\angle AED\).
- 3.151 är ritad i rätt skala (1,5).
- 3.284 har fått en egen figur, eftersom den hade samma som 3.256.

**Facit:** varje steg har en rubrik, även i delkorten för 3.151 och 3.177.

**Kontroll:** validatorn ger 0 fynd, och självrättningen i Kunskapsgymmet ger väntat resultat. Skydd: `tools/ma2-kap3-korda-bevis-2026-10-26.test.js`.

## Etapp 7: avstånd, mittpunkt och koordinatgeometri (2026-10-26)

**Figurerna** är ritade i rutnät och var skalenliga. Problemet var texterna.

**Dubbletter med nya tal och sammanhang**
- 3.342 hade samma punkter som 3.264. Nu kör en robotgräsklippare från \((-2,-3)\) till \((7,9)\), och svaret är 15 m.
- 3.341 hade samma punkter som 3.263. Nu hänger en lykta mitt på en lina mellan \((-3,8)\) och \((7,2)\), och svaret är \((2,5)\).
- 3.319 hade samma rektangel som 3.288. Nu gäller det en pool med hörnen \((-3,-1)\) till \((5,4)\), och svaret är 40 m².
- 3.362 hade samma uppbyggnad och samma svar som 3.301. Nu är det en ny triangel med svaret 36.
- 3.2036 hade samma triangel som 3.203. Nu är det en rätvinklig triangel, \((0,0)\), \((4,2)\) och \((1,8)\).

**Nästan identiska texter med ny form**
- 3.358 är omvänd: avståndet är givet och \(b\) ska bestämmas.
- I 3.326 adderar Elin förflyttningarna i x- och y-led, och eleven ska förklara felet.
- 3.343 handlar om Hanna som går förbi ett träd, där trädet är mittpunkten.
- I 3.128 flyger en fågel.
- 3.2045 handlar om staket runt en hage.

**Facit:** varje steg har en rubrik.

**Tester:** `felrapporter-2026-10-14-1325.test.js` har uppdaterats med 3.341:s nya tal.

**Kontroll:** validatorn ger 0 fynd, och självrättningen i Kunskapsgymmet ger väntat resultat. Skydd: `tools/ma2-kap3-koordinat-2026-10-26.test.js`.
