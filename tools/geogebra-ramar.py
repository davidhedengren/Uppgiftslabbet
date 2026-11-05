"""Ritar inramningar på en GeoGebra-skärmbild och beskär den (tools/geogebra-statistik-bilder.js).
Argument: fil, ramar som JSON [[x,y,b,h], ...] och beskärning [x,y,b,h], allt i CSS-pixlar (bilden är tagen med skala 2).
Bilden sparas med begränsad färgpalett så att den blir liten."""
import json, sys
from PIL import Image, ImageDraw

fil, ramar, klipp = sys.argv[1], json.loads(sys.argv[2]), json.loads(sys.argv[3])
S = 2
bild = Image.open(fil).convert('RGB')
rita = ImageDraw.Draw(bild)
for nr, r in enumerate(ramar, 1):
    if not r:
        continue
    x, y, b, h = [v * S for v in r]
    m = 5
    rita.rounded_rectangle([x - m, y - m, x + b + m, y + h + m], radius=10, outline=(214, 40, 40), width=5)
x, y, b, h = [int(round(v * S)) for v in klipp]
bild = bild.crop((x, y, min(bild.width, x + b), min(bild.height, y + h)))
bild = bild.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
bild.save(fil, optimize=True)
