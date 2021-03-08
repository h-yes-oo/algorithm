import sys
sys.setrecursionlimit(10**6)

def DFS(x_current,y_current, rain):
  ground[x_current][y_current] = 1
  for dirc in range(4):
    x = x_current + dx[dirc]
    y = y_current + dy[dirc]
    if 0<=x<n and 0<=y<n and ground[x][y] == 0 and info[x][y]>rain:
      DFS(x,y,rain)

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/14/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    info = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    res = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for rain in range(100):
      ground = [[0]*n for _ in range(n)]
      count = 0
      for i in range(n):
        for j in range(n):
          if ground[i][j] == 0 and info[i][j] > rain:
            count += 1
            DFS(i,j,rain)
      if count > res:
        res = count
      if count == 0:
        break
    print(res)

'''
max와 min을 이중 루프를 돌려서 구할 필요가 없이, 최대값의 조건이 되면 for loop를 break 하도록 !

이중 루프를 불필요하게 많이 돌리지 말것 !!

재귀를 많이 돌려야할때에는 sys.setrecursionlimit를 10**6로 설정할 것 !!
'''
