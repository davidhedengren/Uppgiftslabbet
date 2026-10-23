# Anpassningsbara paneler, 2026-10-23

Användarönskemål: smalare högerpanel på laptop, mer plats för uppgifterna
och möjlighet att dra panelgränserna själv.

- Standardbredd höger: 300 px vid 961–1440 px skärm, 360 px på större skärm.
- Standardbredd vänster: 236 px till 1180 px skärm, annars 252 px.
- Två dragbara avdelare. Bredden sparas lokalt under `ul-panelbredder-v1`.
- Dubbelklick/Home återställer respektive panels standardbredd.
- Avdelarna går att fokusera och styra med vänster/höger pil (10 px),
  eller Shift + pil (40 px). ARIA anger panel, orientering och bredd.
- Mittpanelen får minst 380 px. Sidoområdena kan inte dras så att de döljer
  mitten. Sparade önskemål anpassas till ett mindre fönster utan att skriva
  över inställningen vid en vanlig fönsterändring.
- Vid högst 960 px behålls den befintliga staplade layouten, utan avdelare.
  Avdelarna visas inte vid utskrift.
- Filerna laddas från `APP_ROOT`, även efter kursnavigering och på GitHub Pages.

Verifiering: `tools/panelstorlek.browser.cjs` körd i Chromium mot den faktiska
appen med Ma3-banken. Godkänt: standardbredder, dragning på båda sidor,
återläsning efter sidladdning, tangentbord, återställning, breddgränser,
961/960 px brytpunkt, 390/768/1024/1366/1920 px, utskrift och inga JS-fel.
Laptopbilden granskad visuellt: uppgiftskort, filter och högerpanelens knappar
har plats; mitten är 814 px vid 1366 px skärmbredd.

Inga uppgifter eller gemensamma bankfiler ingår i denna layoutändring.
