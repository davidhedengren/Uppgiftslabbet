# Fy1 parallellkoppling: delkorten hade ledtråden ”I serie går samma ström genom alla resistorer …” (2026-11-22).
SPAN = r"I en parallellkoppling ligger samma spänning över varje gren som över batteriet."
STROM = r"Spänningen över varje resistor är batteriets spänning. Ohms lag ger strömmen: \(I=U/R\)."
TOT = r"Strömmen delar sig i grenarna. Den totala strömmen är summan av strömmarna genom grenarna."
ERS = r"Ersättningsresistansen i en parallellkoppling: \(\frac{1}{R_{ers}}=\frac{1}{R_1}+\frac{1}{R_2}+\ldots\) Du kan också använda \(R_{ers}=U/I_{tot}\)."
L = {
    '8.16': {'a': STROM, 'b': TOT, 'c': ERS,
             'd': r"Dela strömmen genom R₁ med den totala strömmen. Vilken gren har minst resistans?"},
    '8.17': {'a': r"Innan den andra resistorn kopplas in finns bara en resistor. Ohms lag ger strömmen.",
             'b': ERS, 'c': r"Ohms lag med ersättningsresistansen ger den totala strömmen.",
             'd': r"Spänningen över den första resistorn är fortfarande batteriets spänning."},
    '8.19': {'a': SPAN, 'b': STROM, 'c': TOT, 'd': ERS},
    '8.51': {'a': STROM, 'b': TOT, 'c': ERS,
             'd': r"Tre lika resistorer parallellt: \(\frac1{R_{ers}}=\frac3R\)."},
    '8.88': {'a': SPAN, 'b': STROM, 'c': ERS},
    '8.91': {'a': SPAN, 'b': STROM, 'c': TOT, 'd': ERS},
    '8.136': {'a': SPAN, 'b': r"Effekten är \(P=UI\), så strömmen är \(I=P/U\).", 'c': TOT,
              'd': r"Ohms lag ger resistansen: \(R=U/I\)."},
    '8.137': {'a': r"Spänningen över R₁ är batteriets spänning. Ohms lag ger strömmen.",
              'b': r"Den totala strömmen delar sig i de två grenarna.", 'c': r"Ohms lag ger \(R_2=U/I_2\).",
              'd': ERS},
    '8.139': {'a': ERS, 'b': r"Ohms lag med ersättningsresistansen ger den totala strömmen.",
              'c': r"Varje ny gren ger strömmen en väg till. Hur påverkar det den totala strömmen vid samma spänning?"},
    '8.141': {'a': r"Ohms lag med batteriets spänning och strömmen ger den totala resistansen.",
              'b': r"Hela strömmen går genom R₁, så \(U_1=R_1I\). Resten av spänningen ligger över parallelldelen.",
              'c': r"Två lika resistorer parallellt har ersättningsresistansen \(R_2/2\). Den är spänningen över parallelldelen delad med strömmen."},
    '8.142': {'a': STROM, 'b': TOT, 'c': ERS},
    '8.155': {'a': SPAN, 'b': STROM, 'c': TOT, 'd': ERS},
}
