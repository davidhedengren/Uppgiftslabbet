const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const bank=ctx.window.BANK;

// Kunskapsgymmet blandar inte alternativen. Rätt svar får därför inte alltid stå först.
// Gäller nivå 1-korten från rundorna 68-79 (2026-10-24).
const OMR=[[4,837,884],[5,629,636],[2,343,358],[6,557,564],[8,620,635]];
const nya=bank.filter(t=>{const m=/^(\d+)\.(\d+)$/.exec(t.id);return m&&OMR.some(([k,a,b])=>+m[1]===k&&+m[2]>=a&&+m[2]<=b)&&t.alternativ;});
test('Nya flervalskort: rätt svar på varierad plats och bokstäver i bokstavsordning',()=>{
 assert.ok(nya.length>=25,nya.length);
 const forst=nya.filter(t=>t.alternativ[0].ratt).length;
 assert.ok(forst<nya.length*0.4,`rätt svar först i ${forst} av ${nya.length}`);
 for(const t of nya){
  const b=t.alternativ.map(a=>a.txt).filter(x=>/^[A-H]$/.test(x));
  assert.equal(b.join(),[...b].sort().join(),t.id);
  assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
 }
});
