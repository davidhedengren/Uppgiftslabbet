"""2026-11-20: Ma2 1.234 b hade alternativ med nyckeln "text" i stället för "txt" (Kunskapsgymmet läser båda,
men felkommentar.py och övriga verktyg använder "txt"). Byter nyckeln, inget annat ändras."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('ma2')
t = b.text('1.234')
n = t.count('{"text":')
assert n == 3, n
b.byte['1.234'] = t.replace('{"text":', '{"txt":')
json.loads(b.byte['1.234'])
print(b.spara(), 'objekt skrivna')
