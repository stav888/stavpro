import soundfile as sf,numpy as np,subprocess,sys
src,dst=sys.argv[1],sys.argv[2]
subprocess.run(["ffmpeg","-y","-v","error","-i",src,"-af","loudnorm=I=-16:TP=-1.5:LRA=11","-ar","48000","/tmp/ln.wav"],check=True)
c,sr=sf.read('/tmp/ln.wav'); c=c.mean(1) if c.ndim>1 else c; hop=int(.01*sr)
db=np.array([20*np.log10(np.sqrt(np.mean(c[i:i+hop]**2))+1e-9) for i in range(0,len(c)-hop,hop)])
last=np.where(db>-45)[0].max(); end=min(len(c),(last+1)*hop+int(.15*sr)); c=c[:end].copy(); db=db[:end//hop]
g=np.ones(len(db)); quiet=db<-40; i=0; regs=[]
while i<len(db):
  if quiet[i]:
    j=i
    while j<len(db) and quiet[j]: j+=1
    if j-i>=15 and i>5: regs.append((i+3,j-3)); g[i+3:j-3]=0
    i=j
  else: i+=1
env=np.repeat(g,hop); env=np.concatenate([env,np.ones(len(c)-len(env))]); k=int(.01*sr); env=np.convolve(env,np.ones(k)/k,mode='same'); c*=env
f=int(.03*sr); c[-f:]*=np.linspace(1,0,f)
c=np.concatenate([np.zeros(int(.15*sr)),c]); sf.write(dst,c,sr)
print('len',round(len(c)/sr,2),'gated',len(regs),'last speech',round((last+1)/100,2))
