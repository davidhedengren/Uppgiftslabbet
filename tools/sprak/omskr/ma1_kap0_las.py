"""Handläsning av Ma1 kapitel 0 (2026-11-20), efter första omgången 2026-11-17.

Drillserierna 0.1266–0.1289 hade "Beräkna … Svara exakt." i varje deluppgift; på papper står nu
"Beräkna. Svara exakt." en gång och deluppgifterna är bara uttryck (delkorten i Kunskapsgymmet är oförändrade).
"Hon" om en okänd person (cyklist, löpare, spelare) blir substantivet.
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '0.131': {'ers': [('Vilket tecken ska stå i rutan', 'Vilket räknetecken ska stå i rutan')]},
    '0.408': {'ers': [('Hon stiger 2,5 m. Vilken nivå befinner hon sig på?', 'Dykaren stiger 2,5 m. Vilken nivå befinner sig dykaren på då?')]},
    '0.124': {'ers': [('<p>Betrakta talen:</p>', '<p>Här är tre tal:</p>')]},
    '0.1235': {'ers': [('Hur långt cyklar hon på 35 minuter?', 'Hur långt cyklar cyklisten på 35 minuter?')]},
    '0.947': {'ers': [('har hon sprungit', 'har löparen sprungit')]},
    '0.1059': {'ers': [('har en person levt när hon fyller 16 år?', 'har man levt när man fyller 16 år?')]},
    '0.1021': {'ers': [('måste hon vinna', 'måste spelaren vinna')]},
}
DEL = re.compile(r'([a-f]\) )Beräkna (\\\(.*?\\\))\. Svara exakt\.')
for u in Bank('ma1').arr:
    if not (u['id'].startswith('0.12') and '<p>Räkna med bråktalen.</p>' in (u.get('t') or '')):
        continue
    e = [('<p>Räkna med bråktalen.</p>', '<p>Beräkna. Svara exakt.</p>')]
    for m in DEL.finditer(u['t']):
        e.append((m.group(0), m.group(1) + m.group(2)))
    R[u['id']] = {'ers': e}
