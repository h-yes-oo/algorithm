import sys
import heapq as hq
for prob in range(3,4):
    sys.stdin = open("section5/10/in"+str(prob)+".txt","rt")
    numbers = []
    while True:
        num = int(sys.stdin.readline())
        if num == -1:
            break
        if num ==0:
            if len(numbers)==0:
                print(-1)
            else:
                print(hq.heappop(numbers))
        else:
            hq.heappush(numbers, num)