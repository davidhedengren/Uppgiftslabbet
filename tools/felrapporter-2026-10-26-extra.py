"""Kompletterar 1531-rättningen; behåller dess figurer, svar och precisionsregler.

Fälten i JSON-filen är manuellt författade/granskade. Kör aldrig om verktyget
utan att först jämföra dessa ID:n med nyare granskningsbeslut.
"""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
patches=json.loads(Path(__file__).with_suffix('.json').read_text())
for file,objects in patches.items():
 path=root/file;source=path.read_text()
 for id,fields in objects.items():
  pos=source.index('"id": "'+id+'"');start=source.rfind('{',0,pos)
  obj,n=json.JSONDecoder().raw_decode(source[start:]);assert obj['id']==id
  obj.update(fields)
  indent=source[source.rfind('\n',0,start)+1:start]
  encoded=json.dumps(obj,ensure_ascii=False,indent=2).replace('\n','\n'+indent)
  source=source[:start]+encoded+source[start+n:]
 path.write_text(source)
 print(file,','.join(objects))
