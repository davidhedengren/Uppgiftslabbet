# Ma3c handgenomläsning: andringskvoter, begreppet_derivata, derivatans_definition, numerisk_derivering (2026-11-19).
VISA = '<p>Visa i din lösning att du har undersökt både derivatans nollställen och intervallets ändpunkter.</p>'
R = {
    '2.01': {'ers': [(r'En växts höjd \(h\) mäts i centimeter.', r'En växt är \(h(t)\) cm hög \(t\) veckor efter planteringen.'),
                     (r'mellan \(t=2\) veckor och \(t=6\) veckor.', 'mellan vecka 2 och vecka 6.')]},
    '2.225': {'ers': [('En tabell ger följande funktionsvärden:', r'Tabellen visar några värden för funktionen \(f\).')]},
    '2.1149': {'ers': [(r'Eleven sätter in \(h=0\)', r'Sedan sätter Märta in \(h=0\)')]},
    '2.523': {'ers': [('Svara med minst två decimaler.', 'Avrunda till två decimaler.')]},
    '3.842': {'ers': [('3t^2+2t+0', '3t^2+2t')]},
    '3.850': {'ers': [('3t^2+2t+0', '3t^2+2t')]},
    '3.1106': {'ers': [('meter, där t mäts i sekunder. Bestäm hastigheten vid t = 1 s.', r'meter, där \(t\) mäts i sekunder. Bestäm hastigheten vid \(t=1\) s.')]},
}
for i in ('2.339', '2.340', '2.341', '2.342', '2.343'):
    R[i] = {'ers': [(VISA, '')]}
