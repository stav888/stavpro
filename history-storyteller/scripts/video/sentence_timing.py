import json,re,difflib,numpy as np,soundfile as sf
S=[l.strip() for l in open('audio/sentences.txt') if l.strip()]
N=lambda s: re.sub(r"[^a-z0-9]","",s.lower().replace('é','e'))
ws=json.load(open('audio/asr_words.json'))
a,sr=sf.read('audio/narration_norm.wav'); a=a.mean(1) if a.ndim>1 else a
hop=int(.01*sr); db=np.array([20*np.log10(np.sqrt(np.mean(a[i:i+hop]**2))+1e-9) for i in range(0,len(a)-hop,hop)])
total=len(a)/sr
sw=[(si,wi,N(w)) for si,s in enumerate(S) for wi,w in enumerate(s.split())]
A=[N(w[0]) for w in ws]; B=[x[2] for x in sw]
sm=difflib.SequenceMatcher(None,B,A,autojunk=False); mp={}
for blk in sm.get_matching_blocks():
  for k in range(blk.size): mp[blk.a+k]=blk.b+k
def runs(lo,hi,minl):
  R=[];i=max(0,lo)
  while i<min(len(db),hi):
    if db[i]<-45:
      j=i
      while j<len(db) and db[j]<-45: j+=1
      if j-i>=minl: R.append((j-i,i,j))
      i=j
    else: i+=1
  return R
def onset(t,lo=None,hi=45):
  c=int(round(t*100)); R=runs(int(lo*100) if lo is not None else c-35, c+hi, 2)
  return max(R)[2]/100 if R else t
on={}
for idx,(si,wi,_) in enumerate(sw):
  if idx in mp: on[(si,wi)]=onset(ws[mp[idx]][1])
# fill gaps by interpolation
for si,s in enumerate(S):
  n=len(s.split())
  for wi in range(n):
    if (si,wi) not in on: print('unmatched',si+1,wi,s.split()[wi])
rows=[];ONS={}
for si in range(1,len(S)):
  prev=[mp[i] for i,(x,y,_) in enumerate(sw) if x==si-1 and i in mp][-1]
  i0=[i for i,(x,y,_) in enumerate(sw) if x==si][0]
  on[(si,0)]=onset(ws[mp[i0]][1],lo=ws[prev][2]-0.1,hi=60)
on[(0,0)]=float(np.argmax(db>-45))/100
for si,s in enumerate(S):
  o=on[(si,0)]; n=len(s.split())
  last=[mp[i] for i,(x,y,_) in enumerate(sw) if x==si and i in mp][-1]
  rows.append({"sentence":si+1,"text":s,"first_word":s.split()[0],"asr_first":ws[mp[[i for i,(x,y,_) in enumerate(sw) if x==si][0]]][0],"word_start":o,"onset":o,"speech_end":ws[last][2],"start":0.0 if si==0 else round(o-0.06,3)})
  ONS[str(si+1)]={str(wi):round(on.get((si,wi),0)-0.02,3) for wi in range(n)}
for i,r in enumerate(rows): r["end"]=rows[i+1]["start"] if i<len(rows)-1 else round(total,3)
for i,r in enumerate(rows):
  if i>0: r['speech_end_prev_ok']=bool(db[int(r['start']*100):int(r['onset']*100)].max()<-45) if r['onset']>r['start'] else False
  print(r['sentence'],r['start'],r['onset'],r['end'],r.get('speech_end_prev_ok'))
json.dump({"rows":rows,"total":total},open('audio_timing.json','w'),indent=1); json.dump(ONS,open('ons.json','w'))
