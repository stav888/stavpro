import sys,torch,numpy as np,av,json
import os; sys.path.insert(0,os.environ.get('CFI_RIFE_DIR','/tmp/cfi/vfi_models/rife')); from rife_arch import IFNet
from PIL import Image
torch.set_num_threads(8)
m=IFNet(arch_ver="4.7"); m.load_state_dict(torch.load(os.environ.get('RIFE47_WEIGHTS','rife47.pth'),weights_only=False)); m.eval()
T=lambda a: torch.from_numpy(a).permute(2,0,1)[None].float()/255
R=json.load(open('audio_timing.json'))['rows']
FR=lambda t: round(t*24)/24
for i in map(int,sys.argv[1:]):
  s=0 if i==1 else FR(R[i-1]['start']); e=FR(R[i]['start']) if i<len(R) else FR(json.load(open('audio_timing.json'))['total'])
  M=int(round((e-s)*24))+3
  ims=[x.to_ndarray(format='rgb24') for x in av.open(f'gen/s{i}.mp4').decode(video=0)][:M]
  H,W=ims[0].shape[:2]; ph,pw=(32-H%32)%32,(32-W%32)%32
  ims=[np.pad(x,((0,ph),(0,pw),(0,0)),mode='edge') for x in ims]
  g=[np.asarray(Image.fromarray(x).convert('L').resize((320,240)),float) for x in ims]
  d=np.array([0]+[np.abs(g[j]-g[j-1]).mean() for j in range(1,len(g))])
  c=np.cumsum(d); c=c/c[-1]; lin=np.linspace(0,1,len(g))
  out=av.open(f'anim/scene{i}_r.mp4','w'); st=out.add_stream('libx264',rate=24); st.width=W;st.height=H;st.pix_fmt='yuv420p'; st.options={'crf':'14'}
  for n in range(M):
    u=n/(M-1); tgt=u   # blend linear and motion-equalized
    cc=0.85*c+0.15*lin; pos=np.interp(tgt,cc,np.arange(len(g)))
    j=int(np.floor(pos)); f=pos-j
    if j>=len(ims)-1 or f<0.02: fr=ims[min(j,len(ims)-1)]
    else:
      with torch.no_grad(): r=m(T(ims[j]),T(ims[j+1]),torch.tensor([[[[float(f)]]]]),[8,4,2,1],False,True).clamp(0,1)
      fr=(r[0].permute(1,2,0).numpy()*255).round().astype(np.uint8)
    for p in st.encode(av.VideoFrame.from_ndarray(np.ascontiguousarray(fr[:H,:W]),format='rgb24')): out.mux(p)
  for p in st.encode(): out.mux(p)
  out.close(); print(i,'src',len(ims),'out',M,flush=True)
