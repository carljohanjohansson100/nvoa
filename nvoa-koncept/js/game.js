/* Avfallets resa: sorteringsspel. Dra en sak till ett kärl, eller välj sak och sedan kärl (tangentbord och touch). */
(function () {
  'use strict';
  var N = window.NVOA, C = window.NVOA_CONTENT || {}, h = N.h;
  var itemsEl = document.getElementById('items'), binsEl = document.getElementById('bins');
  var fb = document.getElementById('feedback'), prog = document.getElementById('game-progress'), reset = document.getElementById('game-reset');
  if (!itemsEl || !binsEl) return;
  var ITEMS = C.items || [], BINS = C.bins || [];
  var binLabel = {}; BINS.forEach(function (b) { binLabel[b.id] = b.label.replace(/\u00ad/g, ''); });
  var st, itemBtn, binBtn, justDragged = false;

  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function say(msg, cls) { fb.textContent = msg; fb.className = 'feedback' + (cls ? ' ' + cls : ''); }
  function itemById(id) { return ITEMS.filter(function (i) { return i.id === id; })[0]; }

  function build() {
    st = { done: {}, counts: {}, wrong: 0, sel: null };
    itemsEl.textContent = ''; binsEl.textContent = ''; itemBtn = {}; binBtn = {};
    shuffle(ITEMS).forEach(function (it) {
      var li = h('li'), b = h('button', { type: 'button', class: 'item', 'data-id': it.id, 'aria-pressed': 'false' });
      b.appendChild(N.render(it.media, { decorative: true, eager: true }));
      b.appendChild(h('span', { text: it.name }));
      li.appendChild(b); itemsEl.appendChild(li); itemBtn[it.id] = b;
      b.addEventListener('click', function (ev) { if (justDragged && ev.detail > 0) return; toggle(it.id); });
      b.addEventListener('pointerdown', function (e) { startDrag(e, it, b); });
    });
    BINS.forEach(function (bn) {
      var b = h('button', { type: 'button', class: 'bin', 'data-bin': bn.id });
      b.appendChild(N.render('bin-' + bn.id, { decorative: true, eager: true }));
      b.appendChild(h('span', { text: bn.label }));
      b.appendChild(h('span', { class: 'count', 'aria-hidden': 'true', text: '0', hidden: true }));
      binsEl.appendChild(b); binBtn[bn.id] = b;
      b.addEventListener('click', function () {
        if (!st.sel) { say('Välj först en sak, och sedan det kärl där den hör hemma.'); return; }
        attempt(st.sel, bn.id);
      });
    });
    progress();
    say('Välj en sak för att börja. Du kan också dra den till ett kärl.');
  }

  function progress() {
    var n = Object.keys(st.done).length;
    prog.textContent = n + ' av ' + ITEMS.length + ' rätt';
  }

  function toggle(id) {
    if (st.sel === id) { select(null); say('Du avmarkerade saken. Välj en ny.'); return; }
    select(id);
    say('Du valde: ' + itemById(id).name + '. Tryck nu på det kärl där den hör hemma.');
  }
  function select(id) {
    st.sel = id;
    Object.keys(itemBtn).forEach(function (k) { itemBtn[k].setAttribute('aria-pressed', String(k === id)); });
  }

  function attempt(id, binId) {
    var it = itemById(id);
    if (!it || st.done[id]) return;
    if (it.bin === binId) {
      st.done[id] = true; st.counts[binId] = (st.counts[binId] || 0) + 1;
      select(null);
      var li = itemBtn[id].parentNode; li.hidden = true;
      var c = binBtn[binId].querySelector('.count'); c.hidden = false; c.textContent = st.counts[binId];
      binBtn[binId].classList.remove('pop'); void binBtn[binId].offsetWidth; binBtn[binId].classList.add('pop');
      progress();
      var left = ITEMS.length - Object.keys(st.done).length;
      if (!left) {
        say('Bra jobbat! Alla ' + ITEMS.length + ' saker hamnade rätt' + (st.wrong ? ' (' + st.wrong + ' fel kärl på vägen – så lär man sig).' : ', utan ett enda felsteg.') + ' Tryck på Börja om om du vill spela igen.', 'done');
        reset.focus();
      } else {
        say('Rätt! ' + it.name + ' hör hemma i ' + binLabel[binId].toLowerCase() + '. ' + left + ' kvar.', 'ok');
        var next = ITEMS.filter(function (x) { return !st.done[x.id]; })[0];
        var shown = Object.keys(itemBtn).filter(function (k) { return !st.done[k]; })[0];
        if (shown && document.activeElement && (document.activeElement === document.body || binsEl.contains(document.activeElement) || itemsEl.contains(document.activeElement))) itemBtn[shown].focus({ preventScroll: true });
      }
    } else {
      st.wrong++;
      var b = itemBtn[id]; b.classList.remove('shake'); void b.offsetWidth; b.classList.add('shake');
      say('Inte riktigt, men bra försök! ' + it.hint + ' Prova ett annat kärl.', 'try');
    }
  }

  /* Dra och släpp med pekare (mus, penna och touch) */
  function startDrag(e, it, btn) {
    if (e.button > 0 || st.done[it.id]) return;
    var x0 = e.clientX, y0 = e.clientY, ghost = null, over = null, moved = false;
    function binAt(x, y) { var el = document.elementFromPoint(x, y); return el && el.closest ? el.closest('.bin') : null; }
    function move(ev) {
      if (!moved && Math.hypot(ev.clientX - x0, ev.clientY - y0) < 8) return;
      if (!moved) {
        moved = true; btn.classList.add('dragging');
        ghost = h('div', { class: 'drag-ghost', 'aria-hidden': 'true' });
        ghost.appendChild(N.render(it.media, { decorative: true, eager: true })); ghost.appendChild(h('div', { text: it.name }));
        document.body.appendChild(ghost);
      }
      ghost.style.left = ev.clientX + 'px'; ghost.style.top = ev.clientY + 'px';
      var b = binAt(ev.clientX, ev.clientY);
      if (b !== over) { if (over) over.classList.remove('over'); over = b; if (b) b.classList.add('over'); }
    }
    function end(ev) {
      document.removeEventListener('pointermove', move); document.removeEventListener('pointerup', end); document.removeEventListener('pointercancel', end);
      if (!moved) return;
      justDragged = true; setTimeout(function () { justDragged = false; }, 60);
      btn.classList.remove('dragging'); if (ghost) ghost.remove(); if (over) over.classList.remove('over');
      var b = ev.type === 'pointerup' ? binAt(ev.clientX, ev.clientY) : null;
      if (b) attempt(it.id, b.getAttribute('data-bin')); else say('Du släppte saken utanför kärlen. Försök igen.');
    }
    document.addEventListener('pointermove', move); document.addEventListener('pointerup', end); document.addEventListener('pointercancel', end);
  }

  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && st && st.sel && document.getElementById('game').contains(document.activeElement)) { select(null); say('Valet är avmarkerat.'); } });
  reset.addEventListener('click', function () { build(); var f = itemsEl.querySelector('.item'); if (f) f.focus(); });
  build();
})();
