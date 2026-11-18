# Fy2 induktion i ledare och växelström: handgenomläsning 2026-11-18.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FORMEL = (r'<p>En spole med \(N\) varv och arean \(A\) som roterar med vinkelhastigheten \(\omega\) i ett homogent magnetfält '
          r'\(B\) ger spänningen \(u=\hat u\sin\omega t\), där \(\hat u=NBA\omega\).</p>')
PARVIS = 'Staven, rörelseriktningen och magnetfältet är parvis vinkelräta.'
R = {
    '3.89': {'ers': [(' Toppvärdet av den inducerade spänningen ges av ε = NBAω.', '')]},
    '3.20': {'ers': [('i ett rent resistivt element på 46 Ω?', 'i ett motstånd på 46 Ω?')]},
    '3.139': {'ers': [('En ren resistor på 92 Ω ansluts till 230 V effektiv växelspänning.', 'Ett motstånd på 92 Ω ansluts till en växelspänning med effektivvärdet 230 V.')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    alla = ' '.join(falt)
    if FORMEL in alla:
        R.setdefault(u['id'], {}).setdefault('ers', []).insert(0, (FORMEL, ''))
    # "parvis vinkelräta" upprepar bara "rör sig vinkelrätt mot fältet" i samma uppgift
    if PARVIS in alla and 'vinkelrätt mot ett homogent magnetfält' in alla:
        e = R.setdefault(u['id'], {}).setdefault('ers', [])
        e += [(' ' + PARVIS, ''), ('<p>' + PARVIS + '</p>', ''), (PARVIS, '')]
