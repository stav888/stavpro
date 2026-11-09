import av,numpy as np,cv2,json,sys
# usage: python compare_versions.py OLD.mp4 NEW.mp4  -> cmp.json (per-frame diff; caption band rows 1420-1600 masked)
a=av.open(sys.argv[1]).decode(video=0); b=av.open(sys.argv[2]).decode(video=0)
rows=[];art=[];cap=[];prev6=prev7=None
for i,(f6,f7) in enumerate(zip(a,b)):
  g6=f6.to_ndarray(format='gray').astype(np.float32); g7=f7.to_ndarray(format='gray').astype(np.float32)
  d=np.abs(g6-g7); m=np.ones_like(d,bool); m[1420:1600]=0
  dot=np.zeros_like(m); dot[580:890,400:700]=1
  out=m&~dot
  mse=((g6-g7)[m]**2).mean(); psnr=99 if mse==0 else 10*np.log10(255**2/mse)
  r=dict(i=i,art=float(d[m].mean()),outdot=float(d[out].mean()),dot=float(d[dot].mean()),psnr=float(psnr))
  if prev6 is not None:
    r['me6']=float(np.abs(g6-prev6)[out].mean()); r['me7']=float(np.abs(g7-prev7)[out].mean())
  rows.append(r); art.append(cv2.resize(g7[200:1400],(360,400))); cap.append(g7[1420:1600].mean(1))
  prev6,prev7=g6,g7
np.save('art.npy',np.array(art)); np.save('cap.npy',np.array(cap)); json.dump(rows,open('cmp.json','w'))
