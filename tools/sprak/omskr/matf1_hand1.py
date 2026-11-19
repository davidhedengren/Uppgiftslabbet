# Ma5: rester efter matf1_alla/monster/forenklad (2026-11-19).
R = {
    '2.679': {'ers': [('<p>Räkna med klockor.</p>', ''), (' Räkna med klockor.', ''), ('Räkna med klockor.', '')]},
    '1.541': {'ers': [(' Skriv antalet i svarsrutan och förklara sambandet i din lösning.', ' Förklara sambandet.')]},
    '3.266': {'ers': [(' Ange svaret i cm³/s.', '')]},
    '3.309': {'ers': [(' (Räkna uppåt längs väggen som positiv riktning.)', ''), ('(Räkna uppåt längs väggen som positiv riktning.)', '')],
              'kg': 'Uppåt längs väggen räknas som positiv riktning.'},
    '4.467': {'ers': [('En fallmodell med positiv riktning nedåt ges av', 'Ett fall beskrivs, med hastigheten räknad positiv nedåt, av')]},
    '4.508': {'ers': [('Positiv riktning väljs nedåt och', 'Hastigheten räknas positiv nedåt och')]},
    '4.568': {'ers': [('Välj positiv riktning uppåt och använd', 'Hastigheten räknas positiv uppåt. Använd')]},
    '4.24': {'ers': [('Föremålet släpps från vila.', 'Föremålet släpps.')]},
    '4.509': {'ers': [('faller utan luftmotstånd från vila.', 'faller utan luftmotstånd från stillastående.')]},
    '4.566': {'ers': [('släpps från vila.', 'släpps.')]},
    '4.567': {'ers': [('och hoppar från vila.', 'och börjar falla från stillastående.')]},
    '4.41': {'ers': [('En massa på 1,0 kg sitter i en ideal fjäder', 'En vikt med massan 1,0 kg sitter i en fjäder')]},
    '1.777': {'ers': [('Räkna med 366 möjliga födelsedagar.', 'Antag att det finns 366 möjliga födelsedagar.')]},
    '3.287': {'ers': [(' Du får använda ett digitalt verktyg.', ''), ('<p>Du får använda ett digitalt verktyg.</p>', '')]},
    '3.53': {'ers': [('Ett digitalt verktyg ger', 'En räknare ger')]},
    '3.74': {'ers': [('Ett digitalt verktyg ger', 'GeoGebra ger')]},
    '4.25': {'ers': [('Ett digitalt verktyg påstår', 'GeoGebra påstår')]},
    '4.45': {'ers': [('Ett digitalt verktyg ger', 'GeoGebra ger')]},
    '4.87': {'ers': [('Ett digitalt verktyg ger', 'GeoGebra ger')]},
    '4.32': {'ers': [('förklarar en elev att', 'förklarar Signe att')]},
}
R['3.309']['ers'].append(('<p></p>', ''))
# "Fördjupning utanför ordinarie Ma5-träning." är metatext (stilguiden); nivån framgår av träningsnivån.
F = 'Fördjupning utanför ordinarie Ma5-träning.'
for _i in ('4.386', '4.30', '4.32', '4.34', '4.106', '4.153', '4.490'):
    R.setdefault(_i, {'ers': []})['ers'] += [('<p>' + F + '</p>', ''), (' ' + F, ''), (F + ' ', ''), (F, ''), ('<p></p>', '')]
for _i in ('4.386', '4.30', '4.32', '4.34', '4.106', '4.153', '4.490'):
    R[_i]['ers'].append(('<p><strong></strong></p>', ''))
