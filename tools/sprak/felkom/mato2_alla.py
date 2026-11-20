# Felkommentarer, Ma4 (mato2), alla återstående flervalsuppgifter (2026-11-20).
HOGER = 'Minus inne i parentesen flyttar grafen åt höger.'
VANSTER = 'Plus inne i parentesen flyttar grafen åt vänster.'
LODRATT = 'Ett tal inne i parentesen flyttar grafen i sidled. Bara ett tal utanför flyttar den uppåt eller nedåt.'
K = {
    '1.401': [None, 'sin x = 1 har bara lösningen x = 90°.', 'sin x kan aldrig vara större än 1 eller mindre än −1.',
              'sin x = −1 har bara lösningen x = 270°.'],
    '2.407': ['ln 1 = 0, så x = 1 är ett nollställe, inte en asymptot.', 'y = 0 är en vågrät linje, inte en lodrät.',
              None, 'ln x går mot −∞ när x går mot 0 från höger. Då finns en lodrät asymptot.'],
    '2.408': ['x = 0 är en lodrät linje, inte en vågrät.', 'e⁰ = 1 är värdet när x = 0. När x växer går e⁻ˣ mot 0.',
              None, 'e⁻ˣ går mot 0 när x växer, så y = 0 är en asymptot.'],
    '2.537': [None, 'Funktionen växer före x = 2 och avtar efter. Det ger en topp, inte en botten.',
              'Vid en terrasspunkt har derivatan samma tecken på båda sidor.', 'Funktionen är deriverbar i x = 2, så där finns ingen asymptot.'],
    '3.518': ['En kon bildas när en linje genom origo roteras.', None, 'Ett klot bildas när en halvcirkel roteras.',
              'En kub kan inte bildas genom rotation.'],
    '4.406': ['60° ligger i första kvadranten, men både real- och imaginärdelen är negativa.',
              '120° ligger i andra kvadranten, där realdelen är negativ men imaginärdelen positiv.',
              '300° ligger i fjärde kvadranten, där realdelen är positiv.', None],
    '4.401': ['−2i har negativ imaginärdel.', None, '2² + 4 = 8, inte 0.', '(−2)² + 4 = 8, inte 0.'],
    '1.634': ['Minus inne i parentesen flyttar grafen åt höger, inte åt vänster.', LODRATT, LODRATT, None],
    '1.653': ['Minus inne i parentesen flyttar grafen åt höger, inte åt vänster.', LODRATT, None, LODRATT],
    '1.654': ['Plus inne i parentesen flyttar grafen åt vänster.', None,
              'Ett tal utanför parentesen flyttar grafen uppåt, inte åt höger.',
              'Ett tal utanför parentesen flyttar grafen nedåt, inte åt höger.'],
    '1.657': [LODRATT, 'Plus inne i parentesen flyttar grafen åt vänster, inte åt höger.', LODRATT, None],
    '1.658': [None, 'Plus inne i parentesen flyttar grafen åt vänster.',
              'Ett tal utanför parentesen flyttar grafen uppåt, inte åt höger.',
              'Ett tal utanför parentesen flyttar grafen nedåt, inte åt höger.'],
    '2.548': ['Produktregeln ger två termer. Termen x²eˣ saknas.', None,
              'Produktregeln ger två termer. Termen 2xeˣ saknas.', 'Produktregeln: f′ = u′v + uv′, inte u′ · u · v.'],
    '2.549': [None, 'Det ska vara minus i täljaren, inte plus.', 'Man kan inte derivera täljare och nämnare var för sig.',
              'Termerna i täljaren har bytt plats, så tecknet blir fel.'],
}
