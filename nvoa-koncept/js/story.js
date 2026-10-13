/* Vattnets väg: fem steg. På bred skärm byter en fast bild plats medan man scrollar, på smal skärm visas en bild per steg. */
(function () {
  'use strict';
  var N = window.NVOA, C = window.NVOA_CONTENT || {}, h = N.h;
  var stages = C.stages || [];
  var steps = document.getElementById('story-steps'), sticky = document.getElementById('story-sticky');
  if (!steps || !stages.length) return;

  var stack = h('div', { class: 'fig-stack' });
  var prog = h('ol', { class: 'progress', 'aria-hidden': 'true' });
  var label = h('p', { class: 'progress-label', 'aria-hidden': 'true' });
  var imgs = [], dots = [], els = [];

  stages.forEach(function (s, i) {
    var img = N.render(s.media);
    img.classList.toggle('is-active', i === 0);
    img.setAttribute('data-i', i);
    stack.appendChild(img); imgs.push(img);
    var dot = h('li'); prog.appendChild(dot); dots.push(dot);

    var li = h('li', { class: 'step', id: 'steg-' + (i + 1), 'aria-labelledby': 'steg-h-' + (i + 1) });
    var fig = h('div', { class: 'step-fig' }); fig.appendChild(N.render(s.media));
    var body = h('div');
    body.appendChild(h('span', { class: 'step-no', text: 'Steg ' + (i + 1) + ' av ' + stages.length }));
    body.appendChild(h('h3', { id: 'steg-h-' + (i + 1), text: s.title }));
    body.appendChild(h('p', { text: s.text }));
    if (s.note) body.appendChild(h('p', { class: 'step-note', text: s.note }));
    li.appendChild(fig); li.appendChild(body);
    steps.appendChild(li); els.push(li);
  });
  sticky.appendChild(stack); sticky.appendChild(prog); sticky.appendChild(label);

  function activate(n) {
    imgs.forEach(function (im, i) {
      im.classList.toggle('is-active', i === n);
      if (i === n) im.removeAttribute('aria-hidden'); else im.setAttribute('aria-hidden', 'true');
    });
    dots.forEach(function (d, i) { d.classList.toggle('is-active', i === n); d.classList.toggle('done', i < n); });
    els.forEach(function (e, i) { e.classList.toggle('is-active', i === n); });
    label.textContent = (n + 1) + ' av ' + stages.length + ': ' + stages[n].title;
  }
  activate(0);

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) activate(els.indexOf(e.target)); });
    }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
    els.forEach(function (e) { io.observe(e); });
  }
})();
