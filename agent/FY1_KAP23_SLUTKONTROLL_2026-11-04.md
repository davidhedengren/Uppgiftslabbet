# Fy1 kapitel 2–3: slutkontroll 2026-11-04

## Omfattning och avgränsning

Kapitel 2–3 omfattar **931 huvuduppgifter och 732 explicita delfacit**. Denna sessions manuella omarbetning omfattar enheter (71/110), mätnoggrannhet (68/9), densitet (178/53) och medelhastighet (92/125), totalt 409 huvuduppgifter och 297 delkort. Fullständiga ID-listor, beräkningar och beslut finns i respektive områdeslogg.

De återstående 522 huvuduppgifterna och 435 delkorten har omarbetats i den parallella sessionen, enligt `FY1_KONSTACC_FACIT_2026-11-04.md` och `FY1_RORELSE_FACIT_2026-11-04.md`. Här efterkontrolleras deras struktur och rendering i båda apparna. Detta är **inte** en ny oberoende numerisk omräkning av samtliga 522 uppgifter. Tidigare numeriska regressionstester körs också.

| Område | Huvuduppgifter | Explicita delfacit |
|---|---:|---:|
| Konstant acceleration | 135 | 232 |
| Acceleration | 48 | 62 |
| Vektorer | 166 | 57 |
| s–t-diagram | 54 | 26 |
| v–t-diagram | 68 | 46 |
| a–t-diagram | 51 | 12 |

## Fynd och ändringar i efterkontrollen

- **77 huvudfacit och 58 delfacit:** 93 olika långa formeluttryck får radbrytningar. Uttrycken har lästs före ändring. Ett tokenjämförelsetest visar att alla tal, matematiska operatorer och enheter i radbrytningsplanen är bevarade. Planen är explicit, inte en generell massomskrivning av facit.
- **3.222:** HTML tolkade `&gt` i TeX-alignment som >, så själva formeln visades fel trots giltig KaTeX. Alignmenttecknet placeras nu efter vänsterledet. Alla 1 663 facit kontrolleras mot denna feltyp.
- **3.65:** uppgiftens modellantagande flyttas före del a och den avslutande resonemangsfrågan blir uttryckligen del d. Fyra delar i frågan motsvarar nu facitets fyra delar. Inga givna data ändras.
- **3.388:** det exakta värdet 142/11 från del a används i accelerationsberäkningen i stället för att sätta ett avrundat mellanled lika med ett exakt bråk. Slutresultat och rättningsnycklar är oförändrade.
- Uppföljningen omfattar fler än fem analoger per mönster. Listorna i 2.15 och 2.64 är värden/alternativ, inte separata delfrågor; de ska inte mekaniskt skapa extra delfacit.

Totalt **78 uppgifter åtgärdade och 444 granskade utan ytterligare fynd i denna efterkontroll**. Statusen gäller denna omgång; de 444 kan ha fått sina äldre facit omskrivna i den parallella omgången. Ingen rapportstatus eller kommentar har skickats till Supabase.

## Kontroller

- Samtliga 957 huvud-/delfacit i de sex områdena renderade i Chromium, KaTeX 0.16.11, mobilbredd 390 px med respektive apps CSS: inga formelfel eller överskjutande matematikrader, rubriker eller svarsrutor efter ändringarna.
- Visuell läsning av de mer omfattande radbrytningarna i 3.86, 3.118, 3.222 och 3.388. De sista justeringarna kontrolleras på nytt.
- De övriga 706 huvud-/delfaciten är renderade och kontrollerade i sina respektive manuella områdesomgångar. Summa 1 663.
- Nytt regressionstest skyddar alla 931/732 facitstrukturer, miniräknartillgång, HTML/TeX-felet, de 93 formlernas matematiska innehåll och 3.65:s delindelning. Tidigare numeriska tester och facitregressioner passerar.
- Inga nivåer, svarsenheter, toleranser eller rättningsnycklar ändras i denna efterkontroll. Verktygsbeslut från de manuella omgångarna bevaras; huvuduppgifter och delkort tillåter miniräknare.

## Alla granskade uppgifter och kommentarsförslag

Fullständiga separata listor över granskade, åtgärdade och granskade utan nytt fel finns även i JSON-filen med samma namn.

| ID | Status | Förslag på kommentar |
|---|---|---|
| 3.4 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.5 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.6 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.7 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.230 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.10 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.11 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.12 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.13 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.240 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.14 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.15 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.16 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.241 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.17 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.18 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.231 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.22 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.23 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.24 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.25 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.26 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.27 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.28 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.29 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.30 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.31 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.242 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.32 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.33 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.34 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.243 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.35 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.36 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.37 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.38 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.39 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.40 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.244 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.41 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.42 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.43 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.44 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.232 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.45 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.46 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.47 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.245 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.48 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.233 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.52 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.56 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.57 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.59 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.60 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.246 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.61 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.62 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.63 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.64 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.252 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.65 | Åtgärdad | Modellantagandet står nu före beräkningarna och resonemangsfrågan är tydligt märkt som del d, precis som i facit. |
| 3.66 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.67 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.68 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.69 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.70 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.71 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.72 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.73 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.74 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.75 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.76 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.77 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.78 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.79 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.80 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.81 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.82 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.83 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.84 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.85 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.86 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.87 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.88 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.89 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.90 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.91 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.92 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.93 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.94 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.95 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.98 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.100 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.105 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.106 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.247 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.107 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.108 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.109 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.110 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.111 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.248 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.112 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.113 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.114 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.249 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.115 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.116 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.117 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.253 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.118 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.119 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.120 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.121 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.122 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.123 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.124 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.135 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.136 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.137 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.138 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.139 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.250 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.140 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.141 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.142 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.251 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.143 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.144 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.145 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.146 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.147 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.148 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.149 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.150 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.151 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.152 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.153 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.154 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.155 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.156 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.157 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.158 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.159 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.160 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.161 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.162 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.163 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.164 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.165 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.166 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.167 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.168 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.169 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.254 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.170 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.171 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.172 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.173 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.174 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.175 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.176 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.177 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.180 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.181 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.182 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.183 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.239 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.184 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.185 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.186 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.187 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.188 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.189 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.190 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.191 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.192 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.193 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.194 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.195 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.196 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.197 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.198 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.199 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.200 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.201 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.202 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.203 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.204 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.205 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.206 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.207 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.208 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.209 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.210 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.211 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.212 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.255 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.213 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.214 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.215 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.216 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.217 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.218 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.219 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.220 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.221 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.222 | Åtgärdad | Formeln visades fel eftersom gt tolkades som ett HTML-tecken. Nu visas gt = 4g(t − 2,50) korrekt och uträkningen är uppdelad i tydliga rader. |
| 3.223 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.224 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.225 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.226 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.227 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.228 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.263 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.264 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.265 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.266 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.267 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.268 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.362 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.365 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.269 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.270 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.271 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.272 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.273 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.274 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.275 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.276 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.277 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.278 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.369 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.370 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.371 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.372 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.373 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.374 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.375 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.376 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.377 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.378 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.379 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.380 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.381 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.382 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.383 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.384 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.385 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.386 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.387 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.388 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. Accelerationen beräknas med det exakta värdet från a), innan svaret avrundas. |
| 3.389 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.390 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.391 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.392 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.393 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.394 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.395 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.396 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.397 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.398 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.399 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.400 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.401 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.402 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.403 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.404 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.405 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.406 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.407 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.408 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.409 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.279 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.360 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.363 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.368 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.280 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.281 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.282 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.283 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.284 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.285 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.294 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.295 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.296 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.297 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.298 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.299 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.300 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.309 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.310 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.311 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.312 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.313 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.317 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.318 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.320 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.326 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.330 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.333 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.340 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.345 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.346 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.347 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.348 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.349 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.350 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.351 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.352 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.353 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.354 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.355 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.361 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.364 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.356 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.357 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.358 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.359 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.367 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.410 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.411 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.412 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.413 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.414 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.415 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.416 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.417 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.418 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.419 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.420 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.421 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.422 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.423 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.424 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.425 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.426 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.427 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.428 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.429 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.430 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.431 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.432 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.433 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.434 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.435 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.436 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.437 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.438 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.439 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.440 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.441 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.442 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.443 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.444 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.445 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.446 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.447 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.448 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.449 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.450 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.451 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.452 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.453 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.454 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.455 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.456 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.457 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.458 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.459 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.460 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.461 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.462 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.463 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.464 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.600 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.601 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.602 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.603 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.604 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.605 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.606 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.607 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.608 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.609 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.610 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.611 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.612 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.613 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.614 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.615 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.616 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.617 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.618 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.619 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.620 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.621 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.622 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.623 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.624 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.625 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.626 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.627 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.628 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.629 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.630 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.631 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.632 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.633 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.634 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.635 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.636 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.637 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.638 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.639 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.640 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.641 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.642 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.643 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.644 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.645 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.646 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.647 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.648 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.649 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.650 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.651 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.652 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.653 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.654 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.655 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.656 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.657 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.658 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.659 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.660 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.661 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.662 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.663 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.664 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.665 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.666 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.667 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.668 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.669 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.670 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.671 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.672 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.673 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.674 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.675 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.676 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.677 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.678 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.679 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.680 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.681 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.682 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.683 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.684 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.685 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.686 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.687 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.688 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.689 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.690 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.691 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.692 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.693 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.694 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.695 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.696 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.697 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.698 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.699 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.700 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.701 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.702 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.703 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.704 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.705 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.706 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.707 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.708 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.709 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.710 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.711 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.712 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.713 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.714 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.715 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.716 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.717 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.718 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.719 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.720 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.721 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.722 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.723 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.724 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.725 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.726 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.727 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.728 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.729 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.730 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.731 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.732 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.733 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.734 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.735 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.736 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.737 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.738 | Åtgärdad | Facitets långa uträkningar har delats upp på fler rader för att vara läsbara på mobilen. |
| 3.739 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.740 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.741 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.742 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.743 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.744 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
| 3.745 | Granskad – inget fel | Facitets stegstruktur, svarsrutor och mobilvisning har efterkontrollerats utan ytterligare fynd. |
