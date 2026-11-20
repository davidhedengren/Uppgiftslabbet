"""Handgranskning av Ma1, risk och säkerhet samt urvalsmetoder (2026-11-20).

Abstrakta "två oberoende risker" och "exponeringar" får vardagliga sammanhang (talen och svaren är oförändrade),
svarsform i parentes blir en vanlig mening eller kgInstruktion, "Välj ett alternativ." tas bort, Anta → Antag.
"""
HUR = 'Hur stor är sannolikheten'
JN = 'Svara ja eller nej och motivera kort.'
R = {
    '5.67': {'ers': [('Vad är sannolikheten att båda misslyckas samtidigt?', f'{HUR} att båda misslyckas samtidigt?')]},
    '5.226': {'ers': [('Vid 800 likadana och oberoende försök förväntas i genomsnitt 12 händelser. Uppskatta risken per försök i procent.',
                       'En fabrik provar 800 likadana lampor. I genomsnitt går 12 av lamporna sönder under provet. Uppskatta risken i procent att en lampa går sönder.')]},
    '5.229': {'ers': [('En viss skada inträffar med risk 8 % vid var och en av 600 likadana exponeringar. Varje skada kostar i genomsnitt 250 kr. Vilken total kostnad förväntas?',
                       'En cykeluthyrning hyr ut cyklar 600 gånger under en säsong. Vid varje uthyrning är risken 8 % att cykeln skadas. En skada kostar i genomsnitt 250 kr att laga. Vilken total kostnad för skador kan uthyrningen räkna med?')]},
    '5.230': {'ers': [('Två oberoende risker är 10 % respektive 20 %. Beräkna sannolikheten att minst en av händelserna inträffar.',
                       f'Risken att tåget är försenat är 10 % och risken att bussen är försenad är 20 %. Förseningarna är oberoende av varandra. {HUR} att minst ett av fordonen är försenat?')]},
    '5.231': {'ers': [('Två oberoende risker är 5 % respektive 10 %. Beräkna sannolikheten att <strong>ingen</strong> av händelserna inträffar.',
                       f'Risken för regn är 5 % på lördag och 10 % på söndag. Vädret de två dagarna är oberoende av varandra. {HUR} att det <strong>inte</strong> regnar någon av dagarna?')]},
    '5.232': {'ers': [('Två oberoende risker är 2 % respektive 3 %.', 'Ett fel upptäcks av två larm som fungerar oberoende av varandra. Det första larmet missar felet med sannolikheten 2 % och det andra med sannolikheten 3 %.'),
                      ('Bestäm sannolikheten att båda händelserna inträffar.', f'{HUR} att båda larmen missar felet?'),
                      ('Bestäm sannolikheten att minst en av dem inträffar.', f'{HUR} att minst ett av larmen missar felet?')]},
    '5.233': {'ers': [('Två oberoende risker är 15 % och 25 %. En elev säger att risken för minst en händelse är',
                       'Två händelser är oberoende av varandra och har risken 15 % respektive 25 %. Wilma säger att risken att minst en av dem inträffar är')]},
    '5.490': {'ers': [('Anta att risken', 'Antag att risken')]},
    '5.632': {'ers': [('(Svara i decimalform.)', 'Svara i decimalform.')]},
    '5.633': {'ers': [(' (Svara i kr.)', '')]},
    '5.635': {'ers': [('(Svara i procent.)', 'Svara i procent.')]},
    '5.639': {'ers': [('(Svara i procent.)', 'Svara i procent.')]},
    '5.640': {'ers': [(' (Svara i kr, med minustecken vid förlust.)', '')], 'kg': 'En förlust skrivs som ett negativt tal.'},
    # urvalsmetoder
    '5.102': {'ers': [('Svara ja eller nej för varje fall och motivera kort.', 'Motivera kort för varje fall.'),
                      (' Svara ja eller nej och motivera kort.', ' Motivera kort.')],
              'kg': 'Svara ja eller nej för varje fall.', 'd': {e: {'kg': 'Svara ja eller nej.'} for e in 'abc'}},
    '5.106': {'ers': [(' Välj ett alternativ.', '')]},
    '5.108': {'ers': [(' Välj ett alternativ.', '')]},
    '5.567': {'ers': [(' Välj ett alternativ.', '')]},
    '5.666': {'ers': [('(Svara i procent.)', 'Svara i procent.')]},
    '5.670': {'ers': [('Anta att andelen', 'Antag att andelen'), ('(Svara i procent.)', 'Svara i procent.')]},
}
