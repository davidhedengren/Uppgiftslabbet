# Instruktioner för alla AI-agenter

Läs `agent/ARBETSINSTRUKTION.md` och dess kompletterande regler före arbete.

Vid bankgranskning eller ändring av självrättning:

1. Läs `agent/FELMONSTER_OCH_BESLUT.md`.
2. Sök upp berörda uppgifts-ID:n och feltyper i `agent/` och relevanta tester.
   Läs tidigare motiveringar innan du ändrar text, facit, nivå eller svarstyp.
3. Följ upp varje feltyp med minst fem liknande uppgifter när sådana finns.
4. Kör de regressionstester som skyddar tidigare rättningar, samt relevanta nya kontroller.
5. Dokumentera nya fynd och beslut i granskningsloggen och uppdatera registret.

Återställ inte ett tidigare beslut utifrån hur andra uppgifter råkar se ut.
En ny rättning är tillåten när en självständig granskning visar att den behövs;
dokumentera då varför det tidigare beslutet ersätts och anpassa testerna efter
korrekt beteende. Ta aldrig bort en regressionstest enbart för att få grön körning.

Uppgiftslabbet är master för de gemensamma bankerna. Följ synkroniseringsreglerna.
