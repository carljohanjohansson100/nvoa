/* Förstoringsvy: Esc stänger, pil vänster/höger bläddrar, Home/End hoppar. Fokus återgår till bilden man tryckte på. */
(function () {
  'use strict';
  var N = window.NVOA, $ = function (i) { return document.getElementById(i); };
  var dlg = $('lightbox'); if (!dlg) return;
  var stage = $('lb-stage'), title = $('lb-title'), src = $('lb-source'), count = $('lb-count');
  var list = [], idx = 0, opener = null;

  function show(i) {
    idx = (i + list.length) % list.length;
    var it = list[idx];
    stage.textContent = '';
    stage.appendChild(N.render(it.id, { eager: true }));
    title.textContent = it.title;
    src.textContent = N.sourceLabel(it);
    count.textContent = 'Bild ' + (idx + 1) + ' av ' + list.length;
  }
  N.openLightbox = function (l, i, trigger) {
    list = l; opener = trigger || null; show(i);
    if (typeof dlg.showModal === 'function') dlg.showModal(); else dlg.setAttribute('open', '');
    $('lb-close').focus();
  };
  $('lb-prev').addEventListener('click', function () { show(idx - 1); });
  $('lb-next').addEventListener('click', function () { show(idx + 1); });
  $('lb-close').addEventListener('click', function () { dlg.close(); });
  dlg.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { e.preventDefault(); show(idx - 1); }
    else if (e.key === 'ArrowRight') { e.preventDefault(); show(idx + 1); }
    else if (e.key === 'Home') { e.preventDefault(); show(0); }
    else if (e.key === 'End') { e.preventDefault(); show(list.length - 1); }
  });
  dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });  // klick på bakgrunden
  dlg.addEventListener('close', function () { if (opener) opener.focus(); });
})();
