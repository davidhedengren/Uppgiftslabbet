import json
from pathlib import Path

p = Path(__file__).resolve().parent.parent / 'uppgiftermato2.js'
raw = p.read_text(encoding='utf-8')
bank = json.loads(raw[raw.index('['):raw.rindex(']')+1])
by_id = {q['id']:q for q in bank}
prefix = ('<ol class="facit-steglista" role="list"><li><p class="facit-metod">'
          '<strong>Tänk så här:</strong> Rita figuren och märk ut givna längder och vinklar.</p></li>'
          '<li><p class="facit-metod">Dela vid behov upp den i standardfigurer innan du använder en formel.</p></li></ol>')
suffix = ('<ol class="facit-steglista" role="list"><li><p class="facit-not">'
          '<strong>Kontroll och insikt:</strong> Kontrollera enheten: längd, area och volym '
          'ska få första, andra respektive tredje potens på längdenheten.</p></li></ol>')
ids = ['2.26','2.74','2.100','2.179','2.183','2.248','2.258']
for task_id in ids:
    q=by_id[task_id]; old=q['s']
    assert old.count(prefix)==old.count(suffix)==1
    new=old.replace(prefix,'').replace(suffix,'')
    if task_id=='2.179':
        new = (r'<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">'
               r'<li><p><strong>Derivera arean.</strong> Eftersom \(A=\pi r^2\) och radien beror på tiden ger kedjeregeln '
               r'\[\frac{dA}{dt}=2\pi r\frac{dr}{dt}.\]</p></li>'
               r'<li><p><strong>Sätt in värdena i centimeter.</strong> Med \(r=75\) cm och \(dr/dt=18\) cm/år får vi '
               r'\[\frac{dA}{dt}=2\pi\cdot75\cdot18=2700\pi.\]</p></li>'
               r'<li><p><strong>Svar:</strong> Arean ökar med \(2700\pi\approx8500\) cm²/år.</p></li></ol></div>')
    start=raw.index(f'    "id": "{task_id}"'); end=raw.index('\n  },',start)
    segment=raw[start:end]; before=json.dumps(old,ensure_ascii=False); after=json.dumps(new,ensure_ascii=False)
    assert segment.count(before)==1
    raw=raw[:start]+segment.replace(before,after,1)+raw[end:]
p.write_text(raw,encoding='utf-8')
