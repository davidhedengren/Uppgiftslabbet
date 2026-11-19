# Ma2 genomläsning, del 1 (2026-11-19): tips i frågan, svarsfält och planeringsjargong.
KOORD = '<p>Skriv x-koordinaten i första svarsfältet och y-koordinaten i det andra.</p>'
R = {
    '2.788': {'ers': [(r' (Tips: kalla \(x-1\) för \(t\).)', r' Använd substitutionen \(t=x-1\).')]},
    '1.922': {'ers': [(' Tips: subtrahera den nedre ekvationen från den övre.', '')]},
    '5.36': {'ers': [('Vid en planeringsövning för social dokumentation används modellen', 'Tiden för social dokumentation beskrivs av modellen')]},
    '5.43': {'ers': [('Timkostnaden i planeringskalkylen är', 'Timkostnaden är')]},
    '5.50': {'ers': [('I planeringsskissen reserveras en 1 m bred fri passage', 'En 1 m bred fri passage ska finnas')]},
    '5.54': {'ers': [('I övningen används 30 % som en intern planeringsgräns för omladdning.', 'Larmet ska laddas när batterinivån når 30 %.')]},
}
for i in ('3.134', '3.184', '3.201', '3.341', '3.343'):
    R[i] = {'ers': [(KOORD, '')], 'kg': 'Skriv x-koordinaten i första svarsfältet och y-koordinaten i det andra.'}
