"""Felrapporter 2026-11-16 08:53 och uppföljning av 08:16. Logg: agent/FELRAPPORTER_2026-11-16_0853.md.

Fy2, uppföljning av 4.18: ledtråden ”Skriv kraften från varje fält separat: F_E=qE och F_B=qvB” fanns i 22 uppgifter
med bara ett magnetfält. Där finns ingen elektrisk kraft, och ofta stod också ”Om partikeln går rakt fram måste
krafterna balansera”, som bara gäller hastighetsfilter. Varje sådan ledtråd ersätts med en ledtråd om just den
uppgiften. Uppgifterna med både E- och B-fält (hastighetsfilter: 3.12, 3.114, 4.37, 4.38, 4.46, 4.48, 4.50) är
oförändrade.

Ma5 2.626 c: eleven skrev 9882586 i stället för 3145725π. Facit är rätt: det exakta värdet är 9 882 586,55…, så
decimaltalet är varken exakt eller rätt avrundat. Frågan säger nu uttryckligen att svaret ska innehålla π.

Kör från repots rot. Idempotent: varje ledtråd skrivs till ett fast innehåll.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bankpatch  # noqa: E402

CENTRIPETAL = r'Magnetkraften fungerar som centripetalkraft: \(qvB=\frac{mv^2}{r}\).'
KOMBINERA = r'Accelerationen ger \(qU=\frac{mv^2}{2}\), och i magnetfältet gäller \(qvB=\frac{mv^2}{r}\).'
HOGERHAND = r'Använd högerhandsregeln för en positiv laddning: hastighet, fält och kraft är vinkelräta mot varandra.'


def p(*meningar):
    return '<p>' + ' '.join(meningar) + '</p>'


# id -> {'': huvudledtråd, 'a': delkort a, …}
LEDTRADAR = {
    '3.11': {'': p(r'Magnetkraften \(F=qvB\) är hela tiden vinkelrät mot hastigheten.', CENTRIPETAL),
             'a': p(r'Magnetkraften \(F=qvB\) är hela tiden vinkelrät mot hastigheten. Vad gör en sådan kraft med farten och med riktningen?'),
             'b': p(CENTRIPETAL, r'Lös ut \(r\).')},
    '3.28': {'': p(CENTRIPETAL, r'Använd sedan \(v=\frac{2\pi r}{T}\) och se vad som händer med \(v\) och \(r\).')},
    '3.45': {'': p(r'Beräkna magnetkraften \(F=qvB\) och jämför den med tyngdkraften \(mg\).')},
    '3.46': {'': p(r'Magnetkraften \(F=qvB\) beror på laddningens storlek men inte på massan.',
                   r'Radien får du ur \(qvB=\frac{mv^2}{r}\).')},
    '3.47': {'': p(HOGERHAND, 'En negativ laddning får kraften åt motsatt håll.')},
    '3.52': {'': p(r'Accelerationen ger \(eU=\frac{mv^2}{2}\). I magnetfältet gäller \(evB=\frac{mv^2}{r}\).')},
    '3.53': {'': p(CENTRIPETAL, r'Lös ut \(m\) och jämför med kända partiklars massor.')},
    '3.54': {'': p(r'Ur \(qvB=\frac{mv^2}{r}\) följer \(p=mv=qBr\).', 'Åt vilket håll spåret böjer av visar laddningens tecken.')},
    '3.56': {'': p(r'Bara komposanten vinkelrätt mot fältet, \(v\sin25^\circ\), ger en magnetkraft och en cirkelrörelse.',
                   r'Komposanten längs fältet, \(v\cos25^\circ\), är konstant.')},
    '3.61': {'': p(HOGERHAND)},
    '3.62': {'': p(HOGERHAND, 'Elektronen är negativ, så kraften blir motsatt riktad.')},
    '3.68': {'': p('Kraften på jonen pekar mot banans krökningscentrum.', HOGERHAND)},
    '4.32': {'': p(HOGERHAND, 'Banan böjer av åt samma håll som kraften.'),
             'a': p(HOGERHAND),
             'b': p('Banan böjer av åt samma håll som den magnetiska kraften.')},
    '4.34': {'': p(r'Magnetkraften fungerar som centripetalkraft: \(evB=\frac{mv^2}{r}\).')},
    '4.35': {'': p(r'Magnetkraften fungerar som centripetalkraft: \(evB=\frac{mv^2}{r}\). Tiden i fältet är tiden för en halvcirkel.'),
             'a': p(r'Magnetkraften fungerar som centripetalkraft: \(evB=\frac{mv^2}{r}\). Lös ut \(v\).'),
             'b': p('Protonen går en halvcirkel med konstant fart. Tiden är halva omkretsen delat med farten.')},
    '4.39': {'': p(r'Accelerationen ger \(eU=\frac{mv^2}{2}\). I magnetfältet gäller \(evB=\frac{mv^2}{r}\).'),
             'a': p(r'Accelerationen ger \(eU=\frac{mv^2}{2}\). Lös ut \(v\).'),
             'b': p(r'I magnetfältet fungerar magnetkraften som centripetalkraft: \(evB=\frac{mv^2}{r}\).')},
    '4.40': {'': p(KOMBINERA, r'Eliminera \(v\) och lös ut \(m\).'),
             'a': p(KOMBINERA, r'Eliminera \(v\) och lös ut \(m\).'),
             'b': p(r'Dividera massan med \(1\ \mathrm u\approx1{,}66\cdot10^{-27}\ \mathrm{kg}\).')},
    '4.41': {'': p(KOMBINERA, r'Eliminera \(v\) och se hur radien beror på massan.')},
    '4.43': {'': p(r'Ur \(qvB=\frac{mv^2}{r}\) följer \(\frac qm=\frac{v}{Br}\).'),
             'a': p(r'Ur \(qvB=\frac{mv^2}{r}\) följer \(\frac qm=\frac{v}{Br}\).'),
             'b': p(r'Beräkna \(\frac qm\) för en proton och för en alfapartikel och jämför med ditt värde.')},
    '4.45': {'': p(KOMBINERA, r'Eliminera \(v\) och se hur \(r\) beror på \(U\).')},
    '4.47': {'': p(KOMBINERA, r'Jonerna går en halvcirkel, så träffpunkten ligger \(2r\) från ingången.'),
             'a': p(KOMBINERA, r'Jonerna går en halvcirkel, så träffpunkten ligger \(2r\) från ingången.'),
             'b': p('Jämför avståndet mellan träffpunkterna med det minsta avstånd som detektorn kan skilja på.')},
    '4.57': {'': p(CENTRIPETAL, r'Lös ut \(r\).')},
}
GAMMAL = 'Skriv kraften från varje fält separat'


def satt_ledtradar(u):
    nya = LEDTRADAR[u['id']]
    delar = {d.get('etikett'): d for d in u.get('spelDelar') or []}
    for nyckel, txt in nya.items():
        mal = u if nyckel == '' else delar[nyckel]
        assert GAMMAL in mal['ledtrad'] or mal['ledtrad'] == txt, (u['id'], nyckel)
        mal['ledtrad'] = txt
    for d in [u, *delar.values()]:
        assert GAMMAL not in (d.get('ledtrad') or ''), (u['id'], d.get('etikett'))


def ma5_2626(u):
    gammal = 'Bestäm den sammanlagda arean av alla tio cirklarna. Svara exakt.'
    ny = r'Bestäm den sammanlagda arean av alla tio cirklarna. Svara exakt, alltså med \(\pi\) i svaret.'
    c = u['spelDelar'][2]
    u['t'] = u['t'].replace(gammal, ny)
    c['fraga'] = c['fraga'].replace(gammal, ny)
    c['t'] = c['t'].replace(gammal, ny)
    for x in (u['t'], c['fraga'], c['t']):
        assert ny in x and gammal + '<' not in x


def main():
    bankpatch.andra('uppgifter2.js', {i: satt_ledtradar for i in LEDTRADAR})
    bankpatch.andra('uppgiftermatf1.js', {'2.626': ma5_2626})
    print('Fy2:', len(LEDTRADAR), 'uppgifter. Ma5: 2.626')


if __name__ == '__main__':
    main()
