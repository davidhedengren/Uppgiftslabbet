# Ma3c: rester efter mato1_alla.py och mato1_monster.py (2026-11-19).
# "med tecken" skrivs aldrig; att en minskning är negativ står i kgInstruktion.
MIN = 'En minskning skrivs som ett negativt tal.'
R = {
    '2.780': {'ers': [(' Ange förändringshastigheten med tecken, avrundad till närmaste hundratal kr/år.', ' Avrunda till närmaste hundratal kr/år.')],
              'd': {'b': {'kg': MIN}}},
    '2.786': {'ers': [(' Ange ett värde med tecken i hela kr/år.', ' Svara i hela kr/år.')], 'kg': MIN, 'd': {'b': {'kg': MIN}}},
    '2.788': {'ers': [(' Ange ett värde med tecken och två decimaler i mg/h.', ' Avrunda till två decimaler.')],
              'kg': MIN + ' Svara i mg/h.', 'd': {'c': {'kg': MIN + ' Svara i mg/h.'}}},
    '2.790': {'ers': [(' Ange ett värde med tecken, avrundat till heltal.', ' Avrunda till heltal.'),
                      (' Ange ett värde med tecken i hela kWh/år.', ' Svara i hela kWh/år.')],
              'd': {'b': {'kg': MIN}, 'c': {'kg': MIN}}},
    '2.792': {'ers': [(' Ange ett värde med tecken och två decimaler i ärenden/vecka².', ' Avrunda till två decimaler.')],
              'kg': MIN + ' Svara i ärenden/vecka².', 'd': {'a': {'kg': MIN + ' Svara i ärenden/vecka².'}}},
    '3.503': {'ers': [(' Svara med tre decimaler:', ' Beräkna och avrunda till tre decimaler:')]},
    '3.590': {'ers': [('Använd digitalt verktyg och svara med två decimaler.', 'Avrunda till två decimaler.')]},
    '3.592': {'ers': [('Använd digitalt verktyg och svara med två decimaler.', 'Avrunda till två decimaler.')]},
    '1.195': {'ers': [('och motivera att funktionen är entydigt bestämd.', 'och motivera att det bara finns en sådan funktion.')]},
}
