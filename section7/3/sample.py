import sys
import time
def DFS(level, total):
  global res
  if level == n:
    if total > 0:
      res.add(total)
  else:
    DFS(level+1, total - info[level])
    DFS(level+1, total)
    DFS(level+1, total + info[level])

if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/3/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    info = list(map(int, sys.stdin.readline().split()))
    s = sum(info)
    res = set()
    DFS(0,0)
    print(s-len(res))
  print("--- %s seconds ---" % (time.time() - start_time))

