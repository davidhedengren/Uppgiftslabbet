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
