"""QA: re-transcribe the FINAL rendered video with faster-whisper medium.en and compare every
highlighted word's on-screen frame with the spoken word time. Prints median/mean/max offset in
frames (24 fps) and the worst words. Target: |offset| <= 2 frames, never early at sentence starts.
Usage: python verify_subtitle_sync.py FINAL.mp4 [subs.json]; edit the spot-check times (sentence starts) per video."""
import json,re,subprocess,sys,numpy as np,difflib
VIDEO=sys.argv[1] if len(sys.argv)>1 else 'final/hanging_gardens_final.mp4'; SUBS=sys.argv[2] if len(sys.argv)>2 else 'final/subs.json'
from faster_whisper import WhisperModel
m=WhisperModel('medium.en',device='cpu',compute_type='int8')
a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',VIDEO,'-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.float32)
ww=[(w.word,w.start) for s in m.transcribe(a,word_timestamps=True,language='en')[0] for w in s.words]
S=json.load(open(SUBS)); on=[]
for f0,f1,ws,hi in S:
    if not on or on[-1][1]!=(tuple(ws),hi) : on.append((f0,(tuple(ws),hi),ws[hi]))
n=lambda w:re.sub(r'[^a-z0-9]','',w.lower())
sm=difflib.SequenceMatcher(None,[n(x[2]) for x in on],[n(x[0]) for x in ww]); off=[]
for A,B,z in sm.get_matching_blocks():
    for i in range(z): off.append((on[i+A][0]-ww[B+i][1]*24, on[i+A][2], ww[B+i][1]))
o=np.array([x[0] for x in off]); print('matched',len(o),'of',len(on),'median %.2f mean %.2f maxabs %.2f within2 %.0f%%'%(np.median(o),o.mean(),np.abs(o).max(),100*np.mean(np.abs(o)<=2)))
for x in sorted(off,key=lambda x:-abs(x[0]))[:8]: print('%.1f fr'%x[0],x[1],'%.2f'%x[2])
for t in [14.79,22.24,26.28,30.91,35.67,39.91,49.12,58.49,63.11,2.58]:
    x=min(off,key=lambda x:abs(x[2]-t)); print('check',x[1],'%.2f'%x[2],'%.1f fr'%x[0])
