# Fy1: kopplingsscheman och variation i serie- och parallellkoppling (2026-11-02)

Lärarens önskemål:

- fler kopplingsscheman och större variation i serie- och parallellkoppling;
- en genomgång om resistans i ledare, med förklaring av enheterna (m² med ρ i Ω·m, mm² när faktorn 10⁻⁶ stryks ur resistiviteten, alltså ρ i Ω·mm²/m).

Samma dag beslutades också att effekt inte ska förekomma i serie- och parallellkopplingskorten, eftersom effekt gås igenom senare. Se commit 106d540: 20 effektkort flyttades till `kopplingar` och effektdelkort fick `spel:false`.

## Nya kort 8.684–8.726 (43 st)

| Område | Kort | Nivå 1 | Nivå 2 | Nivå 3 |
|---|---:|---:|---:|---:|
| seriekoppling | 23 | 9 | 9 | 5 |
| parallellkoppling | 20 | 7 | 7 | 6 |

Variation, utöver de vanliga resistorkretsarna:

- **Sammanhang:** ficklampa, ljusslinga, LDR, lysdiod med förkopplingsresistor och USB, reglerbar resistor, taklampa, husvagn med 12 V och säkring, hemmets elnät.
- **Mätare:** två amperemetrar i samma slinga, voltmetrar över olika delar (även två överlappande, en ovanför och en under kretsen), voltmeter som egen gren, amperemetrar i grenar och i huvudledningen.
- **Brytare:** öppen brytare i serie (spänningen över brytaren), i en gren (L₁ påverkas inte), och en brytare som sluts (ökning av huvudströmmen).
- **Fel i kretsen:** lampa skruvas ur, kortsluten lampa (orange ledning), felsökning med voltmeter.
- **Representationer:** schema, tabell med mätvärden, förgreningsfigur med strömpilar, anslutningspunkter A–B, markerade punkter P/Q/R.
- **Svarsformer:** numeriskt, två delar, flerval med kommentar till varje felaktigt alternativ, antal.

Alla 43 kort har ledtråd och sammanhängande fysikfacit. Ingen fråga handlar om effekt eller energi. Värden med fler än två värdesiffror har `svarVardesiffror: 2` och oavrundat `rättSvar`. Inga facit krockar med andra facit i samma område. På nivå 1–2 visas batteriets spänning bara när den behövs (annars "U").

## Kopplingsscheman i 17 äldre kort

8.361, 8.363, 8.365, 8.369, 8.392 (serie) samt 8.362, 8.364, 8.366, 8.367, 8.368, 8.642, 8.643, 8.644, 8.645, 8.672, 8.673 och 8.676 (parallell). Bara `t` ändrades; figuren står efter första stycket. Figurerna visar inga tal som ger bort svaret. 8.646 och 8.677 fick ingen figur, eftersom ett schema inte hjälper där.

## Genomgång (Kunskapsgymmet `typuppgifter-fy1.js`)

`fy1-grund-8-06r`, "Resistans i en ledare", ligger i området `kretsar` efter "Ohms lag" och tränar familjen "Resistivitet och ledarresistans". Den räknar samma koppartråd på två sätt:

1. ρ = 1,7·10⁻⁸ Ω·m med A i m²;
2. 1,7·10⁻⁸ = 0,017·10⁻⁶, alltså ρ = 0,017 Ω·mm²/m med A direkt i mm².

Steget "Blanda inte de två sätten" förklarar att faktorn 10⁻⁶ ska finnas på ett ställe. Med ρ i Ω·m och A i mm² blir svaret en miljon gånger för litet.

## Kontroller

- `node --check` på banken och `typuppgifter-fy1.js`.
- Validatorn har inga fynd för de nya ID:na.
- SVG-granskaren har 0 fynd i 41 + 17 figurer.
- Kretsar: en SVG-bana per sammanhängande ledning, inga ledningar förbi komponenter, prickar i noderna. Amperemetrar i serie, voltmetrar parallellt. Lysdioden ritas i framriktningen från batteriets pluspol.
- Facit och ledtrådar har renderats och lästs.
- Självrättningen är provad i Kunskapsgymmet med `delSvarRatt`, 31 fall. Exempel: 8.693 godtar 5,3, 5,28 och 5,28 V men inte 5,2. 8.702 godtar 17, 16,7 och 0,017 A men inte 16. 8.721 godtar 67 och 66,7 men inte 66.
- Antal kort i Kunskapsgymmet: seriekoppling 51 → 74, parallellkoppling 83 → 103.
- Test: `tools/fysik1-kopplingsscheman-2026-11-02.test.js` (antal, nivåer, figurer, ingen effekt, oberoende facit, inga facitkrockar). Kretstesterna, multimeter-, omgång 8/11- och nivå 3-testerna går också igenom.

Byggskripten (`krets.py`, `bygg_koppl.py`, `figtill_koppl.py`) ligger i sessionens scratchpad. `krets.py` innehåller mallarna `serie`, `parallell`, `serie_poler`, `parallell_poler` och `forgrening`.
