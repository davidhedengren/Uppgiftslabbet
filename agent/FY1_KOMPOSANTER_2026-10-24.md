# Fy1 vektorer: mängdträning i komposanter, 2026-10-24

Lärarens önskemål: många uppgifter om vektorer i olika former, till exempel att beräkna komposanter, komposantuppdela med trigonometri och komposantuppdela grafiskt. Området behöver mycket mängdträning.

Området är Fy1 `vektorer` (kap 3). Det hade 53 kort, varav cirka 10 om komposanter. Ma1 hade inga kort om komposantuppdelning.

## Nya kort (70, 3.620–3.689)

| Delmoment (`familjNyckel`) | Antal | Innehåll |
|---|---|---|
| Komposanter utan trigonometri | 19 | Avläsning i rutnät med skala (1 ruta = 0,5 N … 50 N, 0,5–3 m/s, 1–20 m), vektorer som inte börjar i origo, inritade komposanter, lodrät kraft (Fx = 0), tecken i olika kvadranter, storlek ur komposanter (Pythagoras) |
| Komposanter med trigonometri | 38 | Sinus och cosinus med vinkel mot x-axeln, mot lodlinjen och mot norr (navigation). Tyngdkraftens komposanter längs och vinkelrätt mot lutande plan (låda, bil, cykel, skidåkare). Kast, stigande flygplan, segel och kanal. Andra, tredje och fjärde kvadranten. Baklänges: storlek ur en komposant och vinkeln. Riktning ur komposanterna (arctan, även i andra kvadranten). Välja rätt uttryck. Lutning ur andel av mg |
| Addera vektorer | 13 | Grafisk addition av två och tre vektorer, vinkelräta krafter, krafter på komposantform, symmetriska rep och linor, vandring och skidtur i väderstreck, plan i sidvind, jämvikt med en tredje kraft, båt i ström (vinkelrät och snett) |

- 18 kort ligger på nivå 1.
- Figurer finns där de hör hemma: rutnät med skala, vinkelfigurer med vinkelbåge och lutande plan.
- Fysikformatet följs:
  - poängen skrivs inom parentes;
  - precisionen anges i parentes efter frågan;
  - toleransen är 0,05 för svar med en decimal och 0 för avläsningar;
  - g = 9,82.
- Inget nytt kort har samma facit som ett annat kort i området. Två lika mallar fick nya formuleringar.

## Rättelser i befintligt material

- **3.285:** ledtråden nämnde ”kateterna 6 och 8”, men vektorn är (5, 7). Den är rättad.
- **`tools/fysik1-kapitel3.test.js`:** kontrollistan för vektorer saknade 3.461–3.464, som en annan session lagt till. De är nu tillagda, och de 66 nya korten med numeriska facit har oberoende omräknade värden i listan. Vektordelen av testet går därmed igenom. Testets andra delar, för acceleration, konstant acceleration, vt-diagram och st-diagram, fallerade redan före ändringen och påverkas inte.

## Kontroll

- Validatorn för Fy1 ger inga nya fynd, med 840 fynd före och efter.
- SVG-granskaren ger bara INFO-fynd för de 29 figurerna: bakgrundsrutan ligger kant i kant med figuren, som i befintliga figurer, och vinkelbågar är markerade för översyn.
- `tools/fysik1-komposanter-2026-10-24.test.js` ger 2/2 pass.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 81 svar. Alla gav väntat resultat. Testet täckte bland annat:
  - svar med enheter och negativa komposanter med båda minustecknen;
  - att omvänd ordning och fel tecken underkänns;
  - grader och svar i två eller tre fält.

## Omgång 2: 43 kort till (3.690–3.732)

Läraren bad om fler kort i komposantdelen.

- **Grafiskt:** förflyttning på 100 m per ruta, fjäderkraft snett uppåt vänster, hastighetspil som börjar mitt i rutnätet, decimal skala (1,5 N), vinkel ur rutnät (även under x-axeln), addition med motsatt riktade komposanter och hastighetsändringen Δv = v₂ − v₁.
- **Trigonometri:**
  - gräsklippare (vågrät komposant och hur hårt den trycker nedåt), resväska, skidlift och vattenskidor;
  - basket, pilbåge, tennisserve nedåt, längdhopp, raket och segelflygplan;
  - kranvajer mot lodlinjen (båda komposanterna);
  - kurser väster om norr, söder om öster och väster om söder.
- **Lutande plan:** rutschkana 35° (figuren skalas nu ned för branta vinklar), skateramp, lastramp, transportband och snöskoter.
- **Baklänges och resonemang:**
  - den okända komposanten ur storleken och den andra komposanten;
  - vinkeln ur storleken och en komposant;
  - kraften i ett rep ur den lodräta komposanten;
  - kursavvikelse och lutning ur en kraftandel;
  - vid vilken vinkel komposanterna blir lika stora;
  - hur komposanten ändras när repet hålls brantare;
  - komposantformen för en kraft rakt åt vänster.
- **Addition och jämvikt:** två bogserbåtar i olika vinklar, lampa i vajer, tre förflyttningar med sydväst, en tredje kraft för jämvikt och flygplan i snedvind.

Kontroll:

- Validatorn för Fy1 ger inga nya fynd. Två kort fick nya tal och en formulering ändrades för att undvika dubblettfacit och lika mallar.
- SVG-granskaren ger bara INFO-fynd.
- Kontrollistan i kapitel 3-testet är utökad med oberoende facit, och vektordelen går igenom.
- `fysik1-komposanter`-testet omfattar nu 3.620–3.732.
- Självrättningen i Kunskapsgymmet testades i webbläsaren med 44 svar, och alla gav väntat resultat.
