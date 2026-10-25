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
