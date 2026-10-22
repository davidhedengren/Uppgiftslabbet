# Blandat sist i varje kapitel

Användaren prioriterar en tydlig ingång till blandad kapitelträning före
fortsatt påfyllnad av tunna områden. Kunskapsgymmet visar nu en vanlig knapp
med rubriken **Blandat**, sist efter områdena i varje kapitel. Den finns både
på kursöversikten och i Punktträna, i samtliga kurser och kursvarianter.
Inga bankobjekt dupliceras eller får nya områdesnycklar.

Urvalet använder befintliga spelbara uppgifter i valt spår och kapitel.
Fristående delkort, exkluderingar, nivåanpassning och tidigare resultat
använder samma motor som vanlig träning. Områden med minst antal visningar
i det pågående passet prioriteras, så ett stort område inte tar över.
Skyddet mot nyss visade uppgifter används före områdesvalet; ett uttömt
område behöver därför inte upprepas medan andra har osedda kort kvar.
Korta pass kan naturligtvis inte rymma alla områden i ett stort kapitel.

Testet upptäckte att samma områdesnyckel kan förekomma i flera kapitel,
bland annat i mato2. Kapitelurvalet måste därför byggas direkt från de
spelbara uppgifternas `kap`, inte från `getAreas()` som samlar per nyckel.
En separat kapitelavgränsning skyddar även lärarens uppgiftsbläddring.

Läget sparas i pågående pass och navigationshistorik, bevaras vid ett pass
till och återupptagning och rensas vid vanlig träningsstart/kurs-/spårbyte.
Resultat fortsätter höra till uppgiftens ursprungliga område, inte ett
konstgjort Blandat-område. Knappen har inget missvisande eget kunskapsmått.

Verifiering i konsumenten:

- `tools/kapitel-blandat.test.js`: jämn områdesfördelning trots olika
  bankstorlekar, rensning av filter, kapitelnycklar som återanvänds och
  knappens tangentbordsstöd.
- `tools/kapitel-blandat.browser.cjs`: 711 val från 69 kapitelurval över
  åtta kurser och alla 13 kurs-/spårkombinationer, utan fel kapitel, tomma
  urval, överhoppade områden eller upprepade ID:n i de testade passen.
- Verklig knappstart, återupptagning, fortsättning och byte till vanlig
  områdesträning vid 390/1280 px, i både ljust och mörkt läge. Inga
  JavaScript-fel eller horisontellt sidöverflöde.
- Befintliga tester för passhistorik, återbesök, nivåhållning och
  självrättning behålls. Hela konsumentens enhetssvit: 211 godkända tester.

Denna ändring fyller inte i sig på banker. Fortsatt innehållsarbete följer
användarens mål om 50–100 varierade nivå 1-kort per område och prioriterar
de tunnaste områdena. Variation ska vara metod, sammanhang, representation
och svarsform, inte enbart utbytta tal. Figur när den hjälper förståelsen.
