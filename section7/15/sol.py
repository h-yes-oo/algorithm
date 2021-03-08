import sys
from collections import deque

if __name__=="__main__":
  for prob in range(5,6):
    sys.stdin = open("section7/15/in"+str(prob)+".txt","rt")
    m,n = map(int, sys.stdin.readline().split())
    tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    Q = deque()
    for i in range(n):
        for j in range(m):
          if tomato[i][j] == 1:
            Q.append((i,j))
    if len(Q) == n*m:
      print(0)
    else:
      day = 0
      while Q:
        progress = False
        for _ in range(len(Q)):
          tmp = Q.popleft()
          for dirc in range(4):
            x = tmp[0] + dx[dirc]
            y = tmp[1] + dy[dirc]
            if 0<=x<n and 0<=y<m and tomato[x][y] == 0:
              tomato[x][y] = 1
              Q.append((x,y))
              progress = True
        if progress:
          day +=1
      complete = True
      for i in range(n):
          for j in range(m):
            if tomato[i][j] == 0:
              complete = False
              break
      if complete:
        print(day)
      else:
        print(-1)
