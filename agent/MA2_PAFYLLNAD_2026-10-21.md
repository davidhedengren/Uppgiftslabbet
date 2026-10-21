# Ma2: påfyllnad med varierade uppgifter, 2026-10-21

## Underlag och avgränsning

Användaren bad om två saker:

- fyll banken där det finns få uppgifter eller lite variation, gärna med figurer,
- fyll på med varierade uppgifter om standardavvikelse, utan formeln för hand, och granska de befintliga.

Användaren påpekade att innehållet måste finnas i ämnesplanen och att inga nya
områden ska skapas. Nya delmoment (familjer) inom befintliga områden är tillåtna.

Uppgifterna är kontrollerade mot Gy25-ämnesplanen för matematik (MATE, SKOLFS 2023:130),
nivå 2:

- "Metoder för att lösa linjära ekvationssystem" och grafiska metoder för att lösa ekvationer.
- "Lägesmått och spridningsmått, däribland percentiler och standardavvikelse, samt
  digitala metoder för att bestämma dessa".

Ett påbörjat tillägg i `tabeller_diagram` togs bort innan det committades. Att
läsa av, granska och välja diagram nämns inte i det centrala innehållet på nivå 2.

## Grafisk lösning av ekvationssystem (1.675–1.683)

Området hade 11 uppgifter, varav 7 var rena avläsningar på nivå 1. Nio nya
uppgifter på nivå 2–4 med egna koordinatsystem:

- **Avläsa skärningspunkt:**
  - 1.675: abonnemang, svar 200 min.
  - 1.676: tre linjer där rätt par ska väljas, svar (4, 1).
  - 1.677: rutnät med steget 0,5, svar (2,5; 4).
  - 1.678: stearinljus, svar 6 h och 8 cm.
- **Tolka grafisk lösning (nytt delmoment):**
  - 1.679: vilket system grafen visar.
  - 1.680: parallella linjer, ingen lösning.
  - 1.681: kontroll genom insättning.
  - 1.682: välja en linje så att systemet saknar lösning.
  - 1.683: bestämma k ur skärningspunkten, svar k = 1.

## Standardavvikelse (4.384–4.395)

Granskningen av de 69 befintliga uppgifterna visade inga facitfel:

- Alla Sx-värden i tabell- och frekvensuppgifterna är omräknade med n − 1 och stämmer.
- Inga uppgifter kräver att man räknar standardavvikelsen för hand. De som beräknar
  Sx ur data har GeoGebra påslaget.

Variationen är däremot låg:

- cirka 18 nästan likadana omvandlingsuppgifter ("alla värden ökas/multipliceras med …"),
- cirka 9 likadana jämförelser ("vilket material har störst spridning?"),
- cirka 18 uppgifter med samma mall för median, typvärde, medelvärde och Sx.

De lämnas orörda, eftersom inget är fel. Användaren får avgöra om några ska tas bort.

Tolv nya uppgifter:

- **Uppskatta och tolka spridning i diagram (nytt delmoment, figurer):**
  - 4.384: tre prickdiagram, svar C.
  - 4.385: uppskatta Sx, svar ungefär 5.
  - 4.386: extremvärde, Sx ökar kraftigt.
  - 4.387: koppla Sx ≈ 5/16 till histogram, svar Q.
  - 4.388: Sx = 0.
  - 4.389: ett värde lika med medelvärdet läggs till, Sx minskar lite.
- **Beräkna och tolka standardavvikelse (GeoGebra):**
  - 4.390: två städers temperaturer, svar 1,2 och 4,4 °C.
  - 4.391: antal värden inom medelvärde ± Sx, svar 8.
  - 4.392: jämnaste golfspelaren, svar B.
  - 4.393: kvalitetskrav Sx ≤ 2,0 g uppfylls inte, Sx ≈ 2,8 g.
- **Jämföra spridning och förändring (teori):**
  - 4.394: standardavvikelsens enhet.
  - 4.395: standardavvikelsen kan inte vara negativ.

Inga uppgifter räknar Sx för hand. Lösningarna hänvisar till Sx i GeoGebras
statistikverktyg, inte till SD(), som ger σ. Data i 4.391 är vald så att inget värde
ligger närmare än 0,5 från intervallgränserna, vilket gör svaret robust mot avrundning.

## Verifiering

- Alla 21 nya uppgifter rättas korrekt i Kunskapsgymmet (2c):
  - flervalsuppgifter med rätt och med fel alternativ,
  - siffersvar med decimalkomma, med enhet och med ett felaktigt värde.
- Alla figurer är granskade på skärmbild:
  - prickdiagrammens höjd anpassas efter den högsta högen,
  - x-axelns etikett ligger ovanför pilen,
  - varje SVG har ett unikt clipPath-id och en maxbredd.
- Test: `tools/ma2-pafyllnad-2026-10-21.test.js`.

## Ombyggda upprepningar i standardavvikelse (samma dag)

Användaren godkände att en del upprepade uppgifter tas bort och byggs om till mer
varierade uppgifter. Uppgifterna byggdes om på plats. ID, `kurs` och
`familjTidigare` behölls, så att länkar och elevhistorik inte går sönder. De gamla
versionerna finns i `MA2_SX_OMBYGGDA_GAMLA_VERSIONER_2026-10-21.json`.

Följande ID:n byggdes om:

- 4.211: flera påståenden om egenskaper.
- 4.212: samma variationsbredd men olika Sx (prickdiagram).
- 4.235: felskrivet värde med GeoGebra, 17,58 → 0,31 m.
- 4.236: antal standardavvikelser från medelvärdet, svar 2,5.
- 4.201: jämföra resultat relativt spridningen, svar Bea.
- 4.102: slå ihop material med samma medelvärde, ungefär 5.
- 4.114: slå ihop material med olika medelvärden, betydligt större än 5.
- 4.174: mätmetoders precision med GeoGebra, 0,22 och 0,03 cm.
- 4.14: ta bort extremvärdet, svar 24.
- 4.65: lådagram och Sx, svar Q.
- 4.173: vilket material har Sx = 0.
- 4.195: värde mer än två standardavvikelser bort, svar 27.
- 4.213: vardagsbeslut utifrån spridning, svar buss 1.

Kvar av de upprepade typerna finns:

- omvandlingar: 4.21, 4.43, 4.49, 4.56, 4.68, 4.75, 4.86, 4.90, 4.93 och 4.109,
- jämförelser: 4.36, 4.84, 4.121 och 4.156.

4.43, 4.49 och 4.90 skyddas av `felrapporter-2026-10-16.test.js` och ändrades inte.

En ändringsvariant ("vilket värde ändras till 20 för största Sx") förkastades,
eftersom tre alternativ gav nästan samma Sx (4,90, 4,92 och 4,89). Den ersattes
av borttagning av ett tydligt extremvärde. Alla 13 kort rättas korrekt i
Kunskapsgymmet, både med rätt och med felaktigt svar.
