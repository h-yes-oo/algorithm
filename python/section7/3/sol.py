import sys
# import time
def DFS(level, total):
  if level == n:
    if total > 0:
      check[total] = 0
  else:
    DFS(level+1, total - info[level])
    DFS(level+1, total)
    DFS(level+1, total + info[level])

if __name__=="__main__":
  # start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/3/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    info = list(map(int, sys.stdin.readline().split()))
    s = sum(info)
    check = [1] * (s + 1)
    DFS(0,0)
    print(sum(check) - 1)
  # print("--- %s seconds ---" % (time.time() - start_time))