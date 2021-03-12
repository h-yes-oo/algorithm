import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open('section8/13/in'+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    friend = [[float('inf')] * n for _ in range(n)]
    while True:
      a,b = map(int, sys.stdin.readline().split())
      if a==-1 and b==-1:
        break
      friend[a-1][b-1] = 1
      friend[b-1][a-1] = 1
    for i in range(n):
        friend[i][i] = 0
    for k in range(n):
      for i in range(n):
        for j in range(n):
          friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])
          friend[j][i] = friend[i][j]

    res = [0] * n
    for i in range(n):
      res[i] = max(friend[i])
    res_score = min(res)
    count = 0
    res_cand = []
    for i in range(n):
      if res[i] == res_score:
        res_cand.append(i+1)
        count += 1
    print(res_score,end= ' ')
    print(count)
    for i in range(len(res_cand)-1):
      print(res_cand[i], end=' ')
    print(res_cand[-1])
    '''
    - 1 - - -
    1 - 1 1 -
    - 1 - 1 1
    - 1 1 - 1
    - - 1 1 -
    '''
      