# Ma2: delkortens inledningar (spelIntro) i telegramstil skrivs som hela meningar (2026-11-22).
# Körs: PYTHONUTF8=1 python tools/sprak/apply.py ma2 tools/sprak/omskr/ma2_intro_telegram.py --skriv
R = {
    '5.01': {'ers': [(
        '<p>18 kampanjpaket säljs. Bas kostar 8 000 kr och Plus 12 000 kr. Faktureringen är 176 000 kr. Rörlig kostnad: 2 500 kr för Bas och 4 000 kr för Plus.</p>',
        '<p>En marknadsföringsbyrå säljer två kampanjpaket. Bas kostar 8 000 kr och Plus kostar 12 000 kr. Under en månad säljs 18 paket, och faktureringen blir 176 000 kr.</p>')]},
    '5.31': {'ers': [(
        '<p>24 besök: korta 25 min, långa 40 min. Besökstid totalt 735 min. Dokumentation 8 min efter varje besök.</p>',
        '<p>Ett hemtjänstlag planerar 24 besök under ett arbetspass. Ett kortare besök tar 25 minuter och ett längre 40 minuter. Den totala besökstiden är 735 minuter. Efter varje besök avsätts 8 minuter för dokumentation.</p>'),
        ('<p>Hur lång blir total tid inklusive dokumentation?</p>', '<p>Hur lång blir den totala tiden inklusive dokumentation?</p>')]},
    '5.43': {'ers': [(
        '<p>14 personer arbetar antingen 8 eller 6 timmar. Totalt 96 timmar. Timkostnad: 190 kr respektive 175 kr.</p>',
        '<p>På ett omsorgsboende arbetar 14 personer under en kväll. Några arbetar ett 8-timmarspass och resten ett 6-timmarspass. Tillsammans arbetar de 96 timmar. Timkostnaden är 190 kr för 8-timmarspassen och 175 kr för 6-timmarspassen.</p>')]},
    '5.53': {'ers': [(
        '<p>Dokumentationstid: normalfördelad med \\(\\mu=24\\) min och \\(\\sigma=4\\) min. Totalt 500 ärenden.</p>',
        '<p>Dokumentationstiden för en viss typ av ärende är ungefär normalfördelad med medelvärdet 24 minuter och standardavvikelsen 4 minuter. Under en period dokumenteras 500 ärenden.</p>')]},
    '5.57': {'ers': [(
        '<p>30 besök: korta 20 min, långa 50 min. Total besökstid 990 min. Lägg därefter till 6 min dokumentation per besök.</p>',
        '<p>Ett hemtjänstområde har 30 planerade besök. Ett kort besök tar 20 minuter och ett långt 50 minuter. Den totala besökstiden är 990 minuter. Till varje besök läggs dessutom 6 minuter dokumentation.</p>')]},
    '5.62': {'ers': [(
        '<p>Efterfrågan är \\(q=a-20p\\). Rörlig kostnad 40 kr/enhet, fasta kostnader 12 000 kr. Vinstens maximipunkt ligger vid \\(p=70\\).</p>',
        '<p>Efterfrågan på en produkt modelleras med \\(q=a-20p\\), där \\(p\\) är priset i kronor och \\(a\\) en konstant. Den rörliga kostnaden är 40 kr per enhet och de fasta kostnaderna är 12 000 kr. Vinstfunktionen har sin maximipunkt när \\(p=70\\).</p>')]},
    '5.65': {'ers': [(
        '<p>Normalfördelning med \\(\\mu=16\\) min och \\(\\sigma=2,5\\) min. Totalt 400 aktiviteter.</p>',
        '<p>Tiden för en viss omsorgsaktivitet är ungefär normalfördelad med medelvärdet 16 minuter och standardavvikelsen 2,5 minuter. Under en period genomförs 400 aktiviteter.</p>')]},
}
