"""Lättläst tvåsidigt grundblad. Återskapas med ReportLab, inga skärmbilder."""
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer,PageBreak
R=Path(__file__).resolve().parent.parent
pdfmetrics.registerFont(TTFont('OpenSans','/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('OpenSansBold','/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf'))
pdfmetrics.registerFontFamily('OpenSans',normal='OpenSans',bold='OpenSansBold',italic='OpenSans',boldItalic='OpenSansBold')
normal=ParagraphStyle('n',fontName='OpenSans',fontSize=9.5,leading=12,textColor=colors.HexColor('#172b40'))
small=ParagraphStyle('s',parent=normal,fontSize=8,leading=11)
h=ParagraphStyle('h',parent=normal,fontName='OpenSansBold',fontSize=13,leading=18,spaceBefore=10,spaceAfter=6)
title=ParagraphStyle('title',parent=h,fontSize=21,leading=25,spaceBefore=0)
P=lambda t:Paragraph(t,normal)
items=[]
def table(rows,widths=[240,270]):
 t=Table([[P(str(c))for c in row]for row in rows],colWidths=widths,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e5eef6')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#8ba7bd')),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#d9e2ea'))]));items.append(t)
def heading(t):items.append(Paragraph(t,h))
items+=[Paragraph('Fysik 1 · Grundblad',title),P('Prefix, vanliga omvandlingar och grundläggande samband. Sida 1 passar arbetet med enheter och mätning; sida 2 används när de senare områdena introduceras.')]
heading('Prefix – faktorn gäller enheten direkt efter prefixet')
table([['<b>Prefix och symbol</b>','<b>Faktor</b>'],['giga G · mega M · kilo k','10<super>9</super> · 10<super>6</super> · 10<super>3</super>'],['hekto h · deka da','10<super>2</super> · 10<super>1</super>'],['deci d · centi c · milli m','10<super>−1</super> · 10<super>−2</super> · 10<super>−3</super>'],['mikro μ · nano n · piko p','10<super>−6</super> · 10<super>−9</super> · 10<super>−12</super>']])
items.append(Spacer(1,6));items.append(P('Exempel: 1 mg = 10<super>−3</super> g = 10<super>−6</super> kg. Mikro kan skrivas μ eller µ. Stor och liten bokstav spelar roll: M är mega, m är milli.'))
heading('Vanliga enheter')
table([['<b>Storhet</b>','<b>Omvandling</b>'],['Längd','1 km = 1000 m · 1 m = 100 cm = 1000 mm'],['Area','1 m² = 10 000 cm² · 1 cm² = 100 mm²'],['Volym','1 m³ = 1000 liter<br/>1 liter = 1 dm³ · 1 ml = 1 cm³'],['Massa','1 ton = 1000 kg · 1 kg = 1000 g<br/>1 hg = 0,1 kg · 1 mg = 10<super>−6</super> kg<br/>1 μg = 10<super>−9</super> kg'],['Tid','1 min = 60 s · 1 h = 3600 s'],['Hastighet','1 m/s = 3,6 km/h = 60 m/min<br/>Från km/h till m/s: dividera med 3,6'],['Densitet','1 g/cm³ = 1 kg/liter = 1000 kg/m³']])
heading('De första sambanden')
table([['<b>Samband</b>','<b>Betydelse och enheter</b>'],['v = s/t · s = vt · t = s/v','Medelfart v (m/s), sträcka s (m), tid t (s).'],['ρ = m/V · m = ρV · V = m/ρ','Densitet ρ (kg/m³), massa m (kg), volym V (m³).']])
items.append(Spacer(1,7));items.append(P('Area och volym: prefixfaktorn måste också kvadreras eller kuberas. Exempel: 1 cm³ = (10<super>−2</super> m)³ = 10<super>−6</super> m³.'))
items.append(PageBreak())
items.append(Paragraph('Grundläggande samband',title));items.append(P('Välj enheter som hör ihop. I gaslagen används pascal, kubikmeter och kelvin.'))
heading('Rörelse och krafter')
table([['<b>Samband</b>','<b>Storheter</b>'],['a = Δv/Δt<br/>v = v<sub>0</sub> + at','Acceleration a (m/s²). Den andra formeln gäller konstant acceleration.'],['s = v<sub>0</sub>t + at²/2<br/>v² = v<sub>0</sub>² + 2as','Förflyttning från startpunkten vid konstant acceleration. Välj teckenriktning.'],['F<sub>res</sub> = ma · F<sub>g</sub> = mg','Resulterande kraft och tyngdkraft, i newton (N).'],['p = F/A','Tryck p (Pa), kraft F (N), area A (m²).']])
heading('Energi, effekt och elektricitet')
table([['<b>Samband</b>','<b>Storheter</b>'],['W = Fs · E<sub>k</sub> = mv²/2<br/>E<sub>p</sub> = mgh · P = W/t','Arbete W (J), kraft i rörelsens riktning F (N), energi E (J), effekt P (W).'],['U = RI · P = UI · Q = It','Spänning U (V), resistans R (Ω), ström I (A), laddning Q (C).'],['1 kWh = 3,6·10<super>6</super> J','Kilowattimme är energi. Kilowatt är effekt.']])
heading('Värme och gaser')
table([['<b>Samband</b>','<b>Storheter</b>'],['Q = mcΔT · Q = ml','Värmeenergi Q (J), specifik värmekapacitet c (J/(kg·K)), fasomvandlingsvärme l (J/kg).'],['pV = nRT<br/>T (K) = temperatur (°C) + 273,15','Tryck p (Pa), volym V (m³), substansmängd n (mol), absolut temperatur T (K).'],['ΔT i kelvin = ΔT i grader Celsius','Temperaturskillnader behöver ingen förskjutning med 273,15.']])
heading('Vanliga tabellvärden')
table([['<b>Storhet</b>','<b>Värde</b>'],['Tyngdacceleration på jorden','g ≈ 9,82 m/s²'],['Gaskonstanten','R ≈ 8,31 J/(mol·K)<br/>Mer precist: cirka 8,31446 J/(mol·K).'],['Vatten','ρ ≈ 1,0 kg/liter som överslagsvärde.<br/>Vid rumstemperatur: cirka 0,997–0,998 kg/liter.<br/>c ≈ 4180 J/(kg·K).']])
def footer(canvas,doc):
 canvas.setFont('OpenSans',8);canvas.setFillColor(colors.HexColor('#5a6b7b'));canvas.drawString(42,22,'Uppgiftslabbet · Kunskapsgymmet · Grundblad 2026-11-11');canvas.drawRightString(553,22,str(doc.page))
(R/'formelblad').mkdir(exist_ok=True)
SimpleDocTemplate(str(R/'formelblad/fy1-grundblad.pdf'),pagesize=(595.276,841.89),leftMargin=42,rightMargin=42,topMargin=32,bottomMargin=37,title='Fysik 1 – Grundblad',author='Uppgiftslabbet och Kunskapsgymmet').build(items,onFirstPage=footer,onLaterPages=footer)
