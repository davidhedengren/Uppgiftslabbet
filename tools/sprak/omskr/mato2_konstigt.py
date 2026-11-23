"""Ma4: konstiga meningar som granskaren hittade 2026-11-23. Körs med tools/sprak/byt_falt.py.

- 1.179–1.186: ”Skissa kurvan … i koordinatsystemet.” följt av ett eget stycke ”för 0 ≤ x ≤ 2π” utan punkt.
- ”Funktionen \\(f(x)=…\\).” utan verb blir ”För funktionen \\(f\\) gäller att \\(f(x)=…\\).” (stilguiden).
- 2.213: ”hos grafen \\(f(x)=…\\)” saknade ”till”.
- Svarsinstruktioner i papperstexten flyttas till kgInstruktion (användarbeslut 2026-11-23): 1.53 b, 2.496,
  4.334, 2.719. 2.577 behåller sin upplysning om dagnumren, omskriven som påstående.
"""


def skissa(kurva, slut):
    return [(f'<p>Skissa kurvan \\({kurva}\\) i koordinatsystemet.</p><p>för \\(0\\le x\\le{slut}\\)</p>',
             f'<p>Skissa kurvan \\({kurva}\\) för \\(0\\le x\\le{slut}\\) i koordinatsystemet.</p>')]


def verblos(namn, uttryck, var='x'):
    return [(f'Funktionen \\({namn}({var})={uttryck}\\).',
             f'För funktionen \\({namn}\\) gäller att \\({namn}({var})={uttryck}\\).')]


BYT = {
    '1.179': skissa('y=\\sin 2x', '2\\pi'),
    '1.180': skissa('y=\\cos(x/2)', '4\\pi'),
    '1.181': skissa('y=2\\sin x', '2\\pi'),
    '1.182': skissa('y=1+2\\cos x', '2\\pi'),
    '1.183': skissa('y=\\sin(x-\\pi/3)', '2\\pi'),
    '1.184': skissa('y=-2\\cos 2x', '2\\pi'),
    '1.185': skissa('y=3\\sin(x/2)-1', '4\\pi'),
    '1.186': skissa('y=1+2\\cos(x+\\pi/4)', '2\\pi'),
    '1.518': verblos('f', '3\\sin(2x)-1'),
    '1.519': verblos('g', '4\\cos(\\pi x/3)+2'),
    '1.524': verblos('f', '\\tan(x/2)'),
    '2.193': verblos('h', '\\sqrt{1+(f(x))^2}'),
    '2.225': verblos('h', 'f(g(x))'),
    '2.263': verblos('h', 'f(2x-1)'),
    '2.462': verblos('f', '(x^2-4)/(x-2)'),
    '2.203': verblos('f', '\\frac{x^2+1}{x-1}'),
    '2.213': [('hos grafen \\(f(x)=\\ln x-x\\)', 'hos grafen till \\(f(x)=\\ln x-x\\)')],
    '1.53': [(' Svara med \\(\\arccos\\) eller med tre decimaler.', '')],
    '2.496': [('</p><p>Ange asymptoten som \\(y=\\ldots\\) och svara därefter ja eller nej.</p>', '</p>')],
    '4.334': [(' Svara med koefficienter med tre decimaler.', '')],
    '2.719': [(' Svara med k med två decimaler.', '')],
    '2.577': [(' Svara med dagnummer, där 1 januari är dag 1.', ' Dag 1 är den 1 januari.')],
}

KG = {
    '1.53': {'b': 'Svara med \\(\\arccos\\) eller med tre decimaler.'},
    '2.496': {'': 'Ange asymptoten som \\(y=\\ldots\\) och svara därefter ja eller nej.'},
    '4.334': {'': 'Svara med koefficienter med tre decimaler.'},
    '2.719': {'': 'Svara med k med två decimaler.'},
}
