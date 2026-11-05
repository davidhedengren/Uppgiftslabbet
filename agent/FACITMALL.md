# Facitmall för Uppgiftslabbet

Användarbeslut 2026-11-04: detta är **standard för alla facit i hela
Uppgiftslabbet**, i både matematik och fysik och i alla sju banker. Mallen gäller
nya uppgifter, omarbetade uppgifter och facit som skrivs om. Äldre facit görs om
efter hand, område för område. Ett facit som inte följer mallen räknas som ett
brist att åtgärda, inte som ett godkänt alternativ.

Förebilder:

- Fysik: Fy1 *Rörelse med konstant acceleration* (`konstacc`, 3.4–3.448).
- Matematik: Ma1 **1.116**.

## 1. Grundprincip

Ett facit är en **numrerad steglista** där varje steg har en **rubrik som säger
vad som görs**. Beräkningen står i samma steg som rubriken, och facit avslutas
med en **svarsrad**. Eleven ska kunna följa lösningen utan att gissa vilken
formel, regel eller metod som används.

1. **Formeln eller regeln ska alltid stå ut.** Skriv inte ”hastighet är
   acceleration gånger tid”, utan rubriken ”Hastighetsformeln: \(v=v_0+at\)”.
   I matematik namnges regeln, till exempel ”Kvadreringsregeln:
   \((a+b)^2=a^2+2ab+b^2\)”.
2. **Rubrikerna är specifika för uppgiften.** De beskriver vad som faktiskt
   händer, till exempel ”x² finns i båda leden och tar ut varandra” eller
   ”Lägg till kasthöjden”. Generiska rubriker som ”Steg 1”, ”Beräkna” och
   ”Förenkla” ensamma används aldrig. Rubriker genereras inte automatiskt.
3. **Hellre ett steg för mycket än ett för lite**, men inga tomma steg. Varje
   steg innehåller antingen en formel, en insättning, en uträkning eller en
   förklaring som för lösningen framåt.
4. **Visa insättningen** med värden och enheter innan resultatet, så att eleven
   ser var talen hamnar.
5. **Andragradsekvationer** (och andra ekvationer som eleverna löser med
   digitalt verktyg) får **alltid en grafisk lösning** i facit, se avsnitt 4.
6. **Svarsraden** upprepar svaret med enhet och lämplig precision. Den ska stämma
   med `rättSvar`, `svarEnhet` och `svarVardesiffror`. Den får aldrig innehålla
   ”None”, ”null” eller tekniska rester.

## 2. HTML-struktur

```html
<div class="facit-v2 facit-stegvis">
  <ol class="facit-steglista" role="list">
    <li>
      <p class="facit-rubrik">Givet och sökt</p>
      <div class="facit-matte">\[\begin{aligned}&v_0=0\\&v=19{,}44\ \mathrm{m/s}\\&s=55\ \mathrm m\end{aligned}\]</div>
      <p>Sökt: accelerationen \(a\). Tiden är inte given.</p>
    </li>
    <li>
      <p class="facit-rubrik">Tidlösa formeln: \(v^2=v_0^2+2as\)</p>
      <p>Formeln behöver inte tiden.</p>
    </li>
    <li>
      <p class="facit-rubrik">Lös ut \(a\) och sätt in</p>
      <div class="facit-matte">\[a=\frac{v^2-v_0^2}{2s}=\frac{19{,}44^2-0^2}{2\cdot55}\approx3{,}44\ \mathrm{m/s^2}\]</div>
    </li>
  </ol>
  <p class="facit-svar"><strong>Svar:</strong> 3,44 m/s².</p>
</div>
```

- Rubrik: `<p class="facit-rubrik">`. Formeln står inline, `\( … \)`, i rubriken.
- Uträkningar: `<div class="facit-matte">\[ … \]</div>`. Förklaringar: `<p>`.
- **Uppgift med flera delfrågor i samma kort** (a, b, c … i ett facit):
  ```html
  <div class="facit-v2 facit-stegvis">
    <div class="facit-del"><span class="facit-mark">a)</span><div class="facit-arbete">
      <ol class="facit-steglista" role="list"> … </ol><p class="facit-svar"><strong>Svar:</strong> …</p>
    </div></div>
    <div class="facit-del"><span class="facit-mark">b)</span><div class="facit-arbete"> … </div></div>
  </div>
  ```
- **Uppdelade uppgifter** (`spelDelning: "deluppgifter"`): varje `spelDelar[i].s`
  är ett eget komplett facit enligt mallen, med egen svarsrad. Huvudfacit `s` är
  delarnas facit efter varandra med `facit-del` enligt ovan.

### Mobil

Facit läses ofta på mobil. Bryt därför långa rader:

- Givna värden står på **egna rader** med `\begin{aligned}&…\\&…\end{aligned}`.
- En lång kedja med ⇒ bryts så att ⇒ börjar en ny rad.
- Undvik att mer än ett likhetstecken med långa bråk står på samma rad.

## 3. Stegtyper

| Steg | När | Rubrik (exempel) |
|---|---|---|
| **Givet och sökt** | Fysik och tillämpningar, nästan alltid | ”Givet och sökt”. Tecken, vald positiv riktning, nollnivå och omvandlade enheter (70 km/h = 19,44 m/s). Avsluta med ”Sökt: …”. |
| **Formel/regel** | Varje gång en formel eller regel används | ”Sträckformeln: \(s=v_0t+\tfrac{at^2}{2}\)”, ”Pq-formeln”, ”Logaritmlagen \(\lg a^b=b\lg a\)”. En rad om **varför** den passar, till exempel ”tiden är inte given”. |
| **Sätt in / lös ut** | Efter formelsteget | ”Lös ut \(a\) och sätt in”, ”Sätt lägena lika”. |
| **Grafisk lösning** | Andragradsekvationer och liknande | ”Lös ekvationen grafiskt”, se avsnitt 4. |
| **Alternativ** | När en annan metod är vanlig | ”Alternativ: lösningsformeln”, ”Alternativ: faktorisera”. Står efter huvudmetoden. |
| **Kontroll** | När den tillför förståelse | ”Kontroll: summan av delspänningarna är 12 V”. |
| **Tolkning/slutsats** | Resonemang, flera rötter, rimlighet | ”Den första skärningen gäller”, ”Varför blir det inte dubbelt så långt?”. |

Minst ett steg i varje facit (och i varje delfacit) ska ha en rubrik med en
formel eller regel i \( … \). Undantag är rena begrepps- eller flervalsfrågor,
där rubriken i stället namnger begreppet (”Tröghetslagen”).

### Formelnamn i fysik (Fy1)

Använd samma namn överallt så att eleverna känner igen dem:

- Hastighetsformeln \(v=v_0+at\)
- Sträckformeln \(s=v_0t+\tfrac{at^2}{2}\). Från vila: \(s=\tfrac{at^2}{2}\). Fall: \(s=\tfrac{gt^2}{2}\).
- Tidlösa formeln \(v^2=v_0^2+2as\)
- Sträcka med medelhastighet \(s=\tfrac{v_0+v}{2}\cdot t\)
- Konstant fart \(s=vt\). Reaktionssträcka \(s_r=v_0t_r\).
- Bromssträcka till stillastående \(s_b=\tfrac{v_0^2}{2b}\). Stoppsträcka \(s_{\text{stopp}}=s_r+s_b\).
- Ohms lag \(U=RI\), effekt \(P=UI\) och så vidare för övriga kapitel.

## 4. Grafisk lösning

**Undantag för Ma2, användarbeslut 2026-11-04:** Vid algebraisk lösning av
andragradsekvationer används pq-formeln som normalmetod när faktorer annars
måste gissas. Visa normalformen, p och q, insättningen och tolkningen av
rötterna. En grafisk huvudlösning eller GeoGebra krävs inte för dessa uppgifter.
Behåll naturlig utbrytning, konjugatregeln och direkt nollprodukt när uttrycket
redan är faktoriserat; använd kvadratrotsmetoden där den passar. Uppgifter
som faktiskt prövar grafisk lösning behåller graf och digitalt verktyg.


Eleverna löser andragradsekvationer (och liknande ekvationer) grafiskt. Facit ska
därför alltid visa det:

1. Skriv ekvationen, till exempel \(0=1{,}5+9{,}0t-4{,}91t^2\).
2. Steget **”Lös ekvationen grafiskt”**: en mening om vad som ritas (”Rita
   \(h(t)\) och läs av var grafen skär t-axeln”) och en **SVG-graf** med:
   - kurvan och eventuell vågrät linje (t.ex. \(s=40\)) eller två kurvor (möte:
     båda lägena), med etiketter med vit kontur;
   - axlar med enhet (”t (s)”, ”h (m)”), stödlinjer och tal;
   - skärningspunkten markerad, en streckad lodlinje och det avlästa värdet
     (”t ≈ 1,99”).
3. Vid två rötter: visa båda, markera och läs av den som efterfrågas, och förklara
   i ett tolkningssteg varför den andra inte gäller eller vad den betyder.
4. Därefter ”Alternativ: lösningsformeln” eller ”Alternativ: faktorisera”.
5. Sätt `geogebra: true` på uppgiften (GeoGebra innebär också tillåten miniräknare).

Graferna i `konstacc` är byggda med hjälpfunktionerna `graf`/`graf2` (se
`agent/FY1_KONSTACC_FACIT_2026-11-04.md`). De följer reglerna för SVG i
`INNEHALLSREGLER.md` 3.9.

## 5. Delfacit och läckage

- Ett delfacit får **aldrig avslöja svaret på en senare del** (se 3.4 i
  `INNEHALLSREGLER.md` och `DELKEDJOR_OCH_FACIT_2026-11-01.md`). Välj hellre en
  formel som inte går via nästa dels svar. Exempel: lös tiden med sträckformeln
  och grafen i stället för att först räkna ut slutfarten, om slutfarten är nästa
  del.
- Ett delfacit **får** använda svar från tidigare delar. Skriv då uttryckligen
  varifrån värdet kommer, till exempel ”Accelerationen från a)”.
- I en grafisk lösning kan en senare dels svar synas naturligt i grafen. Markera
  och läs då bara av den efterfrågade punkten.

## 6. Kortare facit på låg nivå

Nivå 1 och enkla enstegsuppgifter kan ha två steg: formelsteget och svarsraden.
Formeln ska ändå stå i en rubrik:

```html
<ol class="facit-steglista" role="list">
  <li><p class="facit-rubrik">Fart från vila: \(v=gt\)</p>
      <div class="facit-matte">\[v=9{,}82\cdot1{,}0=9{,}82\ \mathrm{m/s}\]</div></li>
</ol>
<p class="facit-svar"><strong>Svar:</strong> 9,82 m/s.</p>
```

## 7. Matematik

Samma struktur. Rubriken namnger regeln eller beskriver förändringen:

- ”Utveckla vänsterledets produkt”, ”Kvadreringsregeln: \((a-b)^2=a^2-2ab+b^2\)”,
  ”Pq-formeln: \(x=-\tfrac p2\pm\sqrt{(\tfrac p2)^2-q}\)”, ”Derivatan av \(e^{kx}\) är \(ke^{kx}\)”.
- Ekvationer som löses grafiskt i kursen (andragradsekvationer, exponential-
  och potensekvationer med digitalt verktyg) får grafisk lösning enligt avsnitt 4.
- Statistik, geometri och resonemang följer samma mall. Se Ma1 1.116 för en
  komplett förebild.

## 8. Checklista före leverans

- [ ] Steglista med specifika rubriker, minst en rubrik med formel/regel.
- [ ] Givet och sökt med tecken, positiv riktning och omvandlingar (fysik).
- [ ] Insättning med enheter, resultat med rimlig precision.
- [ ] Grafisk lösning med graf vid andragradsekvationer, `geogebra: true`.
- [ ] Svarsraden stämmer med `rättSvar`, `svarEnhet` och `svarVardesiffror`.
- [ ] Inget delfacit avslöjar en senare dels svar.
- [ ] Långa rader brutna för mobil.
- [ ] Facit renderat (KaTeX) och läst, i mobilbredd, före leverans.
- [ ] Regressionstest kontrollerar formatet (se `tools/fysik1-konstacc-facit-2026-11-04.test.js`).

## Statistikfacit: visa GeoGebra steg för steg (5 november 2026)

Användaren vill att statistikfacit lär eleven att använda GeoGebra. När uppgiften löses med verktyget ska varje huvudfacit och relevant fristående delkort ange uppgiftens faktiska data, hur de matas in, vilka menyval som används, vilket resultat som läses av och hur det tolkas eller avrundas. Välj lämplig metod för rådata, frekvenstabell, diagram respektive normalfördelning; en allmän uppmaning att ”använda GeoGebra” räcker inte. Sätt GeoGebra och miniräknare som tillåtna när verktyget används. Undvik att avslöja senare delars svar.

I GeoGebras svenska Classic-kalkylblad har gränssnittet kontrollerats: markera celler → stapeldiagramknappen → Envariabelanalys → Σx. Statistikpanelen visar stickprovsstandardavvikelsen som **s**, medan uppgifterna ofta skriver **Sx**; förklara att s motsvarar Sx och skilj den från σ. Gränssnitt kan variera mellan versioner. Visa gärna en relevant och korrekt skärmbild om det är möjligt; hitta inte på en skärmbild. Se [första granskningen](MA2_STATISTIK_GEOGEBRA_BILDER_2026-11-05.md).

### Skärmbilder som visar var man klickar (användarbeslut 2026-11-05)

Användaren: i uppgifter som är tänkta att lösas med GeoGebra ska facit ha **tydliga skärmbilder som visar hur det ser ut i GeoGebra och var man ska trycka**, så att eleven kan lära sig verktyget av facit. Det ersätter ”visa gärna en skärmbild” ovan: skärmbilder är standard för GeoGebra-facit.

- Ett steg per handgrepp, var och ett med sin bild: öppna Kalkylblad (Meny → Perspektiv → Kalkylblad), skriv och markera uppgiftens värden, välj verktyget, visa resultatet (till exempel Σx) och läs av den rad som behövs.
- Bilderna är riktiga skärmbilder från GeoGebra Classic på svenska med uppgiftens egna värden. Knappar och rader är inringade med numrerade markeringar. Rita aldrig efter eller hitta på en skärmbild.
- I delkort döljs de rader i statistikpanelen som skulle avslöja en senare dels svar. Sista delen och huvudfacit får visa hela panelen.
- Nämn att GeoGebra visar decimaltal med punkt (1.7889 betyder 1,7889).
- Bilderna tas med `tools/geogebra-skarmbilder.js`, som också läser av panelens värden så att facit kan kontrolleras mot dem. Se [stegbilderna](MA2_STATISTIK_GEOGEBRA_STEGBILDER_2026-11-05.md).
