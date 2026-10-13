/* Driftinformation: tre påhittade exempel och en förenklad karta. Markeringarna och listan hör ihop. */
(function () {
  'use strict';
  var N = window.NVOA, C = window.NVOA_CONTENT || {}, h = N.h;
  var list = document.getElementById('drift-list'), map = document.getElementById('map');
  var data = C.disruptions || []; if (!list || !map) return;
  var cls = { 'Planerad': 'st-p', 'Pågående': 'st-n', 'Information': 'st-i' };

  var fig = h('figure', { style: 'margin:0' });
  fig.appendChild(N.render('karta-drift'));
  fig.appendChild(h('figcaption', { text: 'Förenklad karta – exempel' }));
  map.appendChild(fig);

  var cards = [], pins = [];
  function select(i, focusCard) {
    cards.forEach(function (c, k) { c.classList.toggle('is-on', k === i); });
    pins.forEach(function (p, k) { p.classList.toggle('is-on', k === i); p.setAttribute('aria-pressed', String(k === i)); });
    if (focusCard) cards[i].scrollIntoView({ block: 'nearest', behavior: N.reduceMotion ? 'auto' : 'smooth' });
  }

  data.forEach(function (d, i) {
    var li = h('li'), a = h('article', { class: 'dcard', 'aria-labelledby': 'dh-' + d.n });
    var tags = h('div', { class: 'dtags' });
    tags.appendChild(h('span', { class: 'badge ' + (cls[d.status] || ''), text: d.status }));
    tags.appendChild(h('span', { class: 'badge ex', text: 'Exempeldata' }));
    a.appendChild(tags);
    a.appendChild(h('h3', { id: 'dh-' + d.n, text: d.n + '. ' + d.title }));
    a.appendChild(h('p', { class: 'dmeta', text: d.area + ' · ' + d.when }));
    a.appendChild(h('p', { text: d.text }));
    var b = h('button', { type: 'button', class: 'btn btn-small', text: 'Visa på kartan' });
    b.addEventListener('click', function () { select(i); map.scrollIntoView({ block: 'nearest', behavior: N.reduceMotion ? 'auto' : 'smooth' }); });
    a.appendChild(b); li.appendChild(a); list.appendChild(li); cards.push(a);

    var p = h('button', { type: 'button', class: 'pin ' + (cls[d.status] || ''), text: String(d.n), 'aria-label': 'Visa störning ' + d.n + ' i listan: ' + d.title, 'aria-pressed': 'false',
      style: 'left:' + d.x + '%;top:' + d.y + '%' });
    p.addEventListener('click', function () { select(i, true); });
    map.appendChild(p); pins.push(p);
  });
})();
