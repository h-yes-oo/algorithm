import sys
from collections import deque
'''
사다리타기 거꾸로 타고 올라가기 !! 생각을 전환하면 이렇게 문제 풀이가 짧아진다
사다리타기에서 유의할 규칙
- 아래로 가는 길이 있어도 오른쪽, 왼쪽 길이 있으면 좌우로 먼저 이동한다
- 한번 밟은 블록은 다시 밟을 수 없다
'''

def DFS(row,col):
  info[row][col] = 0
  if row == 0:
    print(col)
  else:
    if col-1>=0 and info[row][col-1]==1:
      DFS(row,col-1)
    elif col+1 < 10 and info[row][col+1]==1:
      DFS(row,col+1)
    else:
      DFS(row-1,col)


if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/16/in"+str(prob)+".txt","rt")
    info = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
    for i in range(10):
      if info[9][i] == 2:
        DFS(9,i)