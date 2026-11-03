'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL);await p.waitForFunction(()=>typeof väljKurs==='function');await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true});
 for(const width of [390,1280]){await p.setViewportSize({width,height:900});for(const [course,id] of [['ma2','3.691'],['ma2','4.514'],['ma2','6.10'],['ma2','3.2064'],['ma1','5.554'],['ma1','5.97'],['mato1','4.23'],['mato1','4.274'],['mato1','4.537'],['mato1','4.548'],['mato1','4.108'],['mato1','4.249'],['mato2','2.17']]){
  assert.equal(await p.evaluate(course=>väljKurs(KURSER.find(k=>k.id===course),document.querySelector(`[data-kurs="${course}"]`)),course),true);
  assert.equal(await p.evaluate(({course,id})=>{state.spår=['ma2','mato2'].includes(course)?'2c':'1c';byggTräd();const q=variantBank().find(q=>q.id===id);if(!q)return false;state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},{course,id}),true,id);
  const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();await card.locator('.facitknapp').click();assert.equal(await card.locator('.katex-error').count(),0,id);
 }}assert.deepEqual(errors,[]);console.log('Alla rapporterade lärarkort och facit fungerar på mobil och dator.');
}finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
