"""Handgranskning av Ma1, sinus, cosinus och tangens."""

DEC = 'Avrunda till en decimal.'
TVA = 'Avrunda till två decimaler.'

def fraga(text, kg=None):
    post = {'t': '<p>' + text + '</p>'}
    if kg:
        post['kg'] = kg
    return post

def figursida():
    return {'ers': [('Bestäm sidan x i triangeln. Svara med en decimal.', 'Hur lång är sidan x?')], 'kg': DEC}

R = {
    '4.13': {'ers': [('Vinklarna mot marken är 28° och 42°.', 'Vinkeln mot marken är 28° i den stora triangeln och 42° i den lilla.'), (' Avrunda alla svar till en decimal.', '')],
             'd': {'a': {'kg': DEC}, 'b': {'kg': DEC}, 'c': {'kg': DEC}}},
    '4.14': fraga('I en rätvinklig triangel är hypotenusan 10 cm. Hur lång är kateten mitt emot vinkeln 40°?', TVA),
    '4.38': {'ers': [('b) Bestäm hypotenusan.', 'b) Hur lång är hypotenusan om kateterna är 8 och 15?')],
             'd': {'b': {'t': r'<p>I en rätvinklig triangel är kateterna 8 och 15. Hur lång är hypotenusan?</p>'}}},
    '4.42': {'ers': [('En elev skriver', 'Noor skriver'), ('Vilken förklaring beskriver felet bäst?', 'Vad är fel i Noors beräkning?')]},
    '4.43': fraga(r'I en rätvinklig triangel är hypotenusan 25 cm. Kateten mitt emot vinkeln \(v\) är 7 cm. Vad är \(\sin v\)?'),
    '4.44': {'ers': [('Bestäm triangelns två spetsiga vinklar. Avrunda till en decimal.', 'Hur stora är triangelns två spetsiga vinklar?')], 'kg': 'Avrunda båda vinklarna till en decimal.'},
    '4.47': {'ers': [(' Välj ett alternativ.', '')]},
    '4.48': {'ers': [('Bestäm längden på den katet som ligger mitt emot 35°. Avrunda till två decimaler.', 'Hur lång är kateten mitt emot vinkeln 35°?')], 'kg': TVA},
    '4.50': {'ers': [('En 9,0 m lång lina bildar', 'En sträckt lina är 9,0 m lång och bildar'), (' Svara med en decimal.', '')], 'kg': DEC},
    '4.122': {'ers': [('Bestäm för triangeln. Svara exakt i bråkform.', 'Använd triangeln i figuren och ange följande värden som exakta bråk.')]},
    '4.171': fraga(r'I en rätvinklig triangel är kateten mitt emot vinkeln \(v\) 4 m lång. Kateten intill \(v\) är 6 m lång. Vilket trigonometriskt samband kan du använda för att bestämma \(v\) direkt?'),
    '4.174': {'ers': [(' Avrunda till två decimaler.', '')], 'd': {'b': {'kg': TVA}}},
    '4.177': {'ers': [('En ramp går 7,5 m horisontellt och lutar 18°. Hur stor är höjdskillnaden? Avrunda till en decimal.', 'En ramp lutar 18° mot marken. Det horisontella avståndet mellan rampens ändar är 7,5 m. Hur stor är höjdskillnaden?')], 'kg': DEC},
    '4.181': fraga('En ramp stiger 4,08 m på en horisontell sträcka av 8,0 m. Vilken vinkel bildar rampen med marken?', DEC),
    '4.209': fraga('En rätvinklig triangel har hypotenusan 12 cm och en vinkel på 30°. Hur lång är kateten mitt emot den vinkeln?'),
    '4.210': fraga('Hypotenusan i en rätvinklig triangel är 10 cm. Hur lång är kateten mitt emot vinkeln 45°?', DEC),
    '4.211': fraga('I en rätvinklig triangel är hypotenusan 14 cm. Hur lång är kateten intill vinkeln 60°?'),
    '4.212': fraga('En rätvinklig triangel har hypotenusan 18 cm och en vinkel på 35°. Hur lång är kateten intill den vinkeln?', DEC),
    '4.213': fraga('I en rätvinklig triangel är kateten intill vinkeln 40° 9 cm lång. Hur lång är den andra kateten?', DEC),
    '4.214': fraga('I en rätvinklig triangel är en vinkel 25°. Kateten intill vinkeln är 16 cm lång. Hur lång är den motstående kateten?', DEC),
    '4.215': fraga('I en rätvinklig triangel är kateten mitt emot vinkeln 52° 7 cm lång. Hur lång är hypotenusan?', DEC),
    '4.216': fraga('En rätvinklig triangel har en vinkel på 38°. Kateten intill vinkeln är 11 cm lång. Hur lång är hypotenusan?', DEC),
    '4.217': fraga(r'I en rätvinklig triangel är kateten mitt emot vinkeln \(v\) 8 cm lång och kateten intill \(v\) 12 cm lång. Hur stor är vinkeln \(v\)?', DEC),
    '4.218': fraga(r'I en rätvinklig triangel är kateten mitt emot vinkeln \(v\) 15 cm lång. Den andra kateten är 9 cm lång. Hur stor är \(v\)?', DEC),
    '4.219': fraga('En ramp är 12 m lång och höjdskillnaden mellan ändarna är 7 m. Vilken vinkel bildar rampen med marken?', DEC),
    '4.220': fraga('En 14 m lång vajer är spänd från marken till en fästpunkt. Avståndet mellan fästena är 11 m mätt horisontellt. Vilken vinkel bildar vajern med marken?', DEC),
    '4.225': fraga('I en rätvinklig triangel är kateten mitt emot vinkeln 20° 5,0 cm lång. Hur lång är hypotenusan?', DEC),
    '4.226': {'ers': [('Vilket påstående måste vara sant?', 'Vilket av påståendena stämmer alltid?')], 'extra': {'visaAlternativ': True}},
    '4.227': {'ers': [('En elev skriver', 'Alex skriver'), ('Vilket är det bästa sättet att rätta lösningen?', 'Hur ska Alex räkna för att få rätt vinkel?')]},
    '4.228': fraga('En stege lutar mot en vägg. Du vet hur lång stegen är och vilken vinkel den bildar med marken. Vilket trigonometriskt samband kan du använda för att räkna ut hur högt stegen når?'),
    '4.229': fraga('Du står på plan mark framför ett torn. Du vet avståndet längs marken till tornets fot och vinkeln från marken upp till toppen. Vilket trigonometriskt samband ger tornets höjd?'),
    '4.405': fraga('Mira känner hypotenusan och kateten mitt emot en spetsig vinkel i en rätvinklig triangel. Hon vill beräkna vinkeln och väljer tangens eftersom den motstående kateten ingår där. Vilket samband bör hon använda? Motivera ditt svar.'),
    '4.410': fraga('Du känner en spetsig vinkel i en rätvinklig triangel och vet hur lång den motstående kateten är. Vilket trigonometriskt samband ger längden på den andra kateten direkt?'),
    '4.411': fraga('Du vet hur lång hypotenusan är och hur stor en spetsig vinkel är i en rätvinklig triangel. Vilket trigonometriskt samband ger längden på kateten mitt emot vinkeln direkt?'),
    '4.423': figursida(),
    '4.424': figursida(),
    '4.425': figursida(),
    '4.426': figursida(),
    '4.427': figursida(),
}
