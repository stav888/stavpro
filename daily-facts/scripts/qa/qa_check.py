#!/usr/bin/env python3
"""Automatic pre-checks for the Daily Facts Arete QA gates. They do NOT replace the QA bot
watching the video; they catch the measurable faults first and give QA numbers to look at.

  clip  CLIP.mp4 [--start partN_start.png --end partN_end.png]
        9:16, duration <= 8.1 s, frozen stretches (ffmpeg freezedetect), first/last frame vs the
        start/end pair (mean abs diff on a 90x160 grey thumbnail; lower = closer)
  seam  PART_N.mp4 PART_N1.mp4 [--continuous]
        last frame of part N vs first frame of part N+1; with --continuous (part N+1 starts from
        part N's end frame) a jump is a FAIL, otherwise it is only reported (themed transition)
  sharp SRC_480.mp4 UP_720.mp4
        sharpness (Laplacian variance) before/after upscale + fine-grain energy (watercolor
        paper grain kept?) on the middle frame
  video FINAL.mp4 [--narration narration.wav]
        9:16, loudness (ebur128 integrated LUFS, true peak), frozen stretches, audio streams,
        and with --narration: source-audio leak = level of the final mix inside the narration's
        pauses (should be near silence)
Exit code 1 if any FAIL. Thresholds are starting values; QA decides on the WARNs.
"""
import argparse, json, re, subprocess, sys
import numpy as np

FAILS, WARNS = [], []
def ok(m): print('  PASS', m)
def warn(m): WARNS.append(m); print('  WARN', m)
def fail(m): FAILS.append(m); print('  FAIL', m)
def run(*a): return subprocess.run(a, capture_output=True, text=True)

def probe(p):
    j = json.loads(run('ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', p).stdout)
    v = next(s for s in j['streams'] if s['codec_type'] == 'video')
    return int(v['width']), int(v['height']), float(j['format']['duration']), [s for s in j['streams'] if s['codec_type'] == 'audio']

def frame(p, where, w=90, h=160):
    args = ['ffmpeg', '-v', 'error'] + (['-sseof', '-0.15'] if where == 'last' else ['-ss', str(where)] if where != 'first' else []) + \
           ['-i', p, '-frames:v', '1', '-vf', f'scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-']
    b = subprocess.run(args, capture_output=True).stdout
    return np.frombuffer(b[:w * h], np.uint8).reshape(h, w).astype(np.float32)

def image(p, w=90, h=160):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-vf', f'scale={w}:{h}', '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True).stdout
    return np.frombuffer(b[:w * h], np.uint8).reshape(h, w).astype(np.float32)

def aspect(p):
    w, h, d, a = probe(p)
    (ok if h > w else fail)(f'aspect {w}x{h} ' + ('(9:16 vertical)' if h > w else 'NOT vertical'))
    return w, h, d, a

def freeze(p, dur, min_s=0.8):
    e = run('ffmpeg', '-hide_banner', '-i', p, '-vf', f'freezedetect=n=0.002:d={min_s}', '-map', '0:v', '-f', 'null', '-').stderr
    st = [float(x) for x in re.findall(r'freeze_start: ([\d.]+)', e)]; en = [float(x) for x in re.findall(r'freeze_end: ([\d.]+)', e)]
    en += [dur] * (len(st) - len(en))
    runs = [(a, b) for a, b in zip(st, en)]
    if not runs: ok(f'no frozen stretch >= {min_s}s')
    for a, b in runs: (fail if b - a >= 1.5 else warn)(f'frozen {a:.2f}-{b:.2f}s ({b-a:.2f}s)')

def diff(a, b): return float(np.abs(a - b).mean())

ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest='cmd', required=True)
c = sp.add_parser('clip'); c.add_argument('clip'); c.add_argument('--start'); c.add_argument('--end')
s = sp.add_parser('seam'); s.add_argument('a'); s.add_argument('b'); s.add_argument('--continuous', action='store_true', help='part N+1 starts from part N end frame')
h = sp.add_parser('sharp'); h.add_argument('src'); h.add_argument('up')
v = sp.add_parser('video'); v.add_argument('video'); v.add_argument('--narration'); v.add_argument('--lufs', type=float, default=-16.0)
a = ap.parse_args()

if a.cmd == 'clip':
    print('CLIP', a.clip); w, hh, d, _ = aspect(a.clip)
    (ok if d <= 8.1 else fail)(f'duration {d:.2f}s (max 8 s per part)')
    freeze(a.clip, d)
    for img, where, name in ((a.start, 'first', 'start'), (a.end, 'last', 'end')):
        if img:
            x = diff(frame(a.clip, where), image(img)); (ok if x < 18 else warn if x < 30 else fail)(f'{where} frame vs {name} image: diff {x:.1f}')
elif a.cmd == 'seam':
    print('SEAM', a.a, '->', a.b); x = diff(frame(a.a, 'last'), frame(a.b, 'first'))
    if a.continuous: (ok if x < 15 else warn if x < 30 else fail)(f'continuous cut: part end vs next part start diff {x:.1f} (should be ~0-15)')
    else: ok(f'scene change (themed transition expected): diff {x:.1f}; QA checks the transition by eye')
elif a.cmd == 'sharp':
    print('SHARP', a.src, '->', a.up)
    _, _, d, _ = aspect(a.up); w, hh = 720, 1280
    def stats(p):
        f = frame(p, d / 2, w, hh)
        lap = f[1:-1, 1:-1] * 4 - f[:-2, 1:-1] - f[2:, 1:-1] - f[1:-1, :-2] - f[1:-1, 2:]
        blur = np.convolve(f.ravel(), np.ones(5) / 5, 'same').reshape(f.shape)
        return float(lap.var()), float(np.abs(f - blur).mean())
    (s0, g0), (s1, g1) = stats(a.src), stats(a.up)
    (ok if s1 >= s0 * 1.1 else warn)(f'sharpness (Laplacian var) {s0:.0f} -> {s1:.0f}')
    (ok if g1 >= g0 * 0.7 else warn)(f'fine grain {g0:.2f} -> {g1:.2f} (below 70% = washes may look plastic: raise PAPER_MIX)')
else:
    print('VIDEO', a.video); w, hh, d, aud = aspect(a.video)
    (ok if len(aud) == 1 else fail)(f'{len(aud)} audio stream(s)')
    e = run('ffmpeg', '-hide_banner', '-nostats', '-i', a.video, '-af', 'ebur128=peak=true', '-f', 'null', '-').stderr
    I = float(e.rsplit('I:', 1)[1].split('LUFS')[0]); TP = float(e.rsplit('Peak:', 1)[1].split('dBFS')[0])
    (ok if abs(I - a.lufs) <= 1.5 else fail)(f'integrated loudness {I:.1f} LUFS (target ~{a.lufs:.0f})')
    (ok if TP <= -1.0 else warn)(f'true peak {TP:.1f} dBTP')
    freeze(a.video, d, 1.0)
    if a.narration:
        def pcm(p):
            return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], capture_output=True).stdout, np.float32)
        n, m = pcm(a.narration), pcm(a.video); L = min(len(n), len(m)); win = 1600
        rn = np.array([np.sqrt(np.mean(n[i:i + win] ** 2)) for i in range(0, L - win, win)]) + 1e-9
        rm = np.array([np.sqrt(np.mean(m[i:i + win] ** 2)) for i in range(0, L - win, win)]) + 1e-9
        quiet = 20 * np.log10(rn / rn.max()) < -45
        if quiet.sum() < 3: warn('narration has almost no pauses to test for source-audio leak (check alignment)')
        else:
            lvl = 20 * np.log10(np.median(rm[quiet]))
            (ok if lvl < -50 else warn if lvl < -40 else fail)(f'mix level inside narration pauses {lvl:.1f} dBFS (source-audio leak if high)')
print(f'RESULT: {"FAIL" if FAILS else "PASS"} ({len(FAILS)} fail, {len(WARNS)} warn)')
sys.exit(1 if FAILS else 0)
