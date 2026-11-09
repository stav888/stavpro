import cv2,numpy as np,sys
p=sys.argv[1]; R=eval(sys.argv[2])
c=cv2.VideoCapture(p);G=[]
while True:
  ok,f=c.read()
  if not ok:break
  G.append(cv2.cvtColor(f,cv2.COLOR_BGR2GRAY).astype(np.float32))
for (y0,y1,x0,x1) in R:
  sh=np.array([cv2.phaseCorrelate(G[0][y0:y1,x0:x1],g[y0:y1,x0:x1])[0] for g in G]); st=np.abs(np.diff(sh,axis=0))
  print(p,(y0,y1,x0,x1),'dx',sh[:,0].min().round(1),sh[:,0].max().round(1),'dy',sh[:,1].min().round(1),sh[:,1].max().round(1),'maxstep',st.max(0).round(2),'steps>1px',int((st.max(1)>1).sum()))
