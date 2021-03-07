import sys
from collections import deque
def DFS(x_now, y_now):
  global count
  if x_now == 6 and y_now == 6:
    count += 1
    return
  else:
    for i in range(4):
      x = x_now + dx[i]
      y = y_now + dy[i]
      if 7>x>=0 and 7>y>=0 and maze[x][y] == 0:
        maze[x][y] = 1
        DFS(x,y)
        maze[x][y] = 0
  

if __name__ == "__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/10/in"+str(prob)+".txt","rt")
    maze = [list(map(int,sys.stdin.readline().split())) for _ in range(7)]
    count = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    maze[0][0]=1
    DFS(0,0)
    print(count)
