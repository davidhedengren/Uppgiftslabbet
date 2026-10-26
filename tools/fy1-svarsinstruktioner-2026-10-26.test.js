'use strict';
/* Användarbeslut 2026-10-26: i Fy1 skrivs enhet och avrundning inte ut när de är underförstådda.
   Precisionen ligger i svarVardesiffror (±2 värdesiffror godtas vid korrekt avrundning).
   Enheten står kvar när den inte är den naturliga SI-enheten eller när givna värden har en annan enhet
   av samma slag. Antal utan enhet rättas exakt. Se agent/FY1_SVARSINSTRUKTIONER_2026-10-26.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const q=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const ren=s=>String(s||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ');
const texter=x=>[x.t,x.spelIntro,...(x.spelDelar||[]).flatMap(d=>[d.t,d.fraga])].map(ren);

test('Avrundningskrav är ersatta av svarVardesiffror i typiska kort',()=>{
  for(const [id,vs] of [['4.447',3],['6.300',4],['5.183',2],['4.91',4],['6.459',3]]){const t=q(id);
    assert.equal(t.svarVardesiffror,vs,id);assert.doesNotMatch(ren(t.t),/decimal|värdesiffr|heltal|Avrunda/,id);}
  assert.deepEqual(q('5.209').svarVardesiffror,[3,3,3]);assert.deepEqual(q('4.9').svarVardesiffror,[3,3]);
});
test('Underförstådda enheter är borttagna, övriga står kvar',()=>{
  assert.doesNotMatch(ren(q('4.447').t),/Svara i m\/s²/);
  assert.match(ren(q('2.321').t),/\(Svara i m\.\)/);   // given i µm
  assert.match(ren(q('6.112').t),/\(Svara i mN\.\)/);  // prefix
  assert.match(ren(q('4.185').spelDelar[1].t),/\(Svara i cm\.\)/);
  assert.match(ren(q('5.184').t),/i kJ, med tecken/);
});
test('Antal utan enhet rättas exakt utan rekommenderade värdesiffror',()=>{
  for(const id of ['2.324','8.661','8.677']){const t=q(id);assert.equal(t.svarVardesiffror,undefined,id);assert.ok(Number.isInteger(t.rättSvar),id);assert.doesNotMatch(ren(t.t),/heltal/,id);}
});
test('Inga trasiga meningar efter rensningen',()=>{
  const fel=[];for(const x of B)for(const t of texter(x)){if(/\(\s*\)|,\s*[.?)]|(?<![a-zåäö])svara\s*[.?)]|\?\.|\u0000/i.test(t))fel.push(x.id);}
  assert.deepEqual([...new Set(fel)],[]);
});
test('svarVardesiffror är heltal 1–12 och hör till numeriska svar',()=>{
  for(const x of B){const vs=[].concat(x.svarVardesiffror??[]);const rs=[].concat(x.rättSvar);
    vs.forEach((v,i)=>{if(v==null)return;assert.ok(Number.isInteger(v)&&v>=1&&v<=12,x.id);if(Array.isArray(x.svarVardesiffror))assert.equal(typeof rs[i],'number',x.id);});}
});
