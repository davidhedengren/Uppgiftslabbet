# Ma2 kap 4 (statistik): revision med figurer, varierade texter och facit med rubriker, 2026-10-27

Användaren bad om samma revision som i kapitel 3: figurer, varierade texter och facit med rubriker.

## Inventering

Kapitlet har 597 kort i nio områden. 448 facit saknade rubriker per steg:

- 278 hade steglista och svar men inga rubriker;
- 135 var löpande text utan steg;
- 35 hade steglista utan svarsrad.

Dessutom saknade 109 delkort rubriker i sina facit.

Revisionen görs område för område:

| Etapp | Område | Kort | Figurer |
|---|---|---|---|
| 1 | lagesmatt | 72 | 4 |
| 2 | kvartiler_percentiler | 59 | 13 |
| 3 | ladagram | 75 | 49 |
| 4 | standardavvikelse | 97 | 21 |
| 5 | normalfordelat_material | 74 | 53 |
| 6 | normalfordelning_digitala_verktyg | 56 | 35 |
| 7 | linjar_regression | 55 | 6 |
| 8 | korrelation_koefficient | 59 | 18 |
| 9 | tabeller_diagram | 51 | 23 |

## Ändrat beslut: steglista i statistikfacit

`ma2-statistik-matt.test.js` och `ma2-statistik-referenser.test.js` (2026-10-13) krävde att facit för de 30 och 60 statistikkort som skapades då saknade steglista. Det kravet är ersatt av grundinställningen från 2026-10-23/25 (Ma1 #1.116): steg med en rubrik per steg, mellanled och svarsrad.

Testerna kräver nu i stället en rubrik per steg och ett svar när facit har en steglista. Övriga kontroller i testerna är oförändrade, till exempel data, Sx, toleranser och delkortens svarsfält.

## Etapp 1: lägesmått (61 kort)

**Figurer**

De fyra figurerna kontrollerades mot data och stämmer:

- 4.317: prickdiagram med medianen 5;
- 4.321: histogram med staplarna 3, 4 och 3;
- 4.323: stapeldiagram, 5 mål på 6 matcher;
- 4.326: stapeldiagram, summan 455 för 12 personer.

Ingen figur behövde ändras.

**Facit**

- Alla 61 kort har facit med en rubrik per steg och svarsrad. Det gäller 59 kort utan rubriker, 4.373, 4.46 och 6.18. 6.18 ligger i kap 4 trots sitt ID.
- Rubrikerna är skrivna för varje kort, till exempel ”Fredagen står för det som fattas” och ”Tre av fem värden i B är högst 50”.
- Hjälpfunktionerna bygger bara beräkningarna. Rubrikerna skickas in per kort, och testet underkänner rubriker som återanvänds mellan kort.
- Delkorten i 14 kort har fått eget facit med rubriker och egen ledtråd.

**Texter i mallfamiljerna**

- **Saknat värde ur medelvärdet:** nio nästan identiska kort har fått olika sammanhang, med samma tal och svar.
  - 4.25: kanelbullar;
  - 4.60: temperatur;
  - 4.85: svampar;
  - 4.111: suddat tal på tavlan;
  - 4.112: basket;
  - 4.200: frågespel;
  - 4.101: ”vilket tal ska läggas till”;
  - 4.205: planta;
  - 4.74 är kvar som ren x-uppgift.
- **Gemensamt medelvärde för två grupper:**
  - 4.31: löparklubb;
  - 4.55: semesterdagar;
  - 4.206: frågespel;
  - 4.77: rektorn tar medelvärdet av klassernas medelvärden, och eleven ska rätta det.
- **Övriga kort:**
  - 4.76 och 4.91 har fått nya sammanhang: ryggsäckar och taxiresor.
  - 4.119 handlar om en målvakt, så att den inte längre liknar 4.17.
  - 4.30 handlar om en lärares exempelresultat, så att den inte längre liknar 4.23.
  - 4.203 handlar om paket och 4.204 om att stå på ett ben.
  - 4.41 handlar om lästid.
  - 4.01 har fått bättre språk.

**Rättat innehåll**

- **4.16:** motexemplets jämförelse var otydlig. Facit visar nu att tre av fem värden i B är högst 50, medan tre av fem i A är minst 50.
- **Ledtrådar:** generiska ledtrådar, som ”Ordna värdena när det behövs …” och ”Vilken information i tabellen …”, är ersatta med specifika. Ledtrådarna i 4.17, 4.60 och 4.74 gav insatta värden eller hela uträkningen och är omskrivna.
- **Flerval:** alla alternativ i 4.244, 4.375 och 6.18 har kommentarer.
- **4.322–4.325:** facit visar nu ”= 4” och inte ”≈ 4,00” när medelvärdet är ett heltal.

## Kontroll

- Facit och ledtråd för alla 61 kort renderades med KaTeX och lästes igenom.
- **Självrättning i Kunskapsgymmet:**
  - 4.31, 4.204 och 4.101 godtar rätt svar och avvisar fel.
  - 4.41 rättas del för del: 9 och 9 ger rätt på båda, 9 och 8 ger rätt och fel.
  - I 4.244 visar fel alternativ sin kommentar.
- **Validatorn:** Ma2 ger 99 fynd mot 103 före ändringen, eftersom fyra nästan lika texter försvann.
- **Test:** `tools/ma2-kap4-lagesmatt-2026-10-27.test.js`. Alla Ma2-tester går igenom (151/151).
