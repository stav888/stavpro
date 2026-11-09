#!/usr/bin/env python3
"""Join per-line Kokoro WAVs into ONE continuous narration and normalise it.

Rebuilt to the exact spec of the Derinkuyu "fixed narration" pass (the original one-off script
was not kept; its QA report is in examples/derinkuyu/narration_report.json):
  * gap between lines           GAP      = 0.40 s
  * internal pauses inside a line (commas, "...") capped to ~0.20 s (INTERNAL)
  * each line already carries 150 ms pads + 5 ms fades from kokoro_tts_lines.py; they are trimmed
    here and the exact gap is re-inserted, so every line boundary is identical
  * loudnorm I=-16 LUFS, TP=-1.5 dBTP, LRA=11, 48 kHz
  * writes a JSON report with the measured gaps + loudness (send it to the QA bot)

Usage: python3 join_narration.py audio/l??.wav -o audio/narration.wav
"""
import argparse, json, subprocess, sys
import numpy as np, soundfile as sf

ap = argparse.ArgumentParser()
ap.add_argument('wavs', nargs='+'); ap.add_argument('-o', '--out', required=True)
ap.add_argument('--gap', type=float, default=0.40); ap.add_argument('--internal', type=float, default=0.20)
ap.add_argument('--lufs', type=float, default=-16.0)
a = ap.parse_args()

def env_db(x, sr, win=0.01):
    n = int(sr * win); e = np.convolve(x ** 2, np.ones(n) / n, 'same'); return 10 * np.log10(e + 1e-12)

def silences(x, sr, thr_db=-45, min_len=0.12):
    """(start, end) sample ranges of silence longer than min_len, relative to peak."""
    db = env_db(x, sr) - 20 * np.log10(np.abs(x).max() + 1e-9)
    q = db < thr_db; out = []; i = 0
    while i < len(q):
        if q[i]:
            j = i
            while j < len(q) and q[j]: j += 1
            if (j - i) / sr >= min_len: out.append((i, j))
            i = j
        else: i += 1
    return out

def fade(x, n):
    n = min(n, len(x) // 2)
    if n > 0: x[:n] *= np.linspace(0, 1, n); x[-n:] *= np.linspace(1, 0, n)
    return x

lines, sr = [], None
for p in a.wavs:
    x, s = sf.read(p, dtype='float32')
    if x.ndim > 1: x = x.mean(1)
    sr = sr or s
    sil = silences(x, sr)
    # trim head/tail silence
    st = sil[0][1] if sil and sil[0][0] == 0 else 0
    en = sil[-1][0] if sil and sil[-1][1] >= len(x) - 1 else len(x)
    core = x[st:en]
    # cap internal pauses
    pieces, last, gaps = [], 0, []
    for s0, s1 in silences(core, sr):
        if s0 == 0 or s1 >= len(core): continue
        keep = int(min(a.internal, (s1 - s0) / sr) * sr)
        pieces.append(core[last:s0]); pieces.append(np.zeros(keep, np.float32)); last = s1; gaps.append(keep / sr)
    pieces.append(core[last:])
    lines.append((fade(np.concatenate(pieces), int(0.005 * sr)), gaps))

G = np.zeros(int(a.gap * sr), np.float32)
head = np.zeros(int(0.15 * sr), np.float32)
y = np.concatenate([head] + sum([[l, G] for l, _ in lines], [])[:-1] + [head])
raw = a.out.rsplit('.', 1)[0] + '_prenorm.wav'; sf.write(raw, y, sr)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af',
                f'loudnorm=I={a.lufs}:TP=-1.5:LRA=11', '-ar', '48000', a.out], check=True)
m = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', a.out, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                   capture_output=True, text=True).stderr
I = float(m.rsplit('I:', 1)[1].split('LUFS')[0]); TP = float(m.rsplit('Peak:', 1)[1].split('dBFS')[0])
rep = {'out': a.out, 'duration_s': round(len(y) / sr, 3), 'lufs_integrated': I, 'true_peak_dbtp': TP,
       'inter_sentence_gap_s': a.gap, 'internal_clause_gaps_s': [round(g, 3) for _, gs in lines for g in gs]}
json.dump(rep, open(a.out.rsplit('.', 1)[0] + '_REPORT.json', 'w'), indent=1); print(json.dumps(rep))
