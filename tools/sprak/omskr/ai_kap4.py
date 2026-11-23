"""AI kapitel 4 (maskininlärning), handskriven språkomskrivning 2026-11-23. Körs med tools/sprak/ai_byt.py.

- Inledningar som var metatext (”Frågorna handlar om …”) säger nu något om saken.
- Klassificeringsmatriserna: frågorna om precision och recall säger vad som räknas (”alla katter”, ”mejlen som
  modellen kallade spam”) i stället för mallens ”fall av katt” och ”orden sades”. Frågeorden varieras.
- Enstaka klumpiga meningar.
"""

ACC = ('Bestäm träffsäkerheten (accuracy), alltså andelen av alla fall som modellen klassar rätt.',
       'Hur stor är träffsäkerheten (accuracy), alltså andelen av alla fall som modellen klassar rätt?')

TYPER = ('Frågorna handlar om olika sorters maskininlärning: övervakad inlärning (klassificering eller regression), '
         'oövervakad inlärning och förstärkningsinlärning.',
         'Maskininlärning delas ofta in i övervakad inlärning (klassificering eller regression), oövervakad inlärning '
         'och förstärkningsinlärning.')


def prec(gammal_ord, ny):
    return (f'Bestäm precisionen, alltså andelen av fallen som modellen kallade {gammal_ord} som verkligen var {gammal_ord}.',
            f'Beräkna precisionen, alltså andelen av {ny}.')


def rec(gammal_ord, ny):
    return (f'Bestäm recall (täckningen), alltså andelen av alla verkliga fall av {gammal_ord} som modellen hittade.',
            f'Hur stor är recall (täckningen), alltså andelen av {ny} som modellen hittade?')


R = {
    **{f'4.0{i}': [TYPER] for i in range(1, 9)},
}
R['4.01'] = [TYPER, ('Vad är det som gör maskininlärning annorlunda än vanlig programmering?',
                     'Vad skiljer maskininlärning från vanlig programmering?')]
R['4.03'] = [TYPER, ('Den får poäng när den vinner och förlorar poäng när den förlorar.',
                     'Den får pluspoäng när den vinner och minuspoäng när den förlorar.')]
R['4.06'] = [TYPER, ('Hälften av etiketterna i en träningsdata är fel, eftersom de som märkte bilderna slarvade.',
                     'En modell tränas på bilder där hälften av etiketterna är fel, eftersom de som märkte bilderna '
                     'slarvade.')]
R.update({
    '4.16': [('Frågorna handlar om överanpassning och underanpassning.',
              'En modell kan vara överanpassad eller underanpassad.')],
    '4.20': [ACC, prec('spam', 'mejlen som modellen kallade spam som verkligen var spam'),
             rec('spam', 'alla spammejl')],
    '4.21': [ACC, ('Hur många av fallen var verkligen cancer?', 'Hur många av patienterna hade verkligen cancer?'),
             rec('cancer', 'alla patienter med cancer'),
             prec('cancer', 'patienterna som modellen sa hade cancer som verkligen hade cancer')],
    '4.22': [ACC, prec('katt', 'djuren som modellen kallade katt som verkligen var katter'),
             rec('katt', 'alla katter'),
             ('Hur många fall av katt missade modellen?', 'Hur många katter missade modellen?')],
    '4.23': [ACC, rec('bedrägeri', 'alla bedrägerier'),
             prec('bedrägeri', 'köpen som modellen kallade bedrägeri som verkligen var bedrägerier')],
    '4.24': [ACC, ('Hur många fall klassades som ägaren fast de egentligen var någon annan?',
                   'Hur många gånger trodde mobilen att det var ägaren fast det egentligen var någon annan?'),
             prec('ägaren', 'försöken där mobilen trodde att det var ägaren som verkligen var ägaren')],
    '4.25': [ACC, ('Hur många fall av fotgängare missade modellen?', 'Hur många bilder med fotgängare missade modellen?'),
             rec('fotgängare', 'alla bilder med fotgängare'),
             prec('fotgängare', 'bilderna där modellen såg en fotgängare som verkligen visade en fotgängare')],
    '4.26': [ACC, ('Hur många fall av burk missade modellen?', 'Hur många burkar missade modellen?'),
             prec('burk', 'föremålen som modellen kallade burk som verkligen var burkar'),
             rec('burk', 'alla burkar')],
    '4.27': [('Hur många fall klassades som fusk fast de egentligen var inte fusk?',
              'Hur många inlämningar klassades som fusk fast de egentligen inte var det?'),
             prec('fusk', 'inlämningarna som modellen kallade fusk som verkligen var fusk'),
             rec('fusk', 'alla fuskade inlämningar')],
    '4.28': [('Positiv klass är orden sades.', 'Positiv klass är att orden sades.'),
             ('Hur många av fallen var verkligen orden sades?', 'I hur många av klippen sades orden verkligen?'),
             ACC,
             prec('orden sades', 'klippen som röstassistenten vaknade av där orden verkligen sades'),
             rec('orden sades', 'alla klipp med orden')],
    '4.29': [ACC, rec('ogräs', 'allt ogräs'),
             prec('ogräs', 'plantorna som modellen kallade ogräs som verkligen var ogräs')],
    '4.33': [('Frågorna handlar om utvärderingsmåtten precision och recall.',
              'Precision och recall är två mått på hur bra en modell är.')],
    '4.35': [('Vilket fel som är värst beror på vad modellen används till. Frågorna handlar om tre olika AI-system.',
              'Vilket fel som är värst beror på vad modellen används till.')],
    '4.40': [('Räkna ut felet för varje dag, kvadrera felen och ta medelvärdet. Hur stort blir det? Talet kallas '
              'medelkvadratfel.',
              'Hur stort är modellens medelkvadratfel, alltså medelvärdet av felen i kvadrat för de fyra dagarna?')],
    '4.47': [('Frågorna handlar om vad linjär regression kan och inte kan visa.',
              'En AI kan använda linjär regression för att hitta samband i data.')],
    '4.62': [('Frågorna handlar om hur valet av k påverkar k närmaste grannar (kNN).',
              'I metoden k närmaste grannar (kNN) måste man välja k.')],
    '4.73': [('Frågorna handlar om vad k betyder i k-means och i kNN.',
              'Både k-means och kNN har ett k i namnet.')],
    '4.85': [('Här följer vi vad som händer när bara bias ändras.', 'I den här neuronen ändras bara bias.')],
})
