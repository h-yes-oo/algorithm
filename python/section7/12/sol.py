import sys

def DFS(x,y):
  global count
  count += 1
  house[x][y] = 0
  for i in range(4):
    x_next = x+dx[i]
    y_next = y+dy[i]
    if 0<=x_next<n and 0<=y_next<n and house[x_next][y_next] == 1:
      DFS(x_next,y_next)
    
if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/12/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    house = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    res = []
    for i in range(n):
      for j in range(n):
        if house[i][j] == 1:
          count = 0
          DFS(i,j)
          res.append(count)
    print(len(res))
    res.sort()
    for x in res:
      print(x)
  
  '''
  1을 찾을 때마다 끝날때까지 DFS 돌리기
  '''

