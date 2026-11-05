"""GeoGebra-skärmbilder i Ma2-statistikfacit 4.343–4.347 (5 nov 2026).

Det första steget i varje delkort ("Undersök/Mata in värdena i GeoGebra") ersätts med bildstegen
(kalkylblad, inmatning, Envariabelanalys, Σx). Uppgiftens egna resonemangssteg behålls och får en
bild av den rad i statistikpanelen som steget använder. Rader som skulle avslöja senare delars svar
döljs i delkortens bilder.

  python tools/geogebra-statistik-serie2-2026-11-05.py spec > spec.json
  python tools/geogebra-statistik-serie2-2026-11-05.py bygg <logg.json> [--skriv]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
_s = importlib.util.spec_from_file_location('serie1', Path(__file__).with_name('geogebra-statistik-serie-2026-11-05.py'))
s1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(s1)
li, img, sv, num, punktnot, gg_block = s1.li, s1.img, s1.sv, s1.num, s1.punktnot, s1.gg_block
BANK = s1.BANK
ALLA = s1.ALLA

# Datamängder: slug -> (värden, beskrivning i rubriker, enhet)
DATA = {
    '4-343': ([19.8, 20, 20, 20.1, 20.4], 'de fem skruvlängderna', 'mm'),
    '4-344': ([2, 2, 2, 2, 2], 'de fem paketens vikter', 'kg'),
    '4-345': ([1, 2, 2, 3, 4, 4, 5], 'besökarnas sju betyg', ''),
    '4-346-a': ([18, 20, 20, 20, 22], 'maskin A:s längder', 'mm'),
    '4-346-b': ([16, 20, 20, 20, 24], 'maskin B:s längder', 'mm'),
    '4-347': ([20, 20, 30, 30, 40, 400], 'de sex gåvorna', 'kr'),
}
MINMAX = ['Min', 'Max']
# Statistikbilder per datamängd: namn -> (inringade rader, synliga rader eller None = alla)
BILDER = {
    '4-343': {'median': (['Median'], ['n', 'Median']), 'medel-s': (['Medel', 's'], [r for r in ALLA if r not in MINMAX]), 'min-max': (MINMAX, None)},
    '4-344': {'median': (['Median'], ['n', 'Median']), 'medel-s': (['Medel', 's'], [r for r in ALLA if r not in MINMAX]), 'min-max': (MINMAX, None)},
    '4-345': {'median': (['Median'], ['n', 'Median']), 'medel-s': (['Medel', 's'], [r for r in ALLA if r not in MINMAX]), 'min-max': (MINMAX, None)},
    '4-346-a': {'medel-s': (['Medel', 's'], None)},
    '4-346-b': {'medel-s': (['Medel', 's'], None)},
    '4-347': {'median': (['Median'], ['n', 'Median']), 'medel-s': (['Medel', 's'], None), 'median-medel': (['Median', 'Medel'], None)},
}
STOLP = {'4-343', '4-344', '4-345', '4-347'}

# Per uppgift och del: (datamängd, med Σx-steg, [(bild, rader att nämna)] till steget efter GeoGebra-steget)
DELAR = {
    '4.343': {'a': ('4-343', True, [('median', ['Median'])]), 'b': ('4-343', False, [('stolp', None)]),
              'c': ('4-343', True, [('medel-s', None)]), 'd': ('4-343', True, [('min-max', MINMAX)])},
    '4.344': {'a': ('4-344', True, [('median', ['Median'])]), 'b': ('4-344', False, [('stolp', None)]),
              'c': ('4-344', True, [('medel-s', None)]), 'd': ('4-344', True, [('min-max', MINMAX)])},
    '4.345': {'a': ('4-345', True, [('median', ['Median'])]), 'b': ('4-345', False, [('stolp', None)]),
              'c': ('4-345', True, [('medel-s', None)]), 'd': ('4-345', True, [('min-max', MINMAX)])},
    '4.346': {'a': ('4-346-a', True, [('medel-s', None)]), 'b': ('4-346-b', True, [('medel-s', None)]),
              'c': (None, None, [('4-346-a:medel-s', ['s']), ('4-346-b:medel-s', ['s'])])},
    '4.347': {'a': ('4-347', True, [('median', ['Median'])]), 'b': ('4-347', False, [('stolp', None)]),
              'c': ('4-347', True, [('medel-s', None)]), 'd': ('4-347', True, [('median-medel', ['Median', 'Medel'])])},
}


def spec():
    jobs = []
    for sl, (vals, _, _) in DATA.items():
        jobs.append({'slug': sl, 'values': vals, 'stolp': sl in STOLP,
                     'stats': [{'name': n, 'frame': f, **({'show': s} if s else {})} for n, (f, s) in BILDER[sl].items()]})
    return {'jobs': jobs}


def statbild(logg, sl, namn, rader):
    st = logg[sl]['stats']
    beskr = DATA[sl][1]
    if namn == 'stolp':
        return img(f'geogebra-{sl}-stolp.png', f'Stolpdiagram över {beskr}. De högsta staplarna är inringade.', 560)
    frame = BILDER[sl][namn][0]
    vis = rader or frame
    txt = f'<p>I GeoGebras statistikpanel för {beskr} står ' + ' och '.join(f'{r} = {st[r]}' for r in vis) + '.</p>'
    txt += punktnot(*[st[r] for r in vis])
    alt = f'Statistikpanelen för {beskr} med ' + ' och '.join(f'{r} = {st[r]}' for r in frame) + ' inringat.'
    return txt + img(f'geogebra-{sl}-{namn}.png', alt, 340)


def bygg(logg, src):
    data = json.loads(src[src.index('['):src.rindex(']') + 1])
    by = {u['id']: u for u in data}
    byten = []
    for uid, delar in DELAR.items():
        u = by[uid]
        nya, huvud = {}, {}
        for d in u['spelDelar']:
            k = d['etikett']
            sl, sigma, bilder = delar[k]
            lis = re.findall(r'<li>.*?</li>', d['s'])
            svar = s1.svarsrad(d['s'])
            # Det första steget är det gamla textsteget för GeoGebra; det ska nämna rätt värden.
            assert 'GeoGebra' in lis[0], (uid, k)
            extra = ''.join(statbild(logg, *(b.split(':') if ':' in b else (sl, b)), r) for b, r in bilder)
            rest = list(lis[1:])
            rest[0] = rest[0][:-5] + extra + '</li>'
            if sl:
                vals, beskr, _ = DATA[sl]
                listtxt = sv('; '.join('%g' % v for v in vals))
                assert listtxt in lis[0], (uid, k, listtxt)  # facit nämnde samma värden
                block = gg_block(sl.replace('-', '.', 1), beskr, listtxt, len(vals), vals, sigma)
                ny_del = ''.join([block] + rest)
                if k == 'a' or (uid == '4.346' and k == 'b'):
                    huvud[k] = ny_del
                else:
                    huvud[k] = li(f'Använd analysen av {beskr} från a)',
                                  '<p>Värdena är redan inskrivna och analyserade med Envariabelanalys i a).</p>') + ''.join(rest)
            else:
                ny_del = lis[0] + ''.join(rest)
                huvud[k] = ny_del
            nya[k] = ('<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">' + ny_del + '</ol>' + svar + '</div>', svar)
            byten.append((d['s'], nya[k][0]))
        ny_huvud = '<div class="facit-v2 facit-stegvis">' + ''.join(
            '<div class="facit-del"><span class="facit-mark">%s)</span><div class="facit-arbete">'
            '<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list">%s</ol>%s</div></div></div>'
            % (k, huvud[k], nya[k][1]) for k in [d['etikett'] for d in u['spelDelar']]) + '</div>'
        byten.append((u['s'], ny_huvud))
    for gammal, ny in byten:
        g = json.dumps(gammal, ensure_ascii=False)
        assert src.count(g) == 1, gammal[:80]
        src = src.replace(g, json.dumps(ny, ensure_ascii=False))
    return src


def main():
    if sys.argv[1] == 'spec':
        print(json.dumps(spec(), ensure_ascii=False, indent=1))
        return
    logg = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
    src = bygg(logg, BANK.read_text(encoding='utf-8'))
    if '--skriv' in sys.argv:
        with open(BANK, 'w', encoding='utf-8', newline='') as f:
            f.write(src)
    print('ok', ' '.join(DELAR))


if __name__ == '__main__':
    main()
