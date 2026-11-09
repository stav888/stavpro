import numpy as np,soundfile as sf
a,sr=sf.read('full_v4_7_0.4_0.3.wav'); a=a if a.ndim==1 else a.mean(1)
hop=int(.01*sr); db=np.array([20*np.log10(np.sqrt(np.mean(a[i:i+hop]**2))+1e-9) for i in range(0,len(a)-hop,hop)])
sil=db<-45; gaps=[];s=None
for i,x in enumerate(sil):
  if x and s is None: s=i
  if not x and s is not None:
    if i-s>=15 and s>0: gaps.append((s,i))
    s=None
out=[];prev=0;added=0;log=[]
for s,e in gaps:
  L=(e-s)/100; ext=0.42 if L>=0.38 else 0.2
  mid=((s+e)//2)*hop; out+= [a[prev:mid], np.zeros(int(ext*sr))]; prev=mid; added+=ext; log.append((round(s/100,2),round(L,2),ext))
out.append(a[prev:]); b=np.concatenate(out)
b=np.concatenate([np.zeros(int(.2*sr)),b,np.zeros(int(.8*sr))])
sf.write('full_v4_breath.wav',b,sr); print(len(gaps),'gaps added',round(added,2),'s total',round(len(b)/sr,2)); print(log)
