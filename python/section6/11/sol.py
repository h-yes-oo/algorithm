import sys
for prob in range(1,6):
  sys.stdin = open("section6/11/in"+str(prob)+".txt","rt")
  n, k = map(int, sys.stdin.readline().split())
  elems = list(map(int, sys.stdin.readline().split()))
  m = int(sys.stdin.readline())
  #res = [0] * k
  count = 0
  def DFS(level, current, sum):
    global count
    if level == k:
      if sum%m == 0:
        count += 1
    else:
      for j in range(current, n):
        #res[level] = elems[j]
        DFS(level+1, j+1, sum+elems[j])
  DFS(0,0,0)
  print(count)

'''
level - 현재까지 뽑은 숫자의 개수
sum - 현재까지 뽑은 수들의 합
count - 정답이 될 수 있는 가지들의 누적 개수
'''