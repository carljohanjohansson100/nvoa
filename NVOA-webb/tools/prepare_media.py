#!/usr/bin/env python3
"""Förbereder webbmedia för NVOA-webb. Endast Python 3 (standardbibliotek) + ffmpeg/ffprobe.

Källmappen öppnas bara för läsning. Inget skickas någonstans.

  python tools/prepare_media.py --inventory     # steg 1: lista material, ändrar inget
  python tools/prepare_media.py                 # steg 2: skapar media/ och content/manifest.js
  python tools/prepare_media.py --source "C:\\...\\NVOA"

Standard för --source är systermappen ..\\NVOA (NVOA-webb ligger bredvid NVOA).
Redan gjorda filer hoppas över (--force för omkörning). Dina redigerade texter i
content/manifest.js bevaras vid omkörning.
"""
import argparse, hashlib, json, re, shutil, subprocess, sys, unicodedata
from pathlib import Path

IMG = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tif', '.tiff'}
VID = {'.mp4', '.mov', '.m4v', '.mkv', '.avi', '.wmv', '.webm', '.mts', '.m2ts'}
DOC = {'.txt', '.md', '.doc', '.docx', '.pdf', '.pptx', '.ppt', '.xlsx', '.rtf'}
BRAND_HINT = re.compile(r'logo|logotyp|grafisk|profil|brand|font|typsnitt|färg|farg', re.I)
# Windows-attribut: OFFLINE, RECALL_ON_OPEN, RECALL_ON_DATA_ACCESS (OneDrive-platshållare)
PLACEHOLDER_ATTRS = 0x1000 | 0x40000 | 0x400000

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'content' / 'manifest.js'
PREFIX = 'window.NVOA_CONTENT = '


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')


def need_tool(name):
    if not shutil.which(name):
        sys.exit(f'{name} hittades inte i PATH. Installera ffmpeg (inkl. ffprobe) och försök igen. Inget har installerats åt dig.')


def probe(path):
    r = run(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_format', '-show_streams', str(path)])
    try:
        j = json.loads(r.stdout)
    except Exception:
        return None
    v = next((s for s in j.get('streams', []) if s.get('codec_type') == 'video'), None)
    if not v:
        return None
    w, h = int(v.get('width', 0)), int(v.get('height', 0))
    rot = 0
    for sd in v.get('side_data_list', []) or []:
        if 'rotation' in sd:
            rot = abs(int(sd['rotation']))
    if str(v.get('tags', {}).get('rotate', '')).lstrip('-') in ('90', '270'):
        rot = 90
    if rot in (90, 270):
        w, h = h, w
    dur = float(j.get('format', {}).get('duration') or v.get('duration') or 0)
    return {'w': w, 'h': h, 'duration': round(dur, 1), 'codec': v.get('codec_name')}


def slug(rel):
    s = unicodedata.normalize('NFKD', rel.with_suffix('').as_posix()).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()[:50]
    return f'{s}-{hashlib.sha1(rel.as_posix().encode()).hexdigest()[:6]}'


def fmt_size(n):
    for u in ('B', 'KB', 'MB', 'GB'):
        if n < 1024 or u == 'GB':
            return f'{n:.0f} {u}' if u == 'B' else f'{n:.1f} {u}'
        n /= 1024


def scan(src):
    files = []
    for p in sorted(src.rglob('*')):
        if not p.is_file():
            continue
        st = p.stat()
        attrs = getattr(st, 'st_file_attributes', 0)
        ext = p.suffix.lower()
        kind = 'bild' if ext in IMG else 'video' if ext in VID else 'dokument' if ext in DOC else 'annat'
        files.append({'path': p, 'rel': p.relative_to(src), 'size': st.st_size, 'kind': kind,
                      'placeholder': st.st_size == 0 or bool(attrs & PLACEHOLDER_ATTRS)})
    return files


def inventory(files):
    ph = [f for f in files if f['placeholder']]
    print(f'\n{len(files)} filer, {fmt_size(sum(f["size"] for f in files))}')
    for f in files:
        info = ''
        if f['kind'] in ('bild', 'video') and not f['placeholder']:
            m = probe(f['path'])
            f['meta'] = m
            if m:
                info = f'{m["w"]}x{m["h"]}' + (f' {m["duration"]}s' if f['kind'] == 'video' else '')
            else:
                info = 'KAN INTE LÄSAS'
        flag = ' [PLATSHÅLLARE]' if f['placeholder'] else ''
        brand = ' [BRAND?]' if BRAND_HINT.search(f['rel'].name) else ''
        print(f'{f["kind"]:9} {fmt_size(f["size"]):>10}  {info:16} {f["rel"]}{flag}{brand}')
    if ph:
        print(f'\nSTOPP: {len(ph)} fil(er) verkar vara OneDrive online-only (0 byte eller offline-attribut).')
        print('Högerklicka mappen i Utforskaren > "Behåll alltid på den här enheten", vänta, och kör om.')
        print('Inget har lästs eller laddats ned från dessa filer.')
        return False
    return True


def ff(args):
    r = run(['ffmpeg', '-y', '-v', 'error', '-nostdin'] + args)
    return r.returncode == 0, r.stderr.strip()


def long_edge(n):
    return f"scale=w='if(gt(iw,ih),min({n},iw),-2)':h='if(gt(iw,ih),-2,min({n},ih))'"


def make_image(src, out_dir, id_):
    big_w, big_j, th = out_dir / f'{id_}.webp', out_dir / f'{id_}.jpg', out_dir / f'{id_}-thumb.webp'
    for dst, extra, edge in ((big_w, ['-c:v', 'libwebp', '-quality', '82'], 2000),
                             (big_j, ['-c:v', 'mjpeg', '-q:v', '3', '-pix_fmt', 'yuvj420p'], 2000),
                             (th, ['-c:v', 'libwebp', '-quality', '75'], 600)):
        if dst.exists() and dst.stat().st_size:
            continue
        ok, err = ff(['-i', str(src), '-map_metadata', '-1', '-frames:v', '1', '-vf', long_edge(edge)] + extra + [str(dst)])
        if not ok:
            return None, err
    m = probe(big_w) or {}
    return {'src': f'media/img/{id_}.webp', 'fallback': f'media/img/{id_}.jpg',
            'thumb': f'media/img/{id_}-thumb.webp', 'w': m.get('w'), 'h': m.get('h')}, None


def make_video(src, out_dir, id_, dur):
    mp4, poster, th = out_dir / f'{id_}.mp4', out_dir / f'{id_}-poster.webp', out_dir / f'{id_}-thumb.webp'
    if not (mp4.exists() and mp4.stat().st_size):
        vf = 'scale=w=1920:h=1080:force_original_aspect_ratio=decrease:force_divisible_by=2,format=yuv420p'
        ok, err = ff(['-i', str(src), '-map_metadata', '-1', '-vf', vf, '-c:v', 'libx264', '-crf', '24', '-preset', 'medium',
                      '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', str(mp4)])
        if not ok:
            mp4.unlink(missing_ok=True)
            return None, err
    t = str(min(2.0, dur / 2))
    for dst, edge in ((poster, 1600), (th, 600)):
        if not (dst.exists() and dst.stat().st_size):
            ok, err = ff(['-ss', t, '-i', str(mp4), '-frames:v', '1', '-vf', long_edge(edge), '-c:v', 'libwebp', '-quality', '78', str(dst)])
            if not ok:
                return None, err
    m = probe(mp4) or {}
    return {'video': f'media/video/{id_}.mp4', 'poster': f'media/video/{id_}-poster.webp',
            'thumb': f'media/video/{id_}-thumb.webp', 'w': m.get('w'), 'h': m.get('h'),
            'duration': m.get('duration', dur)}, None


def load_manifest():
    if MANIFEST.exists():
        t = MANIFEST.read_text(encoding='utf-8').strip()
        if t.startswith(PREFIX):
            return json.loads(t[len(PREFIX):].rstrip(';\n '))
    return {}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--source', default=str(ROOT.parent / 'NVOA'))
    ap.add_argument('--inventory', action='store_true')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    src = Path(a.source)
    if not src.is_dir():
        sys.exit(f'Källmappen finns inte: {src}')
    need_tool('ffmpeg'); need_tool('ffprobe')
    print(run(['ffmpeg', '-version']).stdout.splitlines()[0])
    print(f'Källa (skrivskyddad): {src}')
    files = scan(src)
    ok = inventory(files)
    if a.inventory or not ok:
        sys.exit(0 if ok else 2)

    old = load_manifest()
    old_items = {i['id']: i for i in old.get('items', [])}
    themes = {t['id']: t for t in old.get('themes', [])}
    items, skipped = [], []
    (ROOT / 'media' / 'img').mkdir(parents=True, exist_ok=True)
    (ROOT / 'media' / 'video').mkdir(parents=True, exist_ok=True)
    media = [f for f in files if f['kind'] in ('bild', 'video')]
    for n, f in enumerate(media, 1):
        rel = f['rel']
        id_ = slug(rel)
        m = f.get('meta') or probe(f['path'])
        print(f'[{n}/{len(media)}] {rel}')
        if not m:
            skipped.append((str(rel), 'kunde inte läsas av ffprobe (t.ex. HEIC?)')); continue
        if f['kind'] == 'bild':
            res, err = make_image(f['path'], ROOT / 'media' / 'img', id_)
        else:
            res, err = make_video(f['path'], ROOT / 'media' / 'video', id_, m['duration'])
        if not res:
            skipped.append((str(rel), err[:200])); continue
        theme = re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', rel.parts[0].lower()).encode('ascii', 'ignore').decode()).strip('-') if len(rel.parts) > 1 else 'ovrigt'
        theme = theme or 'ovrigt'
        if theme not in themes:
            themes[theme] = {'id': theme, 'title': (rel.parts[0] if len(rel.parts) > 1 else 'Övrigt'),
                             'text': 'TODO: kort introtext för temat'}
        item = {'id': id_, 'type': 'image' if f['kind'] == 'bild' else 'video', 'theme': theme,
                'caption': 'TODO: bildtext', 'hero': False, 'hidden': False, 'source': rel.as_posix()}
        item.update(res)
        prev = old_items.get(id_)
        if prev:  # bevara redaktörens texter och val
            for k in ('theme', 'caption', 'hero', 'hidden', 'order'):
                if k in prev:
                    item[k] = prev[k]
        items.append(item)

    manifest = {
        'site': old.get('site') or {
            'title': 'Nacka Vatten och Avfall',
            'subtitle': 'TODO: underrubrik',
            'intro': 'TODO: kort inledning till visningen',
            'footer': 'Internt demomaterial. Endast för NVOA:s personal.'},
        'themes': list(themes.values()),
        'items': items}
    MANIFEST.write_text(PREFIX + json.dumps(manifest, ensure_ascii=False, indent=2) + ';\n', encoding='utf-8')
    total = sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())
    todo = sum(1 for i in items if str(i['caption']).startswith('TODO'))
    print(f'\nKlart: {len(items)} objekt, {len(skipped)} hoppade över, {todo} bildtexter med TODO.')
    print(f'Total storlek NVOA-webb: {fmt_size(total)}')
    for r, why in skipped:
        print(f'  HOPPADE ÖVER: {r}: {why}')
    print('Redigera texter i content/manifest.js. Öppna index.html.')


if __name__ == '__main__':
    main()
