import sys
import time

'''
1 : 1
2 : 1 1
3 : 1 1 1 or 5 -1 -1
4 : 5 -1
5 : 5
'''

if __name__=="__main__":
  start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/7/in"+str(prob)+".txt","rt")
    hs, cow = map(int, sys.stdin.readline().split())
    diff = cow - hs
    if diff < 0:
      print(-diff)
    else:
      jumps = diff // 5
      remain = diff % 5
      if remain == 1:
        jumps += 1
      elif remain == 2 or remain == 4:
        jumps += 2
      elif remain == 3:
        jumps += 3
      print(jumps)
  print("--- %s seconds ---" % (time.time() - start_time))