(() => {
  'use strict';
  const C = window.NVOA_CONTENT || { site: {}, themes: [], items: [] };
  const $ = (s, r = document) => r.querySelector(s);
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isTodo = t => !t || /^\s*TODO/i.test(t);
  const capText = i => (isTodo(i.caption) ? '' : i.caption);
  const altText = i => capText(i) || (i.type === 'video' ? 'Video från NVOA' : 'Bild från NVOA');

  function h(tag, attrs, ...kids) {
    const e = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs || {})) {
      if (v === false || v == null) continue;
      if (k === 'class') e.className = v; else if (k === 'text') e.textContent = v; else e.setAttribute(k, v === true ? '' : v);
    }
    kids.flat().forEach(c => c != null && e.append(c));
    return e;
  }

  const items = (C.items || []).filter(i => !i.hidden)
    .map((it, n) => [it, n]).sort((a, b) => (a[0].order ?? 1e9) - (b[0].order ?? 1e9) || a[1] - b[1]).map(x => x[0]);
  const themes = (C.themes || []).filter(t => items.some(i => i.theme === t.id));
  const site = C.site || {};

  /* ---- Medianoder ---- */
  function picture(i, big) {
    const img = h('img', { src: big && i.fallback ? i.fallback : i.thumb, alt: altText(i), loading: 'lazy', decoding: 'async', width: i.w || null, height: i.h || null });
    if (big && i.src) return h('picture', {}, h('source', { type: 'image/webp', srcset: i.src }), img);
    return i.type === 'image' && i.thumb ? h('picture', {}, h('source', { type: 'image/webp', srcset: i.thumb }), img) : img;
  }
  function tile(i, list, feature) {
    const b = h('button', { type: 'button', class: 'tile' + (feature ? ' feature' : ''), 'data-id': i.id,
      'aria-label': (i.type === 'video' ? 'Spela video: ' : 'Förstora bild: ') + altText(i) },
      i.type === 'video' ? h('img', { src: i.thumb, alt: '', loading: 'lazy', decoding: 'async', width: i.w || null, height: i.h || null })
        : (feature ? picture(i, true) : picture(i, false)));
    if (i.type === 'video') b.append(h('span', { class: 'play', 'aria-hidden': 'true', text: '▶ Video' }));
    if (capText(i)) b.append(h('span', { class: 'cap', text: capText(i) }));
    b.addEventListener('click', () => openLightbox(typeof list === 'function' ? list() : list, i));
    return b;
  }

  /* ---- Sida ---- */
  document.title = (site.title || 'NVOA') + ' – bildvisning';
  $('#brand').textContent = site.title || 'Nacka Vatten och Avfall';
  $('#hero-title').textContent = site.title || '';
  const txt = (id, v) => { const e = $(id); if (isTodo(v)) e.hidden = true; else e.textContent = v; };
  txt('#hero-sub', site.subtitle); txt('#hero-intro', site.intro); txt('#footer-text', site.footer);

  if (!items.length) {
    $('#themes').append(h('p', { class: 'empty', text: 'Inget material ännu. Kör tools/prepare_media.py och ladda om sidan.' }));
    $('#galleri').hidden = true; $('#btn-present').hidden = true; $('#btn-present2').hidden = true;
    return;
  }

  // Hero
  const heroItem = items.find(i => i.hero) || items.find(i => i.type === 'video') || items[0];
  const hm = $('#hero-media');
  if (heroItem.type === 'video') {
    const v = h('video', { muted: true, loop: true, playsinline: true, preload: 'auto', poster: heroItem.poster, 'aria-hidden': 'true', tabindex: '-1' });
    v.muted = true; v.append(h('source', { src: heroItem.video, type: 'video/mp4' }));
    hm.append(v);
    const tg = $('#hero-toggle'); tg.hidden = false;
    const sync = () => { const p = !v.paused; tg.textContent = p ? 'Pausa bakgrundsvideo' : 'Spela bakgrundsvideo'; tg.setAttribute('aria-pressed', String(!p)); };
    tg.addEventListener('click', () => { v.paused ? v.play().catch(() => {}) : v.pause(); sync(); });
    if (!reduceMotion) v.play().then(sync).catch(sync); else sync();
  } else {
    const p = picture(heroItem, true); p.querySelector('img').loading = 'eager'; p.querySelector('img').alt = ''; hm.append(p);
  }

  // Teman
  const nav = $('#nav'), tw = $('#themes');
  themes.forEach(t => {
    const list = items.filter(i => i.theme === t.id);
    nav.append(h('a', { href: '#t-' + t.id, text: isTodo(t.title) ? t.id : t.title }));
    const sec = h('section', { class: 'theme', id: 't-' + t.id, 'aria-labelledby': 'h-' + t.id },
      h('h2', { id: 'h-' + t.id, text: isTodo(t.title) ? t.id : t.title }),
      isTodo(t.text) ? null : h('p', { text: t.text }),
      h('div', { class: 'theme-grid' }, list.map((i, n) => tile(i, list, n === 0 && list.length > 2))));
    tw.append(sec);
  });
  nav.append(h('a', { href: '#galleri', text: 'Galleri' }));

  // Galleri med filter
  const state = { theme: 'alla', type: 'alla' };
  const grid = $('#grid'), filters = $('#filters');
  const visible = () => items.filter(i => (state.theme === 'alla' || i.theme === state.theme) && (state.type === 'alla' || i.type === state.type));
  items.forEach(i => grid.append(tile(i, visible)));
  const fbtns = [];
  const fbtn = (group, val, label) => {
    const b = h('button', { type: 'button', class: 'btn', 'aria-pressed': String(state[group] === val), text: label });
    b.addEventListener('click', () => { state[group] = val; apply(); });
    b.dataset.g = group; b.dataset.v = val; fbtns.push(b); return b;
  };
  [['alla', 'Alla teman'], ...themes.map(t => [t.id, isTodo(t.title) ? t.id : t.title])].forEach(([v, l]) => filters.append(fbtn('theme', v, l)));
  filters.append(h('span', { class: 'sep', 'aria-hidden': 'true' }));
  [['alla', 'Bild och video'], ['image', 'Endast bilder'], ['video', 'Endast video']].forEach(([v, l]) => filters.append(fbtn('type', v, l)));
  function apply() {
    const vis = new Set(visible().map(i => i.id));
    grid.querySelectorAll('.tile').forEach(t => { t.hidden = !vis.has(t.dataset.id); });
    fbtns.forEach(b => b.setAttribute('aria-pressed', String(state[b.dataset.g] === b.dataset.v)));
    $('#count').textContent = vis.size + ' av ' + items.length + ' objekt visas';
  }
  apply();

  /* ---- Lightbox ---- */
  const lb = $('#lightbox'), stage = $('#lb-stage');
  let list = [], idx = 0, opener = null;
  function lbRender() {
    const i = list[idx];
    stage.querySelectorAll('video').forEach(v => v.pause());
    stage.replaceChildren();
    if (i.type === 'video') {
      const v = h('video', { controls: true, playsinline: true, preload: 'metadata', poster: i.poster, 'aria-label': altText(i) }, h('source', { src: i.video, type: 'video/mp4' }));
      stage.append(v); if (!reduceMotion) v.play().catch(() => {});
    } else stage.append(picture(i, true)), stage.querySelector('img').loading = 'eager';
    $('#lb-caption').textContent = capText(i);
    $('#lb-count').textContent = (idx + 1) + ' / ' + list.length;
    $('#lb-prev').disabled = $('#lb-next').disabled = list.length < 2;
  }
  const lbMove = d => { idx = (idx + d + list.length) % list.length; lbRender(); };
  function openLightbox(l, item) {
    list = l; idx = Math.max(0, l.indexOf(item)); opener = document.activeElement;
    lbRender(); lb.showModal(); $('#lb-close').focus();
  }
  $('#lb-prev').addEventListener('click', () => lbMove(-1));
  $('#lb-next').addEventListener('click', () => lbMove(1));
  $('#lb-close').addEventListener('click', () => lb.close());
  lb.addEventListener('close', () => { stage.querySelectorAll('video').forEach(v => v.pause()); stage.replaceChildren(); opener && opener.focus && opener.focus(); });
  lb.addEventListener('keydown', e => {
    if (e.target.tagName === 'VIDEO' && (e.key === ' ' || e.key === 'k')) return;
    if (e.key === 'ArrowRight') { lbMove(1); e.preventDefault(); } else if (e.key === 'ArrowLeft') { lbMove(-1); e.preventDefault(); }
  });
  let sx = null, sy = null;
  stage.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') { sx = e.clientX; sy = e.clientY; } });
  stage.addEventListener('pointerup', e => {
    if (sx == null) return;
    const dx = e.clientX - sx, dy = e.clientY - sy; sx = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) lbMove(dx < 0 ? 1 : -1);
  });
  lb.addEventListener('click', e => { if (e.target === lb) lb.close(); });

  /* ---- Presentationsläge ---- */
  const show = $('#show'), sstage = $('#show-stage'), SLIDE_MS = 7000;
  let si = 0, paused = false, timer = null, t0 = 0, elapsed = 0, idleT = null;
  const state$ = $('#show-state');
  function sRender() {
    clearTimeout(timer); elapsed = 0;
    const i = items[si];
    sstage.replaceChildren();
    if (i.type === 'video') {
      const v = h('video', { muted: true, playsinline: true, preload: 'auto', poster: i.poster }, h('source', { src: i.video, type: 'video/mp4' }));
      v.muted = true; v.addEventListener('ended', () => { if (!paused) sNext(1); });
      sstage.append(v); if (!paused) v.play().catch(() => {});
    } else { const p = picture(i, true); sstage.append(p); p.querySelector('img').loading = 'eager'; }
    if (capText(i)) sstage.append(h('div', { class: 'show-caption', text: capText(i) }));
    $('#show-count').textContent = (si + 1) + ' / ' + items.length;
    sTick(true);
  }
  function sTick(reset) {
    cancelAnimationFrame(sTick.raf);
    const i = items[si], bar = $('#show-progress');
    state$.textContent = paused ? 'Pausad – mellanslag återupptar' : 'Spelar – valfri tangent pausar';
    if (i.type === 'video') { bar.style.width = '0'; return; }
    if (reset) t0 = performance.now() - elapsed;
    const step = () => {
      if (paused) return;
      elapsed = performance.now() - t0;
      bar.style.width = Math.min(100, elapsed / SLIDE_MS * 100) + '%';
      if (elapsed >= SLIDE_MS) sNext(1); else sTick.raf = requestAnimationFrame(step);
    };
    if (!paused) sTick.raf = requestAnimationFrame(step);
  }
  function sNext(d) { si = (si + d + items.length) % items.length; sRender(); }
  function sPause(p) {
    paused = p; const v = sstage.querySelector('video');
    if (v) p ? v.pause() : v.play().catch(() => {});
    sTick(true);
  }
  function sIdle() { show.classList.remove('idle'); clearTimeout(idleT); idleT = setTimeout(() => show.classList.add('idle'), 3000); }
  function startShow() {
    si = 0; paused = reduceMotion; show.showModal(); show.focus(); sRender(); sIdle();
    if (show.requestFullscreen) show.requestFullscreen().catch(() => {});
  }
  show.addEventListener('keydown', e => {
    sIdle();
    if (e.key === 'Escape') return;
    if (e.target.closest('button') && (e.key === 'Enter' || e.key === ' ')) return;
    e.preventDefault();
    if (e.key === ' ') sPause(!paused);
    else if (e.key === 'ArrowRight') { sPause(true); sNext(1); }
    else if (e.key === 'ArrowLeft') { sPause(true); sNext(-1); }
    else if (!paused) sPause(true);
  });
  show.addEventListener('mousemove', sIdle);
  show.addEventListener('click', e => { if (!e.target.closest('button')) sPause(!paused); });
  $('#show-close').addEventListener('click', () => show.close());
  show.addEventListener('close', () => {
    clearTimeout(timer); clearTimeout(idleT); cancelAnimationFrame(sTick.raf); sstage.replaceChildren();
    if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
  });
  document.addEventListener('fullscreenchange', () => { if (!document.fullscreenElement && show.open) show.close(); });
  ['#btn-present', '#btn-present2'].forEach(s => $(s).addEventListener('click', startShow));
})();
