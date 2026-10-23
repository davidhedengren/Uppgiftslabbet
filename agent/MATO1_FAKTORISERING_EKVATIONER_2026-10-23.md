# Mato1: faktorisering och polynomekvationer, 2026-10-23

13 nya fristående uppgifter för både 1b och 1c: **1.900–1.912**.
Sex i faktorisera_polynom och sju i polynomekvationer. Områdena hade
28 respektive 38 huvudobjekt före tillägget, nu 34 respektive 45.
Inventeringen av äldre texter avsåg variation, inte en ny fullständig
certifiering av deras facit. Bland jämförelserna ingick 1.846, 1.847,
1.874, 1.875, 1.876 och 1.879; de ändras inte.

## Alla nya och detaljgranskade uppgifter

| ID | Nivå | Innehåll och facit | Föreslagen kommentar |
| --- | --- | --- | --- |
| 1.900 | 1/E | Gemensam faktor i delad rektangel; 2x+5 | Ny figuruppgift om hur area och sidlängd hänger ihop. |
| 1.901 | 1/E | Välj faktorformen till x²−5x+6; (x−2)(x−3) | Ny grunduppgift som skiljer produktform från en ofullständig omskrivning. |
| 1.902 | 3/C | Gruppera x³+4x²+3x+12; (x+4)(x²+3) | Ny uppgift om att hitta en gemensam parentes. |
| 1.903 | 2/E | Kvadrat med två borttagna remsor; 4x²−12x+9 | Ny areauppgift där hörnet inte ska räknas bort två gånger. |
| 1.904 | 3/C | Graf med dubbelt nollställe; (x+1)²(x−2) | Ny koppling mellan grafens beröring och upprepad faktor. |
| 1.905 | 3/C | Två rötter och konstantterm i moniskt kubikpolynom; a=−2 | Ny uppgift där den tredje roten kan bestämmas före koefficienten. |
| 1.906 | 1/E | x(x+4)=0; 0 och −4 | Ny enkel träning på nollproduktmetoden. |
| 1.907 | 1/E | Läs två rötter ur graf; −2 och 3 | Ny grafisk avläsning med två svarsfält utan ordningskrav. |
| 1.908 | 2/E | Hitta tappad lösning efter division med x; 0 | Ny felanalys: division med x kan ta bort nollroten. |
| 1.909 | 2/E | Rektangel med area 10 och sidor x, x+3; 2 cm | Ny geometrisk modell där negativ längd väljs bort. |
| 1.910 | 3/C | Två kurvors skärningspunkter; x=−2, 2, 3 | Ny kombination av funktioner, gruppering och tre rötter. |
| 1.911 | 4/C | Vik en låda med volym 384 cm³ ur 20×16 cm ark; x=2 eller 4 cm | Ny modelluppgift med GeoGebra och kontroll av möjliga längder. |
| 1.912 | 2/E | (x−a)(x+2)(x−4) har exakt två olika rötter; a=−2 eller 4 | Ny parameteruppgift där två faktorer måste ge samma rot. |

Fyra uppgifter vardera på nivå 1, 2 och 3; en på nivå 4. 1.912 bedömdes
först som nivå 3, men tabellen ger stöd som gör nivå 2 rimligare.
Vanlig räknare tillåts i samtliga; den ersätter inte algebran. GeoGebra
tillåts också i 1.911, där modellval och rimlighetsprövning är huvudsyftet.
De övriga kräver inte digitala funktioner.

Nio egna SVG-figurer/tabeller. 1.901, 1.902, 1.906 och 1.908 saknar figur:
uttrycken och felsökningen är själva underlaget, en extra bild tillför inte
information. Facit visar centrala mellanled i sammanhängande förklaringar.

## Granskningsutfall

**Alla detaljgranskade:** 1.900–1.912, individuellt listade ovan.
**Åtgärdade äldre uppgifter:** inga. Under konstruktionen korrigerades
enhetsbeskrivningen i 1.900/1.903. Visuell kontroll av 1.911 avslöjade att
råa mindre-än-tecken i HTML svalde delar av facit. Tecknen kodas nu som
HTML-entiteter; browserprovet kontrollerar att hela villkoret och meningen
efter faktiskt syns. Motsvarande text- och facitkontroll av 1.900, 1.903,
1.904, 1.905, 1.909, 1.910 och 1.912 hittade ingen sådan trunkering.

**Granskad – inget fel efter konstruktionskontrollen:** samtliga 13.
Kommentarsförslag står i tabellen. Inga rapportstatusar ändras i tjänsten.

## Verifiering

- Sex nya matematiska testgrupper och två tidigare faktoriseringsgrupper godkända.
- Browserprov: 120 rättningskontroller, 26 elevvyer och 26 lärarvyer,
  vid 390/1280 px. Omordnade faktorprodukter, naturliga prefix, omkastade
  rötter, enheter, felaktiga svar och upprepade rötter testas.
- Faktorform krävs där den efterfrågas; fullt utvecklat polynom godtas inte
  som faktorform. Numeriska rotlistor är mängder, utan dolt ordningskrav.
- Full validator oförändrad: ERROR 1485, WARNING 230, INFO 1446; inga nya fynd.
- Nio SVG kontrollerade med repo-validatorns geometriregler via Playwright.
  Inga ERROR, en WARNING, nio INFO. Varningen avser 1.910:s underliggande
  kurva utanför bildrutan; uttrycklig clipPath begränsar den synliga grafen
  korrekt. INFO avser vita bakgrundsrektanglar vid bildkanten.
- Alla figurer visuellt granskade; inga avklippta etiketter, KaTeX-fel eller
  överflöden i slutkontrollen. Bankkopiorna är identiska.

Skydd: `tools/ma3-faktorisering-ekvationer-2026-10-23.test.js` och
Kunskapsgymmets motsvarande `.browser.cjs`.
