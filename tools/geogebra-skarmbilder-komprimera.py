"""Komprimerar GeoGebra-skärmbilder: skalar till 1,5x CSS-storlek och sparar med
en anpassad palett. Användning: python tools/geogebra-skarmbilder-komprimera.py fil.png ...
"""
import sys
from PIL import Image

SKALA = 0.75  # bilderna tas med deviceScaleFactor 2 -> 1,5x CSS-pixlar


def komprimera(fil):
    bild = Image.open(fil).convert('RGB')
    w, h = bild.size
    bild = bild.resize((round(w * SKALA), round(h * SKALA)), Image.LANCZOS)
    bild = bild.quantize(colors=96, method=Image.MEDIANCUT, dither=Image.NONE)
    bild.save(fil, optimize=True)
    return bild.size


if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f, komprimera(f))
