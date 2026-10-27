# Ma4: felaktig standardtext och facit för komplexa tal

## Granskade och ändrade uppgifter

| Uppgift | Ändring och kontroll |
|---|---|
| 4.12 | Felaktiga råd om exponentiell förändring borttagna. Samtliga tre delars belopp och argument motiveras; samma slutsvar och tidigare polära svarsrättning behålls. |
| 4.197 | Fyra självständiga delkort och huvudfacit förklarar belopp, kvadrant och argument. Lagrade svar skrivs i parserns stödda format och svarstypen är `polar`, eftersom uppgiften begär polär form. |
| 4.198 | Fyra delkort förklarar belopp och riktning på koordinataxlarna. Lagrade svar skrivs i parserns stödda format och svarstypen är `polar`. Reella resultat kan fortfarande förenklas. |
| 4.199 | Fyra delkort visar insättning av de trigonometriska värdena vid omvandling till rektangulär form. |
| 4.203 | Fyra delkort använder Eulers formel och visar insättning före slutsvar. |
| 4.204 | Fyra delkort bestämmer belopp och argument före exponentiell form. |
| 4.288 | Fyra delkort visar belopp och argument; c och d har nu hela den efterfrågade polära formen. Svarsformatet ändras till `polar_0_2pi` så att angivet argumentintervall även prövas i självrättningen. |
| 2.482 | Irrelevanta råd om startvärde och logaritmer borttagna. Kedjeregeln ger \(f'(\pi/6)=e\sqrt3\). |
| 2.483 | Samma malltext borttagen; kedjeregeln ger \(f'(0)=\cos 1\), i radianer. |
| 2.485 | Samma malltext borttagen; kedjeregeln ger \(I'(\pi/2)=-0,4\). En lång formel delas upp för mobilvisning. |
| 2.467 | Samma malltext borttagen. För \(x\to\infty\) närmar sig grafen \(y=1\), och \(f(0)=2\). Uppgiften är avstängd från ordinarie spelträning. |
| 4.105 | Samma malltext borttagen. \(|z|=2\), argumentet är \(2\pi/3\) och \(z^3=8\). Den långa formeln i b delas upp för mobilvisning och delkortet förklarar hur den exponentiella formen tas fram. |

Ingen matematisk slutsats ändrades. I de sju första är huvudfacit och varje
delkorts facit omskrivna; de fem andra har fått de två irrelevanta
standardstyckena borttagna och två av dem dessutom kortare formelrader.
För 4.197 och 4.198 har även svarsformat och
lagrade facit ändrats, eftersom testet visade att de tidigare lagrade
LaTeX-svaren inte accepterades av rättningen. Inga uppgiftsformuleringar
eller betygspoäng ändras. Svarsformatet i 4.288 ändras så att det angivna
vinkelintervallet kontrolleras. Delkortens nivåer behålls: de handlar om
standardvinklar och direkt omvandling; ingen räknare eller GeoGebra behövs.
2.482, 2.483, 2.485 och 4.105 använder exakta standardvärden utan räknare;
2.467 behåller tillåten miniräknare för grafskissen.

## Fortsatt sökning

Den specifika formuleringen ”Skilj på startvärde och förändringsfaktor”
söktes i alla sju banker. De tolv uppgifterna ovan och 4.322 från
föregående omgång var de relevanta träffarna i Ma4. Sökningen efter en fras
innebär inte att övriga facit är manuellt granskade. En annan vanligt
förekommande malltext om att rita figur har identifierats för fortsatt
uppgiftsvis granskning, bland annat bland integraler; den ska inte tas bort
maskinellt utan kontroll av respektive uppgift.

Författarkällor: `tools/ma4-komplexa-facit-2026-10-27.py`,
`tools/ma4-felaktig-facittext-2026-10-27.py` och
`tools/ma4-polara-svar-2026-10-27.py`, `tools/ma4-polar-intervall-2026-10-27.py`,
`tools/ma4-mobilfacit-2026-10-27.py`, `tools/ma4-facit-kedjeregel-2026-10-27.py`,
`tools/ma4-facit-euler-2026-10-27.py` och `tools/ma4-euler-deluppgift-2026-10-27.py`.
Dessa förutsätter det dåvarande
bankinnehållet och ska inte köras blint på en senare version. Inga
rapportstatusar eller kommentarer har skrivits till produktionsdatabasen.

## Kontroller

- Bankfilerna i de båda repona är identiska. JavaScript-syntax och diff har kontrollerats.
- Befintliga tester `felrapporter-2026-10-15.test.js` och konsumentens
  `polara-svar.test.js` är godkända. Det senare har utökats med oberoende
  real- och imaginärdelar samt formkrav för tolv svar i 4.197, 4.198 och 4.288.
- I Kunskapsgymmet kördes 212 svarskontroller för de 11 tillgängliga
  huvuduppgifterna på mobil och dator, inklusive alternativa polära och
  exponentiella skrivsätt, felaktiga värden, rektangulära svar och vinklar
  utanför det föreskrivna intervallet. Alla svarskontroller gick igenom.
  Den första mobilkontrollen fann två överlånga formler, som därefter
  justerades och testades om. 2.467 är inte tillgänglig för vanlig träning.
- Uppgiftslabbet visade samtliga 12 uppgifter i 2c utan rapporterade
  JavaScript- eller KaTeX-fel. Delkort och mobilfacit har kontrollerats
  även visuellt i Kunskapsgymmet. Inga figurer har ändrats.
