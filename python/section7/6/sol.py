import sys
import time

def DFS(level, current):
  global count
  if level == n:
    print(current)
    count += 1
    return
  if code[level] == 0:
    return
  else:
    DFS(level+1,current+chr(64+code[level]))
    if code[level] == 1 and level < n-1:
        DFS(level+2,current+chr(64+ 10 + code[level+1]))
    elif code[level] == 2 and level < n-1 and code[level+1]<7:
        DFS(level+2,current+chr(64+20 + code[level+1]))

if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/6/in"+str(prob)+".txt","rt")
    code = sys.stdin.readline().strip()
    code = list([int(char) for char in code])
    n = len(code)
    count = 0
    DFS(0,'')
    print(count)
  print("--- %s seconds ---" % (time.time() - start_time))