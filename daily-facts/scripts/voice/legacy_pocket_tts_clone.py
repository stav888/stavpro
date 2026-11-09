"""LEGACY (Petra era, before 2026-10-24): Pocket TTS voice clone of the channel narrator.
Picks the best of 4 seeds by ASR match (>=0.85) and speaker similarity (Resemblyzer), then atempo 0.9.
Replaced by Kokoro af_heart (kokoro_tts_lines.py). Kept for reference."""
import numpy as np, librosa, soundfile as sf, re, torch, subprocess
from resemblyzer import VoiceEncoder, preprocess_wav
from faster_whisper import WhisperModel
from pocket_tts import TTSModel
import os
REF=os.environ['REF_WAV']  # clean 10-20 s clip of the channel's original narration voice
O=os.environ.get('STORY_DIR','.').rstrip('/')+'/'
S=[open(O+"script_full_en.txt").read().replace("\n"," ").strip()]
_X=["Two thousand years ago, deep in a silent desert, the Nabataeans carved an entire city into rose-red cliffs, and the only way in was a narrow, shadowed canyon that wound deeper and deeper into the stone, where the light slowly faded and every footstep echoed, until suddenly, like a dream, the Treasury rose before them, carved straight into the mountain."]
enc=VoiceEncoder(); asr=WhisperModel('small.en',compute_type='int8'); tgt=enc.embed_utterance(preprocess_wav(REF))
norm=lambda s:re.sub(r"[^a-z0-9 ]"," ",s.lower().replace("'","").replace("-"," ")).split()
def ok(y,s):
    h=norm(' '.join(w.word for g in asr.transcribe(librosa.resample(y,orig_sr=24000,target_sr=16000),word_timestamps=True)[0] for w in g.words))
    print('  asr:',' '.join(h)); import difflib; r=difflib.SequenceMatcher(None,h,norm(s)).ratio(); return r>=0.85
def trim(y):
    i=np.where(np.abs(y)>0.01)[0]; return y[max(0,i[0]-1200):i[-1]+9600]
m=TTSModel.load_model(temp=0.6); st=m.get_state_for_audio_prompt(REF); parts=[]
for s in S:
    best=None
    for seed in range(4):
        torch.manual_seed(seed); a=trim(m.generate_audio(st,s,copy_state=True).numpy())
        if not ok(a,s): continue
        sf.write('/tmp/p.wav',a,24000); e=enc.embed_utterance(preprocess_wav('/tmp/p.wav')); sc=float(e@tgt/np.linalg.norm(e)/np.linalg.norm(tgt))
        if best is None or sc>best[0]: best=(sc,a)
    print(s, best and best[0]); parts.append(best[1] if best else a)
for k,y in enumerate(parts):
    y=np.concatenate([np.zeros(1200,np.float32),y]); sf.write(O+f"full{k+1}_raw.wav",y,24000)
    subprocess.run(f"ffmpeg -y -v error -i {O}full{k+1}_raw.wav -af 'atempo=0.9' -ar 48000 {O}full{k+1}.wav",shell=True,check=True)
