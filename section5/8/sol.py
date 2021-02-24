import time
start_time = time.time()
import sys
for prob in range(1,6):
    sys.stdin = open("section5/8/in"+str(prob)+".txt","rt")
    n=int(sys.stdin.readline().strip())
    words = []
    for _ in range(n):
        words.append(sys.stdin.readline().strip())
    for _ in range(n-1):
        words.remove(sys.stdin.readline().strip())
    print(words[0])
print("--- %s seconds ---" % (time.time() - start_time))