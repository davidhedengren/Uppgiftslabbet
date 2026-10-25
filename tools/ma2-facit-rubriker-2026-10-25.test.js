'use strict';
/* Facit enligt grundinställningen (Ma1 #1.116, CLAUDE.md): varje steg har en rubrik som säger vad man gör,
   och facit slutar med ett tydligt svar. Gäller alla kort i serien S (3.2000–3.2999, 4.2000–4.2999) och de
   facit som skrevs om i kap 3 etapp 1. geometri_problemlosning behåller löpande facit men med samma rubriker. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=c.window.BANKMA2,nr=id=>+id.split('.')[1];
const SERIE=B.filter(q=>(q.kap===3||q.kap===4)&&nr(q.id)>=2000&&nr(q.id)<3000);
const ETAPP1=['3.48','3.77','3.297','3.311','3.313'].map(id=>B.find(q=>q.id===id));
function kontrollera(namn,s){
  assert.match(s,/facit-svar/,`${namn}: svar saknas`);
  const steg=(s.match(/<li>/g)||[]).length+(s.match(/class="facit-stycke"/g)||[]).length,rub=(s.match(/class="facit-rubrik"/g)||[]).length;
  assert.ok(steg>0,`${namn}: facit saknar steg`);
  assert.ok(rub>=steg,`${namn}: ${steg} steg men ${rub} rubriker`);
}
test('Facit i serien S har en rubrik per steg och ett svar',()=>{
  assert.ok(SERIE.length>=320,SERIE.length);
  for(const q of [...SERIE,...ETAPP1]){
    kontrollera(q.id,q.s);
    assert.ok((q.ledtrad||'').length>20,`${q.id}: ledtråd saknas`);
    for(const d of q.spelDelar||[]){kontrollera(`${q.id}${d.etikett}`,d.s);assert.ok((d.ledtrad||'').length>10,`${q.id}${d.etikett}: ledtråd saknas`);}
  }
});
test('Problemlösning: löpande facit med rubriker, utan steglista',()=>{
  for(const q of SERIE.filter(q=>q.omr==='geometri_problemlosning')){assert.doesNotMatch(q.s,/facit-steglista/,q.id);assert.match(q.s,/facit-stycke/,q.id);}
});
