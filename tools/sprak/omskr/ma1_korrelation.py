"""Handgranskning av Ma1, korrelation (2026-11-20), och kvarvarande "Välj ett alternativ." i hela Ma1.

"Välj ett alternativ." tas bort (apply.py sätter då visaAlternativ så att alternativen syns på papper).
Påståenden utan fråga (5.190, 5.193) får "Stämmer påståendet?". "En elev" får namn där alternativen inte nämner "eleven".
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '5.78': {'ers': [('Ett bils ålder', 'En bils ålder')]},
    '5.76': {'ers': [('En elev säger:', 'Leo säger:')]},
    '5.79': {'ers': [('En elev läser att', 'Saga läser att')]},
    '5.190': {'ers': [('orsakar sömnproblem.</p>', 'orsakar sömnproblem.</p><p>Stämmer påståendet?</p>')]},
    '5.193': {'ers': [('svårt att tolka som orsak.</p>', 'svårt att tolka som orsak.</p><p>Stämmer påståendet?</p>')]},
    '5.679': {'ers': [('(Svara i procent.)', 'Svara i procent.')]},
}
for u in Bank('ma1').arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    alla = ' '.join(falt)
    ers = []
    for a in ('<p>Välj ett alternativ.</p>', ' Välj ett alternativ.', 'Välj ett alternativ.'):
        if a in alla:
            ers.append((a, ''))
            alla = alla.replace(a, '')
    if ers:
        R.setdefault(u['id'], {'ers': []})['ers'].extend(ers)
# Tomma stycken <p></p> i delkort (rester från tidigare borttagningar)
for i in ('2.111', '6.50', '7.92', '7.115', '7.166'):
    R.setdefault(i, {'ers': []})['ers'].append(('<p></p>', ''))
