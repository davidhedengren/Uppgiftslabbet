# Ma1 faktorisering: nytt svarsformat `största_faktor` och mängdträning, 2026-11-06

Användaren: ”Kanske ett nytt svarsformat eller liknande? för det är ju viktigt att de kan bryta ut största
möjliga faktor, jag tror vi har jobbat med det i en annan session nyss för ma3. kanske går det nu?”

## Bakgrund

- Ma3c-sessionen samma dag byggde `förkortat_uttryck`. Det formatet kontrollerar att ett **bråk** är förkortat, inte att en faktor är utbruten.
- Det befintliga formatet `faktoriserat` (Ma2) kräver bara en produkt med rätt gradtal. Därför godtogs 2(6x²+9x) för 6x²+9x.
- Ma1:s äldre faktoriseringsuppgifter använder två svarsfält, ett för faktorn och ett för parentesen. Det fungerar inte för mängdträning med a)–d).

## Nytt format i Kunskapsgymmet: `största_faktor`

Formatet finns i `index.html` som `storstaFaktorRatt`, med aliaset `storsta_faktor`. Svaret godtas när:

1. det är algebraiskt lika med facit;
2. det är en produkt och inte en summa på toppnivå;
3. varje parentesfaktor saknar gemensam faktor, det vill säga heltalskoefficienterna har största gemensamma delare 1 och ingen variabel finns i alla termer;
4. övriga faktorer är tal, bokstäver eller potenser, utan decimaltal eller division.

| Exempel (facit 6x²+9x om inget annat anges) | Godtas? |
|---|---|
| 3x(2x+3), (2x+3)·3x, 3 · x · (2x + 3) | ja |
| 2x^(2)(2x−1) (potensknappen, facit 4x³−2x²) | ja |
| −3(2x+3) och 3(−2x−3) (facit −6x−9) | ja |
| 3ab(2+3a) (facit 6ab+9a²b) | ja |
| 3(2x²+3x), x(6x+9) | nej |
| 2(4x+6) (facit 8x+12) | nej |
| 6x²+9x, (6x²+9x) | nej |
| 6(x+1,5) (facit 6x+9) | nej |
| 3a(2b+3ab) | nej |

Formatet finns också i listan över format som rättas direkt med `formatRatt`, så att inga generella genvägar godtar ett algebraiskt likvärdigt men ofaktoriserat svar. Det finns även i `parentesSaknas`, som varnar för en saknad parentes.

Självtest: `KG_TEST_STORSTA_FAKTOR()` med 20 fall. `KG_TEST_MA4_SVAR()` och `KG_TEST_ANSWER_CHECKER()` ger fortfarande `true`. Formatet gäller bara uppgifter som anger det.

## Mängdträning: 20 uppgifter, 42 kort (#1.1685–1.1704)

Område `faktorisering`. Antalet delar varierar: 7 uppgifter har en del, 7 har två, 3 har tre och 3 har fyra. Svårigheten ökar från a) till d), och varje del har en egen träningsnivå.

- **Bryt ut största gemensamma faktor**, i stigande svårighet:
  - talfaktor: 5x+15, 12−8x;
  - variabel: x²+5x;
  - båda: 6x²+9x, 15x³+10x²;
  - tre termer: 4x³−6x²+2x, 18x²−12x+6;
  - negativ faktor: −4x−8, −6x²−9x.
- **Flera variabler och potenser**: 6ab+9a, 4xy−8x²y, 10a²b+15ab², 12x²y³−18xy², 9a³b²−6a²b och ab+ab².

Facit följer FACITMALL:

1. ”Största gemensamma faktorn till talen 6 och 9 är 3”, med 6 = 3·2 och 9 = 3·3.
2. ”Alla termer innehåller \(x\). Den lägsta potensen som finns i alla termer bryts ut”.
3. ”Dividera varje term med \(3x\)”, med en rad per term.
4. ”Skriv uttrycket som \(3x\) gånger parentesen”.
5. ”Kontroll: multiplicera in \(3x\). Termerna i parentesen har ingen gemensam faktor kvar …”.

Ledtråden frågar efter det största tal som talen är delbara med, och efter bokstäver som finns i alla termer. Uppgifterna har ingen figur och miniräknaren är avstängd.

## Verifiering

- Byggskriptet `tools/bygg-ma1-faktorisering-2026-11-06.py` kontrollerar med sympy att produkten är frågans polynom och att parentesen är primitiv (`terms_gcd` och `content`).
- Mastertestet `tools/ma1-faktorisering-2026-11-06.test.js` räknar om varje svar ur frågan, oberoende av byggaren:
  - värdet jämförs i tre punkter med flera variabler;
  - koefficienterna i parentesen ska ha största gemensamma delare 1;
  - ingen variabel får finnas i alla termer.
- I Kunskapsgymmet kör `tools/storsta-faktor-2026-11-06.browser.cjs` självtestet och appens riktiga `expandGameTask` och `delSvarRatt` i headless Chrome på alla 42 kort.
  - Facit och faktorerna i omvänd ordning godtas.
  - Följande underkänns: den oförändrade frågan, bara talfaktorn utbruten, bara bokstaven utbruten och fel tal. Resultat: 0 fel.
- Hela Kunskapsgymmets testsvit ger samma misslyckade tester som före ändringen: admin-online, delkort, felrapporter-2026-10-25, Ma2 GeoGebra-statistik och Ma3-funktioner/sinus.
- Facit renderades i 390 px. Den bredaste formeln är 281 px, och 1.1694 har lästs i skärmbild.

Ma1:s äldre tvåfältsuppgifter i faktorisering lämnas orörda.
