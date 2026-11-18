# Fy1 2.59: felrapporten 2026-11-11 kräver att eleven får veta precisionen (en decimal). Den står nu i
# kgInstruktion i stället för i texten (fellogg-fy1-2026-11-11 läser både t och kgInstruktion).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

u = Bank('fy1').obj('2.59')
K = 'Svara med en decimal.'
R = {'2.59': {'kg': K, 'd': {(d.get('etikett') or chr(97 + i)): {'kg': K} for i, d in enumerate(u.get('spelDelar') or [])}}}
