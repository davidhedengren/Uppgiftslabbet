'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../uppgifter.js'),'utf8'),ctx);
const q=id=>ctx.window.BANK.find(x=>x.id===id),k=8.99e9,e=1.602e-19,me=9.109e-31,g=9.82;
// Modeller från frågornas givna data, oberoende av bankens facit och granskningslogg.
const cases=[
 ['8.11',[200/.05,5e-9*200/.05,null]],['8.29',[null,120/.04]],['8.30',230/.004/1000],
 ['8.47',[60/.012,e*60/.012/me,.5*(e*60/.012/me)*(.04/2e7)**2*1000,null]],
 ['8.48',180/(7.2e-16/e)*100],['8.59',[k*25e-9/.08**2,k*25e-9/.16**2,null]],
 ['8.60',[12/.025,4e-9*12/.025,null]],['8.65',52e-6/7.5e-9/1000],
 ['8.69',[8e-16*1.2e5,8e-16*1.2e5/g,null]],['8.101',[1e-15*1e6,5e-12*g,null]],
 ['8.102',60/.025],['8.104',[4e-9*8000,2e-9*g,4e-9*8000-2e-9*g,(4e-9*8000-2e-9*g)/2e-9]],
 ['8.105',[1.5/100,300/.015,4e-9*300/.015,null]],['8.106',[k*25e-9/.04**2,k*25e-9/.08**2,null]],
 ['8.107',3.6e-9*4500*1e6],['8.114',1.673e-27*8e10/e*.05],['8.115',[null,null,k*40e-9/.02**2,k*40e-9/.04**2]],
 ['8.168',[90/.03,null]],['8.170',[4e-9*3000,4e-9*3000/g*1e6,null]],
 ['8.332',3e-9*4e4],['8.333',600/.03],['8.334',.018/6000*1e6],['8.335',5e-9*8e4],['8.336',.12/4e-6],
 ['8.337',k*3e-6/.25**2],['8.338',-3e-6*1600],['8.339',367000*.35**2/k*1e6],['8.340',-.006/2000*1e6],
 ['8.341',k*2e-6/.20**2],['8.342',-3e-6*1400],['8.343',k*4e-6/.30**2],['8.345',k*6e-6/.40**2],
 ['8.346',-3e-6*1200],['8.347',k*4.5e-6/.18**2],['8.348',2*k*2e-6/(.20/2)**2],
 ['8.349',e*2e4/me],['8.350',Math.hypot(1600,1000)],['8.351',2*k*3e-6/.34**2],
 ['8.352',e*2.6e4/me],['8.353',Math.hypot(1500,900)],['8.355',e*2.4e4/me],['8.356',Math.hypot(1800,1200)],
 ['8.357',k*3e-6/.30**2-k*3e-6/.30**2],['8.358',e*2.2e4/me],['8.359',Math.hypot(1700,1100)],['8.360',2*k*3e-6/.36**2]
];
function close(actual,expected,id){
 if(expected===null)return; // fria motiveringar/alternativ granskas separat
 if(Array.isArray(expected)){expected.forEach((v,i)=>close(actual[i],v,id));return;}
 assert.equal(typeof actual,'number',id);assert.ok(Math.abs(actual-expected)<=Math.max(1e-22,Math.abs(expected)*1e-8),`${id}: ${actual} != ${expected}`);
}
test('Samtliga numeriska fältuppgifter följer oberoende fysikmodeller',()=>{for(const[id,value]of cases)close(q(id).rättSvar,value,id);});
test('Fältstyrka, kraft, tecken och nya omvända frågor har rätt enheter',()=>{
 assert.deepEqual(Array.from(q('8.106').svarEnhet).slice(0,2),['N/C','N/C']);
 assert.equal(q('8.339').svarEnhet,'µC');assert.equal(q('8.340').svarEnhet,'µC');
 assert.equal(q('8.357').rättSvar,0);assert.match(q('8.357').t,/\+3,0 µC/);assert.doesNotMatch(q('8.357').t,/−3,0 µC/);
 for(const id of ['8.338','8.342','8.346'])assert.ok(q(id).rättSvar<0);
 assert.equal(q('8.169').spel,false);assert.equal(q('8.169').traningsniva,3);
});
test('Avrundning till två värdesiffror tillåts där givna data motiverar det',()=>{
 assert.ok(Math.abs(q('8.47').rättSvar[2]-1.8)<=q('8.47').tolerans[2]);
 assert.ok(Math.abs(q('8.115').rättSvar[3]-220000)<=q('8.115').tolerans[3]);
});
test('Ledtrådar i de granskade korten är ämnesspecifika och rutinfrågor är E/nivå 2',()=>{
 const ids=Object.keys(JSON.parse(fs.readFileSync(require('node:path').join(__dirname,'../agent/FALT_HELA_FYSIK1_2026-10-10.json'),'utf8')).reviews);
 for(const id of ids){const task=q(id);for(const h of [task.ledtrad,...(task.spelDelar||[]).map(p=>p.ledtrad)])assert.doesNotMatch(h||'',/Vilket samband kopplar ihop de givna storheterna/);}
 for(const id of ['8.337','8.341','8.343','8.345','8.347','8.350','8.353','8.356','8.359']){assert.equal(q(id).niva,'E');assert.equal(q(id).traningsniva,2);}
});
