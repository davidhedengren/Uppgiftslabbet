'use strict';
// Kör från valfri katalog. Befintlig bank verifieras och de sex korten läggs sist.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const bankfil = path.join(__dirname, '..', 'uppgifter.js');
const kort = [
  {
    "id": "2.371",
    "kap": 2,
    "omr": "densitet",
    "familj": "Sammansatta och ihåliga föremål",
    "familjNyckel": "densitet__sammansatt_densitet_och_ihaliga_foremal",
    "typ": "skilja öppna och slutna porer med två vägningar",
    "niva": "A",
    "poang": "(0/1/2)",
    "traningsniva": 5,
    "arbetsinsats": 3,
    "formaga": [
      "problemlösning",
      "modellering"
    ],
    "miniräknare": true,
    "geogebra": false,
    "spel": true,
    "självrättning": true,
    "t": "<p>En torr keramikbit väger 216,0 g och har yttervolymen 125,0 cm³. Själva keramikmaterialet har densiteten 2,70 g/cm³. En del porer har kontakt med ytan, andra är helt slutna.</p><span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 110\" width=\"360\" height=\"110\" role=\"img\" aria-label=\"En öppen por har en kanal till ytan. Den slutna poren är helt omsluten.\" style=\"max-width:100%;height:auto\"><title>En öppen por har en kanal till ytan. Den slutna poren är helt omsluten.</title><rect width=\"360\" height=\"110\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><rect x=\"28\" y=\"36\" width=\"304\" height=\"64\" fill=\"#ecdcc0\" stroke=\"#425766\"/><path d=\"M83 35 V59 Q66 82 90 87 Q114 84 99 62 V35\" fill=\"#bcdfee\" stroke=\"#425766\"/><ellipse cx=\"245\" cy=\"68\" rx=\"23\" ry=\"14\" fill=\"white\" stroke=\"#425766\"/><text x=\"92\" y=\"23\" text-anchor=\"middle\">Öppen por</text><text x=\"245\" y=\"23\" text-anchor=\"middle\">Sluten por</text></g></svg></span><p>När alla öppna porer har fyllts med vatten torkar Sara av ytan och väger biten igen. Nu väger den 244,0 g. Hur stor andel av bitens yttervolym utgörs av slutna porer?</p>",
    "ledtrad": "<p>Vad mäter ökningen på vågen? Vilka tre delar fyller tillsammans bitens yttervolym?</p>",
    "s": "<div class=\"facit-v2 facit-stegvis\"><ol class=\"facit-steglista\" role=\"list\"><li><p class=\"facit-rubrik\">Givet och sökt</p><p>Den torra bitens massa kommer från keramikmaterialet. Yttervolymen omfattar både material och porer. Sökt: de slutna porernas andel av hela bitens volym.</p></li><li><p class=\"facit-rubrik\">Materialets volym: \\(V=m/\\rho\\)</p><p>Med materialets densitet blir den fasta keramikens volym 216,0 g / (2,70 g/cm³) = 80,0 cm³.</p></li><li><p class=\"facit-rubrik\">Vattnet i de öppna porerna: \\(V_p=\\Delta m/\\rho_{\\rm vatten}\\)</p><p>Vattnet som stannat kvar väger 244,0 − 216,0 = 28,0 g. Med densiteten 1,00 g/cm³ fyller det 28,0 cm³.</p></li><li><p class=\"facit-rubrik\">De slutna porernas andel: \\(f=V_s/V\\)</p><p>Kvar i biten finns 125,0 − 80,0 − 28,0 = 17,0 cm³ slutna porer. Andelen av hela biten är 17,0/125,0 = 0,136.</p></li></ol><p class=\"facit-svar\"><strong>Svar:</strong> 13,6 % av bitens yttervolym.</p></div>",
    "rättSvar": 13.6,
    "svarstyp": "numeriskt",
    "svarFormat": "numeriskt",
    "svarEnhet": "%",
    "svarVardesiffror": 3,
    "tolerans": 0.05
  },
  {
    "id": "2.372",
    "kap": 2,
    "omr": "densitet",
    "familj": "Densitet ur diagram och mätdata",
    "familjNyckel": "densitet__densitet_fran_diagram_och_matdata",
    "typ": "bestämma ett minerals densitet ur två prov med olika massandelar",
    "niva": "A",
    "poang": "(0/1/2)",
    "traningsniva": 5,
    "arbetsinsats": 3,
    "formaga": [
      "problemlösning",
      "modellering"
    ],
    "miniräknare": true,
    "geogebra": false,
    "spel": true,
    "självrättning": true,
    "t": "<p>Två stenprover består av ljusa och mörka mineralkorn utan hålrum. Figuren visar hur massan är fördelad i varje prov.</p><span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 110\" width=\"360\" height=\"110\" role=\"img\" aria-label=\"Prov A innehåller 90 g mörka och 30 g ljusa korn. Prov B innehåller 30 g mörka och 90 g ljusa.\" style=\"max-width:100%;height:auto\"><title>Prov A innehåller 90 g mörka och 30 g ljusa korn. Prov B innehåller 30 g mörka och 90 g ljusa.</title><rect width=\"360\" height=\"110\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><text x=\"40\" y=\"37\" text-anchor=\"middle\">Prov A</text><text x=\"40\" y=\"83\" text-anchor=\"middle\">Prov B</text><rect x=\"78\" y=\"15\" width=\"192\" height=\"30\" fill=\"#a3b5c0\" stroke=\"#425766\"/><rect x=\"270\" y=\"15\" width=\"64\" height=\"30\" fill=\"#efddc1\" stroke=\"#425766\"/><rect x=\"78\" y=\"61\" width=\"64\" height=\"30\" fill=\"#a3b5c0\" stroke=\"#425766\"/><rect x=\"142\" y=\"61\" width=\"192\" height=\"30\" fill=\"#efddc1\" stroke=\"#425766\"/><text x=\"174\" y=\"36\" text-anchor=\"middle\">90 g mörka</text><text x=\"302\" y=\"36\" text-anchor=\"middle\">30 g</text><text x=\"110\" y=\"82\" text-anchor=\"middle\">30 g</text><text x=\"238\" y=\"82\" text-anchor=\"middle\">90 g ljusa</text></g></svg></span><p>Prov A har volymen 45,0 cm³ och prov B har volymen 55,0 cm³. Vilken densitet har det ljusa mineralet?</p>",
    "ledtrad": "<p>Tänk dig tre exemplar av prov B. Hur mycket av varje mineral återstår om du tar bort lika mycket material som i ett prov A?</p>",
    "s": "<div class=\"facit-v2 facit-stegvis\"><ol class=\"facit-steglista\" role=\"list\"><li><p class=\"facit-rubrik\">Givet och sökt</p><p>Sökt: de ljusa kornens densitet. Vi behöver skilja deras massa och volym från de mörka kornens.</p></li><li><p class=\"facit-rubrik\">Lika mycket mörkt mineral: \\(3\\cdot30=90\\)</p><p>Tre prov B innehåller 90 g mörka och 270 g ljusa korn. Ta bort mängderna i ett prov A. Alla mörka korn försvinner och 270 − 30 = 240 g ljusa korn återstår.</p></li><li><p class=\"facit-rubrik\">De ljusa kornens volym: \\(V=3V_B-V_A\\)</p><p>Proverna saknar hålrum. Då kan vi även subtrahera volymerna. De återstående kornens volym är 3 · 55,0 − 45,0 = 120,0 cm³.</p></li><li><p class=\"facit-rubrik\">Densiteten: \\(\\rho=m/V\\)</p><p>De ljusa kornens densitet är 240 g / 120,0 cm³ = 2,0 g/cm³.</p></li></ol><p class=\"facit-svar\"><strong>Svar:</strong> 2,0 g/cm³.</p></div>",
    "rättSvar": 2,
    "svarstyp": "numeriskt",
    "svarFormat": "numeriskt",
    "svarEnhet": "g/cm³",
    "svarVardesiffror": 2,
    "tolerans": 0.05
  },
  {
    "id": "2.373",
    "kap": 2,
    "omr": "densitet",
    "familj": "Densitet, flytförmåga och modeller",
    "familjNyckel": "densitet__densitet_och_flytformaga",
    "typ": "beräkna återstående lastförmåga när ett sidofack läcker",
    "niva": "A",
    "poang": "(0/1/2)",
    "traningsniva": 5,
    "arbetsinsats": 3,
    "formaga": [
      "problemlösning",
      "modellering"
    ],
    "miniräknare": true,
    "geogebra": false,
    "spel": true,
    "självrättning": true,
    "t": "<p>En rektangulär ponton flyter vågrätt i en sjö där vattnets densitet är 1,00 kg/liter. När pontonen är tom och tät ligger undersidan 18,0 cm under ytan. Pontonen har vertikala sidor och bottenarean 0,960 m².</p><span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 110\" width=\"360\" height=\"110\" role=\"img\" aria-label=\"Ponton med vatten i sidofacket och torrt huvudfack. Vattenytan i sidofacket ligger i nivå med sjön.\" style=\"max-width:100%;height:auto\"><title>Ponton med vatten i sidofacket och torrt huvudfack. Vattenytan i sidofacket ligger i nivå med sjön.</title><rect width=\"360\" height=\"110\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><rect x=\"8\" y=\"60\" width=\"344\" height=\"42\" fill=\"#d5edf5\" stroke=\"#425766\"/><rect x=\"58\" y=\"27\" width=\"240\" height=\"62\" fill=\"white\" stroke=\"#425766\"/><rect x=\"222\" y=\"60\" width=\"76\" height=\"23\" fill=\"#b5ddeb\" stroke=\"#425766\"/><rect x=\"222\" y=\"83\" width=\"76\" height=\"6\" fill=\"#e8d7bc\" stroke=\"#425766\"/><line x1=\"222\" y1=\"27\" x2=\"222\" y2=\"89\" stroke=\"#537080\" stroke-width=\"2\"/><text x=\"137\" y=\"66\" text-anchor=\"middle\">Torrt fack</text><text x=\"258\" y=\"17\" text-anchor=\"middle\">Sidofack</text></g></svg></span><p>Ett sidofack får en läcka. Vattnet i facket står sedan lika högt som i sjön. Facket har vertikala väggar, bottenarean 0,240 m² och ett golv som ligger 4,0 cm över pontonens undersida.</p><p>Hur tung last kan pontonen nu bära om undersidan får ligga högst 35,0 cm under ytan? Lasten fördelas så att pontonen ligger vågrätt.</p>",
    "ledtrad": "<p>Hur mycket mer vatten tränger pontonen undan vid den nya vattenlinjen? Vad behöver den bära utöver lasten?</p>",
    "s": "<div class=\"facit-v2 facit-stegvis\"><ol class=\"facit-steglista\" role=\"list\"><li><p class=\"facit-rubrik\">Givet och sökt</p><p>Sökt: den största lasten efter läckan. Själva pontonens massa är densamma vid båda vattenlinjerna.</p></li><li><p class=\"facit-rubrik\">Extra undanträngd massa: \\(\\Delta m=\\rho A\\Delta h\\)</p><p>Djupet ökar med 0,350 − 0,180 = 0,170 m. Den extra undanträngda vattenmassan är 1 000 · 0,960 · 0,170 kg = 163,2 kg. Så mycket kan pontonen bära utöver sin ursprungliga massa.</p></li><li><p class=\"facit-rubrik\">Vattnet i facket: \\(m_f=\\rho A_fh_f\\)</p><p>Vattendjupet mäts från fackets eget golv. Det är 0,350 − 0,040 = 0,310 m. Det inläckta vattnet väger 1 000 · 0,240 · 0,310 kg = 74,4 kg.</p></li><li><p class=\"facit-rubrik\">Massan som återstår för lasten: \\(m_L=\\Delta m-m_f\\)</p><p>Vid den djupaste tillåtna vattenlinjen bär pontonen både det inläckta vattnet och lasten. För lasten återstår 163,2 − 74,4 = 88,8 kg.</p></li></ol><p class=\"facit-svar\"><strong>Svar:</strong> 88,8 kg.</p></div>",
    "rättSvar": 88.8,
    "svarstyp": "numeriskt",
    "svarFormat": "numeriskt",
    "svarEnhet": "kg",
    "svarVardesiffror": 3,
    "tolerans": 0.05
  },
  {
    "id": "3.748",
    "kap": 3,
    "omr": "konstacc",
    "familj": "Sträcka vid konstant acceleration",
    "familjNyckel": "konstacc__stracka_vid_konstant_acceleration",
    "typ": "bestämma ett tågs längd ur fyra passertider vid två givare",
    "niva": "A",
    "poang": "(0/1/2)",
    "traningsniva": 5,
    "arbetsinsats": 3,
    "formaga": [
      "problemlösning",
      "modellering"
    ],
    "miniräknare": true,
    "geogebra": false,
    "spel": true,
    "självrättning": true,
    "t": "<p>Ett tåg ökar farten med konstant acceleration på ett rakt spår. Två givare, A och B, står 84,0 m från varandra. De registrerar när tågets front och bakände passerar. Båda givarna använder samma klocka.</p><span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 112\" width=\"360\" height=\"112\" role=\"img\" aria-label=\"Fronten passerar A vid 0,00 s och B vid 6,00 s. Bakänden passerar A vid 4,00 s och B vid 9,00 s.\" style=\"max-width:100%;height:auto\"><title>Fronten passerar A vid 0,00 s och B vid 6,00 s. Bakänden passerar A vid 4,00 s och B vid 9,00 s.</title><rect width=\"360\" height=\"112\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><text x=\"34\" y=\"43\" text-anchor=\"middle\">Front</text><text x=\"39\" y=\"93\" text-anchor=\"middle\">Bakände</text><line x1=\"95\" y1=\"50\" x2=\"322\" y2=\"50\" stroke=\"#537080\" stroke-width=\"2\"/><line x1=\"95\" y1=\"100\" x2=\"322\" y2=\"100\" stroke=\"#537080\" stroke-width=\"2\"/><circle cx=\"95\" cy=\"50\" r=\"4\" fill=\"#1d7899\"/><text x=\"95\" y=\"37\" text-anchor=\"middle\">A · 0,00 s</text><circle cx=\"245\" cy=\"50\" r=\"4\" fill=\"#1d7899\"/><text x=\"245\" y=\"37\" text-anchor=\"middle\">B · 6,00 s</text><circle cx=\"195\" cy=\"100\" r=\"4\" fill=\"#1d7899\"/><text x=\"195\" y=\"87\" text-anchor=\"middle\">A · 4,00 s</text><circle cx=\"320\" cy=\"100\" r=\"4\" fill=\"#1d7899\"/><text x=\"320\" y=\"87\" text-anchor=\"middle\">B · 9,00 s</text></g></svg></span><p>Hur långt är tåget?</p>",
    "ledtrad": "<p>Både fronten och bakänden färdas 84 m mellan givarna. När har tåget just den fart som är medelfarten för respektive passage?</p>",
    "s": "<div class=\"facit-v2 facit-stegvis\"><ol class=\"facit-steglista\" role=\"list\"><li><p class=\"facit-rubrik\">Givet och sökt</p><p>Fronten kör 84,0 m under tiden 0–6 s. Bakänden kör samma sträcka under tiden 4–9 s. Sökt: avståndet mellan front och bakände.</p></li><li><p class=\"facit-rubrik\">Medelfarten: \\(v_m=\\Delta s/\\Delta t\\)</p><p>Farten ökar linjärt. Därför uppnås medelfarten precis mitt i respektive tidsintervall. Vid 3,00 s är farten 84,0/6,00 = 14,0 m/s. Vid 6,50 s är den 84,0/5,00 = 16,8 m/s.</p></li><li><p class=\"facit-rubrik\">Accelerationen: \\(a=\\Delta v/\\Delta t\\)</p><p>Mellan dessa båda tidpunkter ökar farten med 2,8 m/s på 3,50 s. Accelerationen blir (16,8 − 14,0)/(6,50 − 3,00) = 0,800 m/s².</p></li><li><p class=\"facit-rubrik\">Tågets längd: \\(L=v_m\\Delta t\\)</p><p>Från att fronten passerar A tills bakänden passerar A rör sig tåget precis en tåglängd. Medelfarten under dessa fyra sekunder är farten vid 2,00 s, alltså en sekund före den första kända farten. Den är 14,0 − 0,800 · 1,00 = 13,2 m/s. Längden blir 13,2 m/s · 4,00 s = 52,8 m.</p></li></ol><p class=\"facit-svar\"><strong>Svar:</strong> 52,8 m.</p></div>",
    "rättSvar": 52.8,
    "svarstyp": "numeriskt",
    "svarFormat": "numeriskt",
    "svarEnhet": "m",
    "svarVardesiffror": 3,
    "tolerans": 0.05
  },
  {
    "id": "3.749",
    "kap": 3,
    "omr": "at_diagram",
    "familj": "Tolka a-t-diagram",
    "familjNyckel": "at_diagram__tolka_och_rita_rorelsediagram",
    "typ": "rekonstruera hastigheten ur acceleration och lägesvillkor och beräkna färdsträcka",
    "niva": "A",
    "poang": "(0/1/2)",
    "traningsniva": 5,
    "arbetsinsats": 3,
    "formaga": [
      "problemlösning",
      "modellering"
    ],
    "miniräknare": true,
    "geogebra": false,
    "spel": true,
    "självrättning": true,
    "t": "<p>En vagn rullar på en rak bana. Diagrammet visar vagnens acceleration. Efter 8,0 s är vagnen tillbaka där den var vid starten av mätningen.</p><span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 168\" width=\"360\" height=\"168\" role=\"img\" aria-label=\"Accelerationen är 2 m/s² från 0 till 4 s, noll från 4 till 6 s och −4 m/s² från 6 till 8 s.\" style=\"max-width:100%;height:auto\"><title>Accelerationen är 2 m/s² från 0 till 4 s, noll från 4 till 6 s och −4 m/s² från 6 till 8 s.</title><rect width=\"360\" height=\"168\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><line x1=\"52\" y1=\"31\" x2=\"52\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"52\" y=\"157\" text-anchor=\"middle\">0</text><line x1=\"172\" y1=\"31\" x2=\"172\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"172\" y=\"157\" text-anchor=\"middle\">4</text><line x1=\"232\" y1=\"31\" x2=\"232\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"232\" y=\"157\" text-anchor=\"middle\">6</text><line x1=\"292\" y1=\"31\" x2=\"292\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"292\" y=\"157\" text-anchor=\"middle\">8</text><line x1=\"52\" y1=\"122\" x2=\"298\" y2=\"122\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"38\" y=\"127\" text-anchor=\"middle\">-4</text><line x1=\"52\" y1=\"78\" x2=\"298\" y2=\"78\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"38\" y=\"83\" text-anchor=\"middle\">0</text><line x1=\"52\" y1=\"56\" x2=\"298\" y2=\"56\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"38\" y=\"61\" text-anchor=\"middle\">2</text><line x1=\"52\" y1=\"24\" x2=\"52\" y2=\"142\" stroke=\"#537080\" stroke-width=\"2\"/><line x1=\"52\" y1=\"78\" x2=\"307\" y2=\"78\" stroke=\"#537080\" stroke-width=\"2\"/><text x=\"42\" y=\"17\" text-anchor=\"middle\">a (m/s²)</text><text x=\"330\" y=\"82\" text-anchor=\"middle\">t (s)</text><line x1=\"52\" y1=\"56\" x2=\"172\" y2=\"56\" stroke=\"#126b91\" stroke-width=\"4\"/><line x1=\"172\" y1=\"78\" x2=\"232\" y2=\"78\" stroke=\"#126b91\" stroke-width=\"4\"/><line x1=\"232\" y1=\"122\" x2=\"292\" y2=\"122\" stroke=\"#126b91\" stroke-width=\"4\"/></g></svg></span><p>Hur lång sträcka har vagnen rullat under de 8,0 sekunderna?</p>",
    "ledtrad": "<p>Skissa hastigheten med en valfri starthastighet. Hur ska skissen flyttas i höjdled för att vagnen ska komma tillbaka till startpunkten?</p>",
    "s": "<div class=\"facit-v2 facit-stegvis\"><ol class=\"facit-steglista\" role=\"list\"><li><p class=\"facit-rubrik\">Givet och sökt</p><p>Förflyttningen efter 8,0 s är noll. Sökt: hela den rullade sträckan. För att kunna räkna den behöver vi veta när vagnen vänder.</p></li><li><p class=\"facit-rubrik\">Hastighetsändringen: \\(\\Delta v=a\\Delta t\\)</p><p>De första 4 s ökar hastigheten med 8 m/s. Den är sedan konstant i 2 s och minskar till sist med 8 m/s. Kalla starthastigheten u. Toppvärdet är u + 8 och slutvärdet är u, med hastigheterna i m/s.</p></li><li><p class=\"facit-rubrik\">Åter till startpunkten: \\(\\Delta s=v_m\\Delta t\\)</p><p>Medelhastigheten blir u + 4 under båda de lutande delarna av hastighetsgrafen. Under de två mittersta sekunderna är den u + 8. Summan av förflyttningarna blir noll. Då får vi 4(u + 4) + 2(u + 8) + 2(u + 4) = 0. Det ger 8u + 40 = 0, alltså u = −5 m/s. Toppvärdet är 3 m/s.<span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 168\" width=\"360\" height=\"168\" role=\"img\" aria-label=\"Hastigheten ökar från −5 till 3 m/s, är konstant och minskar sedan till −5 m/s.\" style=\"max-width:100%;height:auto\"><title>Hastigheten ökar från −5 till 3 m/s, är konstant och minskar sedan till −5 m/s.</title><rect width=\"360\" height=\"168\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><line x1=\"52\" y1=\"31\" x2=\"52\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"52\" y=\"157\" text-anchor=\"middle\">0</text><line x1=\"172\" y1=\"31\" x2=\"172\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"172\" y=\"157\" text-anchor=\"middle\">4</text><line x1=\"232\" y1=\"31\" x2=\"232\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"232\" y=\"157\" text-anchor=\"middle\">6</text><line x1=\"292\" y1=\"31\" x2=\"292\" y2=\"140\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"292\" y=\"157\" text-anchor=\"middle\">8</text><line x1=\"52\" y1=\"133\" x2=\"298\" y2=\"133\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"38\" y=\"138\" text-anchor=\"middle\">-5</text><line x1=\"52\" y1=\"78\" x2=\"298\" y2=\"78\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"38\" y=\"83\" text-anchor=\"middle\">0</text><line x1=\"52\" y1=\"45\" x2=\"298\" y2=\"45\" stroke=\"#dce4e8\" stroke-width=\"2\"/><text x=\"38\" y=\"50\" text-anchor=\"middle\">3</text><line x1=\"52\" y1=\"24\" x2=\"52\" y2=\"142\" stroke=\"#537080\" stroke-width=\"2\"/><line x1=\"52\" y1=\"78\" x2=\"307\" y2=\"78\" stroke=\"#537080\" stroke-width=\"2\"/><text x=\"42\" y=\"17\" text-anchor=\"middle\">v (m/s)</text><text x=\"330\" y=\"82\" text-anchor=\"middle\">t (s)</text><polyline points=\"52,133 172,45 232,45 292,133\" fill=\"none\" stroke=\"#126b91\" stroke-width=\"3\"/></g></svg></span></p></li><li><p class=\"facit-rubrik\">Vagnen vänder när \\(v=0\\)</p><p>I början tar det 5/2 = 2,5 s att gå från −5 till 0 m/s. I slutet tar det 3/4 = 0,75 s att gå från 3 till 0 m/s. Vagnen rullar alltså bakåt de första 2,5 s och de sista 1,25 s.</p></li><li><p class=\"facit-rubrik\">Hela sträckan: \\(s=2s_{\\rm bak}\\)</p><p>De två trianglarna under tidsaxeln ger ½ · 5 · (2,5 + 1,25) m = 9,375 m bakåt. Vagnen slutar där den började och har därför rullat lika långt framåt. Hela sträckan är 2 · 9,375 m = 18,75 m.</p></li></ol><p class=\"facit-svar\"><strong>Svar:</strong> 19 m.</p></div>",
    "rättSvar": 18.75,
    "svarstyp": "numeriskt",
    "svarFormat": "numeriskt",
    "svarEnhet": "m",
    "svarVardesiffror": 2,
    "tolerans": 0.5
  },
  {
    "id": "2.374",
    "kap": 2,
    "omr": "medelhastighet",
    "familj": "Sträcka, tid och fart",
    "familjNyckel": "medelhastighet__stracka_tid_och_fart",
    "typ": "planera en busstransport så att två vandringsgrupper kommer fram samtidigt",
    "niva": "A",
    "poang": "(0/1/2)",
    "traningsniva": 5,
    "arbetsinsats": 3,
    "formaga": [
      "problemlösning",
      "modellering"
    ],
    "miniräknare": true,
    "geogebra": false,
    "spel": true,
    "självrättning": true,
    "t": "<p>Två vandringsgrupper ska till en stuga 18 km bort längs en rak väg. En minibuss rymmer en grupp i taget. Grupp A börjar i bussen samtidigt som grupp B börjar gå. När A släpps av går de vidare mot stugan. Bussen vänder, hämtar B och kör dem till stugan.</p><span class=\"fig\"><svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 360 126\" width=\"360\" height=\"126\" role=\"img\" aria-label=\"Bussen kör från start till A:s avstigning, tillbaka till mötet med B och sedan till stugan. Skissen är inte skalenlig.\" style=\"max-width:100%;height:auto\"><title>Bussen kör från start till A:s avstigning, tillbaka till mötet med B och sedan till stugan. Skissen är inte skalenlig.</title><rect width=\"360\" height=\"126\" fill=\"white\"/><g fill=\"#203746\" font-family=\"Arial,sans-serif\" font-size=\"14\"><text x=\"31\" y=\"18\" text-anchor=\"middle\">Start</text><line x1=\"31\" y1=\"26\" x2=\"31\" y2=\"96\" stroke=\"#e4e8ea\" stroke-width=\"2\"/><text x=\"130\" y=\"18\" text-anchor=\"middle\">Möte</text><line x1=\"130\" y1=\"26\" x2=\"130\" y2=\"96\" stroke=\"#e4e8ea\" stroke-width=\"2\"/><text x=\"234\" y=\"18\" text-anchor=\"middle\">Avstigning</text><line x1=\"234\" y1=\"26\" x2=\"234\" y2=\"96\" stroke=\"#e4e8ea\" stroke-width=\"2\"/><text x=\"327\" y=\"18\" text-anchor=\"middle\">Stuga</text><line x1=\"327\" y1=\"26\" x2=\"327\" y2=\"96\" stroke=\"#e4e8ea\" stroke-width=\"2\"/><line x1=\"31\" y1=\"38\" x2=\"234\" y2=\"38\" stroke=\"#196680\" stroke-width=\"2\"/><path d=\"M227 34 L234 38 L227 42\" fill=\"none\" stroke=\"#196680\" stroke-width=\"2\"/><line x1=\"234\" y1=\"63\" x2=\"130\" y2=\"63\" stroke=\"#196680\" stroke-width=\"2\"/><path d=\"M137 59 L130 63 L137 67\" fill=\"none\" stroke=\"#196680\" stroke-width=\"2\"/><line x1=\"130\" y1=\"88\" x2=\"327\" y2=\"88\" stroke=\"#196680\" stroke-width=\"2\"/><path d=\"M320 84 L327 88 L320 92\" fill=\"none\" stroke=\"#196680\" stroke-width=\"2\"/><text x=\"180\" y=\"116\" text-anchor=\"middle\">Bussens tre körsträckor</text></g></svg></span><p>Bussen kör i 36 km/h och båda grupperna går i 6,0 km/h. Hur långt från starten ska A släppas av för att grupperna ska komma fram samtidigt? Bortse från tiden för stoppen.</p>",
    "ledtrad": "<p>Båda grupperna färdas hela vägen med samma två farter. Vad måste då gälla för deras gångsträckor om restiderna ska bli lika?</p>",
    "s": "<div class=\"facit-v2 facit-stegvis\"><ol class=\"facit-steglista\" role=\"list\"><li><p class=\"facit-rubrik\">Givet och sökt</p><p>Sökt: avståndet till A:s avstigning. Varje grupp färdas 18 km framåt. Bara den tomma bussen kör tillbaka.</p></li><li><p class=\"facit-rubrik\">Lika lång restid: \\(t=d/6+(18-d)/36\\)</p><p>En grupp som går en kilometer längre åker en kilometer kortare och kommer fram senare. Grupperna måste därför gå lika långt. Kalla gångsträckan d km. Då hämtas B vid d km och A släpps av vid 18 − d km.</p></li><li><p class=\"facit-rubrik\">Buss och vandrare under samma tid: \\(s=vt\\)</p><p>Fram till mötet med B hinner bussen sex gånger så långt som B. Bussen kör först 18 − d km, sedan (18 − d) − d = 18 − 2d km tillbaka. Det ger (18 − d) + (18 − 2d) = 6d. Därav följer 36 = 9d och d = 4,0 km.</p></li><li><p class=\"facit-rubrik\">A:s avstigning: \\(18-d\\)</p><p>A släpps av 18 − 4,0 = 14 km från starten. Båda grupperna går då 4 km och åker 14 km.</p></li></ol><p class=\"facit-svar\"><strong>Svar:</strong> 14 km från starten.</p></div>",
    "rättSvar": 14,
    "svarstyp": "numeriskt",
    "svarFormat": "numeriskt",
    "svarEnhet": "km",
    "svarVardesiffror": 2,
    "tolerans": 0.5
  }
];
const before = fs.readFileSync(bankfil, 'utf8');
const parse = s => JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
const old = parse(before);
const existing = kort.map(q => old.find(t => t.id === q.id));
if (existing.every(Boolean)) {
  assert.deepEqual(existing, kort, 'Samma ID finns redan med annat innehåll.');
  console.log('De sex uppgifterna finns redan i banken.');
} else {
  assert.ok(existing.every(q => !q), 'Ett eller flera ID:n är redan upptagna.');
  assert.ok(before.endsWith('\n];\n'), 'Oväntat bankformat.');
  const additions = JSON.stringify(kort, null, 2).slice(2, -2);
  const after = before.slice(0, -4) + ',\n' + additions + '\n];\n';
  assert.deepEqual(parse(after), [...old, ...kort]);
  fs.writeFileSync(bankfil + '.ny', after, {flag:'wx'});
  fs.renameSync(bankfil + '.ny', bankfil);
  console.log('Tillagda i Fysik 1:', kort.map(q => q.id).join(', '));
}
