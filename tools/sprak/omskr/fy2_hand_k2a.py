# Fy2 kapitel 2 (pendlar, vågrörelser, stående vågor): handgenomläsning 2026-11-18.
# Formelraden för strängens våghastighet stryks också: övriga uppgifter i området (2.67, 2.125, 2.134, 2.178)
# förutsätter redan att eleven har sambandet från formelsamlingen.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

FORMEL = r'<p>Våghastigheten i en spänd sträng är \(v=\sqrt{\dfrac{F}{\mu}}\), där \(\mu\) är massan per längdenhet.</p>'
R = {
    '2.176': {'ers': [('Luftmotståndet är så litet att du kan bortse från det.', 'Bortse från luftmotståndet.')]},
    '2.498': {'ers': [('En plan pendel och en massa som svänger i en fjäder', 'En plan pendel och en vikt som svänger i en fjäder')]},
    '2.64': {'ers': [(' Du kan ange den som en vinkel, i radianer eller som en tidsförskjutning uttryckt med perioden \\(T\\), och beskriv gärna med ord.', '')]},
    '2.429': {'ers': [('röra sig sammanlagt 1,0 km', 'röra sig totalt 1,0 km')]},
    '2.131': {'ers': [('En sträng är fixerad i båda ändar', 'En sträng är fast i båda ändar')]},
}
b = Bank('fy2')
for u in b.arr:
    falt = [u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))]
    if any(FORMEL in x for x in falt):
        R.setdefault(u['id'], {}).setdefault('ers', []).insert(0, (FORMEL, ''))
R['2.178'] = {'ers': [(' Våghastigheten på en sträng ges av <em>v</em> = √(<em>F</em>/<em>μ</em>), där <em>μ</em> är massan per längdenhet.', '')]}
