import torchaudio as ta, torch, perth
if perth.PerthImplicitWatermarker is None: perth.PerthImplicitWatermarker=perth.DummyWatermarker
from chatterbox.tts import ChatterboxTTS
m=ChatterboxTTS.from_pretrained(device="cpu")
for i in range(1,5):
    torch.manual_seed(7)
    w=m.generate(open(f"p{i}.txt").read().strip(),audio_prompt_path="k_am_eric.wav",exaggeration=0.6,cfg_weight=0.45)
    ta.save(f"p{i}.wav",w,m.sr); print("done",i,w.shape[-1]/m.sr,flush=True)
