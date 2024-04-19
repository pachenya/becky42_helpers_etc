#
# queen.py by Becky42nd
#

import random as rn

xy=\
((-1,-1),(0,-1),(1,-1),\
 (-1, 0),(0, 0),(1, 0),\
 (-1, 1),(0, 1),(1, 1))

EMPTY=0
FULL=1
QAT=2
WIDTH=8
N_QS=8

b=[[EMPTY for ii in range(8)] for jj in range(8)]

def clearmap():
  for i in range(8):
    for j in range(8):
      b[i][j]=EMPTY

def queen_t(x,y):
  rval=[]
  for d in xy:
    for j in range(WIDTH):
      xx=x+d[0]*j
      yy=y+d[1]*j
      if xx<0 or xx>=WIDTH or yy<0 or yy>=WIDTH:
        break
      t = (xx,yy)
      rval.append(t)
  return rval
  
def can_place(x,y):
  if b[x][y]!=EMPTY:
      return False
  return True

def do_place(x,y):
  tmp=queen_t(x,y)
  for t in tmp:
    b[t[0]][t[1]]=FULL
  b[x][y]=QAT

def prtmap():
  print('-----------------')
  for i in range(WIDTH):
    print('|',end='')
    for j in range(WIDTH):
      v = b[i][j]
      c = '.'
      if v==QAT:
        c='Q'
      print(c+'|',end='')
    print('')
    print('-----------------')
  print('')

def main():
  cnt=0
  anscnt=0
  N_TRY=100
  N_ANS=2
  while cnt<N_TRY:
    clearmap()
    miss=False
    for q in range(N_QS): # N_QS==8
      xs = rn.randint(0,7)
      for xx in range(WIDTH):
        x = (xs+xx) % WIDTH
        if can_place(x,q):
          do_place(x,q)
          break
        else:
          if xx==WIDTH-1:
            miss=True
      if miss:
        break
    if not miss:
      anscnt+=1
      prtmap()
      if anscnt>=N_ANS:
        break
    cnt+=1

main()    
