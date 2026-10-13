/* Renderar media från manifestet (media/manifest.js). Ändra bara manifestet för att byta ut en bild eller film.
   Filändelsen i "path" styr hur objektet visas:
     .svg .jpg .jpeg .png .webp  -> <img>
     .mp4 .webm                  -> <video>
     .html                       -> animerad scen i <iframe> (de genererade filmerna) */
(function () {
  'use strict';
  var N = window.NVOA = window.NVOA || {};
  var items = (window.NVOA_MEDIA && window.NVOA_MEDIA.items) || [];
  var byId = {};
  items.forEach(function (i) { byId[i.id] = i; });
  var reduceMotion = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function get(id) { return byId[id] || null; }

  function kind(it) {
    var p = String(it.path || '').split('?')[0].toLowerCase();
    if (/\.html?$/.test(p)) return 'scene';
    if (/\.(mp4|webm|ogv|mov)$/.test(p)) return 'video';
    if (/\.(svg|jpe?g|png|webp|gif|avif)$/.test(p)) return 'image';
    return it.type === 'video' ? 'video' : 'image';
  }

  function h(tag, attrs) {
    var e = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      var v = attrs[k];
      if (v === false || v == null) return;
      if (k === 'text') e.textContent = v; else e.setAttribute(k, v === true ? '' : v);
    });
    return e;
  }

  function mime(path) {
    var p = path.toLowerCase();
    return /\.webm/.test(p) ? 'video/webm' : /\.ogv/.test(p) ? 'video/ogg' : 'video/mp4';
  }

  /* opts: eager (ladda direkt), bare (bakgrundsfilm utan reglage), decorative (tom alt-text) */
  function render(id, opts) {
    opts = opts || {};
    var it = get(id);
    if (!it) {
      console.warn('Media saknas i manifestet: ' + id);
      return h('span', { class: 'missing', text: '[Media saknas: ' + id + ']' });
    }
    var k = kind(it);
    if (k === 'image') {
      var decorative = opts.decorative != null ? opts.decorative : (opts.bare || it.decorative);
      return h('img', { src: it.path, alt: decorative ? '' : (it.alt || it.title || ''), loading: opts.eager ? 'eager' : 'lazy', decoding: 'async', 'data-media-id': id });
    }
    if (k === 'video') {
      var v = h('video', { poster: it.poster, preload: 'metadata', playsinline: true, 'data-media-id': id,
        controls: !opts.bare, muted: opts.bare, loop: opts.bare, 'aria-hidden': opts.bare ? 'true' : false, tabindex: opts.bare ? '-1' : false,
        'aria-label': opts.bare ? false : (it.title || '') });
      if (opts.bare) { v.muted = true; if (!reduceMotion) v.autoplay = true; }
      v.appendChild(h('source', { src: it.path, type: mime(it.path) }));
      if (it.captions) v.appendChild(h('track', { kind: 'captions', src: it.captions, srclang: 'sv', label: 'Svenska', default: true }));
      v.appendChild(document.createTextNode('Din webbläsare kan inte spela upp filmen.'));
      return v;
    }
    var f = h('iframe', { src: it.path + (opts.bare ? '?bare=1' : ''), title: opts.bare ? false : 'Film: ' + (it.title || ''),
      loading: opts.eager ? 'eager' : 'lazy', sandbox: 'allow-scripts', 'data-media-id': id, 'data-scene': '1',
      'aria-hidden': opts.bare ? 'true' : false, tabindex: opts.bare ? '-1' : false });
    return f;
  }

  function sourceLabel(it) {
    var video = kind(it) !== 'image';
    if (it.source === 'nvoa') return (video ? 'Film' : 'Foto') + ': NVOA';
    return (video ? 'Illustrerad film' : 'Illustration') + ' skapad för konceptdemon';
  }

  N.media = { get: get, kind: kind, items: items };
  N.render = render;
  N.sourceLabel = sourceLabel;
  N.h = h;
  N.reduceMotion = reduceMotion;
})();
