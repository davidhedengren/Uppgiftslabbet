"""AI kapitel 3 (minimax och alfa–beta, 3.01–3.80), handskriven språkomskrivning 2026-11-23.
Körs med tools/sprak/ai_byt.py. Uppgifterna 3.81–3.255 skrevs samma dag i lärarens stil och ändras inte här.

- Inledningar som var metatext (”Frågorna handlar om …”).
- Svarsinstruktionen ”(Ta beskärningarna i den ordning de sker …)” i 3.05 c och 3.24 c flyttas till kgInstruktion.
- Enstaka klumpiga formuleringar.
"""

ORDNING = ' (Ta beskärningarna i den ordning de sker: nod, α och β för var och en.)'
KG_ORDNING = 'Ta beskärningarna i den ordning de sker: nod, α och β för var och en.'

R = {
    '3.05': [(ORDNING, ''), {'@kg': {'c': KG_ORDNING}}],
    '3.24': [(ORDNING, ''), {'@kg': {'c': KG_ORDNING}}],
    '3.43': [('Frågorna handlar om hur minimax fungerar.', 'Spelträdet söks igenom med minimax.')],
    '3.44': [('Frågorna handlar om hur ett spel beskrivs som ett spelträd för en spelagent.',
              'En spelagent beskriver ett spel som ett spelträd.')],
    '3.45': [('Frågorna handlar om vad rotens minimaxvärde betyder.',
              'En spelagent har räknat ut rotens minimaxvärde i ett spelträd.')],
    '3.66': [('Två elever spelar ett tärningsfritt räknespel. Talen i löven är vad MAX vinner, negativt betyder att MAX '
              'förlorar.',
              'Två elever spelar ett räknespel. Talen i löven är vad MAX vinner. Ett negativt tal betyder att MAX '
              'förlorar.')],
}
