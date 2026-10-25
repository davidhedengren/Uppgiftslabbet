# Fy1: nivå 3 i tunna områden, 2026-10-25

**Lärarbeslut:**

- Fyll inte medicinska metoder, standardmodellen eller strålning möter materia. Där görs få uppgifter.
- Fyll övriga tunna områden ett i taget, och pusha efter varje område.
- Uppgifterna ska vara varierade och ingå i kursen, utan svåra eller krångliga formuleringar. Stilen ska likna de befintliga korten.
- Facit görs enligt instruktionen, och figurer används där de passar.

Läget mättes med appens nivålogik efter dagens övriga omgångar. Antal kort på nivå 3:

| Område | Kort på nivå 3 |
|---|---|
| em_stralning | 4 |
| enheter | 5 |
| tyngdkraft | 5 |
| falt | 5 |
| strom | 7 |
| parallellkoppling | 7 |
| potential | 7 |
| sonderfall | 7 |

Varje område kontrolleras i `tools/fysik1-niva3-tunna-2026-10-25.test.js` (nivå, format, facitkrav och dubblettfacit). Numeriska kort i kap 9 läggs också till i strålnings- och kärnfysiktesternas listor.

## 1. Elektromagnetisk strålning (em_stralning): 6 kort, 9.576–9.581

Tre av de fyra befintliga nivå 3-korten var varianter av ”fotoner per sekund”. De nya korten har andra frågetyper:

| ID | Innehåll |
|---|---|
| 9.576 | Energin i en mol fotoner |
| 9.577 | Hur mycket kortare våglängden blir när radiostationen byter frekvens |
| 9.578 | Ljuseffekt ur antalet fotoner (baklänges) |
| 9.579 | Vilken sorts strålning en foton på 5,0 eV är (flerval efter beräkning) |
| 9.580 | Energiintervallet för synligt ljus |
| 9.581 | Hur många gånger större energi en foton av blått ljus har än en mobilfoton |

Konstanterna är desamma som i strålningstestet (h = 6,63·10⁻³⁴ J·s, c = 3,00·10⁸ m/s). Ingen figur, eftersom det inte tillförde något.

Facitgranskningen gjordes före infogningen:

- Facit och ledtråd renderades och lästes igenom.
- Alla facit har metodtext och svarsrad.
- 9 långa räkneled radbröts för mobil.

Kontroller:

- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades i Kunskapsgymmet med 20 svar, och alla gav väntat resultat.

## Lärarbeslut: konstanter slås upp i formelsamlingen

Läraren beslutade att naturkonstanter inte ska stå i uppgifterna. Svar räknade med c = 2,998·10⁸ ska också godkännas. Regeln står nu i `CLAUDE.md`.

Dagens fysikkort söktes igenom:

- **Konstanter i frågan:** 9.526, 9.527, 9.532, 8.650 och den nya 9.576. De togs bort.
- **Konstanter i ledtråden:** 8.638, 9.537, 9.539 och 9.542. Ledtrådarna formulerades om.
- **Toleranser:** alla kort med c eller h räknades om med formelsamlingens värden (6,626·10⁻³⁴ och 2,998·10⁸).
  - Bara 9.539 underkände då ett korrekt avrundat svar (496 mot facit 497 nm), så toleransen vidgades till 1 nm.

Testet kontrollerar att inga naturkonstanter står kvar i frågor eller ledtrådar.

## 2. Måttenheter och prefix (enheter): 6 kort, 2.359–2.364

| ID | Innehåll |
|---|---|
| 2.359 | Tvärsnittsarean av ett hårstrå i mm² (prefix i kvadrat) |
| 2.360 | Hur långt ljuset färdas på en nanosekund (c slås upp) |
| 2.361 | Volym och kantlängd för en guldkub ur densiteten |
| 2.362 | En laddares energi i kJ och kWh |
| 2.363 | Ungefär antalet sandkorn i en liter (storleksordning) |
| 2.364 | Löparens fart ur tempot i min per km |

Kontroller:

- Facit renderades och lästes igenom, och alla räkneled ryms på mobil.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 29 svar, inklusive de rättade konstantkorten. Alla gav väntat resultat.

## 3. Tyngdkraft: 5 kort, 4.897–4.901

| ID | Innehåll |
|---|---|
| 4.897 | Vilken planet det är, ur en mätning (flerval, jämför med formelsamlingen) |
| 4.898 | Lastbilens massa ur tyngdkraften 0,15 MN, i ton |
| 4.899 | Tyngden av en hink med vatten (densiteten ingår) |
| 4.900 | Vilken låda som har störst tyngd, 12 kg på månen eller 2,0 kg på jorden (flerval efter beräkning) |
| 4.901 | Kraftmätarens mätområde på jorden och på månen |

g-värden står inte i frågorna. Toleranserna godtar både 9,81 och 9,82 m/s² samt 1,62 och 1,63 m/s².

De numeriska korten har lagts till i tyngdkraftslistan i `fysik1-kapitel4.test.js`. Antalet i `fysik1-tyngdkraft-variation-2026-10-21` är nu 46 kort, varav 44 spelbara.

Kontroller:

- Facit renderades och lästes igenom, och 3 räkneled radbröts.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 13 svar, och alla gav väntat resultat.

## 4. Elektriska fält och fältstyrka (falt): 6 kort, 8.661–8.666

Tre av de fem befintliga nivå 3-korten var samma mall (fältet mellan +Q och −Q i P). De nya korten:

| ID | Innehåll |
|---|---|
| 8.661 | Antal elementarladdningar på en svävande oljedroppe |
| 8.662 | Kraften när plattorna flyttas isär med samma spänning |
| 8.663 | Avståndet för en given fältstyrka från en punktladdning |
| 8.664 | Fältet mellan två lika positiva laddningar, där fälten subtraheras (figur) |
| 8.665 | Fältets storlek och riktning ur kraften på en negativ laddning (flerval) |
| 8.666 | Fältet när laddningen dubblas och avståndet tredubblas |

Konstanterna k och e slås upp i formelsamlingen.

Kontroller:

- Facit renderades och lästes igenom, och 5 räkneled radbröts.
- SVG-granskaren ger 0 fynd. Plustecknen ritades som linjer.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 17 svar, och alla gav väntat resultat.

## 5. Kretsar och ström (strom): 5 kort, 8.667–8.671

| ID | Innehåll |
|---|---|
| 8.667 | Resistans och ström ur ett U–I-diagram med två resistorer (figur) |
| 8.668 | Glödlampans resistans vid två spänningar ur en böjd I–U-kurva (figur) |
| 8.669 | Tiden för en mol elektroner vid 2,0 A (konstanterna slås upp) |
| 8.670 | Voltmeter kopplad i serie med en lampa (flerval) |
| 8.671 | Resistans ur ändringen i spänning och ström |

Kontroller:

- Facit renderades och lästes igenom, och 4 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 14 svar, och alla gav väntat resultat.

## 6. Parallellkoppling: 6 kort, 8.672–8.677

| ID | Innehåll |
|---|---|
| 8.672 | Ström genom den ena grenen ur totalströmmen, via ersättningsresistansen |
| 8.673 | En tredje lampa kopplas in: ny ström och ersättningsresistans |
| 8.674 | Okänd resistans ur två amperemetrar (kretsfigur) |
| 8.675 | Två hushållslampor i ett vägguttag: total ström och resistans |
| 8.676 | En ledning utan resistans parallellt med en lampa, alltså kortslutning (flerval) |
| 8.677 | Hur många resistorer på 150 Ω som behövs för högst 22 Ω |

Kontroller:

- Facit renderades och lästes igenom.
- Testet hittade att 8.677 saknade svarsinstruktion, och den lades till.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 14 svar, och alla gav väntat resultat.

## 7. Potential: 6 kort, 8.678–8.683

Nästan alla befintliga nivå 3-kort var potentialvandringar med flera batterier. De nya korten:

| ID | Innehåll |
|---|---|
| 8.678 | Negativ potential i P när pluspolen är jordad (kretsfigur) |
| 8.679 | Hur mycket en elektrons rörelseenergi ökar när den går från −20 V till +30 V |
| 8.680 | En proton som accelereras genom 2,0 kV och sedan bromsas med 500 V |
| 8.681 | Energin i ett mobilbatteri (3,7 V, 3 000 mAh) |
| 8.682 | R₁ och R₂ ur ett potentialdiagram runt kretsen (figur) |
| 8.683 | Åt vilket håll en elektron börjar röra sig i ett fält (flerval) |

Kontroller:

- Facit renderades och lästes igenom.
  - ”3,000 Ah” skrevs om till ”3 000 mAh = 3,0 Ah”.
  - Batterietiketten i figuren flyttades.
  - 4 räkneled radbröts.
- SVG-granskaren ger 0 fynd.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 16 svar, och alla gav väntat resultat.

## 8. Sönderfall: 5 kort, 9.582–9.586

| ID | Innehåll |
|---|---|
| 9.582 | Antal alfa- och beta-minus-sönderfall från Th-232 till Pb-208 |
| 9.583 | Våglängden för en gammafoton på 0,662 MeV från Ba-137 (svar i pm) |
| 9.584 | Vilket sönderfall som är möjligt när massskillnaden bara är 0,00080 u (flerval) |
| 9.585 | Energin vid tritiums beta-minus-sönderfall (svar i keV) |
| 9.586 | Sönderfallstyp ur ett N–Z-diagram med stabilitetsband (figur, flerval) |

Övriga ändringar och kontroller:

- 9.557: meningen ”Elektronens massa är 0,000549 u.” togs bort ur frågan, eftersom konstanten ska slås upp i formelsamlingen. Svaret 1,20 MeV gäller fortfarande.
- 9.583 räknas med 6,626·10⁻³⁴ och 2,998·10⁸ och har toleransen 0,01. Svaren 1,87 och 1,88 godkänns båda.
- Facit renderades och lästes igenom. 4 räkneled radbröts.
- I figuren blev etiketten ”stabila kärnor” en förklaring uppe till vänster, och de lodräta rutlinjerna togs bort. SVG-granskaren ger 0 fynd.
- Validatorn ger 788 fynd både före och efter ändringen.
- Självrättningen testades med 12 svar, och alla gav väntat resultat.
