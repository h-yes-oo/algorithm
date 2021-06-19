import sys
import time
from collections import deque

if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/7/in"+str(prob)+".txt","rt")
    hs, cow = map(int, sys.stdin.readline().split())
    MAX = 100000
    ch = [0] * (MAX+1)
    dis = [0] * (MAX+1)
    ch[hs] = 1
    dis[hs] = 0
    dQ = deque()
    dQ.append(hs)
    while dQ:
      now=dQ.popleft()
      if now==cow:
        break
      for next_step in(now-1, now+1, now+5):
        if 0<next_step<=MAX:
          if ch[next_step] == 0:
            dQ.append(next_step)
            ch[next_step]=1
            dis[next_step]=dis[now]+1
    print(dis[cow])
  print("--- %s seconds ---" % (time.time() - start_time))