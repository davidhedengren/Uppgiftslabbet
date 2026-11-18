# Fy2 ljud och hörsel: handgenomläsning 2026-11-18.
# Formelraden om ljudnivå och intensitet stryks, liksom hörtröskeln I0 (konstant i formelsamlingen).
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FORMEL = (r'<p>Ljudnivå: \(L=10\lg\dfrac{I}{I_0}\) där \(I_0=1{,}0\cdot10^{-12}\) W/m². En källa som sänder ut effekten \(P\) '
          r'lika mycket åt alla håll ger intensiteten \(I=\dfrac{P}{4\pi r^2}\) på avståndet \(r\).</p>')
R = {
    '2.172': {'ers': [(' Hörtröskeln är 1,0·10<sup>−12</sup> W/m<sup>2</sup>.', '')]},
    '2.194': {'ers': [(r' Referensintensiteten är \(I_0=1{,}0\cdot10^{-12}\,\mathrm{W/m^2}\).', '')]},
    '2.195': {'ers': [(r' Referensintensiteten är \(I_0=1{,}0\cdot10^{-12}\,\mathrm{W/m^2}\).', '')]},
    '2.334': {'ers': [('<p>Ljudintensiteter från flera källor på samma ställe adderas.</p>', '')]},
    '2.108': {'ers': [('En hundvissla avger 24 kHz. Klassificera ljudet för en människa: infraljud, hörbart ljud eller ultraljud.',
                       'En hundvissla ger ljud med frekvensen 24 kHz. Är det infraljud, hörbart ljud eller ultraljud för en människa?')]},
    '2.103': {'ers': [('uppskatta högtalarens akustiska effekt', 'uppskatta högtalarens ljudeffekt')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(FORMEL in x for x in falt):
        R.setdefault(u['id'], {}).setdefault('ers', []).insert(0, (FORMEL, ''))
