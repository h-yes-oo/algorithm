import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/7/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    dy = [[0]*n for _ in range(n)]
    dy[0][0] = board[0][0]
    for i in range(1,n):
      dy[0][i] = dy[0][i-1] + board[0][i]
      dy[i][0] = dy[i-1][0] + board[i][0]
    for i in range(1,n):
      for j in range(1,n):
        min_e = dy[i-1][j]
        if dy[i][j-1] < min_e:
          min_e = dy[i][j-1]
        dy[i][j] = min_e + board[i][j]
    print(dy[n-1][n-1])


'''
3 3 5
2 3 4
6 5 2

3 6 11
5 8 12
11 13 14
'''
      