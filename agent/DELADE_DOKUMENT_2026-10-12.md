# Accepterade delningar saknas i Mina prov – 2026-10-12

Rapport: en kollega har delat ett prov. Mottagaren har accepterat men hittar
inte provet i ”Mina prov och övningsblad”.

## Bekräftad orsak och åtgärd

`minaHämta()` hämtar kontots dokument med `ul_mina`. `minaRita()` filtrerade
sedan listan till enbart `roll === 'agare'`. Alla mottagna dokument försvann
därmed ur den nya Mina-vyn. Den äldre laddadialogen visar redan hela samma
RPC-lista, och `minaPost()` har redan stöd för etiketten ”Delat av …” och
knappen ”Lämna” för mottagare.

Ägarfiltret är borttaget i Mina-listan. Det gäller både prov och övningsblad.
Listan visar fortfarande endast det som den befintliga `ul_mina`-funktionen
returnerar för användaren. Sökning, sortering och uppdelning efter dokumenttyp
behålls. Den gemensamma banken använder fortsatt sin separata RPC-lista och
visar inte personliga delningar genom denna ändring.

Efter lyckad acceptans öppnas nu ”Mina prov och övningsblad” med en ny hämtning,
rätt rubrik och rensat sökfält. Tidigare stod mottagaren kvar i förfrågningsvyn
efter att inbjudan försvunnit. Vid avböjning stannar man i förfrågningsvyn.
Vid misslyckad acceptans visas felet och knappen går att använda igen.

Mina-vyns introduktion förklarar också att kollegors delade dokument ingår.
Ägarens och mottagarens befintliga åtgärder behålls: mottagaren lämnar dokumentet
i stället för att radera originalet. Ägarens publiceringsknapp visas inte för
mottagaren. Databasbehörighet, RPC, SQL och uppgiftsbanker har inte ändrats.

## Verifiering

- `tools/delade-dokument.test.js` kör den faktiska listfunktionen. Mot den
  gamla versionen misslyckas testerna för mottagna dokument och sökning;
  testet för gemensamma banken passerar. Efter rättningen passerar alla tre.
- Tillsammans med `tools/sparskydd.test.js`: **15/15 godkända**, inklusive
  skyddet för osparade utkast och uttrycklig sparning av delade original.
- `tools/delade-dokument.browser.py` använder den riktiga vyn, riktiga knappar
  och verkliga `delningÖppna`/`sparLaddaDokument`, med isolerade RPC-fixturer.
  Den kontrollerar redan mottaget prov/övningsblad, accepterad ny inbjudan,
  uppdaterad lista, sökning, avböjning, misslyckad acceptans med återaktiverad
  knapp, separat skolbank, mottagarens åtgärder och öppning av ett delat prov
  med en uppgift. Mobil 390 px och dator 1280 px är visuellt kontrollerade.
  Inga JavaScript-fel uppstod.
- Supabase-trafik blockeras i webbläsartestet. Inga riktiga inbjudningar,
  prov, medlemskap eller konton har ändrats genom testerna. Kollegornas
  specifika liveposter har inte hämtats; rättningen avser det återskapade
  frontendfelet, inte en utförd databasreparation.
- Syntax och `git diff --check` kontrolleras före leverans. Ändringen gäller
  bara Uppgiftslabbet; Kunskapsgymmet behöver ingen synk.

Kommentar till användaren: ”Mina prov visade bara dokument du själv äger.
Nu visas också dokument som kollegor delat med dig. Efter acceptans öppnas
dokumentlistan direkt.”
