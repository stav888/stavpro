"""Current editor (Hanging Gardens, 1080x1920, 24 fps). Narration-first: each scene lasts
LEAD+line+TAIL (max 7.5 s), and the calmest window of each Flow clip (least frame-to-frame motion)
is picked to fill it. Watercolor-wash transition over paper texture (0.5 s), paper fade in/out,
clip ambience ducked under the voice, loudnorm, then bold white Montserrat subtitles (3-7 words,
hard cuts) with the spoken word in ONE highlight colour (cyan 2EF2FF here, chosen with QA), at 70%
of the height. Scene 3 used a lock mask (s3_lock.png) to freeze a drifting area of the clip.
Font: set MONTSERRAT_TTF."""
import os
import numpy as np, json, subprocess, re, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,24; SR=48000
D=json.load(open('audio/lines.json'))
LEAD,TAIL,TR=0.25,0.35,0.5
# --- scene durations
dur=[min(8-TR,max(3.0,LEAD+d['dur']+TAIL)) for d in D]
nf=[round(x*FPS) for x in dur]; cut=np.cumsum([0]+nf); N=int(cut[-1]); TRF=round(TR*FPS)
# --- motion analysis, choose window
def frames(i,w=90,h=160):
    b=subprocess.run(['ffmpeg','-v','error','-i',f'clips/{i:02d}.mp4','-vf',f'scale={w}:{h}','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
    return np.frombuffer(b,np.uint8).reshape(-1,h,w).astype(np.float32)
starts=[]
for k in range(15):
    f=frames(k+1); df=np.abs(np.diff(f,axis=0)).mean((1,2)); need=nf[k]+TRF
    best=None
    for s in range(0,len(f)-need+1):
        w=df[s:s+need-1]; sc=w.max()+0.3*w.std()+0.02*s
        if best is None or sc<best[0]: best=(sc,s)
    starts.append(best[1]/FPS)
# window: clip time = start + (t - (scene_start - TR/2))
win=[(starts[k],starts[k]+(nf[k]+TRF)/FPS) for k in range(15)]
json.dump({'dur':dur,'win':win},open('final/trims.json','w'),indent=1)
for k in range(15): print(k+1,'scene %.2fs window %.2f-%.2f'%(dur[k],*win[k]))
# --- audio
T=N/FPS; narr=np.zeros(int(T*SR)+SR); amb=np.zeros((len(narr),2))
import scipy.signal as ss
for k in range(15):
    a,sr=sf.read(f'audio/l{k+1:02d}.wav'); a=ss.resample_poly(a,2,1)
    o=int((cut[k]/FPS+LEAD)*SR); narr[o:o+len(a)]+=a
    b=subprocess.run(['ffmpeg','-v','error','-ss',str(win[k][0]),'-t',str(win[k][1]-win[k][0]),'-i',f'clips/{k+1:02d}.mp4','-f','f32le','-ac','2','-ar',str(SR),'-'],capture_output=True).stdout
    b=np.frombuffer(b,np.float32).reshape(-1,2).copy(); fl=int(TR*SR)
    b[:fl]*=np.linspace(0,1,fl)[:,None]; b[-fl:]*=np.linspace(1,0,fl)[:,None]
    o=max(0,int((cut[k]/FPS-TR/2)*SR)); n=min(len(b),len(amb)-o); amb[o:o+n]+=b[:n]
narr=narr/np.abs(narr).max()*0.8
env=np.convolve((np.abs(narr)>0.02).astype(float),np.ones(int(.4*SR)),'same')>0
env=np.convolve(env.astype(float),np.ones(int(.3*SR))/int(.3*SR),'same')
CLIP_AUDIO=float(os.environ.get('CLIP_AUDIO','0'))  # since 2026-11-09: generator audio muted by default (QA: no source audio leaking)
g=(0.30-0.20*env)*CLIP_AUDIO  # with CLIP_AUDIO=1: ambient ~-10dB idle, ~-20dB under voice (old Hanging Gardens mix)
rms=np.sqrt((amb**2).mean())+1e-9; amb=amb/rms*0.08
mix=amb*g[:,None]+narr[:,None]; mix=mix[:int(T*SR)]
sf.write('final/mix_raw.wav',mix,SR)
subprocess.run('ffmpeg -v error -y -i final/mix_raw.wav -af "loudnorm=I=-16:TP=-1.5:LRA=9" -ar 48000 final/mix.wav',shell=True,check=True)
# --- subtitles
P=os.environ.get('MONTSERRAT_TTF','Montserrat-VariableFont_wght.ttf')
def font(sz):
    f=ImageFont.truetype(P,sz); f.set_variation_by_name('Bold'); return f
CY=(0x2E,0xF2,0xFF)
subs=[]  # (f0,f1,words,hi_index)
WW=json.load(open('audio/whisper_words.json'))
for k,d in enumerate(D):
    sw=d['text'].split(); words=[]
    for w in sw:
        if re.search(r'\w',w): words.append(w)
        else: words[-1]+=' '+w
    tk=[[None]+x for x in WW[k]]; assert len(tk)==len(words),(k,len(tk),len(words))
    F0=font(80); dd=ImageDraw.Draw(Image.new('L',(1,1)))
    def wd(ix): return dd.textlength(' '.join(words[q] for q in ix),font=F0)
    def split(ix):
        if len(ix)<=7 and wd(ix)<=1100: return [ix]
        best=None
        for c in range(1,len(ix)):
            A,B=ix[:c],ix[c:]
            sc=abs(wd(A)-wd(B))/300+10*((len(A)<3)+(len(B)<3))-(2 if re.search(r'[.,?!—]$',words[A[-1]]) else 0)
            if best is None or sc<best[0]: best=(sc,A,B)
        return split(best[1])+split(best[2])
    ph=split(list(range(len(words))))
    t0=cut[k]/FPS+LEAD
    for pi,p in enumerate(ph):
        for j,i in enumerate(p):
            s=t0+tk[i][1]; e=t0+(tk[p[j+1]][1] if j+1<len(p) else (tk[ph[pi+1][0]][1] if pi+1<len(ph) else tk[i][2]+0.25))
            if j+1==len(p) and pi+1==len(ph) and k<14: e=min(e,(cut[k+1]-TRF//2)/FPS)
            subs.append((round(s*FPS),round(e*FPS),tuple(words[q] for q in p),j))
cache={}
def sub_img(ws,hi):
    key=(ws,hi)
    if key in cache: return cache[key]
    sz=84
    while True:
        f=font(sz); d=ImageDraw.Draw(Image.new('L',(1,1))); sp=d.textlength(' ',font=f)
        Wt=sum(d.textlength(w,font=f) for w in ws)+sp*(len(ws)-1)
        if Wt<=940: break
        sz-=4
    x0=(W-Wt)/2; y=H*0.70
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh); x=x0
    for w in ws: sd.text((x+4,y+5),w,font=f,fill=(0,0,0,200)); x+=sd.textlength(w,font=f)+sp
    lay=sh.filter(ImageFilter.GaussianBlur(6)); d=ImageDraw.Draw(lay); x=x0
    for i,w in enumerate(ws):
        d.text((x,y),w,font=f,fill=CY if i==hi else (255,255,255),stroke_width=3,stroke_fill=(20,12,6,180)); x+=d.textlength(w,font=f)+sp
    cache[key]=lay; return lay
sub_at={}
for f0,f1,ws,hi in subs:
    for f in range(f0,f1): sub_at[f]=(ws,hi)
# --- video
class Clip:
    def __init__(s,k):
        s.p=subprocess.Popen(['ffmpeg','-v','error','-ss',str(win[k][0]),'-i',f'clips/{k+1:02d}.mp4','-vf',f'scale={W}:{H}:flags=lanczos','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE); s.i=-1; s.last=None
    def get(s,j):
        while s.i<j:
            b=s.p.stdout.read(W*H*3)
            if len(b)<W*H*3: break
            s.last=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32); s.i+=1
        return s.last
CL={}
LOCK=None
_x=np.arange(W,dtype=np.float32); MSK=np.clip((0.41*W-_x)/(0.04*W),0,1)[None,:,None]
def shot(k,f):
    global LOCK
    if k not in CL: CL[k]=Clip(k)
    fr=CL[k].get(f-(cut[k]-TRF//2))
    if k==2 and fr is not None:
        if LOCK is None: LOCK=np.asarray(Image.open('final/s3_lock.png').convert('RGB')).astype(np.float32)
        fr=fr*(1-MSK)+LOCK*MSK
    return fr
def ez(p): return p*p*(3-2*p)
rng=np.random.default_rng(7)
nz=np.asarray(Image.fromarray((rng.random((48,27))*255).astype(np.uint8)).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(25))).astype(np.float32)/255
nz=(nz-nz.min())/(nz.max()-nz.min()); paper=np.array([244,236,220],np.float32)
def wash(a,b,p):
    m=np.clip((ez(p)*1.6-0.3-nz*0.6+0.3)/0.35,0,1)[...,None]; o=a*(1-m)+b*m
    return o*(1-0.18*np.sin(np.pi*p))+paper*0.18*np.sin(np.pi*p)
pr=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i','final/mix.wav','-map','0:v','-map','1:a','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','final/hanging_gardens_final.mp4'],stdin=subprocess.PIPE)
h=TRF//2
for f in range(N):
    k=max(i for i in range(15) if cut[i]<=f); fr=shot(k,f)
    if k>=1 and f<cut[k]+h: fr=wash(shot(k-1,f),fr,(f-cut[k]+h+1)/(TRF+1))
    elif k<14 and f>=cut[k+1]-h: fr=wash(fr,shot(k+1,f),(f-cut[k+1]+h+1)/(TRF+1))
    if f<10: fr=paper+(fr-paper)*ez(f/10)
    if f>N-14: fr=fr+(paper-fr)*ez((f-(N-14))/14)
    im=Image.fromarray(np.clip(fr,0,255).astype(np.uint8)).convert('RGBA')
    if f in sub_at: im=Image.alpha_composite(im,sub_img(*sub_at[f]))
    pr.stdin.write(im.convert('RGB').tobytes())
    for kk in list(CL):
        if kk<k-1: CL[kk].p.kill(); del CL[kk]
pr.stdin.close(); pr.wait(); print('done',N/FPS)
json.dump([(a,b,list(c),d) for a,b,c,d in subs],open('final/subs.json','w'))
