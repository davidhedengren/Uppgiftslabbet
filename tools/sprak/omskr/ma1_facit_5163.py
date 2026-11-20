"""Ma1 5.163 c (2026-11-20): delkortets svarsrad följer nu frågan (nettovinst vid första träff på fjärde kastet).
Körs direkt: python tools/sprak/omskr/ma1_facit_5163.py [--skriv]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('ma1')
GAMMAL = '<strong>Svar:</strong> Nettovinst: 4, 3, 2 eller 1 poäng.'
NY = r'<strong>Svar:</strong> Fyra kast kostar 4 poäng och träffen ger 5 poäng, så nettovinsten blir \(5-4=1\) poäng.'
d = next(x for x in b.obj('5.163')['spelDelar'] if x['etikett'] == 'c')
if GAMMAL in d['s']:
    b.ersatt('5.163', [(d['s'], d['s'].replace(GAMMAL, NY))])
print(b.dubbletter or 'ok')
if '--skriv' in sys.argv:
    print(b.spara(), 'objekt skrivna')
