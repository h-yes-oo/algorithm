import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
'''
direction
0 : down
1 : right
2 : left
'''

def DFS(row,col,direction):
  global end
  if row == 9:
    end = info[9][col]
  else:
    if direction == 0:
      if 0<=col+1<10 and info[row][col+1] == 1:
        DFS(row,col+1,1)
      elif 0<=col-1<10 and info[row][col-1] == 1:
        DFS(row,col-1,2)
      else:
        DFS(row+1,col,0)
    elif direction == 1:
      if 0<=col+1<10 and info[row][col+1] == 1:
        DFS(row,col+1,1)
      else:
        DFS(row+1,col,0)
    else:
      if 0<=col-1<10 and info[row][col-1] == 1:
        DFS(row,col-1,2)
      else:
        DFS(row+1,col,0)

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/16/in"+str(prob)+".txt","rt")
    info = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
    dr = [0,0,-1]
    dc = [1,-1,0]
    dirc = [1,2,0]
    for start in range(10):
      end = 1
      if info[0][start] == 1:
        DFS(0,start,0)
        if end == 2:
          print(start)
          break