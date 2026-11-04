# Skiljelinjer mellan facit i PDF

Användarönskemål 2026-11-04: separera uppgifternas facit visuellt på samma sätt
som frågorna, så att lösningarna inte blandas ihop vid PDF-export.

`index.html`: utskriftens `.fu` får en underkant på 0,55 pt i #b8b8b8,
samma som `.pdf-pu`, och 9 pt luft före linjen. Regeln delas med
layoutpapprets facitstilar. Linjen ligger efter hela uppgiften, även när flera
kort har grupperats till a), b) osv. Långa facit får fortfarande delas över
sidor; ingen ny regel tvingar hela lösningen att hållas på en sida.

Verifierat med Chromium, appens `bladHTML` och riktiga bankfacit: åtta kort
grupperade till sju uppgifter, både prov och övningsblad, med/utan facit,
enkla och långa lösningar samt grupperade deluppgifter. Kontrollerat
utskrifts- och layoutstilar, inga KaTeX-fel. En sjusidigt exporterad A4-PDF
utan bakgrundsutskrift innehåller sju frågelinjer och sju facitlinjer.
Facitsidor med deluppgifter och sidöverskridande lösning är visuellt lästa.
Layoutredigeraren visar sedan tidigare enbart frågor; dess beteende ändras inte.

Inga uppgifter, facittexter, metadata eller Kunskapsgymmet-filer ändras här.
