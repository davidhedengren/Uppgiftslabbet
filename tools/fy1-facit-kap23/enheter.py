"""71 individually reviewed unit tasks. Authoring data, not a bank-wide heuristic."""
from render import *
# Prefixes and simple single conversions. Explicit factors chosen per question.
singles={
'2.204':(r'Mikro: \(1\ \mu\mathrm m=10^{-6}\ \mathrm m\)',r'3{,}6\ \mu\mathrm m=3{,}6\cdot10^{-6}\ \mathrm m',r'3{,}6\cdot10^{-6}\ \mathrm m'),
'2.205':(r'Areaomvandling: \(1\ \mathrm{m^2}=100^2\ \mathrm{cm^2}\)',r'0{,}045\ \mathrm{m^2}=0{,}045\cdot10\,000\ \mathrm{cm^2}=450\ \mathrm{cm^2}',r'450\ \mathrm{cm^2}','En kvadratmeter är en kvadrat med sidan 100 cm. Båda längderna räknas om, så faktorn är 100², inte 100.'),
'2.206':(r'Liter: \(1\ \mathrm l=10^{-3}\ \mathrm{m^3}\)',r'2{,}8\ \mathrm l=2{,}8\cdot10^{-3}\ \mathrm{m^3}=0{,}0028\ \mathrm{m^3}',r'0{,}0028\ \mathrm{m^3}'),
'2.207':(r'Timmar till sekunder: \(1\ \mathrm h=3600\ \mathrm s\)',r'0{,}75\ \mathrm h=0{,}75\cdot3600\ \mathrm s=2700\ \mathrm s',r'2700\ \mathrm s'),
'2.208':(r'Fartomvandling: \(1\ \mathrm{km/h}=\frac{1}{3{,}6}\ \mathrm{m/s}\)',r'63\ \mathrm{km/h}=\frac{63}{3{,}6}\ \mathrm{m/s}=17{,}5\ \mathrm{m/s}',r'17{,}5\ \mathrm{m/s}','En kilometer är 1000 m och en timme är 3600 s. Därför divideras talet med 3,6.'),
'2.209':(r'Mega: \(1\ \mathrm{MW}=10^6\ \mathrm W\)',r'4{,}2\ \mathrm{MW}=4{,}2\cdot10^6\ \mathrm W',r'4{,}2\cdot10^6\ \mathrm W'),
'2.210':(r'Mikro: \(1\ \mu\mathrm A=10^{-6}\ \mathrm A\)',r'350\ \mu\mathrm A=350\cdot10^{-6}\ \mathrm A=0{,}000350\ \mathrm A',r'0{,}000350\ \mathrm A'),
'2.211':(r'Densitetsenheter: \(1\ \mathrm{g/cm^3}=1000\ \mathrm{kg/m^3}\)',r'5{,}6\ \mathrm{g/cm^3}=5{,}6\cdot1000\ \mathrm{kg/m^3}=5600\ \mathrm{kg/m^3}',r'5600\ \mathrm{kg/m^3}',r'Ett gram är \(10^{-3}\) kg och en kubikcentimeter är \(10^{-6}\) m³. Kvoten mellan faktorerna är \(10^{-3}/10^{-6}=1000\).'),
'2.212':(r'Nano: \(1\ \mathrm{ns}=10^{-9}\ \mathrm s\)',r'1{,}8\cdot10^{-8}\ \mathrm s=\frac{1{,}8\cdot10^{-8}}{10^{-9}}\ \mathrm{ns}=18\ \mathrm{ns}',r'18\ \mathrm{ns}'),
'2.213':(r'Meter till millimeter: \(1\ \mathrm m=1000\ \mathrm{mm}\)',r'0{,}00047\ \mathrm m=0{,}00047\cdot1000\ \mathrm{mm}=0{,}47\ \mathrm{mm}',r'0{,}47\ \mathrm{mm}'),
'2.321':(r'Mikro: \(1\ \mu\mathrm m=10^{-6}\ \mathrm m\)',r'75\ \mu\mathrm m=75\cdot10^{-6}\ \mathrm m=0{,}000075\ \mathrm m',r'0{,}000075\ \mathrm m','En mikrometer är en miljondels meter. Tjockleken är densamma; bara enheten ändras.')}
for id,args in singles.items(): setq(id,*conv(*args))
# Each row includes a named conversion rule, actual substitution and final unit.
series={
'2.5':[
(r'Centimeter: \(1\ \mathrm{cm}=10^{-2}\ \mathrm m\)',r'45\ \mathrm{cm}=45\cdot10^{-2}\ \mathrm m=0{,}45\ \mathrm m',r'0{,}45\ \mathrm m'),
(r'Millimeter: \(1\ \mathrm{mm}=10^{-3}\ \mathrm m\)',r'8{,}4\ \mathrm{mm}=8{,}4\cdot10^{-3}\ \mathrm m=0{,}0084\ \mathrm m',r'0{,}0084\ \mathrm m'),
(r'Kilometer: \(1\ \mathrm{km}=1000\ \mathrm m\)',r'0{,}75\ \mathrm{km}=0{,}75\cdot1000\ \mathrm m=750\ \mathrm m',r'750\ \mathrm m'),
(r'Mil: \(1\ \text{mil}=10\,000\ \mathrm m\)',r'3{,}2\ \text{mil}=3{,}2\cdot10\,000\ \mathrm m=32\,000\ \mathrm m',r'32\,000\ \mathrm m'),
(r'Nanometer: \(1\ \mathrm{nm}=10^{-9}\ \mathrm m\)',r'620\ \mathrm{nm}=620\cdot10^{-9}\ \mathrm m=6{,}2\cdot10^{-7}\ \mathrm m',r'6{,}2\cdot10^{-7}\ \mathrm m'),
(r'Decimeter: \(1\ \mathrm{dm}=10^{-1}\ \mathrm m\)',r'15\ \mathrm{dm}=15\cdot10^{-1}\ \mathrm m=1{,}5\ \mathrm m',r'1{,}5\ \mathrm m')],
'2.22':[
(r'Giga: \(1\ \mathrm{GHz}=10^9\ \mathrm{Hz}\)',r'2{,}4\ \mathrm{GHz}=2{,}4\cdot10^9\ \mathrm{Hz}',r'2{,}4\cdot10^9\ \mathrm{Hz}'),
(r'Mega: \(1\ \mathrm{MHz}=10^6\ \mathrm{Hz}\)',r'88\ \mathrm{MHz}=88\cdot10^6\ \mathrm{Hz}',r'88\,000\,000\ \mathrm{Hz}'),
(r'Kilo: \(1\ \mathrm{kBq}=10^3\ \mathrm{Bq}\)',r'37\ \mathrm{kBq}=37\cdot1000\ \mathrm{Bq}=37\,000\ \mathrm{Bq}',r'37\,000\ \mathrm{Bq}'),
(r'Mega: \(1\ \mathrm{MBq}=10^6\ \mathrm{Bq}\)',r'12\ \mathrm{MBq}=12\cdot10^6\ \mathrm{Bq}',r'12\,000\,000\ \mathrm{Bq}'),
(r'Mikro: \(1\ \mu\mathrm{Gy}=10^{-6}\ \mathrm{Gy}\)',r'150\ \mu\mathrm{Gy}=150\cdot10^{-6}\ \mathrm{Gy}=0{,}000150\ \mathrm{Gy}',r'0{,}000150\ \mathrm{Gy}'),
(r'Milli: \(1\ \mathrm{mSv}=10^{-3}\ \mathrm{Sv}\)',r'2{,}4\ \mathrm{mSv}=2{,}4\cdot10^{-3}\ \mathrm{Sv}=0{,}0024\ \mathrm{Sv}',r'0{,}0024\ \mathrm{Sv}')],
'2.32':[
(r'Kilo: \(1\ \mathrm{kW}=10^3\ \mathrm W\)',r'2{,}4\ \mathrm{kW}=2{,}4\cdot1000\ \mathrm W=2400\ \mathrm W',r'2400\ \mathrm W'),
(r'Mega: \(1\ \mathrm{MW}=10^6\ \mathrm W\)',r'850\ \mathrm{MW}=850\cdot10^6\ \mathrm W',r'850\,000\,000\ \mathrm W'),
(r'Milli: \(1\ \mathrm{mW}=10^{-3}\ \mathrm W\)',r'45\ \mathrm{mW}=45\cdot10^{-3}\ \mathrm W=0{,}045\ \mathrm W',r'0{,}045\ \mathrm W'),
(r'Hästkrafter: \(1\ \mathrm{hk}\approx735\ \mathrm W\)',r'1{,}5\ \mathrm{hk}\approx1{,}5\cdot735\ \mathrm W=1102{,}5\ \mathrm W',r'1102{,}5\ \mathrm W',r'Med tabellvärdet 735,5 W/hk blir resultatet 1103,25 W. Båda tabellvärdena ger ungefär 1,10 kW.'),
(r'Kilo: \(1\ \mathrm{kW}=10^3\ \mathrm W\)',r'0{,}60\ \mathrm{kW}=0{,}60\cdot1000\ \mathrm W=600\ \mathrm W',r'600\ \mathrm W'),
(r'Giga: \(1\ \mathrm{GW}=10^9\ \mathrm W\)',r'12\ \mathrm{GW}=12\cdot10^9\ \mathrm W',r'12\,000\,000\,000\ \mathrm W')],
'2.33':[
(r'Kilo: \(1\ \mathrm{kJ}=1000\ \mathrm J\)',r'45\ \mathrm{kJ}=45\cdot1000\ \mathrm J=45\,000\ \mathrm J',r'45\,000\ \mathrm J'),
(r'Mega: \(1\ \mathrm{MJ}=10^6\ \mathrm J\)',r'2{,}5\ \mathrm{MJ}=2{,}5\cdot10^6\ \mathrm J',r'2{,}5\cdot10^6\ \mathrm J'),
(r'Kilowattimmar: \(1\ \mathrm{kWh}=3{,}6\cdot10^6\ \mathrm J\)',r'3{,}0\ \mathrm{kWh}=3{,}0\cdot3{,}6\cdot10^6\ \mathrm J',r'10\,800\,000\ \mathrm J','En watt är en joule per sekund. En kWh är därför 1000 W gånger 3600 s.'),
(r'Wattimmar: \(1\ \mathrm{Wh}=3600\ \mathrm J\)',r'250\ \mathrm{Wh}=250\cdot3600\ \mathrm J=900\,000\ \mathrm J',r'900\,000\ \mathrm J'),
(r'Milli: \(1\ \mathrm{mJ}=10^{-3}\ \mathrm J\)',r'1{,}5\ \mathrm{mJ}=1{,}5\cdot10^{-3}\ \mathrm J=0{,}0015\ \mathrm J',r'0{,}0015\ \mathrm J'),
(r'Kilokalorier: \(1\ \mathrm{kcal}=4184\ \mathrm J\)',r'500\ \mathrm{kcal}=500\cdot4184\ \mathrm J=2\,092\,000\ \mathrm J',r'2\,092\,000\ \mathrm J','Med tabellvärdet 4186 J/kcal blir resultatet 2 093 000 J. Skillnaden kommer från omvandlingsfaktorn.')],
'2.57':[
(r'Kilo: \(1\ \mathrm{kN}=1000\ \mathrm N\)',r'4{,}5\ \mathrm{kN}=4{,}5\cdot1000\ \mathrm N=4500\ \mathrm N',r'4500\ \mathrm N'),
(r'Milli: \(1\ \mathrm{mN}=10^{-3}\ \mathrm N\)',r'250\ \mathrm{mN}=250\cdot10^{-3}\ \mathrm N=0{,}25\ \mathrm N',r'0{,}25\ \mathrm N'),
(r'Mega: \(1\ \mathrm{MN}=10^6\ \mathrm N\)',r'1{,}2\ \mathrm{MN}=1{,}2\cdot10^6\ \mathrm N',r'1{,}2\cdot10^6\ \mathrm N'),
(r'Kilo: \(1\ \mathrm{kPa}=1000\ \mathrm{Pa}\)',r'300\ \mathrm{kPa}=300\cdot1000\ \mathrm{Pa}',r'300\,000\ \mathrm{Pa}'),
(r'Bar: \(1\ \mathrm{bar}=10^5\ \mathrm{Pa}\)',r'2{,}5\ \mathrm{bar}=2{,}5\cdot10^5\ \mathrm{Pa}',r'250\,000\ \mathrm{Pa}'),
(r'Hekto: \(1\ \mathrm{hPa}=100\ \mathrm{Pa}\)',r'1013\ \mathrm{hPa}=1013\cdot100\ \mathrm{Pa}',r'101\,300\ \mathrm{Pa}')],
'2.60':[
(r'Minuter: \(1\ \mathrm{min}=60\ \mathrm s\)',r'25\ \mathrm{min}=25\cdot60\ \mathrm s=1500\ \mathrm s',r'1500\ \mathrm s'),
(r'Timmar: \(1\ \mathrm h=3600\ \mathrm s\)',r'3{,}5\ \mathrm h=3{,}5\cdot3600\ \mathrm s=12\,600\ \mathrm s',r'12\,600\ \mathrm s'),
(r'Dygn: \(1\ \text{dygn}=24\cdot3600\ \mathrm s\)',r'2\ \text{dygn}=2\cdot86\,400\ \mathrm s=172\,800\ \mathrm s',r'172\,800\ \mathrm s'),
(r'Milli: \(1\ \mathrm{ms}=10^{-3}\ \mathrm s\)',r'480\ \mathrm{ms}=480\cdot10^{-3}\ \mathrm s=0{,}480\ \mathrm s',r'0{,}480\ \mathrm s'),
(r'Mikro: \(1\ \mu\mathrm s=10^{-6}\ \mathrm s\)',r'25\ \mu\mathrm s=25\cdot10^{-6}\ \mathrm s=0{,}000025\ \mathrm s',r'0{,}000025\ \mathrm s'),
(r'År till sekunder: \(1\ \text{år}\approx3{,}156\cdot10^7\ \mathrm s\)',r'1{,}5\ \text{år}\approx1{,}5\cdot3{,}156\cdot10^7\ \mathrm s',r'4{,}734\cdot10^7\ \mathrm s','Vi använder ett genomsnittligt år. Antalet sekunder blir ungefärligt eftersom kalenderår kan vara olika långa.')],
'2.66':[
(r'Milli: \(1\ \mathrm{mA}=10^{-3}\ \mathrm A\)',r'250\ \mathrm{mA}=250\cdot10^{-3}\ \mathrm A=0{,}250\ \mathrm A',r'0{,}250\ \mathrm A'),
(r'Mikro: \(1\ \mu\mathrm A=10^{-6}\ \mathrm A\)',r'45\ \mu\mathrm A=45\cdot10^{-6}\ \mathrm A=0{,}000045\ \mathrm A',r'0{,}000045\ \mathrm A'),
(r'Kilo: \(1\ \mathrm{k\Omega}=1000\ \Omega\)',r'4{,}7\ \mathrm{k\Omega}=4{,}7\cdot1000\ \Omega=4700\ \Omega',r'4700\ \Omega'),
(r'Mega: \(1\ \mathrm{M\Omega}=10^6\ \Omega\)',r'2{,}2\ \mathrm{M\Omega}=2{,}2\cdot10^6\ \Omega',r'2\,200\,000\ \Omega'),
(r'Milli: \(1\ \mathrm{mV}=10^{-3}\ \mathrm V\)',r'12\ \mathrm{mV}=12\cdot10^{-3}\ \mathrm V=0{,}012\ \mathrm V',r'0{,}012\ \mathrm V'),
(r'Kilo: \(1\ \mathrm{kV}=1000\ \mathrm V\)',r'400\ \mathrm{kV}=400\cdot1000\ \mathrm V',r'400\,000\ \mathrm V')],
'2.68':[
(r'km/h till m/s: dividera med \(3{,}6\)',r'v=\frac{90}{3{,}6}\ \mathrm{m/s}=25\ \mathrm{m/s}',r'25\ \mathrm{m/s}'),
(r'm/s till km/h: multiplicera med \(3{,}6\)',r'v=15\cdot3{,}6\ \mathrm{km/h}=54\ \mathrm{km/h}',r'54\ \mathrm{km/h}'),
(r'km/h till m/s: dividera med \(3{,}6\)',r'v=\frac{5{,}0}{3{,}6}\ \mathrm{m/s}\approx1{,}39\ \mathrm{m/s}',r'1{,}39\ \mathrm{m/s}','Avrunda först på slutet till de två decimaler som frågan anger.'),
(r'm/s till km/h: multiplicera med \(3{,}6\)',r'v=340\cdot3{,}6\ \mathrm{km/h}=1224\ \mathrm{km/h}',r'1224\ \mathrm{km/h}'),
(r'km/h till m/s: dividera med \(3{,}6\)',r'v=\frac{108}{3{,}6}\ \mathrm{m/s}=30\ \mathrm{m/s}',r'30\ \mathrm{m/s}'),
(r'm/s till km/h: multiplicera med \(3{,}6\)',r'v=0{,}50\cdot3{,}6\ \mathrm{km/h}=1{,}8\ \mathrm{km/h}',r'1{,}8\ \mathrm{km/h}')],
'2.76':[
(r'Gram till kilogram: \(1\ \mathrm g=10^{-3}\ \mathrm{kg}\)',r'250\ \mathrm g=250\cdot10^{-3}\ \mathrm{kg}=0{,}250\ \mathrm{kg}',r'0{,}250\ \mathrm{kg}'),
(r'Milligram till kilogram: \(1\ \mathrm{mg}=10^{-6}\ \mathrm{kg}\)',r'45\ \mathrm{mg}=45\cdot10^{-6}\ \mathrm{kg}=0{,}000045\ \mathrm{kg}',r'0{,}000045\ \mathrm{kg}','Milli avser gram. Först delar man med 1000 för att få gram, sedan med 1000 för att få kilogram.'),
(r'Ton: \(1\ \text{ton}=1000\ \mathrm{kg}\)',r'2{,}4\ \text{ton}=2{,}4\cdot1000\ \mathrm{kg}=2400\ \mathrm{kg}',r'2400\ \mathrm{kg}'),
(r'Hektogram: \(1\ \mathrm{hg}=0{,}1\ \mathrm{kg}\)',r'780\ \mathrm{hg}=780\cdot0{,}1\ \mathrm{kg}=78\ \mathrm{kg}',r'78\ \mathrm{kg}'),
(r'Mikrogram till kilogram: \(1\ \mu\mathrm g=10^{-9}\ \mathrm{kg}\)',r'0{,}60\ \mu\mathrm g=0{,}60\cdot10^{-9}\ \mathrm{kg}=6{,}0\cdot10^{-10}\ \mathrm{kg}',r'6{,}0\cdot10^{-10}\ \mathrm{kg}',r'Mikro ger \(10^{-6}\) gram. Ett gram är \(10^{-3}\) kg, så den samlade faktorn är \(10^{-6}\cdot10^{-3}=10^{-9}\).'),
(r'Gram till kilogram: \(1\ \mathrm g=10^{-3}\ \mathrm{kg}\)',r'12\,000\ \mathrm g=12\,000\cdot10^{-3}\ \mathrm{kg}=12\ \mathrm{kg}',r'12\ \mathrm{kg}')]
}
for id,rows in series.items(): multi(id,[conv(*row) for row in rows])
# Area and volume: the exponent belongs to the conversion factor as well.
for id, rows, power in [
('2.61', [('350','cm','10^{-2}','0{,}035'),('4{,}2','dm','10^{-1}','0{,}042'),('1200','mm','10^{-3}','0{,}0012'),('0{,}25','km','10^3',r'250\,000'),('3','ha',None,r'30\,000'),('45','dm','10^{-1}','0{,}45')],2),
('2.74', [('250','cm','10^{-2}','0{,}000250'),('3{,}5','dm','10^{-1}','0{,}0035'),('12','l',None,'0{,}012'),('800','mm','10^{-3}',r'8\cdot10^{-7}'),('250','ml',None,'0{,}000250'),('4{,}0','hl',None,'0{,}40')],3)]:
    plans=[]
    special={'ha':('10^4',r'\mathrm{ha}'),'l':('10^{-3}',r'\mathrm l'),'ml':('10^{-6}',r'\mathrm{ml}'),'hl':('10^{-1}',r'\mathrm{hl}')}
    for val,unit,factor,out in rows:
        dest=rf'\mathrm{{m^{power}}}'
        if factor:
            src=rf'\mathrm{{{unit}^{power}}}'
            rule=rf'Omvandling av {"area" if power==2 else "volym"}: \(1\ {src}=({factor})^{power}\ {dest}\)'
            calc=rf'{val}\ {src}={val}\cdot({factor})^{power}\ {dest}={out}\ {dest}'
            why=f'En {"area innehåller två" if power==2 else "volym innehåller tre"} längdfaktorer. Därför upphöjs längdens omvandlingsfaktor till {power}.'
        else:
            f,src=special[unit];rule=rf'Enhetsbyte: \(1\ {src}={f}\ {dest}\)'
            calc=rf'{val}\ {src}={val}\cdot {f}\ {dest}={out}\ {dest}'
            why={'ha':'En hektar är 10 000 kvadratmeter.','l':'En liter är en kubikdecimeter.','ml':'En milliliter är en kubikcentimeter.','hl':'En hektoliter är 100 liter, alltså 0,1 m³.'}[unit]
        plans.append(conv(rule,calc,out+r'\ '+dest,why))
    multi(id,plans)
# Density conversions are ratios: do not square/cube the mass factor.
multi('2.1',[
conv(r'Densitet: \(\rho=m/V\)',r'2{,}7\ \mathrm{g/cm^3}=\frac{2{,}7\cdot10^{-3}\ \mathrm{kg}}{10^{-3}\ \mathrm{dm^3}}=2{,}7\ \mathrm{kg/dm^3}',r'2{,}7\ \mathrm{kg/dm^3}','Ett gram är 0,001 kg och en kubikcentimeter är 0,001 dm³. Faktorerna tar ut varandra i kvoten.'),
conv(r'Densitet: \(\rho=m/V\)',r'1000\ \mathrm{kg/m^3}=\frac{1000\cdot1000\ \mathrm g}{1000\ \mathrm l}=1000\ \mathrm{g/l}',r'1000\ \mathrm{g/l}','Omvandla både kilogram till gram och kubikmeter till liter.'),
conv(r'Densitet: \(\rho=m/V\)',r'5{,}0\ \mathrm{g/ml}=\frac{5{,}0\cdot10^{-3}\ \mathrm{kg}}{10^{-6}\ \mathrm{m^3}}=5000\ \mathrm{kg/m^3}',r'5000\ \mathrm{kg/m^3}','En milliliter är en kubikcentimeter, alltså en miljondels kubikmeter.'),
conv(r'Densitet: \(\rho=m/V\)',r'850\ \mathrm{kg/m^3}=\frac{850\cdot1000\ \mathrm g}{10^6\ \mathrm{cm^3}}=0{,}850\ \mathrm{g/cm^3}',r'0{,}850\ \mathrm{g/cm^3}','Ett kilogram är 1000 g, medan en kubikmeter är 1 000 000 cm³.'),
conv(r'Densitet: \(\rho=m/V\)',r'1{,}0\ \mathrm{kg/l}=\frac{1{,}0\ \mathrm{kg}}{10^{-3}\ \mathrm{m^3}}=1000\ \mathrm{kg/m^3}',r'1000\ \mathrm{kg/m^3}','En liter är 0,001 m³. Massan per hel kubikmeter är därför 1000 gånger massan per liter.')])
plans=[]
for value,forward,result in [('2{,}7',True,'2700'),('998',False,'0{,}998'),('13{,}6',True,r'13\,600'),('1{,}29',False,'0{,}00129'),('0{,}92',True,'920'),('7870',False,'7{,}87')]:
    unit=r'\mathrm{kg/m^3}' if forward else r'\mathrm{g/cm^3}'
    op=rf'{value}\cdot1000' if forward else rf'\frac{{{value}}}{{1000}}'
    plans.append(conv(r'Densitetsenheter: \(1\ \mathrm{g/cm^3}=1000\ \mathrm{kg/m^3}\)',op+r'\ '+unit+'='+result+r'\ '+unit,result+r'\ '+unit,r'Massans faktor är \(10^{-3}\) och volymens \(10^{-6}\) vid byte från g/cm³ till kg/m³. Kvoten är 1000. Vid byte åt andra hållet dividerar vi med 1000.'))
multi('2.58',plans)
multi('2.9',[
([(r'Tidsskillnad: \(\Delta t=t_{\text{slut}}-t_{\text{start}}\)',p('Från 18:40 till 20:40 går två timmar. Därifrån till 21:15 går ytterligare 35 minuter.')+m(r'\Delta t=2\cdot60+35=155\ \mathrm{min}'))],'Filmen är 155 minuter lång.'),
conv(r'Minuter till sekunder: \(1\ \mathrm{min}=60\ \mathrm s\)',r'\Delta t=155\cdot60\ \mathrm s=9300\ \mathrm s',r'9300\ \mathrm s','Filmens längd från a) är 155 minuter.')])
# The introductory model was accidentally missing from the question.
if 'I en förenklad tidsmodell' not in byid['2.10']['t']: byid['2.10']['t']=p(r'I en förenklad tidsmodell räknas ett år som exakt \(3{,}156\cdot10^7\) sekunder.')+byid['2.10']['t']
multi('2.10',[
conv(r'Total tid: \(t=N\,t_{\text{år}}\)',r't=17\cdot3{,}156\cdot10^7=536\,520\,000\ \mathrm s',r'536\,520\,000\ \mathrm s','Vi beräknar exakt 17 år enligt den givna modellen.'),
conv(r'Grundpotensform: \(a\cdot10^n\), där \(1\le a\lt10\)',r'536\,520\,000=5{,}3652\cdot10^8\approx5{,}4\cdot10^8',r'5{,}4\cdot10^8\ \mathrm s','Behåll två värdesiffror, 5 och 3. Nästa siffra är 6, så 3 avrundas upp till 4.'),
([(r'Åldersintervall: \(17\le N<18\)',p('Att någon är 17 år betyder vanligen att personen har fyllt 17 men ännu inte 18. Det anger inte en exakt tid sedan födelsen.')+m(r'17\cdot3{,}156\cdot10^7\le t<18\cdot3{,}156\cdot10^7')+m(r'536\,520\,000\ \mathrm s\le t<568\,080\,000\ \mathrm s'))],'Man kan ange ett intervall enligt modellen, men inte ett exakt antal sekunder utifrån enbart åldern 17 år.')])
# Solar scale: each card retains its own given quantities.
scale=[(r'Givet och sökt',p(r'Solens modelldiameter är 22 cm = 0,22 m och verkliga diameter är \(1{,}392\cdot10^9\) m. Vi söker skalan \(1:n\).')),
(r'Skalans nämnare: \(n=D_{\text{verklig}}/D_{\text{modell}}\)',m(r'n=\frac{1{,}392\cdot10^9}{0{,}22}\approx6{,}33\cdot10^9'))]
bscale=[(r'Längdskala: \(k=D_{\text{modell}}/D_{\text{verklig}}\)',p('Alla längder minskas med samma faktor, även avståndet till jorden.')+m(r'k=\frac{0{,}22}{1{,}392\cdot10^9}')),
(r'Avstånd i modellen: \(r_{\text{modell}}=kr_{\text{verklig}}\)',m(r'r_{\text{modell}}=\frac{0{,}22\cdot1{,}496\cdot10^{11}}{1{,}392\cdot10^9}\ \mathrm m')+m(r'r_{\text{modell}}\approx23{,}6\ \mathrm m'))]
cscale=[(r'Längdskala: \(k=D_{\text{sol,modell}}/D_{\text{sol}}\)',p('Använd solens diametrar för att få samma skala som i hela modellen.')+m(r'k=\frac{0{,}22}{1{,}392\cdot10^9}')),
(r'Jordens modelldiameter: \(d_{\text{modell}}=kd_{\text{jord}}\)',m(r'd_{\text{modell}}=\frac{0{,}22\cdot1{,}276\cdot10^7}{1{,}392\cdot10^9}\ \mathrm m')+m(r'd_{\text{modell}}\approx0{,}00202\ \mathrm m=2{,}02\ \mathrm{mm}'))]
multi('2.11',[(scale,r'Skalan är ungefär \(1:(6{,}33\cdot10^9)\).'),(bscale,'Avståndet är ungefär 23,6 m.'),(cscale,'Jordens diameter i modellen är ungefär 2,02 mm.')])
pa=([(r'Diagonalens längd: \(d=6{,}1\cdot25{,}4\ \mathrm{mm}\)',m(r'd=154{,}94\ \mathrm{mm}')),
(r'Pythagoras sats: \(N_d=\sqrt{N_x^2+N_y^2}\)',p('Bildpunkterna är kvadratiska. Skärmens diagonal uttryckt i bildpunktsbredder fås därför med Pythagoras sats.')+m(r'N_d=\sqrt{2778^2+1284^2}\approx3060{,}38')),
(r'Bildpunkter per längd: \(p=N_d/d\)',m(r'p=\frac{\sqrt{2778^2+1284^2}}{154{,}94}\approx19{,}8\ \mathrm{mm^{-1}}'))],r'Ungefär 19,8 bildpunkter per mm.')
pb=([(r'Bildpunktsbredd: \(b=d/N_d\)',p('Använd de ursprungliga värdena från a), så att avrundningen inte påverkar nästa svar.')+m(r'b=\frac{154{,}94}{\sqrt{2778^2+1284^2}}\ \mathrm{mm}')),
(r'Millimeter till mikrometer: \(1\ \mathrm{mm}=1000\ \mu\mathrm m\)',m(r'b\approx0{,}0506276\ \mathrm{mm}\approx50{,}6\ \mu\mathrm m'))],r'Ungefär 50,6 µm.')
pc=([(r'Bildpunktsbredd: \(b=1/p\)',p('I detta kort är 19,8 bildpunkter per mm det givna värdet. En bildpunkt upptar därför 1/19,8 mm.')+m(r'b=\frac{1}{19{,}8}\ \mathrm{mm}\approx0{,}050505\ \mathrm{mm}')),
(r'Millimeter till mikrometer: \(1\ \mathrm{mm}=1000\ \mu\mathrm m\)',m(r'b=\frac{1000}{19{,}8}\ \mu\mathrm m\approx50{,}5\ \mu\mathrm m'))],'Ungefär 50,5 µm med kortets givna värde.')
multi('2.12',[pa,pb],[pa,pc])
# Basic scientific notation: sign of exponent follows how the decimal point moves.
multi('2.21',[conv(r'Grundpotensform: \(a\cdot10^n\), där \(1\le a\lt10\)',eq,ans,why) for eq,ans,why in [
(r'0{,}00042=4{,}2\cdot10^{-4}',r'4{,}2\cdot10^{-4}','4,2 måste delas med 10 000 för att ge det ursprungliga talet.'),
(r'93\,000\,000=9{,}3\cdot10^7',r'9{,}3\cdot10^7','9,3 multiplicerat med tio miljoner ger det ursprungliga talet.'),
(r'0{,}0000000156=1{,}56\cdot10^{-8}',r'1{,}56\cdot10^{-8}','1,56 måste delas med hundra miljoner.'),
(r'6021=6{,}021\cdot10^3',r'6{,}021\cdot10^3','Flytta decimaltecknet tre steg åt vänster och kompensera med tusen.'),
(r'0{,}75=7{,}5\cdot10^{-1}',r'7{,}5\cdot10^{-1}','7,5 delas med tio.'),
(r'250\cdot10^9=2{,}5\cdot10^2\cdot10^9=2{,}5\cdot10^{11}',r'2{,}5\cdot10^{11}','250 skrivs som 2,5 gånger 100. Vid multiplikation av tiopotenser adderas exponenterna.')]])
multi('2.19',[
conv(r'Rörelseenergi: \(E_k=mv^2/2\)',r'[E_k]=\mathrm{kg}\left(\frac{\mathrm m}{\mathrm s}\right)^2=\mathrm{kg\,m^2/s^2}=\mathrm J',r'\mathrm{kg\,m^2/s^2}=\mathrm J','Sifferfaktorn 1/2 har ingen enhet. Hastighetens enhet ska kvadreras.'),
conv(r'Tryck: \(p=F/A\)',r'[p]=\frac{\mathrm{kg\,m/s^2}}{\mathrm{m^2}}=\mathrm{kg/(m\,s^2)}=\mathrm{Pa}',r'\mathrm{kg/(m\,s^2)}=\mathrm{Pa}','En newton är kg·m/s². Dividera med areans enhet m².'),
conv(r'Densitet: \(\rho=m/V\)',r'[\rho]=\frac{\mathrm{kg}}{\mathrm{m^3}}',r'\mathrm{kg/m^3}'),
conv(r'Effekt: \(P=W/t\)',r'[P]=\frac{\mathrm J}{\mathrm s}=\mathrm{kg\,m^2/s^3}=\mathrm W',r'\mathrm{kg\,m^2/s^3}=\mathrm W','Här betecknar W i formeln arbete, medan W som enhet betyder watt.'),
conv(r'Newtons andra lag: \(F=ma\)',r'[F]=\mathrm{kg}\cdot\mathrm{m/s^2}=\mathrm N',r'\mathrm{kg\,m/s^2}=\mathrm N')])
# Energy conversions and applications, explicitly separating each sought quantity.
multi('2.29',[
conv(r'Kilokalorier till joule: \(1\ \mathrm{kcal}=4184\ \mathrm J\)',r'E=2000\cdot4184\ \mathrm J=8\,368\,000\ \mathrm J',r'8\,368\,000\ \mathrm J','Med tabellvärdet 4186 J/kcal blir svaret 8 372 000 J. Båda omvandlingsfaktorerna godtas.'),
([(r'Kilokalorier till joule: \(1\ \mathrm{kcal}=4184\ \mathrm J\)',m(r'E=2000\cdot4184\ \mathrm J=8\,368\,000\ \mathrm J')),
(r'Joule till kWh: \(1\ \mathrm{kWh}=3{,}6\cdot10^6\ \mathrm J\)',m(r'E=\frac{8\,368\,000}{3{,}6\cdot10^6}\ \mathrm{kWh}\approx2{,}32\ \mathrm{kWh}')+p('Med 4186 J/kcal blir det i stället ungefär 2,33 kWh. Skillnaden beror på tabellvärdet.'))],'Ungefär 2,32 kWh (2,33 kWh med 4186 J/kcal).'),
conv(r'Energi vid konstant effekt: \(E=Pt\)',r'E=0{,}060\ \mathrm{kW}\cdot5{,}0\ \mathrm h=0{,}30\ \mathrm{kWh}',r'0{,}30\ \mathrm{kWh}','60 W = 0,060 kW. Med kilowatt och timmar blir energin direkt i kilowattimmar.'),
([(r'Tiden i sekunder: \(t=5{,}0\cdot3600\ \mathrm s\)',m(r't=18\,000\ \mathrm s')),
(r'Energi vid konstant effekt: \(E=Pt\)',m(r'E=60\ \mathrm W\cdot18\,000\ \mathrm s=1\,080\,000\ \mathrm J'))],r'\(1{,}08\cdot10^6\) J.'),
([(r'Energi per händelse: \(1\ \mathrm{eV}=1{,}602\cdot10^{-19}\ \mathrm J\)',m(r'E_1=5{,}0\cdot10^6\cdot1{,}602\cdot10^{-19}\ \mathrm J')+m(r'E_1=8{,}01\cdot10^{-13}\ \mathrm J')),
(r'Total energi: \(E_{\text{tot}}=NE_1\)',m(r'E_{\text{tot}}=10^{12}\cdot8{,}01\cdot10^{-13}\ \mathrm J=0{,}801\ \mathrm J')+p('Med det avrundade tabellvärdet 1,60·10⁻¹⁹ J/eV blir svaret 0,800 J.'))],'0,801 J (0,800 J med det avrundade tabellvärdet).')])
setq('2.34',[(r'Areaomvandling: \(1\ \mathrm{m^2}=(100\ \mathrm{cm})^2\)',p('Eleven har bara använt längdens faktor 100. En area har två längder som båda måste räknas om.')+m(r'1\ \mathrm{m^2}=10\,000\ \mathrm{cm^2}')),
(r'Multiplicera arean med \(10\,000\)',m(r'0{,}75\ \mathrm{m^2}=0{,}75\cdot10\,000\ \mathrm{cm^2}=7500\ \mathrm{cm^2}'))],'7500 cm². Faktorn är 10 000, inte 100.')
multi('2.35',[
([(r'Givet och sökt',p('A4-arket har längden 297 mm = 0,297 m och bredden 210 mm = 0,210 m. Vi söker arean.')),
(r'Rektangelns area: \(A=lb\)',m(r'A=0{,}297\cdot0{,}210\ \mathrm{m^2}=0{,}06237\ \mathrm{m^2}'))],'0,06237 m².'),
([(r'Fotbollsplanens area: \(A=lb\)',m(r'A_{\text{plan}}=105\cdot68\ \mathrm{m^2}=7140\ \mathrm{m^2}')),
(r'Antal ark som areakvot: \(N=A_{\text{plan}}/A_{\text{ark}}\)',p('Arket har arean 0,06237 m². Vi jämför sammanlagda areor; hur arken behöver klippas eller placeras ingår inte.')+m(r'N=\frac{7140}{0{,}06237}\approx114\,478')+p('Avrundat till närmaste tusental blir det 114 000.'))],'Ungefär 114 000 ark.')])
fa=conv(r'Bränslevolym: \(V=q\,s\)',r'V=0{,}58\ \mathrm{l/mil}\cdot10\ \mathrm{mil}=5{,}8\ \mathrm l',r'5{,}8\ \mathrm l','100 km är 10 mil. Förbrukningen 0,58 liter per mil multipliceras med antalet mil.')
fb=conv(r'Tillförd energi: \(E=e_VV\)',r'E=9{,}7\ \mathrm{kWh/l}\cdot5{,}8\ \mathrm l=56{,}26\ \mathrm{kWh}',r'56{,}3\ \mathrm{kWh}','På 100 km används 0,58·10 = 5,8 liter bensin. Varje liter innehåller 9,7 kWh.')
fc=([(r'Jämför energierna: \(k=E_{\text{bensin}}/E_{\text{el}}\)',m(r'k=\frac{0{,}58\cdot10\cdot9{,}7}{18}\approx3{,}13')),
('Tillförd energi är inte samma sak som nyttigt arbete',p('Bensinbilen tillförs ungefär 3,13 gånger så mycket energi på samma sträcka. Det betyder inte att hjulen utför 3,13 gånger så mycket arbete: en större del av bensinens energi kan bli värme.'))],'Bensinbilens tillförda energi är ungefär 3,13 gånger elbilens.')
multi('2.36',[fa,fb,fc])
setq('2.214',[(r'Givet och sökt',p('Kubsidan är 2,5 cm = 0,025 m. Vi söker volymen i m³.')),
(r'Kubens volym: \(V=a^3\)',m(r'V=(0{,}025\ \mathrm m)^3=1{,}5625\cdot10^{-5}\ \mathrm{m^3}')+p('Avrunda till tre värdesiffror först i svaret.'))],r'\(1{,}56\cdot10^{-5}\) m³.')
setq('2.215',[(r'Omvandla båda längderna: \(1\ \mathrm{mm}=10^{-3}\ \mathrm m\)',m(r'l=120\cdot10^{-3}\ \mathrm m=0{,}120\ \mathrm m')+m(r'b=80\cdot10^{-3}\ \mathrm m=0{,}080\ \mathrm m')),
(r'Rektangelns area: \(A=lb\)',m(r'A=0{,}120\cdot0{,}080\ \mathrm{m^2}=0{,}0096\ \mathrm{m^2}'))],'0,0096 m².')
setq('2.216',[(r'Volymflöde: \(q=V/t\)',p('12 liter passerar på en minut. Omvandla både volymen och tiden: 12 l = 0,012 m³ och 1 min = 60 s.')+m(r'q=\frac{0{,}012\ \mathrm{m^3}}{60\ \mathrm s}=0{,}00020\ \mathrm{m^3/s}'))],r'\(2{,}0\cdot10^{-4}\) m³/s.')
setq('2.217',[(r'Enheten för produkten: \([mv]=[m][v]\)',m(r'[mv]=\mathrm{kg}\cdot\mathrm{m/s}=\mathrm{kg\,m/s}')),
(r'Energienheten: \(1\ \mathrm J=1\ \mathrm{kg\,m^2/s^2}\)',p('Energi kräver en längdfaktor och en tidsfaktor mer än produkten mv har. Enheterna på ekvationens båda sidor stämmer alltså inte.'))],r'Formeln \(E=mv\) kan inte beskriva energi. Produkten har enheten kg·m/s, inte joule.')
setq('2.218',[(r'Volymskala: \(V_{\text{verklig}}=k^3V_{\text{modell}}\)',p('Skalan 1:50 innebär att varje längd blir 50 gånger så stor. Volymen innehåller tre längdfaktorer.')+m(r'V=50^3\cdot18\ \mathrm{cm^3}=2\,250\,000\ \mathrm{cm^3}')),
(r'Kubikcentimeter till kubikmeter: \(1\ \mathrm{m^3}=10^6\ \mathrm{cm^3}\)',m(r'V=\frac{2\,250\,000}{10^6}\ \mathrm{m^3}=2{,}25\ \mathrm{m^3}'))],'2,25 m³.')
setq('2.219',[(r'Givet och sökt',p('Radien är 12 mm = 0,012 m. Vi söker cirkelns area i m².')),
(r'Cirkelns area: \(A=\pi r^2\)',m(r'A=\pi(0{,}012\ \mathrm m)^2\approx0{,}000452389\ \mathrm{m^2}')+p('Avrunda till tre värdesiffror.'))],r'\(4{,}52\cdot10^{-4}\) m².')
# Conversion comparisons and model limitations.
setq('2.64',[(r'Gemensam areaenhet: \(1\ \mathrm{dm^2}=10^{-2}\ \mathrm{m^2}\)',p('Räkna om alla areor till m² innan de jämförs.')+m(r'34\ \mathrm{dm^2}=34\cdot10^{-2}\ \mathrm{m^2}=0{,}34\ \mathrm{m^2}')+m(r'3200\ \mathrm{mm^2}=3200\cdot10^{-6}\ \mathrm{m^2}=0{,}0032\ \mathrm{m^2}')+m(r'4150\ \mathrm{cm^2}=4150\cdot10^{-4}\ \mathrm{m^2}=0{,}415\ \mathrm{m^2}')),
('Jämför talen i samma enhet',m(r'0{,}45>0{,}415>0{,}34>0{,}0032'))],r'\(0{,}45\ \mathrm{m^2}>4150\ \mathrm{cm^2}>34\ \mathrm{dm^2}>3200\ \mathrm{mm^2}\).')
setq('2.220',[(r'Energitäthet: \(u=E/V\)',p('0,45 MJ = 0,45·10⁶ J lagras i en liter = 10⁻³ m³. Vi söker energin per hel kubikmeter.')+m(r'u=\frac{0{,}45\cdot10^6\ \mathrm J}{10^{-3}\ \mathrm{m^3}}=4{,}5\cdot10^8\ \mathrm{J/m^3}'))],r'\(4{,}5\cdot10^8\) J/m³.')
multi('2.65',[
([(r'Enheter för \(g\) och \(h\)',p('g är en acceleration: hastighetsändring per sekund. h är en längd.')+m(r'[g]=\mathrm{m/s^2},\qquad[h]=\mathrm m'))],'g mäts i m/s² och h i m.'),
([(r'Enhetsprodukt: \([2gh]=[g][h]\)',p('Sifferfaktorn 2 saknar enhet.')+m(r'[2gh]=\mathrm{m^2/s^2}')),
(r'Kvadratrotens enhet: \([\sqrt{2gh}]=\sqrt{[2gh]}\)',m(r'[\sqrt{2gh}]=\sqrt{\mathrm{m^2/s^2}}=\mathrm{m/s}'))],r'\(2gh\) har enheten m²/s²; \(\sqrt{2gh}\) har enheten m/s.'),
([(r'Fartens enhet: \([v]=\mathrm{m/s}\)',p(r'Bara \(\sqrt{2gh}\) har rätt enhet för fart. Uttrycket \(2gh\) kan uteslutas.')),
('Enhetsanalys bestämmer inte enhetslösa tal',p(r'Även \(\sqrt{gh}\) har enheten m/s. Enhetsanalysen kan därför inte avgöra om faktorn 2 är rätt eller ensam bevisa hela formeln.'))],r'\(\sqrt{2gh}\) har rätt enhet, men sifferfaktorn måste bestämmas på annat sätt.')])
setq('2.221',[(r'Massflöde: \(\dot m=m/t\)',p('850 kg passerar på 1 h = 3600 s. Massan är redan i rätt enhet; vi byter tidsenhet.')+m(r'\dot m=\frac{850\ \mathrm{kg}}{3600\ \mathrm s}\approx0{,}236\ \mathrm{kg/s}'))],'Ungefär 0,236 kg/s.')
multi('2.67',[
conv(r'Nano: \(1\ \mathrm{nm}=10^{-9}\ \mathrm m\)',r'6{,}2\ \mathrm{nm}=6{,}2\cdot10^{-9}\ \mathrm m',r'6{,}2\cdot10^{-9}\ \mathrm m'),
conv(r'Giga och grundpotensform: \(1\ \mathrm{Gm}=10^9\ \mathrm m\)',r'24\ \mathrm{Gm}=24\cdot10^9\ \mathrm m=2{,}4\cdot10^{10}\ \mathrm m',r'2{,}4\cdot10^{10}\ \mathrm m','Talet framför tiopotensen ska vara minst 1 men mindre än 10. Skriv 24 som 2,4·10.'),
conv(r'Potensprodukt: \(10^a10^b=10^{a+b}\)',r'3{,}4\cdot10^3\ \mathrm{km}=3{,}4\cdot10^3\cdot10^3\ \mathrm m=3{,}4\cdot10^6\ \mathrm m',r'3{,}4\cdot10^6\ \mathrm m','Kilometer ger ytterligare en faktor 10³.'),
conv(r'Piko och grundpotensform: \(1\ \mathrm{pm}=10^{-12}\ \mathrm m\)',r'155\ \mathrm{pm}=155\cdot10^{-12}\ \mathrm m=1{,}55\cdot10^{-10}\ \mathrm m',r'1{,}55\cdot10^{-10}\ \mathrm m','155 = 1,55·10². Exponenterna 2 och −12 adderas.')])
setq('2.222',[(r'Gemensam längdenhet: \(1\ \mathrm{nm}=10^{-9}\ \mathrm m\)',m(r'5{,}0\cdot10^{-8}\ \mathrm m=50\ \mathrm{nm}')+p('Det andra skiktet är alltså tjockare än skiktet på 30 nm.')),
(r'Förhållande: \(k=d_{\text{tjock}}/d_{\text{tunn}}\)',m(r'k=\frac{50\ \mathrm{nm}}{30\ \mathrm{nm}}\approx1{,}67'))],'Det tjockare skiktet är 1,67 gånger så tjockt.')
multi('2.59',[
conv(r'Knop till km/h: \(1\ \text{knop}=1{,}852\ \mathrm{km/h}\)',r'v=22\cdot1{,}852\ \mathrm{km/h}=40{,}744\ \mathrm{km/h}',r'40{,}7\ \mathrm{km/h}'),
([(r'Knop till km/h: \(1\ \text{knop}=1{,}852\ \mathrm{km/h}\)',m(r'v=22\cdot1{,}852\ \mathrm{km/h}=40{,}744\ \mathrm{km/h}')),
(r'km/h till m/s: dividera med \(3{,}6\)',m(r'v=\frac{40{,}744}{3{,}6}\ \mathrm{m/s}\approx11{,}3\ \mathrm{m/s}')+p('Använd det oavrundade värdet tills svaret anges.'))],'11,3 m/s.')])
multi('2.62',[conv(h,c,a) for h,c,a in [
(r'Milli: \(1\ \mathrm{mm}=10^{-3}\ \mathrm m\)',r'0{,}0045\ \mathrm m=4{,}5\cdot10^{-3}\ \mathrm m=4{,}5\ \mathrm{mm}',r'4{,}5\ \mathrm{mm}'),
(r'Mikro: \(1\ \mu\mathrm s=10^{-6}\ \mathrm s\)',r'3{,}2\cdot10^{-6}\ \mathrm s=3{,}2\ \mu\mathrm s',r'3{,}2\ \mu\mathrm s'),
(r'Mega: \(1\ \mathrm{MW}=10^6\ \mathrm W\)',r'5{,}6\cdot10^6\ \mathrm W=5{,}6\ \mathrm{MW}',r'5{,}6\ \mathrm{MW}'),
(r'Nano: \(1\ \mathrm{nm}=10^{-9}\ \mathrm m\)',r'1{,}2\cdot10^{-7}\ \mathrm m=120\cdot10^{-9}\ \mathrm m=120\ \mathrm{nm}',r'120\ \mathrm{nm}'),
(r'Giga: \(1\ \mathrm{GHz}=10^9\ \mathrm{Hz}\)',r'8{,}4\cdot10^9\ \mathrm{Hz}=8{,}4\ \mathrm{GHz}',r'8{,}4\ \mathrm{GHz}'),
(r'Milli: \(1\ \mathrm{mA}=10^{-3}\ \mathrm A\)',r'0{,}025\ \mathrm A=25\cdot10^{-3}\ \mathrm A=25\ \mathrm{mA}',r'25\ \mathrm{mA}\text{ (även }2{,}5\ \mathrm{cA}\text{)}')]])
multi('2.63',[
([(r'Masskala vid samma material: \(m_{\text{stor}}=k^3m_{\text{liten}}\)',p('Alla längder blir 20 gånger så stora. Volymen blir 20³ gånger så stor, och densiteten ändras inte.')+m(r'm_{\text{stor}}=20^3\cdot45\ \mathrm{kg}=360\,000\ \mathrm{kg}'))],'360 000 kg.'),
([(r'Bärkraft enligt modellen: \(F_{\max,\text{stor}}=k^2F_{\max,\text{liten}}\)',p('Frågan antar att bärkraften är proportionell mot tvärsnittsarean. Arean växer med längdfaktorn i kvadrat.')+m(r'F_{\max,\text{stor}}=20^2\cdot12\,000\ \mathrm N=4{,}8\cdot10^6\ \mathrm N'))],r'\(4{,}8\cdot10^6\) N.'),
([(r'Tyngdkraft: \(F_g=mg\)',m(r'F_{g,\text{liten}}=45\cdot9{,}82=441{,}9\ \mathrm N')+m(r'F_{g,\text{stor}}=360\,000\cdot9{,}82=3\,535\,200\ \mathrm N')),
(r'Jämför bärkraft med tyngd: \(k_F=F_{\max}/F_g\)',m(r'k_{F,\text{liten}}=\frac{12\,000}{441{,}9}\approx27{,}2')+m(r'k_{F,\text{stor}}=\frac{4{,}8\cdot10^6}{3\,535\,200}\approx1{,}36')),
('Tolka hur marginalen ändras',p('Båda kvoterna är större än 1. Enligt modellen bär båda sin egen tyngd, men den stora konstruktionen har mycket mindre marginal eftersom tyngden växer snabbare än bärkraften.'))],'Kvoterna är ungefär 27,2 och 1,36. Båda bär sin egen tyngd enligt modellen.'),
([(r'Modellens antagande: \(F_{\max}\propto A\)',p('Modellen räknar bara med hur tvärsnittsarean påverkar bärkraften. En verklig konstruktion kan också böjas eller knäckas. Materialfel, hur lasten fördelas och extra laster kan minska hållfastheten.'))],'Slutsatsen i c) gäller den förenklade modellen. En verklig konstruktion behöver även kontrolleras mot andra sätt att gå sönder.')])
volstep=(r'Rätblockets volym: \(V=lbh\)',p('Bassängens invändiga mått är 12 m, 5,0 m och 1,6 m. När den fylls till kanten är vattenvolymen hela rätblockets volym.')+m(r'V=12\cdot5{,}0\cdot1{,}6\ \mathrm{m^3}=96\ \mathrm{m^3}'))
multi('2.69',[([volstep],'96 m³.'),([volstep,(r'Kubikmeter till liter: \(1\ \mathrm{m^3}=1000\ \mathrm l\)',m(r'V=96\cdot1000\ \mathrm l=96\,000\ \mathrm l'))],'96 000 liter.')])
setq('2.223',[(r'Bildpunktsbredd: \(d=b/N\)',p('Sensorbredden 23,5 mm delas i 6000 lika breda bildpunkter.')+m(r'd=\frac{23{,}5}{6000}\ \mathrm{mm}')),
(r'Millimeter till mikrometer: \(1\ \mathrm{mm}=1000\ \mu\mathrm m\)',m(r'd=\frac{23{,}5\cdot1000}{6000}\ \mu\mathrm m\approx3{,}92\ \mu\mathrm m'))],'Ungefär 3,92 µm.')
multi('2.70',[
conv(r'Volymflöde: \(q=V/t\)',r'q=\frac{30\cdot10^{-3}\ \mathrm{m^3}}{60\ \mathrm s}=0{,}0005\ \mathrm{m^3/s}',r'0{,}0005\ \mathrm{m^3/s}','30 liter = 0,030 m³ och en minut = 60 s.'),
conv(r'Volym per minut: \(V_{60}=q\cdot60\ \mathrm s\)',r'V_{60}=1{,}2\cdot1000\cdot60\ \mathrm l=72\,000\ \mathrm l',r'72\,000\ \mathrm{l/min}','1,2 m³/s är 1200 liter varje sekund. På en minut passerar 60 gånger den volymen.'),
conv(r'Massflöde: \(\dot m=m/t\)',r'\dot m=\frac{18\cdot1000\ \mathrm{kg}}{3600\ \mathrm s}=5\ \mathrm{kg/s}',r'5\ \mathrm{kg/s}','18 ton = 18 000 kg och en timme = 3600 s.'),
conv(r'Volym per timme: \(V_{\mathrm h}=q\cdot3600\ \mathrm s\)',r'V_{\mathrm h}=0{,}250\cdot3600\ \mathrm l=900\ \mathrm l',r'900\ \mathrm{l/h}','250 ml/s är 0,250 l/s. En timme innehåller 3600 sekunder.'),
conv(r'Massa per dygn: \(m=\dot m\,t\)',r'm=2{,}0\cdot86\,400\ \mathrm{kg}=172\,800\ \mathrm{kg}=172{,}8\ \text{ton}',r'172{,}8\ \text{ton/dygn}','Ett dygn har 24·3600 = 86 400 sekunder. Ett ton är 1000 kg.')])
setq('2.224',[(r'Samma material: \(m=\rho V\)',p('Densiteten är samma i modell och original. Massorna har därför samma förhållande som volymerna.')),
(r'Volymskala: \(V_{\text{stor}}/V_{\text{liten}}=k^3\)',p('Skalan 1:25 innebär att längd, bredd och höjd alla ökar med 25. Därför blir massfaktorn 25³, inte 25.')+m(r'm_{\text{original}}=0{,}80\cdot25^3\ \mathrm{kg}=12\,500\ \mathrm{kg}'))],'12 500 kg, alltså 12,5 ton. Massan växer med volymen.')
setq('2.71',[(r'Kvadratens area: \(A=s^2\)',p('Sidan är positiv, så vi tar den positiva kvadratroten ur arean.')+m(r's=\sqrt{6{,}25\ \mathrm{cm^2}}=2{,}5\ \mathrm{cm}')),
(r'Centimeter till millimeter: \(1\ \mathrm{cm}=10\ \mathrm{mm}\)',m(r's=2{,}5\cdot10\ \mathrm{mm}=25\ \mathrm{mm}'))],'25 mm.')
multi('2.72',[
conv(r'Mikro: \(1\ \mu\mathrm m=10^{-6}\ \mathrm m\)',r'4{,}5\ \mu\mathrm m=4{,}5\cdot10^{-6}\ \mathrm m',r'4{,}5\cdot10^{-6}\ \mathrm m'),
conv(r'Nano: \(1\ \mathrm{nm}=10^{-9}\ \mathrm m\)',r'0{,}00000012\ \mathrm m=120\cdot10^{-9}\ \mathrm m=120\ \mathrm{nm}',r'120\ \mathrm{nm}\text{, exempelvis}',r'Även 0,12 µm är rätt: båda prefixformerna beskriver samma längd.'),
([(r'Gemensam enhet: \(1\ \mu\mathrm m=1000\ \mathrm{nm}\)',m(r'0{,}3\ \mu\mathrm m=0{,}3\cdot1000\ \mathrm{nm}=300\ \mathrm{nm}')+p('500 nm är större än 300 nm.'))],'500 nm är störst.')])
setq('2.225',[(r'Lös ut konstanten: \(k=F/v^2\)',p('Vi jämför enheterna i den givna modellen F = kv².')+m(r'[k]=\frac{\mathrm N}{(\mathrm{m/s})^2}')),
(r'Newtons enhet: \(1\ \mathrm N=1\ \mathrm{kg\,m/s^2}\)',m(r'[k]=\frac{\mathrm{kg\,m/s^2}}{\mathrm{m^2/s^2}}=\mathrm{kg/m}')+p('Sekundfaktorerna tar ut varandra, och en meter återstår i nämnaren.'))],'k har enheten kg/m och kan inte vara dimensionslös.')
multi('2.73',[
conv(r'Kvadratens area: \(A=a^2\)',r'A=(0{,}030\ \mathrm m)^2=0{,}0009\ \mathrm{m^2}',r'0{,}0009\ \mathrm{m^2}','Sidan 3,0 cm = 0,030 m. Arean avser en enda sidoyta.'),
conv(r'Kubens volym: \(V=a^3\)',r'V=(0{,}030\ \mathrm m)^3=0{,}000027\ \mathrm{m^3}',r'2{,}7\cdot10^{-5}\ \mathrm{m^3}','Sidan är 0,030 m. Volymen innehåller tre längdfaktorer.'),
conv(r'Areaskala: \(A_2/A_1=(a_2/a_1)^2\)',r'\frac{A_2}{A_1}=\left(\frac{6{,}0}{3{,}0}\right)^2=2^2=4',r'4','Båda sidlängderna i en sidoyta fördubblas.'),
conv(r'Volymskala: \(V_2/V_1=(a_2/a_1)^3\)',r'\frac{V_2}{V_1}=\left(\frac{6{,}0}{3{,}0}\right)^3=2^3=8',r'8','Alla tre längderna fördubblas.'),
conv(r'Volymskala: \(V_{\text{kub}}/V_{\text{modell}}=(a_{\text{kub}}/a_{\text{modell}})^3\)',r'\frac{V_{\text{kub}}}{V_{\text{modell}}}=10^3=1000',r'1000','Kubens sida är tio gånger modellens sida. Frågan ber om kubens volym dividerad med modellens.')])
multi('2.226',[([
(r'Enhetsvillkor: \([T]=[\ell]^a[g]^b\)',p('C saknar enhet. Vänsterledet har enheten s; högerledets enheter måste bli desamma.')+m(r'\mathrm s=\mathrm m^a(\mathrm{m/s^2})^b=\mathrm m^{a+b}\mathrm s^{-2b}')),
(r'Jämför exponenterna: \(a+b=0\) och \(-2b=1\)',p('På vänster sida är meterexponenten 0 och sekundexponenten 1.')+m(r'-2b=1\ \Rightarrow\ b=-\frac12')+m(r'a=-b=\frac12'))],r'\(a=\frac12\) och \(b=-\frac12\).')])
multi('2.75',[
conv(r'Kvadratens area: \(A=s^2\)',r'A=(0{,}01x)^2\ \mathrm{m^2}=10^{-4}x^2\ \mathrm{m^2}',r'10^{-4}x^2\ \mathrm{m^2}','Sidan x centimeter är 0,01x meter. Hela talet 0,01x ska kvadreras.'),
conv(r'Kubens volym: \(V=s^3\)',r'V=(0{,}01x)^3\ \mathrm{m^3}=10^{-6}x^3\ \mathrm{m^3}',r'10^{-6}x^3\ \mathrm{m^3}','Sidan i meter är 0,01x. Hela omvandlingsfaktorn upphöjs till tre.'),
conv(r'Sätt in \(x=4{,}0\) i volymuttrycket',r'V=10^{-6}\cdot4{,}0^3\ \mathrm{m^3}=6{,}4\cdot10^{-5}\ \mathrm{m^3}',r'6{,}4\cdot10^{-5}\ \mathrm{m^3}','Kontroll direkt i centimeter: 4³ = 64 cm³. Eftersom 1 cm³ = 10⁻⁶ m³ ger båda metoderna samma volym.')])
multi('2.227',[([
(r'Enhetsvillkor: \([x]=[a]^p[t]^q\)',p('C är enhetslös. Vänsterledet har enheten m.')+m(r'\mathrm m=(\mathrm{m/s^2})^p\mathrm s^q=\mathrm m^p\mathrm s^{-2p+q}')),
(r'Jämför exponenterna: \(p=1\), \(-2p+q=0\)',p('Meterexponenten ska vara 1 och sekundexponenten 0.')+m(r'p=1,\qquad q=2p=2')),
(r'Ändringsfaktor: \(x_{\text{ny}}/x_{\text{gammal}}=2^p3^q\)',p('Samma C används. Accelerationen ger en faktor 2 och tiden en faktor 3².')+m(r'\frac{x_{\text{ny}}}{x_{\text{gammal}}}=2^1\cdot3^2=18'))],r'\(p=1\), \(q=2\) och längden multipliceras med 18.')])
# Newer illustrated tasks: full explanations instead of merely wrapping old prose.
setq('2.322',[(r'Givet och sökt',p('Panelens längd är 120 cm = 1,20 m och bredden 80 cm = 0,80 m. Vi söker arean i m².')),
(r'Rektangelns area: \(A=lb\)',m(r'A=1{,}20\cdot0{,}80\ \mathrm{m^2}=0{,}96\ \mathrm{m^2}'))],'0,96 m².')
setq('2.323',[(r'Liter till kubikcentimeter: \(1\ \mathrm l=1000\ \mathrm{cm^3}\)',m(r'V=3{,}6\cdot1000\ \mathrm{cm^3}=3600\ \mathrm{cm^3}')+p('Denna volym passerar på 1 min = 60 s.')),
(r'Volymflöde: \(q=V/t\)',m(r'q=\frac{3600\ \mathrm{cm^3}}{60\ \mathrm s}=60\ \mathrm{cm^3/s}'))],'60 cm³/s.')
setq('2.324',[(r'Givet och sökt',p('Vi söker antalet avslutade mätningar. Räkna båda tiderna i sekunder.')+m(r't_{\text{tot}}=2\cdot60=120\ \mathrm s')+m(r't_{\text{mätning}}=150\cdot10^{-3}=0{,}150\ \mathrm s')),
(r'Antal mätningar: \(N=t_{\text{tot}}/t_{\text{mätning}}\)',m(r'N=\frac{120}{0{,}150}=800')+p('Kvoten är ett heltal. Alla dessa mätningar hinner därför avslutas.'))],'800 mätningar.')
setq('2.325',[(r'Givet och sökt',p('Regnets höjd är 12 mm = 0,012 m. Takets area är 35 m². Vi söker vattenvolymen i liter.')),
(r'Volym av ett lager: \(V=Ah\)',p('Tänk vattnet som ett tunt rätblock över hela taket.')+m(r'V=35\cdot0{,}012\ \mathrm{m^3}=0{,}42\ \mathrm{m^3}')),
(r'Kubikmeter till liter: \(1\ \mathrm{m^3}=1000\ \mathrm l\)',m(r'V=0{,}42\cdot1000\ \mathrm l=420\ \mathrm l'))],'420 liter.')
setq('2.326',[(r'Volymökning: \(\Delta V=V_{\text{slut}}-V_{\text{start}}\)',m(r'\Delta V=1{,}8-0{,}6=1{,}2\ \mathrm{ml}')),
(r'Milliliter till mikroliter: \(1\ \mathrm{ml}=1000\ \mu\mathrm l\)',m(r'\Delta V=1{,}2\cdot1000\ \mu\mathrm l=1200\ \mu\mathrm l'))],'1200 µl.')
setq('2.359',[(r'Radie från diameter: \(r=d/2\)',p('Tvärsnittet behandlas som en cirkel. Arean kräver radien, alltså halva den givna diametern.')+m(r'r=70/2=35\ \mu\mathrm m=0{,}035\ \mathrm{mm}')),
(r'Cirkelns area: \(A=\pi r^2\)',m(r'A=\pi\cdot(0{,}035\ \mathrm{mm})^2\approx0{,}00385\ \mathrm{mm^2}'))],r'Ungefär \(3{,}85\cdot10^{-3}\) mm².')
setq('2.360',[(r'Givet och sökt',p(r'Tiden är \(1\ \mathrm{ns}=10^{-9}\) s. Ljusfarten i vakuum är ungefär \(3{,}00\cdot10^8\) m/s. Vi söker sträckan i centimeter.')),
(r'Konstant fart: \(s=ct\)',m(r's=3{,}00\cdot10^8\cdot10^{-9}\ \mathrm m=0{,}30\ \mathrm m')),
(r'Meter till centimeter: \(1\ \mathrm m=100\ \mathrm{cm}\)',m(r's=0{,}30\cdot100\ \mathrm{cm}=30\ \mathrm{cm}'))],'Ungefär 30 cm.')
setq('2.361',[(r'Givet och sökt',p('Massan är 1,0 kg = 1000 g och densiteten 19,3 g/cm³. Vi söker volymen och sedan kubens kantlängd.')),
(r'Densitet: \(\rho=m/V\Rightarrow V=m/\rho\)',m(r'V=\frac{1000\ \mathrm g}{19{,}3\ \mathrm{g/cm^3}}\approx51{,}8\ \mathrm{cm^3}')),
(r'Kubens volym: \(V=a^3\Rightarrow a=\sqrt[3]{V}\)',p('Behåll det oavrundade volymvärdet i räknaren.')+m(r'a=\sqrt[3]{\frac{1000}{19{,}3}}\ \mathrm{cm}\approx3{,}73\ \mathrm{cm}'))],'Volymen är 51,8 cm³ och kantlängden 3,73 cm.')
setq('2.362',[(r'Givet och sökt',p('Effekten är 18 W. Tiden 2 h 30 min är 2,5 h eller 9000 s. Vi söker samma energi i kJ och kWh.')),
(r'Energi: \(E=Pt\)',m(r'E=18\ \mathrm W\cdot9000\ \mathrm s=162\,000\ \mathrm J=162\ \mathrm{kJ}')),
(r'Kilowattimmar från \(E=Pt\)',p('18 W = 0,018 kW. Med timmar som tidsenhet blir resultatet kWh.')+m(r'E=0{,}018\ \mathrm{kW}\cdot2{,}5\ \mathrm h=0{,}045\ \mathrm{kWh}'))],'162 kJ, vilket är samma energi som 0,045 kWh.')
setq('2.363',[(r'Liter till kubikmillimeter: \(1\ \mathrm l=(100\ \mathrm{mm})^3\)',m(r'V_{\text{tot}}=10^6\ \mathrm{mm^3}')),
(r'Kornets volym enligt modellen: \(V_{\text{korn}}=a^3\)',m(r'V_{\text{korn}}=(0{,}5\ \mathrm{mm})^3=0{,}125\ \mathrm{mm^3}')),
(r'Antal korn: \(N=V_{\text{tot}}/V_{\text{korn}}\)',m(r'N=\frac{10^6}{0{,}125}=8\cdot10^6')+p('Modellen antar att kornen fyller hela volymen utan luftmellanrum. Verkliga sandkorn packas inte helt tätt.'))],r'Ungefär \(8\cdot10^6\) sandkorn enligt modellen.')
setq('2.364',[(r'Givet och sökt',p('Löparen färdas 1 km = 1000 m på 4 min 30 s = 270 s. Vi söker farten.')),
(r'Fart: \(v=s/t\)',p('Tempo anger tid per sträcka; fart anger i stället sträcka per tid.')+m(r'v=\frac{1000\ \mathrm m}{270\ \mathrm s}\approx3{,}70\ \mathrm{m/s}'))],'Ungefär 3,70 m/s.')
if __name__=='__main__':
    targets={q['id'] for q in bank if q['omr']=='enheter'}
    assert set(changes)==targets,(targets-set(changes),set(changes)-targets)
    assert len(targets)==71
    save()
    print('71 huvudfacit och samtliga 110 delfacit omskrivna.')
