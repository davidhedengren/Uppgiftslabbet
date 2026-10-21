# Fysik 1: acceleration och hastighetsdiagram, 2026-10-21

Fortsättning efter medelhastighetsomgången. Mätnoggrannhet hoppas fortfarande
över enligt användarbeslut. Befintliga uppgiftstyper inventerades för att
komplettera med begrepp, diagram och olika problem, inte bara talvarianter.
Detta är inte en ny fullständig granskning av hela rörelsekapitlet.

## Alla nya och granskade uppgifter

| ID | Innehåll | Nivå | Svar |
|---|---|---:|---|
| 3.440 | Direkt beräkning av medelacceleration | 1 | 2 m/s² |
| 3.441 | Bromsning åt vänster och tecken på accelerationen | 2 | +2 m/s² |
| 3.442 | Parallella hastighetsgrafer: samma acceleration trots olika hastighet | 2 | C |
| 3.443 | Bromssträcka som triangelarea i hastighetsdiagram | 2 | 24 m |
| 3.444 | Avläs när rörelsen byter riktning | 1 | 2 s |
| 3.445 | Hiss nedåt som bromsar; skilj fart från hastighetens tecken | 2 | +0,50 m/s² |
| 3.446 | Acceleration från bromssträcka, utan given tid | 3 | −2,7 m/s² |
| 3.447 | Bestäm okänd högsta fart ur sträcka och diagram | 3 | 10 m/s |
| 3.448 | Ikappkörning: lika position är inte lika hastighet | 4 | 7,29 s |

Samtliga har egen SVG, kort uppgiftsspecifik ledtråd, förklarande lösning och
självbärande kort. Miniräknare är tillåten. GeoGebra behövs inte för avläsning,
area eller den andragradsekvation som förekommer. Exakta uttryck godtas där
relevant, exempelvis 2+sqrt(28) i 3.448 och −64/24 i 3.446. Ingen standardkonstant
eller färdig formelledning har lagts i själva frågan.

Nivå 1 är direkt samband med enkla tal respektive avläsning vid nollhastighet.
Nivå 2 kräver teckenhantering, lutningsjämförelse eller enkel geometrisk area.
Nivå 3 kräver ett metodval eller en ekvation utifrån flera delar av diagrammet.
Nivå 4 kräver två lägesmodeller, en andragradsekvation och val av fysisk lösning.

Lösningen till 3.446 visar ekvation, insatta värden och negativ acceleration.
3.447 visar de tre områdenas bidrag. 3.448 förklarar varför negativ tid förkastas
och varför hastighetslikhet vid 2 s inte innebär att vagnarna har mötts.

## Granskad – inget fel

Fem närliggande befintliga uppgifter är lösta och testade i faktisk rättning:

| ID | Kontroll | Föreslagen kommentar |
|---|---|---|
| 3.190 | 30/7 ≈ 4,29 m/s²; nivå 1 | Granskad – inget fel: både 4,29 och det oavrundade beräkningsvärdet godkänns. |
| 3.191 | Retardationens storlek 14/4,8 ≈ 2,92 m/s²; nivå 2 | Granskad – inget fel: frågan gäller storleken, så svaret ska vara positivt. |
| 3.194 | (18−15)/3,6/2,5 = 1/3 m/s²; nivå 2 | Granskad – inget fel: fartökningen behöver först omvandlas från km/h till m/s. |
| 3.270 | 9/4 = 2,25 m/s²; nivå 1 | Granskad – inget fel: accelerationen är 2,25 m/s². |
| 3.279 | (13,5−5)/1,8 ≈ 4,72 s; nivå 2 | Granskad – inget fel: både 4,72 s och det oavrundade beräkningsvärdet godkänns. |

Samtliga fem tillåter miniräknare och behöver inte GeoGebra. Inga ändringar i
dessa uppgifter bedömdes nödvändiga. Inga rapporter har stängts eller kommentarer
skickats till elever.

## Åtgärdade befintliga fel

Inga. Denna omgång tillför nio uppgifter. Alla äldre bankobjekt är strukturellt
jämförda med föreversionen och oförändrade. Samtliga manuellt granskade ID:n är
de nio nya och de fem jämförelseuppgifterna ovan.

## Verifiering

- Oberoende beräkningar och identitetskontroller, bland annat att vagnarnas
  positioner verkligen är lika vid den positiva lösningen i 3.448.
- Faktisk självrättning vid 390 och 1280 px med rätta och felaktiga svar,
  tecken, enheter och beräkningsuttryck: 96 kontroller och 28 visningar.
- Nya SVG:er kontrollerade med validator och visuellt. En kollision mellan
  tidsaxelns rubrik och sista graderingen i 3.447 hittades och rättades.
  Slutkontrollen har inga ERROR/WARNING, bara väntad INFO om vita bakgrunder.
- Bankvalidator före/efter: inga nya fynd. Inga dubbla ID:n.
- Tester: `tools/fysik1-acceleration-2026-10-21.test.js`, föregående
  medelhastighetstester samt konsumentens motsvarande browsertest.
- Master `uppgifter.js` synkas identiskt till Kunskapsgymmet. Konsumentens
  BANK_VERSION uppdateras. Browserkontrollerna skriver inte XP eller elevdata.

Vid leveransen integreras även remoteomgången med 48 uppgifter i andra områden
(master 113ae07, konsument c119a10). Dessa tillhör inte granskningen ovan.
Ingen av de nio nya rörelseuppgifternas ID:n krockar med remoteomgången.
