import sys
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]
def find_pizza(row,col):
  Q = deque()
  check = [[0]*size for _ in range(size)]
  check[row][col] = 1
  for i in range(4):
    r = row + dr[i]
    c = col + dc[i]
    if 0<=r<size and 0<=c<size:
      Q.append((r,c))
  level=0
  while Q:
    level += 1
    for i in range(len(Q)):
      tmp = Q.popleft()
      if board[tmp[0]][tmp[1]] == 2:
        return level
      else:
        for i in range(4):
          r = tmp[0] + dr[i]
          c = tmp[1] + dc[i]
          if 0<=r<size and 0<=c<size and check[r][c] == 0:
            check[r][c] = 1
            Q.append((r,c))


def Pizza(level, bound):
  global res
  if level == diff:
    total = 0
    for i in range(size):
      for j in range(size):
        if board[i][j] == 1:
          total += find_pizza(i,j)
    if total < res:
      res = total
  else:
    for i in range(bound,total_store):
      pos = pizza[i]
      board[pos[0]][pos[1]] = 0
      Pizza(level+1, i+1)
      board[pos[0]][pos[1]] = 2


if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/17/in"+str(prob)+".txt","rt")
    size, store = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
    pizza = []
    for i in range(size):
      for j in range(size):
        if board[i][j] == 2:
          pizza.append((i,j))
    total_store = len(pizza)
    diff = total_store - store
    res = float('inf')
    Pizza(0,0)
    print(res)

