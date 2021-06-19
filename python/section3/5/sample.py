import sys
if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section3/5/in"+str(prob)+".txt","rt")
    n,goal = map(int,sys.stdin.readline().split())
    elem = list(map(int,sys.stdin.readline().split()))
    lt = 0
    rt = 1
    tot = elem[0]
    cnt = 0
    while True:
      if tot < goal:
        if rt < n:
          tot += elem[rt]
          rt+=1
        else:
          break
      elif tot == goal:
        cnt += 1
        tot -= elem[lt]
        lt += 1
      else:
        tot -= elem[lt]
        lt += 1
    print(cnt)