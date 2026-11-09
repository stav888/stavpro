from kokoro import KPipeline
import soundfile as sf, numpy as np
T="In the nineteen eighties... an inventor from Ohio, named Stanley Meyer, built a small dune buggy. He made an incredible claim: it could run on nothing... but water. Investors believed him. But the truth, was far stranger."
for lc,vs in [('a',['am_adam','am_echo','am_eric','am_liam','am_onyx','am_michael','am_fenrir','am_puck']),('b',['bm_george','bm_lewis','bm_daniel','bm_fable'])]:
    p=KPipeline(lang_code=lc, repo_id='hexgrad/Kokoro-82M')
    for v in vs:
        a=np.concatenate([x[2] for x in p(T,voice=v,speed=1.0)]); sf.write(f'k_{v}.wav',a,24000); print(v,flush=True)
