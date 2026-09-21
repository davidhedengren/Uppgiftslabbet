'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const crypto = require('node:crypto');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const { analyzeSvgFigures, buildReport, collectSvgStrings, extractAll, overlaySvg, resolveChromePath, validateBatchResults, verifyFindingTraceability } = require('./granska-svg.js');

function svg(body, attrs = '') {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120" width="200" height="120" ${attrs}>${body}</svg>`;
}

async function findings(markup) {
  const [result] = await analyzeSvgFigures([{ bank: 'test', taskId: 'T', svg: markup, paths: ['t'] }], { batchSize: 50 });
  return result.findings;
}

function has(items, code, severity) {
  return items.some((item) => item.code === code && (!severity || item.severity === severity));
}

function angleBase(arc, label = '<text x="55" y="70" font-size="12">90°</text>') {
  return svg(`<line x1="40" y1="80" x2="100" y2="80" stroke="black"/><line x1="40" y1="80" x2="40" y2="20" stroke="black"/>${arc}${label}`);
}

function fixtureRepo(tasks) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'svg-extract-test-'));
  const banks = [
    ['uppgifter.js', 'BANK'], ['uppgifter2.js', 'BANK2'], ['uppgifterma1.js', 'BANKMA1'],
    ['uppgifterma2.js', 'BANKMA2'], ['uppgiftermatf1.js', 'BANKMATF1'],
    ['uppgiftermato1.js', 'BANKMATO1'], ['uppgiftermato2.js', 'BANKMATO2']
  ];
  for (const [file, variable] of banks) fs.writeFileSync(path.join(dir, file), `window.${variable}=${JSON.stringify(file === 'uppgifter.js' ? tasks : [])};\n`);
  return dir;
}

function sourceFigure(overrides = {}) {
  const figure = {
    bank: 'test', course: 'Test', taskId: 'T', taskIndex: 0, taskHash: 'task-hash',
    figureIndex: 0, paths: ['t[svg:0]'], sourceKind: 'inline', sourceRefs: [],
    svg: svg('<text x="20" y="20">ok</text>'), ...overrides
  };
  figure.hash = crypto.createHash('sha256').update(figure.svg).digest('hex');
  figure.sourceKey = [figure.bank, figure.taskIndex, figure.taskId, figure.figureIndex, figure.hash, ...figure.paths].join('|');
  return figure;
}

test('clean figure has no findings', async () => {
  const result = await findings(svg('<line x1="20" y1="90" x2="180" y2="90" stroke="black"/><text x="100" y="30" text-anchor="middle" font-size="14">Rubrik</text>'));
  assert.deepEqual(result, []);
});

test('detects intentional text-line collision', async () => {
  const result = await findings(svg('<line x1="20" y1="60" x2="180" y2="60" stroke="black" stroke-width="3"/><text x="100" y="64" text-anchor="middle" font-size="18">korsning</text>'));
  assert.ok(has(result, 'TEXT_GEOMETRY_COLLISION', 'WARNING'));
});

test('detects text-text collision', async () => {
  const result = await findings(svg('<text x="70" y="60" font-size="20">ABC</text><text x="82" y="60" font-size="20">XYZ</text>'));
  assert.ok(has(result, 'TEXT_TEXT_COLLISION', 'WARNING'));
});

test('ignores exact duplicate text with the same content and bounding box', async () => {
  const result = await findings(svg('<text x="70" y="60" font-size="20">ABC</text><text x="70" y="60" font-size="20">ABC</text>'));
  assert.equal(has(result, 'TEXT_TEXT_COLLISION'), false);
});

test('detects point-label collision', async () => {
  const result = await findings(svg('<circle cx="70" cy="60" r="6" fill="black"/><text x="66" y="64" font-size="16">P</text>'));
  assert.ok(has(result, 'POINT_LABEL_COLLISION', 'WARNING'));
});

test('names measurement label crossing its segment', async () => {
  const result = await findings(svg('<line x1="25" y1="60" x2="175" y2="60" stroke="black" stroke-width="2"/><text x="100" y="65" text-anchor="middle" font-size="16">12 cm</text>'));
  assert.ok(has(result, 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'WARNING'));
});

test('text inside filled shapes away from their boundaries is not a geometry collision', async () => {
  const result = await findings(svg([
    '<rect x="10" y="10" width="50" height="90" fill="#eee" stroke="black"/><text x="35" y="60" text-anchor="middle" font-size="12">rect</text>',
    '<circle cx="100" cy="60" r="35" fill="#eee" stroke="black"/><text x="100" y="64" text-anchor="middle" font-size="12">circle</text>',
    '<polygon points="145,15 195,15 195,105 145,105" fill="#eee" stroke="black"/><text x="170" y="64" text-anchor="middle" font-size="12">polygon</text>'
  ].join('')));
  assert.equal(has(result, 'TEXT_GEOMETRY_COLLISION'), false);
});

test('coordinate-grid numeric tick labels do not create warning floods or become measurements', async () => {
  const lines = [30, 60, 90, 120, 150].map((x) => `<line x1="${x}" y1="15" x2="${x}" y2="105" stroke="#ddd"/>`).join('') +
    [30, 60, 90].map((y) => `<line x1="20" y1="${y}" x2="180" y2="${y}" stroke="#ddd"/>`).join('');
  const labels = [30, 60, 90, 120, 150].map((x, i) => `<text x="${x}" y="64" text-anchor="middle" font-size="10">${i - 2}</text>`).join('');
  const result = await findings(svg(lines + labels));
  assert.equal(result.filter((x) => /(?:TEXT_GEOMETRY|MEASUREMENT_LABEL)/.test(x.code)).length, 0);
});

test('aggregates one label intersecting multiple geometry pieces into one finding', async () => {
  const result = await findings(svg('<line x1="20" y1="60" x2="180" y2="60" stroke="black"/><polyline points="20,55 100,60 180,55" fill="none" stroke="black"/><text x="100" y="65" text-anchor="middle" font-size="16">12 cm</text>'));
  const collisions = result.filter((x) => x.code === 'MEASUREMENT_LABEL_CROSSES_GEOMETRY');
  assert.equal(collisions.length, 1);
  assert.equal(collisions[0].count, 2);
  assert.equal(collisions[0].elements.length, 3);
  assert.equal(collisions[0].affectedElementIds.length, 2);
});

test('detects partial and fully outside content plus edge clipping', async () => {
  const partial = await findings(svg('<rect x="185" y="30" width="30" height="20" fill="red"/>'));
  assert.ok(has(partial, 'OBJECT_PARTIALLY_OUTSIDE_VIEWBOX', 'WARNING'));
  assert.equal(partial.filter((x) => x.severity === 'WARNING').length, 1);
  assert.equal(has(partial, 'EDGE_CLIPPING', 'WARNING'), false);

  const outside = await findings(svg('<circle cx="240" cy="60" r="10" fill="red"/>'));
  assert.ok(has(outside, 'OBJECT_FULLY_OUTSIDE_VIEWBOX', 'ERROR'));
});

test('accepts correctly centered and aligned angle arc and degree label', async () => {
  const result = await findings(angleBase('<path d="M 65 80 A 25 25 0 0 0 40 55" fill="none" stroke="blue"/>'));
  assert.equal(result.some((x) => x.code.startsWith('ANGLE_') || x.code === 'DEGREE_LABEL_MISPLACED'), false);
});

test('warns when a confidently paired numeric degree label disagrees with the local angle', async () => {
  const result = await findings(angleBase('<path d="M 65 80 A 25 25 0 0 0 40 55" fill="none" stroke="blue"/>', '<text x="55" y="70" font-size="12">45°</text>'));
  assert.ok(has(result, 'ANGLE_LABEL_VALUE_MISMATCH', 'WARNING'));
});

test('skips angle-value comparison for symbolic labels and reversed uncertain arcs', async () => {
  const symbolic = await findings(angleBase('<path d="M 65 80 A 25 25 0 0 0 40 55" fill="none" stroke="blue"/>', '<text x="55" y="70" font-size="12">x°</text>'));
  assert.equal(has(symbolic, 'ANGLE_LABEL_VALUE_MISMATCH'), false);
  const reversed = await findings(angleBase('<path d="M 65 80 A 25 25 0 1 1 40 55" fill="none" stroke="blue"/>', '<text x="55" y="70" font-size="12">45°</text>'));
  assert.equal(has(reversed, 'ANGLE_LABEL_VALUE_MISMATCH'), false);
});

test('detects off-center angle arc', async () => {
  const result = await findings(angleBase('<path d="M 90 70 A 20 20 0 0 0 70 50" fill="none" stroke="blue"/>'));
  assert.ok(has(result, 'ANGLE_ARC_OFF_CENTER', 'WARNING'));
});

test('detects angle arc endpoint or direction mismatch with legs', async () => {
  const result = await findings(angleBase('<path d="M 65 80 A 25 25 0 0 1 40 105" fill="none" stroke="blue"/>'));
  assert.ok(has(result, 'ANGLE_ARC_DIRECTION_MISMATCH', 'WARNING'));
});

test('detects opposite-sweep angle arc even when both endpoints match the legs', async () => {
  const result = await findings(angleBase('<path d="M 65 80 A 25 25 0 1 1 40 55" fill="none" stroke="blue"/>'));
  assert.ok(has(result, 'ANGLE_ARC_DIRECTION_MISMATCH', 'WARNING'));
});

test('detects unreasonable degree label placement', async () => {
  const result = await findings(angleBase('<path d="M 65 80 A 25 25 0 0 0 40 55" fill="none" stroke="blue"/>', '<text x="155" y="20" font-size="12">90°</text>'));
  assert.ok(has(result, 'DEGREE_LABEL_MISPLACED', 'WARNING'));
});

test('does not let a wrong-side degree label suppress misplaced detection', async () => {
  const result = await findings(angleBase('<path d="M 65 80 A 25 25 0 0 0 40 55" fill="none" stroke="blue"/>', '<text x="55" y="103" font-size="12">90°</text>'));
  assert.ok(has(result, 'DEGREE_LABEL_MISPLACED', 'WARNING'));
});

test('pairs degree labels one-to-one so one label cannot satisfy two arcs', async () => {
  const result = await findings(svg([
    '<line x1="30" y1="95" x2="55" y2="95" stroke="black"/><line x1="30" y1="95" x2="30" y2="60" stroke="black"/><path d="M 45 95 A 15 15 0 0 0 30 80" fill="none" stroke="blue"/>',
    '<line x1="80" y1="95" x2="105" y2="95" stroke="black"/><line x1="80" y1="95" x2="80" y2="60" stroke="black"/><path d="M 95 95 A 15 15 0 0 0 80 80" fill="none" stroke="blue"/>',
    '<text x="55" y="84" text-anchor="middle" font-size="10">90°</text>'
  ].join('')));
  assert.ok(result.filter((x) => x.code === 'DEGREE_LABEL_MISPLACED').length >= 1);
});

test('pairs separate angle arcs with their local vertices and nearest degree labels', async () => {
  const result = await findings(svg([
    '<line x1="30" y1="95" x2="80" y2="95" stroke="black"/><line x1="30" y1="95" x2="30" y2="45" stroke="black"/>',
    '<path d="M 50 95 A 20 20 0 0 0 30 75" fill="none" stroke="blue"/><text x="43" y="82" font-size="10">90°</text>',
    '<line x1="125" y1="95" x2="180" y2="95" stroke="black"/><line x1="125" y1="95" x2="125" y2="40" stroke="black"/>',
    '<path d="M 145 95 A 20 20 0 0 0 125 75" fill="none" stroke="blue"/><text x="138" y="82" font-size="10">90°</text>'
  ].join('')));
  assert.equal(result.some((x) => x.code.startsWith('ANGLE_') || x.code === 'DEGREE_LABEL_MISPLACED'), false);
});

test('detects suspicious tiny, huge, or reversed angle arcs', async () => {
  const tiny = await findings(angleBase('<path d="M 42 80 A 2 2 0 0 0 40 78" fill="none" stroke="blue"/>'));
  assert.ok(has(tiny, 'ANGLE_ARC_SUSPICIOUS', 'INFO'));
  const huge = await findings(angleBase('<path d="M 130 80 A 90 90 0 1 0 40 -10" fill="none" stroke="blue"/>'));
  assert.ok(has(huge, 'ANGLE_ARC_SUSPICIOUS', 'INFO'));
});

test('detects obvious malformed geometry but accepts percentage SVG sizing', async () => {
  const validPercent = await findings('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120" width="100%" height="100%"><rect x="10" y="10" width="180" height="100"/></svg>');
  assert.equal(has(validPercent, 'INVALID_GEOMETRY'), false);
  const result = await findings(svg('<circle cx="50" cy="50" r="-4"/><path d="M 10 10 L nope 40" stroke="black"/>'));
  assert.ok(has(result, 'INVALID_GEOMETRY', 'ERROR'));
});

test('accepts SVG length units and percentages on coordinates and radii', async () => {
  const result = await findings('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120" width="200px" height="120px"><circle cx="50%" cy="60px" r="10%"/><rect x="1cm" y="2mm" width="20px" height="10pt"/></svg>');
  assert.equal(has(result, 'INVALID_GEOMETRY'), false);
});

test('detects deterministically truncated path command syntax', async () => {
  const result = await findings(svg('<path d="M 10 10 L" stroke="black"/>'));
  assert.ok(has(result, 'INVALID_GEOMETRY', 'ERROR'));
});

test('accepts separated and compact arc flags for absolute and relative repeated segments', async () => {
  const validPaths = [
    'M0 0 A10 10 0 0 0 10 20',
    'M0 0 A10 10 0 1 1 10 20',
    'M0 0 A10 10 0 0010 20',
    'M0 0 A10 10 0 0110 20',
    'M0 0 A10 10 0 10-10 20',
    'M0 0 A10 10 0 11-10 20',
    'M0 0 a10 10 0 0010 20',
    'M0 0 a10 10 0 01-10 20',
    'M0 0 A10 10 0 0110 20 12 12 0 10-5 6',
    'M0 0 a10 10 0 11-10 20 12 12 0 005-6'
  ];
  for (const d of validPaths) {
    const result = await findings(svg(`<path d="${d}"/>`));
    assert.equal(has(result, 'INVALID_GEOMETRY'), false, d);
  }
});

test('rejects invalid or malformed arc flags and incomplete arc groups', async () => {
  const invalidPaths = [
    'M0 0 A10 10 0 2 0 10 20',
    'M0 0 A10 10 0 0 3 10 20',
    'M0 0 A10 10 0 2-10 20',
    'M0 0 A10 10 0 0x10 20',
    'M0 0 A10 10 0 010e 20',
    'M0 0 A10 10 0 01',
    'M0 0 A10 10 0 0110'
  ];
  for (const d of invalidPaths) {
    assert.ok(has(await findings(svg(`<path d="${d}"/>`)), 'INVALID_GEOMETRY', 'ERROR'), d);
  }
});

test('preserves invalid initial-command, arc-radius, and general arity checks', async () => {
  const invalidPaths = [
    'L 10 10 M 20 20 L 40 40',
    'M 10 10 A -2 20 0 0 1 50 50',
    'M 10 10 A 20 -2 0 0 1 50 50',
    'M 10 10 L 20',
    'M 10 10 C 20 20 30 30 40'
  ];
  for (const d of invalidPaths) {
    assert.ok(has(await findings(svg(`<path d="${d}"/>`)), 'INVALID_GEOMETRY', 'ERROR'), d);
  }
  const valid = await findings(svg('<path d="M 10 10 20 20 30 10 L 40 20 50 10 A 10 10 0 0 1 60 20 10 10 0 1 0 80 20 Z"/>'));
  assert.equal(has(valid, 'INVALID_GEOMETRY'), false);
});

test('analyzes valid path geometry in inline SVG that omits xmlns', async () => {
  const result = await findings('<svg viewBox="0 0 200 120" width="200" height="120"><path d="M 10 100 L 190 100" stroke="black"/><text x="100" y="30">ok</text></svg>');
  assert.equal(has(result, 'INVALID_GEOMETRY'), false);
});

test('honors root viewBox scaling as well as nested transforms and text-anchor', async () => {
  const scaled = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120" width="400" height="240"><line x1="20" y1="90" x2="180" y2="90" stroke="black"/><text x="100" y="30" text-anchor="middle" font-size="14">Rubrik</text></svg>';
  assert.deepEqual(await findings(scaled), []);
  const result = await findings(svg('<g transform="translate(80 20) rotate(12)"><line x1="0" y1="70" x2="80" y2="70" stroke="black"/><text x="40" y="25" text-anchor="middle" dominant-baseline="middle" font-size="14">centrerad</text></g>'));
  assert.deepEqual(result, []);
});

test('ignores hidden and zero-area text elements', async () => {
  const result = await findings(svg('<line x1="20" y1="90" x2="180" y2="90" stroke="black"/><text x="0" y="0"><tspan display="none">ghost</tspan></text><text display="none" x="50" y="50">hidden</text>'));
  assert.deepEqual(result, []);
});

test('opaque label background suppresses covered geometry collision', async () => {
  const result = await findings(svg('<line x1="20" y1="60" x2="180" y2="60" stroke="black"/><rect x="72" y="45" width="56" height="24" fill="white"/><text x="100" y="62" text-anchor="middle" font-size="14">12 cm</text>'));
  assert.equal(has(result, 'MEASUREMENT_LABEL_CROSSES_GEOMETRY'), false);
  assert.equal(has(result, 'TEXT_GEOMETRY_COLLISION'), false);
});

test('sanitizes active SVG content before browser analysis and report embedding', async () => {
  const malicious = svg('<script>globalThis.__svgPwned=1</script><foreignObject><iframe src="https://evil.invalid/"></iframe></foreignObject><rect x="10" y="10" width="20" height="20" onload="globalThis.__svgPwned=2" fill="url(https://evil.invalid/a.svg#p)"/><use href="javascript:alert(1)"/><text x="50" y="50">safe</text>');
  const source = sourceFigure({ taskId: 'SEC', svg: malicious });
  const [result] = await analyzeSvgFigures([source]);
  assert.match(result.sanitizedSvg, /safe/);
  assert.doesNotMatch(result.sanitizedSvg, /script|foreignObject|iframe|onload|javascript:|https:\/\//i);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'svg-report-test-'));
  try {
    buildReport(dir, { banks: [{ bank: 'test', course: 'Test', tasks: 1, tasksContainingSvg: 1, rawOccurrences: 1, figures: 1 }], figures: [source], references: [] }, [result], 1);
    const html = fs.readFileSync(path.join(dir, 'SVG_GRANSKNING.html'), 'utf8');
    assert.doesNotMatch(html, /globalThis\.__svgPwned|foreignObject|iframe|onload|javascript:|https:\/\/evil\.invalid/i);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test('analyzes internal use geometry and reports unresolved or external references without loading them', async () => {
  const markup = svg('<defs><g id="segment" transform="translate(5 0)"><line x1="0" y1="0" x2="80" y2="0" stroke="black"/></g></defs><use href="#segment" x="40" y="60"/><use href="#missing"/><image href="https://evil.invalid/remote.svg"/><text x="85" y="65" text-anchor="middle" font-size="16">12 cm</text>');
  const result = await findings(markup);
  assert.ok(has(result, 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'WARNING'));
  assert.ok(has(result, 'UNRESOLVED_SVG_REFERENCE'));
  assert.ok(has(result, 'EXTERNAL_SVG_REFERENCE'));
});

test('expands forward-referenced nested use chains with transforms and cycle protection', async () => {
  const markup = svg('<use href="#outer" x="10" y="20" transform="translate(5 0)"/><defs><use id="outer" href="#middle" x="10"/><g id="middle"><use href="#inner" x="5" y="40"/></g><g id="inner" transform="translate(5 0)"><line x1="0" y1="0" x2="80" y2="0" stroke="black"/><use href="#cycle"/></g><g id="cycle"><use href="#cycle"/></g></defs><text x="75" y="65" text-anchor="middle" font-size="16">12 cm</text>');
  const result = await findings(markup);
  assert.ok(has(result, 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'WARNING'));
});

test('applies symbol viewBox viewport scaling when materializing use geometry', async () => {
  const markup = svg('<defs><symbol id="scaled" viewBox="0 0 10 10" preserveAspectRatio="none"><line x1="0" y1="5" x2="10" y2="5" stroke="black"/></symbol></defs><use href="#scaled" x="20" y="20" width="160" height="80"/><text x="100" y="65" text-anchor="middle" font-size="16">12 cm</text>');
  const result = await findings(markup);
  assert.ok(has(result, 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'WARNING'));
});

test('CLI chrome preflight honors a valid CHROME_PATH override', () => {
  const custom = process.execPath;
  assert.equal(resolveChromePath({}, { CHROME_PATH: custom }), custom);
});

test('CLI chrome preflight uses the CHROME_PATH environment override', () => {
  const run = spawnSync(process.execPath, [path.join(__dirname, 'granska-svg.js'), '--chrome-preflight'], { encoding: 'utf8', env: { ...process.env, CHROME_PATH: process.execPath } });
  assert.equal(run.status, 0, run.stderr);
  assert.equal(run.stdout.trim(), process.execPath);
});

test('preserves input identity across multiple Chrome analysis batches', async () => {
  const input = Array.from({ length: 5 }, (_, i) => ({ bank: 'test', taskId: `B${i}`, figureIndex: i, paths: [`p${i}`], hash: `h${i}`, svg: svg(`<text x="20" y="20">label-${i}</text>`) }));
  const output = await analyzeSvgFigures(input, { batchSize: 2, maxBatchCharacters: 100000 });
  assert.deepEqual(output.map((item) => item.taskId), input.map((item) => item.taskId));
  assert.deepEqual(output.map((item) => item.elements.find((element) => element.tag === 'text').text), input.map((_, i) => `label-${i}`));
});

test('fails closed when a finding is attached to another bank, task, figure, or SVG source', async () => {
  const dir = fixtureRepo([
    { id: 'DUP', t: svg('<line x1="10" y1="60" x2="190" y2="60"/><text x="100" y="64">source A</text>') },
    { id: 'DUP', t: svg('<circle cx="100" cy="60" r="20"/><text x="100" y="64">source B</text>') }
  ]);
  try {
    const extraction = extractAll(dir);
    assert.equal(extraction.figures.length, 2);
    assert.notEqual(extraction.figures[0].sourceKey, extraction.figures[1].sourceKey);
    assert.deepEqual(extraction.figures.map((item) => item.taskIndex), [0, 1]);
    const analyzed = await analyzeSvgFigures(extraction.figures, { batchSize: 1 });
    const verified = verifyFindingTraceability(extraction, analyzed);
    assert.equal(verified.figures, 2);

    for (const field of ['bank', 'taskId', 'taskIndex', 'figureIndex', 'hash', 'sourceKey']) {
      const tampered = structuredClone(analyzed);
      tampered[0][field] = field === 'taskIndex' || field === 'figureIndex' ? 999 : 'fel-källa';
      assert.throws(() => verifyFindingTraceability(extraction, tampered), /spårbar|källa|proveniens/i, field);
    }

    const badElement = structuredClone(analyzed);
    badElement[0].findings = [{ severity: 'WARNING', code: 'PROBE', reason: 'probe', elements: [999] }];
    assert.throws(() => verifyFindingTraceability(extraction, badElement), /element/i);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test('uses the project course names for all seven bank files', () => {
  const extraction = extractAll(path.resolve(__dirname, '..'));
  assert.deepEqual(Object.fromEntries(extraction.banks.map((item) => [item.bank, item.course])), {
    'uppgifter.js': 'Fysik - nivå 1',
    'uppgifter2.js': 'Fysik - nivå 2',
    'uppgifterma1.js': 'Matematik - nivå 1',
    'uppgifterma2.js': 'Matematik - nivå 2',
    'uppgiftermato1.js': 'Matematik fortsättning - nivå 1',
    'uppgiftermato2.js': 'Matematik fortsättning - nivå 2',
    'uppgiftermatf1.js': 'Matematik fördjupning - nivå 1'
  });
});

test('real-bank provenance keeps same numeric IDs in uppgifter.js and uppgifterma2.js separate', async () => {
  const repoRoot = path.resolve(__dirname, '..');
  const extraction = extractAll(repoRoot);
  const basic2120 = extraction.figures.filter((item) => item.bank === 'uppgifter.js' && item.taskId === '2.120');
  const ma22120 = extraction.figures.filter((item) => item.bank === 'uppgifterma2.js' && item.taskId === '2.120');
  const basic4133 = extraction.figures.filter((item) => item.bank === 'uppgifter.js' && item.taskId === '4.133');
  const ma24133 = extraction.figures.filter((item) => item.bank === 'uppgifterma2.js' && item.taskId === '4.133');

  assert.equal(basic2120.length, 1);
  assert.equal(basic2120[0].taskIndex, 191);
  assert.deepEqual(basic2120[0].paths, ['t[svg:0]']);
  assert.equal(ma22120.length, 0, 'Ma2 2.120 är fyrverkeriuppgiften och har ingen SVG');

  assert.equal(basic4133.length, 2);
  assert.equal(basic4133[1].taskIndex, 584);
  assert.deepEqual(basic4133[1].paths, ['s[svg:0]']);
  assert.match(basic4133[1].svg, /5,0 kg/);
  assert.match(basic4133[1].svg, />golv</);
  assert.equal(ma24133.length, 1);
  assert.notEqual(ma24133[0].hash, basic4133[1].hash, 'Ma2 4.133 är en annan figur');

  const selected = [basic2120[0], basic4133[1], ma24133[0]];
  const analyzed = await analyzeSvgFigures(selected, { batchSize: 1 });
  const verified = verifyFindingTraceability({ ...extraction, figures: selected }, analyzed);
  assert.equal(verified.figures, 3);
  assert.ok(analyzed[0].findings.some((item) => item.code === 'ANGLE_ARC_OFF_CENTER'));
  assert.ok(analyzed[1].findings.some((item) => item.code === 'TEXT_TEXT_COLLISION'));
  assert.equal(analyzed[2].findings.length, 0);
});

test('rejects browser batch results with missing or mismatched indexes', () => {
  assert.throws(() => validateBatchResults([{ i: 1 }], 1), /index/i);
  assert.throws(() => validateBatchResults([], 1), /antal|count/i);
});

test('skips geometry below opacity-zero ancestors', async () => {
  const result = await findings(svg('<g opacity="0"><line x1="20" y1="60" x2="180" y2="60" stroke="black"/><text x="100" y="65" text-anchor="middle" font-size="16">12 cm</text></g>'));
  assert.deepEqual(result, []);
});

test('labels deterministic findings separately from volatile report metadata', async () => {
  const source = sourceFigure({ taskId: 'D' });
  const [result] = await analyzeSvgFigures([source]);
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'svg-determinism-test-'));
  try {
    const report = buildReport(dir, { banks: [{ bank: 'test', course: 'Test', tasks: 1, tasksContainingSvg: 1, rawOccurrences: 1, figures: 1 }], figures: [source], references: [] }, [result], 17);
    assert.equal(report.json.findingsDeterministic, true);
    assert.deepEqual(report.json.volatileMetadata, ['generatedAt', 'summary.runtimeMs']);
    assert.equal('deterministic' in report.json, false);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test('generated HTML contains no trailing whitespace from sanitized SVG text nodes', async () => {
  const source = sourceFigure({ taskId: 'W', svg: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">\n  <text x="1" y="10">x</text>   \n</svg>' });
  const [result] = await analyzeSvgFigures([source]);
  result.findings.push({ severity: 'INFO', code: 'PROBE', reason: 'probe', elements: [] });
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'svg-whitespace-test-'));
  try {
    buildReport(dir, { banks: [{ bank: 'test', course: 'Test', tasks: 1, tasksContainingSvg: 1, rawOccurrences: 1, figures: 1 }], figures: [source], references: [] }, [result], 1);
    const html = fs.readFileSync(path.join(dir, 'SVG_GRANSKNING.html'), 'utf8');
    assert.doesNotMatch(html, /[ \t]+$/m);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});

test('extracts namespace-prefixed inline SVG roots and inserts overlays before their closing root', async () => {
  const markup = '<s:svg xmlns:s="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><s:text x="1" y="10">x</s:text></s:svg>';
  const occurrences = collectSvgStrings({ nested: { html: `before ${markup} after` } });
  assert.equal(occurrences.length, 1);
  assert.equal(occurrences[0].svg, markup);
  const [result] = await analyzeSvgFigures([{ bank: 'test', course: 'Test', taskId: 'P', figureIndex: 0, svg: markup, paths: [occurrences[0].path], hash: 'p' }]);
  result.findings.push({ severity: 'INFO', code: 'PROBE', reason: 'probe', elements: [] });
  assert.match(overlaySvg(result), /svg-review-overlay[\s\S]*<\/s:svg>$/i);
});

test('analyzes safe local SVG file references and maps remote or unresolved references without fetching', async () => {
  const dir = fixtureRepo([{ id: 'REF', nested: { html: '<img src="assets/local.svg?cache=1#shape"><a href="https://example.invalid/remote.svg?v=2">x</a>', css: 'background:url(assets/local.svg#again);mask:url("assets/missing.svg?x=1")' } }]);
  try {
    fs.mkdirSync(path.join(dir, 'assets'));
    fs.writeFileSync(path.join(dir, 'assets', 'local.svg'), svg('<line x1="20" y1="60" x2="180" y2="60" stroke="black"/><text x="100" y="65" text-anchor="middle" font-size="16">12 cm</text>'));
    const extraction = extractAll(dir);
    assert.equal(extraction.figures.length, 1);
    assert.equal(extraction.figures[0].paths.length, 2);
    assert.equal(extraction.figures[0].sourceKind, 'local-file');
    assert.deepEqual([...new Set(extraction.references.map((item) => item.status))].sort(), ['external', 'local', 'unresolved']);
    const analyzed = await analyzeSvgFigures(extraction.figures, { batchSize: 1 });
    assert.ok(has(analyzed[0].findings, 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'WARNING'));
    const report = buildReport(dir, extraction, analyzed, 1);
    assert.equal(report.json.externalInventory.length, 4);
    assert.ok(report.json.externalInventory.some((item) => item.status === 'external' && item.ref.includes('remote.svg')));
    assert.ok(report.json.externalInventory.some((item) => item.status === 'unresolved' && item.ref.includes('missing.svg')));
    assert.ok(report.json.externalInventory.every((item) => item.taskId === 'REF' && item.path.startsWith('nested.')));
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});
