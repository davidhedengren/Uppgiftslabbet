"""Felrapporter från Kunskapsgymmet 2026-11-16 08:16 (Lars-Åke Andersson). Logg: agent/FELRAPPORTER_2026-11-16_0816.md.

Fy2 3.208: ”Ta bort pilen med I jämte figuren. Den förvirrar bara.” Den röda lodräta pilen med ett minustecken till
höger om slingan (tänkt som ”fältet minskar”) tas bort. Texten säger redan att fältet minskar.

Fy2 4.18 a: ”Får fel med 2 värdesiffror skrev 2.0*10^7 istf 1.96*10^7.” Spänningen 2,0 MV har två värdesiffror, så
a och b får svarVardesiffror 2: ett svar godtas om det är facit korrekt avrundat till elevens precision (2,0·10^7 och
1,96·10^7). Facit för b räknas om: 6,626·10^-34 / (1,67·10^-27 · 1,96·10^7) = 2,02·10^-14 m (inte 2,03).
Ledtråden handlade om fältkrafter (qE, qvB) och byts mot en ledtråd om energi och de Broglies samband. Samma
felplacerade mening fanns i 4.17 och 4.27, där det inte heller finns några fält.

Fy2 3.29: ”Vinkelmarkeringen (själva böjen) är upp och ned.” Bågen för 30° hade sweep-flaggan 0, så dess mittpunkt
hamnade ovanför nålen. Med sweep 1 ligger mittpunkten i kompassens centrum. Alla banker är genomsökta efter samma
fel (en båge vars mittpunkt inte är ett hörn i figuren men vars spegling är det): bara 3.29 hade det.

Kör från repots rot. Idempotent: varje ändring skrivs till ett fast innehåll.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bankpatch  # noqa: E402

FALTMENING = r' Skriv kraften från varje fält separat: \(F_E=qE\) och \(F_B=qvB\).'


def fy2_3208(u):
    pil = re.compile(r'<line x1="296" y1="60" x2="296" y2="180"[^>]*/><polygon points="296\.0,180\.0 302\.0,170\.0 290\.0,170\.0"[^>]*/>'
                     r'<text x="296" y="198"[^>]*>−</text>')
    u['t'] = pil.sub('', u['t'])
    assert 'x1="296"' not in u['t'] and '>−</text>' not in u['t']


def fy2_3029(u):
    u['t'] = u['t'].replace('A 26 26 0 0 0 181 93.48', 'A 26 26 0 0 1 181 93.48')
    assert 'A 26 26 0 0 1 181 93.48' in u['t']


def utan_faltmening(u):
    u['ledtrad'] = u['ledtrad'].replace(FALTMENING, '')
    for p in u.get('spelDelar') or []:
        if p.get('ledtrad'):
            p['ledtrad'] = p['ledtrad'].replace(FALTMENING, '')


def fy2_418(u):
    # Exakt värde med m_p = 1,6726·10^-27 kg, så att också svar med fyra siffror (1,957·10^7) jämförs rätt.
    u['rättSvar'] = [19573000, 2.02e-14, None]
    u['tolerans'] = [294000, 3e-16, None]
    u['svarVardesiffror'] = [2, 2, None]
    gammal, ny = r'2{,}03\cdot10^{-14}', r'2{,}02\cdot10^{-14}'
    kvot_g, kvot_n = r'\approx4{,}9\cdot10^3', r'\approx5{,}0\cdot10^3'
    u['s'] = u['s'].replace(gammal, ny).replace(kvot_g, kvot_n)
    u['ledtrad'] = (r'<p>Protonens rörelseenergi efter accelerationen är \(eU\). Sätt den lika med \(\frac{m_pv^2}{2}\) '
                    r'för att få farten, och använd sedan de Broglies samband \(\lambda=\frac{h}{m_pv}\).</p>')
    a, b, c = u['spelDelar']
    a['ledtrad'] = (r'<p>Protonens rörelseenergi efter accelerationen är \(eU\). Sätt \(eU=\frac{m_pv^2}{2}\) '
                    r'och lös ut \(v\).</p>')
    b['s'] = b['s'].replace(gammal, ny)
    b['ledtrad'] = (r'<p>Bestäm först farten ur \(eU=\frac{m_pv^2}{2}\). Använd sedan de Broglies samband '
                    r'\(\lambda=\frac{h}{p}=\frac{h}{m_pv}\).</p>')
    c['t'] = c['t'].replace(gammal, ny)
    c['s'] = c['s'].replace(gammal, ny).replace(kvot_g, kvot_n).replace(
        r'Atomstorleken är ungefär \(4{,}9\cdot10^3\) gånger större.', r'Atomstorleken är ungefär \(5{,}0\cdot10^3\) gånger större.')
    c['ledtrad'] = '<p>Skriv atomstorleken i meter och dividera den med våglängden.</p>'
    for x in (u['s'], b['s'], c['t'], c['s']):
        assert '2{,}03' not in x
    assert r'4{,}9\cdot10^3' not in c['s']


FY2 = {
    '3.208': fy2_3208,
    '3.29': fy2_3029,
    '4.17': utan_faltmening,
    '4.18': fy2_418,
    '4.27': utan_faltmening,
}


def main():
    bankpatch.andra('uppgifter2.js', FY2)
    print('Fy2:', sorted(FY2))


if __name__ == '__main__':
    main()
