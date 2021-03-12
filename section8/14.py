import sys
from collections import deque

if __name__=="__main__":
  n, m = map(int,sys.stdin.readline().split())
  flow = [[float('inf')] * n for _ in range(n)]
  degree = [0] * n
  Q = deque()
  for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    flow[a-1][b-1] = 1
    degree[b-1] += 1
  for i in range(n):
    if degree[i] == 0:
      Q.append(i)
  while Q:
    x=Q.popleft()
    print(x+1, end=' ')
    for i in range(n):
      if flow[x][i] == 1:
        degree[i] -= 1
        flow[x][i] = 0
        if degree[i] == 0:
          Q.append(i)


  '''
  1 6 2 5 4 3
  '''