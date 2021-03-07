import sys
import time
if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/8/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    apples = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    total = 0
    boundary = (n-1)//2
    for i in range(boundary):
      for j in range(boundary-i, boundary+i+1):
        total += apples[i][j]
    total += sum(apples[boundary])
    for i in range(n-1,boundary,-1):
      left = n-1 - i
      for j in range(boundary-left, boundary+left+1):
        total += apples[i][j]
    print(total)
  print("--- %s seconds ---" % (time.time() - start_time))


'''
n=3
1
0 1 2
1

n=5
2
123
012345
123
2

n=7
3
234
12345
01234567
12345
234
3

(n-1)//2
'''