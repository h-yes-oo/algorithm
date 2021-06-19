import sys
for prob in range(1,6):
  sys.stdin = open("section6/10/in"+str(prob)+".txt","rt")
  n, m = map(int,sys.stdin.readline().strip().split())
  check = [0] * m
  res = 0
  def DFS(level,current):
    global res
    if level == m:
      for i in range(m-1):
          print(check[i],end=' ')
      print(check[-1])
      res += 1
    else:
      for j in range(current,n+1):
        check[level]=j
        DFS(level+1,j+1)
  DFS(0,1)
  print(res)

'''
n - 1부터 n까지 선택 가능
m - m개를 뽑고 싶음
check - 선택된 숫자들의 리스트 / 크기 m
res - 선택이 끝난 조합의 누적 수

DFS
level - 지금까지 뽑은 숫자들의 누적 수
current - 앞으로 이 숫자부터 n까지만 뽑을 수 있다
'''
