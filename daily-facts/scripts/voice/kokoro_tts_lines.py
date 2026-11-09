"""Kokoro TTS, one WAV per script line + word tokens (Derinkuyu / Hanging Gardens).
Input: script.txt with "N|line" rows.  Output: audio/lNN.wav (24 kHz) + audio/lines.json.
Voice af_heart. These videos used speed 0.92 (the S092 voice); since 2026-10-30 the rule is SLOWER
than 0.92, so set KOKORO_SPEED (e.g. 0.86-0.88). Regnal numbers are spelled out for the TTS
("Nebuchadnezzar II" -> "the Second"); add others to FIX.
Each line: trim at -45 dB, 5 ms fades (120 samples), 150 ms silence pad each side."""
import os
import numpy as np, soundfile as sf, json
from kokoro import KPipeline
p=KPipeline(lang_code='a',repo_id='hexgrad/Kokoro-82M'); sr=24000
FIX={'Nebuchadnezzar II':'Nebuchadnezzar the Second'}
def fix(t):
    for a,b in FIX.items(): t=t.replace(a,b)
    return t
L=[fix(l.split('|',1)[1].strip()) for l in open('script.txt') if '|' in l]
out=[]
for i,s in enumerate(L,1):
    auds=[];toks=[];off=0.0
    for r in p(s,voice='af_heart',speed=float(os.environ.get('KOKORO_SPEED','0.88'))):
        a=np.asarray(r.audio); 
        for t in (r.tokens or []):
            if t.start_ts is not None and t.text.strip(): toks.append([t.text,off+t.start_ts,off+(t.end_ts or t.start_ts)])
        auds.append(a); off+=len(a)/sr
    a=np.concatenate(auds)
    e=np.convolve(np.abs(a),np.ones(240)/240,'same'); th=np.abs(a).max()*10**(-45/20); ix=np.where(e>th)[0]
    s0=max(ix[0]-48,0); a=a[s0:min(ix[-1]+48,len(a))].copy(); f=120; a[:f]*=np.linspace(0,1,f); a[-f:]*=np.linspace(1,0,f); P=np.zeros(int(.15*sr)); a=np.concatenate([P,a,P]); s0-=len(P)
    toks=[[w,max(0,b-s0/sr),max(0,c-s0/sr)] for w,b,c in toks]
    sf.write(f'audio/l{i:02d}.wav',a,sr); out.append({'text':s,'dur':len(a)/sr,'toks':toks})
    print(i,round(len(a)/sr,2),len(toks))
json.dump(out,open('audio/lines.json','w'),indent=1)
