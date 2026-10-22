# Pedagogiska regler

## Självständig bedömning

Befintlig metadata, facit, strukturplacering och närliggande uppgifter är jämförelsematerial. De får inte behandlas som facit för klassificeringen. Agenten ska först analysera uppgiften självständigt och därefter jämföra med projektets konventioner.

## Fyra separata beslut

Följande ska bedömas var för sig:

1. **Matematisk förmåga** – vad eleven faktiskt måste förstå och göra.
2. **Nivå/svårighet** – komplexitet, antal steg, strategival, abstraktionsgrad och krav på motivering.
3. **Självrättningsbarhet** – om elevens slutsvar kan representeras och bedömas entydigt.
4. **Tekniskt svarsformat** – hur det matematiska svaret säkert uttrycks i Kunskapsgymmets datamodell och gränssnitt.

Ett beslut inom en dimension får inte automatiskt bestämma de andra. Särskilt gäller:

- `resonemang` eller `problemlösning` innebär inte automatiskt manuell rättning,
- hög nivå innebär inte automatiskt manuell rättning,
- ett numeriskt slutsvar innebär inte automatiskt att uppgiften främst prövar procedur,
- ett tekniskt lättformat svar får inte sänka eller förändra den pedagogiska avsikten.

## Matematisk verifiering

Före ändring av svar eller rättningsmetadata ska agenten:

- lösa uppgiften självständigt,
- kontrollera definitionsmängd och eventuella extralösningar,
- avgöra om svaret är ordnat eller oordnat,
- identifiera alla giltiga lösningar och likvärdiga representationer,
- kontrollera enheter, avrundning och rimlig tolerans,
- verifiera att uppgiftstext, facit och maskinellt rätt svar beskriver samma matematik.

Numeriska kontroller får stödja analysen men ersätter inte matematisk argumentation när exakthet eller fullständighet är avgörande.

## Förmåga

Förmågeklassificeringen ska grundas på elevens huvudsakliga kognitiva arbete. Flera förmågor får anges när de faktiskt prövas, men listan ska inte fyllas med förmågor som bara förekommer perifert.

Exempel på frågor att ställa:

- Krävs främst en känd algoritm eller metod? Då talar det för procedur.
- Krävs förståelse av samband, representationer eller villkor? Då kan begrepp vara relevant.
- Krävs val eller konstruktion av strategi i en obekant situation? Då kan problemlösning vara relevant.
- Krävs förklaring, värdering, generalisering eller logiskt sammanhängande argument? Då kan resonemang vara relevant.

## Nivå

Nivån ska bedömas oberoende av aktuell etikett. Beakta bland annat:

- hur bekant metoden rimligen är,
- hur många beroende steg som krävs,
- om strategi är given eller måste väljas,
- om representationer måste växlas,
- hur stor risken är för relevanta felslut,
- om eleven måste motivera, generalisera eller värdera.

Ändra inte nivå enbart för att rättningsformatet ändras.

### Träningsnivå 1 och 2

**Träningsnivå 1 ska innehålla de allra enklaste uppgifterna.** Eleven ska kunna
känna igen ett grundbegrepp eller använda ett direkt, tydligt samband med enkla
tal. Exempel är att identifiera en sträcka, läsa av en motsvarande vinkel,
halvera en given medelpunktsvinkel eller multiplicera en sida med en given enkel
längdskala. Nivå 1 ska vara en trygg ingång till ett nytt delmoment.

**Träningsnivå 2 är lite svårare men kan fortfarande vara E.** Hit hör till
exempel att först bestämma en längdskala och sedan använda den, summera en hel
sida före topptriangelsatsen, lösa en proportion med kordasatsen eller
bisektrissatsen, kombinera två vinkelregler eller beräkna koordinatskillnader
före avståndsformeln. Krångligare tal eller flera beroende steg kan också
motivera nivå 2. Fler rutinberäkningar är inte i sig skäl att ändra E till C.

Bedöm varje uppgift och varje delkort för sig. Ett kort som redan anger
längdskalan eller ett mellanresultat kan vara nivå 1 även när hela uppgiften
är svårare. Ett nivå 1-kort får inte kräva att eleven först löser en osynlig
tidigare del. Alla nödvändiga givna uppgifter och figurer ska följa med kortet.

I fysik ska nivå 1–2 ha en kort, konkret situation och en tydlig fråga.
Visa bara de tal och materialdata som behövs för den aktuella frågan.
Ett kort om fjäderenergi behöver exempelvis inte uppgifterna för ett senare
kast, och ett kort om uppvärmning behöver inte smältvärmet. Om ett tidigare
mellanresultat behövs, ange det direkt och med tillräcklig precision för
självrättningen. Facit ska då utgå från det givna mellanresultatet.
Behåll nödvändiga fysikaliska villkor, referensriktning och nollnivå.
Säg vem kraften verkar på och vad eleven ska bestämma. Förklara skillnaden
mellan övertryck och absolut tryck när den annars kan missförstås.
Kontrollera alltid den visade svarsenheten mot `svarEnhet`.

I Fysik 1 ska nivå 1 till exempel kunna vara en direkt beräkning av tryck från
kraft och area i rätt enheter, rörelsemängd från massa och fart, eller effekt
från arbete och tid. En direkt energi- eller lyftkraftsformel med enkla tal kan
också vara nivå 1. En kvadrering är alltså inte ensam skäl att höja nivån.
Enhetsomvandling tillsammans med en fysikberäkning, flera beroende steg,
procenter eller mer krävande tal hör normalt till nivå 2. Även dessa kan vara E.
Stötar med två rörliga kroppar och riktningsval, eller problem som kombinerar
rörelsemängd vid en stöt med energibevarande efteråt, kan motivera nivå 3.
Givna mellanresultat ska vägas in när nivån på ett separat kort bedöms.

Fackord som eleven behöver lära sig får användas, men förklara dem när de annars
gör frågan svår att förstå. Skriv till exempel ”pilar som visar krafterna” i en
ritinstruktion och ”utan att temperaturen ändras” i stället för ”isotermt”.
Ange vad en fart mäts i förhållande till i kast- och rekylproblem. Skilj kraften
från ett visst föremål, exempelvis golvet, från summan av alla krafter.
Medelfart som medelvärdet av start- och slutfart förutsätter konstant acceleration;
det villkoret ska stå i uppgiften när beräkningen kräver det.

## Självrättning

En uppgift lämpar sig för självrättning när samtliga godtagbara slutsvar kan representeras utan att det matematiska innehållet förvanskas. Bedöm särskilt:

- antal svarsfält,
- fältens ordning och etiketter,
- om lösningsmängden är ordnad eller oordnad,
- om alternativa exakta uttryck måste godtas,
- om tolerans behövs,
- om enheter eller intervall ingår,
- om elevens motivering är en uttrycklig del av det som ska bedömas.

En svår problemlösnings- eller resonemangsuppgift kan vara självrättande när slutsvaret är entydigt representerbart. Om det däremot är själva argumentationen, modellen eller värderingen som ska bedömas kan manuell bedömning fortfarande behövas.

## Tekniska begränsningar

Kunskapsgymmets faktiska renderings- och rättningskod ska verifieras när ett nytt eller känsligt svarsformat används. Om systemet saknar ett matematiskt korrekt format ska agenten:

1. bevara uppgiftens pedagogiska kvalitet,
2. dokumentera begränsningen,
3. föreslå teknisk utveckling eller redaktionellt beslut,
4. inte skriva om uppgiften enbart för att passa begränsningen utan godkännande.

## ID och redaktionell kontinuitet

Uppgifts-ID ska bevaras när uppgiftens identitet i huvudsak är densamma. Nytt ID kan övervägas vid en så omfattande matematisk eller pedagogisk omarbetning att uppgiften i praktiken blivit en ny uppgift. Ett sådant beslut ska vara uttryckligt och får inte tas som bieffekt av automatisk korrigering.

## Heuristiska fynd

Validatorer får påvisa misstänkta avvikelser, men osäkra regler får inte presenteras som säkra matematiska fel. Heuristiska fynd ska klassificeras med rätt osäkerhetsnivå och får inte masskorrigeras utan redaktionell granskning.

## Kort och naturligt språk i fysikuppgifter

Skriv som i en vanlig gymnasieuppgift. Lägg inte till formella modellförklaringar
som inte hjälper eleven att förstå frågan. I vanliga uppgifter om tryck mot en
yta räcker ”trycket”; skriv inte ”medeltrycket” och lägg inte till ”anta jämnt
tryck över respektive kontaktyta”. Fråga hellre ”hur många gånger större är
trycket?” än ”bestäm kvoten av trycken”. Tekniska inledningar som ”alla effekter
avser nyttig mekanisk effekt i rörelseriktningen” ska ersättas med en konkret
beskrivning när det behövs för att skilja motorns effekt från tillförd el eller
bränsleenergi.

Behåll villkor som påverkar svaret, men skriv dem enkelt. ”Bortse från luftens
massa” är tydligare än ”luften har försumbar massa”. När trycket faktiskt varierar
med djupet kan frågan behöva ett medelvärde; skilj då detta från trycket vid en
viss punkt. Viktiga fackord som eleven ska lära sig får användas. Granska varje
träff i sitt sammanhang och kontrollera även de fristående spelkorten.

## Obligatorisk återrapportering efter granskning

Varje genomförd granskning ska avslutas med en konkret lista som användaren kan
använda för att hantera rapporterna. Detta gäller även när granskningen inte
hittar några fel. Redovisa alltid:

1. **Alla granskade uppgifter:** kurs, uppgifts-ID och berörd deluppgift.
2. **Alla åtgärdade uppgifter:** vad som faktiskt var fel och vad som ändrats.
   Om inga fel har rättats ska det stå uttryckligen.
3. **Alla granskade uppgifter utan fel:** märk dem **Granskad – inget fel** och
   förklara kort varför det befintliga svaret eller beteendet är korrekt.
4. **Förslag på kommentar efter varje rapport:** skriv en kort, färdig svensk
   kommentar som kan återkopplas till den som rapporterat. Ta med den avgörande
   beräkningen eller skillnaden i tolkning när det hjälper eleven.

Listan över alla granskade uppgifter är den fullständiga översikten. De andra
listorna anger utfallet. Eventuella osäkra eller ofullständigt granskade fall ska
redovisas separat som **Kvar att utreda**, med vad som saknas; de får inte markeras
som åtgärdade eller utan fel.

En felrapport bevisar inte att uppgiften är fel. Kontrollera först uppgift,
beräkning, visat facit och faktisk självrättning. Ett förtydligande av en redan
korrekt lösning ska redovisas som ett pedagogiskt förtydligande, inte som ett
rättat svarsfel. Ange vilka texter som förbättrats även om rapportens sakfråga
bedöms som **Granskad – inget fel**. Hitta inte på elevens inmatning när den saknas.

Skilj mellan föreslagen rapportstatus och status som faktiskt har sparats i
rapportsystemet. Påstå inte att rapporter har avslutats eller att kommentarer
har skickats enbart därför att kod eller bankfiler har ändrats och pushats.

## Följdgranskning av liknande fel

Användarens instruktion 2026-10-09: för varje upptäckt fel ska agenten försöka
hitta minst fem liknande uppgifter i banken och granska dem i sitt sammanhang.
Sök efter samma felorsak, även utanför det aktuella kapitlet eller kursen när
det är relevant. En liknande uppgift är inte automatiskt felaktig.

Redovisa ursprungsfelet, jämförelseuppgifternas ID:n, vad som kontrollerats och
utfallet för varje uppgift. Om färre än fem relevanta jämförelser hittas ska
sökningen och begränsningen anges. Uppgifter med samma felorsak får granskas
som en gemensam grupp, men varje uppgift ska bedömas individuellt. Nya feltyper
som hittas under granskningen ska också följas upp med en sökning efter
liknande fall. Bevara skillnaden mellan fullständig granskning och en
avgränsad kontroll, exempelvis enbart svarsfält eller delkortens facit.

## Värdesiffror i fysik – användarbeslut 2026-10-22

Om ingen precision anges rekommenderas lika många värdesiffror som det minst
noggranna **relevanta mätvärdet**. Korrekt avrundade slutsvar med ±2 värdesiffror
godtas, dock minst en. Rekommenderat 2 innebär alltså 1–4, men inte 5.
Detta är inte en procentuell feltolerans: talet måste vara korrekt avrundat
vid den precision eleven faktiskt har skrivit, även efter enhetsbyte.

Uttryckliga krav på exempelvis två decimaler, tre värdesiffror, heltal eller
exakt form behålls enligt användarens förtydligande samma dag. Ändra inte
äldre sådana krav mekaniskt. Exakta antal, koefficienter, enhetsomvandlingar
och standardkonstanter ska inte sänka mätvärdenas precision. Bedöm det
fristående kortets egna givna värden, inte data som bara hör till andra delar.
Vid addition/subtraktion och osäkerhetsuppgifter krävs en särskild bedömning;
tillämpa inte multiplikationens tumregel blint på exempelvis massdefekter.

Spara den manuellt verifierade rekommendationen i `svarVardesiffror` (tal per
kort, array per svar i huvuduppgiften). Spara oavrundat `rättSvar`; maskinen
avrundar till elevens precision. Använd ingen textheuristik för att fylla
metadata över hela banken. Äldre kort utan verifierad metadata behåller
befintlig rättning tills de granskats. Se FP93 för införandets faktiska omfattning.

Avslutande nollor i heltal är tvetydiga: 9400 kan stå för två värdesiffror.
För entydigt fler siffror används decimaler eller grundpotensform, t.ex.
9,400·10³ (fyra) och 9,4000·10³ (fem). Inledande nollor och exponentens siffror
räknas inte. Informera eleven om rekommendationen och accepterat spann vid
svarsfältet när standardregeln används.

## Miniräknare i fysik

Användarbeslut 2026-10-09: miniräknare är alltid tillåten i Fysik 1 och Fysik 2,
även för enkla begreppsuppgifter. Använd `miniräknare:true` i fysikbankerna.
Bedöm uppgiftens nivå efter förståelsen och beräkningen, inte efter om eleven
använder räknare. Detta ändrar inte reglerna för matematikuppgifter.

## Formelsamling i fysik – inga standardkonstanter eller formelledningar i frågan

Användarbeslut 2026-10-12: eleverna ska träna på att hitta standardkonstanter och välja formel. Ange inte exempelvis ”Använd g = 9,82”, Coulombs konstant, gravitationskonstanten eller en färdig lösningsformel i uppgiftstexten. Regeln gäller Fysik 1 och 2, läraruppgift, `spelIntro` och alla separata kort (`t`/`fraga`). Facit ska förklara formelvalet och visa konstanter och insättningar. Ledtrådar bakom separat knapp hålls åtskilda från frågan.

Nödvändiga situationsdata, experimentvärden, fjäderkonstanter, material-/isotopdata och lokala/modelldefinierade värden får inte raderas. Behåll även fysikaliska antaganden, positiv riktning och nollnivå. Formler som är själva föremålet för en felsökning eller härledning ingår i uppgiften. Skriv modelluppgifter som givna fakta utan extra uppmaningar att använda en bestämd formel. Kontrollera att självrättningen godtar de relevanta tabellvärdenas svar med rätt enhet och avrundning; använd granskade mål per uppgift, inte en allmän procenttolerans. Se FP34 och `FYSIK_FORMELSAMLING_2026-10-12.md`.

## Avrundning – metodförklaring i facit, inte i frågan

Användarbeslut 2026-10-13 efter Ma1 #0.189: skriv exempelvis ”Avrunda 2,675 till två decimaler.” Lägg inte till en påminnelse om att en avslutande femma avrundas uppåt eller vilken siffra eleven ska titta på. Vanlig skolavrundning för positiva tal förutsätts; förklaringen hör hemma i facit eller bakom den separata ledtrådsknappen. Det gäller även rutinpåminnelser vid halvsteg i frågor om avrundningsgränser.

Behåll efterfrågad noggrannhet och enhet. Behåll också riktad avrundning när den definierar situationen, till exempel att en betalning avrundas uppåt. Metoder och svarsalternativ som eleven ska jämföra, granska eller motivera är själva uppgiftens innehåll och ska inte tas bort som ledningar. En särskild avrundningsmodell som avviker från vanlig skolavrundning måste fortfarande anges. Se FP41 och `MA1_AVRUNDNINGSLEDNINGAR_2026-10-13.md`.

## Statistik: Sx som räkningsstandard

Användarbeslut 2026-10-14: när eleven beräknar standardavvikelse från en
värdelista, frekvenstabell eller ett histogram ska uppgiften använda räknarens
**Sx**, med **n−1** i nämnaren. Skriv Sx i frågan så att måttet är entydigt.
Fråga, huvudfacit, delkort, ledtrådar, maskinsvar och tolerans ska följa samma
beräkning. Frekvenser räknas som antal observationer, inte antal tabellrader.
Histogram använder de angivna intervallmittpunkterna och ger uppskattningar.

Detta ersätter FP28–29:s tidigare pedagogiska val av σx för beskrivande
rådataberäkningar. Det betyder inte att de tidigare σx-beräkningarna var
matematiskt fel. Sx och σx är olika väldefinierade mått. Påstå inte att en grupp
är ett slumpmässigt stickprov utan stöd i uppgiften.

Behåll **σ som given parameter i normalfördelningar och sannolikhetsmodeller**.
Där finns ingen rådataberäkning att byta till n−1. Förskjutning och skalning
påverkar Sx enligt samma regler som andra standardavvikelser. Vid sammanslagning
av grupper använder varje grupp kvadratsumman (n−1)·Sx²; räkna också med
skillnaderna mellan gruppmedelvärdena. Om antalet observationer ändras ska även
nämnaren ändras. Uppgifter om oförändrad standardavvikelse måste lösas om helt.

### Verktyg för standardavvikelse

Senaste användarbeslutet 2026-10-14 ersätter den tidigare spärren för vanlig
miniräknare: standardavvikelseberäkningar tillåter GeoGebra **och** miniräknare.
Sätt `geogebra:true` och `miniräknare:true`. GeoGebra behövs för statistikfunktionen,
men tillståndet att använda den vanliga miniräknaren får inte dras in.
Separata korts uttryckliga verktygsmetadata går före förälderns, med det
överordnade kravet att tillåten GeoGebra alltid innebär tillåten miniräknare.

## Verktygsval i varje granskning

Användarbeslut 2026-10-14 gäller vid konstruktion, analys, rättning och revidering.
**Kontrollera alltid både `miniräknare` och `geogebra` för huvuduppgiften och varje
fristående delkort.** Verktygstaggar är en del av den pedagogiska granskningen,
inte något som får lämnas till en separat framtida kontroll.

1. Identifiera först vad eleven ska lära sig och vad svaret prövar.
2. Tillåt miniräknare när beräkningarna inte kan göras snabbt och enkelt i huvudet:
   till exempel multiplikation med stora tal utanför enkla tabellfakta (ungefär
   upp till 11:ans tabell), besvärliga divisioner, potenser, rötter, logaritmer
   och numeriska värden av sinus, cosinus och tangens.
3. Fråga: **Gör miniräknaren uppgiften för lätt eller tar den bort det som ska
   prövas?** Om svaret är nej får miniräknare gärna tillåtas även när den inte
   är absolut nödvändig. Gymnasiematematiken ska normalt inte pröva huvudräkning
   eller hur väl eleven ställer upp aritmetiska algoritmer för hand.
4. Tillåt GeoGebra när arbetet kräver digitala verktyg: digital grafanalys,
   grafritning/undersökning, statistiska mått från data, regression, numerisk
   lösning av ekvationer och mer avancerade integraler/derivator där ett digitalt
   verktyg behövs. Anger frågan att digitala verktyg ska/får användas måste
   metadata tillåta det. Att läsa av en redan given enkel figur kräver inte
   automatiskt GeoGebra.
5. **GeoGebra tillåtet ⇒ miniräknare alltid tillåten.** Detta gäller såväl
   huvuduppgift som delkort. En GeoGebra-tagg får aldrig kombineras med spärrad
   miniräknare, även om den inbyggda miniräknaren saknar en viss funktion.
6. Om ett verktyg skulle ge bort den metod, det samband eller det resonemang
   som uttryckligen prövas, gör ett pedagogiskt motiverat undantag. Exempel:
   användning av potenslagar, exakt symbolisk algebra eller en kvalitativ
   förutsägelse före digital beräkning. Motivera undantaget i granskningsloggen;
   ett stort tal eller ordet ”graf” räcker inte ensamt som beslutsgrund.
7. Kontrollera särskilt blandade uppgifter. En del som ska lösas utan digitalt
   verktyg och en annan som kräver det behöver skilda delkort/behörigheter.
   Hela uppgiftens tillstånd får inte blint användas för alla delar.

Fysikens tidigare regel gäller fortsatt: miniräknare är alltid tillåten i
Fysik 1 och 2. GeoGebra bedöms efter behovet av digitala funktioner.
Dokumentera verktygsbeslut tillsammans med nivå, facit och självrättning.
Heuristiska sökningar får hitta granskningskandidater men ska inte massändra
verktygsflaggor utan en pedagogisk bedömning.
