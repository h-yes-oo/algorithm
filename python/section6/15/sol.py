import sys
def DFS(go_to):
  global count, n
  if go_to == n:
    count += 1
    # print(path)
  else:
    for i in range(1,n+1):
      if graph[go_to][i] == 1 and res[i] == 0:
        res[i] = 1
        # path.append(i)
        DFS(i)
        res[i] = 0
        # path.pop()

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section6/15/in"+str(prob)+".txt","rt")
    n, m = map(int, sys.stdin.readline().split())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
      i,j = map(int, sys.stdin.readline().split())
      graph[i][j] = 1
    res = [0] * (n+1)
    count = 0
    res[1] = 1
    # path = []
    # path.append(1)
    DFS(1)
    print(count)

'''
graph에서 인덱스 번호를 그대로 사용할 수 있도록 크기를 n이 아니라 n+1로 설정한다
res 는 지나간 노드를 1로 표시 (노드의 중복을 막기위해)
'''

    