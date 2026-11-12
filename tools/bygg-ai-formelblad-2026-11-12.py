"""Formelblad för Artificiell intelligens nivå 1 (formelblad/ai.pdf), 12 november 2026.

Läraren rapporterade på AI 4.26 b: ”Här behövs formelblad för beräkning av precision, recall och accuracy.”
Bladet visas med knappen Formelblad i Kunskapsgymmet (FORMELBLAD.ai i index.html) och kan skrivas ut.
Beteckningarna är desamma som i AI-banken: Träffsäkerhet = (TP + TN) / alla, f = g + h,
w ny = w − α · lutning och så vidare. Begrepp utanför AI1, till exempel F1, finns inte med.
Återskapas med ReportLab:

  python tools/bygg-ai-formelblad-2026-11-12.py
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

R = Path(__file__).resolve().parent.parent
FONT = Path('/usr/share/fonts/truetype/dejavu')
pdfmetrics.registerFont(TTFont('DejaVu', str(FONT / 'DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont('DejaVuBold', str(FONT / 'DejaVuSans-Bold.ttf')))
pdfmetrics.registerFontFamily('DejaVu', normal='DejaVu', bold='DejaVuBold', italic='DejaVu', boldItalic='DejaVuBold')
INK = colors.HexColor('#172b40')
normal = ParagraphStyle('n', fontName='DejaVu', fontSize=9.5, leading=13, textColor=INK)
h = ParagraphStyle('h', parent=normal, fontName='DejaVuBold', fontSize=12.5, leading=16, spaceBefore=7, spaceAfter=4)
title = ParagraphStyle('t', parent=h, fontSize=19, leading=24, spaceBefore=0)
P = lambda t: Paragraph(t, normal)  # noqa: E731
items = []


def tabell(rader, bredd=(205, 306)):
    t = Table([[P(str(c)) for c in r] for r in rader], colWidths=list(bredd), repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e5eef6')),
                           ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                           ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#b8c7d6')),
                           ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 4)]))
    items.append(t)


def rubrik(t):
    items.append(Paragraph(t, h))


# ---------------------------------------------------------------- sida 1: sökning och spel
items += [Paragraph('Artificiell intelligens 1 · Formelblad', title),
          P('Sida 1: sökning och spel. Sida 2: maskininlärning.')]
rubrik('Oinformerad sökning')
tabell([['<b>Begrepp</b>', '<b>Regel</b>'],
        ['Kö (först in, först ut)', 'Det som lades in först tas ut först. BFS använder en kö.'],
        ['Stack (sist in, först ut)', 'Det som lades in sist tas ut först. DFS använder en stack.'],
        ['Bredden först (BFS)', 'Undersöker alla noder på ett avstånd innan nästa. Hittar en väg med minst antal steg.'],
        ['Djupet först (DFS)', 'Följer en gren så långt det går innan den backar.'],
        ['Grannordning', 'Den ordning som grannarna prövas i. ↑ → ↓ ← betyder: ovanför, höger, nedanför, vänster.']])
rubrik('Informerad sökning')
tabell([['<b>Samband</b>', '<b>Betydelse</b>'],
        ['Manhattanavstånd<br/>h = |Δx| + |Δy|', 'Antal rutor i sidled plus antal rutor i höjdled, utan att räkna med väggar.'],
        ['Prioritetskö', 'Lägst värde tas ut först.'],
        ['Girig bäst först', 'Tar ut noden med lägst h.'],
        ['A*<br/>f = g + h', 'g: kostnaden från start hittills. h: uppskattad kostnad kvar till målet. Lägst f tas ut först.'],
        ['Tillåten heuristik', 'h överskattar aldrig den verkliga kostnaden kvar till målet.']])
rubrik('Spelträd')
tabell([['<b>Begrepp</b>', '<b>Regel</b>'],
        ['Minimax', 'MAX väljer det största värdet bland barnen, MIN det minsta. Värdena förs upp från löven.'],
        ['Alfa–beta', 'α: det bästa MAX är säker på hittills. β: det bästa MIN är säker på hittills.<br/>'
                      'Återstående barn beskärs när α ≥ β. Beskärning ändrar inte rotens värde.']])
items.append(PageBreak())

# ---------------------------------------------------------------- sida 2: maskininlärning
items += [Paragraph('Maskininlärning', title)]
rubrik('Klassificeringsmatris')
m = Table([[P(''), P('<b>Förutsagt: positiv</b>'), P('<b>Förutsagt: negativ</b>')],
           [P('<b>Verkligt: positiv</b>'), P('TP (sant positiv)'), P('FN (falskt negativ, missad)')],
           [P('<b>Verkligt: negativ</b>'), P('FP (falskt positiv, falskt larm)'), P('TN (sant negativ)')]],
          colWidths=[130, 190, 190], hAlign='LEFT')
m.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#b8c7d6')),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e5eef6')),
                       ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#e5eef6')),
                       ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 5)]))
items += [m, Spacer(1, 4), P('Raderna är den verkliga klassen och kolumnerna det modellen förutsade.')]
rubrik('Utvärderingsmått')
tabell([['<b>Mått</b>', '<b>Betydelse</b>'],
        ['Träffsäkerhet (accuracy)<br/>= (TP + TN) / alla fall', 'Andelen av alla fall som modellen klassar rätt.'],
        ['Precision<br/>= TP / (TP + FP)', 'Andelen av fallen som modellen kallade positiva som verkligen var positiva.'],
        ['Recall (täckning)<br/>= TP / (TP + FN)', 'Andelen av alla verkligt positiva fall som modellen hittade.']])
rubrik('Regression och gradientnedstigning')
tabell([['<b>Samband</b>', '<b>Betydelse</b>'],
        ['y = kx + m', 'Linjär modell: k är lutningen och m är värdet när x = 0.'],
        ['Fel = verkligt − förutsagt', 'Positivt när modellen gissar för lågt, negativt när den gissar för högt.'],
        ['Medelkvadratfel', 'Medelvärdet av felen i kvadrat. Ju mindre, desto bättre passar modellen.'],
        ['w<sub>ny</sub> = w − α · lutning', 'Ett steg i gradientnedstigning. α är steglängden (inlärningstakten).']])
rubrik('kNN och k-means')
tabell([['<b>Samband</b>', '<b>Betydelse</b>'],
        ['Avstånd i kvadrat<br/>= (Δx)² + (Δy)²', 'Används för att jämföra vilka punkter som ligger närmast.'],
        ['kNN', 'Den nya punkten får den klass som flest av de k närmaste grannarna har.'],
        ['k-means', 'Varje punkt tillhör det närmaste centrumet. Sedan flyttas varje centrum till medelvärdet av sina punkter '
                    '(x och y var för sig).']])
rubrik('Neuroner')
tabell([['<b>Samband</b>', '<b>Betydelse</b>'],
        ['z = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + … + b', 'Viktad summa av indata x med vikterna w, plus bias b.'],
        ['Stegfunktion', 'Utdata 1 om z ≥ 0, annars 0.'],
        ['ReLU', 'Utdata z om z är positivt, annars 0.']])


def sidfot(canvas, doc):
    canvas.setFont('DejaVu', 8)
    canvas.setFillColor(colors.HexColor('#5a6b7b'))
    canvas.drawString(42, 22, 'Uppgiftslabbet · Kunskapsgymmet · Artificiell intelligens 1 · Formelblad 2026-11-12')
    canvas.drawRightString(553, 22, str(doc.page))


(R / 'formelblad').mkdir(exist_ok=True)
SimpleDocTemplate(str(R / 'formelblad/ai.pdf'), pagesize=(595.276, 841.89), leftMargin=42, rightMargin=42, topMargin=32,
                  bottomMargin=37, title='Artificiell intelligens 1 – Formelblad', author='Uppgiftslabbet och Kunskapsgymmet',
                  invariant=1).build(items, onFirstPage=sidfot, onLaterPages=sidfot)
print('formelblad/ai.pdf skapad')
