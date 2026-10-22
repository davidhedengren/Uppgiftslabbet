'use strict';
/* Påfyllnad 2026-10-22: 93 kort på nivå 1 i Ma2:s ekvationssystem (1.900–1.992). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));
const nya=B.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===1&&n>=900&&n<=992;});
const get=id=>{const t=nya.find(x=>x.id===id);assert.ok(t,id);return t;};

test('93 kort på nivå 1, tre obekanta bara för 2c',()=>{
  assert.equal(nya.length,93);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.equal(t.poang,'1/0/0',t.id);
    assert.deepEqual(t.kurs,t.omr==='ekvationssystem_tre_obekanta'?['2c']:['2a','2b','2c'],t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    if(t.svarstyp==='flera_delar'){assert.equal(t.svarEtiketter.length,t.rättSvar.length,t.id);assert.equal(t.svarsstruktur,'ordnad',t.id);
      assert.deepEqual(t.självrättning,t.rättSvar.map(()=>true),t.id);}
  }
  assert.deepEqual(per,{substitutionsmetoden:18,additionsmetoden:18,linjara_ekvationssystem:15,ekvationssystem_tillampningar:18,ekvationssystem_tre_obekanta:14,grafisk_losning_ekvationssystem:10});
});

test('Facit uppfyller systemen',()=>{
  // id: lista av funktioner som ska bli 0 för (x, y[, z]) = rättSvar
  const S={'1.900':[(x,y)=>y-2*x,(x,y)=>x+y-9],'1.901':[(x,y)=>y-x-1,(x,y)=>x+y-7],'1.902':[(x,y)=>x-3,(x,y)=>2*x+y-10],'1.903':[(x,y)=>y-4,(x,y)=>x+2*y-13],
    '1.907':[(x,y)=>y-3*x,(x,y)=>y-x-4],'1.908':[(x,y)=>x-2*y,(x,y)=>x+y-12],'1.912':[(x,y)=>y+x-6,(x,y)=>y-2*x],'1.913':[(x,y)=>y-2*x+1,(x,y)=>x+y-5],
    '1.914':[(x,y)=>x-y-2,(x,y)=>x+y-10],'1.917':[(x,y)=>y-5,(x,y)=>y-2*x-1],
    '1.918':[(x,y)=>x+y-10,(x,y)=>x-y-2],'1.920':[(x,y)=>2*x+y-8,(x,y)=>x-y-1],'1.921':[(x,y)=>x+2*y-9,(x,y)=>-x+3*y-1],'1.922':[(x,y)=>3*x+y-14,(x,y)=>x+y-6],
    '1.924':[(x,y)=>2*x+3*y-12,(x,y)=>-2*x+y-4],'1.926':[(x,y)=>4*x+y-13,(x,y)=>2*x-y-5],'1.927':[(a,b)=>a+b-15,(a,b)=>a-b-3],'1.929':[(x,y)=>3*x-y-5,(x,y)=>x+y-7],
    '1.931':[(x,y)=>x+3*y-11,(x,y)=>x-3*y+1],'1.933':[(x,y)=>-x+y-1,(x,y)=>x+y-7],'1.934':[(x,y)=>6*x+y-20,(x,y)=>6*x-y-16],'1.935':[(x,y)=>x+y,(x,y)=>x-y-6],
    '1.939':[(x,y)=>x+y-20,(x,y)=>x-y-4],'1.941':[(x,y)=>x+y-9,(x,y)=>y-x-1],'1.944':[(a,b)=>a+b-30,(a,b)=>a-b-4],'1.945':[(l,b)=>2*l+2*b-24,(l,b)=>l-2*b],
    '1.946':[(x,y)=>x-y,(x,y)=>x+y-10],'1.949':[(a,b)=>a+b-300,(a,b)=>a-b-100],'1.950':[(x,y)=>x+y-18,(x,y)=>x-2*y],
    '1.952':[(k,b)=>k+b-50,(k,b)=>k+2*b-70],'1.953':[(p,s)=>3*p+s-35,(p,s)=>2*p+s-25],'1.954':[(k,s)=>s+2*k-34,(k,s)=>s+3*k-46],'1.955':[(k,a)=>a+5*k-150,(k,a)=>a+10*k-250],
    '1.956':[(x,y)=>x+y-50,(x,y)=>x-y-10],'1.957':[(l,m)=>l-m-3,(l,m)=>l+m-21],'1.959':[(a,p)=>2*a+p-13,(a,p)=>a+p-9],'1.960':[(x,y)=>y-100*x,(x,y)=>y-300-50*x],
    '1.961':[(k,v)=>k+v-10,(k,v)=>v-4*k],'1.962':[(s,l)=>4*s+2*l-26,(s,l)=>2*s+2*l-16],'1.963':[(x,y)=>y-50-2*x,(x,y)=>y-10-6*x],'1.964':[(d,e)=>d+e-1500,(d,e)=>2*d+e-2400],
    '1.965':[(a,b)=>a+b-14,(a,b)=>a-b-2],'1.967':[(a,b)=>a+b-40,(a,b)=>a-3*b],'1.968':[(l,s)=>l+s-10,(l,s)=>l-s-2],
    '1.969':[(x,y,z)=>x+y+z-9,(x,y,z)=>y+z-5,(x,y,z)=>z-2],'1.970':[(x,y,z)=>x-1,(x,y,z)=>x+y-4,(x,y,z)=>x+y+z-10],'1.971':[(x,y,z)=>x+y+z-10,(x,y,z)=>y-3,(x,y,z)=>z-2],
    '1.974':[(x,y,z)=>x+y+z-12,(x,y,z)=>x-y,(x,y,z)=>y-z],'1.977':[(x,y,z)=>2*x-6,(x,y,z)=>x+y-5,(x,y,z)=>y+z-7],'1.980':[(x,y,z)=>x+y+z-10,(x,y,z)=>x-y,(x,y,z)=>z-4],
    '1.981':[(x,y,z)=>x-y-1,(x,y,z)=>y-2,(x,y,z)=>z-x-y],'1.982':[(x,y,z)=>x+y+z-11,(x,y,z)=>y-2*x,(x,y,z)=>z-x-3],
    '1.983':[(x,y)=>y-x-1,(x,y)=>y+x-5],'1.984':[(x,y)=>y+2*x+1,(x,y)=>y-x-2],'1.985':[(x,y)=>y-x+4,(x,y)=>y+0.5*x+1],'1.986':[(x,y)=>x+2,(x,y)=>y-3],
    '1.988':[(x,y)=>y-2*x-1,(x,y)=>y+x-7],'1.989':[(x,y)=>y-x-5,(x,y)=>y+2*x+4],'1.990':[(x,y)=>y-2*x+3,(x,y)=>y+x-3]};
  for(const [id,f] of Object.entries(S)){const v=get(id).rättSvar;for(const g of f)assert.ok(Math.abs(g(...v))<1e-12,`${id}: ${v}`);}
  assert.equal(get('1.905').rättSvar,4);assert.equal(get('1.909').rättSvar,3);assert.equal(get('1.915').rättSvar,2);
  assert.equal(get('1.923').rättSvar,-2);assert.equal(get('1.925').rättSvar,5);assert.equal(get('1.930').rättSvar,2);
  assert.equal(get('1.975').rättSvar,6);assert.equal(get('1.976').rättSvar,15-9);assert.deepEqual(get('1.979').rättSvar,[6,10]);
});
