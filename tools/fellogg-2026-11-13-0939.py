"""Felrapporter från Kunskapsgymmet 2026-11-13 09:39 (Lars-Åke Andersson). Logg: agent/FELRAPPORTER_2026-11-13_0939.md.

Fy2 4.3: ”Dopplereffekt har vi valt att inte ha med – varken ljud eller ljus.” Dopplerdelarna tas bort i 4.3 och i
liknande uppgifter (2.112, 2.114, 2.115, 5.52, 5.379, 5.380). Delmomentet ”Infraljud, ultraljud och dopplereffekt” heter åter
”Infraljud och ultraljud”.

Ma5 4.358: separabla differentialekvationer tas sällan upp. Uppgiften ger lösningsformen och frågar efter
begynnelsevärdet och en kontroll genom derivering.

Ma5 2.179 och 2.468: ”Vi tar inte upp hur man löser rekursionsformler allmänt till explicita formler.” Samma
jämviktsmetod fanns i 2.15, 2.180, 2.203 och 2.204. Nu ges den explicita formeln, och eleven kontrollerar och
använder den, eller också hittar eleven den genom ett mönster med stöd i frågan (2.56, 2.180).

Kör från repots rot. Idempotent: varje uppgift skrivs till ett fast innehåll.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bankpatch  # noqa: E402


def steg(rubrik, *rader):
    return f'<li><p class="facit-rubrik">{rubrik}</p>' + ''.join(r if r.startswith('<') else f'<p>{r}</p>' for r in rader) + '</li>'


def facit(stegen, svar):
    return ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ''.join(stegen) + '</ol>'
            f'<p class="facit-svar"><strong>Svar:</strong> {svar}</p></div>')


def del_facit(et, stegen, svar):
    return (f'<div class="facit-del"><span class="facit-mark">{et})</span><div class="facit-arbete"><ol class="facit-steglista" role="list">'
            + ''.join(stegen) + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div></div>')


# ============================================================================ Fy2

GAMMAL_FAM, NY_FAM = 'Infraljud, ultraljud och dopplereffekt', 'Infraljud och ultraljud'


def byt_familj(u):
    if u['familj'] in (GAMMAL_FAM, NY_FAM) and u['omr'] == 'ljud_horsel':
        u['familj'] = NY_FAM
        tid = [f for f in (u.get('familjTidigare') or []) if f != NY_FAM]
        if GAMMAL_FAM not in tid:
            tid.append(GAMMAL_FAM)
        u['familjTidigare'] = tid


def fy2_43(u):
    u['typ'] = 'beräkna gångtid och våglängd för radiosignal, ur text, sökt tid och våglängd'
    u['niva'], u['poang'] = 'E', '(2/0/0)'
    u['t'] = (r'<p>En rymdsond kommunicerar med jorden med radiovågor med frekvensen 8,4 GHz. Sonden befinner sig '
              r'\(2{,}25\cdot10^{11}\) m från jorden.</p><p>a) Hur lång tid tar det för signalen att nå jorden?</p>'
              r'<p>b) Vilken våglängd har signalen?</p>')
    u['s'] = ('<div class="facit-v2 facit-stegvis">'
              + del_facit('a', [steg('Givet och sökt', r'Avståndet är \(d=2{,}25\cdot10^{11}\ \mathrm m\). Radiovågor färdas med ljusfarten \(c\). Sökt: tiden \(t\).'),
                                steg(r'Sträcka = fart · tid: \(d=ct\)', r'\[t=\frac dc=\frac{2{,}25\cdot10^{11}}{2{,}998\cdot10^8}\ \mathrm s=751\ \mathrm s\]',
                                     r'\(751\ \mathrm s\) är ungefär \(12{,}5\) minuter.')],
                         r'Signalen tar \(751\ \mathrm s\), alltså cirka \(12{,}5\) minuter.')
              + del_facit('b', [steg('Givet och sökt', r'Frekvensen är \(f=8{,}4\ \mathrm{GHz}=8{,}4\cdot10^9\ \mathrm{Hz}\). Sökt: våglängden \(\lambda\).'),
                                steg(r'Vågekvationen: \(c=f\lambda\)', r'\[\lambda=\frac cf=\frac{2{,}998\cdot10^8}{8{,}4\cdot10^9}\ \mathrm m=0{,}0357\ \mathrm m\]')],
                         r'Våglängden är cirka \(3{,}6\ \mathrm{cm}\).')
              + '</div>')
    u['ledtrad'] = r'<p>Radiovågor färdas med ljusfarten. Använd sträcka = fart · tid för tiden och \(c=f\lambda\) för våglängden.</p>'


def fy2_2114(u):
    u['typ'] = 'bestämma avstånd med ekolod och ultraljudets våglängd, ur text och figur, sökt avstånd och våglängd'
    u['niva'], u['poang'] = 'C', '(1/1/0)'
    fig = u['t'][u['t'].index('<span class="fig'):]
    fig = re.sub(r'<line x1="351\.000" y1="69\.000"[^>]*/>', '', fig)
    fig = re.sub(r'<polygon points="432,69[^"]*"[^>]*/>', '', fig)
    fig = re.sub(r'<text x="394\.00" y="53\.00"[^>]*>v</text>', '', fig)
    fig = fig.replace('Fartyg rör sig längs ljudets utbredningsriktning bort från en stilla ubåt',
                      'Ultraljudspuls från en ubåt till ett fartyg och ekot tillbaka')
    assert '>v</text>' not in fig and 'rör sig' not in fig
    u['t'] = ('<p>En stillaliggande ubåt sänder en ultraljudspuls med frekvensen 30 kHz mot ett fartyg. Ekot från fartyget kommer '
              'tillbaka till ubåten 0,48 s efter att pulsen skickades. Ljudets fart i havsvatten är 1500 m/s.</p>'
              '<p>a) Hur långt från ubåten är fartyget?</p><p>b) Vilken våglängd har ultraljudet i vattnet?</p>' + fig)
    u['s'] = ('<div class="facit-v2 facit-stegvis">'
              + del_facit('a', [steg('Givet och sökt', r'Ljudets fart är \(v=1500\ \mathrm{m/s}\). Tiden \(t=0{,}48\ \mathrm s\) gäller vägen fram till fartyget och tillbaka. Sökt: avståndet \(d\).'),
                                steg(r'Ekot går sträckan \(2d\): \(2d=vt\)', r'\[d=\frac{vt}2=\frac{1500\cdot0{,}48}{2}\ \mathrm m=360\ \mathrm m\]')],
                         r'Fartyget är \(360\ \mathrm m\) från ubåten.')
              + del_facit('b', [steg('Givet och sökt', r'Frekvensen är \(f=30\ \mathrm{kHz}=3{,}0\cdot10^4\ \mathrm{Hz}\). Sökt: våglängden \(\lambda\).'),
                                steg(r'Vågekvationen: \(v=f\lambda\)', r'\[\lambda=\frac vf=\frac{1500}{3{,}0\cdot10^4}\ \mathrm m=0{,}050\ \mathrm m\]')],
                         r'Våglängden är \(5{,}0\ \mathrm{cm}\).')
              + '</div>')
    u['ledtrad'] = '<p>Ekot har gått både fram till fartyget och tillbaka.</p>'


FIG_2115 = ('<span class="fig smal"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="480" height="270" role="img" '
            'aria-label="En ultraljudsgivare på huden skickar en puls ner till en gränsyta mellan två organ. Ekot går tillbaka upp till givaren. '
            'Djupet d till gränsytan är okänt." style="max-width:100%;height:auto"><title>Ultraljudspuls och eko i kroppen</title>'
            '<rect width="480" height="270" fill="white"/>'
            '<rect x="20" y="70" width="440" height="180" fill="#fbeee9"/>'
            '<rect x="20" y="190" width="440" height="60" fill="#f1d3c8"/>'
            '<line x1="20" y1="70" x2="460" y2="70" stroke="#8a5a44" stroke-width="2.4"/>'
            '<text x="30" y="60" font-family="Arial, sans-serif" font-size="15" fill="#223047">hud</text>'
            '<line x1="20" y1="190" x2="460" y2="190" stroke="#8a5a44" stroke-width="2" stroke-dasharray="7 5"/>'
            '<text x="30" y="214" font-family="Arial, sans-serif" font-size="15" fill="#223047">gränsyta mellan två organ</text>'
            '<rect x="190" y="34" width="100" height="36" rx="4" fill="#eaf2f8" stroke="#223047" stroke-width="2"/>'
            '<text x="240" y="57" font-family="Arial, sans-serif" font-size="15" fill="#223047" text-anchor="middle">givare</text>'
            '<line x1="222" y1="74" x2="222" y2="178" stroke="#2867a8" stroke-width="2.4"/><polygon points="222,186 217,175 227,175" fill="#2867a8"/>'
            '<text x="212" y="135" font-family="Arial, sans-serif" font-size="14" fill="#2867a8" text-anchor="end">puls</text>'
            '<line x1="258" y1="186" x2="258" y2="82" stroke="#b54b42" stroke-width="2.4"/><polygon points="258,74 253,85 263,85" fill="#b54b42"/>'
            '<text x="268" y="135" font-family="Arial, sans-serif" font-size="14" fill="#b54b42">eko</text>'
            '<line x1="390" y1="70" x2="390" y2="190" stroke="#223047" stroke-width="1.6"/>'
            '<line x1="382" y1="70" x2="398" y2="70" stroke="#223047" stroke-width="1.6"/><line x1="382" y1="190" x2="398" y2="190" stroke="#223047" stroke-width="1.6"/>'
            '<text x="402" y="136" font-family="Arial, sans-serif" font-size="17" fill="#223047" font-style="italic">d</text>'
            '</svg></span>')


def fy2_2115(u):
    u['typ'] = 'bestämma djup med ultraljudseko i kroppen, ur text och figur, sökt djup'
    u['niva'], u['poang'] = 'C', '(0/1/0)'
    u['formaga'] = ['procedur', 'begrepp']
    u['rättSvar'], u['tolerans'], u['svarEnhet'], u['svarVardesiffror'] = 5.005, 0.05, 'cm', 2
    u.pop('manuellKomplettering', None)
    u['t'] = ('<p>Vid en ultraljudsundersökning skickar givaren en kort puls in i kroppen. Ekot från gränsytan mellan två organ kommer '
              'tillbaka till givaren 65 µs efter att pulsen skickades. Ljudets fart i kroppsvävnad är 1540 m/s.</p>'
              '<p>Hur djupt under huden ligger gränsytan? (Svara i cm.)</p>' + FIG_2115)
    u['s'] = facit([steg('Givet och sökt', r'Ljudets fart är \(v=1540\ \mathrm{m/s}\). Tiden \(t=65\ \mathrm{\mu s}=65\cdot10^{-6}\ \mathrm s\) gäller vägen ner till gränsytan och upp igen. Sökt: djupet \(d\).'),
                    steg(r'Ekot går sträckan \(2d\): \(2d=vt\)', r'\[d=\frac{vt}2=\frac{1540\cdot65\cdot10^{-6}}{2}\ \mathrm m=0{,}0501\ \mathrm m\]',
                         r'\(0{,}0501\ \mathrm m\) är \(5{,}0\ \mathrm{cm}\).')],
                   r'Gränsytan ligger \(5{,}0\ \mathrm{cm}\) under huden.')
    u['ledtrad'] = '<p>Ekot går både ner till gränsytan och upp igen.</p>'


KVASAR = r'<p>En kvasar har rödförskjutningen \(z=0{,}25\). Hubblekonstanten i modellen är \(70\) km/(s·Mpc).</p>'
RATT_552 = 'Universum expanderar medan ljuset är på väg, så ljusets våglängd sträcks ut'
ALT_552 = [
    {'txt': RATT_552, 'ratt': True},
    {'txt': 'Kvasaren är kall och sänder därför ut rött ljus', 'ratt': False,
     'kommentar': 'Rödförskjutning betyder att hela spektrumet har flyttats mot längre våglängder, inte att källan är röd.'},
    {'txt': 'Ljuset tappar fart på vägen genom rymden', 'ratt': False,
     'kommentar': 'Ljusets fart i vakuum är alltid c. Det är våglängden som ändras.'},
    {'txt': 'Damm mellan oss och kvasaren färgar ljuset rött', 'ratt': False,
     'kommentar': 'Damm flyttar inte spektrallinjerna. Rödförskjutningen gäller alla linjer i spektrumet.'},
]


def fy2_552(u):
    d_mpc = 0.25 * 299792.458 / 70
    t_gar = d_mpc * 1e6 * 3.26156 / 1e9
    assert abs(t_gar - 3.492) < 0.001
    u['typ'] = 'beräkna fart och avstånd ur rödförskjutning, ljusets gångtid och förklara rödförskjutningen, ur text, sökt fart, avstånd och tid'
    u['niva'], u['poang'], u['traningsniva'] = 'C', '(1/2/0)', 3
    u['formaga'] = ['procedur', 'begrepp']
    u['t'] = (KVASAR + '<p><strong>a)</strong> Bestäm farten bort från oss med \\(v=zc\\) och avståndet med Hubbles lag. (Svara i km/s och Mpc.)</p>'
              '<p><strong>b)</strong> Ungefär hur länge har ljuset från kvasaren varit på väg, om man räknar med \\(t=d/c\\)? (Svara i miljarder år.)</p>'
              '<p><strong>c)</strong> Vad orsakar kvasarens rödförskjutning enligt dagens kosmologi?</p>')
    a_steg = [steg('Givet och sökt', r'\(z=0{,}25\) och \(H_0=70\ \mathrm{km/(s\cdot Mpc)}\). Sökt: farten \(v\) och avståndet \(d\).'),
              steg(r'Farten ur rödförskjutningen: \(v=zc\)', r'\[v=0{,}25\cdot2{,}998\cdot10^5\ \mathrm{km/s}=7{,}50\cdot10^4\ \mathrm{km/s}\]'),
              steg(r'Hubbles lag: \(v=H_0d\)', r'\[d=\frac v{H_0}=\frac{7{,}50\cdot10^4}{70}\ \mathrm{Mpc}=1{,}07\cdot10^3\ \mathrm{Mpc}\]')]
    a_svar = r'Farten är \(7{,}5\cdot10^4\ \mathrm{km/s}\) och avståndet \(1{,}07\cdot10^3\ \mathrm{Mpc}\).'
    b_steg = [steg('Givet och sökt', r'Avståndet är \(d=1{,}07\cdot10^3\ \mathrm{Mpc}\). Sökt: ljusets gångtid \(t\).'),
              steg(r'Avståndet i ljusår, med \(1\ \mathrm{pc}\approx3{,}26\) ljusår', r'\(1{,}07\cdot10^3\ \mathrm{Mpc}=1{,}07\cdot10^9\ \mathrm{pc}\) och \(1{,}07\cdot10^9\cdot3{,}26\approx3{,}49\cdot10^9\).',
                   r'Avståndet är alltså ungefär \(3{,}49\cdot10^9\) ljusår.'),
              steg(r'Sträcka = fart · tid: \(t=d/c\)', 'Ljuset färdas ett ljusår på ett år, så tiden är 3,49 miljarder år.',
                   'Överslaget bortser från att universum har expanderat medan ljuset var på väg.')]
    b_svar = 'Ljuset har varit på väg i ungefär 3,5 miljarder år.'
    c_steg = [steg('Rödförskjutningen kommer från universums expansion',
                   'Medan ljuset färdas mot oss expanderar rummet. Ljusvågorna sträcks ut, så alla spektrallinjer får längre våglängd.',
                   'Ju längre ljuset har färdats i det expanderande rummet, desto större blir rödförskjutningen.')]
    c_svar = RATT_552 + '.'
    u['s'] = ('<div class="facit-v2 facit-stegvis">' + del_facit('a', a_steg, a_svar) + del_facit('b', b_steg, b_svar)
              + del_facit('c', c_steg, c_svar) + '</div>')
    u['ledtrad'] = '<p>Rödförskjutningen ger farten med \\(v=zc\\), och Hubbles lag ger avståndet.</p>'
    u['rättSvar'] = [[74948.1145, 1070.68735], round(t_gar, 2), RATT_552]
    u['tolerans'] = [[749.481145, 10.706873499999999], 0.035, None]
    u['svarEnhet'] = [['km/s', 'Mpc'], 'miljarder år', None]
    u['svarFormat'] = [['numeriskt', 'numeriskt'], 'numeriskt', None]
    u['självrättning'] = [True, True, True]
    u.pop('svarVardesiffror', None)  # index räknas per svarsfält, och del a har två fält

    def kort(fraga, stegen, svar):
        return KVASAR + fraga, ('<div class="facit-v2 facit-stegvis"><div class="facit-arbete"><ol class="facit-steglista" role="list">' + ''.join(stegen)
                                + f'</ol><p class="facit-svar"><strong>Svar:</strong> {svar}</p></div></div>')
    ta, sa = kort('<p>Bestäm farten bort från oss med \\(v=zc\\) och avståndet med Hubbles lag. (Svara med farten i km/s och avståndet i Mpc.)</p>', a_steg, a_svar)
    tb, sb = kort('<p>Avståndet till kvasaren är \\(1{,}07\\cdot10^3\\) Mpc. Ungefär hur länge har ljuset varit på väg, om man räknar med \\(t=d/c\\)? '
                  '(Svara i miljarder år.)</p>', b_steg, b_svar)
    tc, sc = kort('<p>Vad orsakar kvasarens rödförskjutning enligt dagens kosmologi?</p>', c_steg, c_svar)
    u['spelDelar'] = [
        {'etikett': 'a', 't': ta, 's': sa, 'ledtrad': '<p>Använd \\(v=zc\\) först och sedan Hubbles lag \\(v=H_0d\\).</p>', 'niva': 'C', 'poang': '0/1/0',
         'svarsstruktur': 'ordnad', 'svarEtiketter': ['Fart', 'Avstånd']},
        {'etikett': 'b', 't': tb, 's': sb, 'ledtrad': '<p>Räkna om avståndet till ljusår. Ljuset färdas ett ljusår på ett år.</p>', 'niva': 'C', 'poang': '0/1/0'},
        {'etikett': 'c', 't': tc, 's': sc, 'ledtrad': '<p>Tänk på vad som händer med rummet medan ljuset är på väg.</p>', 'niva': 'E', 'poang': '1/0/0',
         'svarstyp': 'alternativ', 'rättSvar': RATT_552, 'självrättning': True, 'svarFormat': None, 'svarEnhet': None, 'tolerans': None,
         'alternativ': ALT_552},
    ]


def fy2_5379(u):
    gammal = 'Figuren visar en stjärnas radialhastighet (hastighet mot eller från oss), mätt med dopplereffekten.'
    if gammal in u['t']:
        u['t'] = u['t'].replace(gammal, 'Figuren visar en stjärnas radialhastighet (hastighet mot eller från oss).')


def fy2_2112(u):
    d = 340 * 6.0e-3 / 2
    assert abs(d - 1.02) < 1e-9
    u['typ'] = 'bestämma avstånd med ekolokalisering, ur text och figur, sökt avstånd'
    u['niva'], u['poang'] = 'C', '(1/1/0)'
    u['rättSvar'], u['tolerans'], u['svarEnhet'], u['svarVardesiffror'] = 1.02, 0.015, 'm', 2
    fig = u['t'][u['t'].index('<span class="fig'):]
    fig = re.sub(r'<line x1="70" y1="132"[^>]*/>', '', fig)
    fig = re.sub(r'<polygon points="120,132[^"]*"[^>]*/>', '', fig)
    fig = fig.replace('insekt (stilla)', 'insekt').replace('Fladdermus som flyger mot en stillasittande insekt.', 'Fladdermus som sänder ultraljud mot en insekt.')
    assert 'y1="132"' not in fig and 'stilla' not in fig
    u['t'] = ('<p>En fladdermus hittar insekter med ekolokalisering. Den sänder ut ett kort ultraljudsskri, och ekot från en insekt kommer '
              'tillbaka till fladdermusen efter 6,0 ms. Ljudets fart i luft är 340 m/s.</p><p>Hur långt från fladdermusen är insekten? (Svara i m.)</p>' + fig)
    u['s'] = facit([steg('Givet och sökt', r'Ljudets fart är \(v=340\ \mathrm{m/s}\). Tiden \(t=6{,}0\ \mathrm{ms}=6{,}0\cdot10^{-3}\ \mathrm s\) gäller vägen till insekten och tillbaka. Sökt: avståndet \(d\).'),
                    steg(r'Ekot går sträckan \(2d\): \(2d=vt\)', r'\[d=\frac{vt}2=\frac{340\cdot6{,}0\cdot10^{-3}}{2}\ \mathrm m=1{,}02\ \mathrm m\]')],
                   r'Insekten är cirka \(1{,}0\ \mathrm m\) från fladdermusen.')
    u['ledtrad'] = '<p>Ekot går både fram till insekten och tillbaka.</p>'


def fy2_5380(u):
    for a in u['alternativ']:
        if a['kommentar'] == 'Stjärnans lilla bana ger dopplerförskjutning i dess spektrum.':
            a['kommentar'] = 'Stjärnans lilla bana gör att den växelvis rör sig mot oss och bort från oss.'


FY2 = {'4.3': fy2_43, '2.112': fy2_2112, '2.114': fy2_2114, '2.115': fy2_2115, '5.52': fy2_552, '5.379': fy2_5379, '5.380': fy2_5380}


# ============================================================================ Ma5

def ma5_4358(u):
    u['typ'] = 'bestämma konstanten i en given lösning och kontrollera genom derivering'
    u['niva'], u['poang'], u['traningsniva'] = 'E', '2/0/0', 2
    u['svarstyp'], u['rättSvar'], u['svarFormat'] = 'uttryck', '4*e^(3*x^2/2)', 'uttryck'
    u['t'] = (r"<p>Differentialekvationen \(y'=3xy\) har lösningar av formen \(y=Ce^{3x^2/2}\), där \(C\) är en konstant.</p>"
              r'<p>Bestäm den lösning som uppfyller \(y(0)=4\). Kontrollera genom derivering att den uppfyller differentialekvationen.</p>')
    u['s'] = facit([steg(r'Sätt in \(x=0\) och \(y=4\) i lösningsformen', r'\[4=Ce^{0}=C\cdot1\quad\Rightarrow\quad C=4\]'),
                    steg(r'Derivera \(y=4e^{3x^2/2}\) med kedjeregeln', r'Den inre funktionen \(\frac32x^2\) har derivatan \(3x\).',
                         r'\[y^{\prime}=4e^{3x^2/2}\cdot3x\]'),
                    steg(r'Jämför med högerledet \(3xy\)', r'\[3xy=3x\cdot4e^{3x^2/2}=y^{\prime}\]', 'Båda leden är lika, så funktionen är en lösning.')],
                   r'\(y=4e^{3x^2/2}\)')
    u['ledtrad'] = r'<p>Sätt in \(x=0\) i lösningsformen. Vad blir \(e^0\)?</p>'


def ma5_2179(u):
    t10 = 20 + 60 * 0.75 ** 10
    u['typ'] = 'beräkna en term med given explicit formel och kontrollera formeln mot rekursionen'
    u['niva'], u['poang'], u['traningsniva'] = 'E', '2/0/0', 2
    u['formaga'] = ['procedur', 'begrepp']
    u['svarstyp'], u['rättSvar'], u['tolerans'], u['svarFormat'] = 'numeriskt', t10, 0, 'numeriskt'
    u['t'] = (r'<p>En talföljd definieras av \(T_0=80\) och</p><p>\[T_{n+1}=0{,}75T_n+5.\]</p>'
              r'<p>Följden kan också beskrivas med den explicita formeln \(T_n=20+60\cdot0{,}75^n\). Beräkna \(T_{10}\).</p>')
    u['s'] = facit([steg('Kontrollera formeln mot rekursionen för de första termerna',
                         r'Rekursionen ger \(T_1=0{,}75\cdot80+5=65\). Formeln ger \(T_0=20+60=80\) och \(T_1=20+60\cdot0{,}75=65\). Värdena stämmer.'),
                    steg(r'Sätt in \(n=10\) i den explicita formeln', r'\[\begin{gathered}T_{10}=20+60\cdot0{,}75^{10}\\=20+60\cdot0{,}0563\ldots\approx23{,}38\end{gathered}\]')],
                   r'\(T_{10}\approx23{,}38\)')
    u['ledtrad'] = r'<p>Med den explicita formeln behöver du inte räkna fram alla tio termerna. Sätt in \(n=10\).</p>'


def ma5_2468(u):
    u['typ'] = 'gränsvärde för talföljd ur given explicit formel'
    u['niva'], u['poang'], u['traningsniva'] = 'E', '2/0/0', 2
    u['svarstyp'], u['rättSvar'], u['tolerans'], u['svarFormat'] = 'numeriskt', 20, 0, 'numeriskt'
    u['t'] = (r'<p>En följd definieras av \(a_0=35\) och \(a_{n+1}=\frac23a_n+\frac{20}3\).</p>'
              r'<p>Det kan visas att \(a_n=20+15\left(\frac23\right)^n\). Vilket värde närmar sig \(a_n\) när \(n\) blir mycket stort?</p>')
    u['s'] = facit([steg('Kontrollera formeln för de första termerna',
                         r'Formeln ger \(a_0=20+15=35\). Rekursionen ger \(a_1=\frac23\cdot35+\frac{20}3=\frac{90}3=30\), och formeln ger \(a_1=20+15\cdot\frac23=30\).'),
                    steg(r'Potensen \(\left(\frac23\right)^n\) går mot 0', r'Eftersom \(0<\frac23<1\) blir \(\left(\frac23\right)^n\) allt mindre när \(n\) växer, till exempel \(\left(\frac23\right)^{20}\approx0{,}0003\).'),
                    steg('Gränsvärdet', r'\[a_n\to20+15\cdot0=20\]')],
                   r'\(a_n\) närmar sig \(20\).')
    u['ledtrad'] = r'<p>Vad händer med \(\left(\frac23\right)^n\) när \(n\) blir stort?</p>'


def ma5_215(u):
    u['typ'] = 'beräkna termer, verifiera given explicit formel för rekursion och bestämma gränsvärde'
    u['t'] = (r'<p>En population beskrivs rekursivt av \(a_0=12000\) och \(a_{n+1}=0{,}78a_n+2400\).</p>'
              r'<p>a) Beräkna \(a_1\) och \(a_2\).</p>'
              r'<p>b) Visa att den explicita formeln \(a_n=\frac{120000}{11}+\frac{12000}{11}\cdot0{,}78^n\) ger rätt startvärde och uppfyller rekursionsformeln.</p>'
              r'<p>c) Vilket värde närmar sig populationen på lång sikt?</p>')
    u['s'] = ('<div class="facit-v2 facit-stegvis">'
              + del_facit('a', [steg('Använd rekursionsformeln två gånger', r'\[a_1=0{,}78\cdot12000+2400=11760\]', r'\[a_2=0{,}78\cdot11760+2400=11572{,}8\]')],
                          r'\(a_1=11760\) och \(a_2\approx11573\).')
              + del_facit('b', [steg(r'Startvärdet: sätt in \(n=0\)', r'\[\frac{120000}{11}+\frac{12000}{11}\cdot1=\frac{132000}{11}=12000=a_0\]'),
                                steg(r'Sätt in formeln i högerledet \(0{,}78a_n+2400\) och skriv \(2400=\frac{26400}{11}\)',
                                     r'Termerna blir \(0{,}78\cdot\frac{120000}{11}=\frac{93600}{11}\) och \(0{,}78\cdot\frac{12000}{11}\cdot0{,}78^n=\frac{12000}{11}\cdot0{,}78^{n+1}\).',
                                     r'\[\frac{93600}{11}+\frac{26400}{11}+\frac{12000}{11}\cdot0{,}78^{n+1}\]',
                                     r'\[=\frac{120000}{11}+\frac{12000}{11}\cdot0{,}78^{n+1}\]'),
                                steg(r'Jämför med formeln för \(a_{n+1}\)', r'\[\frac{120000}{11}+\frac{12000}{11}\cdot0{,}78^{n+1}=a_{n+1}\]',
                                     'Högerledet blir precis formeln för nästa term, så formeln uppfyller rekursionen.')],
                          'Formeln ger rätt startvärde och uppfyller rekursionen.')
              + del_facit('c', [steg(r'\(0{,}78^n\) går mot 0 när \(n\) växer', r'\[a_n\to\frac{120000}{11}\approx10909\]')],
                          'Populationen närmar sig ungefär 10 900 individer.')
              + '</div>')
    u['ledtrad'] = '<p>I b: sätt in formeln för \\(a_n\\) i högerledet och förenkla. Skriv 2400 som ett bråk med nämnaren 11.</p>'


def ma5_256(u):
    u['typ'] = 'hitta explicit formel ur rekursion genom ett givet mönster'
    u['niva'], u['traningsniva'] = 'C', 3
    u['t'] = (r'<p>En talföljd definieras av \(a_1=3\) och</p><p>\[a_{n+1}=2a_n+1.\]</p>'
              r'<p>Beräkna de fyra första termerna och lägg till 1 till varje term. Vilka tal får du? Använd mönstret för att bestämma en explicit formel för \(a_n\).</p>')
    u['s'] = facit([steg('Beräkna de första termerna med rekursionen', r'\(a_1=3\), \(a_2=2\cdot3+1=7\), \(a_3=2\cdot7+1=15\), \(a_4=2\cdot15+1=31\).'),
                    steg('Lägg till 1 till varje term', r'\(4,\ 8,\ 16,\ 32\), alltså \(2^2,\ 2^3,\ 2^4,\ 2^5\). Term nummer \(n\) blir \(2^{n+1}\).'),
                    steg('Skriv den explicita formeln', r'\[a_n+1=2^{n+1}\quad\Rightarrow\quad a_n=2^{n+1}-1\]'),
                    steg('Kontrollera i rekursionen', r'\[2a_n+1=2\left(2^{n+1}-1\right)+1=2^{n+2}-1=a_{n+1}\]')],
                   r'\(a_n=2^{n+1}-1\)')
    u['ledtrad'] = '<p>Vilken känd talföljd får du när du lägger till 1 till termerna?</p>'


def ma5_2180(u):
    u['typ'] = 'hitta explicit formel ur rekursion genom ett givet mönster'
    u['niva'], u['traningsniva'] = 'C', 3
    u['t'] = (r'<p>En talföljd definieras av \(a_1=5\) och \(a_{n+1}=3a_n-4\).</p>'
              r'<p>Beräkna de fyra första termerna och dra bort 2 från varje term. Vilka tal får du? Använd mönstret för att bestämma en explicit formel för \(a_n\).</p>')
    u['s'] = facit([steg('Beräkna de första termerna med rekursionen', r'\(a_1=5\), \(a_2=3\cdot5-4=11\), \(a_3=3\cdot11-4=29\), \(a_4=3\cdot29-4=83\).'),
                    steg('Dra bort 2 från varje term', r'\(3,\ 9,\ 27,\ 81\), alltså \(3^1,\ 3^2,\ 3^3,\ 3^4\). Term nummer \(n\) blir \(3^n\).'),
                    steg('Skriv den explicita formeln', r'\[a_n-2=3^n\quad\Rightarrow\quad a_n=2+3^n\]'),
                    steg('Kontrollera i rekursionen', r'\[3a_n-4=3\left(2+3^n\right)-4=2+3^{n+1}=a_{n+1}\]')],
                   r'\(a_n=2+3^n\)')
    u['ledtrad'] = '<p>Vilken känd talföljd får du när du drar bort 2 från termerna?</p>'


def ma5_2203(u):
    n = next(k for k in range(1, 50) if 50 * (1 - 0.8 ** k) > 45)
    assert n == 11
    u['typ'] = 'använda given explicit formel i dosmodell, sökt antal doser'
    u['niva'], u['traningsniva'] = 'C', 3
    u['svarstyp'], u['rättSvar'], u['tolerans'], u['svarFormat'] = 'numeriskt', n, 0, 'numeriskt'
    u['t'] = (r'<p>En medicinmängd följer rekursionen</p><p>\[M_0=0,\qquad M_{n+1}=0{,}8M_n+10.\]</p>'
              r'<p>Det kan visas att \(M_n=50\left(1-0{,}8^n\right)\). För vilket minsta \(n\) är medicinmängden större än 45?</p>')
    u['s'] = facit([steg('Kontrollera formeln mot rekursionen', r'Rekursionen ger \(M_1=0{,}8\cdot0+10=10\), och formeln ger \(M_1=50(1-0{,}8)=10\).'),
                    steg(r'Ställ upp olikheten \(50\left(1-0{,}8^n\right)>45\)', r'\[1-0{,}8^n>0{,}9\quad\Leftrightarrow\quad0{,}8^n<0{,}1\]'),
                    steg('Lös med logaritmer', r'\[n>\frac{\lg0{,}1}{\lg0{,}8}\approx10{,}3\]',
                         r'Olikheten vänder när man delar med \(\lg0{,}8\), eftersom det talet är negativt.'),
                    steg('Kontrollera med två värden', r'\(M_{10}=50\left(1-0{,}8^{10}\right)\approx44{,}6\) och \(M_{11}=50\left(1-0{,}8^{11}\right)\approx45{,}7\).')],
                   r'\(n=11\)')
    u['ledtrad'] = r'<p>Lös olikheten \(50\left(1-0{,}8^n\right)>45\). Du kan också göra en tabell på räknaren eller i GeoGebra.</p>'


def ma5_2204(u):
    u['typ'] = 'rekursion med gränsvärde och given explicit formel'
    u['niva'], u['traningsniva'] = 'C', 3
    u['rättSvar'], u['svarFormat'] = [12, 12.25], ['numeriskt', 'numeriskt']
    u['svarEtiketter'] = ['gränsvärde', 'a₅']
    bas = r'<p>En talföljd definieras av \(a_0=20\) och</p><p>\[a_{n+1}=0{,}5a_n+6.\]</p>'
    fb = r'Följden kan också skrivas \(a_n=12+8\cdot0{,}5^n\). Beräkna \(a_5\) med formeln.'
    u['t'] = bas + f'<ol type="a"><li>Bestäm följdens gränsvärde.</li><li>{fb}</li></ol>'
    a_steg = [steg('Om följden närmar sig ett gränsvärde \\(L\\) ändras termerna nästan inte längre', r'\[L=0{,}5L+6\quad\Rightarrow\quad0{,}5L=6\quad\Rightarrow\quad L=12\]')]
    b_steg = [steg('Kontrollera formeln mot rekursionen', r'Rekursionen ger \(a_1=0{,}5\cdot20+6=16\), och formeln ger \(a_1=12+8\cdot0{,}5=16\).'),
              steg(r'Sätt in \(n=5\) i formeln', r'\[a_5=12+8\cdot0{,}5^5=12+\frac8{32}=12{,}25\]')]
    u['s'] = '<div class="facit-v2 facit-stegvis">' + del_facit('a', a_steg, 'Gränsvärdet är 12.') + del_facit('b', b_steg, r'\(a_5=12{,}25\)') + '</div>'
    u['ledtrad'] = '<p>I a: om följden har ett gränsvärde L är L = 0,5L + 6. I b: sätt in n = 5 i formeln.</p>'
    for d in u['spelDelar']:
        if d['etikett'] == 'a':
            d['s'] = facit(a_steg, 'Gränsvärdet är 12.')
        else:
            d['t'] = bas + f'<div class="spel-en-del">{fb}</div>'
            d['s'] = facit(b_steg, r'\(a_5=12{,}25\)')
            d['niva'], d['poang'], d['traningsniva'] = 'E', '1/0/0', 2


MA5 = {'4.358': ma5_4358, '2.179': ma5_2179, '2.468': ma5_2468, '2.15': ma5_215, '2.56': ma5_256, '2.180': ma5_2180,
       '2.203': ma5_2203, '2.204': ma5_2204}


def main():
    import json
    src = open('uppgifter2.js', encoding='utf-8').read()
    fam_ids = [u['id'] for u in json.loads(src[src.index('['):src.rindex(']') + 1]) if u.get('omr') == 'ljud_horsel' and u['familj'] in (GAMMAL_FAM, NY_FAM)]
    # Uppgifter som bara byter namn på delmomentet ändras i texten, så att deras egen formatering bevaras (2.301 har
    # blandad formatering som bankpatch inte kan återge).
    for uid in sorted(set(fam_ids) - set(FY2)):
        start, slut, obj, _ = bankpatch.hitta(src, uid)
        bit = src[start:slut]
        if obj['familj'] == GAMMAL_FAM:
            bit = bit.replace(f'"familj": "{GAMMAL_FAM}"', f'"familj": "{NY_FAM}"', 1)
            tid = obj.get('familjTidigare') or []
            ny_tid = [f for f in tid if f != NY_FAM] + [GAMMAL_FAM]
            gammal_txt = json.dumps(tid, ensure_ascii=False, indent=2).replace('\n', '\n    ')
            ny_txt = json.dumps(ny_tid, ensure_ascii=False, indent=2).replace('\n', '\n    ')
            assert bit.count(f'"familjTidigare": {gammal_txt}') == 1, uid
            bit = bit.replace(f'"familjTidigare": {gammal_txt}', f'"familjTidigare": {ny_txt}')
            src = src[:start] + bit + src[slut:]
    json.loads(src[src.index('['):src.rindex(']') + 1])
    with open('uppgifter2.js', 'w', encoding='utf-8', newline='') as fh:
        fh.write(src)
    andr = {}
    for uid in FY2:
        def fn(u, uid=uid):
            if uid in FY2:
                FY2[uid](u)
            byt_familj(u)
        andr[uid] = fn
    bankpatch.andra('uppgifter2.js', andr)
    bankpatch.andra('uppgiftermatf1.js', MA5)
    print('Fy2:', sorted(andr), 'Ma5:', sorted(MA5))


if __name__ == '__main__':
    main()
