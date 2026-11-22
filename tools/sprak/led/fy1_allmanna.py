# Fy1: innehållslösa ledtrådar (”Utgå från de givna värdena och kontrollera enheterna”, ”Vilket samband kopplar ihop
# de givna storheterna?”, ”Andragradsekvation.”, ”Relativ fart.”, ”Tänk på riktningarna.”) och tyngdkraftsråd (2026-11-22).
Q = r"Energin som tas upp är \(Q=mc\Delta T\)."
Qm = r"Energin är \(Q=mc\Delta T\). Lös ut den storhet som söks."
PE = r"Effekt är energi per tid: \(P=E/t\)."
BLAND = r"Avgiven värme är lika med upptagen värme: \(m_1c_1(T_1-T)=m_2c_2(T-T_2)\). Lös ut sluttemperaturen T."
CBLAND = r"Avgiven värme är lika med upptagen värme. Lös ut metallens specifika värmekapacitet."
COUL = r"Coulombs lag: \(F=k\frac{|Q_1Q_2|}{r^2}\). Skriv laddningarna i C och avståndet i m."
TYNGD = r"Tyngdkraften är \(F_g=mg\)."
ANDRA = r"Ställ upp ett samband för sträcka och tid. Det blir en andragradsekvation, som du löser med pq-formeln eller grafiskt."
KAST = r"Använd \(s=v_0t+\frac{at^2}{2}\) med vald positiv riktning. Det blir en andragradsekvation i t."
KOLL = r"Rörelsemängden bevaras. Välj en positiv riktning, så att hastigheter åt andra hållet blir negativa."
REL = r"Arbeta med farten relativt den andra: skillnaden i fart när de rör sig åt samma håll och summan när de rör sig mot varandra."
L = {
    # ---------- värme ----------
    '7.13': {'a': Q + r" 12 liter vatten väger 12 kg per minut.", 'b': r"Skriv om energin till kWh och multiplicera med elpriset.",
             'c': r"Multiplicera kostnaden per dusch med 365."},
    '7.18': {'a': r"Värmeeffekten är U-värdet gånger arean gånger temperaturskillnaden.", 'b': PE + r" Tiden är 2000 timmar.",
             'c': r"Räkna energin med det nya U-värdet och jämför."},
    '7.30': {'a': r"Varje sekund värms 0,80 kg vatten 12 K. " + Q + r" Energin per sekund är effekten.", 'b': Q},
    '7.31': {'a': r"\(T=t+273\), där t är temperaturen i grader Celsius.", 'b': r"\(t=T-273\)."},
    '7.33': {'a': Q, 'b': PE + r" Lös ut tiden."},
    '7.36': {'a': r"Massan är densiteten gånger volymen.", 'b': Q, 'c': PE + r" Lös ut tiden."},
    '7.37': {'a': r"Verkningsgraden är nyttig effekt delad med tillförd effekt.", 'b': r"Det som inte blir nyttig effekt blir värme.",
             'c': r"Varje sekund ska kylvattnet ta upp 60 kJ. " + Qm},
    '7.40': {'a': r"Vattnet svalnar tills det har samma temperatur som rummet.", 'b': Qm},
    '7.41': {'a': Q + r" Skriv den specifika värmekapaciteten i J/(kg·K).", 'b': PE + r" Tiden är 10 minuter."},
    '7.42': {'a': Q, 'b': r"Lägesenergin är \(E=mgh\). Lös ut h."},
    '7.82': {'a': BLAND, 'b': BLAND, 'c': r"Jämför de två sluttemperaturerna."},
    '7.83': {'a': Q, 'b': r"Bara 80 % av den tillförda energin går till aluminiumet.", 'c': r"Resten, 20 %, går till omgivningen."},
    '7.137': {'a': Q, 'b': Qm, 'c': Q},
    '7.138': {'a': Qm + r" Temperaturen ökar.", 'b': Qm + r" Temperaturen minskar."},
    '7.139': {'a': Qm, 'b': Qm, 'c': Qm},
    '7.140': {'a': Qm, 'b': Qm, 'c': Qm},
    '7.148': {'a': r"Räkna energin för kastrullen och för vattnet var för sig och addera. " + Q,
              'b': r"Dela vattnets energi med den totala energin."},
    '7.150': {'a': Q + r" 245 liter vatten väger 245 kg.", 'b': PE + r" Lös ut tiden."},
    '7.159': {'a': r"Vattnet kan inte bli varmare än kokpunkten.", 'b': PE + r" Räkna först energin som behövs."},
    '7.160': {'a': PE + r" Räkna först energin som vattnet tar upp.",
              'b': r"Verkningsgraden är energin som går till vattnet delad med elenergin."},
    '7.166': {'a': BLAND, 'b': BLAND},
    '7.167': {'a': BLAND, 'b': BLAND},
    '7.176': {'a': CBLAND, 'b': CBLAND, 'c': CBLAND},
    '7.177': {'a': BLAND, 'b': BLAND, 'c': BLAND},
    '7.122': r"Temperaturändringen är skillnaden mellan start- och sluttemperaturen.",
    '7.123': r"Energi är effekt gånger tid: \(E=Pt\).",
    '7.124': PE,
    '7.126': r"Vad kallas det när två föremål har kommit fram till samma temperatur?",
    '7.127': Qm,
    '7.128': r"Vilket sätt att överföra värme fungerar utan något ämne emellan?",
    # ---------- tyngdkraft ----------
    '4.51': {'a': TYNGD},
    '6.2': TYNGD + r" Trycket är kraften delad med arean.",
    '6.2a': None,
    '8.101': {'b': TYNGD},
    '8.104': {'b': TYNGD},
    '8.170': {'b': TYNGD + r" Lös ut m."},
    # ---------- Coulombs lag ----------
    '8.21': {'b': COUL, 'c': r"Kraften är omvänt proportionell mot avståndet i kvadrat."},
    '8.23': {'b': COUL, 'c': r"Vad säger Newtons tredje lag om två kroppar som påverkar varandra?"},
    '8.57': {'b': COUL},
    '8.67': r"När kulorna nuddar varandra delas den sammanlagda laddningen lika.",
    '8.67a': None,
    '8.68': {'b': COUL + r" Räkna kraften från A och från C var för sig och tänk på riktningarna."},
    '8.72': COUL + r" Hur ändras kraften när avståndet eller laddningarna fördubblas?",
    '8.74': {'b': COUL},
    # ---------- fart och andragradsekvationer ----------
    '2.294': {'c': REL},
    '2.297': {'a': REL + r" Hur lång tid tar det att ta in avståndet?"},
    '2.301': {'c': ANDRA + r" Låt farten vara v och skriv tiderna som sträcka delat med fart."},
    '2.303': {'c': r"Farten nedströms är kanotistens fart plus strömmens, och uppströms minus. Den totala tiden ger en andragradsekvation."},
    '2.315': {'a': r"Skriv tiderna som sträcka delat med fart och sätt skillnaden lika med 2,0 h. Det blir en andragradsekvation.",
              'b': r"Skriv tiderna som sträcka delat med fart och sätt skillnaden lika med 1,5 h. Det blir en andragradsekvation.",
              'c': r"Skriv deras totala tider som sträcka delat med fart och sätt dem lika. Det blir en andragradsekvation."},
    '2.317': r"Farten nedströms är båtens fart plus strömmens, och uppströms minus. Sträckan är densamma.",
    '2.318': r"Personens fart relativt marken är 3,0 + 0,65 m/s åt ena hållet och 3,0 − 0,65 m/s åt andra.",
    '2.318c': None,
    '2.320': r"Pulserna kommer med 5,0 s mellanrum men ubåten åker mot dem. Hur lång tid går det mellan att ubåten möter två pulser?",
    '3.383': {'b': KAST},
    '3.388': {'b': r"Bestäm först v och a med de givna värdena. Sedan ger \(s=v_0t+\frac{at^2}{2}\) en andragradsekvation för halva sträckan."},
    '3.389': {'c': r"Ställ upp läget för både cyklisten och bilen som funktion av tiden och sätt dem lika. Det blir en andragradsekvation."},
    '3.399': {'a': KAST + r" Den mindre lösningen är på väg upp.", 'b': KAST + r" Den större lösningen är på väg ned."},
    '3.400': {'b': KAST + r" Välj uppåt som positiv riktning. Marken ligger 7,0 m under startpunkten."},
    '3.404': {'a': KAST + r" Marken ligger 2,50 m under startpunkten."},
    # ---------- kollisioner ----------
    '5.402': KOLL, '5.403': KOLL + r" Skriv farterna i m/s.", '5.406': KOLL,
    '5.418': {'a': KOLL},
    '5.426': {'a': KOLL},
    '5.434': KOLL,
}
# Nycklar med None och bokstav sist är bara anteckningar om att delkortet täcks av huvudposten nedan.
for k in [k for k, v in L.items() if v is None]:
    del L[k]
# Delkort som har samma allmänna ledtråd som huvuduppgiften.
L['6.2'] = {'': TYNGD + r" Trycket är kraften delad med arean.", 'a': TYNGD}
L['8.67'] = {'': r"När kulorna nuddar varandra delas den sammanlagda laddningen lika.",
             'a': r"När kulorna nuddar varandra delas den sammanlagda laddningen lika."}
L['8.72'] = {'': COUL, 'a': COUL, 'b': r"Kraften är omvänt proportionell mot avståndet i kvadrat.",
             'c': r"Kraften är proportionell mot produkten av laddningarna."}
L['2.318'] = {'': r"Personens fart relativt marken är 3,0 + 0,65 m/s åt ena hållet och 3,0 − 0,65 m/s åt andra.",
              'c': REL}
