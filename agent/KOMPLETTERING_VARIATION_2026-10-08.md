# Genomförd komplettering: variation och enkla ingångar

2026-10-08. Genomför rekommendationerna i
[Variation och luckor](VARIATION_OCH_LUCKOR_2026-10-08.md).
Grafteori ingår inte längre i matf1 och ska inte läggas till. Detta är nu
uttryckligen dokumenterat i CLAUDE.md och båda strukturfilernas kommentarer.

## Nya uppgifter

44 fristående uppgifter: 34 i Fysik 1 och 10 i matf1. De ger andra
representationer och metodval, snarare än fler talvarianter av samma formel.
Alla är E-uppgifter: 23 på träningsnivå 1 och 21 på nivå 2.
35 uppgifter har en egen SVG-figur. 31 har numeriska svar och 13 har
strukturerade svarsalternativ med ett rätt alternativ. Alternativen blandas
av appen. Varje lösning förklarar den avgörande principen och visar bara de
beräkningar som behövs.

| Område | Antal | ID | Vad som tillkommer |
| --- | ---: | --- | --- |
| Impuls och medelkraft | 8 | 5.601–5.608 | Rektangel, triangel, två kraftnivåer, medelkraft, motsatta kraftriktningar, slutfart och längre stopp. Jämförelser prövar area snarare än toppkraft. |
| Rörelseenergi och energiprincipen | 10 | 5.609–5.618 | Massa respektive fart, energistaplar, fall med angiven nollnivå, friktion, bromsning, energiflöde och fart från en mätning. |
| Arbete | 4 | 5.619–5.622 | Negativt arbete, lika arbete med olika kraftgrafer, vinkelrät kraft och arbete i ett uttryckligen avgränsat intervall. |
| Tryck | 8 | 6.549–6.556 | Samma kloss på olika sidor, total kontaktyta för två fötter, snösko, staplade klossar, kraft, area och hydraulik. |
| Newtons tredje lag | 4 | 4.754–4.757 | Pilar på två olika föremål, lika stora motkrafter, varför krafterna inte tar ut varandra på en vagn, och acceleration vid olika massor. |
| Kombinatorik | 10 | 1.792–1.801 | Grupp kontra roller, dubbelräkning, kod med/utan upprepning, addition kontra multiplikation, valtabell, en bestämd person och sannolikhet utan återläggning. |

Nivå 1 använder direkt avläsning, ett enkelt samband eller ett grundläggande
metodval. Nivå 2 innehåller bland annat grafareor, energiförluster,
kvadrerade fartförhållanden, enhetsomvandling eller flera beroende steg.
#5.611, ett direkt avläst energivärde följt av en subtraktion, är nivå 1.

## Reviderade seriekopplingsuppgifter

De två utpekade nivåglappen kontrollerades även med sina faktiska delkort.

- **8.40 a–d:** nivåerna är nu 1, 2, 2, 1. a summerar två resistanser.
  b har den givna totalresistansen och omvandlar strömmen till mA. c har
  given ström och beräknar båda effekterna. Dess slutsvar anger nu både
  0,088 W och 0,132 W. d får egna batteridata och ett numeriskt slutsvar
  0,220 W; tidigare stod bara uttrycket P₁ + P₂ i delens slutsvar.
- **8.124 a–c:** nivåerna är 1, 1, 1. a frågar uttryckligen efter
  kopplingens namn med ett ord. b summerar resistanserna. c ger
  totalresistansen direkt och frågar i A, samma enhet som svarsfältet.
- Båda huvuduppgifterna och deras facit följer delarna. E-bedömning och
  poäng har anpassats till de enkla rutinfrågorna. De ursprungliga
  kretsfigurerna och numeriska svarsvärdena har bevarats.
- De fem numeriska delkorten har enkla exakta svar. Toleransen är därför
  0; en avvikande resistans såsom 551 Ω ska inte godtas för 220 + 330 Ω.
  Identifieringen i 8.124a och tvåeffektsfrågan i 8.40c behåller manuell
  bedömning, med tydliga facit. De är inte automatiskt rättade kort.

Övriga befintliga uppgiftsobjekt är identiska med utgångsversionen.
Inga befintliga ID:n har tagits bort. Bankerna innehåller nu 3715
fysikuppgifter och 1541 matf1-uppgifter.

## Verifiering

- 74 tester i Uppgiftslabbet och 62 i Kunskapsgymmet passerar. Nio nya
  innehållstester integrerar de faktiskt ritade graferna, räknar energier
  och tryck oberoende samt räknar upp grupper, koder och kuldragningar.
- Chromium: 44 nya huvuduppgifter och samtliga sju reviderade delkort
  kontrollerade med appens verkliga delning och facitkontroll.
- Alla 57 matematikuttryck i de nya uppgifterna och alla formler i de
  reviderade korten renderas utan KaTeX-fel.
- 148 accepterade/avvisade svar passerar verklig svarskontroll. Det
  inkluderar samtliga alternativs rätta, felaktiga och kombinerade val,
  enheter N·s/Ns/N s/kg m/s, fel enhet N, negativa arbeten, ström i A/mA
  samt sannolikhet som bråk, decimal och procent.
- Alla 35 nya SVG-figurer har kontrollerats visuellt och med
  tools/granska-svg.js i Chromium: inga geometrifynd. Grafareor och
  värden på axlar har dessutom kontrollerats oberoende av facit.
- Alla nya kort har renderats vid 1280 och 390 px utan sidöverflöde.
  Utvalda mobila frågor, lösningar och alla sju reviderade delkort har
  granskats visuellt. Jämförelsernas två uträkningar står på var sin rad.
- Full bankvalidator: fy1 har fortfarande 0 ERROR, 8 WARNING, 655 INFO;
  matf1 har fortfarande 0 ERROR, 8 WARNING, 71 INFO. Inga nya fynd.
- JavaScript-syntax, git diff --check och identiska bankkopior kontrollerade.
  Kunskapsgymmets BANK_VERSION är uppdaterad.

Verifieringssammanställningen finns i
[KOMPLETTERING_VARIATION_2026-10-08.json](KOMPLETTERING_VARIATION_2026-10-08.json).
Detta verifierar ändringarna, inte samtliga oförändrade uppgifter i banken.
