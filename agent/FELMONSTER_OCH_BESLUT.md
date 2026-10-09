# Register över felmönster och tidigare beslut

Detta är ingången för framtida granskning. Läs den före bankändringar och sök
sedan upp uppgifts-ID:t i `agent/` och i testerna. Granskningsloggarna innehåller
matematisk kontroll, exakta ändringar, utfall och kommentarsförslag. Git visar
diffen och historiken. Registret är ett urval av återkommande mönster, inte en
förteckning över varje fel som någonsin rättats.

## Arbetsgång för nästa agent

1. Sök ID och feltyp, exempelvis `rg -n '1\.234|begreppssvar' agent tools`.
2. Läs aktuell uppgift, dess delkort och den tidigare motiveringen.
3. Lös matematiken självständigt och testa det faktiska elevflödet.
4. Undersök minst fem liknande uppgifter per feltyp när det finns relevanta fall.
5. Skriv en ny logg: granskade ID:n, ändrade ID:n, **Granskad – inget fel**,
   osäkra/ofullständiga kontroller och färdiga kommentarsförslag.
6. Lägg till nya felmönster eller uppdatera relevanta poster här. Länka testerna.

Ett tidigare beslut får ändras om det visar sig felaktigt, men det ska ske med
ny matematisk/pedagogisk motivering och verifiering. Befintliga mönster i banken
är inte facit. Ett test får inte tas bort eller försvagas för att dölja en återgång.

## FP-01: Frågan och rättningssvaret mäter olika saker

**Sök efter:** ”Vad betyder”, ”förklara”, ”ange skärningen”, flera namngivna storheter
med svar som bara består av ett belopp eller en punktsträng.

**Beslut:** antal svarsfält, etiketter, ordning och rättning ska motsvara frågan.
Begreppsfrågor får inte rättas genom att eleven måste gissa en exakt fras.
Använd granskade förklaringsalternativ eller manuell bedömning när det behövs.

**Exempel:** ma2 1.234 b frågade vad 45 betydde men lagrade ”45 kr”. Nu prövas
förståelsen av fast avgift genom förklaringsalternativ på spelkortet. 1.29 har
x/y-fält; 1.299 har fält för T-shirts och hoodies. 2.12 b frågar efter faktorn.

**Skydd:** Kunskapsgymmet `tools/modellgranskning-ma2-2026-10-09.browser.py`,
`tools/felrapporter-2026-10-09-2049.browser.py`.

**Underlag:** [modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md),
[rapporter 20:49](FELRAPPORTER_2026-10-09_2049.md).

## FP-02: Delkort saknar tidigare information eller visar andra delars facit

**Sök efter:** `spelDelning`, saknat `spelDelar[i].s`, ”använd”, ”samma”, ”modellen”,
”mer än så”, facit som börjar med ett mellanresultat utan att det ges på kortet.

**Beslut:** varje kort ska innehålla sina givna värden, formel/figur, eget facit
och relevant ledtråd. Om ett tidigare resultat behövs för den avsedda nivån,
ge det direkt. Kalibrera kortets nivå efter den information som faktiskt visas.
Huvuduppgiftens och spelkortens delar ska ha entydig koppling till svaren.

**Exempel:** ma2 1.271 b får kilometerpriset och c hela taximodellen. 2.11 b får
förändringsfaktorn. 2.361, 2.363 och 2.365 har egna delfacit. 2.195 b får
kvadratkompletterad form i sitt kort och en förklaring till minsta värdet.

**Skydd:** `tools/delkort.test.js`, `tools/foljdgranskning-ma2-2026-10-09.browser.py`,
`tools/modellgranskning-ma2-2026-10-09.browser.py`,
`tools/kvadratkomplettering-2026-10-09.browser.py` (Kunskapsgymmet).

**Underlag:** [följdgranskning](FOLJDGRANSKNING_MA2_2026-10-09.md),
[modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md),
[kvadratkomplettering](KVADRATKOMPLETTERING_2026-10-09.md).

## FP-03: Algebraisk likhet räcker inte när en särskild form efterfrågas

**Sök efter:** ”faktorisera”, ”kvadratkomplettera”, ”förenkla”, ”decimalform”
kombinerat med generiskt `svarFormat:"uttryck"` eller saknat format.

**Beslut:** kontrollera både matematiskt värde och efterfrågad form. Generiska
likhetsgenvägar får inte godkänna ursprungsuttrycket i en omskrivningsuppgift.
Använd ett uttryckligt svarsformat; ändra inte vanlig uttrycksrättning globalt.

**Exempel:** ma2 2.19, 2.71, 2.88 a, 2.190, 2.194 och 2.195 a använder
`kvadratkompletterat`. `(x-3)^2+4` och `4+(3-x)^2` godtas; `x^2-6x+13` är
matematiskt lika men besvarar inte kvadratkompletteringsfrågan.

**Avgränsning:** den nya kontrollen gäller x-polynom på formen `A*(x+h)^2+k`,
med en uttrycklig kvadrat och x-koefficient ±1 inne i parentesen. Den ska inte
sättas på godtyckliga andra uppgiftstyper utan separat granskning och tester.

**Skydd:** `tools/kvadratkomplettering-2026-10-09.browser.py` i Kunskapsgymmet.
**Underlag:** [kvadratkomplettering](KVADRATKOMPLETTERING_2026-10-09.md).

## FP-04: Modellvillkor och svarsenheter saknas eller blandas ihop

**Sök efter:** olika storheter i samma ekvation, saknad `svarEnhet`, avrundat
facit med för snäv tolerans, rörelsemodeller utan nödvändigt fartvillkor.

**Beslut:** behåll bara villkor som behövs och skriv dem enkelt. Kontrollera
fråga, beräkning, visad enhet och accepterade elevsvar tillsammans.

**Exempel:** ma2 1.37 använder kg kryddblandning och kg salt, inte odefinierad
salthalt i liter. 1.326 anger lika paddlingsfart relativt vattnet. 1.325 får kg
i svarsfältet. Se också fysikrapporten om tre värdesiffror.

**Skydd:** `tools/modellgranskning-ma2-2026-10-09.browser.py`,
`tools/felrapport-6-422.browser.py` i Kunskapsgymmet.
**Underlag:** [modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md),
[fy1 6.422](FELRAPPORT_6_422_2026-10-09.md).

## FP-05: Nivå eller variation följer en mall i stället för elevens arbete

**Sök efter:** identiska grafsvar, nivå 1 med modellering och flera beroende steg,
eller delkort som är lika högt graderade trots givna mellanresultat.

**Beslut:** nivå 1 är de allra enklaste uppgifterna. Bedöm träningsnivå, E/C/A
samt arbetsinsats separat. Höj eller sänk individuellt. Variationsproblem kräver
inte att varje liknande uppgift ändras.

**Exempel:** ma2 1.296–1.302 ligger på nivå 2; grafuppgifter har varierade
skärningspunkter. 3.529 a ligger på 4 medan 3.523 sänktes till 2. Taxikorten
1.271 har nivåerna 3/2/1 efter vad som ges på varje kort.

**Skydd och underlag:** [rapporter 20:49](FELRAPPORTER_2026-10-09_2049.md),
[följdgranskning](FOLJDGRANSKNING_MA2_2026-10-09.md),
[modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md) och deras webbläsartester.

## FP-06: Facit räknar rätt men förklarar inte beräkningen

**Sök efter:** ”Lös systemet” följt av enbart svar, uppdelade meningar i flera
numrerade steg, långa formler som kräver sidscrollning, fel variabelnamn.

**Beslut:** visa den avgörande substitutionen/eliminationen och nödvändiga
mellanled i korta, begripliga rader. I fysik används inte numrerade steg enligt
användarens instruktion. Kontrollera facit på mobil och dator.

**Exempel:** ma2 1.296–1.302 hade ingen uträkning mellan system och svar.
1.223 fick en kortare elimination; 1.30:s förklaring jämförde felaktigt
”x-koefficienterna” trots att det var y-koefficienterna.

**Skydd och underlag:** [följdgranskning](FOLJDGRANSKNING_MA2_2026-10-09.md),
[modellgranskning](MODELLGRANSKNING_MA2_2026-10-09.md), motsvarande webbläsartester.

## Att hitta äldre historik

Övriga granskningar finns i `agent/FELRAPPORT*.md`, `agent/FYSIK*.md` och
andra ämnesspecifika loggar. Sök alltid även där. Detta register ersätter inte
historiken eller ämnesreglerna. Rapportstatus i appen är skild från Git-historik;
en push innebär inte att rapporter har markerats som avslutade.
