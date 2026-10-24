/* Lokal visningskontroll, utan konto eller skrivning till Supabase. */
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM||'/usr/bin/chromium',args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1366,height:1000}}),errors=[],rows=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route('https://*.supabase.co/**',r=>r.abort());
  await page.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
  if(process.env.REVIEW_DEPS)await page.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{
   const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);
   return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],'package',m[2])});
  });
  await page.goto(process.env.REVIEW_URL||'http://localhost:8028');
  await page.waitForFunction(()=>typeof väljKurs==='function');
  for(const id of ['mato1']){
   const started=await page.evaluate(async id=>{
    const kurs=KURSER.find(k=>k.id===id);
    return await väljKurs(kurs,document.querySelector('[data-kurs="'+id+'"]'));
   },id);
   assert.equal(started,true);
   const tracks=await page.evaluate(()=>[...new Set(DB.bank.filter(q=>/^(1\.(92[5-9]|93[0-2])|3\.(1191|120[7-9]|121[0-4]))$/.test(q.id)).flatMap(q=>q.kurs))]);
   for(const track of tracks){
    const info=await page.evaluate(track=>{
     state.spår=track;byggTräd();
     const tasks=variantBank().filter(q=>/^(1\.(92[5-9]|93[0-2])|3\.(1191|120[7-9]|121[0-4]))$/.test(q.id));
     const checked=[];
     for(const q of tasks){
      state.omr=new Set([q.kap+':'+q.omr]);const list=urval();const position=list.findIndex(t=>t.id===q.id);
      rita(Math.floor(position/UPPGIFTER_PER_SIDA));
      checked.push({id:q.id,found:position>=0,rendered:!!document.querySelector('#lista article.kort[data-id=\"'+q.id+'\"]'),areaButton:!!document.querySelector('[data-omr=\"'+q.kap+':'+q.omr+'\"]')});
     }
     return {
      track,checked,oldButton:!!document.querySelector('[data-omr$=\":np_repetition\"]'),oldText:document.querySelector('#träd').textContent.includes('Repetera inför Nationella provet'),
      expected:DB.bank.filter(q=>/^(1\.(92[5-9]|93[0-2])|3\.(1191|120[7-9]|121[0-4]))$/.test(q.id)&&q.kurs.includes(track)).map(q=>q.id).sort(),
      ids:tasks.map(q=>q.id).sort(),
      latex:document.querySelectorAll('#lista .katex-error').length,
      explanation:document.querySelector('.kapgrupp:last-child .np-repetition-info')?.textContent,
      alternatives:tasks.filter(q=>q.alternativ).map(q=>({id:q.id,visible:q.alternativ.every(a=>uppgiftsText(q).includes(a.txt))}))
     };
    },track);
    assert.equal(info.oldButton,false);assert.equal(info.oldText,false);
    assert.ok(info.checked.every(q=>q.found&&q.rendered&&q.areaButton),JSON.stringify(info.checked));
    assert.deepEqual(info.ids,info.expected);
    assert.equal(info.latex,0);assert.ok(info.alternatives.every(a=>a.visible));
    rows.push({course:id,...info});
   }
  }
  const out=process.env.REVIEW_OUT||'/tmp/ma3-kontinuitet-deriverbarhet';fs.mkdirSync(out,{recursive:true});
  await page.screenshot({path:out+'/uppgiftslabbet.png',fullPage:true});
  fs.writeFileSync(out+'/uppgiftslabbet.json',JSON.stringify({rows,errors},null,2));
  assert.deepEqual(errors,[]);console.log({tracks:rows.length,errors});
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
