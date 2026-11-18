# Fy2 kapitel 4 del 1 (EM-vågor, vågrörelselära, temperaturstrålning, stråloptik): handgenomläsning 2026-11-18.
# Stefan–Boltzmanns lag med σ och Wiens konstant står i formelsamlingen och stryks ur frågorna.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

SB = (r'<p>Stefan–Boltzmanns lag: \(M=e\sigma T^4\) där \(\sigma=5{,}67\cdot10^{-8}\) W/(m²K⁴) och \(e\) är emissionstalet '
      r'(1 för en svart kropp). Nettoeffekt: \(P=e\sigma A\left(T^4-T_0^4\right)\).</p>')
R = {
    '4.56': {'ers': [('Bestäm gitterkonstanten, alltså avståndet mellan två intilliggande spalter, uttryckt i meter.', 'Bestäm gitterkonstanten.')]},
    '4.6': {'ers': [('Det synliga området kan tas som 400–700 nm.', 'Synligt ljus har våglängder mellan 400 och 700 nm.')]},
    '4.59': {'ers': [(' Wiens konstant är 2,898·10<sup>−3</sup> m·K.', '')]},
    '4.369': {'ers': [('Ljuset går 1,00 m i vakuum på en viss tid.', '<p>Ljuset går 1,00 m i vakuum på 3,34 ns.</p>')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(SB in x for x in falt):
        R.setdefault(u['id'], {}).setdefault('ers', []).insert(0, (SB, ''))
