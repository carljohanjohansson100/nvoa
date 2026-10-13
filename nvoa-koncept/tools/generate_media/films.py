"""Animerade scener: hero (vattnets kretslopp) + tre filmer. Allt är deterministiskt: draw(t) ritar bilden vid tid t."""
import json
from lib import *
from engine import build_page

# =====================================================================
# HERO – vattnets kretslopp (1200 x 700)
# =====================================================================
HERO_PTS = [(170, 480), (360, 480), (360, 320), (400, 320), (400, 490), (640, 490), (640, 335), (682, 335), (682, 372),
            (682, 440), (940, 440), (940, 405), (1100, 405), (1100, 580), (110, 580), (110, 480), (170, 480)]
IA, IB, IC = 8, 11, 12  # index: slut kran/handfat, start bassäng, slut bassäng


def hero_static(poster=False):
    SH = 400  # vänsterförskjutning: extra sjö och natur bakom textpanelen
    d = Doc(1700, 700, 'Vattnets kretslopp: från sjö via vattenverk och rör till kranen i ett hem, vidare i avloppet till reningsverket och tillbaka till sjön.')
    d.d(lg('hsky', '#a9d8f0', '#f3fbfe'), lg('hlake', P['water2'], P['water']), lg('hsoil', '#9a7a58', '#6e5440'),
        lg('hbas', '#8fd0cf', P['teal']))
    b = []
    b.append(rect(0, 0, 1700, 420, 'url(#hsky)'))
    b.append(g(circ(1410, 110, 60, P['warm'], 'opacity=".2"') + circ(1410, 110, 38, '#ffc766') +
               ''.join(line(1410, 110 - 52, 1410, 110 - 70, '#ffc766', 5, f'transform="rotate({a} 1410 110)"') for a in range(0, 360, 45)), None, 'id="sun"'))
    for i, (x, y, s_) in enumerate([(150, 90, 1.5), (700, 60, 1.2), (1150, 130, 1.0)]):
        b.append(g(cloud(0, 0, s_, .95), f'translate({x} {y})', f'id="cl{i}"'))
    b.append(poly([(0, 330), (130, 230), (300, 320), (420, 200), (560, 300), (720, 190), (860, 300), (1020, 230), (1200, 320), (1360, 240), (1500, 320), (1700, 300), (1700, 410), (0, 410)], '#9db9c6'))
    b.append(path('M0 372 C200 330 400 360 600 345 S 1000 320 1200 355 S 1600 330 1700 350 V420 H0Z', P['green3']))
    b.append(path('M0 392 C300 365 600 395 900 378 S 1500 370 1700 388 V430 H0Z', P['green2']))
    b.append(rect(0, 398, 1700, 14, P['green']))
    b.append(rect(0, 410, 1700, 290, 'url(#hsoil)'))
    for x, y in [(60, 640), (250, 560), (520, 620), (800, 560), (1050, 650), (1380, 600), (1180, 520), (400, 520)]:
        b.append(ell(x, y, 16, 9, P['earth2'], 'opacity=".45"'))
    # sjö (bred, bakom textpanelen)
    b.append(path(f'M0 400 H{250 + SH} C{264 + SH} 432 {264 + SH} 482 {238 + SH} 518 L0 545Z', 'url(#hlake)'))
    b.append(path(f'M0 400 H{250 + SH}', 'none', P['foam'], 3, 'id="w0" opacity=".9"'))
    b.append(path(f'M0 430 H{250 + SH}', 'none', '#ffffff', 2.5, 'id="w1" opacity=".5"'))
    for i, (x, y, s_, k) in enumerate([(30, 402, 1.5, 'pine'), (90, 402, 1.2, 'pine'), (150, 402, 1.6, 'pine'), (225, 402, 1.2, 'pine'), (290, 402, 1.5, 'pine'),
                                        (360, 402, 1.3, 'round'), (430, 402, 1.5, 'pine'), (510, 402, 1.2, 'pine'), (580, 402, 1.4, 'pine'), (645, 402, 1.2, 'round'),
                                        (1200, 404, 1.5, 'round'), (1260, 404, 1.2, 'pine'), (1670, 404, 1.3, 'pine')]):
        b.append(g(tree(0, 0, s_, k), f'translate({x} {y})', f'id="tr{i}"'))
    # själva kretsloppet (förskjutet)
    c = []
    c.append(rect(300, 292, 120, 108, '#e9eef0', 3) + poly([(290, 295), (360, 248), (430, 295)], P['deep']))
    c.append(rect(316, 316, 24, 28, P['water2'], 2) + rect(380, 316, 24, 28, P['water2'], 2) + drop(360, 300, .6, '#ffffff'))
    c.append(rect(434, 300, 44, 100, P['grey2'], 2) + ell(456, 300, 22, 7, '#e5eef2') + rect(434, 340, 44, 10, P['water'], 0, 'opacity=".85"'))
    c.append(rect(590, 285, 170, 115, '#f7efe0', 3) + poly([(574, 289), (675, 218), (776, 289)], P['brick']) + rect(715, 232, 14, 34, P['earth2']))
    c.append(rect(604, 300, 56, 46, P['water2'], 3, f'stroke="{P["ink"]}" stroke-width="3"') + rect(720, 330, 28, 70, P['earth'], 2))
    c.append(rect(610, 376, 150, 24, '#d7c7a4') + rect(656, 366, 56, 12, '#cfd8dc', 4, f'stroke="{P["grey"]}" stroke-width="2"'))
    c.append(rect(918, 376, 236, 60, '#c8d4da', 3))
    c.append(rect(928, 390, 100, 40, 'url(#hbas)', 3) + rect(1044, 390, 100, 40, 'url(#hbas)', 3))
    c.append(rect(1150, 330, 50, 70, '#e9eef0', 3) + rect(1160, 346, 14, 16, P['water2'], 2) + rect(1180, 346, 10, 16, P['water2'], 2))
    A = HERO_PTS[:IA + 1]
    Bp = HERO_PTS[IA:IB + 1]
    Cp = HERO_PTS[IC:]
    c.append(pipe(A, '#d6ebf5', 13))
    c.append(pipe(Bp, '#dedcb8', 13))
    c.append(pipe(Cp, '#d6ebf5', 13))
    c.append(g('', None, 'id="dots"'))
    if poster:
        import math
        pts = HERO_PTS
        cum = [0]
        for i in range(1, len(pts)):
            cum.append(cum[-1] + math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]))
        L = cum[-1]
        for k in range(30):
            dd = (k / 30 + .02) * L
            i = 1
            while i < len(cum) - 1 and cum[i] < dd:
                i += 1
            s_ = (dd - cum[i - 1]) / (cum[i] - cum[i - 1])
            x = pts[i - 1][0] + (pts[i][0] - pts[i - 1][0]) * s_
            y = pts[i - 1][1] + (pts[i][1] - pts[i - 1][1]) * s_
            col = P['water'] if i <= IA else (P['waste'] if i <= IB else (P['teal'] if i <= IC else P['water2']))
            c.append(circ(round(x, 1), round(y, 1), 5.5, col, 'stroke="#ffffff" stroke-width="1.5"'))
    b.append(g(''.join(c), f'translate({SH} 0)'))
    return d, ''.join(b)


HERO_JS = """
FILM={id:'hero',D:24,still:6,caps:[],
init:function(){
 var PTS=__PTS__;this.R=H.along(PTS);var R=this.R;
 this.L1=R.cum[__IA__];this.L2=R.cum[__IB__];this.L3=R.cum[__IC__];
 this.N=30;this.dots=[];var g=H.$('dots');
 for(var i=0;i<this.N;i++){this.dots.push(H.el('circle',{r:5.5,stroke:'#fff','stroke-width':1.5},g))}
},
draw:function(t){
 var self=this,R=this.R,K=H.TAU;
 for(var i=0;i<this.N;i++){
  var d=H.ph(t,2,i/this.N)*R.L,p=R.at(d),c;
  if(d<this.L1)c='#2a7fb8';else if(d<this.L2)c='#8b8a5c';
  else if(d<this.L3)c=H.col('#8b8a5c','#3aa6a0',(d-this.L2)/(this.L3-this.L2));else c='#4fb3de';
  this.dots[i].setAttribute('cx',p[0].toFixed(1));this.dots[i].setAttribute('cy',p[1].toFixed(1));this.dots[i].setAttribute('fill',c);
 }
 var span=2000,x0=[150,700,1250];
 for(var i=0;i<3;i++){var x=((x0[i]+span*t/FILM.D)%span)-150;H.tf('cl'+i,'translate('+x.toFixed(1)+' '+[90,60,130][i]+')')}
 H.tf('sun','rotate('+(360*t/FILM.D).toFixed(1)+' 1410 110)');
 for(var w=0;w<2;w++){var s='M0 '+(400+w*30);for(var x=0;x<=650;x+=10){s+=' L'+x+' '+(400+w*30+Math.sin(x/22+K*t*(2+w)/FILM.D*(w?-1:1))*3.2).toFixed(1)}H.$('w'+w).setAttribute('d',s)}
 for(var i=0;i<13;i++){H.tf('tr'+i,'translate('+[30,90,150,225,290,360,430,510,580,645,1200,1260,1670][i]+' 404) rotate('+(Math.sin(K*2*t/FILM.D+i)*1.6).toFixed(2)+')')}
}};
""".replace('__PTS__', json.dumps([list(p) for p in HERO_PTS])).replace('__IA__', str(IA)).replace('__IB__', str(IB)).replace('__IC__', str(IC))


def hero_scene():
    d, svg = hero_static()
    return build_page('Vattnets kretslopp (illustration)', d.title, 1700, 700, svg, HERO_JS, '#a9d8f0', ''.join(d.defs))


def hero_poster():
    d, svg = hero_static(True)
    d.body = [svg]
    return d.out()


# =====================================================================
# FILM 1 – En dag på reningsverket (800 x 420)
# =====================================================================
def f1_static():
    b = []
    d = Doc(800, 420, 'En dag på reningsverket: avloppsvatten passerar galler, sedimentering och luftning och släpps ut renat i en sjö.')
    d.d(lg('f1w', '#b9b78a', '#8b8a5c'), lg('f1w2', '#8fd0cf', P['teal']), lg('f1w3', P['water2'], P['water']), lg('f1soil', '#9a7a58', '#6e5440'))
    b.append(rect(0, 0, 800, 215, '#bfe3f5', 0, 'id="sky"'))
    b.append(g(circ(0, 0, 34, P['warm'], 'opacity=".25"') + circ(0, 0, 20, '#ffc766'), None, 'id="sun"'))
    b.append(g(circ(0, 0, 18, '#f1efe0'), None, 'id="moon"'))
    b.append(g(cloud(0, 0, .9, .9), None, 'id="cl0"'))
    b.append(path('M0 205 C150 180 300 200 450 190 S 700 175 800 195 V220 H0Z', P['green3']))
    b.append(rect(0, 208, 800, 10, P['green']))
    b.append(rect(0, 216, 800, 204, 'url(#f1soil)'))
    # byggnad + gångväg
    b.append(rect(10, 150, 60, 60, '#e9eef0', 2) + poly([(4, 152), (40, 126), (76, 152)], P['deep']) + rect(24, 170, 14, 40, P['warm'], 2) + rect(46, 168, 18, 16, P['water2'], 2))
    b.append(rect(560, 164, 14, 46, P['grey']) + circ(567, 162, 10, P['warm']))
    # bassänger (betong)
    for (x, w_, y, h_, fill) in [(70, 80, 232, 120, 'f1w'), (190, 170, 232, 120, 'f1w'), (400, 180, 232, 120, 'f1w2')]:
        b.append(rect(x - 8, y - 6, w_ + 16, h_ + 14, '#c8d4da', 4))
        b.append(rect(x, y + 6, w_, h_ - 8, f'url(#{fill})', 2))
    # sedimentering: slambotten
    b.append(path('M190 340 L360 340 L360 330 Q330 318 275 326 Q220 318 190 330Z', '#6e5a3c', None, 0, 'opacity=".9"'))
    # luftare
    for i in range(6):
        b.append(rect(418 + i * 28, 338, 14, 4, P['ink'], 2))
    # sjö
    b.append(rect(626, 226, 174, 130, 'url(#f1w3)', 0))
    b.append(path('M626 226 C640 244 640 300 626 356 V226Z', P['grey2']))
    b.append(path('M626 226 H800', 'none', P['foam'], 3, 'id="lw" opacity=".9"'))
    for x in [690, 730, 770]:
        b.append(line(x, 232, x - 4, 205, P['green'], 3) + line(x + 7, 232, x + 12, 204, P['green'], 3))
    # rör
    b.append(poly([(0, 262), (70, 262)], 'none', P['deep'], 16) + poly([(0, 262), (70, 262)], 'none', '#dedcb8', 11))
    for (x1, x2) in [(150, 190), (360, 400), (580, 626)]:
        b.append(poly([(x1, 262), (x2, 262)], 'none', P['deep'], 16) + poly([(x1, 262), (x2, 262)], 'none', '#d6ebf5', 11))
    # galler
    b.append(g(''.join(line(100 + i * 10, 240, 100 + i * 10, 345, P['ink'], 3) for i in range(5)), None, 'id="screen"'))
    b.append(g(rect(-3, -8, 6, 22, P['ink'], 2) + ''.join(line(-18 + i * 9, 14, -18 + i * 9, 26, P['warm2'], 3) for i in range(5)) + rect(-24, 10, 48, 5, P['warm2'], 2), 'translate(125 240)', 'id="rake"'))
    b.append(g(''.join(circ(0 + i * 6, -i % 2 * 4, 3.5, '#6e5a3c') for i in range(6)), 'translate(86 345)'))
    # markerade steg
    for i, (x, w_, lab) in enumerate([(70, 80, '1 Galler'), (190, 170, '2 Sedimentering'), (400, 180, '3 Luftning'), (626, 174, '4 Utlopp')]):
        b.append(rect(x - 8, 226, w_ + 16, 134, 'none', 6, f'id="hl{i}" stroke="{P["warm"]}" stroke-width="5" opacity="0"'))
        cx = x + w_ / 2
        b.append(rect(cx - 62, 366, 124, 26, P['ink'], 13, 'opacity=".72"') + text(cx, 384, lab, 14, '#ffffff'))
    b.append(g('', None, 'id="parts"'))
    b.append(g('', None, 'id="dots"'))
    b.append(g(person(0, 0, .95, '#ffffff', P['ink'], SKIN[1], '#2a1c14', True, True), 'translate(100 210)', 'id="wk"'))
    b.append(g(
        path('M0 0 q16 -8 32 0 q-8 6 -16 6 q-8 0 -16 -6Z', '#ef8a3d') + path('M32 0 l8 -4 l0 8Z', '#ef8a3d') + circ(8, -1, 1.6, P['ink']),
        None, 'id="fish0"'))
    b.append(g(
        path('M0 0 q16 -8 32 0 q-8 6 -16 6 q-8 0 -16 -6Z', '#f1c04a') + path('M32 0 l8 -4 l0 8Z', '#f1c04a') + circ(8, -1, 1.6, P['ink']),
        None, 'id="fish1"'))
    d.body = b
    return d, ''.join(b)


F1_JS = """
FILM={id:'reningsverk',D:28,still:8,
caps:[[0,6,'Avloppsvatten från hem och verksamheter rinner in till reningsverket.'],
[6,12,'Först fångas det grova. Ett galler tar bort sådant som inte hör hemma i avloppet.'],
[12,18,'I sedimenteringsbassängen sjunker tungt material till botten och blir slam.'],
[18,24,'I luftningsbassängen får bakterier syre av luftbubblor. De bryter ner det som är löst i vattnet.'],
[24,28,'Det renade vattnet leds ut i en sjö. Reningsverket arbetar hela dygnet.']],
init:function(){
 var p=H.$('parts');this.sed=[];this.bub=[];this.N=22;this.dots=[];
 for(var i=0;i<18;i++)this.sed.push(H.el('circle',{r:2.6,fill:'#6e5a3c'},p));
 for(var i=0;i<24;i++)this.bub.push(H.el('circle',{r:3,fill:'none',stroke:'#fff','stroke-width':1.6,opacity:.8},p));
 var g=H.$('dots');for(var i=0;i<this.N;i++)this.dots.push(H.el('circle',{r:4.2,stroke:'#fff','stroke-width':1},g));
 this.seed=[];for(var i=0;i<18;i++)this.seed.push([(i*37%100)/100,(i*53%100)/100]);
},
draw:function(t){
 var D=FILM.D,K=H.TAU;
 var a=K*t/D,sunY=-Math.sin(a),day=H.clamp(.5+1.4*Math.sin(a),0,1);
 H.$('sky').setAttribute('fill',H.col('#16324a','#bfe3f5',day));
 H.tf('sun','translate('+(400-340*Math.cos(a)).toFixed(1)+' '+(205-170*Math.sin(a)).toFixed(1)+')');
 H.op('sun',Math.sin(a)>-.05?1:0);
 H.tf('moon','translate('+(400+340*Math.cos(a)).toFixed(1)+' '+(205+170*Math.sin(a)).toFixed(1)+')');
 H.op('moon',Math.sin(a)<.05?1:0);
 H.tf('cl0','translate('+(((100+900*t/D)%900)-100).toFixed(1)+' 60)');
 // flödet: gråbrunt -> klart
 for(var i=0;i<this.N;i++){var f=H.ph(t,2,i/this.N),x=f*800;
  var k=H.clamp((x-60)/560,0,1);var d=this.dots[i];d.setAttribute('cx',x.toFixed(1));d.setAttribute('cy',(262+Math.sin(f*40+i)*2.5).toFixed(1));
  d.setAttribute('fill',H.col('#8b8a5c','#7cc4e8',k));d.setAttribute('opacity',.95)}
 // rivare
 H.tf('rake','translate(125 '+(244+34*(.5+.5*Math.sin(K*6*t/D))).toFixed(1)+')');
 // slam
 for(var i=0;i<18;i++){var f=H.ph(t,3,this.seed[i][0]),x=205+this.seed[i][1]*140+Math.sin(f*9+i)*4,y=244+f*84;
  var c=this.sed[i];c.setAttribute('cx',x.toFixed(1));c.setAttribute('cy',y.toFixed(1));c.setAttribute('opacity',H.clamp(4*(1-f),0,1).toFixed(2))}
 // bubblor
 for(var i=0;i<24;i++){var f=H.ph(t,4,(i*.173)%1),x=424+(i%6)*28+Math.sin(f*14+i)*4,y=336-f*84,c=this.bub[i];
  c.setAttribute('cx',x.toFixed(1));c.setAttribute('cy',y.toFixed(1));c.setAttribute('r',(2+f*2.2).toFixed(1));c.setAttribute('opacity',(1-f*.6).toFixed(2))}
 // markering av aktivt steg
 var s=t<6?-1:t<12?0:t<18?1:t<24?2:3;
 for(var i=0;i<4;i++)H.op('hl'+i,i===s?.95:0);
 // vattenyta sjö
 var w='M626 226';for(var x=626;x<=800;x+=8)w+=' L'+x+' '+(226+Math.sin(x/16+K*3*t/D)*2.2).toFixed(1);H.$('lw').setAttribute('d',w);
 // medarbetare på gångväg
 var wf=H.seg(t,3,25),wx=60+wf*520;H.tf('wk','translate('+wx.toFixed(1)+' 211)');H.op('wk',H.pulse(t,3,25,1.2));
 // fiskar
 for(var i=0;i<2;i++){var f=H.ph(t,1,i*.5),x=650+f*110;H.tf('fish'+i,'translate('+x.toFixed(1)+' '+(300+i*28+Math.sin(f*K*2)*4).toFixed(1)+')');H.op('fish'+i,H.pulse(f,0,1,.12))}
}};
"""


def film1():
    d, svg = f1_static()
    return build_page('En dag på reningsverket (illustrerad film)', d.title, 800, 420, svg, F1_JS, '#16324a', ''.join(d.defs))


# =====================================================================
# FILM 2 – Så blir matavfall biogas (800 x 420)
# =====================================================================
GAS = [(485, 128), (485, 100), (618, 100), (618, 262)]
DIG = [(500, 306), (500, 374), (735, 374), (735, 392)]


def f2_static():
    b = []
    d = Doc(800, 420, 'Så blir matavfall biogas: matavfall från ett kök hämtas av en sopbil, rörs om i en tank utan syre, blir biogas till en buss och biogödsel till åkern.')
    d.d(lg('f2s', '#bfe3f5', '#eef9fd'), lg('f2d', '#7a5a3c', '#5b4332'))
    b.append(rect(0, 0, 800, 305, 'url(#f2s)'))
    b.append(g(cloud(0, 0, 1, .95), 'translate(260 50)', 'id="cl0"'))
    b.append(g(cloud(0, 0, .8, .9), 'translate(600 90)', 'id="cl1"'))
    b.append(path('M0 292 C120 268 260 290 400 276 S 680 262 800 280 V310 H0Z', P['green3']))
    b.append(rect(0, 298, 800, 8, P['green']))
    b.append(rect(0, 300, 800, 50, '#93a8b3') + line(0, 325, 800, 325, '#ffffff', 3, 'stroke-dasharray="22 16" opacity=".7"'))
    b.append(rect(0, 350, 800, 70, P['green2']))
    b.append(rect(0, 350, 800, 5, P['green']))
    # kök
    b.append(rect(14, 96, 226, 206, '#f7efe0', 4) + rect(8, 88, 238, 14, P['brick'], 3))
    b.append(rect(34, 124, 74, 60, P['water2'], 3, f'stroke="{P["ink"]}" stroke-width="3"') + line(71, 124, 71, 184, P['ink'], 3) + line(34, 154, 108, 154, P['ink'], 3))
    b.append(rect(24, 252, 206, 50, '#d7c7a4') + rect(24, 248, 206, 8, '#e9dcc0', 2))
    b.append(rect(88, 216, 56, 34, P['green'], 5) + rect(94, 228, 44, 3, '#ffffff', 1, 'opacity=".4"'))
    b.append(g(rect(0, -6, 62, 8, P['green2'], 3), 'translate(86 216)', 'id="lid"'))
    b.append(g('', None, 'id="scraps"'))
    b.append(g(rect(-14, -4, 28, 36, P['paper'], 4, f'stroke="{P["grey"]}" stroke-width="2"') + path('M-8 -4 q8 -12 16 0', 'none', P['green'], 3), 'translate(186 250)', 'id="bag"'))
    # anläggning
    b.append(rect(404, 292, 164, 10, P['ink'], 2))
    b.append(rect(420, 168, 132, 126, '#c8d4da', 3))
    b.append(path('M420 168 A66 46 0 0 1 552 168Z', '#e5eef2'))
    b.append(rect(436, 196, 100, 78, '#6d5239', 30))
    for r_ in range(4):
        b.append(line(420, 190 + r_ * 24, 552, 190 + r_ * 24, '#b7c6cd', 2, 'opacity=".5"'))
    b.append(g('', None, 'id="mix"'))
    # rör
    b.append(poly(GAS, 'none', P['deep'], 15) + poly(GAS, 'none', '#f7e0a8', 10))
    b.append(poly(DIG, 'none', P['deep'], 15) + poly(DIG, 'none', '#c8b89a', 10))
    b.append(rect(604, 262, 28, 38, P['warm'], 4) + rect(610, 268, 16, 10, P['ink'], 2) + circ(618, 258, 8, P['warm2']))
    b.append(g('', None, 'id="gasdots"') + g('', None, 'id="digdots"'))
    # åker
    for i, x in enumerate([650, 690, 730, 770]):
        b.append(g(path('M0 0 V-30', 'none', P['green'], 4) + path('M0 -14 q-14 -4 -16 -18 q14 2 16 18Z M0 -22 q14 -4 16 -18 q-14 2 -16 18Z', P['green2']) + path('M0 -30 q-6 -10 0 -20 q6 10 0 20Z', P['green3']),
                   f'translate({x} 408) scale(0.01)', f'id="sp{i}"'))
    b.append(g('', None, 'id="trk"'))
    # sopbil
    b.append(g(sopbil(0, 0, 1.15), 'translate(-200 338)', 'id="truck"'))
    # buss (kör åt höger)
    bus = (rect(-62, -66, 124, 50, P['water'], 8) + rect(-56, -58, 28, 24, P['foam'], 3) + rect(-22, -58, 28, 24, P['foam'], 3) + rect(12, -58, 28, 24, P['foam'], 3) +
           rect(44, -58, 14, 36, P['foam'], 3) + circ(-38, -14, 12, P['ink']) + circ(38, -14, 12, P['ink']) + circ(-38, -14, 5, P['grey2']) + circ(38, -14, 5, P['grey2']) +
           rect(-62, -30, 124, 6, P['green'], 0) + path('M-20 -74 q10 -10 20 0', 'none', P['green'], 4))
    b.append(g(bus, 'translate(700 340)', 'id="bus"'))
    b.append(g('', None, 'id="smoke"'))
    d.body = b
    return d, ''.join(b)


F2_JS = """
FILM={id:'biogas',D:26,still:13,
caps:[[0,5,'Matavfallet läggs i en särskild påse i köket.'],
[5,11,'Sopbilen hämtar påsarna och kör dem till en behandlingsanläggning.'],
[11,17,'I en sluten tank rörs matavfallet om utan syre. Bakterier bryter ner det.'],
[17,22,'Då bildas biogas. Den kan bli bränsle till bussar och andra fordon.'],
[22,26,'Det som blir kvar kan användas som biogödsel på åkermark.']],
init:function(){
 this.GAS=H.along(__GAS__);this.DIG=H.along(__DIG__);
 var s=H.$('scraps');this.sc=[];for(var i=0;i<3;i++)this.sc.push(H.el('circle',{r:7,fill:['#f2c744','#d9662f','#9bcf6a'][i]},s));
 var m=H.$('mix');this.mx=[];for(var i=0;i<26;i++)this.mx.push(H.el('circle',{r:3.2,fill:['#9bcf6a','#f2c744','#d9662f','#c8a46a'][i%4]},m));
 var g=H.$('gasdots');this.gd=[];for(var i=0;i<12;i++)this.gd.push(H.el('circle',{r:4.5,fill:'#fff3c4',stroke:'#e0a82e','stroke-width':1.5},g));
 var q=H.$('digdots');this.dd=[];for(var i=0;i<10;i++)this.dd.push(H.el('circle',{r:4.5,fill:'#8d6e4f',stroke:'#fff','stroke-width':1},q));
},
draw:function(t){
 var D=FILM.D,K=H.TAU;
 H.tf('cl0','translate('+(((260+900*t/D)%900)-100).toFixed(1)+' 50)');H.tf('cl1','translate('+(((600+900*t/D)%900)-100).toFixed(1)+' 90)');
 // påsen och locket
 var lidOpen=H.pulse(t,.4,3.6,.5);H.tf('lid','translate(86 216) rotate('+(-lidOpen*70).toFixed(1)+' 0 0)');
 for(var i=0;i<3;i++){var a=.9+i*.8,f=H.seg(t,a,a+1.2),y=170+f*(i?66:68);var c=this.sc[i];
  c.setAttribute('cx',(104+i*14).toFixed(1));c.setAttribute('cy',y.toFixed(1));c.setAttribute('opacity',(f>0&&f<.98)?1:0)}
 H.tf('bag','translate(186 250) scale('+(1+.0*0)+')');H.op('bag',H.pulse(t,3,5.2,.5)>0?1:1);
 // sopbil: åker in 5-10, tippar 10-11.2
 var tf=H.ease(H.seg(t,4.6,9.8)),tx=-200+tf*(565);
 H.tf('truck','translate('+tx.toFixed(1)+' 338)');H.op('truck',H.pulse(t,4.4,11.4,.7));
 // omrörning i tanken
 for(var i=0;i<26;i++){var a=K*(t*2/D*3)+i*.6,r=14+(i%5)*7,x=486+Math.cos(a+i)*r*1.4,y=235+Math.sin(a+i)*r*.45,c=this.mx[i];
  c.setAttribute('cx',x.toFixed(1));c.setAttribute('cy',y.toFixed(1));c.setAttribute('opacity',H.mix(.35,1,H.pulse(t,10.5,22,1.5)).toFixed(2))}
 // gas
 var ge=H.pulse(t,12,22.5,1.2);
 for(var i=0;i<12;i++){var p=this.GAS.at(H.ph(t,3,i/12)*this.GAS.L),c=this.gd[i];c.setAttribute('cx',p[0].toFixed(1));c.setAttribute('cy',p[1].toFixed(1));c.setAttribute('opacity',ge.toFixed(2))}
 // buss
 var bf=H.ease(H.seg(t,18.4,22.8)),bx=690+bf*320;H.tf('bus','translate('+bx.toFixed(1)+' 340)');H.op('bus',H.pulse(t,14.2,23.2,.8));
 // biogödsel
 var de=H.pulse(t,19,25,.8);
 for(var i=0;i<10;i++){var p=this.DIG.at(H.ph(t,3,i/10)*this.DIG.L),c=this.dd[i];c.setAttribute('cx',p[0].toFixed(1));c.setAttribute('cy',p[1].toFixed(1));c.setAttribute('opacity',de.toFixed(2))}
 for(var i=0;i<4;i++){var s=H.ease(H.seg(t,21+i*.5,24.8))*1.0,o=1-H.seg(t,25.2,26);H.tf('sp'+i,'translate('+[650,690,730,770][i]+' 408) scale('+Math.max(.01,s).toFixed(3)+')');H.op('sp'+i,s>0.02?o:0)}
}};
""".replace('__GAS__', json.dumps([list(p) for p in GAS])).replace('__DIG__', json.dumps([list(p) for p in DIG]))


def film2():
    d, svg = f2_static()
    return build_page('Så blir matavfall biogas (illustrerad film)', d.title, 800, 420, svg, F2_JS, '#bfe3f5', ''.join(d.defs))


# =====================================================================
# FILM 3 – Vad händer när du spolar? (800 x 420)
# =====================================================================
F3_PTS = [(112, 232), (112, 292), (560, 292), (640, 292), (690, 292), (690, 336), (770, 336)]
PUMP_IDX_X = 560  # pumpens läge längs röret


def f3_static():
    b = []
    d = Doc(800, 420, 'Vad händer när du spolar? Avloppsvattnet rinner från toaletten genom rör under gatan till en pumpstation och vidare till reningsverket.')
    d.d(lg('f3s', '#bfe3f5', '#eef9fd'), lg('f3d', '#8d6e4f', '#6e5440'))
    b.append(rect(0, 0, 800, 240, 'url(#f3s)'))
    b.append(g(cloud(0, 0, 1, .95), 'translate(300 40)', 'id="cl0"'))
    b.append(g(cloud(0, 0, .8, .9), 'translate(640 70)', 'id="cl1"'))
    b.append(path('M0 226 C140 202 300 224 450 212 S 700 200 800 218 V250 H0Z', P['green3']))
    b.append(rect(0, 236, 800, 8, P['green']))
    b.append(rect(0, 244, 800, 176, 'url(#f3d)'))
    b.append(rect(190, 236, 340, 14, '#93a8b3'))  # gata
    # hus med badrum
    b.append(rect(20, 112, 170, 126, '#f7efe0', 3) + poly([(10, 116), (105, 56), (200, 116)], P['brick']))
    b.append(rect(34, 128, 142, 108, '#dfeef4', 2))
    for r_ in range(3):
        for c_ in range(5):
            b.append(rect(34 + c_ * 28.4, 128 + r_ * 36, 28.4, 36, 'none', 0, 'stroke="#ffffff" stroke-width="2"'))
    # toalett
    b.append(rect(112, 176, 40, 44, '#ffffff', 5, f'stroke="{P["grey"]}" stroke-width="2"') + rect(116, 170, 32, 8, '#ffffff', 3, f'stroke="{P["grey"]}" stroke-width="2"'))
    b.append(rect(120, 160, 14, 10, P['water2'], 2, 'id="btn"'))
    b.append(rect(80, 200, 44, 22, '#ffffff', 8, f'stroke="{P["grey"]}" stroke-width="2"') + rect(88, 218, 28, 18, '#ffffff', 4, f'stroke="{P["grey"]}" stroke-width="2"'))
    b.append(rect(86, 203, 32, 9, P['water2'], 4, 'id="bowl"'))
    b.append(g(ell(0, 0, 11, 3.5, '#ffffff', 'opacity=".9"') + ell(0, 0, 5, 1.8, P['water'], ''), 'translate(102 207)', 'id="swirl"'))
    # pumpstation
    b.append(rect(500, 258, 120, 76, '#cfdde5', 4, f'stroke="{P["grey"]}" stroke-width="3"'))
    b.append(rect(488, 216, 144, 30, P['brick'], 3) + poly([(480, 220), (560, 180), (640, 220)], P['ink']))
    b.append(rect(536, 224, 22, 22, P['water2'], 2))
    b.append(circ(560, 292, 24, '#ffffff', f'stroke="{P["ink"]}" stroke-width="4"') + circ(560, 292, 7, P['ink'], 'id="hub"'))
    b.append(g(''.join(line(0, 0, 0, -20, P['ink'], 4) for _ in [0]) + line(0, 0, 17, 10, P['ink'], 4) + line(0, 0, -17, 10, P['ink'], 4), 'translate(560 292)', 'id="pump"'))
    b.append(circ(600, 268, 5, '#4caf6a', 'id="led"'))
    # reningsverk
    b.append(rect(690, 262, 100, 100, '#c8d4da', 4) + rect(698, 282, 40, 36, P['teal'], 3) + rect(744, 282, 40, 36, P['water2'], 3) + rect(698, 324, 86, 28, P['water2'], 3))
    b.append(rect(700, 218, 60, 44, '#e9eef0', 3) + poly([(694, 220), (730, 194), (766, 220)], P['deep']) + rect(710, 230, 14, 16, P['water2'], 2))
    # rör
    pts = F3_PTS
    b.append(poly(pts, 'none', P['deep'], 16) + poly(pts, 'none', '#dedcb8', 11))
    # gatubrunn
    b.append(rect(284, 232, 40, 8, P['ink'], 2) + rect(296, 238, 16, 54, P['grey'], 0, 'opacity=".6"'))
    b.append(g('', None, 'id="dots"'))
    b.append(g(rect(-13, -7, 26, 14, '#ffffff', 5, f'stroke="{P["grey"]}" stroke-width="2"') + path('M-8 -2 q4 -3 8 0 t8 0', 'none', P['grey'], 1.8), 'translate(112 232)', 'id="wipe"'))
    # etiketter
    for (x, lab) in [(105, 'Hemma'), (400, 'Ledningar under gatan'), (560, 'Pumpstation'), (740, 'Reningsverk')]:
        wlab = 18 + len(lab) * 7.6
        b.append(rect(x - wlab / 2, 376, wlab, 26, P['ink'], 13, 'opacity=".75"') + text(x, 394, lab, 14, '#ffffff'))
    d.body = b
    return d, ''.join(b)


F3_JS = """
FILM={id:'spolning',D:24,still:14,
caps:[[0,6,'Du spolar. Vattnet och det som följer med försvinner ner genom toalettens avlopp.'],
[6,12,'Det rinner i husets rör vidare till ett större ledningsnät under gatan.'],
[12,18,'Pumpstationer hjälper vattnet vidare. Våtservetter och annat som inte ska spolas kan fastna i pumparna.'],
[18,24,'Spola bara kiss, bajs och toalettpapper. Då når avloppsvattnet reningsverket som det ska.']],
init:function(){
 this.R=H.along(__PTS__);this.N=26;this.dots=[];var g=H.$('dots');
 for(var i=0;i<this.N;i++)this.dots.push(H.el('circle',{r:4.4,stroke:'#fff','stroke-width':1.2},g));
 var pr=this.R.cum;this.pumpD=pr[2];this.beforeD=pr[1];
},
draw:function(t){
 var D=FILM.D,K=H.TAU,R=this.R;
 H.tf('cl0','translate('+(((300+900*t/D)%900)-100).toFixed(1)+' 40)');H.tf('cl1','translate('+(((640+900*t/D)%900)-100).toFixed(1)+' 70)');
 // spolning 1-4 s
 var fl=H.pulse(t,1,4.2,.3);
 H.$('btn').setAttribute('fill',fl>0&&t<1.7?'#f2a03d':'#7cc4e8');
 H.tf('swirl','translate(102 207) rotate('+(t*420).toFixed(0)+')');H.op('swirl',fl);
 H.$('bowl').setAttribute('height',(9-5*H.pulse(t,1.2,2.6,.4)).toFixed(1));
 // blockering 14-18
 var block=H.pulse(t,13.6,18.2,.4);
 // dropparna
 for(var i=0;i<this.N;i++){var d=H.ph(t,2,i/this.N)*R.L,p=R.at(d),c=this.dots[i];
  var after=d>this.pumpD;var o=.95;if(after)o=1-.85*block;
  c.setAttribute('cx',p[0].toFixed(1));c.setAttribute('cy',p[1].toFixed(1));
  c.setAttribute('fill',H.col('#8b8a5c','#3aa6a0',H.clamp((d-R.cum[3])/(R.L-R.cum[3]),0,1)));c.setAttribute('opacity',o.toFixed(2))}
 // pump
 H.tf('pump','translate(560 292) rotate('+((t*(block>.5?10:260))%360).toFixed(1)+')');
 var led=H.$('led');led.setAttribute('fill',block>.5?'#e0402f':'#4caf6a');led.setAttribute('opacity',block>.5?(.55+.45*Math.sin(t*14)).toFixed(2):1);
 // våtservett: färdas 5.5-13.6 till pumpen, fastnar, tas bort efter 18
 var wf=H.seg(t,5.5,13.6),wd=wf*this.pumpD,wp=R.at(wd);
 var jig=(t>13.6&&t<18)?Math.sin(t*30)*1.5:0;
 H.tf('wipe','translate('+(wp[0]+jig).toFixed(1)+' '+(wp[1]-(t>13.6?9:0)).toFixed(1)+')');
 H.op('wipe',t<5.5?0:(t<18?1:1-H.seg(t,18,19)));
}};
""".replace('__PTS__', json.dumps([list(p) for p in F3_PTS]))


def film3():
    d, svg = f3_static()
    return build_page('Vad händer när du spolar? (illustrerad film)', d.title, 800, 420, svg, F3_JS, '#bfe3f5', ''.join(d.defs))
