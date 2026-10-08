# Fortsatt granskning: energi, tryck och kombinatorik

2026-10-08. Uppgiftslabbet är master; de två ändrade bankerna synkas byte för byte till Kunskapsgymmet.

## Omfattning och resultat

Ändrat 43 huvuduppgifter i Fysik 1 (71 ändrade träningskort) och 113 i matf1 (129 ändrade träningskort). Alla ID:n och befintliga SVG-bilder bevaras.

Inventeringen omfattar arbete, effekt, rörelseenergi, blandade energiuppgifter, tryck och vätsketryck i Fysik 1 samt multiplikations- och additionsprincipen, permutationer, kombinationer, kombinatorisk sannolikhet, binomialsatsen och lådprincipen i matf1. Den manuella fördjupningen och ändringarna är avgränsade till fynden nedan. Formatkontrollen omfattar båda hela bankerna; detta är inte ett påstående om att alla övriga beräkningar i bankerna har verifierats på nytt.

## Pedagogiska beslut

- En fråga ska ange vad som söks och innehålla de givna värden som behövs på det enskilda kortet.
- Skilj negativt bromsarbete från det positiva beloppet på energin som försvinner.
- Skilj tillförd och nyttig effekt samt medeleffekt och momentan effekt.
- Ange om ordningen spelar roll, om tecken får upprepas och om lag har namn. Bokstavskoder behöver inte vara riktiga ord.
- Facit ska först förklara den centrala idén och sedan visa den relevanta beräkningen. Exakt upprepad metodtext har kortats utan att beräkningen ändrats.
- Lådprincipen förklaras med personer, mappar eller tal i den aktuella situationen; onödiga bevis av maximalitet har tagits bort när frågan bara ber om en undre gräns.
- Träningsnivå bedöms per delkort. E/C/A och uppgifts-ID:n har bevarats.
- 1.435 och 1.541 har manuell komplettering: talet självrättas, men förklaringen ska också redovisas.

## Rättade svar

| Kort | Före | Efter |
|---|---:|---:|
| fy1 6.458c | 0.07976923076923077 | 0.07989973366755444 |
| fy1 5.591b | 2663.6225266362253 | 2664 |
| fy1 6.422b | 30947.046843177188 | 30549.898167006108 |
| fy1 5.493a | 4339.5 | -4339.5 |
| fy1 6.455b | 3615.5319038020925 | 3564.1547861507124 |
| fy1 5.511b | 136638.3744855967 | 136666.66666666666 |
| fy1 5.511c | 700.7096127466497 | 700.8547008547008 |
| fy1 5.495c | 596.6679842375655 | 600 |
| fy1 5.485b | 11.965829938900207 | 11.922708757637475 |
| fy1 5.494 | 12.403799999999999 | -12.403799999999999 |

Dessutom rättas mellanledet i 6.442a: 13 600 × 9,82 × 0,760 = 101 499,52 Pa. Maskinsvaret var redan rätt.

## Ändrade träningsnivåer

| Kort | Före | Efter |
|---|---:|---:|
| fy1 6.458c | 3 | 2 |
| fy1 6.455b | 3 | 2 |
| fy1 5.37a | 2 | 1 |
| fy1 5.511b | 3 | 2 |
| fy1 5.511c | 3 | 2 |
| fy1 5.495c | 3 | 1 |
| matf1 1.199 | 1 | 2 |
| matf1 1.627 | 1 | 2 |
| matf1 1.535 | 1 | 2 |
| matf1 1.143 | 1 | 2 |
| matf1 1.538 | 1 | 2 |
| matf1 1.633 | 1 | 2 |
| matf1 1.739b | 1 | 2 |
| matf1 1.396 | 3 | 2 |
| matf1 1.197 | 1 | 2 |
| matf1 1.780 | 4 | 3 |
| matf1 1.125a | 2 | 3 |
| matf1 1.617 | 5 | 3 |
| matf1 1.647c | 1 | 2 |
| matf1 1.198 | 1 | 2 |
| matf1 1.62 | 3 | 2 |
| matf1 1.616 | 4 | 3 |
| matf1 1.642 | 1 | 2 |
| matf1 1.641 | 4 | 3 |
| matf1 1.128 | 1 | 2 |
| matf1 1.64 | 4 | 3 |
| matf1 1.660a | 1 | 2 |
| matf1 1.65 | 4 | 2 |
| matf1 1.121 | 1 | 2 |
| matf1 1.626 | 3 | 1 |
| matf1 1.668b | 1 | 2 |

## Verifiering

- 112 oberoende beräkningskontroller av ändrade lösningar och givna mellanresultat; resultaten finns i JSON-filen intill rapporten.
- 65 tester i master och 59 i Kunskapsgymmet. Sju nya regressionstester kontrollerar energibalans, egna mellanvärden, helt antal vindkraftverk, fullständig uppräkning av lag och sannolikhetsutfall samt lådfördelningar och binomialpolynom.
- Långa uträkningar radbryts vid relevanta samband; fallen i 1.435 och 1.448 visas på egna rader för att gå att läsa på mobil.
- Faktisk självrättning i Chromium: korrekta enheter, negativa arbeten, heltalsgräns, bråk/procent och onamngivna lag. LaTeX-rendering och facitkontroll av alla kort från ändrade huvuduppgifter.
- Visuell kontroll av exempel i mobilformat och datorformat, inklusive fristående kort och lösningar.
- Giltig JavaScript/JSON, bevarad ID-ordning, oförändrade SVG-strängar, git diff --check och identiska bankkopior.
- Inga nya ERROR eller WARNING i bankkontrollen. Före/efter: Fysik 1 0/8, matf1 0/10; varningarna fanns sedan tidigare.

Körning: `node --test tools/energi-kombinatorik.test.js tools/deluppgifter.test.js tools/formatera-fysikfacit.test.js tools/granska-uppgifter.test.js tools/geometri-ma2.test.js tools/sparskydd.test.js`. I Kunskapsgymmet: `node --test tools/*.test.js`.

## Ändringslista per huvuduppgift

| Bank och ID | Område | Ändring |
|---|---|---|
| fy1 5.30 | effekt | 5.30a |
| fy1 5.37 | rorelseenergi | 5.37a |
| fy1 5.55 | rorelseenergi | 5.55a |
| fy1 5.151 | effekt | 5.151 |
| fy1 6.55 | tryck | 6.55a |
| fy1 5.190 | rorelseenergi | onödig bromstid borttagen |
| fy1 5.583 | effekt | 5.583: jämn acceleration behövs för maximal effekt |
| fy1 5.590 | effekt | 5.590a; 5.590b; 5.590c |
| fy1 5.591 | effekt | 5.591a; 5.591b |
| fy1 5.592 | effekt | 5.592a; 5.592b; 5.592c; 5.592d |
| fy1 5.598 | effekt | 5.598a; 5.598b; 5.598c |
| fy1 5.481 | rorelseenergi | 5.481a |
| fy1 5.483 | rorelseenergi | 5.483a |
| fy1 5.485 | rorelseenergi | 5.485b |
| fy1 5.486 | rorelseenergi | 5.486: start från vila och trissmodell angivna |
| fy1 5.488 | rorelseenergi | 5.488a; 5.488b; 5.488c; 5.488d |
| fy1 5.493 | rorelseenergi | 5.493a; 5.493b |
| fy1 5.494 | rorelseenergi | 5.494 |
| fy1 5.495 | rorelseenergi | 5.495c |
| fy1 5.503 | rorelseenergi | 5.503b |
| fy1 5.505 | rorelseenergi | 5.505b; 5.505c |
| fy1 5.509 | rorelseenergi | 5.509a; 5.509c; 5.509d |
| fy1 5.511 | rorelseenergi | 5.511b; 5.511c |
| fy1 5.513 | rorelseenergi | 5.513a; 5.513b |
| fy1 5.517 | rorelseenergi | 5.517a |
| fy1 5.548 | rorelseenergi | 5.548a; 5.548b |
| fy1 5.549 | rorelseenergi | 5.549: medeleffekt skiljs från konstant momentan effekt |
| fy1 6.421 | tryck | 6.421a; 6.421b |
| fy1 6.422 | tryck | 6.422b |
| fy1 6.424 | tryck | 6.424b |
| fy1 6.431 | tryck | 6.431 |
| fy1 6.435 | tryck | 6.435 |
| fy1 6.440 | vatsketryck | 6.440b |
| fy1 6.442 | vatsketryck | 6.442a: rättat felräknat mellanled |
| fy1 6.443 | vatsketryck | 6.443a |
| fy1 6.455 | vatsketryck | 6.455b |
| fy1 6.458 | vatsketryck | 6.458c; 6.458a; 6.458b |
| fy1 5.502 | arbete | 5.502 |
| fy1 5.520 | arbete | 5.520b; 5.520c; 5.520d |
| fy1 5.525 | arbete | 5.525a |
| fy1 5.527 | arbete | 5.527b |
| fy1 5.528 | arbete | 5.528c |
| fy1 5.535 | arbete | 5.535b |
| matf1 1.37 | mult_add_principen | 1.37 |
| matf1 1.60 | ladprincipen | 1.60 |
| matf1 1.62 | ladprincipen | 1.62 |
| matf1 1.64 | ladprincipen | 1.64 |
| matf1 1.65 | ladprincipen | 1.65 |
| matf1 1.68 | ladprincipen | 1.68 |
| matf1 1.133 | ladprincipen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.134 | ladprincipen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.135 | ladprincipen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.150 | ladprincipen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.151 | ladprincipen | kortat exakt upprepad metodtext; beräkningen bevarad; 1.151: tydligare vad som ska visas |
| matf1 1.39 | mult_add_principen | 1.39 |
| matf1 1.53 | mult_add_principen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.393 | ladprincipen | 1.393 |
| matf1 1.130 | mult_add_principen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.131 | mult_add_principen | 1.131 |
| matf1 1.396 | ladprincipen | 1.396 |
| matf1 1.132 | mult_add_principen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.148 | mult_add_principen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.149 | mult_add_principen | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.75 | permutationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.121 | permutationer | 1.121: bokstavsordningar, inte ordboksord; 1.121 |
| matf1 1.466 | kombinationer | 1.466 |
| matf1 1.125 | kombinationer | 1.125a; 1.125b; kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.156 | kombinationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.188 | permutationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.189 | permutationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.191 | permutationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.192 | permutationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.211 | kombinationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.214 | kombinationer | 1.214 |
| matf1 1.215 | kombinationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.218 | permutationer | 1.218: bokstavsordningar, inte ordboksord |
| matf1 1.222 | permutationer | 1.222 |
| matf1 1.223 | permutationer | 1.223 |
| matf1 1.301 | kombinationer | 1.301 |
| matf1 1.302 | kombinationer | 1.302 |
| matf1 1.143 | binomialsatsen | 1.143 |
| matf1 1.435 | kombinatorik_sannolikhet | 1.435; resonemanget bedöms manuellt; självrättningen gäller talet |
| matf1 1.128 | kombinatorik_sannolikhet | 1.128 |
| matf1 1.448 | kombinatorik_sannolikhet | 1.448 |
| matf1 1.197 | kombinatorik_sannolikhet | 1.197 |
| matf1 1.198 | kombinatorik_sannolikhet | 1.198 |
| matf1 1.199 | kombinatorik_sannolikhet | 1.199 |
| matf1 1.200 | kombinatorik_sannolikhet | 1.200 |
| matf1 1.504 | ladprincipen | 1.504 |
| matf1 1.505 | ladprincipen | 1.505 |
| matf1 1.507 | ladprincipen | 1.507 |
| matf1 1.508 | ladprincipen | 1.508 |
| matf1 1.515 | permutationer | 1.515: bokstavsordningar, inte ordboksord |
| matf1 1.516 | permutationer | 1.516: bokstavsordningar, inte ordboksord |
| matf1 1.517 | permutationer | 1.517: bokstavsordningar, inte ordboksord |
| matf1 1.533 | binomialsatsen | 1.533 |
| matf1 1.534 | binomialsatsen | 1.534 |
| matf1 1.535 | binomialsatsen | 1.535 |
| matf1 1.538 | binomialsatsen | 1.538 |
| matf1 1.540 | binomialsatsen | 1.540 |
| matf1 1.541 | binomialsatsen | resonemanget bedöms manuellt; självrättningen gäller talet; 1.541: tydlig skillnad mellan talet och förklaringen |
| matf1 1.543 | binomialsatsen | 1.543 |
| matf1 1.545 | binomialsatsen | 1.545 |
| matf1 1.547 | binomialsatsen | 1.547 |
| matf1 1.549 | kombinatorik_sannolikhet | språk: antal kronor/ettor |
| matf1 1.550 | kombinatorik_sannolikhet | språk: antal kronor/ettor |
| matf1 1.552 | kombinatorik_sannolikhet | språk: antal kronor/ettor |
| matf1 1.557 | kombinatorik_sannolikhet | språk: antal kronor/ettor |
| matf1 1.558 | kombinatorik_sannolikhet | 1.558 |
| matf1 1.559 | kombinatorik_sannolikhet | språk: antal kronor/ettor |
| matf1 1.633 | kombinatorik_sannolikhet | 1.633 |
| matf1 1.696 | kombinatorik_sannolikhet | 1.696c: antal i stället för sannolikhetsformat |
| matf1 1.708 | kombinatorik_sannolikhet | 1.708c: antal i stället för sannolikhetsformat; 1.708d: antal i stället för sannolikhetsformat |
| matf1 1.711 | kombinatorik_sannolikhet | 1.711 |
| matf1 1.725 | kombinatorik_sannolikhet | 1.725b: antal i stället för sannolikhetsformat |
| matf1 1.728 | kombinatorik_sannolikhet | 1.728c: antal i stället för sannolikhetsformat |
| matf1 1.578 | mult_add_principen | 1.578: bokstavskoder i huvudfråga och delkort |
| matf1 1.579 | mult_add_principen | 1.579: bokstavskoder i huvudfråga och delkort |
| matf1 1.580 | mult_add_principen | 1.580: tydligt om tillåtna siffror och upprepning |
| matf1 1.583 | mult_add_principen | 1.583: tydligt om tillåtna siffror och upprepning |
| matf1 1.584 | mult_add_principen | 1.584: tydligt om tillåtna siffror och upprepning |
| matf1 1.616 | mult_add_principen | 1.616 |
| matf1 1.626 | mult_add_principen | 1.626 |
| matf1 1.627 | mult_add_principen | 1.627 |
| matf1 1.641 | mult_add_principen | 1.641 |
| matf1 1.735 | mult_add_principen | 1.735: tydligt om tillåtna siffror och upprepning |
| matf1 1.736 | mult_add_principen | 1.736: tydligt om tillåtna siffror och upprepning |
| matf1 1.745 | mult_add_principen | 1.745: tydligt om tillåtna siffror och upprepning |
| matf1 1.589 | permutationer | 1.589: bokstavskoder i huvudfråga och delkort |
| matf1 1.590 | permutationer | 1.590: bokstavskoder i huvudfråga och delkort |
| matf1 1.591 | permutationer | 1.591: bokstavskoder i huvudfråga och delkort |
| matf1 1.663 | permutationer | 1.663: bokstavskoder i huvudfråga och delkort |
| matf1 1.668 | permutationer | 1.668b |
| matf1 1.669 | permutationer | 1.669a |
| matf1 1.739 | permutationer | 1.739: bokstavskoder i huvudfråga och delkort; 1.739b; 1.739c; 1.739d |
| matf1 1.740 | permutationer | 1.740: bokstavskoder i huvudfråga och delkort; 1.740a; 1.740b; 1.740c |
| matf1 1.742 | permutationer | 1.742 |
| matf1 1.596 | kombinationer | 1.596 |
| matf1 1.597 | kombinationer | 1.597 |
| matf1 1.598 | kombinationer | 1.598 |
| matf1 1.599 | kombinationer | 1.599 |
| matf1 1.600 | kombinationer | 1.600 |
| matf1 1.601 | kombinationer | 1.601 |
| matf1 1.618 | kombinationer | kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.642 | kombinationer | 1.642 |
| matf1 1.643 | kombinationer | 1.643b |
| matf1 1.644 | kombinationer | 1.644b; 1.644c |
| matf1 1.647 | kombinationer | 1.647c |
| matf1 1.652 | kombinationer | 1.652b; 1.652c; 1.652d |
| matf1 1.654 | kombinationer | 1.654a; 1.654b; 1.654d |
| matf1 1.657 | kombinationer | 1.657c; kortat exakt upprepad metodtext; beräkningen bevarad |
| matf1 1.659 | kombinationer | 1.659a; 1.659c |
| matf1 1.660 | kombinationer | 1.660a |
| matf1 1.661 | kombinationer | 1.661b; 1.661c; 1.661d |
| matf1 1.617 | ladprincipen | 1.617 |
| matf1 1.780 | ladprincipen | 1.780 |
