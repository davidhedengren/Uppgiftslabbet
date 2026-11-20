# Ma5 (2026-11-20): 2.79, 2.157, 2.209 behåller "Du får använda potenser eller upprepa faktorerna." i uppgiftstexten
# (felrapportbeslut, låst av felrapporter-2026-10-13.test.js). matf1_las3.py flyttade meningen; här återställs den.
# Den tillfälliga kgInstruktion som las3 lade till togs bort för hand samma dag (kg '' ignoreras av apply.py).
R = {i: {'ers': [('som en produkt av primtal.</p>', 'som en produkt av primtal. Du får använda potenser eller upprepa faktorerna.</p>')], 'kg': ''}
     for i in ('2.79', '2.157', '2.209')}
