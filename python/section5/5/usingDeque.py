import time
start_time = time.time()
import sys
from collections import deque
for prob in range(1,6):
    sys.stdin = open("section5/5/in"+str(prob)+".txt","rt")
    n,k = map(int,sys.stdin.readline().strip().split())
    dq = list(range(1,n+1))
    dq = deque(dq)
    while len(dq) > 1:
        for _ in range(k-1):
            cur=dq.popleft()
            dq.append(cur)
        dq.popleft()
    print(dq.popleft())
print("--- %s seconds ---" % (time.time() - start_time))