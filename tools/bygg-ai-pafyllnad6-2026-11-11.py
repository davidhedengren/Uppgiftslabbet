"""AI-banken 2026-11-11, nionde omgången: minimax och beskärning på E- och C-nivå.

Användarens önskemål: fler minimaxuppgifter och beskärningsuppgifter på E–C-nivå.
Tolkning (AI_NIVAINDELNING.md, tillägg): fullständig alfa–beta-spårning är
fortfarande A. Nya beskärningsuppgifter här har stöd, med träd i två nivåer, givna
mellanvärden och ett enda beslut. De är därför C, och begreppsfrågor om vad
beskärning är blir E. Nivåerna sätts i nivåskriptets OVERRIDE.

Kör efter bygg-ai-pafyllnad5-2026-11-11.py och före bygg-ai-nivaer-2026-11-11.py.
"""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_spec = importlib.util.spec_from_file_location('ai_kg', os.path.join(HERE, 'bygg-ai-kunskapsgymmet-2026-11-11.py'))
K = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(K)
from ai_figurer import step, game_tree  # noqa: E402
import ai_sokalgoritmer as A  # noqa: E402
import ai_speltrad as T  # noqa: E402

p, alt, num, val, kg_task = K.p, K.alt, K.num, K.val, K.kg_task
BANK = 'uppgifterai.js'
MM = p('Spelträdet söks igenom med minimax.')


def fig(vals, root_max, title, leaf_names=True, spacing=60):
    return game_tree(T.to_figure(T.build(vals, root_max)), root_max, title, leaf_names=leaf_names, spacing=spacing)


def mc(fraga, rubrik, text, alts, ledtrad, tn):
    return val(fraga, [step(rubrik, text)], [alt(t, r, k) for t, r, k in alts], ledtrad, tn)


# ======================================================================== minimax

def t350():
    vals = [[-1, [1]], [-1]]
    assert A.minimax(vals, True) == -1
    intro = (fig(vals, True, 'Spelträd för stickspelet. Roten är MAX, A och B är MIN och C är MAX. Under A ligger först draget att ta 2 stickor och sedan draget att ta 1.', leaf_names=False, spacing=120) +
             p('Tre stickor ligger på bordet. Spelarna turas om att ta 1 eller 2 stickor, och den som tar den sista stickan vinner. MAX börjar.') +
             p('Trädet visar spelet. Talet 1 i ett löv betyder att MAX vinner och −1 att MIN vinner. Spelträdet söks igenom med minimax.'))
    a = num('Vilket värde får A?', [step('A är MIN:s tur med två stickor kvar', 'MIN kan ta 2 stickor och vinna direkt (−1), eller ta 1 och lämna en till MAX (C = 1).'),
                                    step('MIN väljer minsta värdet', 'A = min(−1, 1) = −1.')], -1, 'Vad gör MIN om MIN kan vinna direkt?', 2)
    b = num('Vilket värde får roten?', [step('Båda dragen ger −1', 'A = −1. B = −1, eftersom MIN tar den sista stickan.'), step('Roten', 'R = max(−1, −1) = −1.')], -1,
            'Bestäm A och B först.', 2)
    c = mc('Vad betyder det att roten får värdet −1?', 'MIN vinner vid bästa spel',
           'Vad MAX än gör i början kan MIN svara så att MIN tar den sista stickan.',
           [('MIN vinner om båda spelar så bra som möjligt', True, 'Rotvärdet är resultatet när båda väljer sina bästa drag.'),
            ('MAX vinner alltid', False, 'Då skulle rotvärdet vara 1.'),
            ('Spelet slutar oavgjort', False, 'Spelet har bara vinst och förlust, 1 eller −1.'),
            ('MIN vinner bara om MAX gör ett misstag', False, 'MIN vinner även när MAX spelar så bra som möjligt.')],
           'Vad betyder −1 i löven?', 3)
    return kg_task('3.50', 'minimax', 'Stickspelet', intro, [a, b, c], 'Talet i ett löv visar vem som vinner. MAX vill ha 1, MIN vill ha −1.', ['procedur', 'begrepp'])


def t351():
    vals = [[2, 7], [6, 8], [5, 1], [3, 9]]
    assert A.minimax(vals, True) == 6
    intro = fig(vals, True, 'Spelträd med MAX i roten och fyra MIN-noder A, B, C och D med två löv var.') + MM
    a = num('Hur många av MIN-noderna A, B, C och D får ett värde som är minst 5?',
            [step('MIN-nodernas värden', 'A = min(2, 7) = 2. B = min(6, 8) = 6. C = min(5, 1) = 1. D = min(3, 9) = 3.'), step('Räkna', 'Bara B har ett värde som är minst 5.')],
            1, 'Bestäm värdet i varje MIN-nod.', 2)
    b = num('Vilket värde får roten?', [step('Roten väljer det största värdet', 'R = max(2, 6, 1, 3) = 6.')], 6, 'Jämför de fyra MIN-nodernas värden.', 1)
    c = mc('Vilket drag väljer roten?', 'Draget till B', 'B ger 6, mer än A (2), C (1) och D (3).',
           [('Draget till A', False, 'A har värdet 2, eftersom MIN väljer 2 före 7.'), ('Draget till B', True, 'B har värdet 6, det största av de fyra.'),
            ('Draget till C', False, 'C har värdet 1, lägst av alla.'), ('Draget till D', False, 'D innehåller lövet 9, men MIN väljer 3.')],
           'Vilket av rotens barn ger rotens värde?', 1)
    return kg_task('3.51', 'minimax', 'Fyra drag för MAX', intro, [a, b, c], 'Varje MIN-nod väljer det minsta av sina löv.', ['procedur'])


def t352():
    vals = [[3, 6], [5, 7]]
    assert A.minimax(vals, True) == 5 and A.minimax([[8, 6], [5, 7]], True) == 6
    intro = fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A och B. Löven heter L1–L4.') + MM
    a = num('Vilket värde får roten?', [step('MIN-noderna', 'A = min(3, 6) = 3. B = min(5, 7) = 5.'), step('Roten', 'R = max(3, 5) = 5.')], 5,
            'Bestäm A och B först.', 1)
    b = mc('Lövet L1 ändras från 3 till 8. Övriga löv är som i bilden. Vilket drag väljer roten nu?', 'A får ett nytt värde',
           'A = min(8, 6) = 6. B = 5. Roten väljer A, eftersom 6 är större än 5.',
           [('Draget till A', True, 'A blir 6 och är nu bättre för MAX än B.'), ('Draget till B', False, 'B är fortfarande 5, men A har blivit 6.'),
            ('Båda är lika bra', False, 'A ger 6 och B ger 5.')], 'Räkna om A med det nya lövet.', 2)
    c = num('Vilket värde får roten efter ändringen?', [step('Roten', 'R = max(6, 5) = 6.')], 6, 'Använd A:s nya värde.', 2)
    return kg_task('3.52', 'minimax', 'Ett löv byter värde', intro, [a, b, c], 'Ett ändrat löv påverkar bara noderna ovanför det.', ['procedur'])


def t353():
    vals = [[4, 1, 6], [3, 8], [7, 2]]
    assert A.minimax(vals, True) == 3
    intro = fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A, B och C.', leaf_names=False) + MM
    a = mc('Vilken spelare väljer i noden A?', 'A är en MIN-nod', 'Nedåtriktade trianglar är MIN-noder.',
           [('MIN', True, 'A har en nedåtriktad triangel.'), ('MAX', False, 'MAX väljer i roten, som har en uppåtriktad triangel.'),
            ('Ingen, A är ett löv', False, 'Löven är rutorna med tal längst ned.')], 'Titta på triangelns riktning.', 1)
    b = num('Hur många drag kan MAX välja mellan i roten?', [step('Räkna rotens barn', 'Roten har tre barn: A, B och C.')], 3, 'Räkna kanterna från roten.', 1)
    c = num('Vilket värde får roten?', [step('MIN-noderna', 'A = min(4, 1, 6) = 1. B = min(3, 8) = 3. C = min(7, 2) = 2.'), step('Roten', 'R = max(1, 3, 2) = 3.')], 3,
            'Bestäm A, B och C först.', 2)
    return kg_task('3.53', 'minimax', 'Läs spelträdet', intro, [a, b, c], 'Uppåtriktad triangel är MAX och nedåtriktad är MIN.', ['begrepp', 'procedur'], 1)


def t354():
    vals = [[4, 9], [4, 6]]
    assert A.minimax(vals, True) == 4
    intro = fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A och B.') + MM
    a = num('Vilket värde får A?', [step('A är en MIN-nod', 'A = min(4, 9) = 4.')], 4, 'MIN väljer minsta värdet.', 1)
    b = mc('A och B får samma värde. Spelar det någon roll för MAX vilket av dragen MAX väljer?', 'Nej, båda garanterar 4',
           'A = 4 och B = min(4, 6) = 4. Om MIN spelar så bra som möjligt slutar båda dragen med 4.',
           [('Nej, båda dragen garanterar värdet 4', True, 'Minimaxvärdet är detsamma.'),
            ('Ja, A är bättre eftersom lövet 9 finns där', False, 'MIN väljer aldrig 9 när 4 finns.'),
            ('Ja, B är bättre eftersom 6 är större än 4', False, 'MIN väljer 4 även i B.'),
            ('Det går inte att säga utan fler löv', False, 'Alla löv syns, så båda värdena är kända.')],
           'Vad väljer MIN i A och i B?', 3)
    return kg_task('3.54', 'minimax', 'Två lika bra drag', intro, [a, b], 'Jämför vad MIN väljer under varje drag.', ['procedur', 'resonemang'])


def t355():
    vals = [[[6, 2], [3, 9]], [[5, 7], [8, 4]]]
    assert A.minimax(vals, False) == 3
    intro = fig(vals, False, 'Spelträd med MIN i roten, MAX-noderna A och B och MIN-noderna C, D, E och F.', leaf_names=False) + MM
    a = num('Vilket värde får D?', [step('D är en MIN-nod', 'D = min(3, 9) = 3.')], 3, 'Vilken triangel har D?', 1)
    b = num('Vilket värde får B?', [step('E och F är MIN-noder', 'E = min(5, 7) = 5. F = min(8, 4) = 4.'), step('B är en MAX-nod', 'B = max(5, 4) = 5.')], 5,
            'Bestäm E och F först.', 2)
    c = num('Vilket värde får roten?', [step('A', 'C = min(6, 2) = 2. D = 3. A = max(2, 3) = 3.'), step('Roten är en MIN-nod', 'R = min(3, 5) = 3.')], 3,
            'Bestäm A på samma sätt som B.', 2)
    return kg_task('3.55', 'minimax', 'MIN i roten, tre nivåer', intro, [a, b, c], 'Växla mellan min och max för varje nivå.', ['procedur'])


# ======================================================================== beskärning med stöd

AB = p('Spelträdet söks igenom med alfa–beta-beskärning (vänster gren först).')


def t356():
    vals = [[5, 8], [3, 9]]
    intro = fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A och B. Löven heter L1–L4.') + AB
    a = mc('Vad betyder det att en gren beskärs?', 'Grenen behöver inte undersökas',
           'Man har redan sett tillräckligt för att veta att grenen inte kan ändra rotens val.',
           [('Grenen undersöks inte, eftersom den inte kan ändra rotens val', True, 'Det sparar arbete utan att ändra svaret.'),
            ('Grenen tas bort ur spelet så att ingen spelare kan välja den', False, 'Draget finns kvar i spelet. Det är bara sökningen som hoppar över det.'),
            ('Grenen får värdet 0', False, 'Beskurna löv får inget värde alls.'),
            ('Grenen undersöks sist', False, 'En beskuren gren undersöks inte alls.')], 'Vad sparar beskärning?', 1)
    b = mc('Ändrar beskärningen rotens värde jämfört med vanlig minimax?', 'Bara grenar som inte påverkar svaret hoppas över',
           'Bara grenar som inte kan påverka rotens val hoppas över. Därför blir värdet detsamma.',
           [('Nej, rotens värde blir detsamma', True, 'Alfa–beta ger samma svar som minimax, med mindre arbete.'),
            ('Ja, värdet blir alltid lägre', False, 'Om värdet ändrades skulle beskärningen ge fel svar.'),
            ('Ja, värdet blir alltid högre', False, 'Värdet ändras inte.'), ('Det beror på hur många löv som beskärs', False, 'Antalet beskurna löv påverkar bara arbetet.')],
           'Vilka grenar är det tillåtet att hoppa över?', 1)
    return kg_task('3.56', 'alfa_beta', 'Vad är beskärning?', intro, [a, b], 'Beskärning hoppar bara över grenar som inte kan ändra svaret.', ['begrepp'], 1)


def t357():
    vals = [[5, 8], [3, 9]]
    r = T.build(vals, True)
    v, ev, cuts, notes = T.alphabeta(r)
    assert v == 5 and T.pruned_leaves(cuts) == ['L4']
    intro = (fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A och B. Löven heter L1–L4.') + AB +
             p('A är redan undersökt och har värdet 5. Sökningen har just utvärderat B:s första löv, L3 = 3.'))
    a = mc('Kan B få ett värde som är större än 3?', 'B är en MIN-nod och blir högst 3',
           'B är en MIN-nod. MIN väljer 3 eller något ännu mindre, så B blir högst 3.',
           [('Nej, B blir högst 3', True, 'MIN väljer aldrig något större än det minsta värdet den redan har.'),
            ('Ja, om L4 är större än 3', False, 'Ett större L4 väljs inte av MIN, så B blir ändå 3.'),
            ('Ja, B blir 9', False, 'MIN väljer det minsta värdet, inte det största.'), ('Det går inte att säga', False, 'MIN kan bara välja 3 eller mindre.')],
           'Väljer MIN största eller minsta värdet?', 3)
    b = mc('Behöver lövet L4 undersökas?', 'B ≤ 3 är sämre för MAX än A = 5',
           'Roten kan redan få 5 via A. B kan som mest ge 3. Vad L4 än är väljer roten A, så L4 kan hoppas över.',
           [('Nej, B kan ändå inte bli bättre än A för MAX', True, 'B ≤ 3 och A = 5. L4 kan inte ändra rotens val.'),
            ('Ja, L4 kan vara 100', False, 'Även om L4 = 100 väljer MIN 3 i B.'),
            ('Ja, alla löv måste alltid undersökas', False, 'Det gäller vanlig minimax, inte alfa–beta.'),
            ('Nej, eftersom L4 ligger längst till höger', False, 'Placeringen avgör inte. Det är jämförelsen mellan 3 och 5.')],
           'Jämför det bästa B kan ge med A:s värde.', 3)
    c = num('Vilket värde får roten?', [step('Jämför', 'A = 5 och B är högst 3. Roten väljer A.')], 5, 'Roten väljer det största värdet.', 1)
    return kg_task('3.57', 'alfa_beta', 'Kan B slå A?', intro, [a, b, c], 'En MIN-nod blir aldrig större än sitt minsta värde hittills.', ['procedur', 'begrepp'])


def t358():
    vals = [[4, 2], [6, 1]]
    r = T.build(vals, False)
    v, ev, cuts, notes = T.alphabeta(r)
    assert v == 4 and T.pruned_leaves(cuts) == ['L4']
    intro = (fig(vals, False, 'Spelträd med MIN i roten och MAX-noderna A och B. Löven heter L1–L4.') + AB +
             p('A är redan undersökt och har värdet 4. Sökningen har just utvärderat B:s första löv, L3 = 6.'))
    a = num('B är en MAX-nod. Vilket är det minsta värde B kan få?', [step('MAX väljer största värdet', 'B har redan 6 att välja, så B blir minst 6.')], 6,
            'Kan MAX välja något sämre än 6 när 6 finns?', 3)
    b = mc('Behöver lövet L4 undersökas?', 'B ≥ 6 är sämre för MIN än A = 4',
           'Roten är en MIN-nod och har redan 4 via A. B blir minst 6, vilket är sämre för MIN. Roten väljer A vad L4 än är.',
           [('Nej, roten väljer A ändå', True, 'B ≥ 6 är större än A = 4, och MIN vill ha lågt värde.'),
            ('Ja, L4 kan vara mindre än 4', False, 'Även om L4 är litet väljer MAX i B värdet 6.'),
            ('Ja, för att B ska få ett exakt värde', False, 'Rotens val beror inte på B:s exakta värde.'),
            ('Nej, eftersom löv med låga tal aldrig undersöks', False, 'Lövets värde är okänt innan det undersöks.')],
           'Jämför det minsta B kan bli med A.', 3)
    c = num('Vilket värde får roten?', [step('Jämför', 'A = 4 och B är minst 6. MIN i roten väljer A.')], 4, 'Roten väljer det minsta värdet.', 1)
    return kg_task('3.58', 'alfa_beta', 'Kan B bli bättre för MIN?', intro, [a, b, c], 'En MAX-nod blir aldrig mindre än sitt största värde hittills.', ['procedur', 'begrepp'])


def t359():
    vals = [[6, 7], [2, 8]]
    r = T.build(vals, True)
    v, ev, cuts, notes = T.alphabeta(r)
    assert v == 6 and T.pruned_leaves(cuts) == ['L4']
    intro = fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A och B. Löven heter L1–L4.') + AB
    a = num('Vilket värde får A?', [step('A är en MIN-nod', 'A = min(6, 7) = 6.')], 6, 'MIN väljer minsta värdet.', 1)
    b = mc('Vilket löv kan hoppas över?', 'L4',
           'Efter A vet roten att den kan få 6. B:s första löv är 2, så B blir högst 2. Då spelar L4 ingen roll.',
           [('L1', False, 'L1 behövs för att bestämma A.'), ('L2', False, 'L2 behövs för att bestämma A, eftersom A = min(6, 7).'),
            ('L3', False, 'L3 måste undersökas. Det är den som visar att B blir högst 2.'),
            ('L4', True, 'B kan inte bli större än 2, så L4 kan inte ändra rotens val.')], 'Undersök A först. Vad visar B:s första löv?', 3)
    return kg_task('3.59', 'alfa_beta', 'Vilket löv kan hoppas över?', intro, [a, b], 'Jämför B:s första löv med A:s värde.', ['procedur'])


def t360():
    vals_a = [[5, 6], [3, 9]]
    vals_b = [[5, 6], [9, 3]]
    pa = T.pruned_leaves(T.alphabeta(T.build(vals_a, True))[2])
    pb = T.pruned_leaves(T.alphabeta(T.build(vals_b, True))[2])
    assert pa == ['L4'] and pb == []
    intro = (fig(vals_a, True, 'Spelträd med MAX i roten och MIN-noderna A och B. Löven heter L1–L4.') + AB +
             p('Tänk dig också att B:s två löv byter plats, så att B:s första löv är 9 och det andra är 3.'))
    a = num('Hur många av B:s löv behöver undersökas i trädet som det ser ut i bilden?',
            [step('A = 5', 'A = min(5, 6) = 5.'), step('B:s första löv är 3', 'B blir högst 3, mindre än 5. B:s andra löv kan hoppas över.')], 1,
            'Jämför B:s första löv med A.', 3)
    b = num('Hur många av B:s löv behöver undersökas om de byter plats?',
            [step('B:s första löv är 9', 'B kan fortfarande bli upp till 9, alltså bättre än A. Sökningen måste fortsätta.'),
             step('B:s andra löv är 3', 'Nu vet man att B = 3. Båda löven har undersökts.')], 2, 'Kan B fortfarande slå A efter lövet 9?', 3)
    c = mc('Vad visar jämförelsen?', 'Ordningen påverkar beskärningen',
           'Rotens värde blir 5 i båda fallen, men hur mycket som kan hoppas över beror på i vilken ordning löven undersöks.',
           [('Ordningen påverkar hur mycket som kan beskäras, men inte rotens värde', True, 'Bra ordning ger mer beskärning.'),
            ('Ordningen ändrar rotens värde', False, 'Roten får 5 i båda fallen.'),
            ('Beskärning fungerar bara när det lägsta lövet ligger sist', False, 'Tvärtom: när ett lågt löv kommer först i B kan resten hoppas över.'),
            ('Ordningen spelar ingen roll', False, 'Med 3 först kan ett löv hoppas över, med 9 först inget.')], 'Jämför svaren i a) och b).', 3)
    return kg_task('3.60', 'alfa_beta', 'Samma löv i olika ordning', intro, [a, b, c], 'Ett lågt löv tidigt i en MIN-nod ger beskärning.', ['procedur', 'begrepp'])


def t361():
    vals = [[4, 6], [1, 5], [2, 3]]
    r = T.build(vals, True)
    v, ev, cuts, notes = T.alphabeta(r)
    assert v == 4 and T.pruned_leaves(cuts) == ['L4', 'L6'] and len(ev) == 4
    intro = (fig(vals, True, 'Spelträd med MAX i roten och MIN-noderna A, B och C med två löv var. Löven heter L1–L6.') + AB +
             p('A undersöks först och får värdet 4.'))
    a = num('Vilket värde får A?', [step('A är en MIN-nod', 'A = min(4, 6) = 4.')], 4, 'MIN väljer minsta värdet.', 1)
    b = num('Hur många löv behöver undersökas totalt?',
            [step('A undersöks helt', 'L1 och L2.'), step('B och C:s första löv', 'L3 = 1 och L5 = 2 är båda mindre än 4. B och C kan därför inte slå A, och L4 och L6 hoppas över.'),
             step('Räkna', 'L1, L2, L3 och L5: 4 löv.')], 4, 'Jämför B:s och C:s första löv med A:s värde.', 3)
    return kg_task('3.61', 'alfa_beta', 'Hur många löv behövs?', intro, [a, b], 'När en MIN-nods första löv redan är sämre än A kan resten av noden hoppas över.', ['procedur'])


def build_all():
    return [t350(), t351(), t352(), t353(), t354(), t355(), t356(), t357(), t358(), t359(), t360(), t361()]


def main():
    with open(BANK, encoding='utf-8', newline='') as fh:
        src = fh.read()
    i, j = src.index('['), src.rindex(']')
    bank = json.loads(src[i:j + 1])
    nya = build_all()
    ids = {u['id'] for u in nya}
    bank = [u for u in bank if u['id'] not in ids] + nya
    assert len({u['id'] for u in bank}) == len(bank)
    with open(BANK, 'w', encoding='utf-8', newline='') as fh:
        fh.write(src[:i] + json.dumps(bank, ensure_ascii=False, indent=2) + src[j + 1:])
    print(f'{len(bank)} uppgifter, varav {len(nya)} nya i denna omgång.')


if __name__ == '__main__':
    main()
