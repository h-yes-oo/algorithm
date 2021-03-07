import sys
from collections import deque
import time
if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/8/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0 , -1]
    apples = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ch = [[0]*n for _ in range(n)]
    total=0
    Q=deque()
    ch[n//2][n//2]=1
    total+=apples[n//2][n//2]
    Q.append((n//2,n//2))
    level = 0
    while True:
      if level == n//2:
        break
      size = len(Q)
      for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
          x=tmp[0]+dx[j]
          y=tmp[1]+dy[j]
          if ch[x][y] == 0:
            total += apples[x][y]
            ch[x][y]=1
            Q.append((x,y))
      level+=1
    print(total)
  print("--- %s seconds ---" % (time.time() - start_time))