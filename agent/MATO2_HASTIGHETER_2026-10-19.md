# Mato2: förändringshastigheter, 2026-10-19

Åtta uppgifter manuellt granskade: **2.125, 2.184, 2.212, 2.180, 2.182,
2.186, 2.187, 2.188**. Tre åtgärdade, fem granskade utan ytterligare fel.
Tidigare beslut i FP59/64/65 bevaras. Detta är en avgränsad omgång, inte en
utfästelse om att hela banken är felfri.

## Åtgärder och kommentarsförslag

| ID | Kommentar |
|---|---|
| 2.125 | Åtgärdad: både exakt och avrundat volymsvar godtas. Tiden 28,1 s i lösningen godtas nu också. Lösningarna visar beräkningarna utan orelaterade metodtexter. Det fristående b-kortet har bara sina egna givna värden och en figur med radien 15 cm. |
| 2.184 | Åtgärdad: förklaringen om parabler är ersatt med kvadratens area och kedjeregeln. Enheterna m respektive m/s godtas. En tydlig kvadratfigur är tillagd. a-kortet är E/nivå 2, b-kortet C/nivå 3. |
| 2.212 | Åtgärdad: lösningen visar varför 80π divideras bort och radien ökar med 1 cm/s. Svar med enheten cm/s godtas. Figurens radielinje når kanten och etiketten överlappar inte ellipsen. |

2.125: dV/dt=4π·10²·0,40=160π cm³/s; V(15)=4500π cm³;
t=4500π/(160π)=28,125 s. Gamla toleransen 0,01 uteslöt lösningens 28,1;
FP65:s nya avrundningsregel verifieras i det verkliga svarsfältet. a byter
uttrycksformat till numeriskt, med fullprecisionsmål och bibehållen enhet.
Det fristående b-kortet får E/nivå 2 eftersom volymökningen redan är given;
heluppgiften och a behåller C/nivå 3. Ballongens gamla radieetikett flyttas
också bort från pilen, i huvudtext och spelintro.

2.184: dA/ds=2s=6 m; ds/dt=1,8/6=0,30 m/s. Huvudpoäng justeras till
1/2/0 för att spegla delarnas bedömning. b-facit härleder sitt eget mellanled.
2.212: V=10πr²; 80π=20π·4·dr/dt ger dr/dt=1 cm/s, C/nivå 3.

Alla tre tillåter räknare. GeoGebra tas bort: det är kedjeregeln och enkla
samband som prövas, ingen digital grafanalys eller avancerad numerisk lösning
behövs. Verktygsval gäller även de separata korten. ID:n bevaras.

## Granskad – inget fel, med kommentarsförslag

| ID | Kommentar |
|---|---|
| 2.180 | Granskad – inget fel: dr/dt=40/(16π)≈0,80 m/min. Exakt värde och rätt avrundning godtas. |
| 2.182 | Granskad – inget fel: radien minskar med 1/(2π)≈0,16 cm/min. Lösningen skiljer den positiva minskningen från den negativa derivatan. |
| 2.186 | Granskad – inget fel: h=3r ger V=πr³ och dr/dt=0,12/(3π·0,80²)≈0,0199 m/min. |
| 2.187 | Granskad – inget fel: dA/dr=12π≈37,7 km och dA/dt=4,8π≈15,1 km²/min. Precision och enheter anges. |
| 2.188 | Granskad – inget fel: dr/dt=5/(2π)≈0,80 m/s och dA/dt=20 m²/s. b-lösningen härleder radiens ökning själv. |

## Verifiering

72 faktiska svarskontroller och 48 visningar i elev-/lärargränssnittet vid
390/1280 px passerar, utan JavaScriptfel, KaTeXfel eller klippta formler.
Nya tester kontrollerar volymderivatan med oberoende numerisk differens,
hela fyllnadstiden samt enheter och fristående kort. Tidigare regressioner
för FP59, FP64, FP65 och bankvalidatorn passerar.
SVG-analys efter rättning: inga ERROR/WARNING; tre INFO gäller avsiktliga vita
bakgrundsrektanglar som fyller viewBox. Figurerna har också granskats visuellt.
Bankvalidatorn har samma 72 befintliga fynd före/efter, inga nya.
Före/efter för alla ändringar finns i motsvarande JSON. Inga elevkommentarer
har skickats och inga produktionsrapporter har avslutats.
