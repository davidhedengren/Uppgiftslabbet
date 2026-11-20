"""Handgranskning av Ma1, beroende händelser (2026-11-20).

Frågorna skrivs som "Hur stor är sannolikheten …?", svarsform i parentes blir en vanlig mening,
"En elev" får namn och upprepningar i delkorten tas bort.
"""
BRAK_P = '(Svara i bråkform.)'
BRAK = 'Svara i bråkform.'
HUR = 'Hur stor är sannolikheten'

R = {
    '5.03': {'ers': [('Bestäm sannolikheten att de får olika färg.', 'Hur stor är sannolikheten att kulorna har olika färg?')]},
    '5.16': {'ers': [('Bestäm sannolikheten att första är röd och andra blå.', 'Hur stor är sannolikheten att den första kulan är röd och den andra blå?')]},
    '5.56': {'ers': [('a) Bestäm sannolikheten för olika färg <strong>utan</strong> återläggning.', 'a) Hur stor är sannolikheten att kulorna har olika färg om dragningen sker <strong>utan</strong> återläggning?'),
                     ('b) Bestäm samma sannolikhet <strong>med</strong> återläggning.', 'b) Hur stor är samma sannolikhet <strong>med</strong> återläggning?'),
                     ('Bestäm sannolikheten för olika färg <strong>utan</strong> återläggning.', 'Hur stor är sannolikheten att kulorna har olika färg om dragningen sker <strong>utan</strong> återläggning?'),
                     ('Bestäm sannolikheten att få en röd och en blå kula <strong>med</strong> återläggning.</p><p><em>Här avses fortfarande sannolikheten att få en röd och en blå kula, men nu med återläggning.</em></p>',
                      'Hur stor är sannolikheten att kulorna har olika färg om dragningen sker <strong>med</strong> återläggning?</p>'),
                     (r'<p><em>Du kan använda sannolikheterna \(5/9\) utan återläggning och \(40/81\) med återläggning.</em></p>',
                      r'<p>Utan återläggning är sannolikheten \(5/9\) och med återläggning \(40/81\).</p>')]},
    '5.123': {'ers': [('4 röda och 2 blåa.', '4 röda och 2 blå.')]},
    '5.167': {'ers': [('4 röda och 2 blåa.', '4 röda och 2 blå.')]},
    '5.149': {'ers': [('En elev räknar sannolikheten', 'Ebba räknar sannolikheten')]},
    '5.606': {'ers': [('En elev har ritat trädet nedan, men en sannolikhet är fel.', 'Hugo har ritat trädet nedan, men en sannolikhet är fel.')]},
    '5.612': {'ers': [(r'En elev räknar \(\frac37\cdot\frac26=\frac17\).', r'Maja räknar \(\frac37\cdot\frac26=\frac17\).')]},
    '5.246': {'ers': [('2 kulor dras utan återläggning. Vad är sannolikheten att alla 2 är röda?', f'Två kulor dras utan återläggning. {HUR} att båda är röda?')]},
    '5.248': {'ers': [('Vad är sannolikheten att även den andra är röd?', f'{HUR} att även den andra är röd?')]},
    '5.249': {'ers': [('Innan något drag har gjorts: vad är sannolikheten att <strong>den andra</strong> kulan blir röd?', f'{HUR} att <strong>den andra</strong> kulan är röd?')]},
    '5.253': {'ers': [('Vad är sannolikheten att den <strong>första</strong> kulan var den röda?', f'{HUR} att den <strong>första</strong> kulan var den röda?')]},
    '8.09': {'ers': [(' (Svara som bråk eller decimaltal.)', '')], 'kg': 'Svara med ett bråk eller ett decimaltal.'},
    '5.607': {'ers': [(' (Svara med ett heltal.)', '')]},
    '5.613': {'ers': [('(Svara i procentenheter med en decimal.)', 'Avrunda till en decimal.')]},
    '5.614': {'ers': [('(Svara i procent med en decimal.)', 'Svara i procent med en decimal.')]},
}
for i in ('5.600', '5.601', '5.602', '5.603', '5.604', '5.605', '5.608', '5.609', '5.610', '5.611', '5.615'):
    R[i] = {'ers': [(BRAK_P, BRAK)]}
