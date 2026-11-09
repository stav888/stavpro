import subprocess,numpy as np,sys
V=sys.argv[1];W,H=540,960
cuts=[0.0, 5.583333333333333, 10.75, 18.5, 23.541666666666668, 26.958333333333332, 29.625, 33.541666666666664, 39.666666666666664, 43.125, 47.541666666666664, 51.59]
raw=subprocess.run(["ffmpeg","-v","error","-i",V,"-vf",f"scale={W}:{H},format=gray","-f","rawvideo","-"],capture_output=True).stdout
f=np.frombuffer(raw,np.uint8).reshape(-1,H,W).astype(np.int16)
d=np.abs(np.diff(f,axis=0)).mean(axis=(1,2))
# exact-ish dup on full frame
for th in (0.1,0.25,0.5):
  out=[]
  for i in range(len(cuts)-1):
    a,b=round(cuts[i]*24),min(round(cuts[i+1]*24),len(d))
    s=d[a:b-1]; dup=s<th
    run=m=0
    for x in dup: run=run+1 if x else 0; m=max(m,run)
    out.append(f"{i+1}:{100*dup.mean():.1f}%/{m/24:.2f}s")
  print("th",th," ".join(out))
print("frames",len(f))
