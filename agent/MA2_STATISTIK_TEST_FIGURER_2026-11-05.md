# Ma2 – regressionstest för figurer, 5 november 2026

`tools/ma2-s5-2026-10-25.test.js` förväntade sig exakt 27 figurer i 53 uppgifter och misslyckades när en korrekt 28:e figur hade lagts till. Historiken visar att Ma2 3.2116 saknade figur i den ursprungliga versionen och fick en efter en felrapport; se `FELRAPPORTER_2026-11-05_0758.md`.

Testet kontrollerar nu att samtliga 27 ursprungliga figuruppgifter och den senare tillagda 3.2116 fortfarande har figurer. Det fortsätter kontrollera tillgänglighetsbeskrivningarna och alla övriga matematiska egenskaper, men tillåter att fler figurer läggs till. Hela testfilen passerar. Inga uppgifter eller rapportstatusar har ändrats.
