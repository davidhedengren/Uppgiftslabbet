'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterma2.js'),'utf8'),ctx);
const models=require('./fixtures/ma2-statistik-referenser.json'),get=id=>ctx.window.BANKMA2.find(q=>q.id===id),plain=x=>JSON.parse(JSON.stringify(x));
const sum=v=>v.reduce((a,b)=>a+b,0),mean=v=>sum(v)/v.length;
const med=v=>{const a=v.slice().sort((a,b)=>a-b);return(a[Math.floor((a.length-1)/2)]+a[Math.floor(a.length/2)])/2;};
const five=v=>{const a=v.slice().sort((a,b)=>a-b),h=Math.floor(a.length/2);return[a[0],med(a.slice(0,h)),med(a),med(a.slice(-h)),a.at(-1)];};
const iqr=v=>{const a=five(v);return a[3]-a[1];},sd=v=>Math.sqrt(mean(v.map(x=>(x-mean(v))**2))),pair=v=>[mean(v),sd(v)];
const mode=v=>{const c=new Map();v.forEach(x=>c.set(x,(c.get(x)||0)+1));return [...c].sort((a,b)=>b[1]-a[1])[0][0];};
function close(a,b){if(Array.isArray(b)){assert.ok(Array.isArray(a));assert.equal(a.length,b.length);b.forEach((x,i)=>close(a[i],x));}else if(typeof b==='number')assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);else assert.equal(a,b);}
function expected(m){const v=m.values;switch(m.type){
 case'percentiles':{const p=Object.fromEntries(m.percentiles);return m.id==='4.352'?[p[50],m.N*.1,m.N*.5]:[p[75]-p[25],m.N*.8,10];}
 case'group_percentiles':return[m.rows.find(r=>r[0]===50).slice(1),m.sizes.map(x=>x/4)];
 case'inverse_percentile':return m.base+m.between/m.N*100;
 case'boxes':{const [a,b]=m.rows.map(r=>r[1]);return m.id==='4.356'?['A',[a[3]-a[1],b[3]-b[1]],[a[4]-a[0],b[4]-b[0]]]:['B','B','nej'];}
 case'percentile_box':return[75-25,10+(100-90),'nej'];
 case'construct_box':return null;
 case'five_from_box':return mean([m.five[0],2*m.five[1]-m.five[0],m.five[2],2*m.five[3]-m.five[4],m.five[4]]);
 case'same_box':return[[mean(m.A),mean(m.B)],JSON.stringify(five(m.A))===JSON.stringify(five(m.B))?'ja':'nej'];
 case'remove':return v.filter((x,i)=>JSON.stringify(five(v.filter((_,j)=>j!==i)))===JSON.stringify(m.rows[1][1]));
 case'data':return[med(v),mode(v),pair(v),iqr(v)];
 case'histogram':{const mid=m.counts.flatMap((c,i)=>Array(c).fill((m.edges[i]+m.edges[i+1])/2));close(v,mid);return[pair(mid),m.id==='4.365'?'nej':[5,10]];}
 case'pooled_mean':return[sum(m.counts.map((n,i)=>n*m.means[i]))/sum(m.counts),'nej'];
 case'missing_mean':return m.N*m.mean-sum(m.known);
 case'new_member':return m.after[0]*m.after[1]-m.before[0]*m.before[1];
 case'max_integer':return m.N*m.mean-2-2*m.median;
 case'append_values':return[pair(v),sd(v.concat(m.added))<sd(v)?'mindre':'större'];
 case'transform_summary':return[(m.mean+m.shift)*m.scale,m.sd*Math.abs(m.scale),(m.median+m.shift)*m.scale];
 case'weighted_data':return[pair(v),med(v),mode(v)];
 case'inverse_count':return(1-m.above/m.N)*100;
 case'count_below':return m.N*m.percentile/100;
 case'count_above':return m.N*(100-m.percentile)/100;
 case'quartiles_frequency':return five(v).slice(1,4);
 case'quartiles_dots':return[med(v),[five(v)[1],five(v)[3],iqr(v)]];
 case'quartile_as_percentile':return m.quartiles[0];
 case'between_percentiles':return m.N*(m.p[1]-m.p[0])/100;
 case'missing_quartile':return m.Q1+m.IQR;
 case'nonuniform_quartiles':case'invariants':case'choose_data':case'interpret_percentile':return null;
 default:throw Error(m.type);
}}
test('35 uppgifters facit kontrolleras med självständiga beräkningar',()=>{assert.equal(models.length,35);for(const m of models)close(plain(get(m.id).rättSvar),expected(m));});
test('Alternativen skiljer lägesmått, spridning och percentiltolkning åt',()=>{
 const chosen=id=>get(id).alternativ.flatMap((a,i)=>a.ratt?[i]:[]);
 close(chosen('4.363'),[1]);close(chosen('4.78'),[0]);
 const inv=models.find(m=>m.id==='4.374'),f=[mean,med,v=>Math.max(...v)-Math.min(...v),iqr,sd];close(chosen(inv.id),f.flatMap((fn,i)=>Math.abs(fn(inv.A)-fn(inv.B))<1e-9?[i]:[]));
 const m=models.find(m=>m.id==='4.375');close(chosen(m.id),m.lists.flatMap((v,i)=>mean(v)===m.mean&&med(v)===m.median&&mode(v)===m.mode?[i]:[]));
 for(const id of ['4.363','4.374','4.375','4.78'])assert.match(get(id).t,/Välj (ett|alla)/);
});
test('Kvartilkonvention, borttagning och största möjliga tal prövas uttömmande',()=>{
 const m=models.find(m=>m.type==='remove');close(five(m.values),m.rows[0][1]);close(expected(m),[4,5]);assert.equal(get(m.id).svarsstruktur,'mängd');assert.match(get(m.id).t,/mitten|mittersta/);
 let max=0,count=0;for(let a=1;a<=6;a++)for(let b=a;b<=6;b++)for(let d=6;d<=30;d++){const e=30-a-b-6-d;if(e>=d){max=Math.max(max,e);count++;}}
 assert.ok(count>0);assert.equal(max,get('4.370').rättSvar);close(five([2,4,7,10,14]),models.find(m=>m.id==='4.360').five);
});
test('Histogrammens staplar följer frekvenser och intervall; avrundning är en decimal',()=>{
 for(const m of models.filter(m=>m.type==='histogram')){const q=get(m.id),tags=[...q.t.matchAll(/<rect class="ref-hist"([^>]*)>/g)].map(x=>Object.fromEntries([...x[1].matchAll(/([\w-]+)="([^"]*)"/g)].map(y=>[y[1],y[2]])));assert.equal(tags.length,m.counts.length);
 const ceiling=Math.ceil(Math.max(...m.counts)/2)*2+2;tags.forEach((t,i)=>{assert.ok(Math.abs(+t.height/190*ceiling-m.counts[i])<.001);assert.ok(Math.abs(+t.x-(62+i/m.counts.length*384))<.001);assert.ok(Math.abs(+t.width-384/m.counts.length)<.001);assert.ok(Math.abs(+t.y + +t.height-245)<.002);});
 assert.match(q.spelDelar[0].fraga,/mittpunkt.*en decimal/);close(q.tolerans[0],[.05,.05]);assert.match(q.spelDelar[0].s,/uppskattning/);
 for(const x of q.rättSvar[0]){const rounded=Math.round(x*10)/10;assert.ok(Math.abs(x-rounded)<.05);assert.ok(Math.abs(x-(rounded+.1))>.05);assert.ok(Math.abs(x-(rounded-.1))>.05);}
 }
});
test('Lådornas kanter och medianer ligger på samma linjära skala som axeln',()=>{
 for(const m of models.filter(m=>['boxes','percentile_box','five_from_box','remove'].includes(m.type))){const q=get(m.id),[lo,hi]=m.axis,rows=m.rows||[['',m.five]],scale=x=>60+(x-lo)/(hi-lo)*390;
 const attrs=cls=>[...q.t.matchAll(new RegExp('<(?:rect|line) class="'+cls+'"([^>]*)>','g'))].map(x=>Object.fromEntries([...x[1].matchAll(/([\w-]+)="([^"]*)"/g)].map(y=>[y[1],y[2]])));
 const boxes=attrs('ref-box'),medians=attrs('ref-median');assert.equal(boxes.length,rows.length);rows.forEach((r,i)=>{assert.ok(Math.abs(+boxes[i].x-scale(r[1][1]))<.001);assert.ok(Math.abs(+boxes[i].width-(scale(r[1][3])-scale(r[1][1])))<.001);assert.ok(Math.abs(+medians[i].x1-scale(r[1][2]))<.001);});
 }
});
test('Tabeller innehåller källdata och alla kort har självständiga förutsättningar',()=>{
 let cards=0;for(const m of models){const q=get(m.id);assert.match(q.t,/<table|<svg/);assert.equal(q.kap,4);close(plain(q.kurs),['2a','2b','2c']);assert.equal(q.miniräknare,true);assert.doesNotMatch(q.s,/facit-steglista|<ol/);
 const cells=[...q.t.matchAll(/<td>(.*?)<\/td>/g)].map(x=>x[1]);const num=x=>Number(x.replace('−','-').replace(',','.'));
 if(['data','quartiles_frequency','weighted_data'].includes(m.type)){const v=[];for(let i=0;i<cells.length;i+=2)v.push(...Array(num(cells[i+1])).fill(num(cells[i])));close(v,m.values.slice().sort((a,b)=>a-b));}
 if(m.type==='percentiles')for(const [p,v]of m.percentiles)assert.ok(cells.includes('P'+p)&&cells.some(x=>num(x.replace(/ (kr|min)/,'').replaceAll(' ',''))===v));
 if(!q.spel){assert.equal(q.id,'4.359');assert.equal(q.självrättning,false);continue;}
 const parts=q.spelDelar||[q];cards+=parts.length;for(const d of parts){assert.ok(d.s&&d.ledtrad);assert.doesNotMatch(d.fraga||d.t,/svaret från|föregående del|använd ditt svar/i);assert.ok(d.traningsniva>=1&&d.traningsniva<=3);}
 if(q.spelDelar){assert.match(q.spelIntro,/<table|<svg/);assert.equal(q.spelDelar.length,q.rättSvar.length);q.spelDelar.forEach((p,i)=>{if(Array.isArray(q.rättSvar[i]))assert.equal(p.svarEtiketter.length,q.rättSvar[i].length);});}
 }assert.equal(cards,60);
});
test('Sex för svåra nivå-1-rutiner omkalibreras; enkla nya avläsningar finns kvar',()=>{
 for(const id of ['4.48','4.63','4.71','4.92','4.171','4.183'])assert.equal(get(id).traningsniva,2);
 for(const [id,part]of [['4.352',0],['4.353',0],['4.354',0],['4.356',2],['4.357',0],['4.358',2],['4.364',1],['4.373',2]])assert.equal(get(id).spelDelar[part].traningsniva,1);
});
