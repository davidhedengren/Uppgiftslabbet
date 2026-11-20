"""Häftet ”Färdighetsträning – Newtons andra lag” i ny layout (2026-11-20).

Underlag: lärarens skannade häfte (15 uppgifter, facit och lösning av exempel 2 och 6). Figurerna ritas om med
tools/newton2_klossar.py, och facit räknas om med g = 9,82 m/s², F = 10 N och m = 1,0 kg. Det gamla facit hade fel i
12 av 15 uppgifter (se agent/FY1_KOPPLADE_KLOSSAR_2026-11-20.md).

  python tools/bygg-hafte-newton2-2026-11-20.py      skriver material/fysik1/*.html och, med Node + Playwright, *.pdf
"""
import json
import math
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).parent))
from newton2_klossar import Kropp, System, figur, frilagg, latex_a, latex_lin, G  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
UT = ROOT / 'material' / 'fysik1'
NAMN = 'Fardighetstraning_Newtons_andra_lag'
F, M = 10.0, 1.0


def et(k):
    i = '<tspan font-style="italic">m</tspan>'
    return i if k == 1 else f'{k}{i}'


def K(k, plats, fr=0.0, fn='f'):
    return Kropp(k, plats, fr, fn, et(k))


UPPG = [
    ('Utan friktion', '', System(bord=[K(1, 'B')], F=F, golv=True)),
    ('Utan friktion', '', System(bord=[K(1, 'B'), K(2, 'B')], F=F, golv=True)),
    ('Utan friktion', '', System(bord=[K(1, 'B'), K(2, 'B'), K(3, 'B')], F=F, golv=True)),
    ('Med friktion', 'Friktionskraften på klossen är 1,0 N.', System(bord=[K(1, 'B', 1.0)], F=F, golv=True)),
    ('Med friktion', 'Friktionskraften är 1,0 N på den lätta klossen och 2,0 N på den tunga.',
     System(bord=[K(1, 'B', 1.0, 'f_1'), K(2, 'B', 2.0, 'f_2')], F=F, golv=True)),
    ('Utan friktion', '', System(vanster=[K(1, 'V')], hoger=[K(2, 'H')])),
    ('Utan friktion', '', System(vanster=[K(1, 'V')], hoger=[K(2, 'H'), K(4, 'H')])),
    ('Utan friktion', '', System(bord=[K(2, 'B')], hoger=[K(1, 'H')])),
    ('Utan friktion', '', System(bord=[K(2, 'B')], hoger=[K(1, 'H'), K(3, 'H')])),
    ('Utan friktion', '', System(bord=[K(3, 'B'), K(2, 'B')], hoger=[K(1, 'H')])),
    ('Med friktion', 'Friktionskraften på klossen på bordet är 1,0 N.', System(bord=[K(1, 'B', 1.0)], hoger=[K(2, 'H')])),
    ('Med friktion', 'Friktionskraften på klossen på bordet är 1,0 N.',
     System(bord=[K(1, 'B', 1.0)], hoger=[K(3, 'H'), K(2, 'H')])),
    ('Utan friktion', '', System(vanster=[K(3, 'V')], hoger=[K(1, 'H')], tomtbord=True)),
    ('Utan friktion', '', System(vanster=[K(1, 'V')], bord=[K(2, 'B')], hoger=[K(3, 'H')])),
    ('Med friktion', 'Friktionskraften på klossen på bordet är 4,0 N.',
     System(vanster=[K(2, 'V')], bord=[K(4, 'B', 4.0)], hoger=[K(3, 'H')])),
]

# Kontrollräkning oberoende av modellen (g = 9,82, m = 1,0 kg, F = 10 N): (a, [S...])
g = G
KONTROLL = {
    1: (10.0, []), 2: (10 / 3, [10 / 3]), 3: (10 / 6, [10 / 6, 5.0]), 4: (9.0, []), 5: (7 / 3, [10 / 3]),
    6: (g / 3, [4 * g / 3]), 7: (5 * g / 7, [12 * g / 7, 8 * g / 7]), 8: (g / 3, [2 * g / 3]),
    9: (2 * g / 3, [4 * g / 3, g]), 10: (g / 6, [g / 2, 5 * g / 6]), 11: ((2 * g - 1) / 3, [(2 * g - 1) / 3 + 1]),
    12: ((5 * g - 1) / 6, [(5 * g - 1) / 6 + 1, 2 * (g - (5 * g - 1) / 6)]), 13: (g / 2, [1.5 * g]),
    14: (g / 3, [4 * g / 3, 2 * g]), 15: ((g - 4) / 9, [2 * (g + (g - 4) / 9), 3 * (g - (g - 4) / 9)]),
}


def tva(v):
    """Två värdesiffror med decimalkomma (10 skrivs 10)."""
    if v == 0:
        return '0'
    e = math.floor(math.log10(abs(v)))
    d = max(0, 1 - e)
    s = f'{round(v, d):.{d}f}'
    return s.replace('.', ',')


def svar():
    ut = []
    for n, (_, _, s) in enumerate(UPPG, 1):
        a, S = s.los()
        ka, kS = KONTROLL[n]
        assert abs(abs(a) - ka) < 1e-9 and all(abs(x - y) < 1e-9 for x, y in zip(S, kS)) and len(S) == len(kS), n
        tal, nn, Ssym = s.symbolisk()
        asym = latex_a(tal, nn).lstrip('-')
        ut.append(dict(n=n, a=abs(a), S=S, asym=asym, Ssym=[latex_lin(x) for x in Ssym], vanster=a < 0))
    return ut


CSS = """
@page { size: A4; margin: 13mm 13mm 15mm 13mm; }
:root { --navy:#1d3954; --teal:#22808f; --orange:#d9822b; --ink:#1f2d3a; --mute:#5d6b78; --line:#dbe3ec; --bg:#f5f8fb; }
* { box-sizing: border-box; }
body { font-family: Inter, "Segoe UI", Arial, sans-serif; color: var(--ink); font-size: 10.5pt; line-height: 1.45; margin: 0; }
.band { background: linear-gradient(120deg, var(--navy) 0%, #24617a 60%, var(--teal) 100%); color: #fff;
        border-radius: 14px; padding: 16px 22px 18px; margin-bottom: 14px; position: relative; overflow: hidden; }
.band::after { content: ""; position: absolute; right: -40px; top: -60px; width: 220px; height: 220px; border-radius: 50%;
        background: rgba(255,255,255,.08); }
.band .kurs { font-size: 8.5pt; letter-spacing: .14em; text-transform: uppercase; opacity: .85; font-weight: 600; }
.band h1 { font-size: 21pt; margin: 4px 0 2px; font-weight: 800; letter-spacing: -.01em; }
.band .under { font-size: 11pt; opacity: .92; }
.rad { display: grid; grid-template-columns: 1.35fr 1fr; gap: 12px; margin-bottom: 12px; }
.ruta { border: 1px solid var(--line); border-radius: 12px; padding: 11px 14px; background: #fff;
        box-shadow: 0 1px 3px rgba(31,45,58,.06); }
.ruta h2 { font-size: 10.5pt; margin: 0 0 6px; color: var(--navy); text-transform: uppercase; letter-spacing: .08em; }
.ruta.givet { background: var(--bg); }
.steg { margin: 0; padding: 0; list-style: none; counter-reset: s; }
.steg li { counter-increment: s; position: relative; padding-left: 26px; margin: 4px 0; }
.steg li::before { content: counter(s); position: absolute; left: 0; top: 1px; width: 18px; height: 18px; border-radius: 50%;
        background: var(--teal); color: #fff; font-size: 8.5pt; font-weight: 700; text-align: center; line-height: 18px; }
.givna { display: grid; grid-template-columns: auto 1fr; gap: 2px 10px; font-size: 11pt; margin: 4px 0 6px; }
.notis { font-size: 9pt; color: var(--mute); }
.utmaning { border-left: 4px solid var(--orange); background: #fff6ec; border-radius: 0 10px 10px 0; padding: 7px 12px;
        margin-bottom: 12px; font-size: 9.8pt; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.kort { border: 1px solid var(--line); border-radius: 12px; padding: 9px 12px 8px; background: #fff; break-inside: avoid;
        box-shadow: 0 1px 3px rgba(31,45,58,.06); display: flex; flex-direction: column; }
.kort.bred { grid-column: span 2; }
.huvud { display: flex; align-items: center; gap: 8px; margin-bottom: 2px; }
.nr { width: 26px; height: 26px; border-radius: 50%; background: var(--navy); color: #fff; font-weight: 800; font-size: 11pt;
        display: flex; align-items: center; justify-content: center; flex: none; }
.pill { font-size: 8.3pt; font-weight: 700; border-radius: 999px; padding: 2px 9px; letter-spacing: .02em; }
.pill.utan { background: #e3f3ea; color: #23704a; }
.pill.med { background: #fdeedd; color: #a65d16; }
.fr { font-size: 9.3pt; color: var(--ink); margin: 3px 0 0; }
.fig { flex: 1; display: flex; align-items: center; justify-content: center; padding: 4px 0; }
.fig svg { max-height: 190px; width: auto !important; max-width: 100%; }
.sokt { font-size: 9.1pt; color: var(--ink); font-weight: 600; border-top: 1px dashed var(--line); padding-top: 4px; }
.sida { break-before: page; }
h2.rubrik { font-size: 15pt; color: var(--navy); margin: 0 0 4px; }
.ingress { color: var(--mute); margin: 0 0 10px; font-size: 9.6pt; }
table.facit { width: 100%; border-collapse: separate; border-spacing: 0; font-size: 10pt; }
table.facit th { background: var(--navy); color: #fff; text-align: left; padding: 6px 9px; font-size: 9pt; letter-spacing: .04em; }
table.facit th:first-child { border-radius: 8px 0 0 0; } table.facit th:last-child { border-radius: 0 8px 0 0; }
table.facit td { padding: 4px 9px; border-bottom: 1px solid var(--line); vertical-align: top; }
table.facit tr:nth-child(even) td { background: var(--bg); }
td.n { font-weight: 800; color: var(--navy); width: 34px; }
.v { font-weight: 700; } .alg { display: block; color: var(--mute); font-size: 8.8pt; margin-top: 1px; }
.ex { border: 1px solid var(--line); border-radius: 12px; padding: 10px 14px; margin-bottom: 12px; break-inside: avoid; }
.ex h3 { margin: 0 0 6px; font-size: 12pt; color: var(--navy); }
.exsteg { display: grid; grid-template-columns: 62px 1fr; gap: 6px 10px; align-items: start; }
.exsteg .lab { font-weight: 800; color: var(--teal); font-size: 9.5pt; padding-top: 2px; }
.fbd { display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }
.fbd svg { width: 190px !important; }
.mini { display: flex; align-items: center; gap: 14px; margin-bottom: 4px; }
.mini > div:first-child { flex: none; width: 250px; }
.mini svg { width: 250px !important; max-height: 170px; }
.katex { font-size: 1.04em; }
@media print { .kort, .ruta { box-shadow: none; } }
.tips { margin: 0 0 12px; background: #f3f8f4; border-color: #cfe5d6; }
.tips h2 { color: #23704a; }
.nw { white-space: nowrap; }
.tips ul { margin: 0; padding-left: 18px; } .tips li { margin: 3px 0; }
"""


def kort(n, villkor, fr, s, sokt):
    fig = figur(s, f'h{n}', f'Uppgift {n}', Ftext='F')
    bred = ''
    return (f'<div class="kort{bred}"><div class="huvud"><div class="nr">{n}</div><span class="pill '
            f'{"med" if villkor.startswith("Med") else "utan"}">{villkor}</span></div>'
            + (f'<p class="fr">{fr}</p>' if fr else '') + f'<div class="fig">{fig}</div><div class="sokt">{sokt}</div></div>')


def sokt_text(s):
    n = len(s.kedja()) - 1
    if n == 0:
        return 'Bestäm accelerationen.'
    if n == 1:
        return 'Bestäm accelerationen och snörkraften <span class="nw">\\(S\\).</span>'
    return 'Bestäm accelerationen och snörkrafterna <span class="nw">\\(S_1\\) och \\(S_2\\).</span>'


def bygg():
    sv = svar()
    delar = []
    # ---------------- sida 1: inledning och uppgifter
    delar.append(
        '<div class="band"><div class="kurs">Fysik 1 · Kraft och rörelse</div>'
        '<h1>Färdighetsträning – Newtons andra lag</h1><div class="under">Kopplade klossar, snören och trissor</div></div>'
        '<div class="rad"><div class="ruta"><h2>Så här gör du</h2><ol class="steg">'
        '<li><strong>Frilägg</strong> varje kloss och rita ut alla krafter som verkar på den.</li>'
        '<li><strong>Välj positiv riktning</strong> och rita ut den. Hela systemet rör sig åt samma håll längs snöret.</li>'
        '<li><strong>Teckna Newtons andra lag</strong>, \\(F_{\\text{res}}=ma\\), för varje kloss.</li>'
        '<li><strong>Lös ekvationssystemet</strong> och beräkna klossarnas gemensamma acceleration och spännkraften i '
        'varje snöre.</li></ol></div>'
        '<div class="ruta givet"><h2>Givet</h2><div class="givna"><span>\\(F\\)</span><span>\\(=10\\ \\text{N}\\)</span>'
        '<span>\\(m\\)</span><span>\\(=1{,}0\\ \\text{kg}\\)</span><span>\\(g\\)</span><span>\\(=9{,}82\\ \\text{m/s}^2\\)</span>'
        '</div><div class="notis">Snören och trissor är masslösa och trissorna är friktionsfria. Snörena är märkta '
        '\\(S_1\\) och \\(S_2\\) när det finns fler än ett.</div></div></div>')
    korten = [kort(n, v, fr, s, sokt_text(s)) for n, (v, fr, s) in enumerate(UPPG, 1)]
    delar.append(
        '<div class="ruta tips"><h2>Bra att veta</h2><ul>'
        '<li>Klossar som sitter ihop med sträckta snören har <strong>samma accelerationsstorlek</strong>.</li>'
        '<li>Snörkraften är <strong>lika stor i hela snöret</strong>, även där snöret går över en trissa.</li>'
        '<li>Tyngdkraften är \\(F_g=mg\\). En hängande kloss som accelererar nedåt har \\(S&lt;mg\\), och en som '
        'accelererar uppåt har \\(S&gt;mg\\).</li>'
        '<li>Kontrollera svaret: om hela systemet ses som en enda kropp är \\(F_{\\text{res}}=m_{\\text{tot}}\\,a\\), '
        'och snörkrafterna tar ut varandra.</li></ul></div>')
    delar.append('<div class="grid">' + ''.join(korten[:4]) + '</div>')
    delar.append('<div class="grid sida">' + ''.join(korten[4:10]) + '</div>')
    delar.append('<div class="grid sida">' + ''.join(korten[10:]) + '</div>')

    # ---------------- facit
    rader = []
    for r in sv:
        def cell(v, alg, enhet):
            return (f'<span class="v">\\({tva(v).replace(",", "{,}")}\\ \\text{{{enhet}}}\\)</span>'
                    f'<span class="alg">\\(\\displaystyle ={alg}\\)</span>')
        a_txt = cell(r['a'], r['asym'], 'm/s}^2\\text{')
        if r['vanster']:
            a_txt += '<span class="alg">klossen \\(3m\\) sjunker</span>'
        S = r['S'] + [None] * (2 - len(r['S']))
        Ss = r['Ssym'] + [None] * (2 - len(r['Ssym']))
        sc = [cell(v, a, 'N') if v is not None else '<span class="alg">–</span>' for v, a in zip(S, Ss)]
        rader.append(f'<tr><td class="n">{r["n"]}</td><td>{a_txt}</td><td>{sc[0]}</td><td>{sc[1]}</td></tr>')
    delar.append(
        '<div class="sida"><h2 class="rubrik">Facit</h2><p class="ingress">Svaren är avrundade till två värdesiffror och '
        'räknade med \\(g=9{,}82\\ \\text{m/s}^2\\). Under varje svar står det algebraiska uttrycket. '
        '\\(f\\), \\(f_1\\) och \\(f_2\\) är friktionskrafterna. Accelerationen är klossarnas gemensamma accelerationsstorlek. '
        'Med ett snöre står snörkraften under \\(S_1\\).</p>'
        '<table class="facit"><thead><tr><th>Nr</th><th>Acceleration \\(a\\)</th><th>Snörkraft \\(S_1\\)</th>'
        '<th>Snörkraft \\(S_2\\)</th></tr></thead><tbody>' + ''.join(rader) + '</tbody></table></div>')

    # ---------------- lösta exempel
    s2 = UPPG[1][2]
    s6 = UPPG[5][2]
    i_m = '<tspan font-style="italic">m</tspan>'
    fb2 = (frilagg('x2a', i_m, [('u', 'F', 44, 'N'), ('d', 'F', 44, 'g'), ('r', 'S', 62, 'S')], 0, 190)
           .replace('>F</text>', '>F<tspan font-size="10" dy="3">N</tspan></text>', 1)
           .replace('>F</text>', '>F<tspan font-size="10" dy="3">g</tspan></text>', 1),
           frilagg('x2b', f'2{i_m}', [('u', 'F', 44, 'N'), ('d', 'F', 52, 'g'), ('l', 'S', 62, 'S'), ('r', 'F', 66, 'F')], 1, 190)
           .replace('>F</text>', '>F<tspan font-size="10" dy="3">N</tspan></text>', 1)
           .replace('>F</text>', '>F<tspan font-size="10" dy="3">g</tspan></text>', 1))
    fb6 = (frilagg('x6a', i_m, [('u', 'S', 56, 'S'), ('d', 'mg', 40, 'g')], 0, 170),
           frilagg('x6b', f'2{i_m}', [('u', 'S', 56, 'S'), ('d', '2mg', 70, 'g')], 1, 170))
    ex2 = (
        '<div class="ex"><h3>Exempel 2: två klossar som dras av kraften <em>F</em></h3>'
        f'<div class="mini"><div>{figur(s2, "xe2", "Uppgift 2", Ftext="F")}</div><div>Klossarna är sammanbundna med ett snöre och '
        'dras åt höger med kraften \\(F\\). Snörkraften \\(S\\) drar klossen \\(m\\) framåt och klossen \\(2m\\) bakåt.</div></div>'
        '<div class="exsteg">'
        f'<div class="lab">Steg 1</div><div><strong>Frilägg.</strong><div class="fbd">{fb2[0]}{fb2[1]}</div>'
        '<div class="notis">Lodrätt tar normalkraften \\(F_N\\) och tyngdkraften \\(F_g\\) ut varandra.</div></div>'
        '<div class="lab">Steg 2</div><div><strong>Komposanter.</strong> Alla krafter är redan vågräta eller lodräta. '
        'Ingen uppdelning behövs.</div>'
        '<div class="lab">Steg 3</div><div><strong>Newtons andra lag för varje kloss.</strong> Positiv riktning åt höger.'
        '\\[\\begin{cases}S=ma & (1)\\\\ F-S=2ma & (2)\\end{cases}\\]</div>'
        '<div class="lab">Steg 4</div><div><strong>Lös ekvationssystemet.</strong> Addera ekvationerna, så försvinner '
        '\\(S\\):\\[F=3ma\\quad\\Rightarrow\\quad a=\\frac{F}{3m}=\\frac{10}{3\\cdot1{,}0}\\ \\text{m/s}^2\\approx3{,}3\\ '
        '\\text{m/s}^2\\]Sätt in \\(a\\) i ekvation (1):\\[S=m\\cdot\\frac{F}{3m}=\\frac{F}{3}=\\frac{10}{3}\\ \\text{N}'
        '\\approx3{,}3\\ \\text{N}\\]</div></div></div>')
    ex6 = (
        '<div class="ex"><h3>Exempel 6: två klossar över en trissa</h3>'
        f'<div class="mini"><div>{figur(s6, "xe6", "Uppgift 6")}</div><div>Den tyngre klossen \\(2m\\) sjunker och drar upp klossen '
        '\\(m\\). Snöret är detsamma på båda sidor om trissan, så snörkraften \\(S\\) är lika stor på båda klossarna.</div></div>'
        '<div class="exsteg">'
        f'<div class="lab">Steg 1</div><div><strong>Frilägg.</strong><div class="fbd">{fb6[0]}{fb6[1]}</div></div>'
        '<div class="lab">Steg 2</div><div><strong>Komposanter.</strong> Alla krafter är lodräta. Ingen uppdelning behövs.</div>'
        '<div class="lab">Steg 3</div><div><strong>Newtons andra lag för varje kloss.</strong> Positiv riktning medurs runt '
        'trissan: uppåt för \\(m\\) och nedåt för \\(2m\\).\\[\\begin{cases}S-mg=ma & (1)\\\\ 2mg-S=2ma & (2)\\end{cases}\\]</div>'
        '<div class="lab">Steg 4</div><div><strong>Lös ekvationssystemet.</strong> Addera ekvationerna:'
        '\\[mg=3ma\\quad\\Rightarrow\\quad a=\\frac{g}{3}=\\frac{9{,}82}{3}\\ \\text{m/s}^2\\approx3{,}3\\ \\text{m/s}^2\\]'
        'Sätt in \\(a\\) i ekvation (1):\\[S=mg+m\\cdot\\frac{g}{3}=\\frac{4mg}{3}=\\frac{4\\cdot1{,}0\\cdot9{,}82}{3}\\ '
        '\\text{N}\\approx13\\ \\text{N}\\]</div></div></div>')
    delar.append('<div class="sida"><h2 class="rubrik">Lösning av exempel 2 och 6</h2><p class="ingress">Samma fyra steg '
                 'fungerar i alla uppgifterna. Börja alltid med friläggningen.</p>' + ex2 + ex6 + '</div>')

    html = ('<!doctype html><html lang="sv"><head><meta charset="utf-8"><title>Färdighetsträning – Newtons andra lag</title>'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">'
            '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>'
            '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" '
            'onload="renderMathInElement(document.body,{delimiters:[{left:\'\\\\[\',right:\'\\\\]\',display:true},'
            '{left:\'\\\\(\',right:\'\\\\)\',display:false}]});document.body.dataset.klar=1"></script>'
            f'<style>{CSS}</style></head><body>' + ''.join(delar) + '</body></html>')
    UT.mkdir(parents=True, exist_ok=True)
    (UT / f'{NAMN}.html').write_text(html, encoding='utf-8')
    return sv


PDF_JS = r"""
const path=require('path'),fs=require('fs');const {chromium}=require('playwright');
const [html,pdf,deps]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.route('**/*',r=>{const u=new URL(r.request().url());
 const m=u.hostname==='cdn.jsdelivr.net'&&u.pathname.match(/^\/npm\/katex@[^/]+\/dist\/(.+)$/);
 if(m) return r.fulfill({path:path.join(deps,'katex','package','dist',m[1])});
 if(u.protocol==='file:') return r.continue(); return r.abort();});
await p.goto('file://'+html);await p.waitForFunction(()=>document.body.dataset.klar==='1',null,{timeout:30000});
await p.waitForTimeout(400);
await p.pdf({path:pdf,format:'A4',printBackground:true,displayHeaderFooter:true,headerTemplate:'<span></span>',
 footerTemplate:'<div style="font-size:7.5pt;color:#7a8794;width:100%;padding:0 13mm;display:flex;justify-content:space-between;font-family:Arial"><span>Färdighetsträning – Newtons andra lag · Fysik 1</span><span>sida <span class=pageNumber></span> av <span class=totalPages></span></span></div>',
 margin:{top:'13mm',bottom:'15mm',left:'13mm',right:'13mm'}});
await b.close();})();
"""


if __name__ == '__main__':
    sv = bygg()
    for r in sv:
        print(r['n'], tva(r['a']), [tva(x) for x in r['S']], r['asym'], r['Ssym'])
    deps = next((a.split('=', 1)[1] for a in sys.argv if a.startswith('--deps=')), None)
    if deps:
        js = UT / '_pdf.cjs'
        js.write_text(PDF_JS, encoding='utf-8')
        try:
            subprocess.run(['node', str(js), str(UT / f'{NAMN}.html'), str(UT / f'{NAMN}.pdf'), deps], check=True)
        finally:
            js.unlink()
        print('PDF:', UT / f'{NAMN}.pdf')
