import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
by_id = {q['id']: q for q in bank}
prefix = ('<ol class="facit-steglista" role="list"><li><p class="facit-metod">'
          '<strong>Tänk så här:</strong> Rita figuren och märk ut givna längder och vinklar.</p></li>'
          '<li><p class="facit-metod">Dela vid behov upp den i standardfigurer innan du använder en formel.</p></li></ol>')
suffix = ('<ol class="facit-steglista" role="list"><li><p class="facit-not">'
          '<strong>Kontroll och insikt:</strong> Kontrollera enheten: längd, area och volym '
          'ska få första, andra respektive tredje potens på längdenheten.</p></li></ol>')

solutions = [
    r'\(x+1\) är positiv på hela intervallet. \(\int_0^2(x+1)\,dx=[x^2/2+x]_0^2=4\). Integralen är därför också den geometriska arean, \(4\).',
    r'Grafen ligger under x-axeln för \(-1&lt;x&lt;0\) och över den för \(0&lt;x&lt;1\). \(\int_{-1}^1x\,dx=[x^2/2]_{-1}^1=0\). De två trianglarnas areor är vardera \(1/2\), så den geometriska arean är \(1\), inte \(0\).',
    r'\(\sin x\) är icke-negativ på \([0,\pi]\). \(\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi=2\). Integralen är därför också den geometriska arean, \(2\).',
    r'\(\sin x\) är positiv på \((0,\pi)\) och negativ på \((\pi,2\pi)\). Delintegralerna är \(2\) respektive \(-2\), så integralen är \(0\). Den geometriska arean är \(2+2=4\).',
]
def facit(text):
    return '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list"><li><p>'+text+'</p></li></ol></div>'

ids = ['3.11', '3.461', '3.473', '3.475', '3.206', '3.179']
for task_id in ids:
    q = by_id[task_id]
    start = raw.index(f'    "id": "{task_id}"')
    end = raw.index('\n  },', start)
    segment = raw[start:end]
    changes = []
    if task_id == '3.11':
        assert len(q['spelDelar']) == len(solutions)
        all_s = '<div class="facit-v2 facit-stegvis">'+''.join(
            f'<div class="facit-del"><span class="facit-mark">{chr(97+i)})</span><div class="facit-arbete">{facit(s)}</div></div>'
            for i,s in enumerate(solutions))+'</div>'
        changes.append((q['s'], all_s))
        changes.extend((d['s'],facit(s)) for d,s in zip(q['spelDelar'],solutions))
        old_intro = 'Avgör om den bestämda integralen direkt ger en geometrisk area eller en tecknad area, och beräkna värdet.'
        new_intro = 'Beräkna integralen. Är värdet också den geometriska arean mellan grafen och x-axeln på intervallet?'
        changes.extend([(q['t'],q['t'].replace(old_intro,new_intro)),
                        (q['spelIntro'],q['spelIntro'].replace(old_intro,new_intro)),
                        (q['ledtrad'], '<p>Undersök var grafen ligger över eller under x-axeln. Areor under axeln bidrar negativt till integralen.</p>')])
    else:
        old = q['s']
        assert old.count(prefix) == old.count(suffix) == 1
        changes.append((old,old.replace(prefix,'').replace(suffix,'')))
    for old,new in changes:
        assert old != new
        before,after=json.dumps(old,ensure_ascii=False),json.dumps(new,ensure_ascii=False)
        assert segment.count(before)==1,(task_id,old[:60],segment.count(before))
        segment=segment.replace(before,after,1)
    raw=raw[:start]+segment+raw[end:]
p.write_text(raw,encoding='utf-8')
