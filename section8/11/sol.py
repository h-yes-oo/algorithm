import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/11/in"+str(prob)+".txt","rt")
    n, limit = map(int,sys.stdin.readline().split())
    dy = [0] * (limit+1)
    for i in range(n):
      score, time = map(int,sys.stdin.readline().split())
      for j in range(limit,time-1,-1):
        tmp = dy[j-time] + score
        if tmp > dy[j]:
          dy[j] = tmp
    print(dy[limit])

'''
이전의 냅색 문제와는 달리, 한가지 문제는 단 한 개만 풀 수가 있다
따라서 같은 문제가 중복되지 않도록 냅색을 뒤에서부터 돌린다 !!
'''
