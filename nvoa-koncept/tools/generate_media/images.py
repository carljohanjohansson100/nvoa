"""Statiska illustrationer: vattnets väg (5), galleri (9), föremål (8), tunnor (7), karta (1)."""
from lib import *

W, H = 800, 500


def ground(d, y, c1=None, c2=None):
    d.a(rect(0, y, d.w, d.h - y, c1 or P['green2']))
    d.a(rect(0, y, d.w, 6, c2 or P['green']))


# ======================= VATTNETS VÄG =======================
def steg_kalla():
    d = Doc(W, H, 'Illustration: en skogssjö med berg i bakgrunden, en intagsbyggnad i vattnet och ett rör som leder in mot land.')
    sky(d)
    d.a(sun(660, 80))
    d.a(cloud(90, 70, 1.2), cloud(300, 110, .8, .9))
    # regnmoln
    d.a(cloud(430, 60, 1.1, 1, '#cfdde5'))
    for i in range(6):
        d.a(line(430 + i * 14, 85 + (i % 2) * 6, 424 + i * 14, 108 + (i % 2) * 6, P['water'], 2.5, 'opacity=".7"'))
    d.a(poly([(0, 280), (140, 150), (260, 250), (400, 140), (560, 270), (700, 170), (800, 260), (800, 330), (0, 330)], '#9db9c6'))
    d.a(poly([(400, 140), (418, 162), (396, 158), (384, 172)], '#ffffff', extra='opacity=".85"'))
    d.a(hills(W, 300, P['green3'], P['green2'], 40))
    for i, x in enumerate([30, 80, 130, 190, 620, 680, 735, 775]):
        d.a(tree(x, 318 + (i % 3) * 8, 1.0 + (i % 2) * .2, 'pine'))
    d.d(lg('lake', P['water2'], P['water']))
    d.a(path('M-10 345 C120 320, 260 335, 400 330 S 700 320, 810 340 V500 H-10Z', 'url(#lake)'))
    d.a(waves(40, 380, 300, 6), waves(380, 410, 340, 7), waves(90, 450, 260, 5, op=.35))
    d.a(path('M520 345 Q 600 360 700 350', 'none', '#ffffff', 3, 'opacity=".5"'))
    # intagsbyggnad
    d.a(rect(300, 360, 80, 60, P['grey2'], 4), rect(296, 350, 88, 14, P['deep'], 4), rect(318, 372, 14, 20, P['water2']), rect(346, 372, 14, 20, P['water2']))
    d.a(rect(336, 420, 8, 60, P['deep']))
    d.a(pipe([(380, 390), (470, 390), (470, 440), (620, 440), (800, 440)], P['water2'], 12))
    d.a(path('M760 425 l24 15 l-24 15Z', P['warm']))
    d.a(drop(180, 440, 1.2, '#ffffff'))
    return d.out()


def steg_vattenverk():
    d = Doc(W, H, 'Illustration: ett vattenverk med byggnad, tre runda tankar, filterbassänger och en medarbetare med hjälm som kontrollerar ett prov.')
    sky(d)
    d.a(cloud(120, 70, 1), cloud(560, 90, 1.1))
    d.a(hills(W, 300, P['green3'], P['green2'], 36))
    ground(d, 340)
    # huvudbyggnad
    d.a(rect(60, 190, 250, 150, '#e9eef0', 4), poly([(50, 192), (185, 140), (320, 192)], P['deep']))
    d.a(rect(90, 220, 50, 60, P['water2'], 3), rect(160, 220, 50, 60, P['water2'], 3), rect(230, 220, 50, 60, P['water2'], 3))
    d.a(rect(160, 290, 40, 50, P['warm'], 3))
    d.a(drop(185, 188, .9, '#ffffff'))
    # tankar
    for i, x in enumerate([350, 450, 550]):
        d.a(rect(x, 230, 80, 110, P['grey2']), ell(x + 40, 340, 40, 10, P['grey2']), ell(x + 40, 230, 40, 12, '#e5eef2'))
        d.a(rect(x, 268, 80, 14, P['water'], 0, 'opacity=".8"'), rect(x + 66, 232, 5, 108, P['grey'], 2))
        for k in range(5):
            d.a(rect(x + 62, 242 + k * 20, 14, 3, P['ink'], 1))
    d.a(pipe([(310, 320), (350, 320)], P['water'], 8), pipe([(430, 330), (450, 330)], P['water'], 8), pipe([(530, 330), (550, 330)], P['water'], 8))
    # filterbassänger
    d.a(rect(330, 372, 420, 90, '#cfdde5', 6))
    d.d(lg('fl', P['water2'], P['water']))
    for i in range(3):
        x = 345 + i * 135
        d.a(rect(x, 384, 120, 66, 'url(#fl)', 4), waves(x + 6, 400, 108, 5, op=.6, amp=3))
        d.a(rect(x, 434, 120, 16, P['sand'], 4, 'opacity=".9"'))
    d.a(person(110, 445, 1.5, '#ffffff', P['ink'], SKIN[1], '#2a1c14', True, False, 'out'))
    d.a(rect(138, 410, 14, 24, P['foam'], 3, f'stroke="{P["deep"]}" stroke-width="2"'), rect(138, 421, 14, 13, P['water'], 2))
    return d.out()


def steg_ledningsnat():
    d = Doc(W, H, 'Illustration: ett villaområde sett uppifrån gatan med ett genomskuret marklager där vattenledningar grenar sig till husen och avloppsrör går åt andra hållet.')
    sky(d, h=250)
    d.a(cloud(100, 50, 1), cloud(600, 70, .9))
    d.a(hills(W, 190, P['green3'], P['green2'], 30))
    d.a(rect(0, 220, W, 22, P['green2']))
    d.a(villa(40, 220, 110, 66), villa(210, 220, 100, 60, '#e9ddc4', P['water']), villa(380, 220, 110, 66, '#f1d9d0'), block(560, 220, 90, 112), villa(690, 220, 90, 56, '#e6e9c9', P['brick']))
    d.a(rect(0, 242, W, 22, P['grey'], 0), line(0, 253, W, 253, '#ffffff', 2, 'stroke-dasharray="14 12"'))
    d.d(lg('jord', P['earth'], P['earth2']))
    d.a(rect(0, 264, W, 236, 'url(#jord)'))
    for x, y in [(60, 470), (210, 300), (420, 480), (610, 300), (720, 470), (300, 472)]:
        d.a(ell(x, y, 10, 6, P['earth2'], 'opacity=".5"'))
    # huvudledning
    d.a(pipe([(0, 340), (800, 340)], P['water'], 16))
    for x in [95, 260, 435, 605, 735]:
        d.a(pipe([(x, 340), (x, 285)], P['water'], 8))
    # avlopp
    d.a(pipe([(0, 430), (800, 430)], P['waste'], 14))
    for x in [60, 230, 400, 640, 745]:
        d.a(pipe([(x, 430), (x, 300)], P['waste'], 6))
    # ventil och pumpstation
    d.a(circ(345, 340, 15, P['warm']), rect(340, 318, 10, 14, P['warm2']))
    d.a(rect(330, 380, 60, 36, P['grey2'], 4, f'stroke="{P["deep"]}" stroke-width="2"'), circ(360, 398, 9, P['water']), path('M355 398 h10 M360 393 v10', 'none', '#fff', 2))
    d.a(rect(24, 452, 190, 40, '#12303f', 8, 'opacity=".55"'))
    d.a(rect(36, 460, 22, 7, P['water2'], 3), text(66, 468, 'rent vatten', 13, '#ffffff', 'start'))
    d.a(rect(36, 477, 22, 7, '#c9c88a', 3), text(66, 485, 'avloppsvatten', 13, '#ffffff', 'start'))
    return d.out()


def steg_hemmet():
    d = Doc(W, H, 'Illustration: ett genomskuret hem. I köket rinner vatten ur en kran i ett glas, i badrummet finns en dusch och en toalett, och en tvättmaskin står bakom.')
    sky(d)
    d.a(hills(W, 330, P['green3'], P['green2'], 30))
    ground(d, 410)
    d.a(poly([(60, 150), (400, 60), (740, 150)], P['brick']))
    d.a(rect(90, 150, 620, 260, '#f7efe0', 4))
    d.a(rect(400, 150, 6, 260, '#e1d3b6'))
    # kök
    d.a(rect(120, 300, 250, 20, '#d7c7a4'), rect(120, 320, 250, 90, '#f0e2c4'))
    d.a(rect(160, 328, 70, 70, '#e3d2ac', 3), rect(250, 328, 70, 70, '#e3d2ac', 3))
    d.a(path('M200 300 v-24 a16 16 0 0 1 32 0', 'none', P['grey'], 6), rect(194, 296, 14, 6, P['grey']))
    d.a(ell(230, 300, 28, 6, P['grey']))
    for k, y in enumerate([282, 296, 310]):
        d.a(drop(246 + (k % 2) * 2, y - 8 + k * 4, .35, P['water2']))
    d.a(rect(280, 270, 26, 34, P['foam'], 4, f'stroke="{P["deep"]}" stroke-width="2.5"'), rect(281, 284, 24, 19, P['water2'], 3))
    d.a(rect(130, 190, 120, 70, P['water2'], 4, f'stroke="{P["ink"]}" stroke-width="3"'), line(190, 190, 190, 260, P['ink'], 3), line(130, 225, 250, 225, P['ink'], 3))
    # badrum
    d.a(rect(420, 190, 12, 110, P['grey']), circ(426, 188, 18, P['grey']))
    for i in range(6):
        d.a(line(448 + i * 10, 196, 440 + i * 12, 280, P['water2'], 2.5, 'opacity=".8"'))
    d.a(rect(420, 300, 140, 8, P['grey2']))
    d.a(rect(590, 330, 70, 56, '#ffffff', 8, f'stroke="{P["grey"]}" stroke-width="2"'), circ(625, 362, 20, P['water2'], f'stroke="{P["grey"]}" stroke-width="3"'))
    d.a(rect(600, 338, 20, 6, P['warm'], 2))
    d.a(rect(520, 330, 46, 58, '#ffffff', 6, f'stroke="{P["grey"]}" stroke-width="2"'), ell(543, 330, 23, 7, '#e6eef2'), rect(530, 388, 26, 10, '#ffffff', 3, f'stroke="{P["grey"]}" stroke-width="2"'))
    # människor
    d.a(person(335, 410, 1.1, P['green'], P['ink'], SKIN[1], '#2a1c14'))
    d.a(person(375, 410, .7, P['warm'], P['deep'], SKIN[2], '#a0642f'))
    # rör under huset
    d.a(rect(0, 410, W, 90, P['earth']))
    d.a(pipe([(0, 450), (220, 450), (220, 330)], P['water'], 10), pipe([(430, 450), (426, 300)], P['waste'], 8), pipe([(430, 450), (800, 450)], P['waste'], 10))
    d.a(path('M60 460 l8 -8 l8 8Z', P['warm']))
    return d.out()


def steg_reningsverk():
    d = Doc(W, H, 'Illustration: ett reningsverk sett från sidan med inlopp, galler, luftningsbassäng med bubblor, en rund slambassäng och rent vatten som rinner ut mot en sjö.')
    sky(d)
    d.a(sun(110, 70), cloud(330, 70, 1.1), cloud(620, 100, .9))
    d.a(hills(W, 300, P['green3'], P['green2'], 36))
    ground(d, 330)
    # lagerbyggnad
    d.a(rect(30, 250, 110, 80, '#e9eef0', 3), poly([(24, 252), (85, 220), (146, 252)], P['deep']), rect(58, 276, 26, 54, P['warm'], 2), rect(96, 270, 30, 24, P['water2'], 2))
    # bassänger
    d.a(rect(165, 335, 160, 100, '#cfdde5', 5))
    d.d(lg('wb', '#a9a77a', P['waste']))
    d.a(rect(175, 355, 140, 70, 'url(#wb)', 4))
    d.a(rect(345, 335, 210, 100, '#cfdde5', 5))
    d.d(lg('wc', P['water2'], P['teal']))
    d.a(rect(355, 355, 190, 70, 'url(#wc)', 4))
    for i, (x, y) in enumerate([(380, 410), (410, 395), (440, 412), (470, 392), (500, 408), (525, 396), (395, 380), (455, 378), (490, 374)]):
        d.a(circ(x, y, 4 + (i % 3), '#ffffff', 'opacity=".75"'))
    # rund slambassäng
    d.a(rect(575, 300, 110, 135, '#cfdde5', 6), ell(630, 300, 55, 14, '#e5eef2'), rect(585, 318, 90, 105, P['water2'], 4, 'opacity=".85"'))
    d.a(line(630, 300, 630, 420, P['ink'], 3), line(600, 420, 660, 420, P['ink'], 3))
    # utlopp till sjö
    d.a(pipe([(325, 395), (345, 395)], P['waste'], 8), pipe([(555, 395), (575, 395)], P['teal'], 8))
    d.a(rect(0, 435, W, 65, P['grey2']))
    d.a(pipe([(0, 470), (160, 470), (160, 400), (165, 395)], P['waste'], 10))
    d.d(lg('lk', P['water2'], P['water']))
    d.a(path('M700 435 C720 420, 780 420, 810 430 V500 H690Z', 'url(#lk)'))
    d.a(pipe([(685, 470), (740, 470)], P['water2'], 10))
    d.a(waves(710, 455, 90, 3, op=.6))
    for x in [715, 740, 765, 790]:
        d.a(line(x, 435, x - 4, 405, P['green'], 3), line(x + 6, 435, x + 10, 408, P['green'], 3))
    d.a(person(210, 335, .8, P['ink'], P['ink'], SKIN[0], '#4a3426', True, True))
    return d.out()


# ======================= GALLERI =======================
def gal_ledningsarbete():
    d = Doc(W, H, 'Illustration: två medarbetare i varselkläder och hjälm arbetar vid en öppen schakt i gatan där ett vattenrör läggs. En grävmaskin och trafikkoner står intill.')
    sky(d, h=260)
    d.a(cloud(120, 60, 1), cloud(560, 80, 1.2))
    d.a(hills(W, 190, P['green3'], P['green2'], 30), villa(60, 250, 120, 70), villa(560, 250, 120, 66, '#e9ddc4', P['water']))
    d.a(rect(0, 250, W, 40, P['grey']), line(0, 270, W, 270, '#fff', 2, 'stroke-dasharray="16 12" opacity=".7"'))
    d.d(lg('jd', P['earth'], P['earth2']))
    d.a(rect(0, 290, W, 210, 'url(#jd)'))
    d.a(poly([(250, 290), (550, 290), (500, 440), (300, 440)], '#5b4636'))
    d.a(pipe([(280, 410), (520, 410)], P['water'], 22))
    d.a(rect(380, 398, 8, 24, P['grey2']), rect(410, 398, 8, 24, P['grey2']))
    d.a(person(330, 290, 1.5, '#ffffff', P['ink'], SKIN[1], '#2a1c14', True, True, 'out'))
    d.a(person(480, 290, 1.4, '#ffffff', P['deep'], SKIN[0], '#a0642f', True, True, 'down', -1))
    # grävmaskin
    d.a(rect(620, 245, 120, 38, P['warm'], 6), rect(640, 205, 56, 45, P['warm'], 6), rect(650, 212, 36, 26, P['water2'], 3), rect(612, 275, 140, 18, P['ink'], 9))
    d.a(poly([(620, 255), (560, 190), (545, 200), (606, 270)], P['warm2']), poly([(560, 190), (530, 270), (545, 275), (575, 195)], P['warm2']))
    d.a(path('M520 270 h32 l-6 22 h-26Z', P['grey']))
    d.a(cone(205, 290, 1.4), cone(255, 290, 1.4), cone(570, 290, 1.4))
    d.a(line(205, 250, 255, 250, P['warm2'], 3), line(255, 250, 300, 250, P['warm2'], 3))
    d.a(circ(100, 360, 30, P['earth2'], 'opacity=".5"'), circ(700, 380, 24, P['earth2'], 'opacity=".5"'))
    return d.out()


def gal_pumpstation():
    d = Doc(W, H, 'Illustration: en liten pumpstation i tegel mitt i grönskan. En servicebil står utanför och en tekniker med surfplatta kontrollerar anläggningen.')
    sky(d)
    d.a(sun(120, 80), cloud(480, 70, 1.1), cloud(670, 120, .8))
    d.a(hills(W, 290, P['green3'], P['green2'], 40))
    for x in [40, 90, 700, 750]:
        d.a(tree(x, 340, 1.3, 'pine'))
    ground(d, 340)
    d.a(rect(0, 400, W, 100, P['grey'], 0), line(0, 450, W, 450, '#fff', 3, 'stroke-dasharray="20 14" opacity=".7"'))
    d.a(rect(300, 220, 200, 120, P['brick'], 3), poly([(288, 224), (400, 160), (512, 224)], P['ink']))
    d.a(rect(330, 260, 46, 80, P['grey'], 2), rect(334, 264, 38, 72, P['grey2']), line(353, 264, 353, 336, P['grey'], 2))
    d.a(rect(420, 250, 56, 36, P['water2'], 3, f'stroke="{P["foam"]}" stroke-width="4"'))
    d.a(drop(448, 262, .6, '#ffffff'))
    d.a(rect(520, 300, 70, 40, P['grey2'], 3), pipe([(500, 320), (520, 320)], P['water'], 8))
    d.a(rect(530, 290, 50, 10, P['deep'], 2), circ(555, 320, 10, P['warm']))
    d.a(van(180, 440, 1.2))
    d.a(person(630, 400, 1.35, P['ink'], P['deep'], SKIN[3], '#16100c', True, True))
    d.a(rect(642, 352, 30, 22, P['ink'], 3, f'stroke="{P["grey"]}" stroke-width="2"'), rect(645, 355, 24, 14, P['water2'], 1))
    return d.out()


def gal_atervinningscentral():
    d = Doc(W, H, 'Illustration: en återvinningscentral med stora färgade containrar, en ramp och människor som lämnar sorterade säckar. En bil väntar vid sidan.')
    sky(d)
    d.a(cloud(130, 60, 1), cloud(560, 90, 1), sun(700, 70))
    d.a(hills(W, 270, P['green3'], P['green2'], 34))
    ground(d, 330, P['grey2'], P['grey'])
    d.a(rect(0, 400, W, 100, '#b7c6cd'))
    # ramp
    d.a(poly([(40, 330), (760, 330), (760, 352), (40, 352)], '#9aaeb8'))
    cols = [(P['green'], 'mat'), (P['water'], 'glas'), (P['warm'], 'plast'), (P['brick'], 'metall'), ('#7d8f9a', 'rest')]
    for i, (c, _) in enumerate(cols):
        x = 70 + i * 135
        d.a(rect(x, 262, 110, 70, c, 4), rect(x - 4, 252, 118, 14, P['ink'], 4))
        for k in range(4):
            d.a(line(x + 20 + k * 24, 272, x + 20 + k * 24, 326, '#ffffff', 2, 'opacity=".25"'))
        d.a(circ(x + 55, 296, 14, '#ffffff', 'opacity=".9"'))
    d.a(path('M125 296 a7 7 0 1 0 14 0 a7 7 0 1 0 -14 0', P['green']), path('M258 292 h14 v10 h-14Z', P['water']))
    d.a(path('M395 303 l7 -14 l7 14Z', P['warm']), circ(530, 296, 6, P['brick']), path('M660 290 h12 v12 h-12Z', '#7d8f9a'))
    d.a(person(180, 440, 1.35, P['water'], P['ink'], SKIN[0], '#a0642f', False, False, 'out'))
    d.a(rect(205, 405, 26, 32, P['green2'], 6), path('M212 405 q6 -10 12 0', 'none', P['green'], 3))
    d.a(person(330, 450, 1.25, P['warm'], P['deep'], SKIN[3], '#16100c'))
    d.a(rect(348, 418, 28, 30, P['water2'], 6), path('M355 418 q7 -10 14 0', 'none', P['water'], 3))
    d.a(car(610, 460, 1.5, P['brick']))
    d.a(person(480, 450, .75, P['green'], P['ink'], SKIN[2], '#a0642f'))
    return d.out()


def gal_sorteringstunnor():
    d = Doc(W, H, 'Illustration: en rad med sju färgglada sorteringskärl med enkla symboler för matavfall, plast, papper, glas, metall, restavfall och elavfall.')
    sky(d)
    d.a(hills(W, 280, P['green3'], P['green2'], 30))
    ground(d, 330, P['sand'], '#e3d3a8')
    items = [(P['green'], 'apple'), (P['warm'], 'bottle'), (P['water'], 'paper'), (P['teal'], 'jar'), (P['brick'], 'can'), ('#7d8f9a', 'bag'), ('#6b4f9a', 'plug')]
    for i, (c, k) in enumerate(items):
        x = 38 + i * 106
        d.a(ell(x + 38, 438, 48, 9, P['ink'], 'opacity=".15"'))
        d.a(bin_shape(x, 230, 76, 205, c))
        cx, cy = x + 38, 330
        d.a(circ(cx, cy, 24, '#ffffff', 'opacity=".95"'))
        if k == 'apple':
            d.a(circ(cx - 5, cy + 2, 9, P['green']), circ(cx + 5, cy + 2, 9, P['green']), path(f'M{cx} {cy-8} q4 -8 9 -9', 'none', P['earth2'], 2.5))
        elif k == 'bottle':
            d.a(rect(cx - 6, cy - 14, 12, 28, P['warm'], 4), rect(cx - 3, cy - 18, 6, 6, P['ink'], 1))
        elif k == 'paper':
            d.a(rect(cx - 10, cy - 13, 20, 26, P['water'], 2), line(cx - 6, cy - 5, cx + 6, cy - 5, '#fff', 2), line(cx - 6, cy + 1, cx + 6, cy + 1, '#fff', 2))
        elif k == 'jar':
            d.a(rect(cx - 9, cy - 10, 18, 22, P['teal'], 4), rect(cx - 7, cy - 15, 14, 6, P['ink'], 2))
        elif k == 'can':
            d.a(rect(cx - 9, cy - 11, 18, 24, P['brick'], 3), ell(cx, cy - 11, 9, 3, '#e8a58f'))
        elif k == 'bag':
            d.a(path(f'M{cx-10} {cy+12} q-2 -18 4 -22 h12 q6 4 4 22Z', '#7d8f9a'), path(f'M{cx-4} {cy-10} q4 -8 8 0', 'none', P['ink'], 2.5))
        else:
            d.a(rect(cx - 8, cy - 4, 16, 14, '#6b4f9a', 3), line(cx - 4, cy - 4, cx - 4, cy - 12, '#6b4f9a', 3), line(cx + 4, cy - 4, cx + 4, cy - 12, '#6b4f9a', 3))
    d.a(person(765, 440, .9, P['water'], P['ink'], SKIN[2], '#a0642f', False, False, 'up', -1))
    return d.out()


def gal_vattenverk_inne():
    d = Doc(W, H, 'Illustration: hallen inne i ett vattenverk med stora blå rör, ventiler, en tank och en medarbetare som läser av en mätare.')
    d.d(lg('hall', '#dfe9ee', '#b9cdd6'))
    d.a(rect(0, 0, W, H, 'url(#hall)'))
    d.a(rect(0, 400, W, 100, '#8fa3ad'), rect(0, 392, W, 10, '#a7b8c0'))
    for i in range(5):
        d.a(rect(60 + i * 160, 40, 70, 120, P['water2'], 4, 'opacity=".5"'), rect(60 + i * 160, 40, 70, 120, 'none', 0, f'stroke="{P["grey"]}" stroke-width="4"'))
    d.a(rect(0, 200, W, 14, P['grey']))
    # tank
    d.a(rect(470, 190, 200, 210, P['grey2'], 6), ell(570, 190, 100, 20, '#e5eef2'), rect(470, 290, 200, 20, P['water'], 0, 'opacity=".85"'))
    for k in range(6):
        d.a(rect(480, 215 + k * 30, 16, 4, P['ink'], 2))
    d.a(circ(570, 345, 26, '#ffffff', f'stroke="{P["ink"]}" stroke-width="4"'), line(570, 345, 582, 332, P['warm2'], 3))
    # rör
    d.a(pipe([(0, 340), (300, 340), (300, 250), (470, 250)], P['water'], 28))
    d.a(pipe([(0, 300), (260, 300), (260, 120)], P['water2'], 18), pipe([(670, 360), (800, 360)], P['water'], 28))
    for (x, y) in [(300, 340), (140, 340), (260, 210), (730, 360)]:
        d.a(rect(x - 8, y - 38, 16, 22, P['grey']), circ(x, y - 42, 18, P['warm'], f'stroke="{P["warm2"]}" stroke-width="3"'), line(x - 12, y - 42, x + 12, y - 42, P['warm2'], 3))
    d.a(rect(60, 150, 70, 90, '#ffffff', 6, f'stroke="{P["grey"]}" stroke-width="3"'), circ(95, 190, 24, P['foam'], f'stroke="{P["ink"]}" stroke-width="3"'), line(95, 190, 106, 178, P['warm2'], 3))
    d.a(person(210, 450, 1.7, '#ffffff', P['ink'], SKIN[1], '#2a1c14', True, True, 'out'))
    return d.out()


def gal_provtagning():
    d = Doc(W, H, 'Illustration: en tekniker i vit rock vid en laboratoriebänk med flaskor och provrör med vatten. En vattendroppe syns på en skärm.')
    d.d(lg('lab', '#eaf4f8', '#cfe3ec'))
    d.a(rect(0, 0, W, H, 'url(#lab)'))
    d.a(rect(0, 360, W, 140, '#c3d3da'), rect(0, 340, W, 28, '#e3ecf0'), rect(0, 366, W, 6, P['grey']))
    d.a(rect(40, 60, 260, 150, P['ink'], 8), rect(52, 72, 236, 126, P['deep'], 4), drop(170, 150, 2.6, P['water2']), waves(80, 182, 180, 6, '#fff', .7, 3))
    d.a(rect(620, 90, 130, 14, P['grey']), rect(620, 140, 130, 14, P['grey']), rect(640, 90, 8, 150, P['grey']))
    for i in range(5):
        x = 440 + i * 50
        d.a(rect(x, 290, 24, 52, P['foam'], 6, f'stroke="{P["deep"]}" stroke-width="2.5"'), rect(x + 2, 312 - (i % 3) * 6, 20, 28 + (i % 3) * 6, P['water2'], 5))
    d.a(rect(430, 340, 250, 8, P['deep'], 3))
    d.a(path('M330 340 l16 -70 h30 l16 70Z', P['foam'], P['deep'], 3), path('M338 340 l11 -44 h24 l11 44Z', P['water']), rect(350, 252, 22, 18, P['grey'], 3))
    d.a(person(210, 470, 1.9, '#ffffff', P['ink'], SKIN[2], '#6b3f1d', False, False, 'out'))
    d.a(rect(240, 380, 18, 60, P['foam'], 6, f'stroke="{P["deep"]}" stroke-width="2.5"', ), rect(242, 400, 14, 40, P['water2'], 4))
    return d.out()


def gal_sopbil():
    d = Doc(W, H, 'Illustration: en sopbil på en villagata en solig dag. Två medarbetare i varselkläder tömmer kärl vid tomtgränsen.')
    sky(d)
    d.a(sun(120, 80), cloud(430, 70, 1.2), cloud(650, 110, .8))
    d.a(hills(W, 260, P['green3'], P['green2'], 30))
    d.a(villa(30, 320, 130, 74, '#f4e3c1', P['brick']), villa(590, 320, 130, 70, '#e5ecd0', P['water']), tree(180, 330, 1.2), tree(740, 340, 1.1, 'pine'))
    ground(d, 322)
    d.a(rect(0, 372, W, 128, P['grey']), line(0, 440, W, 440, '#fff', 3, 'stroke-dasharray="20 14" opacity=".7"'))
    d.a(sopbil(300, 450, 1.7))
    d.a(bin_shape(520, 350, 36, 56, P['green']), bin_shape(562, 350, 36, 56, '#7d8f9a'))
    d.a(person(470, 395, 1.1, P['warm'], P['ink'], SKIN[3], '#16100c', True, True, 'out', -1))
    d.a(person(180, 410, 1.1, P['warm'], P['deep'], SKIN[0], '#a0642f', True, True, 'down', 1))
    d.a(drop(690, 440, 1.1, P['water2']))
    return d.out()


def gal_miljohus():
    d = Doc(W, H, 'Illustration: några grannar vid ett miljöhus med flera kärl. En vuxen och ett barn sorterar förpackningar tillsammans medan en granne vinkar.')
    sky(d)
    d.a(cloud(100, 70, 1), cloud(600, 60, 1.1))
    d.a(block(60, 330, 120, 190), block(640, 330, 100, 150, '#e2d4b2'))
    ground(d, 330)
    d.a(rect(0, 330, W, 8, P['green']))
    d.a(rect(0, 400, W, 100, '#b7c6cd'))
    d.a(rect(260, 230, 280, 170, P['earth'], 4), poly([(246, 236), (400, 180), (554, 236)], P['ink']))
    d.a(rect(278, 290, 244, 110, '#3b2d24', 3))
    for i, c in enumerate([P['green'], P['warm'], P['water'], P['brick']]):
        d.a(bin_shape(286 + i * 60, 308, 52, 90, c))
    d.a(person(210, 450, 1.4, P['water'], P['ink'], SKIN[1], '#2a1c14', False, False, 'out'))
    d.a(person(255, 450, .8, P['warm'], P['deep'], SKIN[1], '#16100c', False, False, 'up'))
    d.a(person(600, 450, 1.4, P['green'], P['ink'], SKIN[3], '#16100c', False, False, 'up', -1))
    d.a(rect(222, 395, 22, 28, P['foam'], 4, f'stroke="{P["water"]}" stroke-width="2"'))
    d.a(dog(700, 460, 1.1, '#b07a4b', -1))
    return d.out()


def gal_sjopromenad():
    d = Doc(W, H, 'Illustration: en gångstig längs en sjö i mjukt ljus. Två personer promenerar med en hund, någon sitter på en bänk och barn leker vid vattenbrynet.')
    sky(d, gid='sk2', c1='#cfe9f5', c2='#fdf3dc')
    d.a(sun(600, 110, 30), cloud(130, 80, 1), cloud(330, 120, .7, .8))
    d.a(hills(W, 250, P['green3'], P['green2'], 40))
    d.d(lg('sj', P['water2'], P['water']))
    d.a(rect(0, 240, W, 110, 'url(#sj)'))
    d.a(waves(30, 270, 240, 5), waves(380, 300, 300, 6), waves(120, 330, 200, 4, op=.35))
    d.a(path('M0 345 C200 330, 500 350, 800 335 V500 H0Z', P['green2']))
    d.a(path('M0 410 C240 390, 520 420, 800 395 V450 C520 470, 240 445, 0 465Z', P['sand']))
    for x in [60, 150, 690, 760]:
        d.a(tree(x, 380, 1.5, 'round'))
    d.a(rect(340, 380, 80, 8, P['earth2'], 2), rect(346, 388, 6, 20, P['earth2']), rect(408, 388, 6, 20, P['earth2']), rect(340, 356, 80, 6, P['earth2'], 2))
    d.a(person(380, 382, 1.1, P['water'], P['ink'], SKIN[2], '#a0642f'))
    d.a(person(500, 450, 1.4, P['warm'], P['ink'], SKIN[1], '#2a1c14', False, False, 'down'))
    d.a(person(560, 450, 1.35, P['green'], P['deep'], SKIN[0], '#4a3426', False, False, 'out'))
    d.a(dog(610, 452, 1.0))
    d.a(person(230, 450, .75, P['warm2'], P['deep'], SKIN[3], '#16100c', False, False, 'up'))
    d.a(person(275, 450, .7, P['teal'], P['ink'], SKIN[0], '#a0642f', False, False, 'down'))
    return d.out()


# ======================= FÖREMÅL (120x120) =======================
def item_doc(title):
    d = Doc(120, 120, title)
    d.a(circ(60, 60, 56, '#ffffff', f'stroke="{P["grey2"]}" stroke-width="2"'))
    return d


def item_bananskal():
    d = item_doc('Illustration: ett bananskal.')
    d.a(path('M30 70 Q40 28 78 30 Q92 32 94 40 Q70 40 54 62 Q40 84 30 70Z', '#f6d34d'), path('M34 72 Q44 36 78 36', 'none', '#e0b323', 3),
        path('M78 30 q6 -8 12 -6 l4 14 q-10 -4 -16 -8Z', P['earth2']), path('M34 68 Q52 100 84 82 Q64 90 46 72Z', '#e6bf34'), path('M30 70 q-4 6 2 10 q6 -2 6 -8Z', P['earth2']))
    return d.out()


def item_schampoflaska():
    d = item_doc('Illustration: en tom plastflaska med pumplock, till exempel en schampoflaska.')
    d.a(rect(42, 36, 36, 62, P['teal'], 10), rect(52, 22, 16, 16, P['ink'], 3), rect(56, 14, 22, 8, P['ink'], 3), rect(46, 56, 28, 24, '#ffffff', 4, 'opacity=".85"'),
        path('M60 62 q6 8 0 14 q-6 -6 0 -14Z', P['water']))
    return d.out()


def item_mjolkkartong():
    d = item_doc('Illustration: en tom mjölkkartong med snedtak.')
    d.a(rect(38, 44, 44, 56, '#ffffff', 2, f'stroke="{P["water"]}" stroke-width="3"'), poly([(38, 44), (50, 24), (70, 24), (82, 44)], P['water']),
        rect(38, 62, 44, 20, P['water'], 0), path('M60 66 q6 8 0 14 q-6 -6 0 -14Z', '#ffffff'))
    return d.out()


def item_syltburk():
    d = item_doc('Illustration: en glasburk med rött lock, till exempel en syltburk.')
    d.a(rect(36, 38, 48, 62, '#dff1fa', 10, f'stroke="{P["water"]}" stroke-width="3"'), rect(36, 60, 48, 40, '#c4426a', 10, 'opacity=".85"'),
        rect(40, 24, 40, 16, P['brick'], 4), rect(44, 70, 32, 18, '#ffffff', 3), path('M56 76 h8 M56 82 h14', 'none', P['grey'], 2), path('M42 46 v16', 'none', '#ffffff', 3, 'opacity=".8"'))
    return d.out()


def item_konservburk():
    d = item_doc('Illustration: en tom konservburk av metall.')
    d.a(rect(38, 36, 44, 62, P['grey2'], 4), ell(60, 36, 22, 6, '#e7eef1'), ell(60, 98, 22, 6, P['grey']), rect(38, 52, 44, 30, P['brick'], 0),
        path('M44 52 v30 M76 52 v30', 'none', '#ffffff', 2, 'opacity=".4"'), circ(60, 67, 8, '#ffffff', 'opacity=".9"'))
    return d.out()


def item_bloja():
    d = item_doc('Illustration: en använd blöja.')
    d.a(path('M24 44 H96 V58 Q96 94 60 96 Q24 94 24 58Z', '#f4f7f9', P['grey'], 3), rect(24, 40, 18, 12, P['water2'], 3), rect(78, 40, 18, 12, P['water2'], 3),
        path('M44 70 q16 12 32 0', 'none', P['water2'], 3), circ(60, 62, 4, P['warm']))
    return d.out()


def item_batteri():
    d = item_doc('Illustration: ett cylinderformat batteri med plustecken.')
    d.a(rect(52, 22, 16, 8, P['grey'], 2), rect(44, 28, 32, 72, P['ink'], 6), rect(44, 28, 32, 22, P['warm'], 6), rect(44, 40, 32, 10, P['warm']),
        path('M60 36 v14 M53 43 h14', 'none', '#ffffff', 3), path('M52 84 h16', 'none', P['grey2'], 3))
    return d.out()


def item_laddare():
    d = item_doc('Illustration: en trasig mobilladdare med sladd och kontakt.')
    d.a(rect(34, 40, 36, 36, '#f4f7f9', 6, f'stroke="{P["grey"]}" stroke-width="3"'), rect(40, 28, 5, 14, P['grey']), rect(58, 28, 5, 14, P['grey']),
        path('M52 76 Q52 100 84 94', 'none', P['ink'], 4), rect(82, 84, 18, 20, P['ink'], 4), path('M44 56 l6 -8 l-2 8 l8 0 l-6 8 l2 -8Z', P['warm']))
    return d.out()


ITEMS = {
    'bananskal': item_bananskal, 'schampoflaska': item_schampoflaska, 'mjolkkartong': item_mjolkkartong,
    'syltburk': item_syltburk, 'konservburk': item_konservburk, 'bloja': item_bloja,
    'batteri': item_batteri, 'laddare': item_laddare,
}

BINS = [
    ('mat', 'Matavfall', P['green']), ('plast', 'Plastförpackningar', P['warm2']),
    ('papper', 'Pappers- och kartongförpackningar', P['water']), ('glas', 'Glasförpackningar', P['teal']),
    ('metall', 'Metallförpackningar', P['brick']), ('rest', 'Restavfall', '#7d8f9a'), ('el', 'Elavfall och batterier', '#6b4f9a'),
]


def bin_svg(id, label, color):
    d = Doc(100, 120, f'Illustration: ett sorteringskärl för {label.lower()}.')
    d.a(ell(50, 112, 38, 6, P['ink'], 'opacity=".15"'), bin_shape(14, 12, 72, 98, color))
    d.a(circ(50, 66, 17, '#ffffff', 'opacity=".92"'), path('M50 56 q9 11 0 20 q-9 -9 0 -20Z', color))
    return d.out()


# ======================= KARTA =======================
def karta():
    d = Doc(800, 560, 'Förenklad kartillustration av ett kustnära område med vik, vägar, parker och tre markerade platser. Inga verkliga gatunamn visas.')
    d.d(lg('hav', '#b8def2', '#8ec9e8'))
    d.a(rect(0, 0, 800, 560, 'url(#hav)'))
    land = 'M-10 120 C60 80 150 110 230 90 C330 60 420 100 520 80 C620 60 720 90 810 70 V570 H-10Z'
    d.a(path(land, '#f1ead6'))
    d.a(path('M300 560 C310 470 360 430 400 380 C430 340 420 300 470 280 C520 262 560 300 600 270 C650 232 700 250 810 230 V570 H300Z', '#bfe0f0'))
    d.a(path('M300 560 C310 470 360 430 400 380 C430 340 420 300 470 280 C520 262 560 300 600 270 C650 232 700 250 810 230', 'none', '#ffffff', 4, 'opacity=".7"'))
    d.a(path('M40 170 C120 150 190 190 260 170 C300 160 330 200 300 240 C260 290 150 280 80 260 C30 245 10 200 40 170Z', P['green3']))
    d.a(path('M500 140 C570 120 650 140 700 175 C740 210 700 250 640 240 C560 230 470 190 500 140Z', P['green3']))
    d.a(path('M90 330 C150 310 230 340 270 390 C250 440 160 450 100 420 C60 395 50 350 90 330Z', P['green3']))
    d.a(path('M-10 150 C60 110 150 140 230 120 C330 90 420 130 520 110', 'none', '#e5dcc0', 3))
    roads = ['M0 300 C150 280 250 330 400 300 S 650 330 800 300', 'M120 100 C140 200 130 300 170 420 S 190 520 200 570',
             'M420 70 C430 150 380 220 400 300', 'M640 80 C620 160 660 230 640 330', 'M250 230 C340 250 440 220 560 250 S 720 230 800 250']
    for r in roads:
        d.a(path(r, 'none', '#ffffff', 11), path(r, 'none', '#d4cab0', 2.5))
    d.a(path('M0 440 C100 460 180 450 250 500', 'none', '#ffffff', 9), path('M0 440 C100 460 180 450 250 500', 'none', '#d4cab0', 2))
    for x, y in [(330, 360), (380, 330), (150, 230), (590, 330), (520, 200), (220, 140)]:
        d.a(rect(x, y, 18, 12, '#e2d1ad', 2), rect(x + 24, y + 6, 16, 12, '#e2d1ad', 2))
    d.a(text(660, 520, 'Förenklad bild, inte skalenlig', 15, P['ink'], 'middle', 600, 'opacity=".6"'))
    return d.out()
