import torchaudio as ta, torch, perth, sys
if perth.PerthImplicitWatermarker is None: perth.PerthImplicitWatermarker=perth.DummyWatermarker
from chatterbox.tts import ChatterboxTTS
m=ChatterboxTTS.from_pretrained(device="cpu")
_inf=m.t3.inference
def inf(*a,**k):
    k["max_new_tokens"]=4500; return _inf(*a,**k)
m.t3.inference=inf
P=open(sys.argv[4] if len(sys.argv)>4 else "script.txt").read().strip()
seed=int(sys.argv[1]); torch.manual_seed(seed)
w=m.generate(P,audio_prompt_path="k_am_eric.wav",exaggeration=float(sys.argv[2]),cfg_weight=float(sys.argv[3]))
ta.save(f"full_g_{seed}_{sys.argv[2]}_{sys.argv[3]}.wav",w,m.sr); print("done",w.shape[-1]/m.sr,flush=True)
