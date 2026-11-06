# Ma1 kapitel 1 (algebra): mängdträning 2026-11-06

Uppdrag: ”fortsätt leta efter områden och svårighetsgrader som saknar uppgifter.”

## Kartläggning

Jag räknade Kunskapsgymmet-kort per område och träningsnivå i Ma1 och Ma2, där varje delkort räknas för sig. Skriptet ligger i scratchpad och följer samma logik som `expandGameTask`.

- **Ma1 kapitel 1 (algebra)** undervisas just nu enligt Planering Ma1a 2627 (v. 42–48: uttryck, ekvationer, multiplikation av uttryck, faktorisering, formler och mönster). Kapitlet hade få kort, särskilt på nivå 3:

  | Område | Nivå 1 | Nivå 2 | Nivå 3 |
  |---|---:|---:|---:|
  | `algebraiska_uttryck` | 20 | 15 | 4 |
  | `linjara_ekvationer` | 20 | 14 | 9 |
  | `ekv_flera_variabeltermer` | 24 | 12 | 5 |
  | `ekv_parenteser` | 25 | 15 | 12 |
  | `formler` | 22 | 22 | 7 |
  | `multiplicera_uttryck` | 15 | 43 | 12 |
  | `monster_samband` | 11 | 14 | 10 |

- **Ma2** har flera tunna områden i kapitel 2, med 18–25 kort på nivå 1–2. Ma2c-klassen repeterar nu inför NP, och Ma3c kapitel 1 fylls på i en annan session.

Jag började därför med det som undervisas nu: Ma1 kapitel 1.

## Levererat: 52 uppgifter, 120 kort (#1.1623–1.1674)

Uppgifterna följer samma upplägg som kapitel 0 (`MA1_KAP0_MANGDTRANING_2026-11-06.md`). Det är vanliga uppgifter utan textproblem. Antalet delar varierar: 14 uppgifter har en del, 17 har två, 12 har tre och 9 har fyra. Svårigheten ökar från a) till d), och varje delkort har en egen `traningsniva`. Över alla kort är 30 på nivå 1, 51 på nivå 2, 36 på nivå 3 och 3 på nivå 4.

| ID | Område (familj) | Innehåll | Kort (nivå 1/2/3/4) |
|---|---|---|---|
| 1.1623–1.1630 | linjara_ekvationer (Lösa enkla ekvationer) | x+7=12 … \(11-\frac{3x}{4}=2\), även x i högerledet och andra bokstäver | 7/9/3/1 |
| 1.1631–1.1637 | ekv_flera_variabeltermer | x-termer i båda leden, också med termer att samla först | 2/8/5 |
| 1.1638–1.1644 | ekv_parenteser (Ekvationer med parenteser, Minustecken framför parentes) | en eller två parenteser, minustecken och negativ faktor framför parentes | 2/8/6 |
| 1.1645–1.1652 | forenkla_uttryck (Förenkla uttryck, Uttryck med parenteser) | samla termer, x²-termer, plus- och minusparenteser | 5/9/6 |
| 1.1653–1.1660 | multiplicera_uttryck (Multiplicera in i en parentes, Multiplicera två parenteser) | k(…), −(…), x(…), 2x(…), (x+a)(x+b), (2x+1)(x+3) | 4/5/8/2 |
| 1.1661–1.1667 | algebraiska_uttryck (Värdet av ett uttryck) | insättning med negativa tal, potenser, två variabler och bråkstreck | 5/5/5 |
| 1.1668–1.1674 | formler (Beräkningar med formler) | P=2l+2b, A=bh/2, s=vt, K=45+12n, F=1,8C+32, y=3x−7, V=lbh. Både framåträkning och att lösa ut en annan storhet. | 5/7/3 |

Antal kort på nivå 1–2 efter påfyllnaden: `algebraiska_uttryck` 45, `ekv_flera_variabeltermer` 46, `linjara_ekvationer` 50, `ekv_parenteser` 50, `formler` 56, `multiplicera_uttryck` 67.

### Facit och ledtrådar

- **Ekvationer** löses med ett steg per operation, och rubriken anger uppgiftens egna tal eller termer, till exempel:
  - ”Multiplicera in \(3\) i parentesen: \(3(x-4)=3x-12\)”;
  - ”Ta bort parenteserna: multiplicera in \(5\) och byt tecken i \((3a+4)\)”;
  - ”Vänster led: samla x-termerna: \(4x-3x=x\) och talen: \(8+3=11\)”;
  - ”Subtrahera \(3x\) från båda leden”;
  - ”Dividera båda leden med −2”.

  x-termerna samlas i det led där koefficienten blir positiv. Varje ekvationsfacit avslutas med en kontroll där VL och HL räknas med lösningen insatt.
- **Förenkling** visar först varje parentes som tas bort och sedan vilka termer som samlas.
- **Två parenteser** visar alla fyra produkterna, till exempel \(x\cdot x+x\cdot 3+2\cdot x+2\cdot 3\). Uträkningen står på tre rader, eftersom den annars blir för bred på mobil.
- **Värdet av ett uttryck** börjar med ”Sätt in \(x=-2\)”. Därefter räknar kapitel 0-motorn steg för steg i rätt räkneordning. Bråkstreck visas som bråk med stegen ”Räkna ut täljaren” och ”Räkna ut nämnaren”.
- **Formler** börjar med att de kända värdena sätts in, med mellanled (till exempel \(120=5\cdot4\cdot h\) och sedan \(120=20h\)). Därefter löses ekvationen. Decimaltal visas med decimalkomma, till exempel 5,5 och 7,5.
- **Ledtrådarna** pekar på första steget i just den deluppgiften, till exempel:
  - ”Börja med att multiplicera in \(3\) i parentesen.”;
  - ”Det finns x-termer i båda leden …”;
  - ”Varje term i den första parentesen ska multipliceras med varje term i den andra.”;
  - ”Byt bokstaven mot talet. Vilken räkneoperation ska göras först: multiplikation eller subtraktion?”.

### Beslut

- **Svarsformat:** `numeriskt` för ekvationer, värden och formler. ”x = 5” och ”5” godtas båda. För förenkling och multiplikation används `förenklat_polynom`, som godtar termerna i valfri ordning men underkänner oförenklade svar som ”7(x−4)”.
- **Faktorisering** ingår inte i omgången. Kunskapsgymmet saknar ett format som kräver att *största* gemensamma faktor bryts ut i ett enda svarsfält, eftersom `faktoriserat` godtar 2(6x²+9x). Befintliga Ma1-uppgifter använder två fält (faktor och parentes). Mängdträning i faktorisering tas i en egen omgång.
- **Mönster** (`monster_samband`, 35 kort på nivå 1–2) behöver figurserier och tas också separat.
- **Miniräknare** är avstängd. Talen är valda för huvudräkning, och det som tränas är den algebraiska proceduren.
- **Inga figurer.** Rena uttryck och ekvationer blir inte tydligare av en bild.
- **Ändring i kapitel 0-motorn:** `del_uttryck(..., brakstreck=True)` skriver division som bråkstreck och ger stegen rubriken ”Räkna ut täljaren/nämnaren”. Standardläget är oförändrat, och kapitel 0-testet går igenom.

## Verifiering

- Byggskriptet `tools/bygg-ma1-kap1-mangdtraning-2026-11-06.py` kontrollerar varje svar med sympy. Ekvationernas lösning och kontrollens VL = HL kontrolleras med exakta bråk.
- Regressionstestet `tools/ma1-kap1-mangdtraning-2026-11-06.test.js` räknar om alla 120 svar direkt ur den fråga eleven ser, utan att använda byggaren:
  - ekvationer och formler löses som linjära funktioner;
  - polynomsvar jämförs med frågan för sex x-värden och kontrolleras för att vara förenklade.

  Testet kontrollerar också stigande nivåer, att rubrikerna innehåller uppgiftens tal och att kontrollen avslutar varje ekvationsfacit.
- Kunskapsgymmets `tools/ma1-kap1-mangdtraning-2026-11-06.test.js` använder appens riktiga `expandGameTask` och `delSvarRatt`. Facit, ”x = …” och polynom i omvänd ordning godtas. Fel värde, fel tecken, fel koefficient och oförenklat uttryck underkänns.
- I headless Chrome gav appens `kvFacit` 0 fel på 52 uppgifter och 120 kort.
- Allt renderades med MathJax i 390 px bredd. Långa rader delades så att den bredaste formeln blev 282 px. Facit har lästs i sin helhet, och 1.1660 granskades även i skärmbild.
- Validatorn ger 0 ERROR och 0 nya WARNING. Den ger en INFO om liknande textmall (1.1637 mot 1.207 och 1.1059), vilket är väntat för mängdträning.
