import sys
from collections import deque

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/13/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    island = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    count = 0
    Q=deque()
    for i in range(n):
      for j in range(n):
        if island[i][j] == 1:
          island[i][j]=0
          Q.append((i,j))
          while Q:
            tmp=Q.popleft()
            for k in range(8):
              x=tmp[0]+dx[k]
              y=tmp[1]+dy[k]
              if 0<=x<n and 0<=y<n and island[x][y]==1:
                island[x][y]=0
                Q.append((x,y))
          count += 1
    print(count)
      