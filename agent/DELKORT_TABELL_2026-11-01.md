# Fortsatt delkortsgranskning 1 november 2026

## Ändrade uppgifter

**Ma2 2.436 a–c:** Originaluppgiften innehåller en tabell, men de tidigare
fristående a/b-korten skrev ut funktionens värden som en lista och hänvisade
ändå till en tabell. Nu följer originaltabellen med alla tre delarna. I
kedjevisning visas tabellen en gång. A ger −3, b ger 0 och c ger den ordnade
punkten (−3, 6). C behåller egna x/y-etiketter och `svarsstruktur:ordnad`.
Ingen tidigare lösning eller rättningsdata har ändrats; miniräknare är
tillåten och GeoGebra behövs inte. Detta bevarar beslutet i
`FELRAPPORTER_2026-10-11_1618.md` om separata facit och ordnade koordinater,
men ersätter det tidigare kortunderlaget med originalets faktiska tabell.

**Ma4 3.116 a:** I en delkedja syns avslutade tidigare delar. Figuren i a
har därför fått texten ”Figuren hör till del a”, så att den inte misstas för
grafen i b eller c. B/c har funktionsuttryck och intervall i text och kräver
inte a:s figur. Volymerna är fortsatt \(26\pi/3\), \(8\pi\) och \(12\pi\),
och båda digitala verktygen är tillåtna. Detta bevarar tidigare beslut i
`FELRAPPORTER_2026-10-20_0703.md` och ändrar inte figuren eller funktionen.

**Kunskapsgymmet:** Svarsfält inom ett redan fristående delkort, exempelvis
x- och y-koordinaten i 2.436 c, kallas nu ”Svar 1 av 2” och ”Svar 2 av 2”
i stället för att felaktigt kallas nya deluppgifter. Detsamma gäller andra
namngivna svarsfält. Riktiga a/b-delar på en heluppgift behåller benämningen
deluppgift. Rättningsordning och sparade svar är oförändrade.

## Liknande fall granskade utan ändring

- Tabellhänvisningar kontrollerades maskinellt i alla sju banker. Ma1 2.16 b
  och 2.70 c ber eleven **skapa** en tabell, så någon befintlig tabell saknas
  inte. Ma1 2.24 och 2.269 samt Ma2 1.12, 1.104 och 2.428 har redan tabellen
  i sina faktiska delkort. Dessa lämnades oförändrade.
- Ma4 3.116 b/c behöver inte figuren från a, eftersom respektive funktion
  och intervall är uttryckligen givna. Rubriken till a:s figur förtydligas
  så att den inte kopplas till de andra funktionerna.
- Sökning efter uttryckliga hänvisningar till svar från tidigare delar gav
  inga träffar bland synliga delkort. Det är inte ett bevis mot alla
  indirekta beroenden eller alla pedagogiskt otydliga formuleringar.

## Kontroller

`delkort-tabell-2026-11-01.test.js` kontrollerar tabellinnehåll, metadata,
ordning och rotationsvolymer. Motsvarande webbläsartest i Kunskapsgymmet
provar hela kedjan, en enda synlig tabell, korrekt och omkastad koordinatordning,
svarsstegens benämning och figurtexten. Både tidigare kedjeprov och
8 659-kortskontrollen kördes igen. Testsviterna har samma kända miljö- och
basversionsfel som i `DELKEDJOR_OCH_FACIT_2026-11-01.md`: mastersviten
godkände 1 058 av 1 101 tester, där de 43 misslyckade hör till SVG-verktygets
Chrome-beroende; Kunskapsgymmet godkände 304 av 314 och samma tio tester
misslyckas även på oförändrad basversion.

Ingen rapportstatus eller kommentar har skrivits till produktionsdatabasen.
