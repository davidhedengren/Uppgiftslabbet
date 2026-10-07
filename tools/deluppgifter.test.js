'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8');
const analysis=fs.readFileSync(path.join(__dirname,'../analys/index.html'),'utf8');
const plain=value=>JSON.parse(JSON.stringify(value));
function load(c,source,names){
  for(const name of names){
    const m=new RegExp(`(?:async )?function ${name}\\(`).exec(source);
    assert.ok(m,`Saknar ${name}`);
    let end=source.indexOf('\n',m.index),script;
    while(end>=0){
      try{script=new vm.Script(source.slice(m.index,end));break;}
      catch(e){if(!(e instanceof SyntaxError)) throw e;}
      end=source.indexOf('\n',end+1);
    }
    assert.ok(script,`Kan inte läsa ${name}`);script.runInContext(c);
  }
}
function setup(){
  let uuid=0;
  const bank=['a','b','c','d'].map((id,i)=>({id,t:'<p>'+id+'</p>',s:'Facit '+id,
    kap:0,omr:'area'+i,niva:i===2?'C':'E',poang:i===2?'0/1/0':'1/0/0',familj:'Familj '+id,
    formaga:['procedur'],rättSvar:i,miniräknare:false,geogebra:false}));
  const c=vm.createContext({state:{blad:[bank[0],bank[3]],spår:'1c'},DB:{bank,omr:{}},AKTIV:{id:'ma1'},
    skyddaSparat:async()=>true,sparUuid:()=> 'group-'+(++uuid),structuredClone,
    rita:()=>{},ritaBlad:()=>{},dokumentTyp:()=> 'ovning',
    $:()=>({value:'Prov',checked:false}),sparLasaAlla:()=>[],sparInstallningar:()=>({}),AKTIV_SPAR_ID:null,
    dokumentOmraden:()=>[]});
  load(c,html,['sparSnapshotUppgift','bladDelbokstav','bladGrupper','bladNumrering',
    'bladNormaliseraGrupper','bladSlappUppgift','bladSeparera','bladFlytta','bladOrdna','bladSattProvdel',
    'sparByggDokument','sparUppgifterUrDokument','analysNiva','analysPoangSumma','analysDelar','byggAnalysOverforing']);
  return c;
}
test('Släpp på en uppgift skapar a/b/c med egna facit, poäng och original-ID:n',async()=>{
  const c=setup(),before=plain(c.DB.bank);
  assert.equal(await c.bladSlappUppgift('b','a'),true);
  assert.equal(await c.bladSlappUppgift('c','b'),true);
  assert.deepEqual(plain(c.bladNumrering().map(n=>n.etikett)),['1 a)','1 b)','1 c)','2.']);
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['a','b','c','d']);
  assert.deepEqual(plain(c.state.blad.map(t=>t.s)),['Facit a','Facit b','Facit c','Facit d']);
  assert.deepEqual(plain(c.state.blad.map(t=>t.poang)),['1/0/0','1/0/0','0/1/0','1/0/0']);
  assert.deepEqual(plain(c.DB.bank),before,'Bankuppgifterna får inte få dokumentmetadata');
});
test('En vald uppgift flyttas utan dubblett och behåller sin lokala redigering',async()=>{
  const c=setup();c.state.blad[1]={...c.state.blad[1],t:'Redigerad',_utrymme:25};
  await c.bladSlappUppgift('d','a');
  assert.equal(c.state.blad.length,2);
  assert.equal(c.state.blad[1].t,'Redigerad');assert.equal(c.state.blad[1]._utrymme,25);
  const before=plain(c.state.blad);
  assert.equal(await c.bladSlappUppgift('a','a'),false);
  assert.equal(await c.bladSlappUppgift('d','a'),false);
  assert.deepEqual(plain(c.state.blad),before);
});
test('Avbrutet skydd för ett sparat prov ändrar inget; okända mål godtas inte',async()=>{
  const c=setup(),before=plain(c.state.blad);let draws=0;
  c.ritaBlad=()=>draws++;c.skyddaSparat=async()=>false;
  assert.equal(await c.bladSlappUppgift('b','a'),false);
  assert.equal(await c.bladSlappUppgift('b','saknas'),false);
  assert.equal(await c.bladSlappUppgift('saknas','a'),false);
  assert.deepEqual(plain(c.state.blad),before);assert.equal(draws,0);
});
test('Kursbyte under skyddsdialogen får inte lägga gamla kursens uppgift i det nya bladet',async()=>{
  const c=setup();c.skyddaSparat=async()=>{c.AKTIV={id:'fy1'};c.state.blad=[];return true;};
  assert.equal(await c.bladSlappUppgift('b'),false);assert.equal(c.state.blad.length,0);
});
test('Släpp i tom yta ger en egen uppgift; ensam kvarvarande del får vanligt nummer',async()=>{
  const c=setup();await c.bladSlappUppgift('b','a');await c.bladSlappUppgift('b');
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['a','d','b']);
  assert.deepEqual(plain(c.bladNumrering().map(n=>n.etikett)),['1.','2.','3.']);
  assert.ok(c.state.blad.every(t=>!t._delgrupp));
});
test('Separera gör delarna till egna uppgifter och behåller deras ordning',async()=>{
  const c=setup();await c.bladSlappUppgift('b','a');await c.bladSlappUppgift('c','a');
  await c.bladSeparera('b');
  assert.deepEqual(plain(c.bladNumrering().map(n=>n.etikett)),['1.','2.','3.','4.']);
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['a','b','c','d']);
  assert.ok(c.state.blad.every(t=>!t._delgrupp));
});
test('Flyttpilar ändrar ordning inom en grupp och flyttar hela gruppen förbi andra uppgifter',async()=>{
  const c=setup();await c.bladSlappUppgift('b','a');await c.bladSlappUppgift('c','a');
  c.bladFlytta(1,-1);
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['b','a','c','d']);
  c.bladFlytta(2,1);
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['d','b','a','c']);
  assert.deepEqual(plain(c.bladNumrering().map(n=>n.etikett)),['1.','2 a)','2 b)','2 c)']);
});
test('Sortering av en del flyttar dess grupp; en egen uppgift kan inte splittra gruppen',async()=>{
  const c=setup();await c.bladSlappUppgift('b','a');await c.bladSlappUppgift('c','a');
  c.bladOrdna([0,2,3,1],1);
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['d','a','b','c']);
  c.bladOrdna([1,0,2,3],0);
  assert.deepEqual(plain(c.state.blad.map(t=>t.id)),['d','a','b','c']);
});
test('En grupp håller ihop i samma provdel både vid tillägg och byte av provdel',async()=>{
  const c=setup();c.state.blad[0]={...c.state.blad[0],_provdel:1};
  await c.bladSlappUppgift('b','a');assert.equal(c.state.blad[1]._provdel,1);
  c.bladSattProvdel(1,2);assert.equal(c.state.blad[0]._provdel,2);assert.equal(c.state.blad[1]._provdel,2);
  c.bladSattProvdel(0,0);assert.ok(c.state.blad.every(x=>!x._provdel));
});
test('Sparade snapshots återskapar grupperna; äldre dokument behåller vanlig numrering',async()=>{
  const c=setup();await c.bladSlappUppgift('b','a');
  const doc=c.sparByggDokument('Grupperat prov','save');
  c.state.blad=c.sparUppgifterUrDokument(plain(doc));
  assert.deepEqual(plain(c.bladNumrering().map(n=>n.etikett)),['1 a)','1 b)','2.']);
  c.state.blad=c.sparUppgifterUrDokument({tasks:[{bankId:'b',order:1},{bankId:'a',order:0}]});
  assert.deepEqual(plain(c.bladNumrering().map(n=>n.etikett)),['1.','2.']);
});
test('Analys får delarnas egna nivåer, poäng, ämnestaggar och samma gruppering',async()=>{
  const c=setup();await c.bladSlappUppgift('c','a');
  const transfer=plain(c.byggAnalysOverforing());
  assert.deepEqual(transfer.data.tasks.map(t=>t.level),[1,3,1]);
  assert.deepEqual(transfer.data.tasks.map(t=>t.areas),[['area0'],['area2'],['area3']]);
  assert.equal(transfer.data.tasks[0].source.documentGroup,transfer.data.tasks[1].source.documentGroup);
  const a=vm.createContext({state:{tasks:transfer.data.tasks},validTasks:()=>transfer.data.tasks,nextId:100,
    partLevel:(p,t)=>p.level||t.level,commitBuild:()=>{}});
  load(a,analysis,['letter','taskNo','partCode','dupTask']);
  assert.deepEqual(transfer.data.tasks.map(t=>a.taskNo(t)),['1a','1b',2]);
  assert.equal(a.partCode(1,0,1),'1b');
  assert.equal(a.partCode(0,1,2),'1a.b');
  a.dupTask(0);
  assert.deepEqual(plain(a.state.tasks.map(t=>a.taskNo(t))),['1a','1b',2,3]);
  assert.ok(!a.state.tasks[2].source.documentGroup);
});
test('Långa grupper fortsätter med aa) efter z)',()=>{
  const c=setup();c.state.blad=Array.from({length:28},(_,i)=>({id:String(i),_delgrupp:'g'}));
  assert.equal(c.bladNumrering()[25].etikett,'1 z)');
  assert.equal(c.bladNumrering()[26].etikett,'1 aa)');
});
