"""Word timestamps for the karaoke highlight (Hanging Gardens).
faster-whisper small.en on each narration line, aligned to the script words with difflib;
missing words fall back to Kokoro token times. Output: audio/whisper_words.json.
Rule since Derinkuyu: run the final check on the FINAL MIXED audio (qa/verify_subtitle_sync.py)
and make sure the highlight is not early at sentence starts."""
import json,re,difflib
from faster_whisper import WhisperModel
m=WhisperModel('small.en',device='cpu',compute_type='int8')
D=json.load(open('audio/lines.json')); out=[]
n=lambda w:re.sub(r'[^a-z0-9]','',w.lower())
for k,d in enumerate(D):
    words=[w for w in d['text'].split() if re.search(r'\w',w)]
    import subprocess,numpy as np
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f'audio/l{k+1:02d}.wav','-f','f32le','-ac','1','-ar','16000','-'],capture_output=True).stdout,np.float32)
    segs,_=m.transcribe(a,word_timestamps=True,language='en',beam_size=5)
    ww=[(w.word,w.start,w.end) for s in segs for w in s.words]
    tk=[t for t in d['toks'] if re.search(r'\w',t[0])]
    res=[None]*len(words)
    sm=difflib.SequenceMatcher(None,[n(w) for w in words],[n(w[0]) for w in ww])
    for a,b,sz in sm.get_matching_blocks():
        for i in range(sz): res[a+i]=list(ww[b+i][1:])
    for op,a1,a2,b1,b2 in sm.get_opcodes():
        if op=='replace' and a2-a1==b2-b1:
            for i in range(a2-a1): res[a1+i]=list(ww[b1+i][1:])
    miss=[i for i,r in enumerate(res) if r is None]
    for i in miss: res[i]=[tk[i][1],tk[i][2]]  # fallback to TTS token
    print(k+1,'miss',[words[i] for i in miss],'|',' '.join(w[0] for w in ww))
    out.append(res)
json.dump(out,open('audio/whisper_words.json','w'))
