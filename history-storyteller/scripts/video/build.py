import json, subprocess, numpy as np, os, sys
from PIL import Image, ImageDraw, ImageFont
OUT=sys.argv[1] if len(sys.argv)>1 else "/workspace/garbo-history-v1.mp4"
FONT=os.environ.get("PATRICK_HAND_TTF","PatrickHand-Regular.ttf")
def f(sz): return ImageFont.truetype(FONT, sz)
T=json.load(open("audio_timing.json")); rows=T["rows"]; TOTAL=T["total"]; N=len(rows)
FIX={}
ONS=json.load(open('ons.json'))
def wrap(d,text,font,maxw):
    ws=text.split(); lines=[]; cur=""
    for wd in ws:
        tt=(cur+" "+wd).strip()
        if d.textlength(tt,font=font)<=maxw: cur=tt
        else: lines.append(cur); cur=wd
    if cur: lines.append(cur)
    return lines
chunks=[]
import math,re
FPS=24
ASR=json.load(open("audio/asr_words.json"))
norm=lambda s: re.sub(r"[^a-z]","",s.lower())
MAN={}
def bwrap(d,txt,font,maxw):
    ws=txt.split()
    if d.textlength(txt,font=font)<=maxw: return [txt]
    best=None
    for i in range(2,len(ws)-1):
        a=" ".join(ws[:i]); b=" ".join(ws[i:])
        if ws[i-1].lower() in ("a","the","to","and","in","of","his","an","be","at","was","from","on","by","named"): continue
        m=max(d.textlength(a,font=font),d.textlength(b,font=font))
        if m<=maxw and (best is None or m<best[0]): best=(m,[a,b])
    return best[1] if best else [txt]
OV={1:[4],4:[5],7:[12],8:[8],10:[5],11:[7,12],12:[8,16],13:[10],14:[6,12]}
def plan(ws,sn=0):
    n=len(ws)
    if sn in OV: return [0]+OV[sn]+[n]
    if n<=10: return [0,n]
    k=2 if n<=20 else 3
    cuts=[]
    for j in range(1,k):
        ideal=n*j/k; cands=[i for i in range(5,n-4) if ws[i-1].endswith(",") or ws[i-1].endswith(":")]
        c=min(cands,key=lambda i:abs(i-ideal)) if cands and min(abs(i-ideal) for i in cands)<=3 else round(ideal)
        cuts.append(c)
    return [0]+cuts+[n]
for r in rows:
    ws=r["text"].split(); bounds=plan(ws,r['sentence'])
    times=[r["start"]+(0.05 if r["sentence"]==1 else 0)]
    for b in bounds[1:-1]:
        target=norm(ws[b]); prev=times[-1]
        hit=[w for w in ASR if w[1]>prev+0.3 and w[1]<r["speech_end"] and norm(w[0])==target]
        occ=sum(1 for x in ws[:b] if norm(x)==target)
        hit=[w for w in ASR if w[1]>r['start'] and w[1]<r['speech_end'] and norm(w[0])==target]
        t=ONS[str(r['sentence'])][str(b)]
        print("split",ws[b],"asr" if hit else "prop",round(t,2))
        times.append(math.floor(t*FPS+1e-6)/FPS)
    times.append(r["end"]-0.05)
    for ci in range(len(bounds)-1):
        txt=" ".join(ws[bounds[ci]:bounds[ci+1]])
        ov=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(ov)
        for fs in (62,56,52):
            font=f(fs); lines=bwrap(d,txt,font,960)
            if all(d.textlength(l,font=font)<=960 for l in lines): break
        y=1430
        for line in lines: d.text((540,y),line,font=font,fill=(12,12,12,255),anchor="ma"); y+=70
        png=f"subpng/c{len(chunks):02d}.png"; ov.save(png)
        st=math.ceil(times[ci]*FPS-1e-6)/FPS; en=math.floor(times[ci+1]*FPS+1e-6)/FPS
        chunks.append({"sentence":r["sentence"],"text":txt,"lines_text":lines,"words":bounds[ci+1]-bounds[ci],"start":st,"end":en,"sent_start":r["start"],"sent_end":r["end"],"png":png,"lines":len(lines)})
        print(r["sentence"],st,en,lines)
bad=[c for c in chunks if c["start"]<c["sent_start"] or c["end"]>c["sent_end"]]
print("chunks",len(chunks),"crossings",len(bad),"min_words",min(c["words"] for c in chunks),"max_lines",max(c["lines"] for c in chunks))
json.dump({"rows":rows,"chunks":chunks,"total":TOTAL},open("timing.json","w"),indent=1)
for i in range(1,N+1):
    ov=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(ov)
    d.text((540,115),"THE SPY WHO INVENTED SPIES",font=f(64),fill=(20,20,20,255),anchor="mm")
    d.line([(400,165),(680,165)],fill=(225,55,40,255),width=6)
    d.text((540,1835),f"\u2014 {i} / {N} \u2014",font=f(32),fill=(130,130,130,255),anchor="mm")
    ov.save(f"static/static{i}.png")
def bbox(src):
    acc=None
    sdur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src]))
    for t in [0.2,2,min(4,sdur-0.3),min(5.5,sdur-0.2)]:
        subprocess.run(["ffmpeg","-y","-v","error","-ss",str(t),"-i",src,"-frames:v","1","/tmp/bb.png"],check=True)
        a=np.asarray(Image.open("/tmp/bb.png").convert("L"))<200
        acc=a if acc is None else (acc|a)
    ys,xs=np.where(acc); H,W=acc.shape; m=14
    return max(0,xs.min()-m),max(0,ys.min()-m),min(W,xs.max()+m),min(H,ys.max()+m)
FR=lambda t: round(t*24)/24
segs=[(0.0 if i==0 else FR(rows[i]["start"]), FR(rows[i+1]["start"]) if i<N-1 else FR(TOTAL)) for i in range(N)]
for idx,(s,e) in enumerate(segs,1):
    dur=round(e-s,3); src=f"anim/scene{idx}_r.mp4"
    x0,y0,x1,y1=bbox(src); cw,ch=(x1-x0)//2*2,(y1-y0)//2*2
    sc=min(1060/cw,1150/ch); sw,sh=int(cw*sc)//2*2,int(ch*sc)//2*2
    x=(1080-sw)//2; y=max(200,min(1400-sh,790-sh//2))
    over=[c for c in chunks if c["end"]>s and c["start"]<e]
    inputs=["-i",src,"-loop","1","-i",f"static/static{idx}.png"]
    for c in over: inputs+=["-loop","1","-i",c["png"]]
    sd=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src])); k=max(1.0,(dur+0.05)/(sd-0.05))
    fl=[f"[0:v]setpts={k:.4f}*(PTS-STARTPTS),trim=0:{dur},setpts=PTS-STARTPTS,crop={cw}:{ch}:{x0}:{y0},scale={sw}:{sh}:flags=lanczos,pad=1080:1920:{x}:{y}:white,fps=24[p0]","[p0][1:v]overlay=0:0[b1]"]; last="b1"
    for bi,c in enumerate(over):
        rs=round(max(c["start"],s)-s,3); re_=round(min(c["end"],e)-s,3)
        fl.append(f"[{last}][{2+bi}:v]overlay=0:0:enable='gte(t,{rs-0.0208:.4f})*lt(t,{re_-0.0208:.4f})'[o{bi}]"); last=f"o{bi}"
    fl.append(f"[{last}]format=yuv420p[v]")
    subprocess.run(["ffmpeg","-y","-v","error"]+inputs+["-filter_complex",";".join(fl),"-map","[v]","-t",str(dur),"-c:v","libx264","-r","24","-preset","medium","-crf","20",f"clips/clip{idx:02d}.mp4"],check=True)
    print("clip",idx,dur,"art",sw,sh,"src dur ok" if float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",src]))>=dur else "SHORT")
open("list.txt","w").write("".join(f"file 'clips/clip{i:02d}.mp4'\n" for i in range(1,N+1)))
subprocess.run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i","list.txt","-c","copy","silent.mp4"],check=True)
subprocess.run(["ffmpeg","-y","-v","error","-i","silent.mp4","-i","audio/narration_norm.wav","-map","0:v","-map","1:a","-c:v","copy","-ar","48000","-c:a","aac","-b:a","192k","-shortest",OUT],check=True)
print("done",OUT)
