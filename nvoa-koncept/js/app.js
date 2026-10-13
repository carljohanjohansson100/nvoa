/* Start: meny, sticky-mått, hjälte, galleri, filmer, kontakt. */
(function () {
  'use strict';
  var N = window.NVOA, C = window.NVOA_CONTENT || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var h = N.h;

  /* Mått för fast banderoll och sidhuvud (används av scroll-padding) */
  var root = document.documentElement;
  function measure() {
    var b = $('.banner'), hd = $('.site-header');
    var bh = b.offsetHeight;
    var sticky = getComputedStyle(hd).position === 'sticky';
    root.style.setProperty('--banner-h', bh + 'px');
    root.style.setProperty('--sticky-h', (bh + (sticky ? hd.offsetHeight : 0)) + 'px');
  }
  measure();
  window.addEventListener('resize', measure);
  if (window.ResizeObserver) { var ro = new ResizeObserver(measure); ro.observe($('.banner')); ro.observe($('.site-header')); }

  /* Meny på små skärmar */
  var btn = $('#menu-btn'), nav = $('#nav');
  function setMenu(open) {
    nav.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? 'Stäng meny' : 'Meny';
    measure();
  }
  btn.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav.classList.contains('open')) { setMenu(false); btn.focus(); }
  });

  /* Alla element med data-media fylls från manifestet */
  document.querySelectorAll('[data-media]').forEach(function (host) {
    host.appendChild(N.render(host.getAttribute('data-media'), { bare: host.hasAttribute('data-bare'), eager: host.hasAttribute('data-hero') }));
  });

  /* Hjälten: paus för rörelse (WCAG 2.2.2) */
  (function () {
    var host = $('.hero-media'), tg = $('#hero-toggle'), el = host.firstElementChild;
    if (!el) return;
    function label(playing) { tg.textContent = playing ? 'Pausa rörelsen' : 'Spela rörelsen'; tg.hidden = false; }
    if (el.tagName === 'IFRAME') {
      window.addEventListener('message', function (e) {
        if (e.source !== el.contentWindow || !e.data || e.data.type !== 'nvoa-scene') return;
        label(e.data.playing);
      });
      el.addEventListener('load', function () { try { el.contentWindow.postMessage({ cmd: 'query' }, '*'); } catch (x) {} });
      tg.addEventListener('click', function () { el.contentWindow.postMessage({ cmd: 'toggle' }, '*'); });
    } else if (el.tagName === 'VIDEO') {
      var sync = function () { label(!el.paused); };
      el.addEventListener('play', sync); el.addEventListener('pause', sync);
      tg.addEventListener('click', function () { el.paused ? el.play() : el.pause(); });
      sync();
    }
  })();

  /* Galleri (nio bilder med kategori) */
  var gal = N.media.items.filter(function (i) { return i.category && N.media.kind(i) === 'image'; });
  var ul = $('#gallery');
  gal.forEach(function (it, idx) {
    var b = h('button', { type: 'button', class: 'tile', 'aria-label': it.category + ' ' + it.title + '. Förstora bild.', 'aria-haspopup': 'dialog' });
    b.appendChild(N.render(it.id));
    var meta = h('span', { class: 'tile-meta' });
    meta.appendChild(h('span', { class: 'tile-cat', text: it.category }));
    meta.appendChild(document.createTextNode(' '));
    meta.appendChild(h('span', { class: 'tile-title', text: it.title }));
    b.appendChild(meta);
    b.addEventListener('click', function () { N.openLightbox(gal, idx, b); });
    var li = h('li'); li.appendChild(b); ul.appendChild(li);
  });

  /* Filmer */
  var films = N.media.items.filter(function (i) { return /^film-/.test(i.id); });
  var fr = $('#films'), frames = [];
  films.forEach(function (it, n) {
    var card = h('article', { class: 'film-card', 'aria-labelledby': 'fh-' + n });
    var frame = h('div', { class: 'film-frame' });
    var media = N.render(it.id);
    frame.appendChild(media); frames.push(media);
    var body = h('div', { class: 'film-body' });
    body.appendChild(h('span', { class: 'tag', text: N.sourceLabel(it) }));
    body.appendChild(h('h3', { id: 'fh-' + n, text: it.title }));
    body.appendChild(h('p', { text: it.caption || '' }));
    if (it.transcript) {
      var d = h('details'); d.appendChild(h('summary', { text: 'Visa hela texten till filmen' }));
      d.appendChild(h('p', { text: it.transcript })); body.appendChild(d);
    }
    card.appendChild(frame); card.appendChild(body); fr.appendChild(card);
  });
  window.addEventListener('message', function (e) {   // endast en film spelas åt gången
    if (!e.data || e.data.type !== 'nvoa-scene' || !e.data.playing) return;
    frames.forEach(function (f) { if (f.contentWindow && f.contentWindow !== e.source) f.contentWindow.postMessage({ cmd: 'pause' }, '*'); });
  });

  /* Kontakt: bara platshållare */
  var dl = $('#contact');
  (C.contact || []).forEach(function (c) {
    var d = h('div'); d.appendChild(h('dt', { text: c.label })); d.appendChild(h('dd', { text: c.value })); dl.appendChild(d);
  });
})();
