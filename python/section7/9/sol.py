import sys
from collections import deque
if __name__ == "__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/9/in"+str(prob)+".txt","rt")
    maze = [list(map(int,sys.stdin.readline().split())) for _ in range(7)]
    path = deque()
    path.append((0,0))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    level=0
    maze[0][0] = 1
    finding = True
    while path and finding:
        for _ in range(len(path)):
          current = path.popleft()
          if current == (6,6):
            finding = False
            print(level)
            break
          else:
            for i in range(4):
              x = current[0] + dx[i]
              y = current[1] + dy[i]
              if 7>x>=0 and 7>y>=0 and maze[x][y] == 0:
                path.append((x,y))
                maze[x][y] = 1
        level += 1
    if finding:
      print(-1)
