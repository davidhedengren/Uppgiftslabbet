"""Ma1, bestämma vinklar."""

DEC = 'Avrunda till en decimal.'

def uppgift(text, kg=None):
    post = {'t': '<p>' + text + '</p>'}
    if kg:
        post['kg'] = kg
    return post

def figurvinkel():
    return {'ers': [('Bestäm vinkeln v i triangeln. Svara i grader med en decimal.', r'Hur många grader är vinkeln \(v\) i triangeln?')], 'kg': DEC}

def korta_fraga(gammal, ny):
    return {'ers': [(gammal, ny)], 'kg': DEC}

R = {
    '4.03': korta_fraga(r'Bestäm vinkeln \(v\) mellan rampen och marken. Svara i grader med en decimal.', r'Hur många grader är vinkeln \(v\) mellan rampen och marken?'),
    '4.16': uppgift(r'För en spetsig vinkel \(v\) gäller att \(\cos v=0{,}642\). Hur många grader är \(v\)?', DEC),
    '4.37': {'ers': [('En garderob som är 230 cm hög står lodrätt på golvet.', 'En 230 cm hög garderob står vinkelrätt mot golvet.'), ('<p>Svara i grader med en decimal.</p>', '')], 'kg': 'Avrunda båda vinklarna till en decimal.'},
    '4.51': uppgift(r'Hypotenusan i en rätvinklig triangel är 10 längdenheter. Kateten mitt emot vinkeln \(v\) är 6 längdenheter. Hur stor är \(v\) i grader?', DEC),
    '4.53': uppgift(r'Vilken spetsig vinkel har cosinusvärdet 0,615?', DEC),
    '4.55': uppgift('En 7,5 m lång vajer är spänd mellan två fästen. Det ena fästet sitter 4,2 m högre än det andra. Vilken vinkel bildar vajern med horisontalplanet?'),
    '4.56': uppgift('En väg stiger 6 m på en horisontell sträcka av 100 m. Lutningen är alltså 6 %. Hur många grader lutar vägen?', DEC),
    '4.58': {'ers': [('I Sverige byggs vägar vanligtvis med högst 5 % lutning. Hur många graders lutning motsvarar det?', 'En väg lutar 5 %. Hur många grader motsvarar det?'), (' Svara med en decimal.', '')], 'd': {'a': {'kg': DEC}, 'c': {'kg': DEC}}},
    '4.60': {'ers': [(' Ordningen spelar ingen roll.', '')]},
    '4.116': {'ers': [(' Markera alla alternativ som stämmer.', '')]},
    '4.117': uppgift('I en rätvinklig triangel är kateterna 7 cm och 11 cm långa. Hur stor är vinkeln mellan hypotenusan och kateten som är 11 cm?'),
    '4.172': {'ers': [(r'Bestäm den spetsiga vinkeln \(v\) i grader. Svara med en decimal.', r'Hur många grader är den spetsiga vinkeln \(v\)?')], 'd': {'a': {'kg': DEC}, 'b': {'kg': DEC}, 'c': {'kg': DEC}}},
    '4.178': uppgift(r'Hypotenusan i en rätvinklig triangel är 10 längdenheter. Kateten intill vinkeln \(v\) är 8 längdenheter. Hur stor är \(v\) i grader?', DEC),
    '4.428': uppgift(r'Vilken spetsig vinkel \(v\) har \(\sin v=0{,}5\)?'),
    '4.430': uppgift(r'För en spetsig vinkel \(v\) gäller \(\tan v=1\). Hur många grader är \(v\)?'),
    '4.431': uppgift(r'Vilken spetsig vinkel \(v\) har \(\sin v=0{,}8\)?', DEC),
    '4.432': uppgift(r'För en spetsig vinkel \(v\) gäller \(\cos v=0{,}25\). Hur stor är \(v\) i grader?', DEC),
    '4.433': uppgift(r'Hur många grader är den spetsiga vinkeln \(v\) om \(\tan v=2{,}5\)?', DEC),
    '4.434': uppgift(r'För en spetsig vinkel \(v\) gäller \(\sin v=0{,}35\). Hur många grader är \(v\)?', DEC),
    '4.435': uppgift(r'Vilken spetsig vinkel har tangensvärdet 0,6?', DEC),
    '4.436': figurvinkel(),
    '4.437': figurvinkel(),
    '4.438': figurvinkel(),
    '4.439': figurvinkel(),
    '4.440': figurvinkel(),
    '4.441': figurvinkel(),
    '4.442': figurvinkel(),
    '4.571': korta_fraga(r'Bestäm vinkeln mellan rymddiagonalen och bottenytan. Svara i grader med en decimal.', 'Hur stor är vinkeln mellan rymddiagonalen och bottenytan?'),
    '4.579': {'ers': [('står lutad mot en lodrät vägg', 'lutar mot en vertikal vägg'), ('och stegens topp är fortfarande mot väggen', 'medan stegens topp ligger an mot väggen'), (' Svara i grader med en decimal.', '')], 'kg': DEC},
    '4.800': uppgift('En rät linje har lutningen 0,4. Hur stor spetsig vinkel bildar linjen med x-axeln?', DEC),
    '4.801': uppgift(r'I en rätvinklig triangel är kateten intill vinkeln \(v\) 90 % så lång som hypotenusan. Hur stor är \(v\)?', DEC),
    '4.802': uppgift('Vilken spetsig vinkel har sinusvärdet 0,25?', DEC),
    '4.803': korta_fraga('Hur stor vinkel bildar stegen med marken? (Svara i grader med en decimal.)', 'Vilken vinkel bildar stegen med marken?'),
    '4.804': {'ers': [('En drake flyger i ett 50 m långt snöre. Draken är 32 m över marken där snöret hålls.', 'Snöret till en drake är sträckt och 50 m långt. Draken är 32 m högre upp än den ände av snöret som du håller i.'), (' (Svara i grader med en decimal.)', '')], 'kg': DEC},
    '4.805': uppgift('En ramp får luta högst 1 : 12. Den får alltså stiga högst 1 m på en horisontell sträcka av 12 m. Vilken är den största tillåtna lutningsvinkeln för rampen?', DEC),
    '4.806': korta_fraga(r'Hur högt står solen, alltså hur stor är vinkeln \(v\)? (Svara i grader med en decimal.)', r'Vilken vinkel \(v\) bildar solstrålarna med marken?'),
    '4.807': korta_fraga(r'Hur stor är takets lutningsvinkel \(v\)? (Svara i grader med en decimal.)', r'Hur stor är takets lutningsvinkel \(v\)?'),
    '4.809': uppgift('Höjdskillnaden i en backe är 120 m. Det horisontella avståndet mellan backens början och slut är 0,8 km. Vilken lutningsvinkel har backen?', DEC),
}
