# Fy2: inledande formelstycken stryks (2026-11-18), som i Fy1. Formlerna står i formelsamlingen.
# Kvar står samband som inte är standard i formelsamlingen eller som definierar en beteckning:
# strängens våghastighet med µ, platta spolens fält, ljudhastighetens temperaturberoende och Bohrs radier/farter.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

STYCKEN = [
    r'<p>En massa \(m\) i en fjäder med fjäderkonstanten \(k\) svänger med perioden \(T=2\pi\sqrt{\dfrac mk}\).</p>',
    r'<p>En sträng fäst i båda ändar har stående vågor när \(l=n\cdot\dfrac\lambda2\).</p>',
    r'<p>Öppen pipa: \(l=n\cdot\dfrac\lambda2\). Halvöppen pipa: \(l=(2k+1)\cdot\dfrac\lambda4\).</p>',
    r'<p>I en lång spole är \(B=\mu_r\mu_0\dfrac{NI}{l}\) (\(\mu_r=1\) utan kärna).</p>',
    r'<p>Gitterekvationen: \(d\sin\alpha_n=n\lambda\).</p>',
    r'<p>de Broglie-våglängd: \(\lambda=\dfrac hp=\dfrac{h}{mv}\).</p>',
    r'<p>Wiens förskjutningslag: \(\lambda_{max}T=2{,}898\cdot10^{-3}\) m·K.</p>',
    r'<p>En plan pendel med längden \(l\) har vid små utslag perioden \(T=2\pi\sqrt{\dfrac lg}\).</p>',
    r'<p>Fotonens energi: \(E=hf=\dfrac{hc}{\lambda}\).</p>',
    r'<p>Reaktanser: \(X_L=2\pi fL\) och \(X_C=\dfrac{1}{2\pi fC}\).</p>',
    r'<p>Tidsdilatation: \(\Delta t=\gamma\,\Delta t_0\), där \(\gamma=\dfrac{1}{\sqrt{1-v^2/c^2}}\).</p>',
    r'<p>Två källor i fas: maximum när vägskillnaden \(\Delta s=n\lambda\), minimum när \(\Delta s=(n+\tfrac12)\lambda\).</p>',
]
R = {}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    e = [(s, '') for s in STYCKEN if any(s in x for x in falt)]
    if e:
        R[u['id']] = {'ers': e}
R.setdefault('6.301', {}).setdefault('ers', []).append((r'Bestäm Lorentzfaktorn \(\gamma=1/\sqrt{1-v^2/c^2}\).', r'Bestäm Lorentzfaktorn \(\gamma\).'))
