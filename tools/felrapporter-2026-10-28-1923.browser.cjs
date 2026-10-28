const {chromium}=require('playwright');
const assert=require('node:assert/strict'),path=require('node:path');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM||'/usr/bin/chromium',args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1280,height:900}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route('https://*.supabase.co/**',r=>r.abort());
  await page.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
  if(process.env.REVIEW_DEPS)await page.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{
   const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);
   return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],'package',m[2])});
  });
  await page.goto(process.env.REVIEW_URL||'http://127.0.0.1:8218');
  await page.waitForFunction(()=>typeof väljKurs==='function');
  assert.equal(await page.evaluate(()=>väljKurs(KURSER.find(k=>k.id==='ma2'),document.querySelector('[data-kurs="ma2"]'))),true);
  for(const track of ['2a','2b','2c']){
   const r=await page.evaluate(track=>{
    state.spår=track;byggTräd();const q=variantBank().find(x=>x.id==='3.669');
    state.omr=new Set([q.kap+':'+q.omr]);const list=urval(),position=list.findIndex(x=>x.id===q.id);
    rita(Math.floor(position/UPPGIFTER_PER_SIDA));
    const card=document.querySelector('#lista article.kort[data-id="3.669"]');
    return {found:position>=0,card:!!card,openQuestion:!altVisas(q),
     labels:[...card.querySelectorAll('svg text')].map(e=>e.textContent.trim()),latex:card.querySelectorAll('.katex-error').length};
   },track);
   assert.ok(r.found&&r.card&&r.openQuestion);assert.equal(r.latex,0);
   assert.ok(!r.labels.some(x=>['I','II','III','IV'].includes(x)),track);
  }
  assert.deepEqual(errors,[]);console.log('Ma2 3.669: öppen fråga och figur kontrollerad i alla tre spår.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
