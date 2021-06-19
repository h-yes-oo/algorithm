import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section3/6/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    max_total = 0
    for i in range(n):
      max_total = max(max_total, sum(board[i]))
    for j in range(n):
      tmp = 0
      for k in range(n):
        tmp += board[k][j]
      max_total = max(max_total, tmp)
    rt = 0
    for i in range(n):
      rt += board[i][i]
    max_total = max(max_total, rt) 
    lt = 0
    for i in range(n):
      lt += board[i][n-1-i]
    max_total = max(max_total, lt) 
    print(max_total)