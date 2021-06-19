import sys

def DFS(len):
  if dy[len]>0:
    return dy[len]
  if len == 1 or len == 2:
    return len
  else:
    dy[len] = DFS(len-1)+DFS(len-2)
    return dy[len]

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/1/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    dy = [0]*(n+1)
    print(DFS(n))

'''
메모이제이션 - 메모를 미리 해두고, 불필요한 호출을 방지한다 -> 훨씬 향상된 속도
'''