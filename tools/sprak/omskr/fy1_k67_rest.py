# Fy1 kap 6 och 7: det som återstod efter fy1_kap67.py (2026-11-18).
# "(Svara i J/(kg·K).)" och andra parenteser som generatorn inte kände igen tas bort; två efterfrågade enheter
# flyttas in i frågan; "sammanlagd" heter "total"; "Räkna bara med tyngdkraften och lyftkraften" heter
# "Bortse från vatten-/luftmotståndet"; "Räkna på …" som rubrik tas bort eller skrivs om.
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank, till_platshallare

SPECIAL = {
    '6.315': ([(' (Svara med storleken i N och riktningen med ett ord (uppåt eller nedåt).)', '')], 'Svara med storleken och riktningen (uppåt eller nedåt).'),
    '6.505': ([(' (Svara i N; ballongens egen tyngd ska inte dras bort.)', ' Ballongens egen tyngd ska inte dras bort.'), (' Svara med tre värdesiffror.', '')], None),
    '6.63': ([('a) Vilken tryckskillnad motsvarar höjdskillnaden? (Svara i kPa och mmHg.)', 'a) Vilken tryckskillnad motsvarar höjdskillnaden, i kPa och i mmHg?')], None),
    '6.106': ([('a) Hur mycket högre är vattentrycket i den stängda kranen än lufttrycket? (Svara i kPa och bar.)',
                'a) Hur mycket högre är vattentrycket i den stängda kranen än lufttrycket, i kPa och i bar?')], None),
    '6.447': ([('En extra massa på 0,800 kg', 'En extra vikt med massan 0,800 kg')], None),
    '6.56': ([(' Bara tyngdkraften och golvets normalkraft verkar på lådan.', '')], None),
    '7.191': ([('<p>Räkna på uppvärmning och fasändring.</p>', ''), (' Räkna på uppvärmning och fasändring.', '')], None),
    '7.218': ([('Räkna på följande blandningar.', 'Följande blandningar görs i ett kärl.')], None),
    '7.221': ([('Räkna på följande blandningar.', 'Följande blandningar görs i ett kärl.')], None),
}
PAREN = re.compile(r' ?\(Svara[^()]*(?:\([^()]*\)[^()]*)*\)')
SAMMAN = [('sammanlagda ', 'totala '), ('sammanlagd ', 'total '), ('Sammanlagd ', 'Total ')]
BARA = [('Räkna bara med tyngdkraften, lyftkraften och eventuell kraft från snöret.', None),
        ('Räkna bara med tyngdkraften och vattnets lyftkraft.', None), ('Räkna bara med vattnets lyftkraft och bollens tyngdkraft.', None),
        ('Räkna bara med tyngdkraften och lyftkraften.', None), ('Räkna bara med lyftkraften och tyngdkraften.', None),
        ('Räkna bara med tyngdkraft och lyftkraft.', None),
        ('Räkna bara med behållarnas volym.', 'Bortse från volymen i röret mellan behållarna.')]

b = Bank('fy1')
R = {}
for u in b.arr:
    if u.get('kap') not in (6, 7):
        continue
    raw = ' '.join([u.get('t') or '', u.get('spelIntro') or ''] + [x or '' for d in u.get('spelDelar') or [] for x in (d.get('t'), d.get('fraga'))])
    alla = ' '.join(till_platshallare(x)[0] for x in raw.split('\x00'))
    e, kg = [], None
    if u['id'] in SPECIAL:
        par, kg = SPECIAL[u['id']]
        for a, c in par:
            if a in alla:
                e.append((a, c)); alla = alla.replace(a, c)
    for m in list(PAREN.finditer(alla)):
        if m.group(0) in alla and raw.count(m.group(0)) == alla.count(m.group(0)):
            e.append((m.group(0), '')); alla = alla.replace(m.group(0), '')
    for a, c in SAMMAN:
        if a in alla and raw.count(a) == alla.count(a):
            e.append((a, c)); alla = alla.replace(a, c)
    for a, c in BARA:
        if a in alla:
            if c is None:
                c = 'Bortse från luftmotståndet.' if re.search(r'\bluft|ballong|helium|vätgas', alla) else 'Bortse från vattenmotståndet.'
            e.append((a, c)); alla = alla.replace(a, c)
    if e or kg:
        R[u['id']] = {'ers': e}
        if kg:
            R[u['id']]['kg'] = kg
