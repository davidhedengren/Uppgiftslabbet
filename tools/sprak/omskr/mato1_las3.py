# Ma3c handgenomläsning: tangent_sekant, absolutbelopp, faktorisera_polynom, gransvarde (2026-11-19).
SP = 'Svara som en produkt.'
KI = 'Kontrollera lösningarna genom insättning.'
R = {
    '1.818': {'ers': [(' ' + SP, '')], 'kg': SP},
    '1.819': {'ers': [(' ' + SP, '')], 'kg': SP},
    '1.842': {'ers': [(' ' + SP, '')], 'kg': SP},
    # gränsvärden utan parentes kunde läsas som (lim x) + 1
    '1.103': {'ers': [(r'\lim_{x\to 1}x + 1', r'\lim_{x\to 1}(x+1)')]},
    '1.106': {'ers': [(r'\lim_{x\to 2}x + 2', r'\lim_{x\to 2}(x+2)')]},
    '1.109': {'ers': [(r'\lim_{x\to -3}x - 3', r'\lim_{x\to -3}(x-3)')]},
    '1.112': {'ers': [(r'\lim_{x\to 4}x + 4', r'\lim_{x\to 4}(x+4)')]},
    '1.115': {'ers': [(r'\lim_{x\to 0}x + 3', r'\lim_{x\to 0}(x+3)')]},
    '1.264': {'ers': [('Kontrollera att alla avlästa lösningar verkligen fungerar.', KI)]},
    '1.265': {'ers': [('Kontrollera att alla avlästa lösningar verkligen fungerar.', KI)]},
    '1.266': {'ers': [('Kontrollera att alla avlästa lösningar verkligen fungerar.', KI)]},
    '1.176': {'ers': [(r', samt avgör tecknet på \(a\)', r' och avgör om \(a\) är positivt eller negativt')]},
    '1.569': {'ers': [(r'\(h=0,1\)', r'\(h=0{,}1\)')]},
    '1.431': {'ers': [('Bestäm den övre gränsen för antalet fiskar med hjälp av sambandet.', 'Bestäm den övre gränsen för antalet fiskar enligt modellen.')]},
}
