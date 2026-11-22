# Fy1: alla korta facit (en rad utan facit-rubrik) med steglista enligt FACITMALL (2026-11-22).
# Enstegsuppgifter har formelsteget och svarsraden (FACITMALL avsnitt 6).
P = r"Rörelsemängd: \(p=mv\)"
IMP = r"Impuls: \(I=F\cdot\Delta t\)"
IMPP = r"Impulslagen: \(I=\Delta p=m\Delta v\)"
TRYCK = r"Tryck: \(p=\frac FA\)"
ARK = r"Arkimedes princip: \(F_L=\rho_{\text{vätska}}\cdot V\cdot g\)"
GAS = r"Allmänna gaslagen: \(pV=nRT\)"
HALV = r"Sönderfallslagen: \(A=A_0\cdot\left(\frac12\right)^{t/T_{1/2}}\)"
AKT = r"Aktivitet = sönderfall per sekund: \(N=A\cdot t\)"
DOS = r"Ekvivalent dos: \(H=w_R\cdot D\)"
DOSR = r"Dos = dos per timme gånger tiden: \(H=\dot H\cdot t\)"
NUK = r"Nuklidbeteckning \({}^A_Z\mathrm X\): masstalet är \(A=Z+N\)"
NEUT = r"Antal neutroner: \(N=A-Z\)"
BEV = 'Masstalet och atomnumret bevaras i en kärnreaktion'
EMC = r"Energi ur massminskning: \(E=\Delta m\cdot931{,}5\ \mathrm{MeV/u}\)"
HT = r"Halveringstjocklek: andelen som passerar är \(\left(\frac12\right)^{n}\), där \(n=\frac{x}{x_{1/2}}\)"
KVARK = r"Kvarkarnas laddning: \(u=+\frac23e\), \(d=-\frac13e\); en antikvark har motsatt tecken"
BIND = r"Bindningsenergi: \(E_b=A\cdot\frac{E_b}{A}\)"
MDEF = r"Massdefekt ur bindningsenergi: \(\Delta m=\frac{E_b}{931{,}5\ \mathrm{MeV/u}}\)"
ALFA = r"Alfasönderfall: en \({}^4_2\mathrm{He}\)-kärna lämnar, så \(A\) minskar med 4 och \(Z\) med 2"
BETAM = r"Beta-minus: en neutron blir en proton, så \(Z\) ökar med 1 och \(A\) är oförändrat"
BETAP = r"Beta-plus: en proton blir en neutron, så \(Z\) minskar med 1 och \(A\) är oförändrat"


def ett(rubrik, matte, svar, text=None):
    return ([(rubrik, matte, text)] if text else [(rubrik, matte)], svar)


def mc(rubrik, text, svar):
    return ([(rubrik, None, text)], svar)


F = {
    # rörelsemängd och impuls
    '5.277': ett(P, r"p=0{,}20\cdot8{,}0=1{,}6\ \mathrm{kg\cdot m/s}", "1,6 kg·m/s"),
    '5.298': ett(P, r"p=2{,}0\cdot3{,}0=6{,}0\ \mathrm{kg\cdot m/s}", "6,0 kg·m/s"),
    '5.299': ett(P, r"p=0{,}45\cdot20=9{,}0\ \mathrm{kg\cdot m/s}", "9,0 kg·m/s"),
    '5.300': ett(P, r"p=90\cdot5{,}0=450\ \mathrm{kg\cdot m/s}", "450 kg·m/s"),
    '5.278': ([('Givet och sökt', r"m=250\ \mathrm g=0{,}250\ \mathrm{kg},\quad v=10\ \mathrm{m/s}", 'Sökt: rörelsemängden p.'),
               (P, r"p=0{,}250\cdot10=2{,}5\ \mathrm{kg\cdot m/s}")], "2,5 kg·m/s"),
    '5.310': ([('Givet och sökt', r"m=150\ \mathrm g=0{,}150\ \mathrm{kg},\quad v=12\ \mathrm{m/s}", 'Sökt: rörelsemängden p.'),
               (P, r"p=0{,}150\cdot12=1{,}8\ \mathrm{kg\cdot m/s}")], "1,8 kg·m/s"),
    '5.311': ([('Givet och sökt', r"m=1\,000\ \mathrm{kg},\quad v=36\ \mathrm{km/h}=\frac{36}{3{,}6}\ \mathrm{m/s}=10\ \mathrm{m/s}", 'Sökt: rörelsemängden p.'),
               (P, r"p=1\,000\cdot10=10\,000\ \mathrm{kg\cdot m/s}")], "1,0·10⁴ kg·m/s"),
    '5.279': ett(P, r"v=\frac pm=\frac{3{,}6}{0{,}30}=12\ \mathrm{m/s}", "12 m/s"),
    '5.301': ett(P, r"v=\frac pm=\frac{20}{5{,}0}=4{,}0\ \mathrm{m/s}", "4,0 m/s"),
    '5.312': ett(P, r"v=\frac pm=\frac{3{,}0}{0{,}20}=15\ \mathrm{m/s}", "15 m/s"),
    '5.280': ett(P, r"m=\frac pv=\frac{4{,}9}{14}=0{,}35\ \mathrm{kg}", "0,35 kg"),
    '5.302': ett(P, r"m=\frac pv=\frac{18}{6{,}0}=3{,}0\ \mathrm{kg}", "3,0 kg"),
    '5.318': ([('Givet och sökt', r"m=0{,}50\ \mathrm{kg},\quad v_0=6{,}0\ \mathrm{m/s},\quad v=0",
                'Rörelseriktningen räknas som positiv. Sökt: impulsen I.'),
               (IMPP, r"I=m(v-v_0)=0{,}50\cdot(0-6{,}0)=-3{,}0\ \mathrm{Ns}")], "−3,0 Ns (riktad mot rörelseriktningen)"),
    '5.309': ett(r"Impulsen ändrar rörelsemängden: \(p_{\text{efter}}=p_{\text{före}}+I\)",
                 r"p_{\text{efter}}=4{,}0+3{,}0=7{,}0\ \mathrm{kg\cdot m/s}", "7,0 kg·m/s"),
    '5.303': ett(IMP, r"I=12\cdot0{,}50=6{,}0\ \mathrm{Ns}", "6,0 Ns"),
    '5.304': ett(IMP, r"I=100\cdot0{,}020=2{,}0\ \mathrm{Ns}", "2,0 Ns"),
    '5.305': ett(IMP, r"F=\frac{I}{\Delta t}=\frac{15}{0{,}30}=50\ \mathrm N", "50 N"),
    '5.306': ett(IMP, r"\Delta t=\frac IF=\frac{8{,}0}{20}=0{,}40\ \mathrm s", "0,40 s"),
    '5.307': ett(IMPP, r"I=2{,}0\cdot3{,}0=6{,}0\ \mathrm{Ns}", "6,0 Ns"),
    '5.308': ([('Givet och sökt', r"m=3{,}0\ \mathrm{kg},\quad I=-6{,}0\ \mathrm{Ns}", 'Framåt räknas som positiv riktning, så impulsen bakåt är negativ. Sökt: Δv.'),
               (IMPP, r"\Delta v=\frac Im=\frac{-6{,}0}{3{,}0}=-2{,}0\ \mathrm{m/s}")], "−2,0 m/s (hastigheten minskar med 2,0 m/s)"),
    # tryck
    '6.222': ett(TRYCK, r"p=\frac{400}{0{,}020}=20\,000\ \mathrm{Pa}", "20 000 Pa"),
    '6.223': ett(TRYCK, r"p=\frac{450}{0{,}025}=18\,000\ \mathrm{Pa}", "18 000 Pa"),
    '6.290': ett(TRYCK, r"p=\frac{250}{0{,}050}=5\,000\ \mathrm{Pa}", "5 000 Pa"),
    '6.350': ett(TRYCK, r"p=\frac{600}{0{,}30}=2\,000\ \mathrm{Pa}", "2 000 Pa"),
    '6.226': ([('Givet och sökt', r"F=600\ \mathrm N,\quad p=15\ \mathrm{kPa}=15\,000\ \mathrm{Pa}", 'Sökt: arean A.'),
               (TRYCK, r"A=\frac Fp=\frac{600}{15\,000}=0{,}040\ \mathrm{m^2}")], "0,040 m²"),
    '6.228': ett(TRYCK, r"F=pA=35\,000\cdot0{,}020=700\ \mathrm N", "700 N"),
    '6.229': ett(TRYCK, r"A=\frac Fp=\frac{400}{16\,000}=0{,}025\ \mathrm{m^2}", "0,025 m²"),
    '6.292': ett(TRYCK, r"A=\frac Fp=\frac{90}{3\,000}=0{,}030\ \mathrm{m^2}", "0,030 m²"),
    '6.352': ett(TRYCK, r"A=\frac Fp=\frac{500}{2\,500}=0{,}20\ \mathrm{m^2}", "0,20 m²"),
    '6.351': ([('Givet och sökt', r"p=3{,}0\ \mathrm{kPa}=3\,000\ \mathrm{Pa},\quad A=0{,}20\ \mathrm{m^2}", 'Sökt: kraften F.'),
               (TRYCK, r"F=pA=3\,000\cdot0{,}20=600\ \mathrm N")], "600 N"),
    # Arkimedes
    '6.271': ([(ARK, r"V=\frac{F_L}{\rho g}=\frac{19{,}64}{1\,000\cdot9{,}82}=0{,}0020\ \mathrm{m^3}"),
               ('Omvandla till liter', r"0{,}0020\ \mathrm{m^3}=2{,}0\ \mathrm{dm^3}=2{,}0\ \text{liter}")], "2,0 liter"),
    '6.321': ([(ARK, r"V=\frac{F_L}{\rho g}=\frac{4{,}91}{1\,000\cdot9{,}82}=0{,}000500\ \mathrm{m^3}"),
               ('Omvandla till kubikcentimeter', r"0{,}000500\ \mathrm{m^3}=500\ \mathrm{cm^3}")], "500 cm³"),
    '6.273': ([('Givet och sökt', r"V=2{,}5\ \text{liter}=0{,}0025\ \mathrm{m^3},\quad\Delta\rho=1\,040-1\,000=40\ \mathrm{kg/m^3}", 'Sökt: ökningen av lyftkraften.'),
               (ARK, r"\Delta F_L=\Delta\rho\cdot V\cdot g=40\cdot0{,}0025\cdot9{,}82\approx0{,}982\ \mathrm N")], "0,982 N"),
    '6.314': ett(r"Densitet: \(m=\rho V\)", r"m=1\,000\cdot0{,}0040=4{,}0\ \mathrm{kg}", "4,0 kg"),
    '6.323': ([('Lyftkraften avlastar kraftmätaren', None, 'Under vatten visar mätaren tyngden minus lyftkraften.'),
               (r"Lyftkraften är skillnaden mellan mätarens utslag: \(F_L=F_{\text{luft}}-F_{\text{vatten}}\)", r"F_L=8{,}0-5{,}5=2{,}5\ \mathrm N")], "2,5 N"),
    '6.361': ([('Krafterna är motriktade', None, 'Den resulterande kraften är skillnaden och pekar åt samma håll som den större kraften.'),
               (r"Resultant: \(F_R=F_g-F_L\)", r"F_R=25-18=7\ \mathrm N")], "7 N nedåt"),
    # gaser
    '6.347': ([('Givet och sökt', r"p=100\ \mathrm{kPa}=100\,000\ \mathrm{Pa},\quad V=10{,}0\ \text{liter}=0{,}0100\ \mathrm{m^3},\quad T=300\ \mathrm K",
                'Sökt: substansmängden n.'),
               (GAS, r"n=\frac{pV}{RT}=\frac{100\,000\cdot0{,}0100}{8{,}31\cdot300}\approx0{,}401\ \mathrm{mol}")], "0,401 mol"),
    '6.330': ett(r"\(1\ \mathrm{bar}=100\ \mathrm{kPa}\)", r"2{,}50\ \mathrm{bar}=2{,}50\cdot100\ \mathrm{kPa}=250\ \mathrm{kPa}", "250 kPa"),
    '6.339': ett(r"Absoluttryck: \(p_{\text{abs}}=p_{\text{över}}+p_{\text{luft}}\)", r"p_{\text{abs}}=220+100=320\ \mathrm{kPa}", "320 kPa"),
    '6.346': ([('Samma temperatur: varje gas uppfyller \\(pV=\\text{konstant}\\)', None,
                r'Gasen i A breder ut sig över båda behållarna, och likaså gasen i B. Sluttrycket är summan av deras tryck.'),
               (r"Summan av \(pV\) bevaras: \(p_AV_A+p_BV_B=p(V_A+V_B)\)", r"p=\frac{200\cdot2{,}00+100\cdot3{,}00}{2{,}00+3{,}00}=\frac{700}{5{,}00}=140\ \mathrm{kPa}")],
              "140 kPa"),
    # aktivitet och halveringstid
    '9.123': ([('Två halveringstider halverar aktiviteten två gånger', r"A=\frac{A_0}{2^2}"),
               ('Lös ut startaktiviteten', r"A_0=150\cdot2^2=600\ \mathrm{Bq}")], "600 Bq"),
    '9.125': ett('Halveringstiden är tiden det tar för aktiviteten att halveras', r"600\ \mathrm{Bq}\to300\ \mathrm{Bq}:\quad T_{1/2}=4{,}5\ \mathrm h", "4,5 h"),
    '9.146': ett('Halveringstiden är tiden det tar för aktiviteten att halveras', r"T_{1/2}=9{,}0-3{,}5=5{,}5\ \mathrm h", "5,5 h",
                 '600 Bq har blivit 300 Bq, alltså en halvering.'),
    '9.251': mc('Aktivitet är antalet sönderfall per sekund', 'Enheten är becquerel: 1 Bq = 1 sönderfall per sekund.', "becquerel (Bq)"),
    '9.127': ett(AKT, r"N=40\cdot5=200", "200 sönderfall"),
    '9.252': ett(AKT, r"N=30\cdot2=60", "60 sönderfall"),
    '9.253': ett('Varje halveringstid är lika lång', r"t=2\cdot8=16\ \mathrm{min}", "16 min"),
    '9.254': ett(HALV, r"A=1\,000\cdot\left(\frac12\right)^3=\frac{1\,000}{8}=125\ \mathrm{Bq}", "125 Bq"),
    '9.135': ett('Efter en halveringstid återstår hälften', None, "cirka 5 730 år",
                 'Halva aktiviteten betyder att en halveringstid har gått sedan trädet dog.'),
    '9.57': ([(HALV, r"A=12\cdot\left(\frac12\right)^{20/8}=12\cdot2^{-2{,}5}"), ('Beräkna', r"A\approx2{,}12\ \mathrm{kBq}")], "2,12 kBq"),
    '9.142': ([(HALV, r"\frac{A}{A_0}=\left(\frac12\right)^{27/6{,}0}=2^{-4{,}5}\approx0{,}0442"), ('Omvandla till procent', r"0{,}0442=4{,}42\ \%")], "4,42 %"),
    '9.86': {
        '': ([('a) Antal halveringstider', r"n=\frac{t}{T_{1/2}}=\frac{12}{3{,}0}=4"),
              (f'b) {HALV}', r"A=6{,}4\cdot\left(\frac12\right)^4=\frac{6{,}4}{16}=0{,}40\ \mathrm{kBq}")], "a) 4 b) 0,40 kBq"),
        'a': ([('Antal halveringstider', r"n=\frac{t}{T_{1/2}}=\frac{12}{3{,}0}=4")], "4"),
        'b': ([(HALV, r"A=6{,}4\cdot\left(\frac12\right)^{12/3{,}0}=\frac{6{,}4}{2^4}=0{,}40\ \mathrm{kBq}")], "0,40 kBq"),
    },
    '9.343': ett(r"Aktivitet: \(A=\lambda N\)", r"A=1{,}38\cdot10^{-11}\cdot2{,}65\cdot10^{18}\approx3{,}66\cdot10^{7}\ \mathrm{Bq}", r"\(3{,}66\cdot10^{7}\) Bq"),
    # stråldoser
    '9.161': ett(DOS, r"D=\frac{H}{w_R}=\frac{4{,}5}{1}=4{,}5\ \mathrm{mGy}", "4,5 mGy"),
    '9.162': ett(DOS, r"D=\frac{H}{w_R}=\frac{10}{20}=0{,}50\ \mathrm{mGy}", "0,50 mGy"),
    '9.174': ett(DOS, r"D=\frac{H}{w_R}=\frac{3{,}6}{1}=3{,}6\ \mathrm{mGy}", "3,6 mGy"),
    '9.180': ett(DOS, r"D=\frac{H}{w_R}=\frac{70}{20}=3{,}5\ \mathrm{mGy}", "3,5 mGy"),
    '9.176': ett(DOS, r"w_R=\frac HD=\frac{80}{4{,}0}=20", "20"),
    '9.178': ([('De absorberade doserna läggs ihop', r"D=1{,}2+1{,}3=2{,}5\ \mathrm{mGy}"), (DOS, r"H=1\cdot2{,}5=2{,}5\ \mathrm{mSv}")], "2,5 mSv"),
    '9.164': mc('Ekvivalent dos tar hänsyn till strålslagets skadlighet', 'Den mäts i sievert. Gray används för absorberad dos och becquerel för aktivitet.', "sievert (Sv)"),
    '9.165': ett(DOSR, r"H=20\cdot3=60\ \mathrm{\mu Sv}", "60 µSv"),
    '9.179': ett(DOSR, r"H=35\cdot2{,}5=87{,}5\ \mathrm{\mu Sv}", "87,5 µSv"),
    '9.259': ett(DOSR, r"H=15\cdot2=30\ \mathrm{\mu Sv}", "30 µSv"),
    '9.166': ett(DOSR, r"\dot H=\frac Ht=\frac{75}{3{,}5}\approx21{,}4\ \mathrm{\mu Sv/h}", "21,4 µSv/h"),
    '9.258': mc('Dosen från en liten källa minskar snabbt med avståndet', 'Avstånd, kort tid och skärmning minskar dosen. Att öka avståndet är det alternativ som hjälper.', "Öka avståndet till källan."),
    # strålning och materia
    '9.183': ett(r"Andelen som passerar: \(\dot H=\text{andel}\cdot\dot H_0\)", r"\dot H=0{,}12\cdot250=30\ \mathrm{\mu Sv/h}", "30 µSv/h"),
    '9.187': ([(HT, r"n=\frac{2{,}7}{0{,}90}=3"), ('Andelen som passerar', r"\left(\frac12\right)^3=0{,}125=12{,}5\ \%")], "12,5 %"),
    '9.284': ([(HT, r"n=\frac{3}{1}=3"), ('Andelen som passerar', r"\left(\frac12\right)^3=0{,}125=12{,}5\ \%")], "12,5 %"),
    '9.286': ([(HT, r"n=\frac{2}{0{,}5}=4"), ('Andelen som passerar', r"\left(\frac12\right)^4=0{,}0625=6{,}25\ \%")], "6,25 %"),
    '9.483': ett(HT, r"n=\frac{2{,}0}{2{,}0}=1\quad\Rightarrow\quad\left(\frac12\right)^1=50\ \%", "50 %"),
    '9.256': mc('Alfapartiklar har mycket kort räckvidd i materia', 'De är tunga och laddade och stoppas redan av ett papper.', "Alfastrålning."),
    '9.257': mc('Gammastrålning är oladdad och växelverkar minst med materia', 'Alfa stoppas av papper och beta av några millimeter metall, men gamma kräver tjock bly eller betong.', "Gamma."),
    # nuklider
    '9.202': ett(NUK, r"Z=6", "6 protoner", 'Det nedre talet är atomnumret, alltså antalet protoner.'),
    '9.241': ett('Atomnumret är antalet protoner', r"Z=6", "6 protoner"),
    '9.242': ett(NUK, r"A=14", "14", 'Det övre talet är masstalet.'),
    '9.205': ett(NUK, r"A=40", "40 nukleoner", 'Masstalet är antalet nukleoner.'),
    '9.204': ett(NUK, r"A=11+12=23", "23"),
    '9.212': ett(NUK, r"A=27+32=59", "59"),
    '9.203': ett(NEUT, r"N=16-8=8", "8 neutroner"),
    '9.209': ett(NEUT, r"N=31-15=16", "16 neutroner"),
    '9.211': ett(NEUT, r"N=37-17=20", "20 neutroner"),
    '9.214': ett(NEUT, r"N=238-92=146", "146 neutroner"),
    '9.217': ett(NEUT, r"N=24-12=12", "12 neutroner"),
    '9.243': ett(NEUT, r"N=18-8=10", "10 neutroner"),
    '9.229': ([(NEUT, r"N_{14}=14-6=8,\qquad N_{12}=12-6=6"), ('Skillnaden', r"8-6=2")], "2"),
    '9.215': ett('En neutral atom har lika många elektroner som protoner', r"N_e=Z=19", "19 elektroner"),
    '9.208': mc('Isotoper har samma atomnummer men olika masstal', r'Bara \({}^{12}_6\mathrm C\) och \({}^{14}_6\mathrm C\) har samma undre tal.', r"\({}^{12}_6\mathrm C\) och \({}^{14}_6\mathrm C\)"),
    '9.216': mc('Isotoper har samma antal protoner', 'Samma grundämne betyder samma atomnummer, så det är antalet neutroner som skiljer.', "antal neutroner."),
    '9.210': mc('Atomnumret avgör grundämnet', 'Antalet protoner i kärnan bestämmer vilket grundämne det är.', "Antalet protoner."),
    '9.213': mc('Nukleon är det gemensamma namnet på kärnans partiklar', 'Både protoner och neutroner kallas nukleoner.', "En proton eller neutron i kärnan."),
    '9.244': mc('Protoner och neutroner bildar atomkärnan', 'Elektronerna finns i skalen runt kärnan.', "Atomkärnan."),
    '9.573': ett(r"Medelvärde viktat med andelarna: \(\bar A=a_1A_1+a_2A_2\)", r"\bar A=0{,}758\cdot35+0{,}242\cdot37\approx35{,}5", "35,5"),
    # bindningsenergi
    '9.223': ett(BIND, r"E_b=23\cdot7{,}85\approx181\ \mathrm{MeV}", "cirka 181 MeV"),
    '9.226': ett(BIND, r"A=\frac{236}{7{,}375}=32", "32 nukleoner"),
    '9.224': ett(MDEF, r"\Delta m=\frac{127{,}6}{931{,}5}\approx0{,}1370\ \mathrm u", "0,1370 u"),
    '9.228': ett(MDEF, r"\Delta m=\frac{492{,}3}{931{,}5}\approx0{,}5285\ \mathrm u", "0,5285 u"),
    '9.230': ett('Skillnaden i bindningsenergi per nukleon', r"8{,}55-7{,}65=0{,}90\ \mathrm{MeV}", "0,90 MeV"),
    # kärnreaktioner, fission och fusion
    '9.195': ett(BEV, r"235+1=141+92+x\quad\Rightarrow\quad x=3", "3 neutroner", 'Varje neutron har masstalet 1.'),
    '9.196': ett(BEV, r"2+3=4+x\quad\Rightarrow\quad x=1", "1 neutron"),
    '9.453': ett(BEV, r"235+1=140+94+x\quad\Rightarrow\quad x=2", "2 neutroner"),
    '9.320': ([(BEV, r"10+1=7+A\quad\Rightarrow\quad A=4"), ('Atomnumret ger vilken partikel det är', r"5+0=3+Z\quad\Rightarrow\quad Z=2")],
              r"4 (X är en alfapartikel, \({}^4_2\mathrm{He}\))"),
    '9.198': ett(EMC, r"E=0{,}24\cdot931{,}5\approx224\ \mathrm{MeV}", "cirka 224 MeV"),
    '9.289': ett(EMC, r"E=0{,}018883\cdot931{,}5\approx17{,}6\ \mathrm{MeV}", "17,6 MeV"),
    '9.462': ett('Varje generation har dubbelt så många klyvningar', r"1,\ 2,\ 4,\ 8", "8 klyvningar"),
    '9.250': mc('Fission betyder klyvning', 'En tung kärna delas i två mindre kärnor och några neutroner, och energi frigörs. Två lätta kärnor som slås ihop är fusion.', "En tung kärna delas i mindre kärnor."),
    'KG-FY1-ALFA-01': ett(ALFA, r"Z_{\text{dotter}}=84-2=82", "82 (bly)"),
    '9.247': ett(ALFA, r"A_{\text{dotter}}=210-4=206", "206"),
    '9.517': ett(ALFA, r"A=222-3\cdot4=210", "210"),
    'KG-FY1-ALFA-04': {
        '': ([('Bara alfasönderfallen ändrar masstalet', r"238-4n_\alpha=206\quad\Rightarrow\quad n_\alpha=8"),
              ('Atomnumret: alfa minskar Z med 2, beta-minus ökar Z med 1', r"92-2\cdot8+n_{\beta}=82\quad\Rightarrow\quad n_{\beta}=6")],
             "8 alfasönderfall och 6 beta-minus-sönderfall"),
        'a': ([('Bara alfasönderfallen ändrar masstalet', r"238-4n_\alpha=206\quad\Rightarrow\quad n_\alpha=8"),
               ('Atomnumret: alfa minskar Z med 2, beta-minus ökar Z med 1', r"92-2\cdot8+n_{\beta}=82\quad\Rightarrow\quad n_{\beta}=6")],
              "8 alfasönderfall och 6 beta-minus-sönderfall"),
    },
    # sönderfall
    'KG-FY1-BM-01': ett(BETAM, r"Z_{\text{dotter}}=53+1=54", "54"),
    'KG-FY1-BP-01': ett(BETAP, r"Z_{\text{dotter}}=11-1=10", "10"),
    '9.315': ett(BETAM, r"A_{\text{dotter}}=131", "131"),
    '9.316': ([(BETAM, r"Z=15+1=16,\quad A=32"), (NEUT, r"N=32-16=16")], "16 neutroner"),
    '9.497': ([(BETAM, r"Z=27+1=28,\quad A=60"), (NEUT, r"N=60-28=32")], "32 neutroner"),
    # standardmodellen
    'GY25-FY1-STD-02': ([(KVARK, None, 'Protonen är uud.'), ('Summera laddningarna', r"Q=\left(\frac23+\frac23-\frac13\right)e=\frac33e=+e")], r"\(Q=+e\)"),
    '9.261': ett(KVARK, r"\frac Qe=\frac23+\frac23-\frac13=1", "+1 e"),
    '9.262': ett(KVARK, r"\frac Qe=\frac23-\frac13-\frac13=0", "0"),
    '9.263': ett(KVARK, r"\frac Qe=3\cdot\frac23=2", "+2 e"),
    '9.264': ett(KVARK, r"\frac Qe=-\frac23-\frac23+\frac13=-1", "−1 e"),
    '9.265': ett(KVARK, r"\frac Qe=\frac23+\frac13=1", "+1 e", 'Anti-nedkvarken har laddningen +⅓ e.'),
    '9.270': ett('En baryon består av tre kvarkar', r"\text{proton}=uud,\quad\text{neutron}=udd", "3"),
    '9.275': mc('Varje kraft har en förmedlande partikel', 'Den elektromagnetiska kraften förmedlas av fotonen.', "Fotonen"),
    '9.279': mc('Varje kraft har en förmedlande partikel', 'Den svaga kraften förmedlas av W⁺-, W⁻- och Z⁰-bosonerna.', "W- och Z-bosonerna"),
    # elektromagnetisk strålning
    '9.306': ([('Givet och sökt', r"f=2{,}4\ \mathrm{GHz}=2{,}4\cdot10^9\ \mathrm{Hz}", 'Sökt: våglängden λ. Ljusfarten c finns i formelsamlingen.'),
               (r"Vågekvationen: \(c=f\lambda\)", r"\lambda=\frac cf=\frac{3{,}00\cdot10^8}{2{,}4\cdot10^9}=0{,}125\ \mathrm m=12{,}5\ \mathrm{cm}")], "12,5 cm"),
    '9.480': ett(r"Fotonens energi: \(E=hf\)", None, "Den fördubblas", 'Energin är proportionell mot frekvensen.'),
    '9.474': mc('Spektrumet i frekvensordning', 'Radiovågor, mikrovågor, infrarött, synligt ljus, ultraviolett, röntgen, gamma. Mellan radiovågor och infrarött ligger mikrovågor.', "Mikrovågor"),
    # el
    '8.382': mc('En amperemeter kopplas i serie med lampan', 'Då går samma ström genom mätaren och lampan.', "A"),
    '8.536': mc('Spänning mäts i läget V', 'Sladdarna sitter redan i rätt uttag, så bara vredet behöver ställas om.', "V"),
    '8.559': mc('Spänning mäts i läget V', 'Sladdarna sitter redan i rätt uttag, så bara vredet behöver ställas om.', "V"),
    # fasövergångar
    '7.129': mc('Gas till vätska kallas kondensation', 'Vattenångan avger energi och blir flytande vatten.', "Kondensation"),
    '7.130': mc('Vätska till fast form kallas frysning (stelning)', 'Vattnet avger energi och blir is.', "Frysning"),
}
