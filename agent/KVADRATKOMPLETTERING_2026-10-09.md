# Kvadratkomplettering och beslutshistorik, 2026-10-09

## Granskning

Granskade och förbättrade: **ma2 2.19, 2.71, 2.88, 2.190, 2.194 och 2.195**,
spår 2c. Ingen i denna grupp föreslås som **Granskad – inget fel**.
Inga rapportstatusar eller elevkommentarer har sparats i rapportsystemet.

## Gemensam felorsak och fem jämförelser

För en kvadratkompletteringsuppgift räcker inte algebraisk likhet. Den generiska
uttrycksrättningen kan godkänna ett avskrivet ursprungsuttryck, trots att det inte
har kvadratkompletterats. Detta följdes upp i de sex uppgifterna ovan: varje
uppgift har alltså fem andra uppgifter med samma efterfrågade omskrivning.

De använder nu det uttryckliga formatet `kvadratkompletterat`. Den vanliga
uttrycksrättningen är oförändrad. Kontrollera både likvärdighet och form före
andra generella rättningsgenvägar. Kravet är en uttrycklig kvadrat av ett
linjärt x-uttryck med koefficient ±1, multiplicerad med en konstant och med
en eventuell konstantterm. Funktionen är avgränsad till denna granskade form.

- Godkänn `(x-3)^2+4`, `4+(3-x)^2`, extra parenteser, ² och LaTeX-form.
- Godkänn funktionsprefix som `f(x)=(x+3)^2-11`.
- Underkänn `x^2-6x+13` i omskrivningsuppgiften trots matematisk likhet.
- Underkänn fel konstant, en onödig nollkvadrat som lagts till originalet och
  ett helt uttryck som felaktigt kvadrerats igen.

Delkortens självständighet kontrollerades också, med jämförelser mot modell-
och exponentialkorten 1.138 b, 1.234 b, 1.271 b/c, 2.11 b och 2.365 b från
föregående runda. Samma regel gäller här: ett kort om minsta värde eller
symmetrilinje ska få den redan kvadratkompletterade formen när detta är den
avsedda enkla avläsningen.

## Individuella åtgärder och kommentarsförslag

| Uppgift | Kontroll och ändring | Föreslagen kommentar |
|---|---|---|
| 2.19 | (x−3)²+4=x²−6x+13. Nytt formkrav i rättningen. Nivå 1→2: halvera koefficienten och justera konstanten är flera beroende moment. | Självrättningen kontrollerar nu att svaret faktiskt är kvadratkompletterat. (x−3)²+4 och likvärdiga kvadratformer godkänns. |
| 2.71 | (x+2)²−3=x²+4x+1. Nytt format. Facit förklarar varför 3 subtraheras. Ledtråden talar inte längre om ”båda sidor” när uppgiften gäller ett uttryck. Nivå 1→2. | Facit visar varför konstanten måste justeras till −3. Rättningen kräver nu kvadratkompletterad form. |
| 2.88 a/b | 2(x−2)²−5=2x²−8x+3, symmetrilinje x=2. Tidigare frågades efter både omskrivning och symmetrilinje men bara x=2 låg som rättningssvar. Nu två tydliga delar med egna svar och facit. b får omskriven funktion. Nivå a=3/C, b=1/E. | Båda frågorna har nu egna svar och lösningar. Kvadratkompletteringen är 2(x−2)²−5 och symmetrilinjen x=2. |
| 2.190 | (x+3)²−7=x²+6x+2. Nytt format. Nivå 2 och befintlig förklaring behålls. | Det räcker inte längre att skriva av originaluttrycket. Kvadratkompletterad form (x+3)²−7 godkänns. |
| 2.194 | (x+5)²−4=x²+10x+21. Nytt format. Nivå 2 och befintligt facit behålls. | Rättningen prövar nu även formen. Svaret är (x+5)²−4. |
| 2.195 a/b | (x+3)²−11=x²+6x−2. a får formkontroll och förklaring. b får omskriven form och förklarar att en kvadrat är minst 0. Minsta värde är −11 vid x=−3; b frågar efter funktionsvärdet, inte x. Nivå a=2, b=1. | Varje del har nu ett förklarande facit. B-kortet innehåller formen som behövs för att direkt bestämma minsta värdet −11. |

## Verifiering

- `tools/kvadratkomplettering-2026-10-09.browser.py` i Kunskapsgymmet:
  24 rättningskontroller och samma 24 inmatningar genom den riktiga svarsknappen.
  Korrekta former, olika ordning, funktionsprefix, LaTeX, upphöjt ², fel svar,
  ursprungsuttryck och försök att kringgå formkravet ingår.
- 32 visningar av åtta kort: mobil/dator och ljust/mörkt tema. Inga KaTeX-fel,
  för breda facitformler eller sidöverbredd. Utvalda mobillösningar granskades visuellt.
- 41 tester för delkort, exakta talsvar, decimalform och procentenheter passerar.
- Ma2-validatorn visar oförändrade kända fynd: 4 ERROR, 166 WARNING, 95 INFO.
- Alla 2121 uppgifts-ID:n bevaras. Endast de sex angivna bankobjekten ändras.
  Inga SVG-figurer ändras. Bankfilen är identisk i de två repona.
- Ändringar i appens kod är avgränsade till det nya uttryckliga svarsformatet,
  dess val i `formatRatt`/`delSvarRatt`, samt bankversionen.

## Beständig historik för nästa AI

På användarens begäran har följande lagts till:

- `agent/FELMONSTER_OCH_BESLUT.md`: sökbart register med feltyper, symptom,
  tidigare beslut, exempel, avgränsningar och länkar till loggar/tester.
- `AGENTS.md` i båda repona: läs tidigare beslut före ändring, följ upp liknande
  fel och kör de tester som skyddar rättningarna.
- Hänvisningar från båda `CLAUDE.md` och masterrepons arbetsinstruktion.

Syftet är att nästa agent ska kunna hitta och förstå rättningarnas motiv.
Ett tidigare beslut får omprövas när det finns bättre underlag, men skälet ska
sparas och beteendet verifieras. Git bevarar tidigare versioner; testerna gör
flera typer av oavsiktlig återgång synliga. Det är inte ett absolut tekniskt
förbud mot att någon senare ändrar innehållet.
