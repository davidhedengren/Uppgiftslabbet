"""Ma1 (2026-11-20): mönster som blev kvar efter handläsningen, hittade med en mönstersökning över hela banken.

"Använd GeoGebra"/"Använd digitalt verktyg" tas bort ur frågan (verktygstaggen räcker), "Vad är sannolikheten"
heter "Hur stor är sannolikheten", Anta → Antag, två anonyma elever i 5.98 får namn.
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '2.36': {'ers': [(' Använd GeoGebra.', '')]},
    '3.61': {'ers': [('Använd GeoGebra och förklara varför det finns mer än en lösning.', 'Förklara varför det finns mer än en lösning.')]},
    '3.133': {'ers': [('Använd GeoGebra och kontrollera att svaret är rimligt.', 'Kontrollera att svaret är rimligt.')]},
    '3.139': {'ers': [('Använd GeoGebra och förklara varför det kan finnas två lösningar.', 'Förklara varför det kan finnas två lösningar.')]},
    '6.88': {'ers': [('Använd GeoGebra för att bestämma alla bredder', 'Bestäm alla bredder')]},
    '6.121': {'ers': [('Använd digitalt verktyg och bygg modellen själv.', 'Bygg modellen själv.')]},
    '7.134': {'ers': [('Använd digitalt verktyg och motivera vilket extremfall som styr.', 'Motivera vilket extremfall som styr.')]},
    '6.106': {'ers': [(' Använd digitalt verktyg.', '')]},
    '2.645': {'ers': [(' Bestäm den med GeoGebra.', ' Bestäm den.')]},
    '3.102': {'ers': [(' Lös ekvationen grafiskt eller med GeoGebra.', ' Lös ekvationen grafiskt.')]},
    '5.98': {'ers': [('En elev säger: ”Resultatet från skola B', 'Hugo säger: ”Resultatet från skola B'), ('En annan säger: ”Skola A', 'Wilma säger: ”Skola A')]},
}
for u in Bank('ma1').arr:
    s = ' '.join([u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    e = R.setdefault(u['id'], {'ers': []})['ers']
    if 'Vad är sannolikheten' in s:
        e.append(('Vad är sannolikheten', 'Hur stor är sannolikheten'))
    for m in set(re.findall(r'\bAnta (?=att)', s)):
        e.append(('Anta att', 'Antag att'))
    if not e:
        del R[u['id']]
