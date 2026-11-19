# Ma3c handgenomläsning: extrempunkter, derivatan_och_grafen, problemlosning_derivata, deriverbarhet (2026-11-19).
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

R = {
    '2.145': {'ers': [('derivatan är nolla', 'derivatan är noll')]},
    '2.276': {'ers': [('där tangenten är horisontella', 'där tangenten är horisontell')]},
    '2.170': {'ers': [(r'Skissa mentalt formen på \(f^{\prime}\) och avgör', r'Hur ser grafen till \(f^{\prime}\) ut? Avgör')]},
    '2.267': {'ers': [(r'Skissa i tanken två olika möjliga grafer till \(f\) och förklara', r'Tänk dig två olika möjliga grafer till \(f\) och förklara')]},
    '3.522': {'ers': [(r'En bollkastares höjd över marken kan modelleras med \(h(t)',
                       r'En boll kastas uppåt. Bollens höjd över marken kan modelleras med \(h(t)')]},
    '3.653': {'ers': [(r'\(t=1,5\)', r'\(t=1{,}5\)')]},
}
# "Derivatan är f'(x)=(x-2)(x-9), där 2 och 9 är olika tal." – bisatsen säger ingenting
RX = re.compile(r', där -?\d+ och -?\d+ är olika tal')
for u in Bank('mato1').arr:
    for m in RX.finditer(u.get('t') or ''):
        R.setdefault(u['id'], {'ers': []})['ers'].append((m.group(0), ''))
