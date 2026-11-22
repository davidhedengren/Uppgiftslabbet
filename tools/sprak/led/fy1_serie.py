# Fy1 seriekoppling: delkorten hade samma ledtråd, som i 8.124 a avslöjade svaret (2026-11-22).
ERS = r"I en seriekoppling adderas resistanserna: \(R_{ers}=R_1+R_2+\ldots\)"
STROM = r"Ohms lag med batteriets spänning och ersättningsresistansen ger strömmen: \(I=U/R_{ers}\)."
DELU = r"Samma ström går genom alla resistorerna. Spänningen över var och en är \(U=RI\)."
EFF = r"Effekten i en resistor är \(P=RI^2\)."
OHM_R = r"Ohms lag ger resistansen: \(R=U/I\)."
L = {
    '8.20': {'a': OHM_R + r" Skriv strömmen i ampere.",
             'b': r"Batteriets spänning delas mellan resistorerna. Dra bort spänningen över den första.",
             'c': OHM_R},
    '8.40': {'a': ERS, 'b': r"Ohms lag ger strömmen: \(I=U/R\).", 'c': EFF, 'd': r"Effekten är \(P=UI\)."},
    '8.55': {'a': ERS, 'b': STROM, 'c': DELU},
    '8.62': {'a': ERS, 'b': STROM, 'c': DELU,
             'd': r"Två resistorer är kvar, så ersättningsresistansen minskar. Ohms lag ger den nya strömmen."},
    '8.64': {'a': r"En amperemeter mäter strömmen som går igenom den. Hur måste den då sitta i förhållande till R?",
             'b': OHM_R, 'c': EFF},
    '8.124': {'a': r"Följ strömmens väg. Går den genom resistorerna efter varandra eller delar den sig?",
              'b': ERS, 'c': r"Ohms lag ger strömmen: \(I=U/R\)."},
    '8.125': {'a': ERS, 'b': STROM,
              'c': r"I en seriekoppling finns bara en väg för strömmen. Vad betyder det för strömmen genom varje resistor?"},
    '8.131': {'a': ERS, 'b': STROM, 'c': DELU,
              'd': r"Dela spänningen över R₃ med batteriets spänning."},
    '8.132': {'a': ERS, 'b': STROM, 'c': DELU,
              'd': r"I en seriekoppling är summan av delspänningarna lika med batteriets spänning."},
    '8.135': {'a': r"Ohms lag med batteriets spänning och strömmen ger den totala resistansen.",
              'b': r"Den totala resistansen är summan av de två. Dra bort 150 Ω.", 'c': EFF},
    '8.138': {'a': ERS, 'b': STROM, 'c': DELU},
}
