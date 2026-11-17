# Ma1 tiopotenser och grundpotensform (omr tiopotenser_prefix), omskrivet för hand 2026-11-17.
# Definitionen av grundpotensform (1 ≤ a < 10) och ”Ange a och n separat.” står inte längre i frågan. Hur svaret
# skrivs in i Kunskapsgymmet står i kgInstruktion. ”En elev skriver …” har fått namn och en tydligare fråga.
AN = 'Skriv talfaktorn a och exponenten n i var sitt fält.'
PREC = 'Svara i grundpotensform med två värdesiffror.'


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


def gp(tal, fore=''):
    return {'t': p((fore + ' ' if fore else '') + f'Skriv {tal} i grundpotensform.'), 'kg': AN}


def ratta(namn, vl, hl):
    return {'t': p(f'{namn} skriver \\({vl}={hl}\\). Likheten stämmer inte. Vad ska det stå i högerledet för att '
                   'talet ska få samma värde?')}


R = {
    '0.232': gp('4 500'),
    '0.233': gp('0,0032'),
    '0.234': gp('78 000 000'),
    '0.235': gp('0,000045'),
    '0.326': {'t': p('Två positiva tal har summan 0,0055. Det ena talet är tio gånger så stort som det andra.',
                     'Skriv det större talet i grundpotensform.'), 'kg': AN},
    '0.329': {'t': p('Vilket av talen är skrivet i grundpotensform?')},
    '0.330': ratta('Lina', '48\\cdot10^4', '4{,}8\\cdot10^3'),
    '0.413': gp('12 300 000'),
    '0.414': gp('0,000000056'),
    '0.593': gp('<strong>62 000</strong>'),
    '0.594': gp('<strong>0,00047</strong>'),
    '0.595': {'t': p('Avståndet mellan två städer är <strong>9 300 000</strong> m. Skriv avståndet i grundpotensform.'), 'kg': AN},
    '0.596': gp('<strong>0,0812</strong>'),
    '0.597': gp('<strong>154 000 000</strong>'),
    '0.598': gp('<strong>0,000006</strong>'),
    '0.599': {'t': p('Det bor <strong>38 500</strong> människor i en stad. Skriv invånarantalet i grundpotensform.'), 'kg': AN},
    '0.600': gp('<strong>0,00205</strong>'),
    '0.601': gp('<strong>720 000 000 000</strong>'),
    '0.602': {'t': p('En partikel har diametern <strong>0,0000000094</strong> m. Skriv diametern i grundpotensform.'), 'kg': AN},
    '0.644': {'t': p('Vilket av talen är <strong>inte</strong> skrivet i grundpotensform?')},
    '0.648': {'t': p('Vilket påstående om talet 0 stämmer?')},
    '0.649': {'t': p('Vilket påstående stämmer om det negativa talet \\(-3{,}4\\cdot10^5\\)?')},
    '0.650': {'t': p('Talen \\(4{,}5\\cdot10^{8}\\) och \\(7{,}2\\cdot10^{8}\\) adderas. Vilket påstående om summan stämmer?')},
    '0.653': ratta('Hassan', '320\\cdot10^5', '3{,}2\\cdot10^5'),
    '0.654': ratta('Tilda', '0{,}45\\cdot10^6', '4{,}5\\cdot10^6'),
    '0.655': ratta('Noah', '76\\cdot10^{-3}', '7{,}6\\cdot10^{-3}'),
    '0.656': ratta('Maja', '0{,}08\\cdot10^4', '8\\cdot10^4'),
    '0.657': ratta('Viktor', '1250\\cdot10^2', '1{,}25\\cdot10^2'),
    '0.658': ratta('Ebba', '0{,}0031\\cdot10^8', '3{,}1\\cdot10^8'),
    '0.659': ratta('Liam', '95\\cdot10^{-7}', '9{,}5\\cdot10^{-7}'),
    '0.660': ratta('Selma', '0{,}7\\cdot10^{-2}', '7\\cdot10^{-2}'),
    '0.661': ratta('Oscar', '640\\cdot10^{-4}', '6{,}4\\cdot10^{-4}'),
    '0.662': ratta('Alice', '0{,}025\\cdot10^9', '2{,}5\\cdot10^9'),
    '0.1073': {'t': p('Jordens massa är ungefär \\(5{,}97\\cdot10^{24}\\) kg. På jorden bor ungefär \\(8\\cdot10^9\\) '
                      'människor, och en människa väger i genomsnitt 70 kg.',
                      'Hur stor andel av jordens massa utgör alla människor tillsammans?'), 'kg': PREC},
    '0.1078': {'t': p('Proxima Centauri är den stjärna som ligger närmast solen. Den är 4,24 ljusår bort, och ett ljusår är '
                      '\\(9{,}46\\cdot10^{15}\\) m. Rymdsonden Voyager 1 färdas med ungefär 17 km/s.',
                      'Hur många år skulle det ta för Voyager 1 att nå Proxima Centauri, om sonden färdades rakt mot '
                      'stjärnan? Ett år är ungefär \\(3{,}16\\cdot10^7\\) s.'), 'kg': PREC},
    '0.1151': {'t': p('Avståndet från solen till jorden är \\(1{,}496\\cdot10^{11}\\text{ m}\\), och ljusets hastighet är '
                      '\\(2{,}998\\cdot10^{8}\\text{ m/s}\\). Hur lång tid tar det för ljuset från solen att nå jorden? '
                      'Svara i minuter och sekunder.'),
               'kg': 'Avrunda till hela sekunder och skriv minuter och sekunder i var sitt fält.'},
    '0.1152': {'t': p('Avståndet från solen till Mars är \\(2{,}28\\cdot10^{11}\\text{ m}\\), och ljusets hastighet är '
                      '\\(3\\cdot10^{8}\\text{ m/s}\\). Hur lång tid tar det för ljuset från solen att nå Mars? '
                      'Svara i minuter och sekunder.'),
               'kg': 'Avrunda till hela sekunder och skriv minuter och sekunder i var sitt fält.'},
    '0.1153': {'t': p('Avståndet från jorden till månen är \\(3{,}84\\cdot10^8\\text{ m}\\). En radiosignal färdas med '
                      'farten \\(3{,}0\\cdot10^8\\text{ m/s}\\). Hur lång tid tar det för signalen att nå månen?')},
}
