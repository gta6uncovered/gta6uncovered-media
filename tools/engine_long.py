# GTA6 Uncovered long-form engine (1920x1080). Usage: python3 -I engine_long.py <video_dir> voice|preview|full|thumb
# <video_dir>/script.py defines NAME, BEATS = [(narration, visual), ...] and optional SPEED.
# Visual kinds: clip (f, s) | card (bg=(f,s), els=[...], src, est) | chapter (n, title, bg)
# Card elements (t=): title, sub, counter, formula, bars, table, chips, map, stats, rule, assume, note, range
import sys, os, json, math, subprocess, importlib.util, hashlib
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(sys.argv[1]); MODE = sys.argv[2]
spec = importlib.util.spec_from_file_location('script', OUT + '/script.py'); sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
BEATS = sc.BEATS
def vfn(txt): return f"{OUT}/vo_{hashlib.md5(txt.encode()).hexdigest()[:10]}.wav"
SPEED = getattr(sc, 'SPEED', 1.08); SEED = getattr(sc, 'SEED', 7)
FOOT = os.environ.get('FOOT', '/home/claude/footage')
AB, I4, I6 = S + '/fonts/ab.ttf', S + '/fonts/i4.ttf', S + '/fonts/i6.ttf'
W, H, FPS = 1920, 1080, 30
AC = (255, 90, 60); WH = (255, 255, 255); YEL = (255, 214, 64); BLK = (0, 0, 0); RED = (235, 50, 50); GRN = (60, 210, 120); GRY = (200, 200, 210)
COL = dict(w=WH, y=YEL, r=RED, g=GRN, a=AC, gr=GRY)
def C(c): return COL.get(c, c) if isinstance(c, str) else c
FONTS = {}
def F(p, s):
    s = max(1, int(s))
    if (p, s) not in FONTS: FONTS[(p, s)] = ImageFont.truetype(p, s)
    return FONTS[(p, s)]
def clamp(t): return max(0.0, min(1.0, t))
def ease(t): t = clamp(t); return 1 - (1 - t) ** 3
def back(t):
    t = clamp(t); c = 1.7
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2

# ---------------- voice ----------------
if MODE == 'voice':
    from kokoro_onnx import Kokoro
    kk = os.environ.get('KK', '/tmp/kk')
    k = Kokoro(kk + '/kokoro-v1.0.onnx', kk + '/voices-v1.0.bin'); dur = {}
    for i, (txt, v) in enumerate(BEATS):
        fn = vfn(txt)
        if not os.path.exists(fn):
            a, sr = k.create(txt, voice='am_fenrir', speed=SPEED, lang='en-us'); sf.write(fn, a, sr)
        a, sr = sf.read(fn); dur[i] = len(a) / sr
    json.dump(dur, open(OUT + '/vo_durations.json', 'w')); print('total voice', round(sum(dur.values()), 1)); sys.exit()

DUR = {int(k): v for k, v in json.load(open(OUT + '/vo_durations.json')).items()}
SEGS, t = [], 0.0
for i, (txt, v) in enumerate(BEATS):
    lead = 0.6 if v['kind'] == 'chapter' else 0.0
    tail = 0.9 if v['kind'] == 'chapter' else 0.35
    d = DUR[i]; SEGS.append(dict(i=i, text=txt, v=v, t0=t, vs=t + lead, vo=d, t1=t + lead + d + tail)); t = SEGS[-1]['t1']
TOTAL = t + 0.6; SEGS[-1]['t1'] = TOTAL

def chapters():
    out = []
    for s in SEGS:
        if s['v']['kind'] == 'chapter':
            m, sec = divmod(int(s['t0']), 60); out.append(f"{m}:{sec:02d} {s['v']['title'].title()}")
    return ['0:00 Intro'] + out

# ---------------- footage ----------------
def grab(f, start, n, w=W, h=H):
    vf = ('crop=1920:816:0:132,' if f == 't2' else '') + f'fps={FPS},scale={w}:{h}:flags=lanczos:force_original_aspect_ratio=increase,crop={w}:{h},eq=contrast=1.06:saturation=1.15'
    cmd = ['ffmpeg', '-loglevel', 'error', '-ss', str(start), '-i', f'{FOOT}/{f}.mp4', '-frames:v', str(n), '-an', '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout; k = len(raw) // (w * h * 3)
    return [Image.frombuffer('RGB', (w, h), raw[i * w * h * 3:(i + 1) * w * h * 3]) for i in range(k)]
BGC = {}
def bg_still(f, s):
    if (f, s) not in BGC:
        im = grab(f, s, 1, 1152, 648)[0].filter(ImageFilter.GaussianBlur(14)).resize((W + 96, H + 54), Image.BILINEAR)
        BGC[(f, s)] = Image.blend(im, Image.new('RGB', im.size, (10, 10, 18)), 0.62)
    return BGC[(f, s)]

# ---------------- drawing ----------------
def tx(d, xy, s, f, fill, sw=6, anchor='mm'): d.text(xy, s, font=f, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=BLK)
def fit(d, s, size, maxw=1700, font=AB):
    while size > 20 and d.textlength(s, font=F(font, size)) > maxw: size -= 2
    return size
def fmtv(v, fm):
    if fm == 'd1': return f'{v:,.1f}'
    if fm == 'd2': return f'{v:,.2f}'
    return f'{int(round(v)):,}'

def draw_el(d, e, lt):
    ty = e['t']; lt = lt - e.get('delay', 0)
    if lt < 0: return
    y = e.get('y', 500); cx = W // 2
    if ty == 'title':
        sz = fit(d, e['s'], e.get('size', 120)); tx(d, (cx, y), e['s'], F(AB, sz * back(lt / 0.35)), C(e.get('col', 'w')), 8)
    elif ty == 'sub':
        g = ease(lt / 0.4); f = F(I6, fit(d, e['s'], e.get('size', 54), font=I6))
        tx(d, (cx, y + 30 * (1 - g)), e['s'], f, (235, 235, 240), 4)
    elif ty == 'note':
        g = ease(lt / 0.4); f = F(I4, 36); w = d.textlength(e['s'], font=f)
        d.rounded_rectangle([cx - w / 2 - 30, y - 34, cx + w / 2 + 30, y + 34], 16, fill=(40, 40, 50), outline=YEL, width=3)
        d.text((cx, y), e['s'], font=f, fill=YEL, anchor='mm')
    elif ty == 'counter':
        g = ease(lt / e.get('dur', 1.6)); v = e.get('frm', 0) + (e['to'] - e.get('frm', 0)) * g
        full = e.get('pre', '') + fmtv(e['to'], e.get('fmt', 'int')) + e.get('suf', '')
        sz = fit(d, full, e.get('size', 200)); s = e.get('pre', '') + fmtv(v, e.get('fmt', 'int')) + e.get('suf', '')
        tx(d, (cx, y), s, F(AB, sz * back(lt / 0.3)), YEL if g < 1 else C(e.get('col', 'y')), 10)
    elif ty == 'formula':
        op = e.get('op', '×'); parts = [(e['q'], WH), (op, GRY), (e['r'], WH), ('=', GRY), (e['c'], YEL)]
        f = F(AB, 92); widths = [d.textlength(p, font=f) for p, _ in parts]; gap = 46
        tot = sum(widths) + gap * 4; scl = min(1, 1760 / tot); x = cx - tot * scl / 2
        labs = ['QUANTITY', '', 'RATE', '', 'COST'] if op == '×' else ['', '', '', '', 'RESULT']
        for j, ((p, col), w) in enumerate(zip(parts, widths)):
            tt = lt - j * 0.45
            if tt >= 0:
                s2 = back(tt / 0.3); xx = x + w * scl / 2
                if j in (0, 2, 4):
                    d.rounded_rectangle([xx - w * scl / 2 - 22, y - 80, xx + w * scl / 2 + 22, y + 80], 22, fill=(20, 20, 28) if j < 4 else (60, 40, 10), outline=YEL if j == 4 else (90, 90, 110), width=4)
                    if labs[j]: d.text((xx, y - 118), labs[j], font=F(I6, 34), fill=GRY, anchor='mm')
                tx(d, (xx, y), p, F(AB, 92 * scl * s2), col, 6)
            x += (w + gap) * scl
    elif ty == 'bars':
        vmax = e['vmax']; n = len(e['items']); bh = 110; gapy = 60
        for j, (name, v, col, lab) in enumerate(e['items']):
            t0 = j * e.get('gap', 0.8); g = ease((lt - t0) / 0.9); yy = y + j * (bh + gapy)
            if lt < t0: continue
            d.text((200, yy - 30), name, font=F(AB, 40), fill=WH, anchor='lm', stroke_width=4, stroke_fill=BLK)
            d.rounded_rectangle([200, yy, 1500, yy + bh - 30], 18, fill=(25, 25, 32))
            d.rounded_rectangle([200, yy, 200 + max(40, 1300 * v / vmax * g), yy + bh - 30], 18, fill=C(col))
            tx(d, (1540, yy + (bh - 30) / 2), lab, F(AB, 58), WH, 5, 'lm')
    elif ty == 'table':
        rows = e['rows']; step = e.get('step', 1.2); x0, x1 = 300, 1620; rh = 92
        d.rounded_rectangle([x0 - 30, y - 30, x1 + 30, y + rh * len(rows) + 10], 26, fill=(14, 14, 20), outline=(80, 80, 100), width=3)
        for j, (a, b) in enumerate(rows):
            tt = lt - j * step
            if tt < 0: continue
            g = ease(tt / 0.4); yy = y + j * rh + rh / 2 - 10; last = a.upper() == 'TOTAL'
            col = YEL if last else WH
            if last: d.line([x0, yy - rh / 2 + 6, x1, yy - rh / 2 + 6], fill=YEL, width=4)
            d.text((x0 + 20 - 40 * (1 - g), yy), a, font=F(AB if last else I6, 50), fill=col, anchor='lm')
            d.text((x1 - 20, yy), b, font=F(AB, 56), fill=col, anchor='rm')
    elif ty == 'chips':
        f = F(AB, 50); rows, row, wsum = [], [], 0
        for it in e['items']:
            w = d.textlength(it, font=f) + 60
            if row and wsum + w + 24 > 1640: rows.append(row); row, wsum = [], 0
            row.append((it, w)); wsum += w + 24
        rows.append(row); k = 0
        for ri, row in enumerate(rows):
            tw = sum(w for _, w in row) + 24 * (len(row) - 1); x = cx - tw / 2
            for it, w in row:
                tt = lt - k * e.get('step', 0.45); k += 1
                if tt >= 0:
                    s2 = back(tt / 0.3); yy = y + ri * 120; xc = x + w / 2; hw, hh = w / 2 * s2, 46 * s2
                    d.rounded_rectangle([xc - hw, yy - hh, xc + hw, yy + hh], int(30 * s2) or 1, fill=AC, outline=WH, width=3)
                    d.text((xc, yy), it, font=F(AB, 50 * s2), fill=WH, anchor='mm')
                x += w + 24
    elif ty == 'map':
        # scale map: big square = county area, small square = city area, both to scale
        g = ease(lt / 0.8); side = 640; bx, by = cx - 520, 160
        d.rectangle([bx, by, bx + side * g, by + side * g], fill=(30, 60, 90), outline=WH, width=4)
        if lt > 0.9:
            ss = side * math.sqrt(e['small'] / e['big']); g2 = back((lt - 0.9) / 0.4)
            sx, sy = bx + side * 0.62, by + side * 0.42
            d.rectangle([sx, sy, sx + ss * g2, sy + ss * g2], fill=AC, outline=WH, width=3)
            d.line([sx + ss, sy + ss / 2, bx + side + 90, by + 470], fill=AC, width=4)
            tx(d, (bx + side + 110, by + 470), f"{e['sl']}: {e['small']:,.0f} sq mi", F(AB, 48), AC, 5, 'lm')
        tx(d, (bx + side + 110, by + 120), e['bl'], F(AB, 56), WH, 5, 'lm')
        tx(d, (bx + side + 110, by + 200), f"{e['big']:,.0f} sq mi", F(AB, 80), YEL, 6, 'lm')
        d.text((bx + side + 110, by + 560), 'Squares drawn to scale', font=F(I4, 32), fill=GRY, anchor='lm')
    elif ty == 'stats':
        n = len(e['items']); wcol = 1700 / n
        for j, (big, lab) in enumerate(e['items']):
            tt = lt - j * 0.9
            if tt < 0: continue
            xx = 110 + wcol * (j + 0.5)
            tx(d, (xx, y), big, F(AB, 150 * back(tt / 0.3)), YEL, 8); tx(d, (xx, y + 120), lab, F(I6, 46), WH, 4)
    elif ty in ('rule', 'assume'):
        s2 = back(lt / 0.35); lab = f"RULE {e['n']}" if ty == 'rule' else 'ASSUMPTION'
        col = (40, 120, 230) if ty == 'rule' else (210, 140, 20)
        st = Image.new('RGBA', (1500, 300), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
        sd.rounded_rectangle([10, 10, 1490, 290], 34, fill=col + (235,), outline=WH + (255,), width=8)
        sd.text((750, 95), lab, font=F(AB, 56), fill=WH, anchor='mm')
        sd.text((750, 195), e['s'], font=F(AB, fit(sd, e['s'], 84, 1400)), fill=YEL, anchor='mm', stroke_width=4, stroke_fill=BLK)
        st = st.rotate(-3, expand=True, resample=Image.BICUBIC)
        if s2 > 0.05:
            st = st.resize((int(st.width * s2), int(st.height * s2))); d._image.paste(st, (cx - st.width // 2, y - st.height // 2), st)
    elif ty == 'range':
        lo, hi, pick = e['lo'], e['hi'], e['pick']; x0, x1 = 360, 1560; g = ease(lt / 0.8)
        d.text((cx, y - 140), e['lab'], font=F(AB, 52), fill=WH, anchor='mm', stroke_width=4, stroke_fill=BLK)
        d.rounded_rectangle([x0, y - 22, x0 + (x1 - x0) * g, y + 22], 22, fill=(60, 140, 220))
        tx(d, (x0, y + 90), f'${lo}', F(AB, 64), WH, 5); tx(d, (x1, y + 90), f'${hi}', F(AB, 64), WH, 5)
        if lt > 1.0:
            g2 = ease((lt - 1.0) / 0.9); px = x0 + (x1 - x0) * (pick - lo) / (hi - lo) * g2 + 0
            px = x0 + (x1 - x0) * ((pick - lo) / (hi - lo))
            d.polygon([(px, y - 40), (px - 30, y - 90), (px + 30, y - 90)], fill=YEL)
            tx(d, (px, y + 170), f'WE USE ${pick}', F(AB, 72 * back((lt - 1.0) / 0.3)), YEL, 6)

def lens(d, cx, cy, r, ring):
    a = math.radians(45); sx, sy = cx + (r - ring / 2) * math.cos(a), cy + (r - ring / 2) * math.sin(a)
    ex, ey = sx + r * 0.85 * math.cos(a), sy + r * 0.85 * math.sin(a); hw = int(ring * 1.2)
    d.line([sx, sy, ex, ey], fill=AC, width=hw); d.ellipse([ex - hw / 2, ey - hw / 2, ex + hw / 2, ey + hw / 2], fill=AC)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AC); d.ellipse([cx - r + ring, cy - r + ring, cx + r - ring, cy + r - ring], fill=(14, 15, 19))
    d.text((cx, cy + r * 0.04), '6', font=F(AB, r * 1.3), fill=WH, anchor='mm')

LOWER = Image.new('RGBA', (W, 150), (0, 0, 0, 0))
_ld = ImageDraw.Draw(LOWER)
for yy in range(150): _ld.line([(0, yy), (W, yy)], fill=(0, 0, 0, int(190 * (yy / 150) ** 0.8)))

def caption(d, seg, t):
    ws = seg['text'].split(); lt = t - seg['vs']
    if lt < 0 or lt > seg['vo'] + 0.2: return
    wt = [len(w) + 2 for w in ws]; tot = sum(wt); acc = 0; starts = []
    for w in wt: starts.append(seg['vo'] * acc / tot); acc += w
    idx = max([i for i, s0 in enumerate(starts) if s0 <= lt] or [0]); c0 = (idx // 7) * 7; chunk = ws[c0:c0 + 7]
    f = F(AB, 50); sp = d.textlength(' ', font=f); widths = [d.textlength(w, font=f) for w in chunk]
    x = W / 2 - (sum(widths) + sp * (len(chunk) - 1)) / 2
    for j, w in enumerate(chunk):
        d.text((x, 1000), w, font=f, fill=YEL if c0 + j == idx else WH, anchor='lm', stroke_width=5, stroke_fill=BLK); x += widths[j] + sp

def chrome(fr, seg, t, est=False, src=''):
    fr.paste(LOWER, (0, H - 150), LOWER); d = ImageDraw.Draw(fr)
    lens(d, 70, 64, 30, 7); d.text((116, 64), 'GTA6 UNCOVERED  ·  THE REAL COST', font=F(AB, 30), fill=WH, anchor='lm', stroke_width=4, stroke_fill=BLK)
    if est:
        d.rounded_rectangle([W - 300, 36, W - 40, 94], 14, fill=(210, 140, 20)); d.text((W - 170, 65), 'ESTIMATE', font=F(AB, 34), fill=WH, anchor='mm')
    if src: d.text((W - 40, 925), 'Source: ' + src, font=F(I4, 26), fill=(210, 210, 215), anchor='rm', stroke_width=3, stroke_fill=BLK)
    if seg['v']['kind'] == 'clip': d.text((40, 925), 'Official Rockstar trailer footage · Unofficial fan channel', font=F(I4, 24), fill=(210, 210, 215), anchor='lm', stroke_width=3, stroke_fill=BLK)
    caption(d, seg, t)
    return d

def shots_of(v):
    return v.get('shots') or [(v['f'], v['s'], v.get('m', 4.5))]
def clip_frames(seg, j, span):
    f, s0, m = shots_of(seg['v'])[j]; need = int(math.ceil(span * FPS)) + 2
    frs = grab(f, s0, min(need, int(min(m, 4.8) * FPS)))  # never more than ~5 s of trailer per clip
    if len(frs) < need: frs = [frs[min(len(frs) - 1, int(i * len(frs) / need))] for i in range(need)]  # slow-mo inside the clean window
    return frs

def seg_frame(seg, t, cache):
    v = seg['v']; lt = t - seg['t0']; span = seg['t1'] - seg['t0']
    if v['kind'] == 'clip':
        sh = shots_of(v); ns = len(sh); sspan = span / ns; j = min(ns - 1, int(lt / sspan)); ls = lt - j * sspan
        if cache.get('j') != j: cache['fr'] = clip_frames(seg, j, sspan); cache['j'] = j
        frs = cache['fr']; src = frs[max(0, min(len(frs) - 1, int(ls * FPS)))]
        z = 1.0 + 0.06 * ls / max(1, sspan); cw, ch = int(W / z), int(H / z)
        fr = src.crop(((W - cw) // 2, (H - ch) // 2, (W + cw) // 2, (H + ch) // 2)).resize((W, H), Image.BILINEAR)
        fl = 0.35 * (1 - clamp(ls / 0.15))
        if fl > 0: fr = Image.blend(fr, Image.new('RGB', (W, H), WH), fl)
        chrome(fr, seg, t); return fr
    bg = bg_still(*v['bg']); ox = int(48 + 40 * math.sin(lt * 0.25)); oy = int(27 * (lt / max(1, span)))
    fr = bg.crop((ox, oy, ox + W, oy + H)).copy(); d = ImageDraw.Draw(fr)
    if v['kind'] == 'chapter':
        g = ease((lt) / 0.5)
        d.rectangle([0, 380, W * g, 700], fill=(255, 90, 60))
        tx(d, (W // 2, 470), f"CHAPTER {v['n']}", F(AB, 60 * back(lt / 0.35)), WH, 5)
        tx(d, (W // 2, 590), v['title'], F(AB, fit(d, v['title'], 120) * back((lt - 0.2) / 0.35)), WH, 8)
        chrome(fr, seg, t); return fr
    for e in v['els']: draw_el(d, e, lt)
    chrome(fr, seg, t, v.get('est', True), v.get('src', '')); return fr

def render_seg(i):
    seg = SEGS[i]; fn = f'{OUT}/parts/p{i:03d}.mp4'
    a, b = int(round(seg['t0'] * FPS)), int(round(seg['t1'] * FPS))
    if os.path.exists(fn): return fn
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', fn + '.tmp.mp4'], stdin=subprocess.PIPE)
    cache = {}
    for k in range(a, b): p.stdin.write(seg_frame(seg, k / FPS, cache).tobytes())
    p.stdin.close(); p.wait(); os.replace(fn + '.tmp.mp4', fn); return fn

SR = 44100
def build_audio():
    N = int(TOTAL * SR) + SR; voice = np.zeros(N); sfx = np.zeros(N); music = np.zeros((N, 2)); rng = np.random.default_rng(SEED)
    for s in SEGS:
        v, sr = sf.read(vfn(s['text']))
        if v.ndim > 1: v = v.mean(1)
        idx = np.round(np.arange(0, len(v), sr / SR)).astype(int); idx = idx[idx < len(v)]; v = v[idx]
        i = int(s['vs'] * SR); voice[i:i + len(v)] += v[:N - i]
    def put(buf, sig, t0, g=1.0):
        i = int(t0 * SR)
        if 0 <= i < len(buf): n = min(len(sig), len(buf) - i); buf[i:i + n] += sig[:n] * g
    def env(n, a, dd): tt = np.arange(n) / SR; return np.minimum(1, tt / max(a, 1e-4)) * np.exp(-tt / dd)
    def lp(x, k): return np.convolve(x, np.ones(k) / k, 'same')
    def whoosh(L=0.45): n = int(L * SR); tt = np.arange(n) / SR; return lp(rng.standard_normal(n), 4) * np.sin(np.pi * tt / L) ** 2 * 0.6
    def boom():
        n = int(1.2 * SR); tt = np.arange(n) / SR; f = 38 + 90 * np.exp(-tt * 9)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.45) + lp(rng.standard_normal(n), 30) * env(n, 0.001, 0.08) * 0.6
    def pop(): n = int(0.09 * SR); tt = np.arange(n) / SR; f = 900 + 700 * np.exp(-tt * 40); return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.025)
    def tick(): n = int(0.03 * SR); return rng.standard_normal(n) * env(n, 0.0005, 0.004) * 0.8
    for s in SEGS[1:]: put(sfx, whoosh(), s['t0'] - 0.2, 0.22)
    for s in SEGS:
        v = s['v']
        if v['kind'] == 'chapter': put(sfx, boom(), s['t0'] + 0.05, 0.7)
        if v['kind'] == 'card':
            for e in v['els']:
                b0 = s['t0'] + e.get('delay', 0)
                if e['t'] == 'counter':
                    tt = 0.0; dur = e.get('dur', 1.6)
                    while tt < dur: put(sfx, tick(), b0 + tt, 0.25); tt += 0.05 + 0.12 * (tt / dur) ** 2
                    put(sfx, pop(), b0 + dur, 0.4)
                elif e['t'] == 'formula': [put(sfx, pop(), b0 + j * 0.45, 0.3) for j in range(5)]
                elif e['t'] in ('bars',): [put(sfx, pop(), b0 + j * e.get('gap', 0.8), 0.3) for j in range(len(e['items']))]
                elif e['t'] == 'table': [put(sfx, pop(), b0 + j * e.get('step', 1.2), 0.3) for j in range(len(e['rows']))]
                elif e['t'] == 'chips': [put(sfx, pop(), b0 + j * e.get('step', 0.45), 0.3) for j in range(len(e['items']))]
                elif e['t'] in ('rule', 'assume'): put(sfx, boom(), b0, 0.35)
    BEAT = 60 / 96; BAR = 4 * BEAT
    def saw(f, n): tt = np.arange(n) / SR; return 2 * ((tt * f) % 1) - 1
    def note(m): return 440 * 2 ** ((m - 69) / 12)
    PROGS = [[[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 56, 59]], [[50, 53, 57], [46, 50, 53], [48, 52, 55], [45, 49, 52]], [[52, 55, 59], [48, 52, 55], [50, 54, 57], [47, 51, 54]]]
    def addm(sig, t0, g, pan=0.0):
        i = int(t0 * SR)
        if i >= N or i < 0: return
        n = min(len(sig), N - i); music[i:i + n, 0] += sig[:n] * g * (1 - max(pan, 0)); music[i:i + n, 1] += sig[:n] * g * (1 + min(pan, 0))
    def kick(): n = int(0.4 * SR); tt = np.arange(n) / SR; f = 46 + 120 * np.exp(-tt * 32); return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.16)
    def hat(): n = int(0.035 * SR); s_ = rng.standard_normal(n); return (s_ - lp(s_, 4)) * env(n, 0.001, 0.01) * 0.3
    chap_t = [s['t0'] for s in SEGS if s['v']['kind'] == 'chapter']
    b, tb = 0, 0.0
    while tb < TOTAL:
        sec = sum(1 for c in chap_t if c <= tb); CH = PROGS[sec % 3]; ch = CH[b % 4]; rt = ch[0] - 24; n = int(BAR * SR)
        pad = sum(lp(saw(note(m), n) + saw(note(m) * 1.007, n), 60) for m in ch) / 6
        addm(pad * np.minimum(1, np.arange(n) / (0.3 * SR)), tb, 0.26)
        for q in range(16):
            tq = tb + q * BEAT / 4
            if q % 4 == 0: addm(kick(), tq, 0.6)
            addm(hat(), tq, 0.6, 0.3 if q % 2 else -0.3)
            if q % 2 == 0:
                m = rt + (12 if (q // 2) % 2 else 0); bn = int(BEAT / 2 * 0.9 * SR); addm(lp(saw(note(m), bn), 14) * env(bn, 0.003, 0.11), tq, 0.3)
        b += 1; tb += BAR
    e = np.convolve(np.abs(voice), np.ones(int(0.15 * SR)) / int(0.15 * SR), 'same')
    duck = 1 - 0.75 * np.clip(e / (e.max() * 0.2), 0, 1); music *= duck[:, None]
    mixd = (music * 0.4 + (voice * 1.7 + sfx)[:, None])[: int(TOTAL * SR)]
    fo = int(1.0 * SR); mixd[-fo:] *= np.linspace(1, 0, fo)[:, None]
    mixd = np.tanh(mixd * 0.9); mixd *= 0.95 / np.abs(mixd).max(); sf.write(OUT + '/mix.wav', mixd, SR)

if MODE == 'preview':
    idx = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(0, len(SEGS), max(1, len(SEGS) // 24)))[:24]
    ims = []
    for i in idx:
        s = SEGS[i]; tt = s['t0'] + min(s['t1'] - s['t0'] - 0.1, 2.8); ims.append(seg_frame(s, tt, {}).resize((480, 270)))
    cols = 4; rows = (len(ims) + cols - 1) // cols; cs = Image.new('RGB', (480 * cols, 270 * rows))
    for j, im in enumerate(ims): cs.paste(im, ((j % cols) * 480, (j // cols) * 270))
    cs.save(OUT + '/contact.jpg', quality=85); print('total', round(TOTAL, 1), 'segs', len(SEGS)); print('\n'.join(chapters()))
elif MODE == 'full':
    from multiprocessing import Pool
    os.makedirs(OUT + '/parts', exist_ok=True)
    build_audio()
    with Pool(int(os.environ.get('JOBS', '2'))) as pool: files = pool.map(render_seg, range(len(SEGS)))
    with open(OUT + '/parts.txt', 'w') as f:
        for fn in files: f.write(f"file '{fn}'\n")
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', OUT + '/parts.txt', '-c', 'copy', OUT + '/video.tmp.mp4'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', OUT + '/video.tmp.mp4', '-i', OUT + '/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                    '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '192k', '-ar', '44100', '-shortest', OUT + '/final.tmp.mp4'], check=True)
    os.replace(OUT + '/final.tmp.mp4', OUT + '/' + sc.NAME + '.mp4')
    open(OUT + '/chapters.txt', 'w').write('\n'.join(chapters())); print('done', sc.NAME, round(TOTAL, 1)); print('\n'.join(chapters()))
elif MODE == 'thumb':
    T = sc.THUMB; im = grab(T['f'], T['s'], 1, 1280, 720)[0]; im = Image.blend(im, Image.new('RGB', im.size, (0, 0, 0)), 0.25); d = ImageDraw.Draw(im)
    d.text((60, 70), T['l1'], font=F(AB, 120), fill=WH, anchor='la', stroke_width=10, stroke_fill=BLK)
    d.text((60, 210), T['l2'], font=F(AB, 230), fill=YEL, anchor='la', stroke_width=14, stroke_fill=BLK)
    d.rounded_rectangle([60, 560, 470, 660], 18, fill=(210, 140, 20)); d.text((265, 610), T.get('tag', 'ESTIMATE'), font=F(AB, 64), fill=WH, anchor='mm')
    im.save(OUT + '/thumb.jpg', quality=90); print('thumb ok')
