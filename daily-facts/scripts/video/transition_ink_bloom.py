"""Themed transitions: ink bloom from the centre, a brush-stroke wipe and a golden-light
cross-fade. Same frame-folder layout as transition_paper_tear.py. Pick the one matching the mood
(fire/gold for burning or sunrise beats, ink for mystery, brush for travel)."""
import numpy as np, os
from PIL import Image, ImageFilter
W,H=1080,1920; starts=[0,111,183,264]; lens=[135,96,105,120]; T=24; N=383
def load(s,i): return np.asarray(Image.open(f's{s}/{min(i,lens[s]-1)+1:04d}.png').convert('RGB')).astype(np.float32)
def noise(scale,seed):
    r=np.random.default_rng(seed); a=r.random((H//scale+2,W//scale+2)).astype(np.float32)
    return np.asarray(Image.fromarray((a*255).astype(np.uint8)).resize((W+2*scale,H+2*scale),Image.BICUBIC))[:H,:W].astype(np.float32)/255
n1=noise(60,1)*0.6+noise(15,2)*0.3+noise(4,3)*0.1
Y,X=np.mgrid[0:H,0:W].astype(np.float32)
paper=np.asarray(Image.effect_noise((W,H),40).filter(ImageFilter.GaussianBlur(1))).astype(np.float32)/255
ink=np.array([45,32,22],np.float32); gold=np.array([255,214,140],np.float32)
def ease(p): return p*p*(3-2*p)
def inkdrop(a,b,p):
    d=np.sqrt((X-W*0.5)**2+(Y-H*0.45)**2)/np.hypot(W/2,H*0.55)
    field=d+0.35*(n1-0.5)          # organic bloom edge
    r=ease(p)*1.3
    m=np.clip((r-field)/0.04,0,1)[...,None]
    rim=np.clip(1-np.abs(r-field)/0.025,0,1)[...,None]*(p<0.97)
    out=a*(1-m)+b*m
    return out*(1-0.75*rim)+ink*(0.75*rim)*(0.85+0.15*paper[...,None])
bristle=np.repeat(np.random.default_rng(5).random((H,1)),W,1).astype(np.float32)
bristle=np.asarray(Image.fromarray((bristle*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur((0,2)))).astype(np.float32)/255
def brush(a,b,p):
    pos=-0.3+ease(p)*1.6
    field=(X/W)*0.75+(1-Y/H)*0.25 + 0.12*(bristle-0.5)+0.06*(n1-0.5)
    m=np.clip((pos-field)/0.02,0,1)[...,None]
    edge=np.clip(1-np.abs(pos-field)/0.03,0,1)[...,None]
    out=a*(1-m)+b*m
    return out*(1-0.35*edge)+ink*0.35*edge
def golden(a,b,p):
    m=ease(np.clip((p-0.2)/0.6,0,1)); g=np.sin(np.pi*p)
    glow=g*np.clip(1.2-np.sqrt((X-W*0.6)**2+(Y-H*0.3)**2)/(H*0.8),0,1)[...,None]
    out=a*(1-m)+b*m
    return out+(gold-out)*0.55*glow
FX=[inkdrop,brush,golden]; os.makedirs('mix',exist_ok=True)
for f in range(N):
    s=max(i for i in range(4) if starts[i]<=f)
    tr=[i for i in range(3) if starts[i+1]<=f<starts[i+1]+T]
    if tr:
        i=tr[0]; p=(f-starts[i+1]+1)/(T+1); img=FX[i](load(i,f-starts[i]),load(i+1,f-starts[i+1]),p)
    else: img=load(s,f-starts[s])
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(f'mix/{f:04d}.png',compress_level=1)
