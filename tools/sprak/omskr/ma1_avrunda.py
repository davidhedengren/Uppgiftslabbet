"""Ma1 (2026-11-20): "Svara med två decimaler." heter "Avrunda till två decimaler." som i lärarens matteprov.
"Svara i U med två decimaler." blir "Avrunda till två decimaler." när svarEnhet visar enheten, annars
"Svara i U och avrunda till två decimaler." ("i procent" behålls alltid, eftersom procent är en del av svaret).
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

RX = re.compile(r'Svara (i ([^ .]+) )?med (en|två|tre|fyra) (decimal|decimaler)\.')
R = {}
for u in Bank('ma1').arr:
    falt = [u.get('t') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    har_enhet = any([u.get('svarEnhet')] + [d.get('svarEnhet') for d in u.get('spelDelar') or []])
    e = []
    for x in falt:
        for m in RX.finditer(x):
            avr = f'avrunda till {m.group(3)} {m.group(4)}.'
            enhet = m.group(2)
            if enhet and (enhet == 'procent' or not har_enhet):
                ny = f'Svara i {enhet} och {avr}'
            else:
                ny = 'A' + avr[1:]
            if (m.group(0), ny) not in e:
                e.append((m.group(0), ny))
    if e:
        R[u['id']] = {'ers': e}
