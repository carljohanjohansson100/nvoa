"""Gemensamma byggstenar för konceptdemons illustrationer (ren SVG, egen palett)."""
import math

P = dict(
    ink='#12303f', deep='#0b3c5d', water='#2a7fb8', water2='#7cc4e8', foam='#dff1fa',
    sky1='#bfe3f5', sky2='#eef9fd', green='#2f7d4f', green2='#5aa469', green3='#a6d39a',
    sand='#f4ead2', earth='#8d6e4f', earth2='#6e5440', warm='#f2a03d', warm2='#d9662f',
    white='#ffffff', grey='#93a8b3', grey2='#cbd8de', brick='#c4694a', waste='#8b8a5c',
    teal='#3aa6a0', paper='#f7f3e8',
)
SKIN = ['#e9b78f', '#c98f66', '#f1cfae', '#8d5a3b']


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


class Doc:
    def __init__(self, w, h, title):
        self.w, self.h, self.title = w, h, title
        self.defs, self.body = [], []

    def d(self, *x):
        self.defs.extend(x)

    def a(self, *x):
        self.body.extend(x)

    def out(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" '
                f'aria-label="{esc(self.title)}"><title>{esc(self.title)}</title>'
                f'<defs>{"".join(self.defs)}</defs>{"".join(self.body)}</svg>\n')


def lg(id, c1, c2, x1=0, y1=0, x2=0, y2=1):
    return (f'<linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')


def rect(x, y, w, h, fill, r=0, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" {extra}/>'


def circ(x, y, r, fill, extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {extra}/>'


def ell(x, y, rx, ry, fill, extra=''):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" {extra}/>'


def path(d, fill='none', stroke=None, sw=0, extra=''):
    s = f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else ''
    return f'<path d="{d}" fill="{fill}"{s} {extra}/>'


def line(x1, y1, x2, y2, stroke, sw=2, extra=''):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linecap="round" {extra}/>')


def poly(pts, fill='none', stroke=None, sw=0, extra=''):
    p = ' '.join(f'{x},{y}' for x, y in pts)
    s = f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else ''
    return f'<polyline points="{p}" fill="{fill}"{s} {extra}/>' if fill == 'none' else \
        f'<polygon points="{p}" fill="{fill}"{s} {extra}/>'


def g(inner, tf=None, extra=''):
    t = f' transform="{tf}"' if tf else ''
    return f'<g{t} {extra}>{inner}</g>'


def text(x, y, s, size=14, fill=None, anchor='middle', weight=600, extra=''):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill or P["ink"]}" '
            f'text-anchor="{anchor}" font-family="system-ui,Segoe UI,Roboto,sans-serif" {extra}>{esc(s)}</text>')


# ---------- natur ----------
def tree(x, y, s=1, kind='round', c=None):
    if kind == 'pine':
        c = c or P['green']
        inner = (rect(-3, -12, 6, 12, P['earth2']) + path('M0 -80 L15 -52 L-15 -52Z', c) +
                 path('M0 -64 L19 -32 L-19 -32Z', c) + path('M0 -44 L23 -8 L-23 -8Z', c))
    else:
        c = c or P['green2']
        inner = (rect(-3, -28, 6, 28, P['earth2']) + circ(0, -48, 22, c) + circ(-13, -36, 14, c) +
                 circ(13, -36, 14, c) + circ(-6, -54, 10, P['green3'], 'opacity=".55"'))
    return g(inner, f'translate({x} {y}) scale({s})')


def cloud(x, y, s=1, op=1, c='#ffffff'):
    inner = circ(0, 0, 18, c) + circ(22, -8, 24, c) + circ(48, 0, 18, c) + rect(0, 0, 48, 18, c)
    return g(inner, f'translate({x} {y}) scale({s})', f'opacity="{op}"')


def sun(x, y, r=26):
    return circ(x, y, r * 1.5, P['warm'], 'opacity=".22"') + circ(x, y, r, '#ffc766')


def hills(w, base, c1, c2, amp=60):
    return (path(f'M0 {base} C {w*.15} {base-amp}, {w*.3} {base-amp*.4}, {w*.45} {base-amp*.8} '
                f'S {w*.78} {base-amp*1.1}, {w} {base-amp*.5} V{base+120} H0Z', c1) +
            path(f'M0 {base+20} C {w*.2} {base-amp*.3}, {w*.4} {base+10}, {w*.6} {base-amp*.2} '
                 f'S {w*.9} {base-amp*.1}, {w} {base+10} V{base+140} H0Z', c2))


def sky(d, w=None, h=None, gid='sk', c1=None, c2=None):
    d.d(lg(gid, c1 or P['sky1'], c2 or P['sky2']))
    d.a(rect(0, 0, w or d.w, h or d.h, f'url(#{gid})'))


def waves(x, y, w, n, c='#ffffff', op=.5, amp=4):
    step = w / n
    dd = f'M{x} {y}' + ''.join(f' q{step/4:.1f} {-amp} {step/2:.1f} 0 t{step/2:.1f} 0' for _ in range(n))
    return path(dd, 'none', c, 2.5, f'opacity="{op}"')


# ---------- människor ----------
def person(x, y, sc=1, shirt=None, pants=None, skin=None, hair=None, helmet=False, vest=False,
           arm='down', facing=1, hat=None):
    shirt = shirt or P['water']
    pants = pants or P['ink']
    skin = skin or SKIN[0]
    hair = hair or '#4a3426'
    s = rect(-9, -28, 8, 28, pants, 3) + rect(1, -28, 8, 28, pants, 3)
    s += rect(-11, -4, 11, 5, P['ink'], 2) + rect(0, -4, 11, 5, P['ink'], 2)
    s += rect(-17, -57, 7, 26, shirt, 3.5)
    if arm == 'up':
        s += g(rect(10, -57, 7, 26, shirt, 3.5), 'rotate(155 13 -54)')
    elif arm == 'out':
        s += g(rect(10, -57, 7, 26, shirt, 3.5), 'rotate(100 13 -54)')
    else:
        s += rect(10, -57, 7, 26, shirt, 3.5)
    s += rect(-12, -59, 24, 33, shirt, 7)
    if vest:
        s += rect(-12, -59, 24, 33, P['warm'], 7) + rect(-12, -48, 24, 3, '#ffffff') + rect(-12, -37, 24, 3, '#ffffff')
    s += rect(-3, -64, 6, 7, skin) + circ(0, -69, 9.5, skin)
    s += path('M-9.5 -70 A9.5 9.5 0 0 1 9.5 -70 Q0 -74 -9.5 -70Z', hair)
    if helmet:
        s += path('M-11.5 -71 A11.5 11.5 0 0 1 11.5 -71Z', P['warm']) + rect(-12.5, -72, 25, 3.5, P['warm2'], 1.5)
    if hat:
        s += path('M-11 -72 Q0 -86 11 -72Z', hat) + rect(-12, -73, 24, 3, hat)
    return g(s, f'translate({x} {y}) scale({sc * facing} {sc})')


def dog(x, y, sc=1, c='#b07a4b', facing=1):
    s = (rect(-16, -20, 30, 14, c, 6) + rect(-14, -8, 5, 10, c, 2) + rect(6, -8, 5, 10, c, 2) +
         circ(18, -22, 8, c) + path('M22 -30 l6 -4 l-1 9Z', P['earth2']) + path('M-16 -16 q-8 -6 -10 -14', 'none', c, 4))
    return g(s, f'translate({x} {y}) scale({sc * facing} {sc})')


# ---------- byggnader ----------
def villa(x, y, w=110, h=70, wall='#f4e3c1', roof=None, door='#8a5a3c', lit=False):
    roof = roof or P['brick']
    win = '#ffe9a8' if lit else P['water2']
    s = rect(x, y - h, w, h, wall, 2)
    s += poly([(x - 8, y - h + 2), (x + w / 2, y - h - 42), (x + w + 8, y - h + 2)], roof)
    s += rect(x + w * .70, y - h - 38, 12, 22, P['earth2'])
    s += rect(x + w * .12, y - 36, 18, 36, door, 2)
    s += rect(x + w * .42, y - h + 18, 22, 22, win, 2, f'stroke="{P["ink"]}" stroke-width="2"')
    s += rect(x + w * .70, y - h + 18, 22, 22, win, 2, f'stroke="{P["ink"]}" stroke-width="2"')
    return s


def block(x, y, w=90, h=120, wall='#e8d8b8'):
    s = rect(x, y - h, w, h, wall, 2) + rect(x - 4, y - h - 6, w + 8, 8, P['grey'], 2)
    for r in range(int(h // 30)):
        for c in range(3):
            s += rect(x + 10 + c * (w - 20) / 3, y - h + 14 + r * 28, 16, 16, P['water2'], 2)
    return s


def bin_shape(x, y, w, h, color, lid=None):
    lid = lid or P['ink']
    s = path(f'M{x+3} {y+h*.15} H{x+w-3} L{x+w-7} {y+h} H{x+7}Z', color)
    s += path(f'M{x+w*.3} {y+h*.25} V{y+h*.9} M{x+w*.5} {y+h*.25} V{y+h*.9} M{x+w*.7} {y+h*.25} V{y+h*.9}',
              'none', '#ffffff', 2, 'opacity=".3"')
    s += rect(x - 2, y, w + 4, h * .16, lid, 3)
    return s


def pipe(pts, color=None, w=10, outline=True):
    color = color or P['water']
    s = ''
    if outline:
        s += poly(pts, 'none', P['deep'], w + 4)
    s += poly(pts, 'none', color, w)
    return s


def cone(x, y, s=1):
    return g(poly([(-9, 0), (9, 0), (3, -26), (-3, -26)], P['warm2']) +
             rect(-4, -18, 8, 4, '#ffffff') + rect(-12, -2, 24, 4, P['ink'], 2), f'translate({x} {y}) scale({s})')


def car(x, y, s=1, color=None, facing=1):
    color = color or P['water']
    inner = (rect(-48, -26, 96, 22, color, 8) + path('M-28 -26 L-18 -46 H20 L34 -26Z', color) +
             path('M-22 -28 L-14 -42 H-2 V-28Z M2 -28 V-42 H16 L26 -28Z', P['foam']) +
             circ(-26, -4, 10, P['ink']) + circ(26, -4, 10, P['ink']) + circ(-26, -4, 4, P['grey2']) + circ(26, -4, 4, P['grey2']))
    return g(inner, f'translate({x} {y}) scale({s*facing} {s})')


def van(x, y, s=1, facing=1):
    inner = (rect(-60, -62, 92, 52, '#ffffff', 6, f'stroke="{P["grey"]}" stroke-width="2"') +
             path('M32 -62 H52 Q62 -62 66 -44 L68 -10 H32Z', '#ffffff', P['grey'], 2) +
             path('M38 -56 H52 Q58 -56 61 -44 H38Z', P['water2']) + rect(-60, -34, 92, 8, P['water'], 0) +
             circ(-34, -8, 12, P['ink']) + circ(46, -8, 12, P['ink']) + circ(-34, -8, 5, P['grey2']) + circ(46, -8, 5, P['grey2']) +
             circ(-14, -48, 8, P['water2']) + path('M-14 -53 q4 5 0 10 q-4 -5 0 -10Z', P['deep']))
    return g(inner, f'translate({x} {y}) scale({s*facing} {s})')


def sopbil(x, y, s=1, facing=1):
    inner = (rect(-80, -72, 104, 56, P['green'], 8) + path('M24 -72 H52 Q62 -72 66 -50 L68 -16 H24Z', P['green'], '#1f5a38', 2) +
             path('M32 -66 H50 Q56 -66 60 -50 H32Z', P['water2']) + rect(-80, -44, 104, 6, P['green2']) +
             rect(-86, -76, 14, 60, P['grey'], 4) + circ(-52, -14, 13, P['ink']) + circ(46, -14, 13, P['ink']) +
             circ(-52, -14, 5, P['grey2']) + circ(46, -14, 5, P['grey2']) +
             path('M-50 -56 a8 8 0 1 0 16 0', 'none', '#ffffff', 3) + path('M-34 -56 l-5 -5 m5 5 l5 -5', 'none', '#ffffff', 3))
    return g(inner, f'translate({x} {y}) scale({s*facing} {s})')


def drop(x, y, s=1, c=None):
    c = c or P['water']
    return g(path('M0 -22 C10 -8 14 -2 14 6 A14 14 0 0 1 -14 6 C-14 -2 -10 -8 0 -22Z', c), f'translate({x} {y}) scale({s})')
