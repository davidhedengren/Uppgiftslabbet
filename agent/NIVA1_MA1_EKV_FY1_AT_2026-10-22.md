# Nivå 1-påfyllnad: Ma1 ekvationer och Fy1 at-diagram – 2026-10-22

Påfyllnaden följer målet om 50–100 varierade kort på nivå 1 per område (se `CLAUDE.md`). Områdena valdes efter vad som undervisas nu:

- **Ma1a (VF26A 2627):** ekvationer med flera variabeltermer och parenteser läses v.43. Bråk och problemlösning med ekvationer följer v.45–46.
- **Fysik 1 (2627):** at-diagram läses v.43.

## Ma1 1.1300–1.1385 (86 kort)

| Område | Före | Efter | Innehåll |
|---|---|---|---|
| ekv_flera_variabeltermer | 1 | 25 | balansvåg med lådor och vikter, påsar och kulor, värdetabell, skärning mellan grafer, ingen lösning eller oändligt många lösningar, första steget, hitta felet, abonnemang, ljus som brinner, vattentankar (graf), spargrisar, parametrar |
| ekv_parenteser | 3 | 25 | dela först, minustecken framför parentes, hitta felet, kvadrat och triangel med samma omkrets, bio med popcorn, rektangelns area, hage, välja ekvation |
| ekv_brak | 5 | 25 | x/4 = 6, medelvärde, dela en nota, x i nämnaren, multiplicera bort nämnaren, stapelmodeller (en tredjedel av klassen, en fjärdedel av vägen), förenkla x/2 + x/2, hitta felet |
| ekv_problemlosning | 4 | 24 | tänk på ett tal, taxi, ålder, vinklar i en triangel, prislinjer (graf), tre tal i rad, påsar med bullar, timlön, likbent triangel, rep, cykelsparande, välja ekvation |

- Alla ekvationer kontrolleras med sympy när korten byggs.
- Kort som bara ber om att lösa eller förenkla har `miniräknare: false`. Textuppgifter med jobbigare tal tillåter räknare.
- Validatorn fann tre textmallar som liknade befintliga kort (1.1311, 1.1325 och 1.1380). De korten är omformulerade.

## Fy1 3.600–3.619 (20 kort, at_diagram 5 → 25)

- **Tolka:** läsa av a, hur länge en bil accelererar, välja diagram för konstant hastighet (fyra små diagram), negativ a och farten, vad arean betyder, fritt fall, när hastigheten ökar snabbast, enheten för arean.
- **Hastighetsändring:** elsparkcykel, bil med starthastighet, inbromsning, hiss, raket, tåg med 60 s tidsaxel, a = 0, spurt, hiss som bromsar (Δv med tecken).
- **Lutning:** a ur ett v-t-diagram (motorväg och skidåkare).

**Lärdom:** ett avläst värde som inte är ett heltal, till exempel 1,5 m/s², godtas också avrundat till 2, enligt avrundningsregeln från 2026-10-19. Hissens acceleration ändrades därför till 1 m/s².

`tools/fysik1-kapitel3.test.js`: at-listan omfattar nu 3.455–3.460 och 3.600–3.619. Delen för at_diagram går igenom. De övriga fem delarna underkändes redan tidigare, eftersom deras id-listor är inaktuella.

## Verifiering

- **Validator:** inga nya fynd i de två bankerna.
- **SVG-granskning:** 0 fynd, efter rättelser av axelnamn, vinkeletiketter och staplade vikter och kulor på vågen.
- **Tester:**
  - `tools/ma1-niva1-ekvationer-2026-10-22.test.js` sätter in facit i 62 ekvationer;
  - `tools/fysik1-niva1-at-diagram-2026-10-22.test.js` kontrollerar formatet;
  - kapitel 3-testet räknar om facit.
- **Kunskapsgymmet:** rättningen är prövad med 64 svar, bland annat x = 4, 4 kg, 4000 g, −2, 5/2, 0,5x, 20 minuter, 40°, 72 km/h och −3 m/s².
