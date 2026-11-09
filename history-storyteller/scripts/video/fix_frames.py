import sys,torch,numpy as np,av
import os; sys.path.insert(0,os.environ.get('CFI_RIFE_DIR','/tmp/cfi/vfi_models/rife')); from rife_arch import IFNet
m=IFNet(arch_ver="4.7"); m.load_state_dict(torch.load(os.environ.get('RIFE47_WEIGHTS','rife47.pth'),weights_only=False)); m.eval()
ims=[x.to_ndarray(format='rgb24') for x in av.open(sys.argv[1]).decode(video=0)]
def sh(a,b,reg=(230,400,500,640)):
  y0,y1,x0,x1=reg; g=lambda x: x.mean(2)[y0:y1,x0:x1]
  A=np.fft.fft2(g(a));B=np.fft.fft2(g(b));R=A*np.conj(B);R/=np.abs(R)+1e-9;c=np.abs(np.fft.ifft2(R))
  # upsampled peak via parabolic
  y,x=np.unravel_index(c.argmax(),c.shape); h,w=c.shape
  def par(m,i,n): 
    l,cc,r=m[(i-1)%n],m[i],m[(i+1)%n]; d=(l-r)/(2*(l-2*cc+r)+1e-12); return i+d
  py=par(c[:,x],y,h); px=par(c[y,:],x,w)
  py=py-h if py>h/2 else py; px=px-w if px>w/2 else px
  return np.round([-px,-py],2)

H,W=ims[0].shape[:2]; ph,pw=(32-H%32)%32,(32-W%32)%32
P=lambda x: torch.from_numpy(np.pad(x,((0,ph),(0,pw),(0,0)),mode='edge')).permute(2,0,1)[None].float()/255
for n in map(int,sys.argv[3:]):
  with torch.no_grad(): r=m(P(ims[n-1]),P(ims[n+1]),torch.tensor([[[[0.5]]]]),[8,4,2,1],False,True).clamp(0,1)
  ims[n]=(r[0].permute(1,2,0).numpy()*255).round().astype(np.uint8)[:H,:W]

o=av.open(sys.argv[2],'w'); s=o.add_stream('libx264',rate=24); s.width=W;s.height=H;s.pix_fmt='yuv420p'; s.options={'crf':'14'}
for x in ims:
  for p in s.encode(av.VideoFrame.from_ndarray(x,format='rgb24')): o.mux(p)
for p in s.encode(): o.mux(p)
o.close()
