# Ma3c handgenomläsning: integral_area, integral_tillampningar (2026-11-19).
# "Bestäm den totala förändringen" säger inte vad som förändras.
def fraga(a, b, ny):
    return (rf'Bestäm den totala förändringen från \(t=0\) till \(t={b}\).', rf'{ny} från \(t=0\) till \(t={b}\)?')


R = {
    '3.48': {'ers': [('Två vägar i en förenklad karta beskrivs av', 'Två vägar på en karta beskrivs av')]},
    '3.326': {'ers': [('Hur långt cyklar hon under 5 s?', 'Hur långt cyklar cyklisten under 5 s?')]},
    '3.593': {'ers': [fraga(0, 8, 'Hur mycket vatten rinner in i tanken')]},
    '3.597': {'ers': [fraga(0, 10, 'Hur mycket vatten pumpas in i bassängen')]},
    '3.598': {'ers': [fraga(0, 4, 'Hur långt kör bilen')]},
    '3.600': {'ers': [fraga(0, 3, 'Hur mycket av ämnet tillförs')]},
}
