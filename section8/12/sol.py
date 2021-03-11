import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/12/in"+str(prob)+".txt","rt")
    n, m = map(int,sys.stdin.readline().split())
    res=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
      res[i][i] = 0
    for i in range(m):
      x,y,z = map(int,sys.stdin.readline().split())
      res[x-1][y-1] = z
    for k in range(n):
      for i in range(n):
        for j in range(n):
          res[i][j] = min(res[i][j],res[i][k]+res[k][j])
    for i in range(n):
      for j in range(n-1):
        if res[i][j] == float('inf'):
          print('M',end=' ')
        else:
          print(res[i][j],end=' ')
      if res[i][n-1] == float('inf'):
        print('M')
      else:
        print(res[i][n-1])


    '''
    dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
    '''
