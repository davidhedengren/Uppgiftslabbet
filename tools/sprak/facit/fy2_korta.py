# Fy2: alla korta facit (en rad utan facit-rubrik) med steglista enligt FACITMALL (2026-11-22).
# Konstanter ur formelsamlingen: g = 9,82 m/s², c = 3,00·10⁸ m/s, h = 6,626·10⁻³⁴ Js, e = 1,602·10⁻¹⁹ C,
# m_e = 9,109·10⁻³¹ kg, m_p = 1,673·10⁻²⁷ kg, σ = 5,67·10⁻⁸ W/(m²K⁴), Wiens konstant 2,898·10⁻³ mK, I₀ = 10⁻¹² W/m².
VAG = r"Vågekvationen: \(v=f\lambda\)"
FJ_T = r"Svängningstid för fjäder: \(T=2\pi\sqrt{\frac mk}\)"
PEND = r"Svängningstid för pendel: \(T=2\pi\sqrt{\frac lg}\)"
HOOKE = r"Hookes lag: \(F=kx\)"
VMAX = r"Största farten vid harmonisk svängning: \(v_{\max}=\omega A\), med \(\omega=\frac{2\pi}{T}=2\pi f\)"
AMAX = r"Största accelerationen vid harmonisk svängning: \(a_{\max}=\omega^2A\)"
LJUDN = r"Ljudnivå: \(L=10\lg\frac{I}{I_0}\), med \(I_0=10^{-12}\ \mathrm{W/m^2}\)"
DL = r"Ändrad intensitet: \(\Delta L=10\lg\frac{I_2}{I_1}\)"
AVST = r"Intensiteten avtar med avståndet i kvadrat: \(\frac{I_2}{I_1}=\left(\frac{r_1}{r_2}\right)^2\)"
OPPEN = r"Pipa öppen i båda ändar (och sträng): grundtonen har \(l=\frac\lambda2\)"
HALVOPPEN = r"Pipa sluten i ena änden: grundtonen har \(l=\frac\lambda4\)"
CIRK_W = r"Vinkelhastighet: \(\omega=\frac vr\)"
CIRK_A = r"Centripetalacceleration: \(a_c=\omega^2r\)"
CIRK_F = r"Centripetalkraft: \(F=\frac{mv^2}{r}\)"
BIL = r"Kraft på strömförande ledare: \(F=BIl\sin\alpha\)"
RAK = r"Fält kring rak ledare: \(B=\frac{\mu_0I}{2\pi a}\), där \(\frac{\mu_0}{2\pi}=2\cdot10^{-7}\ \mathrm{Tm/A}\)"
QVB = r"Kraft på laddning i magnetfält: \(F=qvB\sin\alpha\)"
EFALT = r"Homogent fält mellan plattor: \(E=\frac Ud\)"
GITTER = r"Gitterformeln: \(d\sin\alpha=k\lambda\)"
SB = r"Stefan–Boltzmanns lag: \(P=e\sigma AT^4\)"
NETTO = r"Nettoutstrålning: \(P=e\sigma A\left(T^4-T_{\text{omg}}^4\right)\)"
WIEN = r"Wiens förskjutningslag: \(\lambda_{\max}T=2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}\)"
FOTON = r"Fotonens energi: \(E=hf=\frac{hc}{\lambda}\)"
SNELL = r"Brytningslagen: \(n_1\sin\alpha_1=n_2\sin\alpha_2\)"
NIND = r"Brytningsindex: \(n=\frac cv\)"
PARA = r"Avstånd ur parallax: \(r=\frac1p\) (r i pc, p i bågsekunder)"
LJUSAR = r"Omvandling: \(1\ \mathrm{pc}=3{,}26\) ljusår"
MAGN = r"Avståndsformeln: \(M=m+5-5\lg r\) (r i pc)"
LUM = r"Magnitud och luminositet: \(\frac{L_1}{L_2}=10^{0{,}4(M_2-M_1)}\)"
HUBBLE = r"Hubbles lag: \(v=H_0d\)"
INDS = r"Inducerad spänning i en stav: \(e=Blv\)"
PYT = r"Pythagoras sats: \(c=\sqrt{a^2+b^2}\)"
HR = 'Läs av i HR-diagrammet'
KELV = 'Temperaturer i kelvin: \\(T=t+273{,}15\\)'


def ett(rubrik, matte, svar, text=None):
    return ([(rubrik, matte, text)] if text else [(rubrik, matte)], svar)


def mc(rubrik, text, svar):
    return ([(rubrik, None, text)], svar)


F = {
    # kast och cirkelrörelse
    '1.118': ([('Givet och sökt', r"v_0=0{,}80\ \mathrm{m/s},\quad a=1{,}6\ \mathrm{m/s^2},\quad s=5{,}00\ \mathrm m",
                'Nedåt räknas som positiv riktning. Sökt: farten v vid ytan.'),
               (r"Tidlösa formeln: \(v^2=v_0^2+2as\)", r"v=\sqrt{0{,}80^2+2\cdot1{,}6\cdot5{,}00}=\sqrt{16{,}64}\approx4{,}1\ \mathrm{m/s}")], "4,1 m/s"),
    '1.124': ([('Stigtiden är halva tiden i luften', r"t_{\text{upp}}=\frac{20{,}0}{2}=10{,}0\ \mathrm s"),
               (r"I högsta punkten är farten 0: \(v=v_0-gt\)", r"0=15{,}0-g\cdot10{,}0\quad\Rightarrow\quad g=1{,}5\ \mathrm{m/s^2}")], "1,5 m/s²"),
    '1.92': ett(CIRK_W, r"\omega=\frac{9{,}0}{0{,}35}\approx26\ \mathrm{rad/s}", "26 rad/s"),
    '1.98': ([('Vinkelhastighet ur frekvensen: \\(\\omega=2\\pi f\\)', r"\omega=2\pi\cdot150\approx942\ \mathrm{rad/s}"),
              (CIRK_A, r"a_c=942{,}5^2\cdot0{,}086\approx7{,}6\cdot10^4\ \mathrm{m/s^2}")], r"\(7{,}6\cdot10^4\) m/s²"),
    '1.100': ([(CIRK_A, r"\omega^2r=6g"), (r"Lös ut \(\omega\)", r"\omega=\sqrt{\frac{6\cdot9{,}82}{11{,}0}}\approx2{,}3\ \mathrm{rad/s}")], "2,3 rad/s"),
    '1.101': ([(CIRK_F, None, r'Massan och radien är desamma, så kraften är proportionell mot \(v^2\).'),
               ('Jämför de två farterna', r"F_2=130\cdot\left(\frac{18{,}0}{14{,}0}\right)^2\approx215\ \mathrm N")], "215 N"),
    # svängningar
    '2.308': ([('Givet och sökt', r"T=2{,}0\ \mathrm s,\quad v_{\max}=40\ \mathrm{cm/s}=0{,}40\ \mathrm{m/s}", 'Sökt: amplituden A.'),
               (VMAX, r"\omega=\frac{2\pi}{2{,}0}=\pi\ \mathrm{rad/s},\qquad A=\frac{v_{\max}}{\omega}=\frac{0{,}40}{\pi}\approx0{,}13\ \mathrm m")], "0,13 m"),
    '2.512': ([('Givet och sökt', r"T=2{,}0\ \mathrm s,\quad v_{\max}=40\ \mathrm{cm/s}=0{,}40\ \mathrm{m/s}", 'Sökt: amplituden A.'),
               (VMAX, r"\omega=\frac{2\pi}{2{,}0}=\pi\ \mathrm{rad/s},\qquad A=\frac{v_{\max}}{\omega}=\frac{0{,}40}{\pi}\approx0{,}13\ \mathrm m")], "0,13 m"),
    '2.465': ett('Under en period går vikten fram och tillbaka: fyra amplituder', r"s=4A=4\cdot0{,}21=0{,}84\ \mathrm m", "0,84 m"),
    '2.468': ett(FJ_T, r"k=\frac{4\pi^2m}{T^2}=\frac{4\pi^2\cdot0{,}200}{2{,}60^2}\approx1{,}17\ \mathrm{N/m}", "1,17 N/m"),
    '2.469': ([('Givet och sökt', r"m=1{,}4\ \mathrm g=0{,}0014\ \mathrm{kg},\quad f=1{,}1\ \mathrm{Hz}", 'Sökt: fjäderkonstanten k.'),
               (FJ_T, r"T=\frac1f\quad\Rightarrow\quad k=4\pi^2f^2m=4\pi^2\cdot1{,}1^2\cdot0{,}0014\approx0{,}067\ \mathrm{N/m}")], "0,067 N/m"),
    '2.470': ett(FJ_T, r"k=\frac{4\pi^2m}{T^2}=\frac{4\pi^2\cdot32}{2{,}0^2}\approx316\ \mathrm{N/m}", "316 N/m"),
    '2.479': ([('Perioden är tiden för en svängning', r"T=\frac{19{,}0}{10}=1{,}90\ \mathrm s"),
               (FJ_T, r"k=\frac{4\pi^2m}{T^2}=\frac{4\pi^2\cdot60}{1{,}90^2}\approx656\ \mathrm{N/m}")], "656 N/m"),
    '2.482': ([(FJ_T, None, r'\(T\) är proportionell mot \(\sqrt m\), så \(\frac{T_2}{T_1}=\sqrt{\frac{m_2}{m_1}}\).'),
               ('Perioden blir 1,20 gånger så lång', r"\frac{m+\Delta m}{m}=1{,}20^2=1{,}44"),
               (r"Lös ut \(\Delta m\)", r"\Delta m=0{,}200\cdot(1{,}44-1)=0{,}088\ \mathrm{kg}")], "0,088 kg"),
    '2.515': ([('Givet och sökt', r"f=0{,}17\ \mathrm{Hz},\quad a_{\max}=0{,}020\cdot9{,}82\approx0{,}196\ \mathrm{m/s^2}", 'Sökt: amplituden A.'),
               (AMAX, r"A=\frac{a_{\max}}{(2\pi f)^2}=\frac{0{,}196}{(2\pi\cdot0{,}17)^2}\approx0{,}17\ \mathrm m")], "0,17 m"),
    '2.516': ([('Givet och sökt', r"A=\frac{8{,}4}{2}\ \mathrm{mm}=4{,}2\ \mathrm{mm},\quad f=\frac{24}{9{,}0}\approx2{,}67\ \mathrm{Hz}",
                'Avståndet mellan vändlägena är två amplituder. Sökt: största farten.'),
               (VMAX, r"v_{\max}=2\pi fA=2\pi\cdot2{,}67\cdot0{,}0042\approx0{,}070\ \mathrm{m/s}")], "0,070 m/s"),
    '2.520': ([(r"Harmonisk svängning: \(a=-\omega^2x\)", r"\omega^2=\frac{5{,}30}{0{,}280}\approx18{,}9\quad\Rightarrow\quad\omega\approx4{,}35\ \mathrm{rad/s}"),
               (r"Frekvensen: \(f=\frac{\omega}{2\pi}\)", r"f=\frac{4{,}35}{2\pi}\approx0{,}692\ \mathrm{Hz}")], "0,692 Hz"),
    '2.536': ([('Givet och sökt', r"m=0{,}400\ \mathrm{kg},\quad k=46{,}0\ \mathrm{N/m},\quad A=3{,}00\ \mathrm m,\quad x=1{,}00\ \mathrm m", 'Sökt: farten v.'),
               (r"Energiprincipen: \(\frac{kA^2}{2}=\frac{kx^2}{2}+\frac{mv^2}{2}\)", r"v=\sqrt{\frac km\left(A^2-x^2\right)}=\sqrt{115\cdot8{,}00}\approx30{,}3\ \mathrm{m/s}")],
              "30,3 m/s"),
    '2.439': ([('Fjädern bär stenens tyngd', r"F=mg=4{,}25\cdot9{,}82\approx41{,}7\ \mathrm N"),
               (HOOKE, r"k=\frac Fx=\frac{41{,}7}{0{,}0262}\approx1{,}59\cdot10^3\ \mathrm{N/m}")], r"\(1{,}59\cdot10^3\) N/m"),
    '2.441': ett(r"Hookes lag med ändringar: \(k=\frac{\Delta F}{\Delta x}\)", r"k=\frac{210-75}{0{,}85-0{,}61}=\frac{135}{0{,}24}\approx563\ \mathrm{N/m}", "cirka 563 N/m"),
    # pendlar
    '2.487': {
        '': ([('a) Perioden är tiden för en hel svängning', r"T=\frac{50}{28}\approx1{,}8\ \mathrm s"),
              (r"b) Frekvensen: \(f=\frac{\text{antal svängningar}}{\text{tid}}\)", r"f=\frac{28}{50}=0{,}56\ \mathrm{Hz}")], "a) 1,8 s b) 0,56 Hz"),
        'a': ([('Perioden är tiden för en hel svängning', r"T=\frac{50}{28}\approx1{,}8\ \mathrm s")], "1,8 s"),
        'b': ([(r"Frekvensen: \(f=\frac{\text{antal svängningar}}{\text{tid}}\)", r"f=\frac{28}{50}=0{,}56\ \mathrm{Hz}")], "0,56 Hz"),
    },
    '2.490': ett(PEND, r"l=\frac{gT^2}{4\pi^2}=\frac{9{,}82\cdot6{,}5^2}{4\pi^2}\approx11\ \mathrm m", "cirka 11 m", 'Linan med karbinhakarna fungerar som en pendel lika lång som väggen.'),
    '2.493': ett(PEND, r"l=\frac{gT^2}{4\pi^2}=\frac{9{,}82\cdot2{,}0^2}{4\pi^2}\approx0{,}99\ \mathrm m", "0,99 m"),
    '2.495': ([(PEND, None, r'Med samma period ger \(g=\frac{4\pi^2l}{T^2}\) att \(g\) är proportionell mot \(l\).'),
               ('Kvoten', r"\frac{g_{\text{Tokyo}}}{g_{\text{Cambridge}}}=\frac{0{,}9927}{0{,}9942}\approx0{,}9985")], "0,9985"),
    '2.496': ett(PEND, r"g=\frac{4\pi^2l}{T^2}=\frac{4\pi^2\cdot2{,}20}{2{,}87^2}\approx10{,}5\ \mathrm{m/s^2}", "10,5 m/s²"),
    '2.500': ([(PEND, None, r'Samma längd ger \(T\) proportionell mot \(\frac{1}{\sqrt g}\).'),
               ('Tyngdaccelerationen är 0,37 gånger så stor', r"T_{\text{Mars}}=\frac{1{,}85}{\sqrt{0{,}37}}\approx3{,}0\ \mathrm s")], "3,0 s"),
    # vågor
    '2.426': ett(VAG, r"\lambda=\frac vf=\frac{340}{60{,}0\cdot10^3}\approx5{,}7\cdot10^{-3}\ \mathrm m", "5,7 mm"),
    '2.427': ([(VAG, r"v=f\lambda=2{,}0\cdot0{,}0850=0{,}17\ \mathrm{m/s}"), ('Tiden till land', r"t=\frac sv=\frac{10}{0{,}17}\approx59\ \mathrm s")], "59 s"),
    '2.430': ([('Båtens längd är en våglängd och tiden mellan två toppar en period', r"\lambda=7{,}0\ \mathrm m,\quad T=3{,}0\ \mathrm s"),
               (r"Vågekvationen: \(v=\frac\lambda T\)", r"v=\frac{7{,}0}{3{,}0}\approx2{,}3\ \mathrm{m/s}")], "2,3 m/s"),
    '2.431': ett(VAG, r"\lambda=\frac vf=\frac{343}{282}\approx1{,}22\ \mathrm m", "1,22 m", 'Avståndet mellan två förtätningar är en våglängd.'),
    '2.434': ett(VAG, r"f=\frac v\lambda=\frac{1\,500}{1{,}0\cdot10^{-3}}=1{,}5\cdot10^6\ \mathrm{Hz}", r"\(1{,}5\cdot10^6\) Hz"),
    '2.394': ([(OPPEN, r"\lambda=\frac vf=\frac{293}{440}"), ('Strängens längd', r"l=\frac\lambda2=\frac{293}{2\cdot440}\approx0{,}333\ \mathrm m")], "0,333 m"),
    '2.395': {
        '': ([(f'a) {OPPEN}', r"\lambda=2l=2\cdot0{,}42=0{,}84\ \mathrm m"), (f'b) {VAG}', r"v=175\cdot0{,}84=147\ \mathrm{m/s}")],
             "a) 0,84 m b) 147 m/s"),
        'a': ([(OPPEN, r"\lambda=2l=2\cdot0{,}42=0{,}84\ \mathrm m")], "0,84 m"),
        'b': ([(VAG, r"v=175\cdot0{,}84=147\ \mathrm{m/s}")], "147 m/s"),
    },
    '2.409': ([(r"Våghastighet i sträng: \(v=\sqrt{\frac{F}{\mu}}\)", None, r'Samma kraft och längd: halva massan ger halva \(\mu\), så farten blir \(\sqrt2\) gånger större.'),
               ('Sätt in', r"v=5{,}00\cdot\sqrt2\approx7{,}07\ \mathrm{m/s}")], "7,07 m/s"),
    '2.368': ([(OPPEN, r"\lambda=2\cdot1{,}36=2{,}72\ \mathrm m"), (VAG, r"f=\frac v\lambda=\frac{338}{2{,}72}\approx124\ \mathrm{Hz}")], "124 Hz"),
    '2.372': ([(OPPEN, r"l=\frac{\lambda}{2}=\frac{v}{2f}"), ('Sätt in ljudfarten i luft, cirka 340 m/s', r"l=\frac{340}{2\cdot520}\approx0{,}33\ \mathrm m"),
               ('Kontrollera mot intervallet', None, '0,33 m ligger mellan 20 och 90 cm.')], "0,33 m"),
    '2.373': ([(HALVOPPEN, r"l=\frac\lambda4=\frac{v}{4f}"), ('Sätt in ljudfarten i luft, cirka 340 m/s', r"l=\frac{340}{4\cdot352}\approx0{,}241\ \mathrm m")], "0,241 m"),
    '2.375': ([(OPPEN, r"l=\frac{v}{2f}"), ('Sätt in ljudfarten i luft, cirka 340 m/s', r"l=\frac{340}{2\cdot40\cdot10^3}\approx4{,}3\cdot10^{-3}\ \mathrm m")], "4,3 mm"),
    '2.377': ([('Ljudfarten vid de två temperaturerna', r"v_0=331\ \mathrm{m/s},\qquad v_{20}=331+0{,}6\cdot20{,}0=343\ \mathrm{m/s}"),
               (f'{OPPEN}, så \\(f=\\frac{{v}}{{2l}}\\) är proportionell mot \\(v\\)', r"f=382\cdot\frac{343}{331}\approx396\ \mathrm{Hz}")], "396 Hz"),
    '2.381': ([(OPPEN, r"l=\frac{v}{2f}"), ('Sätt in ljudfarten i luft, cirka 340 m/s', r"l=\frac{340}{2\cdot130{,}8}\approx1{,}30\ \mathrm m")], "1,30 m"),
    '2.382': ([(HALVOPPEN, r"\lambda=4l=4\cdot0{,}028=0{,}112\ \mathrm m"), (VAG, r"f=\frac{340}{0{,}112}\approx3{,}0\cdot10^3\ \mathrm{Hz}")], "cirka 3,0 kHz"),
    # ljudnivå
    '2.319': ett(LJUDN, r"I=I_0\cdot10^{L/10}=10^{-12}\cdot10^{12}=1{,}0\ \mathrm{W/m^2}", "1,0 W/m²"),
    '2.320': ett(LJUDN, r"L=10\lg\frac{1{,}5\cdot10^{-6}}{10^{-12}}=10\lg(1{,}5\cdot10^6)\approx62\ \mathrm{dB}", "62 dB"),
    '2.332': ett(DL, r"\frac{I_1}{I_2}=10^{(95{,}0-70{,}0)/10}=10^{2{,}5}\approx316", "316 gånger"),
    '2.336': ett(DL, r"L=98{,}0+10\lg8\approx98{,}0+9{,}0=107\ \mathrm{dB}", "107 dB", 'Åtta lika starka bilar ger åtta gånger så stor intensitet.'),
    '2.337': ett(DL, r"L=85-10\lg2\approx85-3=82\ \mathrm{dB}", "82 dB", 'En smällare ger halva intensiteten.'),
    '2.341': ett(DL, r"L=140-10\lg4\approx140-6=134\ \mathrm{dB}", "134 dB", 'En motor av fyra ger en fjärdedel av intensiteten.'),
    '2.343': ([(AVST, r"\frac{I_2}{I_1}=\left(\frac{5{,}0}{10\,000}\right)^2"),
               (DL, r"\Delta L=10\lg\left(\frac{5{,}0}{10\,000}\right)^2=20\lg(5{,}0\cdot10^{-4})\approx-66\ \mathrm{dB}"),
               ('Ny ljudnivå', r"L=103-66=37\ \mathrm{dB}")], "37 dB"),
    '2.345': ([(AVST, None, 'Pappan är 1,50/0,30 = 5 gånger längre bort.'), (DL, r"\Delta L=10\lg5^2=20\lg5\approx14\ \mathrm{dB}")], "14 dB"),
    '2.346': ([(DL, r"109-90=10\lg N"), ('Lös ut antalet personer', r"N=10^{1{,}9}\approx79")], "ungefär 80 personer"),
    # magnetism och elektriska fält
    '3.366': ett(RAK, r"B=\frac{2\cdot10^{-7}\cdot65}{0{,}045}\approx2{,}9\cdot10^{-4}\ \mathrm T", r"\(2{,}9\cdot10^{-4}\) T"),
    '3.370': ett(RAK, r"B=\frac{2\cdot10^{-7}\cdot10{,}0\cdot10^3}{100}=2{,}0\cdot10^{-5}\ \mathrm T", r"\(2{,}0\cdot10^{-5}\) T"),
    '3.381': ett(r"Platt spole: \(B=\frac{\mu_0NI}{2r}\)", r"B=\frac{4\pi\cdot10^{-7}\cdot40\cdot1{,}5}{2\cdot0{,}25}\approx1{,}5\cdot10^{-4}\ \mathrm T", r"\(1{,}5\cdot10^{-4}\) T"),
    '3.357': ett(BIL, r"F=0{,}040\cdot3{,}5\cdot0{,}040=5{,}6\cdot10^{-3}\ \mathrm N", r"\(5{,}6\cdot10^{-3}\) N", 'Ledaren är vinkelrät mot fältet, så sin α = 1.'),
    '3.360': ett(BIL, r"F=51\cdot10^{-6}\cdot120\cdot240\cdot\sin68^\circ\approx1{,}4\ \mathrm N", "1,4 N"),
    '3.462': ett(BIL, r"B=\frac{F}{Il}=\frac{0{,}12}{3{,}0\cdot0{,}40}=0{,}10\ \mathrm T", "0,10 T"),
    '3.463': ett(BIL, r"I=\frac{F}{Bl}=\frac{0{,}060}{0{,}30\cdot0{,}10}=2{,}0\ \mathrm A", "2,0 A"),
    '3.475': mc('Högerhandsregeln: tummen i strömmens riktning, fingrarna visar fältet', 'Tummen pekar in i pappret, och då böjer sig fingrarna medurs.', "Medurs"),
    '3.510': ett(PYT, r"B=\sqrt{18^2+48^2}\approx51\ \mathrm{\mu T}", "cirka 51 µT", 'Den vågräta och den lodräta komponenten är vinkelräta.'),
    '3.347': ett(EFALT, r"E=\frac{25\cdot10^3}{0{,}050}=5{,}0\cdot10^5\ \mathrm{V/m}", r"\(5{,}0\cdot10^5\) V/m"),
    '3.348': ett(EFALT, r"d=\frac UE=\frac{720}{80\cdot10^3}=9{,}0\cdot10^{-3}\ \mathrm m", "9,0 mm"),
    '3.349': ett(EFALT, r"U=Ed=3{,}0\cdot10^6\cdot1\,500=4{,}5\cdot10^9\ \mathrm V", r"\(4{,}5\cdot10^9\) V"),
    '3.316': ett(QVB, r"v=\frac{F}{eB\sin37^\circ}=\frac{3{,}5\cdot10^{-15}}{1{,}602\cdot10^{-19}\cdot2{,}5\cdot10^{-3}\cdot\sin37^\circ}\approx1{,}5\cdot10^7\ \mathrm{m/s}",
                 r"\(1{,}5\cdot10^7\) m/s"),
    '3.323': ([('Givet och sökt', r"E_k=55\ \mathrm{keV}=55\cdot10^3\cdot1{,}602\cdot10^{-19}\ \mathrm J\approx8{,}81\cdot10^{-15}\ \mathrm J,\quad B=0{,}35\ \mathrm T",
                'Sökt: banradien r.'),
               (r"Rörelseenergi: \(E_k=\frac{mv^2}{2}\)", r"v=\sqrt{\frac{2E_k}{m_p}}=\sqrt{\frac{2\cdot8{,}81\cdot10^{-15}}{1{,}673\cdot10^{-27}}}\approx3{,}25\cdot10^6\ \mathrm{m/s}"),
               (r"Banradie i magnetfält: \(r=\frac{mv}{qB}\)", r"r=\frac{1{,}673\cdot10^{-27}\cdot3{,}25\cdot10^6}{1{,}602\cdot10^{-19}\cdot0{,}35}\approx0{,}097\ \mathrm m")], "0,097 m"),
    '3.334': ([(r"Omloppstid i magnetfält: \(T=\frac{2\pi m}{qB}\)", r"T=\frac{2\pi\cdot6{,}64\cdot10^{-27}}{2\cdot1{,}602\cdot10^{-19}\cdot0{,}050}\approx2{,}60\cdot10^{-6}\ \mathrm s"),
               ('Böjning 90° är en fjärdedels varv', r"t=\frac T4\approx6{,}5\cdot10^{-7}\ \mathrm s")], r"\(6{,}5\cdot10^{-7}\) s"),
    '3.411': ett(r"Toppvärdet hos en generator: \(\hat e=NBA\omega\), med \(\omega=2\pi f\)",
                 r"B=\frac{\hat e}{NA\cdot2\pi f}=\frac{5\,500}{150\cdot0{,}85\cdot2\pi\cdot60{,}0}\approx0{,}11\ \mathrm T", "0,11 T"),
    '3.415': ett(INDS, r"e=0{,}20\cdot0{,}50\cdot3{,}0=0{,}30\ \mathrm V", "0,30 V", 'Läs av B, stavens längd l och farten v i figuren.'),
    '3.506': mc('Läs av i grafen', 'Vid farten 4,0 m/s ligger linjen vid 0,8 V.', "0,8 V"),
    # interferens och optik
    '2.601': ett(PYT, r"r_1=\sqrt{12^2+5{,}0^2}=\sqrt{169}=13\ \mathrm{cm}", "13 cm"),
    '2.602': ett(PYT, r"r=\sqrt{60^2+80^2}=\sqrt{10\,000}=100\ \mathrm m", "100 m"),
    '2.608': ett(r"Första minimum: vägskillnaden är \(\Delta s=\frac\lambda2\)", r"\lambda=2\cdot0{,}34=0{,}68\ \mathrm m", "0,68 m"),
    '4.422': ett(GITTER, r"d=\frac{\lambda}{\sin20{,}5^\circ}=\frac{632{,}8\cdot10^{-9}}{\sin20{,}5^\circ}\approx1{,}81\cdot10^{-6}\ \mathrm m", "1,81 µm"),
    '4.429': ([(GITTER, None, r'Samma \(d\) och \(\lambda\) ger \(\sin\alpha_3=3\sin\alpha_1\).'),
               ('Sätt in', r"\sin\alpha_3=3\sin18{,}0^\circ\approx0{,}927\quad\Rightarrow\quad\alpha_3\approx68{,}0^\circ")], r"\(68{,}0^\circ\)"),
    '4.431': ett(GITTER, r"\sin\alpha=\frac{\lambda}{20\lambda}=0{,}050\quad\Rightarrow\quad\alpha\approx2{,}9^\circ", r"\(2{,}9^\circ\)"),
    '4.435': ([('Givet och sökt', r"d=1{,}35\cdot10^{-3}\ \mathrm{cm}=1{,}35\cdot10^{-5}\ \mathrm m,\quad\lambda=510\ \mathrm{nm},\quad k=2", 'Sökt: vinkeln α.'),
               (GITTER, r"\sin\alpha=\frac{2\cdot510\cdot10^{-9}}{1{,}35\cdot10^{-5}}\approx0{,}0756\quad\Rightarrow\quad\alpha\approx4{,}33^\circ")], r"\(4{,}33^\circ\)"),
    '4.437': ([('Gitterkonstanten ur ritsor per millimeter', r"d=\frac{1}{380}\ \mathrm{mm}\approx2{,}63\cdot10^{-6}\ \mathrm m"),
               (GITTER, r"\lambda=\frac{d\sin22{,}0^\circ}{2}=\frac{2{,}63\cdot10^{-6}\cdot\sin22{,}0^\circ}{2}\approx493\ \mathrm{nm}")], "493 nm"),
    '4.372': ([(NIND, r"v=\frac cn=\frac{3{,}00\cdot10^8}{1{,}33}"), ('Tiden', r"t=\frac sv=\frac{1{,}33\cdot150}{3{,}00\cdot10^8}\approx6{,}65\cdot10^{-7}\ \mathrm s")], "0,665 µs"),
    '4.375': ([('Frekvensen ändras inte när ljuset byter medium', None, r'Då är våglängden proportionell mot farten, \(\lambda=\frac vf\).'),
               ('Sätt in', r"\lambda=592\cdot\frac{2{,}25\cdot10^8}{3{,}00\cdot10^8}=444\ \mathrm{nm}")], "444 nm"),
    '4.387': ett(SNELL, r"n_2=\frac{1{,}45\sin64{,}0^\circ}{\sin53{,}0^\circ}\approx1{,}63", "1,63"),
    '4.391': ett(SNELL, r"n=\frac{\sin63{,}0^\circ}{\sin47{,}0^\circ}\approx1{,}22", "1,22", 'Luften har brytningsindex 1,00.'),
    '4.411': ([(r"Totalreflexion: \(\sin\alpha\ge\frac{n_2}{n_1}\)", None, 'Strålen totalreflekteras om infallsvinkeln är minst gränsvinkeln.'),
               ('Lös ut det största brytningsindexet', r"n_2\le1{,}50\sin58{,}0^\circ\approx1{,}27")], "1,27"),
    # elektromagnetiska vågor och temperaturstrålning
    '4.449': ett(r"Vågekvationen för ljus: \(c=f\lambda\)", r"f=\frac c\lambda=\frac{3{,}00\cdot10^8}{545\cdot10^{-9}}\approx5{,}50\cdot10^{14}\ \mathrm{Hz}", r"\(5{,}50\cdot10^{14}\) Hz"),
    '4.496': ett(r"Vågekvationen för ljus: \(c=f\lambda\)", r"\frac\lambda2=\frac{3{,}00\cdot10^8}{2\cdot2{,}0\cdot10^9}=0{,}075\ \mathrm m", "0,075 m"),
    '4.497': ett(r"Radiovågor går med ljusfarten: \(t=\frac sc\)", r"t=\frac{2{,}28\cdot10^{11}}{3{,}00\cdot10^8}=760\ \mathrm s", "760 s (cirka 12,7 min)"),
    '4.450': ([(KELV, r"T=0+273{,}15=273{,}15\ \mathrm K"), (SB, r"P=5{,}67\cdot10^{-8}\cdot1{,}0\cdot273{,}15^4\approx316\ \mathrm W")], "316 W"),
    '4.451': ([('Givet och sökt', r"r=0{,}060\ \mathrm m,\quad T=600+273{,}15=873{,}15\ \mathrm K", 'Sökt: utstrålad effekt P.'),
               ('Klotets area: \\(A=4\\pi r^2\\)', r"A=4\pi\cdot0{,}060^2\approx0{,}0452\ \mathrm{m^2}"),
               (SB, r"P=5{,}67\cdot10^{-8}\cdot0{,}0452\cdot873{,}15^4\approx1{,}49\cdot10^3\ \mathrm W")], "1,49 kW"),
    '4.453': ([('Givet och sökt', r"A=238\ \mathrm{cm^2}=0{,}0238\ \mathrm{m^2},\quad T=373{,}15\ \mathrm K,\quad T_{\text{omg}}=293{,}15\ \mathrm K", 'Sökt: nettoenergin på 60 s.'),
               (NETTO, r"P=5{,}67\cdot10^{-8}\cdot0{,}0238\cdot\left(373{,}15^4-293{,}15^4\right)\approx16{,}2\ \mathrm W"),
               (r"Energi: \(E=Pt\)", r"E=16{,}2\cdot60\approx972\ \mathrm J")], "972 J"),
    '4.455': ([('Givet och sökt', r"d=0{,}020\ \mathrm m,\quad T=62+273{,}15=335{,}15\ \mathrm K,\quad T_{\text{omg}}=295{,}15\ \mathrm K,\quad e=0{,}12",
                'Sökt: förlusten per meter rör. Mantelarean för 1 m rör är \\(\\pi d\\cdot1\\).'),
               (NETTO, r"\frac Pl=0{,}12\cdot5{,}67\cdot10^{-8}\cdot\pi\cdot0{,}020\cdot\left(335{,}15^4-295{,}15^4\right)\approx2{,}1\ \mathrm W")], "2,1 W per meter"),
    '4.458': ([(KELV, r"T=240+273{,}15=513{,}15\ \mathrm K"), (SB, r"P=0{,}74\cdot5{,}67\cdot10^{-8}\cdot0{,}60\cdot513{,}15^4\approx1{,}75\cdot10^3\ \mathrm W")], "1,75 kW"),
    '4.459': ([(KELV, r"T_1=373{,}15\ \mathrm K,\quad T_2=673{,}15\ \mathrm K,\quad T_{\text{omg}}=293{,}15\ \mathrm K"),
               (NETTO, r"\frac{P_2}{P_1}=\frac{673{,}15^4-293{,}15^4}{373{,}15^4-293{,}15^4}\approx16{,}5")], "16,5 gånger"),
    '4.462': ([('Cylinderns mantelarea: \\(A=\\pi dl\\)', r"A=\pi\cdot0{,}015\cdot0{,}25\approx0{,}0118\ \mathrm{m^2}"),
               (SB, r"T=\sqrt[4]{\frac{P}{\sigma A}}=\sqrt[4]{\frac{1\,000}{5{,}67\cdot10^{-8}\cdot0{,}0118}}\approx1\,106\ \mathrm K"),
               ('Omvandla till grader Celsius', r"1\,106-273\approx833\ ^\circ\mathrm C")], "833 °C"),
    '4.463': ([(KELV, r"T=303{,}15\ \mathrm K,\quad T_{\text{omg}}=288{,}15\ \mathrm K"),
               (NETTO, r"P=0{,}900\cdot5{,}67\cdot10^{-8}\cdot275\cdot\left(303{,}15^4-288{,}15^4\right)\approx2{,}18\cdot10^4\ \mathrm W")], "21,8 kW"),
    '4.464': ([(KELV, r"T=1\,123{,}15\ \mathrm K,\quad T_{\text{omg}}=291{,}15\ \mathrm K"),
               (NETTO, r"P=0{,}980\cdot5{,}67\cdot10^{-8}\cdot0{,}200\cdot\left(1\,123{,}15^4-291{,}15^4\right)\approx1{,}76\cdot10^4\ \mathrm W")], "17,6 kW"),
    '4.465': ([(KELV, r"T=383{,}15\ \mathrm K,\quad T_{\text{omg}}=323{,}15\ \mathrm K"),
               (NETTO, r"P=0{,}750\cdot5{,}67\cdot10^{-8}\cdot1{,}20\cdot\left(383{,}15^4-323{,}15^4\right)\approx543\ \mathrm W")], "543 W"),
    '4.466': ([(KELV, r"T=283{,}15\ \mathrm K,\quad T_{\text{omg}}=258{,}15\ \mathrm K"),
               (NETTO, r"P=0{,}200\cdot5{,}67\cdot10^{-8}\cdot1{,}60\cdot\left(283{,}15^4-258{,}15^4\right)\approx36{,}0\ \mathrm W")], "36,0 W"),
    '4.467': ([(KELV, r"T_{\text{bastu}}=323{,}15\ \mathrm K,\quad T_{\text{hud}}=308{,}15\ \mathrm K"),
               (NETTO, r"P=0{,}98\cdot5{,}67\cdot10^{-8}\cdot1{,}50\cdot\left(323{,}15^4-308{,}15^4\right)\approx157\ \mathrm W",
                'Bastun är varmare än huden, så nettoströmmen går in mot kroppen.')], "157 W"),
    '4.469': ([(KELV, r"T=306{,}15\ \mathrm K,\quad T_{\text{omg}}=295{,}15\ \mathrm K"),
               (NETTO, r"P=0{,}97\cdot5{,}67\cdot10^{-8}\cdot1{,}50\cdot\left(306{,}15^4-295{,}15^4\right)\approx99\ \mathrm W")], "99 W"),
    '4.475': ett(WIEN, r"T=\frac{2{,}898\cdot10^{-3}}{750\cdot10^{-9}}\approx3\,864\ \mathrm K", "3 864 K"),
    '4.476': ([(KELV, r"T=850+273{,}15=1\,123{,}15\ \mathrm K"), (WIEN, r"\lambda_{\max}=\frac{2{,}898\cdot10^{-3}}{1\,123{,}15}\approx2{,}6\cdot10^{-6}\ \mathrm m")],
              r"\(2{,}6\cdot10^{-6}\) m"),
    # ljus som partiklar och materievågor
    '4.361': ([(r"Utträdesarbetet: \(E_0=hf_0\)", r"E_0=6{,}626\cdot10^{-34}\cdot1{,}04\cdot10^{15}\approx6{,}89\cdot10^{-19}\ \mathrm J"),
               ('Omvandla till elektronvolt', r"\frac{6{,}89\cdot10^{-19}}{1{,}602\cdot10^{-19}}\approx4{,}30\ \mathrm{eV}")], "4,30 eV"),
    '4.478': ett(FOTON, r"\lambda=\frac{hc}{E}=\frac{6{,}626\cdot10^{-34}\cdot3{,}00\cdot10^8}{6{,}4\cdot10^{-19}}\approx3{,}1\cdot10^{-7}\ \mathrm m", r"\(3{,}1\cdot10^{-7}\) m"),
    '4.480': ([(FOTON, r"E=\frac{6{,}626\cdot10^{-34}\cdot3{,}00\cdot10^8}{730\cdot10^{-9}}\approx2{,}72\cdot10^{-19}\ \mathrm J"),
               ('Antal fotoner per sekund och kvadratmeter', r"N=\frac{680}{2{,}72\cdot10^{-19}}\approx2{,}5\cdot10^{21}")], r"\(2{,}5\cdot10^{21}\)"),
    '4.485': ett(FOTON, r"\frac{hf_{FM}}{hf_{AM}}=\frac{91{,}9\cdot10^6}{665\cdot10^3}\approx138", "138"),
    '4.490': ([(r"Energi i en puls: \(E=Pt\)", r"E=0{,}68\cdot0{,}025=0{,}017\ \mathrm J"),
               (FOTON, r"E_f=\frac{6{,}626\cdot10^{-34}\cdot3{,}00\cdot10^8}{640\cdot10^{-9}}\approx3{,}11\cdot10^{-19}\ \mathrm J"),
               ('Antal fotoner', r"N=\frac{0{,}017}{3{,}11\cdot10^{-19}}\approx5{,}5\cdot10^{16}")], r"\(5{,}5\cdot10^{16}\)"),
    '4.491': ([('40 % av energin når näthinnan', r"E=0{,}40\cdot4{,}0\cdot10^{-17}=1{,}6\cdot10^{-17}\ \mathrm J"),
               (FOTON, r"E_f=\frac{6{,}626\cdot10^{-34}\cdot3{,}00\cdot10^8}{510\cdot10^{-9}}\approx3{,}90\cdot10^{-19}\ \mathrm J"),
               ('Antal fotoner', r"N=\frac{1{,}6\cdot10^{-17}}{3{,}90\cdot10^{-19}}\approx41")], "41 fotoner"),
    '4.492': ([(FOTON, r"E_f=\frac{6{,}626\cdot10^{-34}\cdot3{,}00\cdot10^8}{460\cdot10^{-9}}\approx4{,}32\cdot10^{-19}\ \mathrm J"),
               (r"Effekt: \(P=\frac Et\)", r"P=\frac{1{,}0\cdot10^8\cdot4{,}32\cdot10^{-19}}{0{,}10}\approx4{,}3\cdot10^{-10}\ \mathrm W")], r"\(4{,}3\cdot10^{-10}\) W"),
    '4.495': ([(FOTON, r"E=\frac{6{,}626\cdot10^{-34}\cdot3{,}00\cdot10^8}{0{,}25\cdot10^{-9}}\approx7{,}95\cdot10^{-16}\ \mathrm J"),
               ('Omvandla till elektronvolt', r"\frac{7{,}95\cdot10^{-16}}{1{,}602\cdot10^{-19}}\approx4{,}96\cdot10^3\ \mathrm{eV}")], "cirka 4 960 eV (4,96 keV)"),
    '4.501': ett(r"de Broglie-våglängd: \(\lambda=\frac hp=\frac{h}{mv}\)",
                 r"\lambda=\frac{6{,}626\cdot10^{-34}}{9{,}109\cdot10^{-31}\cdot4{,}0\cdot10^6}\approx1{,}8\cdot10^{-10}\ \mathrm m", r"\(1{,}8\cdot10^{-10}\) m"),
    # astronomi
    '5.346': ([(PARA, r"r=\frac{1}{0{,}54831}\approx1{,}824\ \mathrm{pc}"), (LJUSAR, r"1{,}824\cdot3{,}264\approx5{,}953\ \text{ljusår}")], "5,953 ljusår"),
    '5.347': ([(PARA, r"r=\frac{1}{0{,}07943}\approx12{,}59\ \mathrm{pc}"), (LJUSAR, r"12{,}59\cdot3{,}264\approx41{,}09\ \text{ljusår}")], "41,09 ljusår"),
    '5.348': ([(LJUSAR, r"r=\frac{10{,}8}{3{,}264}\approx3{,}31\ \mathrm{pc}"), (PARA, r"p=\frac1r=\frac{1}{3{,}31}\approx0{,}302''")], "0,302″"),
    '5.431': ett(PARA, r"r=\frac{1}{0{,}50}=2{,}0\ \mathrm{pc}", "2,0 pc"),
    '5.432': ett(PARA, r"p=\frac{1}{20}=0{,}050''", "0,050″"),
    '5.441': ett(PARA, r"r=\frac{1}{0{,}0025}=400\ \mathrm{pc}", "400 pc"),
    '5.353': ([(MAGN, r"-7{,}0=0{,}1+5-5\lg r"), (r"Lös ut \(\lg r\)", r"\lg r=\frac{0{,}1+7{,}0+5}{5}=2{,}42\quad\Rightarrow\quad r=10^{2{,}42}\approx263\ \mathrm{pc}")], "263 pc"),
    '5.354': ([(PARA, r"r=\frac{1}{0{,}760}\approx1{,}316\ \mathrm{pc}"), (MAGN, r"M=-0{,}27+5-5\lg1{,}316\approx4{,}13")], "4,13"),
    '5.425': ett(MAGN, r"M=7{,}0+5-5\lg40\approx4{,}0", "cirka 4,0"),
    '5.359': ett(LUM, r"\frac{L_1}{L_2}=10^{0{,}4\cdot3{,}83}\approx34", "cirka 34 gånger"),
    '5.427': ett(LUM, r"\frac{L_1}{L_2}=10^{0{,}4\cdot2{,}5}=10^1=10", "10 gånger"),
    '5.419': mc('Lägre magnitud betyder ljusare', 'Sirius har lägst apparent magnitud i tabellen.', "Sirius"),
    '5.424': mc('Större magnitud betyder svagare ljus', '+8 är svagare än gränsen +6.', "Nej"),
    '5.332': ett(HUBBLE, r"v=70\cdot16{,}5\approx1\,160\ \mathrm{km/s}", "cirka 1 200 km/s"),
    '5.333': ett(HUBBLE, r"v=70\cdot100=7\,000\ \mathrm{km/s}", "7 000 km/s"),
    '5.310': mc('Mycket massiva stjärnor slutar i en supernova', 'Kärnan kollapsar och de yttre lagren slungas ut. Kvar blir en neutronstjärna eller ett svart hål.', "Supernova"),
    '5.311': mc('HR-diagrammets temperaturaxel är omvänd', 'De hetaste stjärnorna står till vänster.', "Åt vänster"),
    '5.321': mc('Tiden mellan två likadana transiter är en omloppstid', 'Planeten passerar framför stjärnan en gång per varv.', "18 dygn"),
    '5.377': ett('Tiden mellan två likadana transiter är en omloppstid', r"T=12{,}5-3{,}0=9{,}5\ \text{dygn}", "9,5 dygn", 'Läs av två dippar i figuren.'),
    '5.400': mc(HR, 'A ligger på linjen för −5 på den lodräta axeln.', r"\(M=-5\)"),
    '5.402': mc(HR, 'Temperaturen är högst längst till vänster. A ligger vid 20 000 K.', "A"),
    '5.406': mc(HR, 'C ligger vid 4 000 K, under bandet märkt K.', "K"),
    '5.407': mc('Svala stjärnor strålar mest vid långa våglängder', 'En stjärna på 3 500 K ser rödaktig ut.', "Rödaktig"),
    '5.409': mc(HR, 'P ligger på linjen för 100.', "100 gånger"),
    '5.414': mc(HR, 'Rigel ligger en bit ovanför linjen för −5, ungefär vid −8.', "cirka −8"),
    '5.416': mc(HR, 'Aldebaran ligger strax till höger om 4 000 K.', "cirka 3 900 K"),
}
