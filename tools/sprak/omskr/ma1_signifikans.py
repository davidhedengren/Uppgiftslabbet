"""Handgranskning av Ma1, signifikans och felkällor (2026-11-20).

Påståenden utan fråga får "Stämmer påståendet?" respektive en fråga som passar alternativen,
förklaringar i parentes blir vanliga meningar före frågan, svarsformer till kgInstruktion.
"""
STAMMER = 'Stämmer påståendet?'
PROP = 'Felmarginalen är ungefär proportionell mot 1 delat med roten ur stickprovets storlek.'
R = {
    '5.30': {'ers': [('"Tycker du inte också att kommunen bör satsa mer pengar på parker?"', '”Tycker du inte också att kommunen bör satsa mer pengar på parker?”')]},
    '5.182': {'ers': [('frågar bara personer som sitter på bussen.</p>', 'frågar bara personer som sitter på bussen.</p><p>Vilken typ av fel riskerar undersökningen?</p>')]},
    '5.553': {'ers': [(f'Felmarginalen halveras ungefär om stickprovet görs ett visst antal gånger större. Hur många gånger större? ({PROP})',
                       f'{PROP} Hur många gånger större måste stickprovet bli för att felmarginalen ska halveras?')]},
    '5.554': {'ers': [(f' ({PROP})', ''), ('±3 procentenheter. Ungefär hur stor', f'±3 procentenheter. {PROP} Ungefär hur stor')]},
    '5.673': {'ers': [(r' (Felmarginalen är ungefär proportionell mot \(1/\sqrt{n}\).)', ''),
                      ('Man vill få ner felmarginalen', r'Felmarginalen är ungefär proportionell mot \(1/\sqrt{n}\), där \(n\) är antalet personer. Man vill få ner felmarginalen')]},
    '5.674': {'ers': [(' (Svara i gram.)', '')]},
    '5.555': {'ers': [(' Svara ja eller nej.', '')], 'kg': 'Svara ja eller nej.'},
}
for i in ('5.207', '5.208', '5.211', '5.214', '5.210'):
    R[i] = {'ers': [('</p>', f'</p><p>{STAMMER}</p>')]}
