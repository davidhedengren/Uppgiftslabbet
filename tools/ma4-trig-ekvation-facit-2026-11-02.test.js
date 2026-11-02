const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato2.js'),'utf8'),c);const bank=JSON.parse(JSON.stringify(c.window.BANKMATO2));
test('Varje delfacit motiverar vinklarna och de allmänna lösningarna anger heltalsvillkoret',()=>{
 for(const id of ['1.16','1.68','1.69','1.132','1.299']){const q=bank.find(q=>q.id===id);assert.ok(q,id);assert.doesNotMatch(q.s,/identiteterna ändrar uttryckets form/);
  for(const d of q.spelDelar){assert.match(d.s,/Svar:/,id+d.etikett);assert.doesNotMatch(d.s,/identiteterna ändrar uttryckets form/,id+d.etikett);if(['1.16','1.68','1.69'].includes(id))assert.match(d.s,/n\\in\\mathbb Z/,id+d.etikett);}}
});
test('De angivna vinklarna och perioderna uppfyller ekvationerna',()=>{
 const r=x=>x*Math.PI/180, near=(a,b)=>assert.ok(Math.abs(a-b)<1e-10,`${a} != ${b}`);
 for(const n of [-3,-1,0,1,3]){near(Math.sin(r(180*n)),0);near(Math.cos(r(180+360*n)),-1);near(Math.tan(r(60+180*n)),Math.sqrt(3));near(Math.cos(r(90+180*n)),0);near(Math.cos(r(360*n)),1);}
 for(const n of [-2,-1,0,1,2]){for(const x of [90*n])near(2*Math.sin(r(x))*Math.cos(r(x)),0);for(const x of [60+180*n,120+180*n])near(Math.sin(r(x))**2,.75);for(const x of [45+90*n])near(2*Math.cos(r(x))**2-1,0);for(const x of [180*n,60+360*n,300+360*n])near(Math.sin(r(x))*(2*Math.cos(r(x))-1),0);}
 for(const x of [30,150])near(Math.sin(r(x)),.5);
 for(const x of [135,225])near(Math.cos(r(x)),-Math.sqrt(2)/2);
 for(const x of [135,315])near(Math.tan(r(x)),-1);
 for(const x of [150,210])near(2*Math.cos(r(x))+Math.sqrt(3),0);
 for(const x of [60,120,240,300])near(4*Math.cos(r(x))**2,1);
});
