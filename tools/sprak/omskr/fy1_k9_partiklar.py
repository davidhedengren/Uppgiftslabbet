# Fy1 kap 9: standardmodellen och de fyra krafterna, genomläsning 2026-11-17.
# Texterna lät redan naturliga; bara formler, formelsamlingsdata och tankehjälp i frågan är borttagna.


def p(*s):
    return ''.join(f'<p>{x}</p>' for x in s)


R = {
    '9.326': {'t': p('Två protoner påverkar varandra både med en elektrisk kraft och med gravitationskraft. Hur många gånger större är den elektriska kraften än gravitationskraften?')},
    '9.328': {'t': p('Antag att jorden och månen hade lika stora laddningar av samma slag. Hur stor laddning skulle de behöva ha för att den elektriska kraften mellan dem skulle bli lika stor som gravitationskraften?')},
    '9.431': {'t': p('I en väteatom attraherar protonen och elektronen varandra både elektriskt och med gravitationskraft.', 'Hur många gånger större är den elektriska kraften än gravitationskraften?')},
    '9.435': {'ers': [('Anta att varje kula fick', 'Antag att varje kula fick')]},
    '9.448': {'ers': [('Hur många kvarkar finns sammanlagt i atomkärnan?', 'Hur många kvarkar finns det i atomkärnan?')]},
}

# Elektromagnetisk strålning och strålning–materia: lät naturligt, bara upprepningen i 9.13 är borttagen.
R['9.13'] = {'t': p('Gammastrålningen halveras för varje 1,2 cm bly den passerar. Detta kallas halveringstjocklek.',
                    'a) Hur många procent passerar ett 2,4 cm tjockt blyskikt?', 'b) Hur många procent passerar ett 6 cm tjockt blyskikt?',
                    'c) Hur tjockt blyskikt behövs för att bara 1,0 % ska passera?')}
