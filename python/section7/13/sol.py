import sys

def DFS(x,y):
  island[x][y] = 0
  for i in range(8):
    x_n = x + dx[i]
    y_n = y + dy[i]
    if 0<= x_n < n and 0<= y_n < n and island[x_n][y_n] == 1:
      DFS(x_n,y_n)

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/13/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    island = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    count = 0
    for i in range(n):
      for j in range(n):
        if island[i][j] == 1:
          DFS(i,j)
          count += 1
    print(count)
    