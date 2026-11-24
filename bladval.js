// Urval för lärarens övningsblad. Uppgifterna kommer från bankvyns aktiva filter.
const Bladval = (() => {
  const nivåer = ['E', 'C', 'A'];
  const område = x => x.kap + ':' + x.omr;
  const familj = x => område(x) + '/' + (x.familj || '');
  const info = new WeakMap();

  function egenskaper(x) {
    if (info.has(x)) return info.get(x);
    const delar = Math.max(1, x.spelDelar?.length || 0, x.delpoang?.length || 0,
      x.svarstyp === 'flera_delar' && Array.isArray(x.rättSvar) ? x.rättSvar.length : 0);
    const tal = v => (Array.isArray(v) ? v : [v]).map(Number).filter(n => n > 0 && Number.isFinite(n));
    const insats = tal(x.arbetsinsats);
    const träning = tal(x.traningsniva);
    const förmågor = [].concat(x.formaga || []);
    const eg = {
      metod: x.typ || x.familj || x.omr, förmåga: förmågor.slice().sort().join("/"),
      rutin: förmågor.includes('procedur') && !förmågor.some(f => ['resonemang','modellering','problemlösning'].includes(f)),
      lång: delar > 1 || insats.some(n => n >= 3),
      svårighet: träning.length ? Math.max(...träning) : 1 + 2 * nivåer.indexOf(x.niva)
    };
    info.set(x, eg);
    return eg;
  }

  // Fördela exakta delmoments- och nivåantal samtidigt. Vid en krock kan en
  // tidigare plats byta nivå så att även ett tunt delmoment får plats.
  function fördelaNivåer(platser, grupper, kvot, slump) {
    const bruk = new Map();
    const fördelat = nivåer.map(() => []);
    const kapacitet = new Map([...grupper].map(([k, xs]) =>
      [k, nivåer.map(n => xs.filter(x => x.niva === n).length)]));
    function placera(k, besökta) {
      if (besökta.has(k)) return false;
      besökta.add(k);
      const antal = bruk.get(k) || [0, 0, 0];
      bruk.set(k, antal);
      const val = nivåer.map((_, i) => i).filter(i => antal[i] < (kapacitet.get(k)?.[i] || 0));
      for (let i = val.length-1; i > 0; i--) {
        const j = Math.floor(slump() * (i+1)); [val[i],val[j]] = [val[j],val[i]];
      }
      for (const i of val) {
        if (fördelat[i].length < kvot[i]) {
          antal[i]++; fördelat[i].push(k); return true;
        }
      }
      for (const i of val) {
        for (let j = 0; j < fördelat[i].length; j++) {
          const annan = fördelat[i][j];
          if (besökta.has(annan)) continue;
          bruk.get(annan)[i]--;
          if (placera(annan, besökta)) {
            antal[i]++; fördelat[i][j] = k; return true;
          }
          bruk.get(annan)[i]++;
        }
      }
      return false;
    }
    for (const k of platser) {
      if (!placera(k, new Set())) throw Error('Delmomenten och nivåantalen går inte att kombinera. Ändra ett antal eller välj fler delmoment.');
    }
    return fördelat.flatMap((lista, i) => lista.map(k => ({k, nivå: nivåer[i]})));
  }

  function dra(pool, val, tidigare = [], historik = new Map(), slump = Math.random) {
    const {antal, profil, längd, familjer, nivåantal} = val;
    if (!Number.isInteger(antal) || antal < 1 || antal > 40) throw Error('Välj mellan 1 och 40 uppgifter.');
    const låsta = tidigare.map((x, i) => ({x, i})).filter(p => p.x._bladLåst);
    if (låsta.some(p => p.i >= antal)) throw Error('En låst uppgift ligger efter bladets sista plats. Höj antalet eller lås upp den.');
    const valda = new Set(låsta.map(p => p.x.id));
    const antalPerFamilj = new Map(), antalPerOmråde = new Map(), antalPerMetod = new Map(), antalPerFörmåga = new Map();
    const räkna = (m, k) => m.set(k, (m.get(k) || 0) + 1);
    function registrera(x) {
      räkna(antalPerFamilj, familj(x)); räkna(antalPerOmråde, område(x));
      räkna(antalPerMetod, egenskaper(x).metod); räkna(antalPerFörmåga, egenskaper(x).förmåga);
    }
    låsta.forEach(({x}) => registrera(x));
    if (familjer && låsta.some(({x}) => !familjer.has(familj(x)))) throw Error('Ett låst delmoment är bortvalt. Välj det eller lås upp uppgiften.');
    const fasta = new Map([...(familjer || [])].filter(([, n]) => n !== null));
    const grupper = new Map();
    for (const x of pool) {
      if (valda.has(x.id) || (familjer && !familjer.has(familj(x)))) continue;
      const k = fasta.has(familj(x)) ? familj(x) : '*';
      if (!grupper.has(k)) grupper.set(k, []);
      grupper.get(k).push(x);
    }
    const platser = [];
    for (const [k, n] of fasta) {
      const kvar = n - (antalPerFamilj.get(k) || 0);
      if (!Number.isInteger(n) || n < 0 || n > antal || kvar < 0) throw Error('Kontrollera antalet per delmoment och de låsta uppgifterna.');
      if (kvar > (grupper.get(k)?.length || 0)) throw Error('Det finns för få uppgifter i ett valt delmoment. Sänk antalet eller bredda urvalet.');
      for (let i = 0; i < kvar; i++) platser.push(k);
    }
    const fria = antal - låsta.length - platser.length;
    if (fria < 0) throw Error('Antalen per delmoment överstiger bladets längd.');
    if (familjer && !familjer.size) throw Error('Markera minst ett delmoment eller låt bladet använda alla.');
    if (grupper.size === 0 && !pool.length && fria) throw Error('Inga uppgifter matchar bankens filter.');
    if (fria && familjer?.size && fasta.size === familjer.size) throw Error('Delmomentens antal måste tillsammans bli ' + antal + '. Du kan också lämna ett antal tomt.');
    if (fria > (grupper.get('*')?.length || 0)) throw Error('Det finns för få valbara uppgifter. Sänk antalet eller lämna minst ett delmoment med fritt antal.');
    for (let i = 0; i < fria; i++) platser.push('*');

    let plan;
    if (nivåantal) {
      if (nivåantal.some(n => !Number.isInteger(n) || n < 0) || nivåantal.reduce((a,b) => a+b, 0) !== antal)
        throw Error('Antalen för E, C och A måste tillsammans bli ' + antal + '.');
      const kvot = nivåantal.map((n,i) => n - låsta.filter(p => p.x.niva === nivåer[i]).length);
      if (kvot.some(n => n < 0)) throw Error('De låsta uppgifterna överskrider en nivåkvot.');
      plan = fördelaNivåer(platser, grupper, kvot, slump);
    } else {
      plan = platser.map(k => ({k}));
    }

    const nya = [];
    for (const [index, plats] of plan.entries()) {
      const möjliga = grupper.get(plats.k).filter(x => !valda.has(x.id) && (!plats.nivå || plats.nivå === x.niva));
      const steg = profil === 'stegring' ? nivåer.filter(n => möjliga.some(x => x.niva === n)) : [];
      const mål = steg[Math.floor(index * steg.length / plan.length)];
      // Dra likvärdiga kandidater likformigt. Senast använda ID:n får vila.
      let bäst, vald, lika = 0;
      for (const x of möjliga) {
        const eg = egenskaper(x), nf = antalPerFamilj.get(familj(x)) || 0;
        const rang = [
          längd === 'alla' || (längd === 'lång') === eg.lång ? 0 : 1,
          mål && x.niva !== mål ? 1 : 0,
          profil === 'rutin' && !eg.rutin ? 1 : 0,
          profil !== 'rutin' || val.täckOmråden ? (antalPerOmråde.get(område(x)) || 0) : 0,
          profil === 'rutin' && !familjer ? -nf : nf,
          historik.get(x.id) || 0,
          (profil === 'rutin' ? -1 : 1) * (antalPerMetod.get(eg.metod) || 0),
          profil === 'rutin' ? 0 : (antalPerFörmåga.get(eg.förmåga) || 0)
        ];
        const skillnad = bäst ? rang.findIndex((v,i) => v !== bäst[i]) : -1;
        if (!bäst || (skillnad >= 0 && rang[skillnad] < bäst[skillnad])) {
          bäst = rang; vald = x; lika = 1;
        } else if (skillnad < 0 && slump() < 1 / ++lika) vald = x;
      }
      valda.add(vald.id); registrera(vald); nya.push(vald);
    }
    if (profil === 'stegring') nya.sort((a,b) => nivåer.indexOf(a.niva)-nivåer.indexOf(b.niva)
      || egenskaper(a).svårighet-egenskaper(b).svårighet || Number(egenskaper(a).lång)-Number(egenskaper(b).lång));
    else if (profil === 'rutin') {
      const ordning = new Map([...new Set(nya.map(familj))].map((k,i) => [k,i]));
      nya.sort((a,b) => ordning.get(familj(a))-ordning.get(familj(b)));
    } else {
      for (let i = nya.length-1; i > 0; i--) {
        const j = Math.floor(slump() * (i+1)); [nya[i],nya[j]] = [nya[j],nya[i]];
      }
    }
    return Array.from({length:antal}, (_,i) => tidigare[i]?._bladLåst ? tidigare[i] : nya.shift());
  }

  function ersätt(pool, lista, index, historik, längd, slump = Math.random) {
    const x = lista[index], upptagna = new Set(lista.map(t => t.id));
    const kandidater = pool.filter(t => !upptagna.has(t.id) && t.niva === x.niva && familj(t) === familj(x));
    if (!kandidater.length) throw Error('Det finns ingen ytterligare uppgift på samma nivå i detta delmoment med dina filter.');
    const likaMetod = kandidater.filter(t => x.typ && t.typ === x.typ);
    const val = {antal:1, profil:'varierad', längd: längd === 'alla' ? (egenskaper(x).lång ? 'lång' : 'kort') : längd};
    return dra(likaMetod.length ? likaMetod : kandidater, val, [], historik, slump)[0];
  }
  return {dra, ersätt, familj, område};
})();
if (typeof module !== 'undefined' && module.exports) module.exports = Bladval;
