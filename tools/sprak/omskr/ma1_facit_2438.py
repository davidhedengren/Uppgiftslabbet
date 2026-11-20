"""Ma1 2.438 (2026-11-20): facit visade \\"Tom\\" med omvända snedstreck; nu ”Tom”.
Körs direkt: python tools/sprak/omskr/ma1_facit_2438.py [--skriv]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('ma1')
s = b.obj('2.438')['s']
GAMMAL = '\\"Tom\\"'
if GAMMAL in s:
    b.ersatt('2.438', [(s, s.replace(GAMMAL, '”Tom”'))])
print(b.dubbletter or 'ok')
if '--skriv' in sys.argv:
    print(b.spara(), 'objekt skrivna')
