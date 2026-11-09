"""Themed transition: the outgoing frame tears in two like watercolor paper (ragged fringe,
cream paper edge, gap shadow). Works on PNG frame folders s0/, s1/ ... (one per scene);
edit starts/lens/N for your timeline. 24-frame (1 s) slow transition."""
import numpy as np
from PIL import Image, ImageFilter
import os
W,H=1080,1920; rng=np.random.default_rng(7)
starts=[0,111,183,264]; lens=[135,96,105,120]; T=24; N=383
def load(s,i): return np.asarray(Image.open(f's{s}/{min(i,lens[s]-1)+1:04d}.png').convert('RGB')).astype(np.float32)
def tearline(seed):
    r=np.random.default_rng(seed); y=np.arange(H)
    x=np.zeros(H)
    for oct,amp in [(3,90),(12,35),(50,14),(200,6),(700,3)]:
        pts=r.uniform(-1,1,oct+2); x+=amp*np.interp(y,np.linspace(0,H,oct+2),pts)
    return W/2+x
paper=np.asarray(Image.effect_noise((W,H),40).filter(ImageFilter.GaussianBlur(1))).astype(np.float32)/255
cream=np.array([243,234,214],np.float32)
X=np.arange(W)[None,:]
def tear(a,b,p,seed):
    e=p*p*(3-2*p)  # ease
    line=tearline(seed); fr=np.random.default_rng(seed+1)
    fib=4+6*np.abs(np.interp(np.arange(H),np.linspace(0,H,300),fr.uniform(-1,1,300)))  # ragged white fringe width
    out=b.copy()
    # gap shadow on b
    off=e*W*0.62
    for side in (-1,1):
        sh=side*off; 
        src=np.roll(a,int(sh),axis=1)  # piece shifted
        ln=(line+sh)[:,None]
        if side<0: m=X<ln; edge=ln-X
        else: m=X>ln; edge=X-ln
        # shadow
        shadow=np.clip(1-np.clip(-edge,0,40)/40,0,1)*(~m)*0.35*min(1,e*4)
        out*=1-shadow[...,None]
        frm=(edge<fib[:,None])&m
        piece=src*(0.92+0.08*paper[...,None])
        piece=np.where(frm[...,None],cream*(0.9+0.1*paper[...,None]),piece)
        out=np.where(m[...,None],piece,out)
    return out
os.makedirs('out',exist_ok=True)
for f in range(N):
    s=max(i for i in range(4) if starts[i]<=f)
    tr=[i for i in range(3) if starts[i+1]<=f<starts[i+1]+T]
    if tr:
        i=tr[0]; p=(f-starts[i+1]+1)/(T+1)
        img=tear(load(i,f-starts[i]),load(i+1,f-starts[i+1]),p,11+i*5)
    else: img=load(s,f-starts[s])
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(f'out/{f:04d}.png',compress_level=1)
