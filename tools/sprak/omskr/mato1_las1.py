# Ma3c genomläsning (2026-11-19): infinitiv efter borttaget "Använd ett digitalt verktyg för att …" blir imperativ.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank
BYT = [('<p>Bestämma ', '<p>Bestäm '), ('. Bestämma ', '. Bestäm '), ('<p>Lösa ', '<p>Lös '), ('<p>Undersöka ', '<p>Undersök ')]
R = {}
for u in Bank('mato1').arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    e = [(a, c) for a, c in BYT if any(a in x for x in falt)]
    if e:
        R[u['id']] = {'ers': e}
