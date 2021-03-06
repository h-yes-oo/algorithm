import sys
import time

def DFS(level, current):
  global count
  if level == n:
    count += 1
    for j in range(current):
      print(chr(res[j]+64),end='')
    print()
  else:
    for i in range(1,27):
      if code[level] == i:
        res[current]=i
        DFS(level+1, current+1)
      elif i >=10 and code[level]==i//10 and code[level+1]==i%10:
        res[current]=i
        DFS(level+2, current+1)

if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/6/in"+str(prob)+".txt","rt")
    code = sys.stdin.readline().strip()
    code = list([int(char) for char in code])
    n = len(code)
    code.insert(n, -1)
    res=[0]*(n+3)
    count = 0
    DFS(0,0)
    print(count)
  print("--- %s seconds ---" % (time.time() - start_time))