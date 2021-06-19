import time
start_time = time.time()
import sys
for prob in range(1,6):
    sys.stdin = open("section5/8/in"+str(prob)+".txt","rt")
    n=int(sys.stdin.readline().strip())
    p=dict()
    for i in range(n):
        word = sys.stdin.readline().strip()
        p[word]=1
    for i in range(n-1):
        word = sys.stdin.readline().strip()
        p[word]=0
    for key,val in p.items():
        if val == 1:
            print(key)
            break
print("--- %s seconds ---" % (time.time() - start_time))