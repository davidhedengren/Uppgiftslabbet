# Ma4: rester efter mato2_alla/monster/forenklad (2026-11-19).
MARK = ' (Markera alla riktiga alternativ.)'
VALJ = 'Välj alla alternativ som stämmer.'
R = {
    '1.143': {'ers': [('Ange tecken med hjälp av den angivna kvadranten.', 'Använd kvadranten för att avgöra om värdet är positivt eller negativt.')]},
    '1.344': {'ers': [('Svara med tre decimaler där svaret inte är exakt.', 'Avrunda till tre decimaler om svaret inte är exakt.')]},
    '1.543': {'ers': [(' Ange förskjutningen med tecken: höger positivt.', '')], 'kg': 'En förskjutning åt höger skrivs som ett positivt tal.'},
    '1.127': {'ers': [('Lös algebraiskt och svara med två decimaler.', 'Lös algebraiskt och avrunda till två decimaler.')]},
    '1.672': {'ers': [('Ange svaret exakt eller med tre decimaler.', 'Svara exakt eller avrunda till tre decimaler.')]},
    '2.573': {'ers': [('Använd ett digitalt verktyg för att lösa ekvationen.', 'Lös ekvationen.')]},
    '4.623': {'ers': [('b) Bestäm sedan med digitalt verktyg', 'b) Beräkna sedan')]},
    '4.624': {'ers': [('Bestäm med digitalt verktyg', 'Bestäm')]},
    '4.629': {'ers': [(' Använd digitalt verktyg.', '')]},
    '2.141': {'ers': [('vill en elev välja', 'vill Nadia välja')]},
    '2.264': {'ers': [(' Ange a i första fältet och uttrycket g(x) i det andra.', ''), ('Ange a i första fältet och uttrycket g(x) i det andra.', '')], 'd': {'a': {'kg': 'Ange a i första fältet och uttrycket g(x) i det andra.'}}},
    '2.267': {'ers': [(' Ange a i första fältet och uttrycket g(x) i det andra.', ''), ('Ange a i första fältet och uttrycket g(x) i det andra.', '')], 'd': {'a': {'kg': 'Ange a i första fältet och uttrycket g(x) i det andra.'}}},
    '2.78': {'ers': [('Ange båda asymptoternas ekvationer i de två svarsfälten.', 'Ange båda asymptoternas ekvationer.')],
             'd': {e: {'kg': 'Skriv en ekvation i varje svarsfält.'} for e in 'abc'}},
    '2.109': {'ers': [(' Skriv den vågräta asymptotens y-värde i svarsrutan för varje deluppgift.', ''), ('Skriv den vågräta asymptotens y-värde i svarsrutan för varje deluppgift.', '')], 'kg': 'Skriv den vågräta asymptotens y-värde.'},
    '6.17': {'ers': [(' Ange båda rötterna i var sitt fält.', ''), ('Ange båda rötterna i var sitt fält.', '')], 'kg': 'Skriv en rot i varje fält.'},
    '3.523': {'ers': [('Funktionen är \\(y=', 'Funktionen ges av \\(y=')]},
    '3.524': {'ers': [('Funktionen är \\(y=', 'Funktionen ges av \\(y=')]},
    '2.122': {'ers': [('<p>Funktionen är</p>', '<p>Funktionen \\(f\\) ges av</p>')]},
    '2.159': {'ers': [('<p>Funktionen är</p>', '<p>Funktionen \\(f\\) ges av</p>')]},
}
for i in ('2.610', '2.667', '2.675', '2.705'):
    R[i] = {'ers': [(MARK, '')], 'kg': VALJ}
