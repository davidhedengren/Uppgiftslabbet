# Ma2 genomläsning, del 2 (2026-11-19): namnkrock och kvarglömd svarsfältsmening.
KOORD = ' Skriv x-koordinaten i första svarsfältet och y-koordinaten i det andra.'
R = {
    '3.407': {'ers': [('vilket fel Melvin gör', 'vilket fel Felix gör'), (' Melvin ', ' Felix ')]},
    '3.92': {'ers': [('Vilket alternativ använder begreppen korrekt?', 'Vilken mening använder begreppen korrekt?')]},
}
for i in ('3.134', '3.184', '3.201', '3.341', '3.343'):
    R[i] = {'ers': [(KOORD, '')], 'kg': 'Skriv x-koordinaten i första svarsfältet och y-koordinaten i det andra.'}
