import time
start_time = time.time()
import sys
for prob in range(1,6):
    sys.stdin = open("section5/5/in"+str(prob)+".txt","rt")
    n,k = map(int,sys.stdin.readline().strip().split())
    prince = list(range(1,n+1))
    idx = k-1
    while len(prince) > 1:
        prince.pop(idx)
        idx += k-1
        if idx >= len(prince):
            idx = idx % len(prince) #여러 바퀴 도는 경우에 유의할 것 !!!
    print(prince[0])
print("--- %s seconds ---" % (time.time() - start_time))