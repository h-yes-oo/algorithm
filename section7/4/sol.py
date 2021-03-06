import sys

def DFS(level, total):
  global count
  if total == bill:
    count += 1
    return
  if total > bill:
    return
  if level == kind:
    return
  else:
    for j in range(num[level]+1):
      next_total = j*coins[level] + total
      DFS(level+1, next_total)
  


if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/4/in"+str(prob)+".txt","rt")
    bill = int(sys.stdin.readline())
    kind = int(sys.stdin.readline())
    coins = [0] * kind
    num = [0] * kind
    for i in range(kind):
      c, n = map(int,sys.stdin.readline().split())
      coins[i] = c
      num[i] = n
    count = 0
    DFS(0,0)
    print(count)