# Ma1 kapitel 0, tillägg 2026-11-17: två uppgifter som språktestet hittade efter första omgången.


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '0.1075': {'t': p('Ett rektangulärt golv mäts till 4,3 m gånger 3,7 m. Båda måtten är avrundade till närmaste decimeter.',
                      'Inom vilka gränser ligger golvets verkliga area?'),
               'kg': 'Svara med två decimaler. Skriv den minsta arean först.'},
    '0.1223': {'t': p('I en klass går 18 tjejer och 12 killar. Hur stor del av klassen är killar? Svara med ett bråk.')},
    # 0.990: facit är avrundat till heltal, så avrundningen behövs i rättningen när den inte står i frågan.
    '0.990': {'kg': 'Avrunda till hela gram.'},
    # 0.991 och 0.992: felrapporten 2026-10-11 19:02 (felrapporter-2026-10-11-1902.test.js) låser att avrundningen
    # står i frågan. Den står kvar, omformulerad.
    '0.991': {'t': p('Bil A drar 0,55 liter bensin per mil och bil B drar 6,8 liter per 100 km. Hur många liter mindre bensin '
                     'drar den snålare bilen på en resa som är 250 km? Avrunda till två decimaler.')},
    '0.992': {'t': p('En tom pool med raka väggar fylls med vatten från en pump. Efter 25 minuter är vattnet 18 cm djupt. '
                     'Poolen ska fyllas till djupet 1,35 m. Hur många timmar tar det att fylla poolen? Avrunda till en decimal.')},
}
