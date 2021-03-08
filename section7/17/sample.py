import sys

def DFS(level, bound):
  global res
  if level == store:
    total = 0
    for j in range(len(house)):
      hr = house[j][0]
      hc = house[j][1]
      distance = float('inf')
      for pos in cb:
        pr = pizza[pos][0]
        pc = pizza[pos][1]
        dis = abs(hr-pr) + abs(hc-pc)
        if dis < distance:
          distance = dis
      total += distance
    if total < res:
      res = total
  else:
    for i in range(bound,len(pizza)):
      cb[level] = i
      DFS(level+1, i+1)


if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/17/in"+str(prob)+".txt","rt")
    size, store = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
    pizza = []
    house = []
    for i in range(size):
      for j in range(size):
        if board[i][j] == 2:
          pizza.append((i,j))
        elif board[i][j] == 1:
          house.append((i,j))
    res = float('inf')
    cb = [0] * store
    DFS(0,0)
    print(res)