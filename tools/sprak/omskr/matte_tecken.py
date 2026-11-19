# Matte, 2026-11-19: "Bestäm tecknet på …" / "avgör tecknet på …" och "Svara med + eller −" / "Svara med 1, 2, 3 eller 4".
# Frågan skrivs som "Avgör om … är positiv eller negativ", svarsformen läggs i kgInstruktion (utan ordet "tecken").
# Körs per bank: SPRAKBANK=mato2 python tools/sprak/apply.py mato2 tools/sprak/omskr/matte_tecken.py
import os
BANK = os.environ.get('SPRAKBANK', 'mato2')
PM = 'Svara med + eller −.'
ALLA = {
    'mato2': {
        '1.138': {'ers': [('Bestäm tecknet på följande uttryck. Svara med <strong>+</strong> eller <strong>−</strong>.', 'Avgör om uttrycken är positiva eller negativa.')],
                  'kg': PM, 'd': {e: {'kg': PM} for e in 'abcd'}},
        '1.308': {'ers': [('Bestäm tecknet på uttrycket utan räknare. Svara med <strong>+</strong> eller <strong>−</strong>.', 'Avgör utan räknare om uttrycken är positiva eller negativa.')],
                  'kg': PM, 'd': {e: {'kg': PM} for e in 'abcd'}},
        '1.563': {'ers': [(' Svara med 1, 2, 3 eller 4.', '')], 'kg': 'Svara med 1, 2, 3 eller 4.'},
        '4.474': {'ers': [(' Svara med 1, 2, 3 eller 4.', '')], 'kg': 'Svara med 1, 2, 3 eller 4.'},
    },
    'mato1': {
        '1.189': {'ers': [(r'avgör tecknet på \(f(3)\) utan att först beräkna hela värdet.', r'avgör om \(f(3)\) är positivt eller negativt utan att först beräkna värdet.')]},
        '3.198': {'ers': [(r'Beskriv tecknet på \(f=F^{\prime}\) och karaktären hos \(F\) vid \(x=-1,2\).',
                           r'Avgör var \(f=F^{\prime}\) är positiv respektive negativ och vilken typ av punkt \(F\) har vid \(x=-1\) och vid \(x=2\).')]},
    },
    'matf1': {
        '4.90': {'ers': [(r"avgör tecknet på \(y'\) när", r"avgör om \(y'\) är positiv eller negativ när")]},
    },
}
R = ALLA.get(BANK, {})
