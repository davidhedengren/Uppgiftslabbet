# Repetera inför Nationella provet

Användarbeslut 2026-10-23: ett eget område sist i matematikkurserna, med
självständiga repetitionsuppgifter som tränar kunskaper och uppgiftstyper
från frisläppta nationella prov. **Ma5/matf1 ska vänta.**

## Genomfört

Första omgången omfattar 80 nya uppgifter i båda apparna:

| Bank | Kapitel | ID:n | Antal |
|---|---:|---|---:|
| ma1 | 8 | 8.01–8.20 | 20 |
| ma2 | 6 | 6.01–6.20 | 20 |
| mato1 | 5 | 5.01–5.20 | 20 |
| mato2 | 6 | 6.01–6.20 | 20 |

Spårfiltrering gör att varje elev ser relevant innehåll. Ingen gammal uppgift
har duplicerats till ett nytt ID i repetitionsområdet. Frågorna har egna
formuleringar, tal, sammanhang, figurer och lösningar. Området anger att de
inte är officiella provuppgifter. De är vanlig träning med bankens verktygsregler,
inte en simulering av ett visst originalprovs delprov eller poänggränser.

Se [granskningsloggen](REPETITION_2026-10-23.md) och
[alla 80 uppgifters granskningsmetadata](REPETITION_2026-10-23.json).
Författarkällan finns i `tools/bygg-np-repetition-2026-10-23.py`.
Den innehåller handskrivna uppgifter och återanvändbara figurhjälpare;
den importerar inga provtexter och vägrar skriva över befintliga ID:n.

## Underlag och avgränsning

- PRIM-gruppens officiella arkiv: https://www.su.se/enheter/prim-gruppen/nationella-prov/niva-1-kurs-1
- Umeå universitets officiella arkiv: https://www.umu.se/institutionen-for-tillampad-utbildningsvetenskap/np/np-2-4/tidigare-givna-prov/
- `kallregister.json`: 232 dokumentlänkar för 142 kurs-/terminskombinationer.
  Detta är en länkinventering, **inte 232 genomgångna prov**.
- Första omgångens tematiska underlag: VT22, Ma1a/b/c delprov B samt
  Ma2a/b/c, Ma3b/c och Ma4. `repetition.underlag` är en tematisk hänvisning,
  inte ett påstående om att en viss egen uppgift motsvarar ett bestämt
  originalnummer. Ämnesplansbaserade kompletteringar ingår också.
- `amnesplaner-gy25.json`: Skolverkets MATE, MATO och MATF, version 1,
  giltiga från 2025-07-01. MATF-snapshoten är källmaterial; inga Ma5-uppgifter
  har konstruerats eller publicerats i denna omgång.

Alla historiska prov är **inte** genomgångna. Registrets `not_reviewed`
gäller uppgiftsvis fullständig arkivgranskning, som återstår. Tematisk läsning
av VT22 ändrar inte den statusen. Original-PDF:er, provtexter och
bedömningsanvisningar finns inte i repot.

Tidigare återpubliceringstillstånd har inte verifierats. Användaren har ändrat
uppdraget till egna repetitionsuppgifter. Ingen tillståndsfråga väntar på svar.
Att ett prov är frisläppt från sekretess är inte i sig en återpubliceringslicens.
Märk därför inte egna uppgifter med exempelvis ”NP Ma3c HT18” så att de ser
ut att vara original, och skapa inte en systematisk nära omskrivning av hela prov.

## Fortsatt arbete

1. Analysera fler frisläppta prov för kunskapskrav, variation och luckor.
2. Konstruera självständiga uppgifter mot dagens ämnesplan och aktuellt spår.
3. Dokumentera exakt vad som lästs, vad som konstruerats och vad som återstår.
4. Kontrollera matematik, språk, nivå, verktyg, självrättning och figurer per ID.
5. Använd samma bankobjekt i båda apparna. Lägg inte samma fråga under flera
   ID:n för att skapa skenbar mängd eller separat progression.

Arkivets Ma1b-sektion innehåller en länk märkt Ma1a VT13 delprov B. Den
källavvikelsen är noterad i registret och får inte automatiskt klassificeras
som Ma1b. Äldre MaA-material kräver egen innehållsgranskning.
