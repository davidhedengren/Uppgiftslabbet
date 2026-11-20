"""Engångsfix 2026-11-20: i 2.510 och 7.02 hamnade felkommentarerna förskjutna ett steg (None på fel plats
i ma1_resten.py). Tar bort kommentarerna i de två alternativlistorna så att ma1_resten.py kan köras om."""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from sprakverktyg import Bank

b = Bank('ma1')
for id_ in ['2.510', '7.02']:
    t = b.text(id_)
    alt = b.obj(id_)['alternativ']
    gammal = json.dumps(alt, ensure_ascii=False)
    assert t.count(gammal) == 1, (id_, t.count(gammal))
    ny = json.dumps([{'txt': a['txt'], 'ratt': a['ratt']} for a in alt], ensure_ascii=False)
    b.byte[id_] = t.replace(gammal, ny)
print(b.spara(), 'objekt skrivna')
