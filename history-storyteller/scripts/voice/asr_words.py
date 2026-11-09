import numpy as np,json,sys,subprocess
from faster_whisper import WhisperModel
src=sys.argv[1]
subprocess.run(["ffmpeg","-y","-v","error","-i",src,"-ac","1","-ar","16000","-f","f32le","/tmp/t16.raw"],check=True)
a=np.fromfile('/tmp/t16.raw',np.float32)
m=WhisperModel('small',device='cpu',compute_type='int8')
s,i=m.transcribe(a,language='en',word_timestamps=True,condition_on_previous_text=False)
ws=[(w.word.strip(),round(w.start,2),round(w.end,2)) for x in s for w in x.words]
print(' '.join(w[0] for w in ws)); json.dump(ws,open(sys.argv[2],'w'))
print([(ws[k][0],ws[k+1][0],ws[k][2],round(ws[k+1][1]-ws[k][2],2)) for k in range(len(ws)-1) if ws[k+1][1]-ws[k][2]>0.45])
