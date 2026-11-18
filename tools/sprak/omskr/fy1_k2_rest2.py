# Fy1 kap 2: 2.138 hade "(Svara med ett heltal.)" i ett eget stycke; 3.51 b behöver riktningen i Kunskapsgymmet.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('fy1')
u = b.obj('2.138')
alla = ' '.join([u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
e = [v for v in ('<p>(Svara med ett heltal.)</p>', ' (Svara med ett heltal.)', '(Svara med ett heltal.)') if v in alla][:1]
R = {'3.51': {'d': {'b': {'kg': 'Öster räknas som positiv riktning.'}}}}
if e:
    R['2.138'] = {'ers': [(e[0], '')]}
