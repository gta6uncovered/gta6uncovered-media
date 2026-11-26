# GTA6 Uncovered video engine. Usage: python3 -I engine.py <video_dir> voice|preview|full
# <video_dir>/script.py defines NAME, LINES, SHOTS, CARDS, IMPACTS, DROP, TICKS, SOURCE.
import sys, os, json, math, subprocess, importlib.util
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont

S = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(sys.argv[1]); MODE = sys.argv[2]
spec = importlib.util.spec_from_file_location('script', OUT + '/script.py'); sc = importlib.util.module_from_spec(spec); spec.loader.exec_module(sc)
LINES, SHOTS, CARDS = sc.LINES, sc.SHOTS, sc.CARDS
IMPACTS_K = getattr(sc, 'IMPACTS', []); DROP = getattr(sc, 'DROP', None); TICKS = getattr(sc, 'TICKS', [])
CAP_Y = getattr(sc, 'CAP_Y', 1450); TAG = getattr(sc, 'TAG', ''); SOURCE = getattr(sc, 'SOURCE', ''); SPEED = getattr(sc, 'SPEED', 1.16); SEED = getattr(sc, 'SEED', 4)
FOOT = os.environ.get('FOOT', '/home/claude/footage')
AB, I4, I6 = S + '/fonts/ab.ttf', S + '/fonts/i4.ttf', S + '/fonts/i6.ttf'
W, H, FPS = 1080, 1920, 30
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
    t = clamp(t); c = 1.9
    return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2

# ---------------- voice ----------------
if MODE == 'voice':
    from kokoro_onnx import Kokoro
    k = Kokoro(os.environ.get('KK', '/tmp/kk') + '/kokoro-v1.0.onnx', os.environ.get('KK', '/tmp/kk') + '/voices-v1.0.bin'); dur = {}
    for key, txt in LINES:
        a, sr = k.create(txt, voice='am_fenrir', speed=SPEED, lang='en-us')
        sf.write(f'{OUT}/vo_{key}.wav', a, sr); dur[key] = len(a) / sr
    json.dump(dur, open(OUT + '/vo_durations.json', 'w')); print(dur, sum(dur.values())); sys.exit()

DUR = json.load(open(OUT + '/vo_durations.json'))
PAD = 0.12
SEGS, t = [], 0.0
for key, txt in LINES:
    d = DUR[key]; SEGS.append(dict(key=key, text=txt, t0=t, vo=d, t1=t + d + PAD)); t += d + PAD
TOTAL = SEGS[-1]['t0'] + SEGS[-1]['vo'] + 0.1
SEGS[-1]['t1'] = TOTAL
SEG = {s['key']: s for s in SEGS}
IMPACTS = [SEG[k]['t0'] + o for k, o in IMPACTS_K]

CUTS = []
for s in SEGS:
    shots = SHOTS[s['key']]; n = len(shots); span = s['t1'] - s['t0']
    for i, sh in enumerate(shots):
        f, st = sh[0], sh[1]; m = sh[2] if len(sh) > 2 else 99
        CUTS.append(dict(file=f, src=st, m=m, a=s['t0'] + span * i / n, b=s['t0'] + span * (i + 1) / n))

def load_shot(c):
    need = int(math.ceil((c['b'] - c['a']) * FPS)) + 2; n = min(need, int(c.get('m', 99) * FPS))
    cmd = ['ffmpeg', '-loglevel', 'error', '-ss', str(c['src']), '-i', f"{FOOT}/{c['file']}.mp4", '-frames:v', str(n), '-an',
           '-vf', ('fps=30,crop=512:864:704:108' if c['file'] == 't2' else 'fps=30,crop=640:1080:640:0') + ',scale=1188:2006:flags=lanczos,eq=contrast=1.08:saturation=1.18', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    fw, fh = 1188, 2006; k = len(raw) // (fw * fh * 3)
    frs = [Image.frombuffer('RGB', (fw, fh), raw[i * fw * fh * 3:(i + 1) * fw * fh * 3]) for i in range(k)]
    if k < need: frs = [frs[min(k - 1, int(j * k / need))] for j in range(need)]  # slow-mo stretch inside the clean window
    return frs

def grad(h, top=True, a=200):
    g = Image.new('L', (1, h))
    for y in range(h): g.putpixel((0, y), int(a * ((1 - y / h) if top else (y / h)) ** 1.6))
    return g.resize((W, h))
TOPG, BOTG = grad(900, True, 225), grad(760, False, 235)
BLACK = Image.new('RGB', (W, H), BLK)

WORDS = []
for s in SEGS:
    ws = s['text'].split(); wt = [len(w) + 2 for w in ws]; tot = sum(wt); acc = 0
    for i, w in enumerate(ws):
        a = s['t0'] + 0.06 + (s['vo'] - 0.12) * acc / tot; acc += wt[i]; WORDS.append((a, w, s['key']))
def chunk_at(t):
    seg = [s for s in SEGS if s['t0'] <= t < s['t1']]
    if not seg: return None, -1, 0
    seg = seg[0]; ws = [w for w in WORDS if w[2] == seg['key']]
    idx = max([i for i, w in enumerate(ws) if w[0] <= t] or [0]); c0 = (idx // 3) * 3
    return [w[1] for w in ws[c0:c0 + 3]], idx - c0, t - ws[idx][0]

def text_c(d, xy, s, f, fill, sw=10, anchor='mm'):
    d.text(xy, s, font=f, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=BLK)

def lens(d, cx, cy, r, ring):
    a = math.radians(45); sx, sy = cx + (r - ring / 2) * math.cos(a), cy + (r - ring / 2) * math.sin(a)
    ex, ey = sx + r * 0.85 * math.cos(a), sy + r * 0.85 * math.sin(a); hw = int(ring * 1.2)
    d.line([sx, sy, ex, ey], fill=AC, width=hw); d.ellipse([ex - hw / 2, ey - hw / 2, ex + hw / 2, ey + hw / 2], fill=AC)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=AC); d.ellipse([cx - r + ring, cy - r + ring, cx + r - ring, cy + r - ring], fill=(14, 15, 19))
    d.text((cx, cy + r * 0.04), '6', font=F(AB, r * 1.3), fill=WH, anchor='mm')

def fmtv(v, fm):
    if fm == 'int': return f'{int(round(v)):,}'
    if fm == 'M': return f'{v:.1f}M' if v < 100 else f'{v:.0f}M'
    if fm == 'B': return f'{v:.2f}B'
    if fm == 'd1': return f'{v:.1f}'
    if fm == 'd2': return f'{v:.2f}'
    return f'{v:.0f}'

def fit(d, s, size, maxw=980, font=AB):
    while size > 20 and d.textlength(s, font=F(font, size)) > maxw: size -= 2
    return size

def draw_el(d, e, lt):
    ty = e['type']; dl = e.get('delay', 0); lt = lt - dl
    if lt < 0: return
    y = e.get('y', 500)
    if ty == 'text':
        font = I6 if e.get('font') == 'i' else AB
        size = fit(d, e['s'], e.get('size', 90), font=font)
        s2 = back(lt / 0.32) if e.get('pop', True) else 1
        text_c(d, (W // 2, y), e['s'], F(font, size * s2), C(e.get('col', 'w')), e.get('sw', 5 if font == I6 else 11))
    elif ty == 'counter':
        g = ease(lt / e.get('dur', 1.6)); v = e.get('frm', 0) + (e['to'] - e.get('frm', 0)) * g
        s = e.get('pre', '') + fmtv(v, e.get('fmt', 'int')) + e.get('suf', '')
        full = e.get('pre', '') + fmtv(e['to'], e.get('fmt', 'int')) + e.get('suf', '')
        size = fit(d, full, e.get('size', 120))
        wob = 1 + 0.06 * math.sin(lt * 22) * (1 - g) if g < 1 else back((lt - e.get('dur', 1.6)) / 0.3) * 0 + 1
        text_c(d, (W // 2, y), s, F(AB, size * back(lt / 0.3) * wob), C(e.get('col', 'y') if g < 1 else e.get('endcol', e.get('col', 'y'))), 12)
    elif ty == 'bars':
        vmax = e['vmax']
        for j, (name, v, col, lab) in enumerate(e['items']):
            t0 = j * e.get('gap', 0.7); g = ease((lt - t0) / 0.8); yy = y + j * 140
            if lt < t0: continue
            d.rounded_rectangle([90, yy, W - 90, yy + 100], 24, fill=(0, 0, 0))
            d.rounded_rectangle([90, yy, 90 + max(48, (W - 180) * v / vmax * g), yy + 100], 24, fill=C(col))
            d.text((120, yy + 50), name, font=F(AB, 40), fill=WH, anchor='lm', stroke_width=5, stroke_fill=BLK)
            d.text((W - 120, yy + 50), lab, font=F(AB, 46), fill=WH, anchor='rm', stroke_width=6, stroke_fill=BLK)
    elif ty == 'stamp':
        s2 = back(lt / 0.35)
        st = Image.new('RGBA', (880, 300), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
        sd.rounded_rectangle([10, 10, 870, 290], 30, outline=WH + (255,), width=10, fill=C(e.get('col', 'r')) + (235,))
        sd.text((440, 105), e['l1'], font=F(AB, fit(sd, e['l1'], 56, 800)), fill=WH, anchor='mm')
        sd.text((440, 200), e['l2'], font=F(AB, fit(sd, e['l2'], 84, 800)), fill=YEL, anchor='mm', stroke_width=4, stroke_fill=BLK)
        st = st.rotate(e.get('ang', -7), expand=True, resample=Image.BICUBIC)
        if s2 > 0.05:
            st = st.resize((int(st.width * s2), int(st.height * s2)))
            d._image.paste(st, (W // 2 - st.width // 2, y - st.height // 2), st)
    elif ty == 'chips':
        f = F(AB, e.get('size', 46)); rows, row, wsum = [], [], 0
        for it in e['items']:
            w = d.textlength(it, font=f) + 56
            if row and wsum + w + 20 > 960: rows.append(row); row, wsum = [], 0
            row.append((it, w)); wsum += w + 20
        rows.append(row); k = 0
        for ri, row in enumerate(rows):
            tw = sum(w for _, w in row) + 20 * (len(row) - 1); x = W / 2 - tw / 2
            for it, w in row:
                tt = lt - k * e.get('step', 0.35); k += 1
                if tt >= 0:
                    s2 = back(tt / 0.3); yy = y + ri * 100; cx = x + w / 2
                    hw, hh = w / 2 * s2, 40 * s2
                    d.rounded_rectangle([cx - hw, yy - hh, cx + hw, yy + hh], int(30 * s2) or 1, fill=C(e.get('bg', 'a')), outline=WH, width=3)
                    d.text((cx, yy), it, font=F(AB, e.get('size', 46) * s2), fill=WH, anchor='mm')
                x += w + 20
    elif ty == 'formula':
        # stacked Real Cost maths: QTY x RATE = COST, one row each, labels on the left
        rows = [(e.get('ql', 'QUANTITY'), e['q']), (e.get('rl', 'x RATE'), e['r']), (e.get('cl', '= COST'), e['c'])]
        for j, (lab, val) in enumerate(rows):
            tt = lt - j * e.get('step', 0.6)
            if tt < 0: continue
            yy = y + j * 150; s2 = back(tt / 0.3); last = j == 2
            d.rounded_rectangle([70, yy - 62, W - 70, yy + 62], 26, fill=(60, 40, 10) if last else (16, 16, 22), outline=YEL if last else (110, 110, 130), width=5)
            d.text((110, yy), lab, font=F(I6, 40), fill=GRY, anchor='lm')
            d.text((W - 110, yy), val, font=F(AB, fit(d, val, 84 * s2, 640)), fill=YEL if last else WH, anchor='rm', stroke_width=5, stroke_fill=BLK)
    elif ty == 'strike':
        size = fit(d, e['s'], e.get('size', 96)); f = F(AB, size * back(lt / 0.3))
        col = C(e.get('col', 'w')); sl = lt - e.get('at', 0.6)
        text_c(d, (W // 2, y), e['s'], f, col if sl < 0 else GRY, 11)
        if sl >= 0:
            tw = d.textlength(e['s'], font=F(AB, size)); g = ease(sl / 0.25)
            d.line([W / 2 - tw / 2 - 10, y, W / 2 - tw / 2 - 10 + (tw + 20) * g, y], fill=RED, width=16)

def overlay(d, t):
    seg = [s for s in SEGS if s['t0'] <= t][-1]; k = seg['key']; lt = t - seg['t0']
    lens(d, 92, 120, 36, 8); d.text((146, 120), 'GTA6 UNCOVERED', font=F(AB, 32), fill=WH, anchor='lm', stroke_width=4, stroke_fill=BLK)
    if TAG:
        tw = d.textlength(TAG, font=F(AB, 34)) + 40
        d.rounded_rectangle([W - 60 - tw, 92, W - 60, 148], 14, fill=(210, 140, 20)); d.text((W - 60 - tw / 2, 120), TAG, font=F(AB, 34), fill=WH, anchor='mm')
    for e in CARDS.get(k, []): draw_el(d, e, lt)
    words, act, wt = chunk_at(t)
    if words:
        f = F(AB, 78); sp = d.textlength(' ', font=f)
        widths = [d.textlength(w.upper(), font=f) for w in words]
        tot = sum(widths) + sp * (len(words) - 1); scl = min(1, 1000 / tot)
        x = W / 2 - tot * scl / 2
        for j, w in enumerate(words):
            pop = 1.0 + (0.12 * (1 - clamp(wt / 0.12)) if j == act else 0)
            d.text((x + widths[j] * scl / 2, CAP_Y), w.upper(), font=F(AB, 78 * pop * scl), fill=YEL if j == act else WH, anchor='mm', stroke_width=10, stroke_fill=BLK)
            x += (widths[j] + sp) * scl
    foot = 'Official Rockstar trailer footage · Unofficial fan channel'
    d.text((W // 2, 1600), foot, font=F(I4, 28), fill=(220, 220, 225), anchor='mm', stroke_width=3, stroke_fill=BLK)
    if SOURCE: d.text((W // 2, 1645), 'Source: ' + SOURCE, font=F(I4, 26), fill=(200, 200, 205), anchor='mm', stroke_width=3, stroke_fill=BLK)

def frame_from(src, t, cut, lt):
    z = 1.0 + 0.06 * (lt / max(0.1, cut['b'] - cut['a'])) + 0.05 * (1 - ease(lt / 0.25))
    cw, ch = int(W / z * 1.1), int(H / z * 1.045)
    cx, cy = src.width // 2 + int(12 * math.sin(t * 0.9)), src.height // 2
    sh = 0
    for im in IMPACTS:
        if 0 <= t - im < 0.35: sh = 22 * (1 - (t - im) / 0.35)
    cx += int(sh * math.sin(t * 90)); cy += int(sh * math.cos(t * 77))
    fr = src.crop((cx - cw // 2, cy - ch // 2, cx + cw // 2, cy + ch // 2)).resize((W, H), Image.BILINEAR)
    fr.paste(BLACK.crop((0, 0, W, 900)), (0, 0), TOPG); fr.paste(BLACK.crop((0, 0, W, 760)), (0, H - 760), BOTG)
    return fr

def render():
    tmp = OUT + '/video.tmp.mp4'
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', tmp], stdin=subprocess.PIPE)
    n = int(TOTAL * FPS); ci = -1; frames = None
    for i in range(n):
        t = i / FPS
        c = max(j for j, c in enumerate(CUTS) if c['a'] <= t)
        if c != ci: frames = load_shot(CUTS[c]); ci = c
        cut = CUTS[c]; lt = t - cut['a']; src = frames[min(len(frames) - 1, int(lt * FPS))]
        fr = frame_from(src, t, cut, lt)
        fl = 0.55 * (1 - clamp(lt / 0.12)) if c > 0 else 0
        for im in IMPACTS:
            if 0 <= t - im < 0.15: fl = max(fl, 0.7 * (1 - (t - im) / 0.15))
        if fl > 0: fr = Image.blend(fr, Image.new('RGB', (W, H), WH), fl)
        overlay(ImageDraw.Draw(fr), t); p.stdin.write(fr.tobytes())
    p.stdin.close()
    if p.wait() != 0: sys.exit('video failed')

SR = 44100
def build_audio():
    N = int(TOTAL * SR) + SR
    voice = np.zeros(N); sfx = np.zeros(N); music = np.zeros((N, 2)); rng = np.random.default_rng(SEED)
    for s in SEGS:
        v, sr = sf.read(f"{OUT}/vo_{s['key']}.wav")
        if v.ndim > 1: v = v.mean(1)
        idx = np.round(np.arange(0, len(v), sr / SR)).astype(int); idx = idx[idx < len(v)]; v = v[idx]
        i = int(s['t0'] * SR); voice[i:i + len(v)] += v[:N - i]
    def put(buf, sig, t0, g=1.0):
        i = int(t0 * SR)
        if 0 <= i < len(buf): n = min(len(sig), len(buf) - i); buf[i:i + n] += sig[:n] * g
    def env(n, a, dd):
        tt = np.arange(n) / SR; return np.minimum(1, tt / max(a, 1e-4)) * np.exp(-tt / dd)
    def lp(x, k): return np.convolve(x, np.ones(k) / k, 'same')
    def whoosh(L=0.45):
        n = int(L * SR); tt = np.arange(n) / SR; w = lp(rng.standard_normal(n), 4)
        return w * np.sin(np.pi * tt / L) ** 2 * 0.6
    def boom():
        n = int(1.2 * SR); tt = np.arange(n) / SR; f = 38 + 90 * np.exp(-tt * 9)
        return (np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.45) + lp(rng.standard_normal(n), 30) * env(n, 0.001, 0.08) * 0.6)
    def riser(L):
        n = int(L * SR); tt = np.arange(n) / SR; f = 200 + 1800 * (tt / L) ** 2
        return (np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.25 + lp(rng.standard_normal(n), 3) * 0.3) * (tt / L) ** 2
    def tick():
        n = int(0.03 * SR); return rng.standard_normal(n) * env(n, 0.0005, 0.004) * 0.8
    def pop():
        n = int(0.09 * SR); tt = np.arange(n) / SR; f = 900 + 700 * np.exp(-tt * 40)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.001, 0.025)
    for c in CUTS[1:]: put(sfx, whoosh(), c['a'] - 0.22, 0.28)
    for im in IMPACTS: put(sfx, boom(), im, 0.9)
    if DROP: put(sfx, riser(1.2), SEG[DROP]['t0'] - 1.2, 0.5)
    for k_, off, dur in TICKS:
        t0 = SEG[k_]['t0'] + off; tt = 0.0
        while tt < dur: put(sfx, tick(), t0 + tt, 0.35); tt += 0.045 + 0.12 * (tt / dur) ** 2
    # pop for every chip / bar / stamp / text reveal
    for k_, els in CARDS.items():
        for e in els:
            base = SEG[k_]['t0'] + e.get('delay', 0)
            if e['type'] == 'chips':
                for j in range(len(e['items'])): put(sfx, pop(), base + j * e.get('step', 0.35), 0.35)
            elif e['type'] == 'bars':
                for j in range(len(e['items'])): put(sfx, pop(), base + j * e.get('gap', 0.7), 0.35)
            elif e['type'] == 'strike':
                put(sfx, whoosh(0.2), base + e.get('at', 0.6), 0.5)
            elif e['type'] in ('text', 'stamp') and e.get('delay', 0) > 0:
                put(sfx, pop(), base, 0.3)
    BEAT = 0.5; BAR = 4 * BEAT
    def saw(f, n): tt = np.arange(n) / SR; return 2 * ((tt * f) % 1) - 1
    def note(m): return 440 * 2 ** ((m - 69) / 12)
    prog = getattr(sc, 'PROG', 0)
    CH = [[[57, 60, 64], [53, 57, 60], [55, 59, 62], [52, 56, 59]], [[50, 53, 57], [46, 50, 53], [48, 52, 55], [45, 49, 52]], [[52, 55, 59], [48, 52, 55], [50, 54, 57], [47, 51, 54]]][prog % 3]
    RT = [c[0] - 24 for c in CH]
    def addm(sig, t0, g, pan=0.0):
        i = int(t0 * SR)
        if i >= N or i < 0: return
        n = min(len(sig), N - i)
        music[i:i + n, 0] += sig[:n] * g * (1 - max(pan, 0)); music[i:i + n, 1] += sig[:n] * g * (1 + min(pan, 0))
    def kick():
        n = int(0.4 * SR); tt = np.arange(n) / SR; f = 46 + 120 * np.exp(-tt * 32)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.002, 0.16)
    def snare():
        n = int(0.4 * SR); s_ = rng.standard_normal(n) * env(n, 0.001, 0.11)
        return lp(s_, 3) * 0.6 + np.sin(2 * np.pi * 185 * np.arange(n) / SR) * env(n, 0.001, 0.05) * 0.4
    def hat():
        n = int(0.035 * SR); s_ = rng.standard_normal(n); return (s_ - lp(s_, 4)) * env(n, 0.001, 0.01) * 0.3
    gap0, gap1 = (SEG[DROP]['t0'] - 0.2, SEG[DROP]['t1']) if DROP else (-1, -1)
    b, tb = 0, 0.0
    while tb < TOTAL:
        ch, rt = CH[b % 4], RT[b % 4]; n = int(BAR * SR)
        pad = sum(lp(saw(note(m), n) + saw(note(m) * 1.007, n), 50) for m in ch) / 6
        addm(pad * np.minimum(1, np.arange(n) / (0.2 * SR)), tb, 0.3)
        for q in range(16):
            tq = tb + q * BEAT / 4
            if gap0 <= tq < gap1: continue
            if q % 4 == 0: addm(kick(), tq, 0.95)
            if q in (4, 12): addm(snare(), tq, 0.55)
            addm(hat(), tq, 0.9, 0.3 if q % 2 else -0.3)
            if q % 2 == 0:
                m = rt + (12 if (q // 2) % 2 else 0); bn = int(BEAT / 2 * 0.9 * SR)
                addm(lp(saw(note(m), bn), 14) * env(bn, 0.003, 0.11), tq, 0.42)
            arp = ch[q % 3] + 24; an = int(BEAT / 4 * SR)
            addm(np.sign(np.sin(2 * np.pi * note(arp) * np.arange(an) / SR)) * env(an, 0.002, 0.05), tq, 0.045, 0.5 if q % 2 else -0.5)
        b += 1; tb += BAR
    e = np.convolve(np.abs(voice), np.ones(int(0.1 * SR)) / int(0.1 * SR), 'same')
    duck = 1 - 0.7 * np.clip(e / (e.max() * 0.25), 0, 1); music *= duck[:, None]
    mixd = (music * 0.55 + (voice * 1.7 + sfx)[:, None])[: int(TOTAL * SR)]
    fo = int(0.04 * SR); mixd[-fo:] *= np.linspace(1, 0, fo)[:, None]
    mixd = np.tanh(mixd * 0.9); mixd *= 0.95 / np.abs(mixd).max()
    sf.write(OUT + '/mix.wav', mixd, SR)

if MODE == 'preview':
    ts = [s['t0'] + min(1.9, s['vo'] * 0.85) for s in SEGS]
    ims = []
    for tt in ts:
        c = max(j for j, c in enumerate(CUTS) if c['a'] <= tt); fr = load_shot(CUTS[c]); lt = tt - CUTS[c]['a']
        im = frame_from(fr[min(len(fr) - 1, int(lt * FPS))], tt, CUTS[c], lt)
        overlay(ImageDraw.Draw(im), tt); ims.append(im.resize((360, 640)))
    cs = Image.new('RGB', (360 * len(ims), 640)); [cs.paste(im, (i * 360, 0)) for i, im in enumerate(ims)]; cs.save(OUT + '/contact.jpg', quality=85)
    print('total', round(TOTAL, 2), 'cuts', len(CUTS))
elif MODE == 'full':
    build_audio(); render()
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', OUT + '/video.tmp.mp4', '-i', OUT + '/mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy',
                    '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11', '-c:a', 'aac', '-b:a', '192k', '-ar', '44100', '-shortest', OUT + '/final.tmp.mp4'], check=True)
    os.replace(OUT + '/final.tmp.mp4', OUT + '/' + sc.NAME + '.mp4'); print('done', sc.NAME, round(TOTAL, 2))
