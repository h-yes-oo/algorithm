import sys

if __name__=="__main__":
  n,m=map(int,sys.stdin.readline().split())
  # res =[]
  # for _ in range(n):
  #   res.append([0] * n)
  res = [[0]*n for _ in range(n)]
  for _ in range(m):
    i,j,k = map(int,sys.stdin.readline().split())
    res[i-1][j-1] = k
  for x in res:
    for y in x:
      print(y,end=' ')
    print()
    

