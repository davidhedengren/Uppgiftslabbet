/* Kör mot lokal HTTP-server: REVIEW_URL=http://localhost:8028 node tools/panelstorlek.browser.cjs */
const {chromium}=require('playwright'),assert=require('node:assert/strict'),fs=require('fs'),path=require('path');
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.CHROMIUM||'/usr/bin/chromium',args:['--no-sandbox']});
 try{
  const page=await browser.newPage({viewport:{width:1366,height:768}}),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.route('https://**',r=>{
   const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex)@[^/]+\/(.+)$/);
   if(m&&process.env.REVIEW_DEPS)return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],'package',m[2])});
   return r.abort();
  });
  const open=async()=>{
   await page.goto(process.env.REVIEW_URL||'http://localhost:8028');
   await page.waitForFunction(()=>typeof väljKurs==='function'&&typeof renderMathInElement==='function');
   await page.evaluate(async()=>{
    document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true;
    await väljKurs(KURSER.find(k=>k.id==='mato1'),document.querySelector('[data-kurs="mato1"]'));
   });
   await page.locator('.panelavdelare').first().waitFor({state:'visible'});
   await page.waitForFunction(()=>document.querySelector('.arbetsyta').style.getPropertyValue('--panel-hoger'));
  };
  const dims=()=>page.evaluate(()=>{
   const y=document.querySelector('.arbetsyta'),b=s=>y.querySelector(s).getBoundingClientRect().width;
   return {left:b('.vänster'),middle:b('.mitten'),right:b('.höger'),width:y.clientWidth,overflow:document.documentElement.scrollWidth>innerWidth+1};
  });
  const wait=()=>page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  const drag=async(s,dx)=>{
   const box=await page.locator(`[data-sida="${s}"]`).boundingBox();
   await page.mouse.move(box.x+6,box.y+box.height*.3);await page.mouse.down();
   await page.mouse.move(box.x+6+dx,box.y+box.height*.3,{steps:8});await page.mouse.up();await wait();
  };
  await open();let d=await dims();assert.equal(d.right,300);assert.ok(d.middle>=800);assert.equal(d.overflow,false);
  await drag('hoger',40);assert.equal((await dims()).right,260);
  await drag('vanster',35);assert.equal((await dims()).left,287);
  await open();d=await dims();assert.equal(d.right,260);assert.equal(d.left,287);
  const right=page.locator('[data-sida="hoger"]');await right.focus();await page.keyboard.press('ArrowLeft');assert.equal((await dims()).right,270);
  await page.keyboard.press('Home');assert.equal((await dims()).right,300);
  await drag('hoger',-1000);d=await dims();assert.ok(d.middle>=380);assert.ok(d.right<=520);
  await right.dblclick();assert.equal((await dims()).right,300);
  await page.locator('[data-sida="vanster"]').dblclick();assert.equal((await dims()).left,252);
  // Desktop settings must not break smaller screens or become mobile grid rows.
  for(const width of [1024,961,960,768,390,1366,1920]){
   await page.setViewportSize({width,height:900});await wait();d=await dims();
   assert.equal(d.overflow,false,'overflow at '+width);
   if(width>960){assert.ok(d.middle>=380);assert.equal(d.right,width>1440?360:300);}
   else{assert.equal(await right.isVisible(),false);assert.ok(Math.abs(d.middle-d.width)<2);}
  }
  await page.setViewportSize({width:1366,height:768});await wait();
  await page.screenshot({path:process.env.REVIEW_SCREENSHOT||'/tmp/panelstorlek-laptop.png'});
  await page.emulateMedia({media:'print'});assert.equal(await right.isVisible(),false);assert.equal(await page.locator('.arbetsyta').isVisible(),false);
  assert.deepEqual(errors,[]);console.log('PASS: defaults, both drags, persistence, keyboard, reset, size limits, seven viewports, print, no page errors.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
