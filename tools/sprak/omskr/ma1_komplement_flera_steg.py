"""Handgranskning av Ma1, komplementhändelse och sannolikhet i flera steg (2026-11-20).

Frågefragment ("Sannolikheten att …?") blir hela frågor, "Vad är sannolikheten" heter "Hur stor är sannolikheten",
svarsform i parentes blir en vanlig mening, abstrakta "steg"-uppgifter får ett sammanhang och "En elev" får namn.
5.163 c: delkortet frågade efter alla möjliga nettovinster men rättades mot huvuduppgiftens c (nettovinst vid träff på
fjärde kastet = 1). Delkortet frågar nu samma sak som huvuduppgiften (svarsraden i delkortets facit rättas i ma1_facit_5163.py).
"""
HUR = 'Hur stor är sannolikheten'
R = {
    # komplementhändelse
    '5.19': {'ers': [('Vad är sannolikheten för komplementhändelsen?', f'{HUR} för komplementhändelsen?')]},
    '5.148': {'ers': [('Vad är sannolikheten att resultatet inte är en sexa?', f'{HUR} att resultatet inte är en sexa?')]},
    '5.168': {'ers': [('Vad är sannolikheten att inte vinna?', f'{HUR} att inte vinna?')]},
    '5.18': {'ers': [('Tre oberoende komponenter har vardera 92 % sannolikhet att fungera. Bestäm sannolikheten att minst en inte fungerar.',
                      f'Ett system har tre komponenter. Varje komponent fungerar med sannolikheten 92 %, oberoende av de andra. {HUR} att minst en komponent inte fungerar?')]},
    '5.32': {'ers': [('En maskin producerar en godkänd detalj med sannolikheten 0,92. Fem detaljer betraktas som oberoende.',
                      'En maskin tillverkar en godkänd detalj med sannolikheten 0,92, oberoende av tidigare detaljer. Maskinen tillverkar fem detaljer.'),
                     ('Bestäm sannolikheten att minst en blir underkänd.', f'{HUR} att minst en detalj blir underkänd?')]},
    '5.139': {'ers': [('Sannolikheten att vinna två gånger i rad?', f'{HUR} att vinna två gånger i rad?'),
                      ('Sannolikheten att vinna minst en gång på 8 spel?', f'{HUR} att vinna minst en gång på 8 spel?')]},
    '5.141': {'ers': [('Anta att bona kan behandlas som oberoende.', 'Antag att fåglarna i de olika bona är oberoende av varandra.')]},
    '5.142': {'ers': [('<p>Svara också i procent.</p>', f'<p>{HUR} att paketet blir försenat? Svara i procent.</p>'),
                      ('b) Svara också i procent.', 'b) Svara på a i procent.')]},
    '5.143': {'ers': [('(1-4)', '(1–4)'), ('(1-6)', '(1–6)')]},
    '5.254': {'ers': [('Försöket upprepas 3 gånger oberoende. Bestäm sannolikheten för <strong>minst en träff</strong>.',
                       f'Försöket görs tre gånger, oberoende av varandra. {HUR} för <strong>minst en träff</strong>?')]},
    '5.256': {'ers': [('i varje av fyra oberoende försök', 'i vart och ett av fyra oberoende försök')]},
    '5.257': {'ers': [('En elev säger:', 'Noah säger:')]},
    '5.258': {'ers': [('i varje av fem oberoende försök', 'i vart och ett av fem oberoende försök'), ('En elev uppskattar', 'Alva uppskattar')]},
    '5.459': {'ers': [('att hon träffar minst en gång', 'att personen träffar minst en gång')]},
    '5.460': {'ers': [('Tre fröer sås.', 'Tre frön sås.')]},
    '5.463': {'ers': [('P(A) = 0,4. En elev påstår att P(inte A) = 0,4 också.', r'För en händelse \(A\) gäller \(P(A)=0{,}4\). Lukas påstår att \(P(\text{inte }A)=0{,}4\) också.')]},
    '8.08': {'ers': [('(Svara i procent.)', 'Svara i procent.')]},
    '5.618': {'ers': [(' (Svara med ett heltal.)', '')], 'kg': 'Svara med ett heltal.'},
    '5.619': {'ers': [('(Svara i procent med två decimaler.)', 'Svara i procent med två decimaler.')]},
    # sannolikhet i flera steg
    '5.20': {'ers': [(' Välj ett alternativ.', '')]},
    '5.38': {'ers': [('Vad är sannolikheten att summan blir udda?', f'{HUR} att summan blir udda?')]},
    '5.155': {'ers': [('Anta oberoende.', 'Ljusen är oberoende av varandra.')]},
    '5.163': {'ers': [('Kasten antas oberoende.', 'Kasten är oberoende av varandra.'),
                      ('Sannolikheten för träff på första kastet?', f'{HUR} att spelaren träffar på första kastet?'),
                      ('Sannolikheten att första träffen kommer på tredje kastet?', f'{HUR} att den första träffen kommer på tredje kastet?'),
                      ('Vilka nettovinster är möjliga om träffen kommer inom de fyra första kasten?', 'Hur stor blir nettovinsten om den första träffen kommer på fjärde kastet?'),
                      ('Hur stor är sannolikheten att spelaren går plus?', 'Hur stor är sannolikheten att spelaren går med vinst?')]},
    '5.262': {'ers': [('Först väljs slumpmässigt en av 2 vägar. Därefter lyckas ett försök med sannolikheten 1/3. Vad är sannolikheten att både rätt väg väljs och försöket lyckas?',
                       f'Hugo ska till en stuga och väljer på måfå en av två vägar. Bara den ena vägen leder rätt. Vid stugan tar han på måfå en av tre nycklar, och bara en av dem passar. {HUR} att han både väljer rätt väg och tar rätt nyckel?')]},
    '5.264': {'ers': [('Två oberoende steg ska lyckas. Sannolikheten att det första lyckas är', 'En robot ska utföra två moment som lyckas eller misslyckas oberoende av varandra. Sannolikheten att det första momentet lyckas är'),
                      ('Bestäm sannolikheten att det andra steget lyckas.', f'{HUR} att det andra momentet lyckas?')]},
    '5.265': {'ers': [('En elev räknar', 'Ella räknar')]},
    '5.269': {'ers': [('För två steg gäller att sannolikheten för att det första steget lyckas är', 'Sannolikheten att klara det första provet i en uttagning är'),
                      ('Sannolikheten att båda stegen lyckas är', 'Bara den som klarar det första provet får göra det andra. Sannolikheten att klara båda proven är'),
                      ('Om steg 2 bara utförs när steg 1 lyckats, hur stor är sannolikheten att steg 2 lyckas givet att steg 1 lyckats?',
                       'Hur stor är sannolikheten att den som har klarat det första provet också klarar det andra?')]},
    '5.617': {'ers': [('(Svara i decimalform.)', 'Svara i decimalform.')]},
}
