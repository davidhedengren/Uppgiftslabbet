# Fokus i svarsfält, 2 november 2026

När en uppgift öppnades satte Kunskapsgymmet fokus på första svarsfältet efter 60 ms. Om eleven redan hunnit välja nästa fält flyttades fokus tillbaka, så att nästa svar kunde hamna i första fältet. Det återskapades på Ma4 **1.132** och **1.299** med flera svar i samma del.

Appen fångar nu den aktuella rutan och uppgiften när fokus planeras. Den automatiska fokusflytten genomförs bara om eleven inte har flyttat fokus, rutan fortfarande är kopplad till samma vy och administratören inte bläddrar. Samma skydd används när nästa svarssteg öppnas. Bytet mellan siffer- och texttangentbord får också bara återföra fokus om eleven inte hunnit välja ett annat fält. Standardfokus till första rutan och till nästa svarssteg behålls när eleven inte gjort något annat.

Liknande situationer granskades: nytt kort, flera rutor samtidigt, byte av uppgift, stegvis svar med Ma1 **2.201**, byte av tangentbord samt avslut av papperspåminnelsen. Papperspåminnelsens fokus sker direkt när eleven stänger den, medan symbolknapparna uttryckligen återför fokus till den aktuella svarsrutan; de har inte ändrats.

Webbläsartestet `svarsfokus-2026-11-02.browser.cjs` återskapade först felet före ändringen och kontrollerar sedan snabbt fältbyte, standardfokus, uppgiftsbyte, tangentbordsbyte och stegvis svar. Svaren kontrolleras också faktiskt. Regression körs för trigonometriska svarsmängder, återupptagning och tidigare delfacit. Hela testsviter körs före push; se leveransen för tidigare kända fel. Ingen rapportstatus eller kommentar har sparats i appen.

Testutfall: fokustestet samt testerna för svarsmängder, passflöde och delfacit passerade. Hela sviten gav 1 068 godkända och 43 tidigare kända SVG-miljöfel i Uppgiftslabbet samt 304 godkända och 10 tidigare kända fel i Kunskapsgymmet.
