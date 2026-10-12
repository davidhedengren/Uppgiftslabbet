'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const html=fs.readFileSync(path.join(__dirname,'../index.html'),'utf8'),content={innerHTML:''};
const c=vm.createContext({
 MINA:{lista:[],inbjudningar:[],bank:null,sök:'',fel:null,lage:'mina'},
 document:{getElementById:id=>id==='minamodal'?{hidden:false}:content},
 KURSER:[{id:'ma2',titel:'Matematik nivå 2'}],
 minaPost:d=>`<i>${d.id}</i>`,minaBankPost:d=>`<i>${d.id}</i>`,
 sparLasaAlla:()=>[],ulEsc:x=>String(x),UL_IKON_PROV:'',UL_IKON_OVNING:''
});
for(const name of ['minaOmradesLista','minaRita']){
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
