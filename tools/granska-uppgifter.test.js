const test = require('node:test');
const assert = require('node:assert/strict');
const path = require('node:path');

const { granskaBank } = require('./granska-uppgifter.js');

const projektrot = path.resolve(__dirname, '..');
const struktur = {
  kapnamn: { '1': 'Algebra' },
  omr: { '1': { algebra: 'Algebraiska uttryck' } },
  spar: { '1': { algebra: ['1c'] } },
  sparTaggar: ['1c'],
  kravKurs: true,
};

function uppgift(overrides = {}) {
  return {
    id: '1.1', kap: 1, omr: 'algebra', kurs: ['1c'], niva: 'E', poang: '1/0/0',
    t: '<p>Beräkna \\(2+2\\).</p>', s: '<p>Svaret är \\(4\\).</p>',
    familj: 'Addition', formaga: ['procedur'], miniräknare: false, geogebra: false,
    svarstyp: 'manuell', rättSvar: null, tolerans: null, självrättning: false,
    ...overrides,
  };
}

const harKod = (r, kod, allvar) => r.fynd.some((f) => f.kod === kod && (!allvar || f.allvar === allvar));
const felkoder = (r) => r.fynd.filter((f) => f.allvar === 'ERROR').map((f) => f.kod);

test('grundformat passerar och ID-/nivåfel hittas', () => {
  assert.deepEqual(felkoder(granskaBank('test.js', [uppgift()], projektrot, struktur)), []);
  const r = granskaBank('test.js', [uppgift({id:'x'}), uppgift({id:'x'}), uppgift({id:'',niva:'',t:'',s:''}), uppgift({id:'z',niva:'B'})], projektrot, struktur);
  for (const kod of ['DUPLICATE_ID','MISSING_ID','MISSING_LEVEL','INVALID_LEVEL','MISSING_TASK_TEXT','MISSING_SOLUTION']) assert.ok(harKod(r, kod, 'ERROR'), kod);
});

test('kapitel och område valideras mot strukturfilen', () => {
  assert.ok(!harKod(granskaBank('test.js',[uppgift()],projektrot,struktur),'UNKNOWN_CHAPTER_AREA'));
  assert.ok(harKod(granskaBank('test.js',[uppgift({omr:'saknas'})],projektrot,struktur),'UNKNOWN_CHAPTER_AREA','ERROR'));
});

test('kurs- och spårtaggar valideras', () => {
  assert.ok(!harKod(granskaBank('test.js',[uppgift()],projektrot,struktur),'INVALID_COURSE_TAG'));
  const r=granskaBank('test.js',[uppgift({id:'1',kurs:[]}),uppgift({id:'2',kurs:['9z']})],projektrot,struktur);
  assert.ok(harKod(r,'MISSING_COURSE_TAGS','ERROR'));
  assert.ok(harKod(r,'INVALID_COURSE_TAG','ERROR'));
});

test('poängmetadata kan passera, saknas, vara trasig eller orimlig', () => {
  assert.ok(!harKod(granskaBank('test.js',[uppgift({poang:'(2/1/0)'})],projektrot,struktur),'INVALID_POINTS'));
  const r=granskaBank('test.js',[uppgift({id:'1',poang:''}),uppgift({id:'2',poang:'1/x/0'}),uppgift({id:'3',poang:'30/0/0'})],projektrot,struktur);
  assert.ok(harKod(r,'MISSING_POINTS','ERROR'));
  assert.ok(harKod(r,'INVALID_POINTS','ERROR'));
  assert.ok(harKod(r,'IMPLAUSIBLE_POINTS','WARNING'));
});

test('familj och förmåga följer faktiskt format', () => {
  assert.ok(!harKod(granskaBank('test.js',[uppgift({familj:['Addition'],formaga:['procedur','resonemang']})],projektrot,struktur),'MISSING_FAMILY'));
  const r=granskaBank('test.js',[uppgift({id:'1',familj:''}),uppgift({id:'2',formaga:[]}),uppgift({id:'3',formaga:['okänd']})],projektrot,struktur);
  assert.ok(harKod(r,'MISSING_FAMILY','ERROR'));
  assert.ok(harKod(r,'MISSING_ABILITY','ERROR'));
  assert.ok(harKod(r,'UNKNOWN_ABILITY','WARNING'));
});

test('miniräknare och geogebra måste vara booleska', () => {
  assert.ok(!harKod(granskaBank('test.js',[uppgift()],projektrot,struktur),'INVALID_AID_METADATA'));
  const r=granskaBank('test.js',[uppgift({miniräknare:undefined,geogebra:'nej'})],projektrot,struktur);
  assert.equal(r.fynd.filter((f)=>f.kod==='INVALID_AID_METADATA').length,2);
});

test('strukturerade deluppgifter och facit kontrolleras', () => {
  const bra=uppgift({svarstyp:'flera_delar',rättSvar:[2,3],självrättning:true,tolerans:[0,0],svarEtiketter:['a','b'],spelDelning:'deluppgifter',spelDelar:[{etikett:'a',t:'<p>1+1?</p>',s:'<p>2</p>'},{etikett:'b',fraga:'<p>1+2?</p>',s:'<p>3</p>'}]});
  const rb=granskaBank('test.js',[bra],projektrot,struktur);
  assert.ok(!harKod(rb,'EMPTY_SUBTASK')); assert.ok(!harKod(rb,'SUBTASK_SOLUTION_MISSING'));
  const dalig=uppgift({svarstyp:'flera_delar',rättSvar:[2],spelDelning:'deluppgifter',spelDelar:[{},{etikett:'b',t:'<p>Fråga</p>'}]});
  const r=granskaBank('test.js',[dalig],projektrot,struktur);
  assert.ok(harKod(r,'EMPTY_SUBTASK','ERROR'));
  assert.ok(harKod(r,'SUBTASK_SOLUTION_MISSING','WARNING'));
  assert.ok(harKod(r,'SUBTASK_ANSWER_COUNT_MISMATCH','WARNING'));
});

test('svarsantal jämförs på topnivå och nästlade strukturer tillåts', () => {
  const bra=uppgift({svarstyp:'flera_delar',rättSvar:[[1,2],3],svarEtiketter:['punkt','värde'],självrättning:[[true,true],true],tolerans:[[0,0],0]});
  assert.ok(!harKod(granskaBank('test.js',[bra],projektrot,struktur),'ANSWER_METADATA_COUNT_MISMATCH'));
  const r=granskaBank('test.js',[uppgift({svarstyp:'flera_delar',rättSvar:[1,2],svarEtiketter:['a','b','c']})],projektrot,struktur);
  assert.ok(harKod(r,'ANSWER_METADATA_COUNT_MISMATCH','WARNING'));
});

test('LaTeX-kontrollen godtar radbrytning med mått och hittar oavslutad matematik', () => {
  const bra=uppgift({t:'<p>\\(x^2\\)</p><p>\\[\\begin{cases}x=1\\\\[2pt]y=2\\end{cases}\\]</p>'});
  assert.ok(!harKod(granskaBank('test.js',[bra],projektrot,struktur),'BROKEN_LATEX'));
  const r=granskaBank('test.js',[uppgift({t:'<p>\\(\\frac{1}{2}</p>'})],projektrot,struktur);
  assert.ok(harKod(r,'BROKEN_LATEX','ERROR'));
});

test('farlig HTML skiljs från misstänkt browser-tolererad HTML', () => {
  assert.ok(!harKod(granskaBank('test.js',[uppgift({t:'<p><strong>Text</strong></p>'})],projektrot,struktur),'DANGEROUS_HTML'));
  const r=granskaBank('test.js',[uppgift({id:'1',t:'<script>alert(1)</script>'}),uppgift({id:'2',t:'<p><div>Text</div></p>'})],projektrot,struktur);
  assert.ok(harKod(r,'DANGEROUS_HTML','ERROR'));
  assert.ok(harKod(r,'SUSPECT_HTML','INFO'));
});

test('SVG parsas och måste ha giltig viewBox', () => {
  const bra=uppgift({t:'<svg viewBox="0 0 10 10"><path d="M0 0L1 1"/></svg>'});
  assert.ok(!harKod(granskaBank('test.js',[bra],projektrot,struktur),'BROKEN_SVG'));
  const r=granskaBank('test.js',[uppgift({id:'1',t:'<svg><path/></svg>'}),uppgift({id:'2',t:'<svg viewBox="0 0 10 10"><g></svg>'})],projektrot,struktur);
  assert.ok(harKod(r,'SVG_VIEWBOX_MISSING','ERROR'));
  assert.ok(harKod(r,'BROKEN_SVG','ERROR'));
});

test('lokala bilder kontrolleras och externa ignoreras', () => {
  const r=granskaBank('test.js',[uppgift({id:'1',t:'<img src="bilder/finns-inte.png" alt="x">'}),uppgift({id:'2',t:'<img src="https://example.com/bild.png" alt="x">'}),uppgift({id:'3',t:'<img src="logo.png" alt="x">'})],projektrot,struktur);
  assert.equal(r.fynd.filter((f)=>f.kod==='MISSING_IMAGE').length,1);
});

test('exakta dubbletter och mycket lika texter får olika allvar', () => {
  const r=granskaBank('test.js',[uppgift({id:'1',t:'<p>Beräkna 12 + 4 och redovisa din metod.</p>'}),uppgift({id:'2',t:'<p>Beräkna 12 + 4 och redovisa din metod.</p>'}),uppgift({id:'3',t:'<p>Beräkna 15 + 7 och redovisa din metod.</p>'})],projektrot,struktur);
  assert.ok(harKod(r,'EXACT_TEXT_DUPLICATE','WARNING'));
  assert.ok(harKod(r,'VERY_SIMILAR_TEXT','INFO'));
});

test('självrättning valideras och alternativ med markerat rätt svar tillåts', () => {
  const bra=[uppgift({id:'1',svarstyp:'numeriskt',rättSvar:4,tolerans:0,självrättning:true,svarFormat:'numeriskt'}),uppgift({id:'2',svarstyp:'alternativ',rättSvar:null,självrättning:true,alternativ:[{txt:'A',ratt:true},{txt:'B',ratt:false}]})];
  assert.ok(!harKod(granskaBank('test.js',bra,projektrot,struktur),'SELFCHECK_WITHOUT_ANSWER'));
  const r=granskaBank('test.js',[uppgift({id:'1',svarstyp:'numeriskt',rättSvar:null,självrättning:true}),uppgift({id:'2',rättSvar:[1,2],självrättning:[true],tolerans:-1}),uppgift({id:'3',svarstyp:'alternativ',rättSvar:null,självrättning:true,alternativ:[{txt:'A',ratt:false}]})],projektrot,struktur);
  assert.ok(harKod(r,'SELFCHECK_WITHOUT_ANSWER','WARNING'));
  assert.ok(harKod(r,'SELFCHECK_SHAPE_MISMATCH','WARNING'));
  assert.ok(harKod(r,'INVALID_TOLERANCE','ERROR'));
  assert.ok(harKod(r,'ALTERNATIVE_WITHOUT_CORRECT','ERROR'));
});

test('svarsmetadata som används genomgående får inte saknas', () => {
  const bra=granskaBank('test.js',[uppgift()],projektrot,struktur);
  assert.ok(!harKod(bra,'MISSING_ANSWER_TYPE'));
  const utanMetadata=uppgift({svarstyp:undefined});
  delete utanMetadata.rättSvar;
  delete utanMetadata.tolerans;
  const r=granskaBank('test.js',[utanMetadata],projektrot,struktur);
  assert.ok(harKod(r,'MISSING_ANSWER_TYPE','ERROR'));
  assert.ok(harKod(r,'MISSING_RIGHT_ANSWER_METADATA','ERROR'));
  assert.ok(harKod(r,'MISSING_TOLERANCE_METADATA','WARNING'));
});
