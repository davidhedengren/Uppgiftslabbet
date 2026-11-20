"""Ma1 (2026-11-20): svarsinstruktioner i parentes, "(Svara i kr.)", blir som i lärarens matteprov.

Enhet som svarEnhet redan visar tas bort, "med ett (hel)tal" tas bort, avrundning blir "Avrunda till …",
övrigt står som vanlig mening utan parentes. Samma regel som ma2_alla.py.
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

ORD = {'en': 'en decimal', 'två': 'två decimaler'}


def ny_text(inre, har_enhet):
    m = re.fullmatch(r'Svara i ([^ ]+?)\.', inre)
    if m:
        return '' if har_enhet else f'Svara i {m.group(1)}.'
    if inre in ('Svara med ett tal.', 'Svara med ett heltal.'):
        return ''
    if inre == 'Svara i procent med en decimal.' and not har_enhet:
        return 'Svara i procent med en decimal.'
    m = re.fullmatch(r'Svara (?:i [^ ]+ )?med (en|två) decimal(?:er)?\.', inre)
    if m:
        return f'Avrunda till {ORD[m.group(1)]}.'
    if inre == 'Svara i hela kg.':
        return 'Avrunda till hela kilogram.'
    if inre == 'Svara i ml, avrundat till heltal.':
        return 'Avrunda till hela milliliter.'
    return inre  # t.ex. "Svara på formen 1:x." och "Svara i grundpotensform med två värdesiffror."


R = {}
for u in Bank('ma1').arr:
    falt = [u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    enheter = [u.get('svarEnhet')] + [d.get('svarEnhet') for d in u.get('spelDelar') or []]
    har_enhet = any(e for e in enheter)
    e = []
    for x in falt:
        for m in re.finditer(r' ?\((Svara[^()]*)\)', x):
            ny = ny_text(m.group(1), har_enhet)
            par = (m.group(0), (' ' + ny) if ny and m.group(0).startswith(' ') else ny)
            if par not in e:
                e.append(par)
    if e:
        R[u['id']] = {'ers': e}
if __name__ == '__main__':
    for k, v in R.items():
        print(k, v['ers'])
