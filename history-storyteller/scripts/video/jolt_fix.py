import sys,torch,numpy as np,av,shutil
import os; sys.path.insert(0,os.environ.get('CFI_RIFE_DIR','/tmp/cfi/vfi_models/rife')); from rife_arch import IFNet
m=IFNet(arch_ver="4.7"); m.load_state_dict(torch.load(os.environ.get('RIFE47_WEIGHTS','rife47.pth'),weights_only=False)); m.eval()
def pc(a,b):
  A=np.fft.fft2(a);B=np.fft.fft2(b);R=A*np.conj(B);R/=np.abs(R)+1e-9;c=np.abs(np.fft.ifft2(R))
  y,x=np.unravel_index(c.argmax(),c.shape); h,w=c.shape
  def par(v,i,n): l,cc,r=v[(i-1)%n],v[i],v[(i+1)%n]; return i+(l-r)/(2*(l-2*cc+r)+1e-12)
  py=par(c[:,x],y,h); px=par(c[y,:],x,w); py=py-h if py>h/2 else py; px=px-w if px>w/2 else px
  return np.array([-px,-py])
for p in sys.argv[1:]:
  ims=[x.to_ndarray(format='rgb24') for x in av.open(p).decode(video=0)]
  G=[x.mean(2) for x in ims]
  s=np.array([pc(G[n-1],G[n]) for n in range(1,len(G))])  # s[n-1]: shift n-1->n
  bad=[n for n in range(1,len(G)-1) if np.hypot(*s[n-1])>0.4 and np.hypot(*(s[n-1]+s[n]))<0.25]
  print(p,'jolts',bad,[np.round(s[n-1],2).tolist() for n in bad])
  if not bad: continue
  H,W=ims[0].shape[:2]; ph,pw=(32-H%32)%32,(32-W%32)%32
  P=lambda x: torch.from_numpy(np.pad(x,((0,ph),(0,pw),(0,0)),mode='edge')).permute(2,0,1)[None].float()/255
  for n in bad:
    with torch.no_grad(): r=m(P(ims[n-1]),P(ims[n+1]),torch.tensor([[[[0.5]]]]),[8,4,2,1],False,True).clamp(0,1)
    ims[n]=(r[0].permute(1,2,0).numpy()*255).round().astype(np.uint8)[:H,:W]
  shutil.copy(p,p.replace('_r.mp4','_prejolt.mp4'))
  o=av.open(p,'w'); st=o.add_stream('libx264',rate=24); st.width=W;st.height=H;st.pix_fmt='yuv420p'; st.options={'crf':'14'}
  for x in ims:
    for q in st.encode(av.VideoFrame.from_ndarray(x,format='rgb24')): o.mux(q)
  for q in st.encode(): o.mux(q)
  o.close()
  G=[x.mean(2) for x in ims]; s=np.array([pc(G[n-1],G[n]) for n in range(1,len(G))])
  print(' after',[n for n in range(1,len(G)-1) if np.hypot(*s[n-1])>0.4 and np.hypot(*(s[n-1]+s[n]))<0.25])
