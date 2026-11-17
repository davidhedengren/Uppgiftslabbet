# Ma1 kapitel 0: decimaltal_positionssystem, avrundning, overslag_grunder och andelar, omskrivet för hand 2026-11-17.
# Filen innehåller fyra små områden, uppdelade i var sin ordlista nedan. De förs in och testas tillsammans. "Välj ett alternativ." och "Svara i …" är borttagna. Avrundningskrav som
# rättningen behöver (facit är avrundat) står i kgInstruktion. "En elev" har fått namn, och "Anta" heter "Antag".


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def avr(n):
    return f'Avrunda till {n}.'


DECIMALTAL = {
    '0.55': {'t': p('Vilken beskrivning av siffran 7 i talet 0,073 stämmer?')},
    '0.401': {'t': p('Vilket tal är störst?')},
    '0.402': {'t': p('Vilket tal är minst?')},
    '0.403': {'t': p('Vilket av talen ligger mellan 2,49 och 2,50?')},
    '0.404': {'t': p('Vilket påstående stämmer?')},
}

AVRUNDNING = {
    '0.191': {'t': p('En längd är 0,4449 m. Den avrundas till 0,445 m. Hur många meter större är det avrundade värdet?')},
    '0.727': {'t': p('Vilket tal avrundas <strong>inte</strong> till 3,2 när du avrundar till närmaste tiondel?')},
    '0.728': {'t': p('Vilket tal avrundas <strong>inte</strong> till 50 när du avrundar till närmaste tiotal?')},
    '0.906': {'t': p('Vilket av talen avrundas till 6,0 när du avrundar till en decimal?')},
    '0.912': {'t': p('En rektangel har måtten 4,6 cm och 2,8 cm, avrundat till närmaste millimeter. Hur stor kan arean som mest '
                     'vara?'), 'kg': 'Svara med två decimaler.'},
    '0.997': {'t': p('Dosen av ett läkemedel är 0,125 mg per kilogram kroppsvikt. Hur många milligram ska en patient som väger '
                     '68 kg få?')},
}

OVERSLAG = {
    '0.197': {'t': p('En klass köper 79 biljetter för 51 kr styck. Uppskatta vad biljetterna kostar totalt genom att avrunda '
                     'både antalet och priset till närmaste tiotal.')},
    '0.204': {'t': p('Leo får 965,3 när han räknar ut 19,7 · 4,9. Vad säger ett överslag om hans svar?')},
    '0.208': {'t': p('Tim gör överslaget 250 · 40 = 10 000 för att uppskatta 247 · 39. Är överslaget för stort eller för litet? '
                     'Hur mycket skiljer det, utan att du först räknar ut 247 · 39? Visa hur du tänker.')},
    '0.210': {'t': p('En förening har 59 800 kr. Den får in 20 300 kr och betalar 9 900 kr. Gör ett överslag av hur mycket '
                     'pengar föreningen har nu genom att avrunda varje belopp till närmaste tusental.')},
    '0.211': {'t': p('Två belopp är 3 980 kr och 3 975 kr. Ella avrundar båda till 4 000 kr och får skillnaden 0 kr. Beräkna den '
                     'exakta skillnaden. Förklara varför små fel i beloppen kan ge ett stort fel i skillnaden.')},
    '0.740': {'t': p('Ida har räknat ut 38,5 · 4,1 och fått svaret 1 578,5. Vilket påstående stämmer?')},
    '0.744': {'t': p('Omar räknar ut 0,52 · 810 och får 42,12. Vilket påstående stämmer?')},
    '0.919': {'t': p('Wilma beräknar \\(0{,}48\\cdot5\\,200\\) och får svaret 24 960. Vilket påstående stämmer?')},
    '0.1008': {'t': p('Jesper räknar ut \\(0{,}25\\cdot824\\) och får 2 060. Vilket påstående stämmer?')},
    '0.1056': {'t': p('Ungefär hur många tandborstar köps i Sverige varje år? Antag att Sverige har 10 miljoner invånare och '
                      'att alla byter tandborste var tredje månad.')},
    '0.1060': {'t': p('Kim uppskattar \\(396\\cdot0{,}248\\) med överslaget \\(400\\cdot0{,}25=100\\). Hur många procent för '
                      'stort är överslaget jämfört med det exakta värdet?'), 'kg': avr('en decimal')},
    '0.1074': {'t': p('Ett människohjärta slår i genomsnitt 70 gånger per minut. Gör ett överslag av hur många gånger det slår '
                      'under ett liv som är 80 år långt.'), 'kg': 'Svara i grundpotensform med en värdesiffra.'},
}

ANDELAR = {
    '0.758': {'t': p('12 av 30 elever cyklar till skolan. Hur många procent av eleverna cyklar?')},
    '0.759': {'t': p('I en låda finns 8 röda och 12 blå kulor. Hur stor andel av kulorna är röda? Svara med ett bråk i '
                     'enklaste form.')},
    '0.782': {'t': p('Vilken andel är störst?')},
    '0.810': {'t': p('En detalj ska vara 72,0 mm lång med toleransen ±0,3 mm. Hur många procent av längden är toleransen?'),
              'kg': avr('två decimaler')},
    '0.811': {'t': p('Vid en kvalitetskontroll kasseras 14 av 320 tillverkade delar. Hur många procent av delarna kasseras?'),
              'kg': avr('en decimal')},
    '0.812': {'t': p('En restaurangägare är på plats hela tiden som restaurangen är öppen: måndag–fredag 11–22, lördag 11–23 och '
                     'söndag 11–18. Hur många procent av en arbetsvecka på 40 timmar arbetar han?')},
    '0.813': {'t': p('På en verkstadsfaktura är arbetskostnaden 3 450 kr och reservdelarna kostar 6 150 kr, båda före moms. Hur '
                     'många procent av beloppet före moms är arbetskostnad?'), 'kg': avr('en decimal')},
    '0.815': {'t': p('Du har 12 liter bensin och ska tillsätta olja så att oljan blir exakt 3 % av den färdiga blandningen. Hur '
                     'många deciliter olja ska du tillsätta?'), 'kg': avr('två decimaler')},
    '0.956': {'t': p('I en påse finns 25 godisbitar, och 5 av dem är lakrits. Hur många procent av godisbitarna är lakrits?')},
    '0.965': {'t': p('En skola har 540 elever, och 45 % av dem är pojkar. Av pojkarna går \\(\\frac13\\) på teknikprogrammet och '
                     'av flickorna \\(\\frac19\\). Hur många procent av skolans elever går på teknikprogrammet?'),
              'kg': avr('en decimal')},
    '0.967': {'t': p('På ett företag är 60 % av de anställda kvinnor. 25 % av kvinnorna och 40 % av männen arbetar deltid. Hur '
                     'många procent av dem som arbetar deltid är kvinnor?'), 'kg': avr('heltal')},
    '0.1014': {'t': p('Av 200 lotter är 50 vinstlotter. Hur många procent av lotterna är vinstlotter?')},
    '0.1023': {'t': p('Ett test för en viss sjukdom är positivt för 90 % av dem som har sjukdomen. Testet blir också positivt för '
                      '5 % av dem som är friska. 2 % av befolkningen har sjukdomen. Hur många procent av dem som får ett '
                      'positivt test är sjuka?'), 'kg': avr('heltal')},
}

OMRADEN = {'decimaltal_positionssystem': DECIMALTAL, 'avrundning': AVRUNDNING, 'overslag_grunder': OVERSLAG,
           'andelar': ANDELAR}
R = {k: v for d in OMRADEN.values() for k, v in d.items()}
