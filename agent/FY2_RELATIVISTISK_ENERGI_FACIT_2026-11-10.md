# Fy2 relativistisk energi: alla 37 uppgifter, 10 november

## Granskade ID:n och ändringar

6.31–6.50, 6.53, 6.54, 6.56, 6.58, 6.65, 6.66, 6.67, 6.340–6.349. Alla 37 huvudfacit och de 12 explicita delfaciten i 6.53/6.54/6.56/6.58 är individuellt omskrivna enligt FACITMALL.md: konkreta rubriker, formler, insättningar, meningsfulla mellanled och svarsrad. Inga allmänna metodinledningar eller avslutande mallråd kvar. Långa beräkningsrader delas för mobil; radbrytningshjälpen ändrar bara placeringen av relationssymboler, aldrig rubriker eller matematik.

- 6.31/6.32/6.34/6.37: viloenergi och massa, eV/MeV/J och SI-omvandlingar förklaras separat. Ingen Lorentzfaktor behövs för rena viloenergier eller enhetsbyten.
- 6.33: tera betyder 10¹²; eV är energi, inte spänning.
- 6.35: skiljer vattnets värmekapacitet från ljusfarten och kopplar tillförd värmeenergi till ökad vilomassa.
- 6.36: K/c² kallas energins massekvivalent i vägens system. Bilens vilomassa ökar inte enbart av fartökningen. Klassisk K räcker vid 150 km/h.
- 6.38/6.39/6.40: visar tid i sekunder, elpris i kr/kWh och verkningsgrad före mass–energiomvandlingen. I 6.40 ska frigjord kärnenergi, inte bara levererad el, användas.
- 6.41/6.42/6.43: samma protonfart men tre olika energier. Viloenergin beror inte på farten; totalenergin är γE₀ och rörelseenergin (γ−1)E₀.
- 6.44–6.46: fartkvot, omvänd energifråga och arbete som energiskillnad visas utan att hoppa över vilken energityp som är given.
- 6.47–6.50: klassisk respektive relativistisk elektronacceleration jämförs. Den klassiska farten nästan 2c i 6.49 är avsiktligt en demonstration av modellens begränsning, inte ett fel som ska döljas.
- **6.53: modellförutsättningen rättad i huvudfråga, intro och fristående kort.** Den gamla frågan beskrev acceleration längs röret samtidigt som facit använde konstant gamma/fart under hela passagen. Elektronerna accelereras nu först till totalenergin 50,0 MeV och passerar därefter en 30,0 m lång mätsträcka med konstant fart. Då gäller L=L₀/γ och τ=t/γ under passagen. Värdena gamma≈97,85, L=0,3066 m, t≈100,1 ns och τ≈1,02 ns bevaras.
- 6.54: skiljer massförlust från väteförbrukning; endast 0,71 % försvinner som energi. Total modelltid cirka 10,5 miljarder år och återstående cirka 5,9 miljarder anges som följder av konstant effekt, inte exakt solprognos.
- 6.56: skillnaden c−v≈3,1 m/s beräknas med stabilt uttryck när beta är nära 1. Varvtiden cirka 90 μs och egentiden cirka 13 ns förklaras utan att ringens omkrets behandlas som en rak stav. Inget gemensamt inertialsystem följer protonen runt hela varvet.
- 6.58: parbildningens två viloenergier, resterande rörelseenergi och rekylens roll för både energi- och rörelsemängdsbevarande. Antagandet om försumbar kärnrekyl i a/b behålls, och andra parbildningsprocesser utesluts inte.
- 6.65/6.67/6.340–6.349: massan respektive massdefekten identifieras, förväxling mellan total/rörelseenergi undviks och begreppsfrågorna får explicit slutsvar.

## Ledtrådar, nivåer och verktyg

Åtta huvudledtrådar (6.31/32/34/38/40/44/45/53) rättas, plus alla tolv delledtrådar i de fyra flerdelade uppgifterna. Fem tydliga följdfynd: 6.31, 6.32, 6.34, 6.38 och 6.40 bad eleven börja med Lorentzfaktorn trots att ingen fart behövdes eller ens var given. 6.45 bad om gamma från farten trots att farten söks; den börjar nu med energikvoten. Delledtrådarna fokuserar på sin egen delfråga.

Alla nivåer, poäng och numeriska maskinfacit bevaras. Miniräknare tillåts på alla 37; GeoGebra behövs inte för dessa direkt isolerbara samband. Befintliga figurer bevaras. Ingen rapportstatus eller kommentar sparas i apparna av denna kodleverans.

## Granskad – inget numeriskt fel

Samtliga befintliga siffersvar stämmer med egen omräkning och de tabellvärden/avrundningar som används. 6.53 hade felaktigt beskriven modell, men de beräknade siffrorna passar den nu uttryckliga passagen vid konstant fart. Fem jämförelser till modellfrågan är 6.45, 6.48 och 6.50 (slutfart ur given energi utan tidspassage), 6.56 (konstant fartbelopp, men cirkelrörelse) samt 6.30 (partikelfärd under vilolivstid). Inga motsvarande oangivna accelerationsförlopp behövde ändras där.

## Test och synk

- 62 faktiska svarsförsök i Kunskapsgymmet, inklusive alla åtta alternativval i 6.345/6.347, rätt/fel tal och sex för precisa svar som korrekt underkänns enligt befintlig ±2-regel. Oavrundade interna maskinvärden ska inte förväxlas med ett tillåtet elevsvar på 15 siffror. Ingen tolerans har vidgats.
- 98 visningskontroller per app: 37 huvudfacit plus 12 delkort vid 390/1280 px. KaTeX, bildladdning och formelbredd kontrollerade. Inga kvarstående nya renderingsfynd.
- Fyra nya matematiska/strukturtester: alla 37 och delfacit, samtliga 24 numeriska svar, mätsträckan i 6.53 och modellerna för sol/acceleratorring. Sju befintliga relativitets-/figurtester passerar.
- Författarkälla och testfiler har prefix `fy2-relativistisk-energi-facit-2026-11-10`. Endast dessa 37 bankobjekt ändras. Master/konsument jämförda före synk; bankkopiorna är identiska efteråt. Python-cache och annan sessions arbete bevaras.

I separat föregående push samma arbetspass hanterades Ma1 0.167 och mobilradbrytningen i 0.278; se MA1_0_167_2026-11-10.md. Ett äldre Ma1-test har ett känt VM-fixturefel (`bankBildadresser` saknas), dokumenterat där. De verkliga Ma1-browserkontrollerna passerade.
