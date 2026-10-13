"""Gemensam mall och motor för självständiga filmscener (HTML + SVG + vanlig JS)."""

CSS = """
*{box-sizing:border-box}
html,body{margin:0;height:100%;background:#0b2a3b;color:#fff;font-family:system-ui,'Segoe UI',Roboto,sans-serif}
.film{display:flex;flex-direction:column;height:100%}
.stage{position:relative;flex:1 1 auto;min-height:0;background:__BG__}
.stage>svg#scene{position:absolute;inset:0;width:100%;height:100%;display:block}
.big{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:76px;height:76px;border-radius:50%;border:0;
  background:rgba(11,42,59,.78);cursor:pointer;display:flex;align-items:center;justify-content:center;padding:0}
.big svg{width:34px;height:34px;margin-left:5px}
.big[hidden]{display:none}
.cap{margin:0;padding:10px 14px;min-height:3.7em;font-size:15px;line-height:1.4;background:#0b2a3b;color:#fff;display:flex;align-items:center}
.bar{display:flex;align-items:center;gap:12px;padding:6px 12px 10px;background:#0b2a3b}
.bar button{flex:none;width:44px;height:44px;border-radius:50%;border:2px solid #f2a03d;background:transparent;color:#fff;cursor:pointer;
  display:flex;align-items:center;justify-content:center;padding:0}
.bar button svg{width:18px;height:18px}
.bar input{flex:1;min-width:0;height:44px;margin:0;accent-color:#f2a03d;cursor:pointer}
.tm{flex:none;font-size:13px;font-variant-numeric:tabular-nums;color:#d6eefa;min-width:5.6em;text-align:right}
:focus-visible{outline:3px solid #f2a03d;outline-offset:3px}
body.bare .cap,body.bare .bar,body.bare .big{display:none}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (max-width:480px){.tm{display:none}.cap{font-size:14px}}
"""

HELPERS = r"""
var H={TAU:Math.PI*2,NS:'http://www.w3.org/2000/svg',
 clamp:function(x,a,b){return Math.max(a,Math.min(b,x))},
 seg:function(t,a,b){return H.clamp((t-a)/(b-a),0,1)},
 ease:function(x){return x*x*(3-2*x)},
 mix:function(a,b,k){return a+(b-a)*k},
 ph:function(t,k,o){var v=(t*k/FILM.D+(o||0))%1;return v<0?v+1:v},
 pulse:function(t,a,b,f){return H.clamp(Math.min((t-a)/f,(b-t)/f),0,1)},
 el:function(n,a,p){var e=document.createElementNS(H.NS,n);for(var k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e},
 rgb:function(c){c=c.replace('#','');return [parseInt(c.substr(0,2),16),parseInt(c.substr(2,2),16),parseInt(c.substr(4,2),16)]},
 col:function(c1,c2,k){var a=H.rgb(c1),b=H.rgb(c2);return 'rgb('+Math.round(H.mix(a[0],b[0],k))+','+Math.round(H.mix(a[1],b[1],k))+','+Math.round(H.mix(a[2],b[2],k))+')'},
 $:function(i){return document.getElementById(i)},
 tf:function(id,v){var e=document.getElementById(id);if(e)e.setAttribute('transform',v)},
 op:function(id,v){var e=document.getElementById(id);if(e)e.setAttribute('opacity',v)},
 along:function(pts){var cum=[0];for(var i=1;i<pts.length;i++){cum.push(cum[i-1]+Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]))}
  return {cum:cum,L:cum[cum.length-1],at:function(d){d=Math.max(0,Math.min(this.L,d));var i=1;while(i<cum.length-1&&cum[i]<d)i++;
   var s=(d-cum[i-1])/((cum[i]-cum[i-1])||1);return [pts[i-1][0]+(pts[i][0]-pts[i-1][0])*s,pts[i-1][1]+(pts[i][1]-pts[i-1][1])*s]}}}
};
"""

ENGINE = r"""
(function(){
var F=window.FILM,D=F.D,$=H.$;
var rm=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var bare=/[?&]bare/.test(location.search);
if(bare){document.body.classList.add('bare');$('scene').setAttribute('preserveAspectRatio','xMidYMid slice');}
var t=F.still,playing=false,last=0,raf=0;
var mt=/[?&]t=([\d.]+)/.exec(location.search);if(mt)t=parseFloat(mt[1])%D;
var PLAY='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.5v15l13-7.5z" fill="currentColor"/></svg>';
var PAUSE='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z" fill="currentColor"/></svg>';
var pp=$('pp'),seek=$('seek'),big=$('big'),cap=$('cap'),tm=$('tm');
function fmt(s){s=Math.floor(s);return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2)}
function render(){
 F.draw(t);
 var txt='';for(var i=0;i<F.caps.length;i++){if(t>=F.caps[i][0]&&t<F.caps[i][1]){txt=F.caps[i][2];break}}
 if(cap.textContent!==txt)cap.textContent=txt;
 seek.value=Math.round(t/D*1000);seek.setAttribute('aria-valuetext',fmt(t)+' av '+fmt(D));
 tm.textContent=fmt(t)+' / '+fmt(D);
}
function ui(){
 pp.innerHTML=playing?PAUSE:PLAY;pp.setAttribute('aria-label',playing?'Pausa filmen':'Spela filmen');
 big.hidden=playing;big.innerHTML=PLAY;
 try{parent.postMessage({type:'nvoa-scene',id:F.id,playing:playing},'*')}catch(e){}
}
function tick(ts){if(!playing)return;var dt=Math.min(.1,(ts-last)/1000);last=ts;t=(t+dt)%D;render();raf=requestAnimationFrame(tick)}
function play(){if(playing)return;playing=true;last=performance.now();raf=requestAnimationFrame(tick);ui()}
function pause(){if(!playing)return;playing=false;cancelAnimationFrame(raf);ui()}
pp.addEventListener('click',function(){playing?pause():play()});
big.addEventListener('click',play);
seek.addEventListener('input',function(){t=(seek.value/1000)*D;if(t>=D)t=D-.001;render()});
window.addEventListener('message',function(e){var m=e.data;if(!m||!m.cmd)return;
 if(m.cmd==='play')play();else if(m.cmd==='pause')pause();else if(m.cmd==='toggle')playing?pause():play();else if(m.cmd==='query')ui()});
document.addEventListener('keydown',function(e){if(e.key===' '&&e.target===document.body){e.preventDefault();playing?pause():play()}});
if(F.init)F.init();
render();ui();
if(bare&&!rm)play();
})();
"""

PAGE = """<!doctype html>
<html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>__CSS__</style></head>
<body>
<main class="film" aria-label="__TITLE__">
<h1 class="vh">__TITLE__</h1>
<div class="stage">
<svg id="scene" viewBox="0 0 __W__ __H__" preserveAspectRatio="xMidYMid meet" role="img" aria-label="__ALT__"><title>__ALT__</title><defs>__DEFS__</defs>__SVG__</svg>
<button id="big" class="big" type="button" tabindex="-1" aria-hidden="true"></button>
</div>
<p id="cap" class="cap" lang="sv"></p>
<div class="bar">
<button id="pp" type="button" aria-label="Spela filmen"></button>
<input id="seek" type="range" min="0" max="1000" value="0" step="1" aria-label="Förlopp i filmen: dra för att hoppa i tiden">
<span id="tm" class="tm" aria-hidden="true"></span>
</div>
</main>
<script>__HELPERS__</script>
<script>__FILMJS__</script>
<script>__ENGINE__</script>
</body></html>
"""


def build_page(title, alt, w, h, svg, filmjs, bg='#bfe3f5', defs=''):
    return (PAGE.replace('__CSS__', CSS.replace('__BG__', bg)).replace('__TITLE__', title).replace('__ALT__', alt)
            .replace('__W__', str(w)).replace('__H__', str(h)).replace('__DEFS__', defs).replace('__SVG__', svg)
            .replace('__HELPERS__', HELPERS).replace('__FILMJS__', filmjs).replace('__ENGINE__', ENGINE))
