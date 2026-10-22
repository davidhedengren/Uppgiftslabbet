# Ma3 – rationella uttryck, 2026-10-22

Åtta nya uppgifter, 1.880–1.887, i `rakna_rationella` för 1b/1c.
Området hade 23 huvuduppgifter och två huvuduppgifter med spelbar nivå 1.
Efter påfyllnaden finns 31 huvuduppgifter, varav sju spelbara på nivå 1.
Fem nya uppgifter har nivå 1 och tre nivå 2. Fyra egna SVG-figurer ger
variation mellan symboler, areor, volym/flöde, priser och felslut vid division.

## Alla granskade uppgifter och kommentarer

| Kurs / ID | Utfall | Kommentar / verifierat svar |
|---|---|---|
| Mato1 1.880 | Ny, granskad – inget fel, nivå 1 | Rektangelns area är x·12/x=12 cm². |
| Mato1 1.881 | Ny, granskad – inget fel, nivå 1 | Vid division med (x+2)/3 multiplicerar man med 3/(x+2). |
| Mato1 1.882 | Ny, granskad – inget fel, nivå 1 | Fyllningstiden är 6x/(2x)=3 minuter. Även 180 s godtas. |
| Mato1 1.883 | Ny, granskad – inget fel, nivå 1 | Priset per bok är (x+4)/(4x) kr. Hela totalpriset delas med fyra. |
| Mato1 1.884 | Ny, granskad – inget fel, nivå 1 | Produkten är 2. Villkoret x≠−3 behövs för förkortningen. |
| Mato1 1.885 | Ny, granskad – inget fel, nivå 2 | x=−2 ger noll i nämnaren och x=3 ger division med noll. x=1 är tillåtet. |
| Mato1 1.886 | Ny, nivå 2; rättningsbrist åtgärdad | Det förenklade uttrycket är 3x. Nu godtas även y=3x och f(x)=3x. Oförenklade uttryck godtas inte. |
| Mato1 1.887 | Ny, granskad – inget fel, nivå 2 | Areorna är 8 och 3 cm². Förhållandet är exakt 8/3. |
| Ma1 1.08 | Följdgranskad rättning, åtgärdad | Summan n+(n+1)+(n+2)=3n+3. Frivilligt vänsterled godtas nu. |
| Ma1 1.11 | Följdgranskad rättning, åtgärdad | 4(x−10)+3·22=4x+26 kr. Frivilligt vänsterled godtas nu. |
| Ma1 1.18 | Följdgranskad rättning, åtgärdad | (x+5)(x+2)−x(x+3)=4x+10 cm². Frivilligt vänsterled godtas nu. |
| Ma1 1.26 | Följdgranskad rättning, åtgärdad | (6x+24)/6=x+4 cm. Frivilligt vänsterled godtas nu. |
| Ma1 1.67 | Följdgranskad rättning, åtgärdad | (x+y)−(x−y)=2y. Frivilligt vänsterled godtas nu. |

Inga äldre facit eller bankobjekt ändras. De fem Ma1-kontrollerna avser
matematik och svarsfält, inte en ny fullständig figur-/nivågranskning.
Kommentarerna är förslag; inga rapporter eller meddelanden sparas i appen.

## Beslut och skydd

- Nya kort är fristående. Miniräknare tillåts; GeoGebra behövs inte för
  dessa grundläggande samband. De faktiska spelkortens verktyg kontrolleras.
- Figurer finns i 1.880, 1.882, 1.883 och 1.887. Övriga frågor handlar
  direkt om symboliska bråk; extra illustrationer skulle bara upprepa dem.
- 1.886 använder `förenklat_polynom`, så att originalkvoten inte kan klistras
  in som färdigt svar. Testet visade att formatet avvisade y=3x trots att
  vanlig uttrycksrättning tillåter vänsterled. Formatet använder nu samma
  befintliga `hogerled` som appens andra format före polynomkontrollen.
- Krav på samlade termer, förkortade koefficienter och rätt variabel består.
  Exempelvis y=2x+x, y=6x/2 och y=4x ska fortfarande underkännas.
- Tidigare FP47 och FP57 lästa. Deras beslut om stora bokstäver,
  definitionsvillkor och fullständiga svar ersätts inte.

## Verifiering

- Två nya matematik-/metadatagrupper godkända i
  `tools/ma3-rationella-2026-10-22.test.js`.
- Konsumentens `tools/brakuttryck.test.js`: sju grupper godkända, inklusive
  ny kontroll av vänsterled samt samtliga äldre förenklingskrav.
- Tidigare `tools/felrapporter-2026-10-14-1325.test.js`: fem grupper godkända.
- Konsumentens motsvarande browserprov testar riktiga svarsfält, alla
  15 icke-tomma valkombinationer i var och en av tre flervalsfrågor och
  fem äldre jämförelseuppgifter. Mobil 390 px och dator 1280 px.
- Resultat: 192 rättningskontroller, 16 elevvyer och 16 lärarvyer godkända.
  Inga JavaScript-fel, trasiga formler eller klippta etiketter hittades.
- Alla nya elevkort och läraruppgifter granskas i båda bredderna.
  Fyra SVG visuellt kontrollerade; noll ERROR/WARNING i geometrikontrollen.
  Fyra INFO gäller den avsiktliga vita bakgrunden vid bildkanten.
- Full bankvalidator före/efter: 1539 ERROR, 230 WARNING, 1446 INFO.
  Inga nya fynd. Äldre fynd utanför denna påfyllnad kvarstår.
- Strukturell diff: endast åtta nya bankobjekt. Bankkopiorna är identiska.
  Pågående lokala fysikutkast har bevarats och ingår inte i denna leverans.
