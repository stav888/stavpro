import subprocess,numpy as np,sys
TH=float(__import__("os").environ.get("TH","0.1"))
for p in sys.argv[1:]:
    raw=subprocess.run(["ffmpeg","-v","error","-i",p,"-vf","scale=320:240,format=gray","-f","rawvideo","-"],capture_output=True).stdout
    f=np.frombuffer(raw,np.uint8).reshape(-1,240,320).astype(np.int16)
    d=np.abs(np.diff(f,axis=0)).mean(axis=(1,2))
    runs=[];s=None
    for i,x in enumerate(d):
        if x<TH:
            s=i if s is None else s
        else:
            if s is not None and i-s>=5: runs.append((round(s/24,2),round(i/24,2)))
            s=None
    if s is not None and len(d)-s>=5: runs.append((round(s/24,2),'end'))
    print(p,len(f),runs)
