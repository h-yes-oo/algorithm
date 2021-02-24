import time
start_time = time.time()

import sys
from collections import deque
for prob in range(1,6):
    sys.stdin = open("section5/6/in"+str(prob)+".txt","rt")
    n,m = map(int, sys.stdin.readline().strip().split())
    patients = list(map(int, sys.stdin.readline().strip().split()))
    order = list(range(n))
    order = deque(order)
    count = 0
    while True:
        if patients[order[0]] == max(patients):
            count += 1
            if(order[0] == m):
                break
            patients[order[0]] = -1
            order.popleft()
        else:
            order.append(order.popleft())
    print(count)

print("--- %s seconds ---" % (time.time() - start_time))