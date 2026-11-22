# Ma5 differentialekvationer och modeller: egna ledtrådar (2026-11-22).
KAR = r"Sätt \(y=e^{rx}\). Då får du den karakteristiska ekvationen \(r^2+ar+b=0\), som du löser med pq-formeln."
KAR2 = KAR + r" Två olika reella rötter ger \(y=C_1e^{r_1x}+C_2e^{r_2x}\)."
DUBB = KAR + r" En dubbelrot r ger \(y=(C_1+C_2x)e^{rx}\)."
KOMPL = KAR + r" Komplexa rötter \(a\pm bi\) ger \(y=e^{ax}(C_1\cos bx+C_2\sin bx)\)."
BV = r"Bestäm först den allmänna lösningen. Sätt sedan in \(y(0)\) och \(y'(0)\) och lös ut konstanterna."
INH = r"Lös först den homogena ekvationen. Lägg sedan till en partikulärlösning av samma typ som högerledet."
INH_KONST = INH + r" Ett konstant högerled ger en konstant ansats \(y_p=A\)."
EULER = r"Eulers metod: \(y_{n+1}=y_n+h\cdot f(x_n,y_n)\), där lutningen räknas i den gamla punkten. Gör ett steg i taget."
LUT = r"Lutningen i en punkt får du genom att sätta in punktens koordinater i högerledet."
INS = r"Kontrollera genom att derivera den givna lösningen och sätta in den i differentialekvationen."
NEWTON = r"Newtons avsvalningslag ger \(T=T_{\text{rum}}+Ce^{-kt}\). Startvärdet bestämmer C och ett mätvärde bestämmer k."
TANK = r"Mängden ändras som inflöde minus utflöde: \(M'=\) (koncentration in)·(flöde in) − \(\frac{M}{V}\)·(flöde ut)."
JAMV = r"Vid jämvikt är förändringshastigheten noll. Sätt högerledet lika med 0."
EXPV = r"\(P'=kP\) ger \(P=P_0e^{kt}\)."
LOG = r"I den logistiska modellen \(P'=kP\left(1-\frac PK\right)\) är K den största populationen, och tillväxten är störst vid \(P=K/2\)."
LOGLOS = r"Den logistiska lösningen är \(y=\frac{K}{1+Ce^{-kt}}\), där C bestäms av startvärdet."
FALL = r"Gränshastigheten nås när accelerationen är noll. Sätt \(v'=0\) och lös ut v."
L = {
    # ---------- homogena av andra ordningen ----------
    '4.01': BV, '4.02': BV, '4.04': KAR2, '4.05': KAR2 + r" Välj till exempel \(C_2=0\).",
    '4.53': KAR2, '4.73': KAR2, '4.74': KAR2, '4.97': KAR2, '4.98': BV,
    '4.10': DUBB, '4.12': r"Den första är av första ordningen: \(y=Ce^{8x}\). " + KOMPL,
    '4.22': BV + r" Den karakteristiska ekvationen har en dubbelrot.",
    '4.43': r"Lösningen har formen för en dubbelrot \(r=-3\). Den karakteristiska ekvationen är alltså \((r+3)^2=0\).",
    '4.54': DUBB, '4.75': DUBB, '4.99': DUBB, '4.100': BV,
    '4.55': KOMPL, '4.77': KOMPL, '4.101': KOMPL, '4.102': BV,
    '4.81': r"Den homogena lösningen innehåller redan \(\sin2x\) och \(\cos2x\). Då måste ansatsen multipliceras med x.",
    '4.06': BV, '4.07': BV, '4.56': BV, '4.82': BV, '4.83': BV,
    '4.121': BV + r" Skriv sedan \(C_1\cos3x+C_2\sin3x\) som \(A\cos(3x+\varphi)\) med \(A=\sqrt{C_1^2+C_2^2}\).",
    '4.127': BV, '4.128': BV, '4.129': BV, '4.169': BV,
    # ---------- inhomogena ----------
    '4.27': INH_KONST, '4.79': INH_KONST, '4.119': INH_KONST, '4.151': INH_KONST,
    '4.80': r"Högerledet är ett förstagradspolynom, så pröva \(y_p=Ax+B\).",
    '4.103': INH + r" Pröva \(y_p=Ae^{2x}\).",
    '4.104': r"Pröva \(y_p=A\cos2x+B\sin2x\) och sätt in i ekvationen.",
    '4.152': INH + r" Pröva \(y_p=Ae^{4x}\).",
    '4.400': r"Integrera två gånger. Begynnelsevillkoren bestämmer de två konstanterna.",
    '4.108': INH_KONST + r" Sätt sedan in begynnelsevillkoren.",
    '4.131': INH_KONST + r" Sätt sedan in begynnelsevillkoren.",
    '4.171': INH_KONST + r" Sätt sedan in begynnelsevillkoren.",
    '4.41': r"Newtons andra lag ger \(y''+9y=6\cos2t\). " + INH + r" Pröva \(y_p=A\cos2t+B\sin2t\).",
    '4.42': INH_KONST + r" När t blir stor går de homogena termerna mot 0.",
    # ---------- riktningsfält och Euler ----------
    '4.19': EULER, '4.39': EULER, '4.58': EULER, '4.85': EULER, '4.111': EULER,
    '4.112': r"Jämför felen för de två steglängderna. Hur ändras felet när steget halveras?",
    '4.20': LUT + r" Fältet är horisontellt där \(x-y=0\).",
    '4.37': r"Var är linjeelementen horisontella i figuren? Där är högerledet noll.",
    '4.38': r"Sätt in punkten \((0,1)\) i den allmänna lösningen och bestäm C.",
    '4.57': LUT,
    '4.84': r"\(y'=2-y\) är negativ när \(y>2\) och positiv när \(y<2\). Vad händer då med lösningarna?",
    '4.110': LUT + r" Vid \((0,3)\) är \(y'=-3\). Vad händer med lutningen när kurvan närmar sig \(y=x-1\)?",
    '4.122': EULER + r" Den exakta lösningen är \(y=e^{-2x}\).",
    '4.132': EULER, '4.133': EULER, '4.134': LUT,
    '4.136': EULER + r" Jämför sedan båda värdena med det exakta.",
    '4.137': LUT + r" Högerledet är noll där \(x-2y=0\).",
    '4.139': EULER,
    '4.172': LUT, '4.173': EULER,
    '4.25': INS + r" Kontrollera också att \(y(0)=1\).",
    '4.26': EULER + r" Jämför sedan med det exakta värdet e.",
    '4.45': INS + r" Termerna med \(C_1\) och \(C_2\) löser den homogena ekvationen.",
    '4.60': r"Sätt in \(x=1\) och \(y=6\) i \(y=Ce^{4x}\) och lös ut C.",
    '4.87': INS + r" Kontrollera att vänsterledet blir 10.",
    '4.117': r"Tolka \(y(5)\approx3{,}84\) med enheterna: vad är y och vad är t?",
    '4.484': r"Om resultatet ändras mycket när steget halveras är felet stort. Vad säger det om hur säker approximationen är?",
    '4.118': r"Det absoluta felet är skillnaden mellan det exakta och det approximativa värdet.",
    '4.163': r"Vad händer med \(T(t)\) när t blir mycket stort?",
    # ---------- förändringsmodeller ----------
    '4.11': EXPV + r" Sätt \(e^{-0{,}00012t}=0{,}52\) och lös ut t.",
    '4.17': NEWTON,
    '4.18': TANK,
    '4.24': r"Lös \(v'=9{,}82-0{,}40v\) med \(v(0)=0\). Sträckan är integralen av hastigheten.",
    '4.467': FALL,
    '4.40': TANK,
    '4.59': TANK + r" Läs noga om volymen är konstant.",
    '4.86': r"Avsvalningen är proportionell mot temperaturskillnaden: \(T'=-k(T-20)\).",
    '4.113': r"Proportionell mot storleken betyder \(P'=kP\).",
    '4.114': r"Nedbrytningen ger termen \(-kM\) och tillförseln \(+20\). Skriv \(M'=20-kM\).",
    '4.115': TANK,
    '4.116': r"\(T(0)=80\) ger C. Sätt sedan \(T(10)=50\) och lös ut k.",
    '4.474': r"Modellen förutsätter konstant rumstemperatur. Vad händer om \(T_r\) i stället är en funktion av tiden?",
    '4.162': TANK,
    '4.164': JAMV,
    '4.165': EXPV + r" Fördubbling betyder \(e^{10k}=2\).",
    '4.166': r"Sätt \(T(5)=50\) och lös ut k med logaritmer.",
    '4.175': EXPV,
    '4.176': r"Jämviktsvärdet är 60 mg, så \(M=60+Ce^{-0{,}3t}\). \(M(0)=0\) ger C.",
    '4.479': r"Vid hög fart växer luftmotståndet snabbare än linjärt. Pröva en modell med \(kv^2\).",
    '4.304': r"Avsvalningen är proportionell mot temperaturskillnaden, och temperaturen minskar när föremålet är varmare än rummet.",
    '4.308': EXPV + r" Fördubbling betyder \(e^{6k}=2\).",
    '4.483': r"När inflödet är större än utflödet ändras volymen med tiden. Då måste V i utflödestermen bytas mot \(V(t)\).",
    '4.500': r"Sätt in \(T=50\) i högerledet.",
    '4.501': r"Sätt in \(T=10\) i högerledet.",
    '4.502': JAMV,
    '4.503': r"Sätt in \(t=0\): \(80=20+C\).",
    '4.504': r"Sätt in \(t=10\) i modellen.",
    '4.505': r"Sätt \(20+60e^{-0{,}10t}=50\) och lös ut t med logaritmer.",
    '4.506': r"Kan \(Ce^{-kt}\) bli negativ om C är positiv?",
    '4.507': r"Vad händer med \(Ce^{-kt}\) när t blir mycket stort?",
    '4.508': r"Integrera accelerationen. Starthastigheten är 0.",
    '4.509': r"Sträckan är integralen av hastigheten \(v=9{,}82t\).",
    '4.510': FALL, '4.511': FALL,
    '4.512': r"Newtons andra lag: \(mv'=mg-0{,}030v\). Dela med massan.",
    # ---------- tillväxt med begränsning ----------
    '4.466': r"Sätt in \(t=9\) i lösningen.",
    '4.468': r"Modellen \(P'=kP\) växer obegränsat. Vad begränsar en verklig population?",
    '4.478': r"Låt bärförmågan vara en funktion av tiden, \(K(t)\), som minskar.",
    '4.309': JAMV + r" Den positiva jämvikten är när parentesen är noll.",
    '4.492': LOG, '4.493': LOG,
    '4.494': r"Sätt in \(P=40\) i högerledet.",
    '4.495': r"Tillväxthastigheten är symmetrisk kring \(K/2\). Vilket värde ligger lika långt från 80 som 40?",
    '4.496': LOG, '4.497': LOG,
    '4.498': r"Sätt in \(P=250\) i högerledet.",
    '4.499': r"Sätt in värdena i \(P'=kP(1-P/K)\) och lös ut k.",
    '4.528': LOGLOS, '4.529': LOGLOS + r" Den största tillväxthastigheten fås vid halva bärförmågan.",
    '4.531': LOGLOS + r" Bestäm k med hjälp av värdet efter 5 dygn.",
    '4.532': LOGLOS, '4.533': LOGLOS, '4.534': LOGLOS, '4.535': LOGLOS,
}
