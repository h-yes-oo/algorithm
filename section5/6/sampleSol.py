import time
start_time = time.time()

import sys
from collections import deque
for prob in range(1,6):
    sys.stdin = open("section5/6/in"+str(prob)+".txt","rt")
    n,m = map(int, sys.stdin.readline().strip().split())
    Q = [(pos, val) for pos, val in enumerate(list(map(int, sys.stdin.readline().strip().split())))]
    Q = deque(Q)
    cnt = 0
    while True:
        cur=Q.popleft()
        if any(cur[1]<x[1] for x in Q):
            Q.append(cur)
        else:
            cnt += 1
            if cur[0] == m:
                break
    print(cnt)

print("--- %s seconds ---" % (time.time() - start_time))