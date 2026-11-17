# Fy1 kap 4 genomläsning: kraftvektorer (2026-11-17).
# Texterna lät naturliga. 4.969–4.972 frågar efter komposanternas tecken, så axlarnas riktning måste stå
# på papperet (den flyttades till kgInstruktion i den riktade omgången). Den står nu som en koordinatbeskrivning.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

AXLAR = ' Den positiva x-axeln pekar åt höger och den positiva y-axeln uppåt.'
b = Bank('fy1')
R = {}
for id_ in ('4.969', '4.970', '4.971', '4.972'):
    u = b.obj(id_)
    t = u['t']
    i = t.index('</p>')
    forsta = t[:i]
    if AXLAR.strip() in t:
        continue
    gammal = forsta[forsta.rfind('.') - 40: ] if False else None
    # lägg meningen sist i första stycket
    R[id_] = {'ers': [(forsta + '</p>', forsta + AXLAR + '</p>')]}
