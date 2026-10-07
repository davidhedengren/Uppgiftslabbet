'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const {facitMatte}=require('./formatera-fysikfacit');

test('Gaslagen får bråkstreck, index och decimalkomma utan nya tal',()=>{
  assert.equal(facitMatte('V₂=98,0·50,0/103≈47,573 liter.'),String.raw`V_{2}=\frac{98{,}0\cdot 50{,}0}{103}\approx 47{,}573\, \mathrm{liter}`);
  assert.equal(facitMatte('p₁V₁=p₂V₂.'),String.raw`p_{1} V_{1}=p_{2} V_{2}`);
});
test('Parenteser, tecken, kvadrater och rotuttryck bevarar räkneordningen',()=>{
  assert.equal(facitMatte('a=(0-14)/7=-2,0 m/s²'),String.raw`a=\frac{\left(0-14\right)}{7}=-2{,}0\, \mathrm{m/s^2}`);
  assert.equal(facitMatte('E_f=200·0,060²/2=0,36 J'),String.raw`E_{\mathrm{f}}=\frac{200\cdot 0{,}060^{2}}{2}=0{,}36\, \mathrm{J}`);
  assert.equal(facitMatte('v=−√(2·9,82·2,50)≈−7,01 m/s'),String.raw`v=-\sqrt{2\cdot 9{,}82\cdot 2{,}50}\approx -7{,}01\, \mathrm{m/s}`);
});
test('Tusentalsgrupper och tiopotenser blir inte produkt eller variabel e',()=>{
  assert.equal(facitMatte('F=49 100 N'),String.raw`F=49\,100\, \mathrm{N}`);
  assert.equal(facitMatte('E=1e3 J'),String.raw`E=1\cdot10^{3}\, \mathrm{J}`);
});
test('Tyngdaccelerationen g förväxlas inte med gram',()=>{
  assert.equal(facitMatte('F = m g'),String.raw`F=m g`);
  assert.equal(facitMatte('m = 10 g'),String.raw`m=10\, \mathrm{g}`);
});
test('Prosa, HTML, okänd syntax och trasiga uttryck lämnas orörda',()=>{
  for(const s of ['Bilen står stilla så F=0','Svar: 8 N','x=(2+3','F=<script>','x=1; alert(2)','a=arcsin(0,2)','1 kWh = 3 600 000 J'])assert.equal(facitMatte(s),null,s);
});

test('Dokumentets facit bevarar lösningsstegen och deras separata slutsvar',()=>{
  const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
  const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8');
  const start=html.indexOf('function LOS(');
  let end=html.indexOf('\n',start),script;
  while(end>=0){
    try{script=new vm.Script(html.slice(start,end));break;}
    catch(e){if(!(e instanceof SyntaxError))throw e;}
    end=html.indexOf('\n',end+1);
  }
  assert.ok(script);
  const c=vm.createContext({plattaListor:()=>{throw new Error('Lösningsstegen får inte plattas ut');}});
  script.runInContext(c);
  const solution='<div class="facit-v2 facit-stegvis"><ol class="facit-steglista"><li><p>Välj samband.</p></li><li><div class="facit-matte">\\[Q=mc\\Delta T\\]</div></li></ol><p class="facit-svar">Svar: 25,1 kJ.</p></div>';
  assert.equal(c.LOS(solution),solution);
});
