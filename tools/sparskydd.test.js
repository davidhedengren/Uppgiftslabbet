'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8');

// Kör appens faktiska funktioner, med lokal lagring och serveranrop isolerade.
function setup(names){
  const values=new Map(), calls=[];
  const c=vm.createContext({
    console,clearTimeout,clearInterval,setTimeout:()=>0,
    document:{getElementById:()=>null},
    AKTIV:{id:'fy1'},AKTIV_SPAR_ID:'local',SKYDD_BEKRÄFTAT:null,sparSenastTömt:null,
    state:{blad:[{id:'2.1',t:'Uppgift',poang:{E:1}}]},
    DELNING:{id:'account',kurs:'fy1',namn:'Prov',synkad:'original',revision:1,bas:{}},
    localStorage:{getItem:k=>values.get(k)||null,setItem:(k,v)=>values.set(k,v)},
    SPAR_KEY:'saved',confirm:()=>true,alert:()=>{},
    $:()=>({value:'Övningsblad'}),
    sparUuid:()=> 'backup',sparInstallningar:()=>({title:'Övningsblad'}),
    dokumentTyp:()=> 'ovning',dokumentOmraden:()=>[],sparSnapshotUppgift:x=>({...x}),
    sparFormatTid:x=>x,sparStatus:()=>{},sparVisaSenast:()=>{},
    sparRensaUtkast:()=>{},sparAutosparaNu:()=>{},rita:()=>{},ritaBlad:()=>{},
    sparSammaInnehåll:()=>false,sparLaddaId:()=>{},
    delningRitaStatus:()=>{},delningByggData:()=>({tasks:[{id:'changed'}]}),
    delningKanon:JSON.stringify,ulSession:{access_token:'test-only'},
    kontoAktivt:()=>true,ulMeddela:()=>{},
    ulRpc:async(name,args)=>{ calls.push({name,args}); return {ok:true,revision:name==='ul_status'?1:2}; }
  });
  for(const name of ['sparLasaAlla','sparSkrivAlla',...names]){
    const match=new RegExp(`(?:async )?function ${name}\\(`).exec(html);
    assert.ok(match,`Missing function ${name}`);
    vm.runInContext(html.slice(match.index,html.indexOf('\n}',match.index)+2),c);
  }
  return {c,values,calls};
}

test('Börja om kan avbrytas utan att blad eller original ändras',()=>{
  const {c,values}=setup(['sparByggDokument','delningKoppla','sparNyttDokument']);
  c.confirm=()=>false;
  assert.equal(c.sparNyttDokument(),false);
  assert.equal(c.state.blad.length,1);
  assert.equal(c.DELNING.id,'account');
  assert.equal(values.size,0);
});
test('Börja om säkerhetskopierar innehållet och kopplar loss båda originalen',()=>{
  const {c,values}=setup(['sparByggDokument','delningKoppla','sparNyttDokument']);
  assert.equal(c.sparNyttDokument(),true);
  const backup=JSON.parse(values.get('saved'))[0];
  assert.equal(backup.tasks[0].snapshot.id,'2.1');
  assert.equal(backup.settings.title,'Övningsblad');
  assert.equal(c.state.blad.length,0);
  assert.equal(c.DELNING.id,null);
  assert.equal(c.AKTIV_SPAR_ID,null);
});
test('Full lokal lagring får inte tömma bladet',()=>{
  const {c}=setup(['sparByggDokument','delningKoppla','sparNyttDokument']);
  c.localStorage.setItem=()=>{throw new Error('QuotaExceededError');};
  assert.equal(c.sparNyttDokument(),false);
  assert.equal(c.state.blad.length,1);
  assert.equal(c.DELNING.id,'account');
});
test('Bakgrundssynk får aldrig skicka ul_spara',async()=>{
  const {c,calls}=setup(['delningSkicka','delningSynka']);
  await c.delningSynka(false);
  await c.delningSkicka('account');
  assert.equal(calls.length,0);
  await c.delningSynka(true);
  assert.deepEqual(calls.map(x=>x.name),['ul_status']);
  assert.equal(c.DELNING.revision,1);
});
test('Explicit sparning skriver innehållet med versionskontroll',async()=>{
  const {c,calls}=setup(['delningSkicka','delningSynka']);
  await c.delningSynka(false,{spara:true});
  assert.equal(calls.length,1);
  assert.equal(calls[0].name,'ul_spara');
  assert.equal(calls[0].args.p_revision,1);
  assert.equal(c.DELNING.revision,2);
});
test('Stängning av fliken sparar endast arbetsutkastet',()=>{
  const {c,calls}=setup(['delningSkickaVidStängning']);
  let drafts=0;
  c.fetch=()=>{throw new Error('Originalet får inte skrivas');};
  c.sparAutosparaNu=()=>drafts++;
  c.delningSkickaVidStängning();
  assert.equal(drafts,1);
  assert.equal(calls.length,0);
});
test('Spara som kopia skickar aldrig ändringar till kontooriginalet',async()=>{
  const {c,calls}=setup(['kontoSpara']);
  c.delningSynka=()=>{throw new Error('Originalet får inte synkas');};
  c.delningKoppla=()=>{}; c.delningAktivera=()=>{};
  await c.kontoSpara('Prov',{kopia:true});
  assert.deepEqual(calls.map(x=>x.name),['ul_skapa']);
  assert.equal(calls[0].args.p_namn,'Prov – kopia');
});
test('Avbruten kontosparning ändrar varken innehåll eller namn',async()=>{
  const {c,calls}=setup(['kontoSpara']);
  c.confirm=()=>false;
  await c.kontoSpara('Nytt namn');
  assert.equal(calls.length,0);
});
test('Misslyckad explicit sparning får inte rapporteras som lyckad',async()=>{
  const {c}=setup(['delningSkicka','delningSynka']);
  c.ulRpc=async()=>{throw new Error('Ingen kontakt');};
  await assert.rejects(c.delningSynka(false,{spara:true}),/Ingen kontakt/);
  assert.equal(c.DELNING.upptagen,false);
  assert.equal(c.DELNING.revision,1);
});
test('Lokalt sparat original kräver bekräftelse för överskrivning',()=>{
  const {c,values}=setup(['sparByggDokument','sparSparaManuellt']);
  values.set('saved',JSON.stringify([{id:'local',tasks:[{bankId:'old'}]}]));
  c.confirm=()=>false;
  assert.equal(c.sparSparaManuellt('Prov'),null);
  assert.equal(JSON.parse(values.get('saved'))[0].tasks[0].bankId,'old');
});
test('Lokal kopia bevarar originalets uppgifter',()=>{
  const {c,values}=setup(['sparByggDokument','sparSparaManuellt']);
  values.set('saved',JSON.stringify([{id:'local',tasks:[{bankId:'old'}]}]));
  c.confirm=()=>{throw new Error('Kopian ska inte ersätta originalet');};
  c.sparSparaManuellt('Prov',{kopia:true});
  const docs=JSON.parse(values.get('saved'));
  assert.equal(docs.find(x=>x.id==='local').tasks[0].bankId,'old');
  assert.equal(docs.find(x=>x.id==='backup').tasks[0].bankId,'2.1');
});
test('Osparade kontoutkast bevaras som separat dokument vid omladdning',()=>{
  const {c,values}=setup(['sparParkeraSparatUtkast']);
  const draft={course:'fy1',tasks:[{bankId:'changed'}],settings:{},
    shared:{id:'account',namn:'Prov',modified:true},updatedAt:'2026-10-07'};
  assert.equal(c.sparParkeraSparatUtkast(draft),true);
  const copy=JSON.parse(values.get('saved'))[0];
  assert.equal(copy.tasks[0].bankId,'changed');
  assert.equal(copy.shared,null);
  assert.equal(copy.activeSaveId,null);
});
