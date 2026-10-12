'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8'),content={innerHTML:''};
const elements=new Map();
const c=vm.createContext({
 MINA:{lista:[],inbjudningar:[],bank:null,sök:'',kurs:'',sortering:'senast',fel:null,lage:'mina'},
 document:{getElementById:id=>{if(id==='minaInnehall')return content;if(!elements.has(id))elements.set(id,{hidden:false,innerHTML:''});return elements.get(id);}},
 KURSER:[{id:'ma2',titel:'Matematik nivå 2',spår:[{id:'2b',etikett:'2b'},{id:'2c',etikett:'2c'}]},{id:'fy1',titel:'Fysik nivå 1'}],
 minaPost:d=>`<i>${d.id}</i>`,minaBankPost:d=>`<i>${d.id}</i>`,
 sparLasaAlla:()=>[],ulEsc:x=>String(x),UL_IKON_PROV:'',UL_IKON_OVNING:''
});
for(const name of ['minaOmradesLista','minaKursEtikett','minaSorteradLista','minaRitaVerktyg','minaRita']){
 const start=html.indexOf(`function ${name}(`);vm.runInContext(html.slice(start,html.indexOf('\n}',start)+2),c);
}
const owned={id:'eget-prov',namn:'Eget prov',kurs:'ma2',typ:'prov',roll:'agare',uppdaterad:'2026-10-12'};
const shared={id:'mottaget-prov',namn:'Geometriprov',kurs:'ma2',typ:'prov',roll:'medlem',uppdaterad:'2026-10-11',omraden:['Likformighet']};
const exercise={id:'mottaget-ovningsblad',namn:'Övningsblad',kurs:'ma2',typ:'ovningsblad',roll:'medlem',uppdaterad:'2026-10-10'};
test('Mina prov visar både ägda och mottagna prov och övningsblad',()=>{
 c.MINA.lage='mina';c.MINA.sök='';c.MINA.lista=[owned,shared,exercise];c.minaRita();
 for(const doc of c.MINA.lista)assert.ok(content.innerHTML.includes(`<i>${doc.id}</i>`),doc.id);
 assert.match(content.innerHTML,/Prov<\/h3><span class="mina-antal">2/);
});
test('Mottagna dokument kan sökas på namn, kurs och område',()=>{
 c.MINA.lage='mina';c.MINA.lista=[owned,shared,exercise];
 for(const term of ['geometri','likformighet','matematik']){
  c.MINA.sök=term;c.minaRita();assert.ok(content.innerHTML.includes('<i>mottaget-prov</i>'),term);
 }
 c.MINA.sök='saknas';c.minaRita();assert.ok(!content.innerHTML.includes('<i>mottaget-prov</i>'));c.MINA.sök='';
});
test('Gemensamma banken hämtar sin egen lista och visar inga personliga delningar',()=>{
 c.MINA.lage='bank';c.MINA.sök='';c.MINA.lista=[owned,shared,exercise];c.MINA.bank={skola:'Testskola',dokument:[{...owned,id:'publicerad-mall'}]};
 c.minaRita();assert.ok(content.innerHTML.includes('<i>publicerad-mall</i>'));
 assert.ok(!content.innerHTML.includes('<i>mottaget-prov</i>'));c.MINA.lage='mina';
});

const docs=[
 {...owned,id:'c',namn:'Prov 10',spar:'2c',agare:'Åsa',omraden:['Likformighet']},
 {...shared,id:'b',namn:'Prov 2',spar:'2b'},
 {...exercise,id:'f',namn:'Övning',kurs:'fy1',uppdaterad:'2026-10-13'}
];
const ids=()=>Array.from(c.minaSorteradLista(docs),d=>d.id);
test('Kurs och spår kan kombineras med sökning även för mottagna dokument',()=>{
 c.MINA.sök='';c.MINA.kurs=JSON.stringify(['ma2',null]);c.MINA.sortering='senast';
 assert.deepEqual(ids(),['c','b']);
 c.MINA.kurs=JSON.stringify(['ma2','2b']);assert.deepEqual(ids(),['b']);
 c.MINA.kurs='';c.MINA.sök='ma2c åsa likformighet';assert.deepEqual(ids(),['c']);
 c.MINA.kurs=JSON.stringify(['fy1',null]);assert.deepEqual(ids(),[]);
 c.MINA.kurs='';c.MINA.sök='';
});
test('Sorteringen använder datum, svenska kursnamn och naturlig namnordning utan att ändra källistan',()=>{
 c.MINA.kurs='';c.MINA.sök='';c.MINA.sortering='senast';assert.deepEqual(ids(),['f','c','b']);
 c.MINA.sortering='namn';assert.deepEqual(ids(),['b','c','f']);
 c.MINA.sortering='kurs';assert.deepEqual(ids(),['f','b','c']);
 assert.deepEqual(docs.map(d=>d.id),['c','b','f']);c.MINA.sortering='senast';
});
test('Kursval och antal byggs från aktuell vy, inte från personliga dokument i skolbanken',()=>{
 c.MINA.lista=docs;c.MINA.lage='mina';c.MINA.sök='prov';c.MINA.kurs='';c.minaRita();
 assert.equal(elements.get('minaTraffar').textContent,'Visar 2 av 3 dokument');
 assert.match(elements.get('minaKurs').innerHTML,/Fysik nivå 1/);
 c.MINA.lage='bank';c.MINA.sök='';c.MINA.bank={skola:'Testskola',dokument:[docs[0]]};c.minaRita();
 assert.doesNotMatch(elements.get('minaKurs').innerHTML,/Fysik/);
 assert.equal(elements.get('minaTraffar').textContent,'Visar 1 av 1 dokument');c.MINA.lage='mina';
});
