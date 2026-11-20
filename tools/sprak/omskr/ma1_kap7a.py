"""Handgranskning av Ma1 kapitel 7, del 1: proportionalitet i yrken, skala, mätning och enheter, överslag, mätfel (2026-11-20).

Telegramstil ("Per liter?", "En del?", "Ämnesmängd?") blir hela frågor, "ritning/karta" väljs, "En elev" får namn
där alternativen inte nämner eleven, "(utan tecken)" och "längden först" flyttas till kgInstruktion.
"""
R = {
    '7.144': {'ers': [('3 liter färg räcker till 24 m².', 'Tre liter färg räcker till 24 m².'),
                      ('a) Per liter?', 'a) Hur stor yta räcker en liter till?'), ('b) 5 liter?', 'b) Hur stor yta räcker 5 liter till?'),
                      ('c) Hur mycket till 60 m²?', 'c) Hur mycket färg behövs till 60 m²?'),
                      ('>Per liter?<', '>Hur stor yta räcker en liter till?<'), ('>5 liter?<', '>Hur stor yta räcker 5 liter till?<'),
                      ('>Hur mycket till 60 m²?<', '>Hur mycket färg behövs till 60 m²?<')]},
    '7.150': {'ers': [('8 lika delar väger 3,2 kg.', 'Åtta likadana delar väger tillsammans 3,2 kg.'),
                      ('a) En del?', 'a) Vad väger en del?'), ('b) 25 delar?', 'b) Vad väger 25 delar?'),
                      ('>En del?<', '>Vad väger en del?<'), ('>25 delar?<', '>Vad väger 25 delar?<')]},
    '7.152': {'ers': [('>Ämnesmängd?<', '>Hur många milliliter av ämnet finns i lösningen?<'), ('>Övrig vätska?<', '>Hur många milliliter utgör resten?<')]},
    '7.154': {'ers': [('>Hur mycket ämne?<', '>Hur många milliliter av ämnet finns i lösningen?<'), ('>Hur mycket övrig vätska?<', '>Hur många milliliter utgör resten?<')]},
    '7.146': {'ers': [('Hur många på 9 timmar?', 'Hur många enheter producerar den på 9 timmar?')]},
    '7.151': {'ers': [('2,5 kg material kräver 0,75 L tillsats. Hur mycket behövs till 8 kg?', 'Till 2,5 kg material behövs 0,75 liter tillsats. Hur mycket tillsats behövs till 8 kg material?')]},
    '7.160': {'ers': [('Hur mycket koncentrat?', 'Hur mycket koncentrat behövs?')]},
    '7.161': {'ers': [('Bestäm koncentrationen.', 'Bestäm blandningens koncentration.')]},
    '7.66': {'ers': [('Vid samma specifika energianvändning ska 1200 enheter produceras. Elpris 1,35 kr/kWh.',
                      'Maskinen ska nu producera 1 200 enheter med samma energianvändning per enhet. Elpriset är 1,35 kr/kWh.')]},
    '7.202': {'ers': [('En ritning/karta har skalan 1:50000. En sträcka är 3,2 cm på bilden.', 'En karta har skalan 1:50 000. En sträcka är 3,2 cm på kartan.')]},
    '7.206': {'ers': [('En ritning/karta har skalan 1:50. En sträcka är 8 cm på bilden.', 'En ritning har skalan 1:50. En sträcka är 8 cm på ritningen.')]},
    '7.204': {'ers': [('En elev räknar', 'Isak räknar')]},
    '7.180': {'ers': [('En elev avrundar', 'Selma avrundar')]},
    '7.436': {'ers': [('En elev räknar ut', 'Theo räknar ut')]},
    '7.105': {'ers': [('<p>Utan att först multiplicera exakt: vilket eller vilka överslag bör ligga närmast? Kontrollera sedan.</p><p>Välj det alternativ som bör ligga närmast.</p>',
                       '<p>Vilket överslag bör ligga närmast det exakta värdet? Svara utan att först multiplicera exakt.</p>')]},
    '7.445': {'ers': [(' (utan tecken)', '')], 'kg': 'Svara med ett positivt tal.'},
    '7.424': {'ers': [(' Svara med antalet minuter utöver de hela timmarna.', '')], 'kg': 'Svara med antalet minuter utöver de hela timmarna.'},
}
for i in ('7.544', '7.545', '7.546'):
    R[i] = {'ers': [('Svara i centimeter, längden först.', 'Svara i centimeter.')], 'kg': 'Ange längden först.'}
