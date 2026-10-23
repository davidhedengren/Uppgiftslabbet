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
  for(const id of ['ma1','ma2','mato1','mato2']){
   const started=await page.evaluate(async id=>{
    const kurs=KURSER.find(k=>k.id===id);
    return await väljKurs(kurs,document.querySelector('[data-kurs="'+id+'"]'));
   },id);
   assert.equal(started,true);
   const tracks=await page.evaluate(()=>[...new Set(DB.bank.filter(q=>q.omr==='np_repetition').flatMap(q=>q.kurs))]);
   for(const track of tracks){
    const info=await page.evaluate(track=>{
     state.spår=track;byggTräd();
     const tasks=variantBank().filter(q=>q.omr==='np_repetition');
     state.omr=new Set([tasks[0].kap+':np_repetition']);rita();
     return {
      track,last:document.querySelector('.kapgrupp:last-child .kaprad').textContent,
      expected:DB.bank.filter(q=>q.omr==='np_repetition'&&q.kurs.includes(track)).map(q=>q.id).sort(),
      ids:tasks.map(q=>q.id).sort(),
      rendered:[...document.querySelectorAll('#lista article.kort')].map(e=>e.dataset.id).sort(),
      latex:document.querySelectorAll('#lista .katex-error').length,
      explanation:document.querySelector('.kapgrupp:last-child .np-repetition-info')?.textContent,
      alternatives:tasks.filter(q=>q.alternativ).map(q=>({id:q.id,visible:q.alternativ.every(a=>uppgiftsText(q).includes(a.txt))}))
     };
    },track);
    assert.match(info.last,/Repetera inför Nationella provet/);
    assert.match(info.explanation,/inte officiella/);
    assert.deepEqual(info.ids,info.expected);assert.deepEqual(info.rendered,info.expected);
    assert.equal(info.latex,0);assert.ok(info.alternatives.every(a=>a.visible));
    rows.push({course:id,...info});
   }
  }
  const out=process.env.REVIEW_OUT||'/tmp/np-repetition';fs.mkdirSync(out,{recursive:true});
  await page.screenshot({path:out+'/uppgiftslabbet.png',fullPage:true});
  fs.writeFileSync(out+'/uppgiftslabbet.json',JSON.stringify({rows,errors},null,2));
  assert.deepEqual(errors,[]);console.log({tracks:rows.length,errors});
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
