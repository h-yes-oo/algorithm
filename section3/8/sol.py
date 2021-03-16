import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section3/8/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    m = int(sys.stdin.readline())
    for _ in range(m):
      row, di, num = map(int,sys.stdin.readline().split())
      row -= 1
      num = num % n
      new_row = [0] * n
      if di == 0:
        for i in range(n):
          if i+num < n:
            new_row[i] = board[row][i+num]
          else:
            new_row[i] = board[row][i+num-n]
      else:
        for i in range(n):
          new_row[i] = board[row][i-num]
      board[row] = new_row
    middle = n // 2
    res = 0
    for row in range(0,middle):
      for col in range(row, n-row):
        res += board[row][col]
    res += board[middle][middle]
    for row in range(middle+1,n):
      exc = n - 1 - row
      for col in range(exc, n-exc):
        res += board[row][col]
    print(res)