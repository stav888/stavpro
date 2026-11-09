"""Derinkuyu editor (720x1280). 7 Flow clips (each a start+end frame pair = 2 script lines)
retimed to the narration (line boundaries found by RMS on the fixed narration), xfade 0.5 s,
ASS karaoke subtitles (\\k word timing from Kokoro tokens scaled to the measured speech span),
clip audio ducked by sidechaincompress under the voice. Faster and simpler than
build_highlight_wash.py, but the themed transitions are only plain fades here."""
#!/usr/bin/env python3
"""Assemble Derinkuyu full 7-clip video with fixed narration.
Usage: python3 build_full_fixed.py [out.mp4]
Defaults to final/derinkuyu_full.mp4
"""
import json, subprocess, wave, sys, os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1] if len(sys.argv) > 1 else 'final/derinkuyu_full.mp4'
path = 'audio/derinkuyu_full_narration_fixed.wav'
N, X, MARGIN_V = 7, 0.5, 128

w = wave.open(path); sr = w.getframerate(); nch = w.getnchannels(); n = w.getnframes()
raw = w.readframes(n); w.close()
x = np.frombuffer(raw, dtype=np.int16).astype(np.float32)
if nch == 2: x = x.reshape(-1, 2).mean(1)
x /= 32768.0
hop = int(sr * 0.01); win = int(sr * 0.02)
rms = np.array([np.sqrt(np.mean(x[i:i+win]**2)) for i in range(0, len(x)-win, hop)])
speech = rms > 0.02
min_gap = int(0.28 / 0.01)
regions = []; i = 0
while i < len(speech):
    if speech[i]:
        j = i
        while j < len(speech) and speech[j]: j += 1
        regions.append([i, j]); i = j
    else:
        i += 1
merged = []
for a, b in regions:
    if merged and a - merged[-1][1] < min_gap:
        merged[-1][1] = b
    else:
        merged.append([a, b])
assert len(merged) == 14, len(merged)
lines_t = [(a * 0.01, b * 0.01) for a, b in merged]
total = n / sr

bounds = [0.0]
for i in range(1, N):
    bounds.append((lines_t[2*i-1][1] + lines_t[2*i][0]) / 2)
bounds.append(total)
S = [bounds[i+1] - bounds[i] for i in range(N)]
scenes = [S[i] + (X if i < N-1 else 0) for i in range(N)]

L = json.load(open('audio/lines.json'))

def ts(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

ass = ["[Script Info]", "PlayResX: 720", "PlayResY: 1280", "", "[V4+ Styles]",
       "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV",
       f"Style: D,DejaVu Sans,46,&H00FFFF00,&H00FFFFFF,&H00000000,&H80000000,1,1,4,1,2,60,60,{MARGIN_V}", "",
       "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i, ln in enumerate(L):
    st, en = lines_t[i]
    speech_dur = en - st
    scale = speech_dur / max(0.01, ln['dur'])
    tk = ln['toks']
    if any(any(c.isalnum() for c in w[0]) for w in tk):
        txt = ""
        for j, (w, b, c) in enumerate(tk):
            nb = tk[j+1][1] if j+1 < len(tk) else ln['dur']
            cs = max(1, int(round((nb - b) * scale * 100))) if j else max(1, int(round(nb * scale * 100)))
            sep = "" if not any(ch.isalnum() for ch in w) else " "
            txt += ("{\\k%d}" % cs) + (sep if txt else "") + w
    else:
        txt = ln['text']
    ass.append(f"Dialogue: 0,{ts(st)},{ts(en+0.12)},D,,0,0,0,,{txt}")
os.makedirs('final', exist_ok=True)
open('final/subs.ass', 'w').write("\n".join(ass))

inp = []; fc = []
for i in range(N):
    inp += ['-i', f'clips/clip{i+1:02d}.mp4']
    f = scenes[i] / 7.9
    tempo = 1 / f
    tempos = []
    t = tempo
    while t > 2.0: tempos.append(2.0); t /= 2.0
    while t < 0.5: tempos.append(0.5); t /= 0.5
    tempos.append(t)
    atempo = ','.join(f'atempo={tt:.6f}' for tt in tempos)
    fc.append(f"[{i}:v]trim=0:7.9,setpts=PTS-STARTPTS,setpts={f:.6f}*PTS,fps=24,scale=720:1280,setsar=1,format=yuv420p[v{i}]")
    fc.append(f"[{i}:a]atrim=0:7.9,asetpts=PTS-STARTPTS,{atempo},apad,atrim=0:{scenes[i]:.3f},volume=0.18[ca{i}]")
cur = 'v0'; off = 0.0
for i in range(1, N):
    off += scenes[i-1] - X
    fc.append(f"[{cur}][v{i}]xfade=transition=fade:duration={X}:offset={off:.3f}[x{i}]")
    cur = f'x{i}'
fc.append(f"[{cur}]ass=final/subs.ass[vout]")
fc.append(''.join(f'[ca{i}]' for i in range(N)) + f'concat=n={N}:v=0:a=1,aresample=48000,aformat=channel_layouts=stereo[amb]')
nar_idx = N
inp += ['-i', path]
fc.append(f'[{nar_idx}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{total:.3f},asetpts=PTS-STARTPTS[nar]')
fc.append('[nar]asplit[nar1][sc]')
fc.append('[amb][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=300[duck]')
fc.append(f'[nar1][duck]amix=inputs=2:normalize=0,atrim=0:{total:.3f}[aout]')
subprocess.run(['ffmpeg', '-y', *inp, '-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', '[aout]',
                '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-b:a', '192k',
                '-t', f'{total:.3f}', out], check=True)
print(out, total)
