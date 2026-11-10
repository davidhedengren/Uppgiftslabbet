# Fy2 längdkontraktion: första facitomgången 10 november

Inventering av alla sju banker visar kvarvarande malltexter främst i Fy2, Ma1, Ma4 och Ma5. Tidigare Ma3-/Ma4-omgångar från parallellsessionen bevaras. Denna avgränsade omgång omfattar 27 uppgifter i Fy2:s längdkontraktion; resterande sju, med bland annat myon-/paradoxresonemang, återstår.

## Granskade och ändrade ID:n

6.11, 6.12, 6.13, 6.14, 6.15, 6.16, 6.17, 6.18, 6.20, 6.21, 6.22, 6.27, 6.28, 6.29, 6.62, 6.63, 6.64, 6.330, 6.331, 6.332, 6.333, 6.334, 6.335, 6.336, 6.337, 6.338, 6.339.

Alla får individuellt författade steg med rubriker, förklaringar av vilken observatör som mäter vad, insättning och svarsrad. Generiska inledningar och avslutningar ersätts av konkreta förklaringar. Numeriska facit har minst en formel i rubrik; begreppskort namnger relevant princip. Svarsraden till 6.339 saknades tidigare och är tillagd. Långa formler radbryts efter faktisk mobilkontroll.

- 6.11: observatörens 41,2 m skiljs från skeppets egenlängd 78,2 m.
- 6.12: behåller båda tidigare godkända ljusfartsalternativen, 34,6 respektive 34,2 ljusår. De får inte ersättas av ett godtyckligt enda tabellvärde.
- 6.13/6.14/6.20/6.64: visar hur farten isoleras ur längdkvoten, inte bara en färdig gammafaktor.
- 6.15/6.16: ingen Lorentzfaktor behövs för enhetsomvandlingen respektive jordens egen restidsberäkning. Det gamla generella rådet att börja med gamma var missvisande i 6.16.
- 6.17/6.18/6.27/6.28: håller jordens avstånd/tid åtskilda från resenärens längd/egentid. Mellanresultat avrundas först i presentationen.
- **6.21: maskinfacit rättat från 100 m till 101√(1−0,20²)=98,959789… m.** Tolerans 1,5 m kunde tidigare även godta 101 m, vilket motsäger slutsatsen om huruvida tåget ryms. Nu anges en decimal och tolerans 0,05 m; 99,0 godtas, 100/101 underkänns. Ingen omklassificering.
- 6.22: ”tittar framåt” ersätts med samtidig mätning av tunneländarna i tågets system. Längdkontraktion är inte samma sak som fotografiskt utseende.
- 6.29/6.333: bara dimensionen längs rörelsen kontraheras. Tvärdimensionerna förblir oförändrade.
- 6.62/6.63/6.330–6.332/6.335–6.338: egenlängd, rörelse och insättning förklaras för det specifika skeppet/staven/tunneln/myonen. 6.335 använder redan given gamma i stället för en onödig fartberäkning.
- 6.334/6.339: astronauten är i vila relativt skeppet och mäter därför egenlängden.

## Granskad matematik – inget fel

De övriga 26 uppgifternas numeriska eller begreppsliga svar stämmer efter egen omräkning. Deras svarsvärden lämnas oförändrade. Presentationen ändras ändå eftersom den inte uppfyllde facitmallen. Alla 27 behåller sina nivåer. Miniräknare tillåts uttryckligen även när äldre metadata saknades. GeoGebra är avstängt: ingen grafavläsning eller digital ekvationslösning behövs för dessa direkt isolerbara relativitetssamband.

Fem närliggande längdberäkningar till 6.21 är separat kontrollerade: 6.11, 6.14, 6.62, 6.63, 6.330. Deras maskinfacit stämmer med respektive efterfrågad storhet. Ingen motsvarande förväxling med den okontraherade längden hittades.

## Verifiering och avgränsning

Författarkälla: tools/fy2-langdkontraktion-facit-2026-11-10.py. Browserharness och cases med samma prefix.

- 44 faktiska svarsförsök i Kunskapsgymmet, inklusive rätt respektive felaktigt maskinsvar i 6.21.
- 54 kortvisningar i vardera appen (27 × mobil/dator), bildladdning, KaTeX-fel och formelbredd kontrolleras. Befintliga figurer bevaras; inga nya diagram behövs för dessa direkta beräkningar.
- Strukturell kontroll: 27 avsedda ID:n, inga andra objekt; varje facit har numrerade steg, specifika rubriker och svarsrader. Bankkopior jämförda före ändring och synkade efteråt.
- Ingen rapportstatus eller kommentar sparas i appen. Om 6.21 rapporteras kan kommentaren vara: ”Maskinfacitet var fel. Tåget mäts till 99,0 m och ryms därför i tunneln i markens system. Frågan och rättningen är korrigerade.”

Kvar i området till nästa omgång: 6.9, 6.19, 6.24, 6.30, 6.51, 6.52, 6.57. Ingen fullständig granskning av deras facit påstås här.

## Andra pushomgången: de sista sju uppgifterna

Efter första pushen är även **6.9, 6.19, 6.24, 6.30, 6.51, 6.52 och 6.57** omskrivna. Därmed har samtliga **34 uppgifter** i området och alla deras explicita delfacit fått mallen.

- 6.9 skiljer mellan skeppets förflyttning enligt jorden och jordens rörelse bort från Pelle i skeppets system.
- 6.19 förklarar att kaptenens avstånd avser samtidiga positioner i skeppets system, inte fotografiskt utseende.
- 6.24 anger nu uttryckligen jordens referenssystem i frågan. Vilolivstid, tidsdilatation och färdsträcka kopplas ihop med insättningar.
- 6.30 visar substitutionen β=v/c, kvadreringen och den positiva rot som ger farten. Inga svarsvärden ändras.
- 6.51 får eget komplett facit per del. Marksystemets färdtid cirka 50,28 μs ger klassiskt cirka 8,1·10⁻¹¹ kvar; egentiden cirka 5,02 μs ger cirka 9,8 %. Samma tid härleds i myonens system från den kontraherade sträckan.
- 6.52 anger händelseordning och koordinatriktning innan samtidighetstransformationen. Med bortre porten minus bakre porten blir Δt′≈−35,6 ns: bortre porten stängs först. Det gamla facitet använde positivt belopp utan definierad ordning. Absolutbeloppet var korrekt. Befintlig jämförelsefigur i facit bevaras.
- 6.57 får separata facit för åldrarna 45/37 år, beräkningen av 12 år i skeppets system och varför vändningen bryter symmetrin. Förklaringen gäller hela resan och använder inte acceleration som en fristående formel för åldersskillnaden.

Ingen ytterligare numerisk rättning eller nivåändring i de sju. Samtliga tillåter miniräknare; inga kräver GeoGebra. Alla 34 granskade frågors svar utom 6.21 var matematiskt korrekta; presentationen ändras ändå.

Utökad browserkontroll omfattar 48 svarsförsök och 82 kortvisningar per app (34 huvudfacit plus sju explicita delkort, två bredder). De manuella sammansatta svaren är dessutom oberoende omräknade med relativitetssambanden och sönderfallslagen. Sju tidigare relativitets-/figurregressioner passerar. Full matematisk granskning av andra områden i bankerna återstår.
