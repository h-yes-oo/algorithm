import sys

if __name__ == "__main__":
  for prob in range(1,6):
    sys.stdin = open("section3/4/in"+str(prob)+".txt","rt")
    n=int(sys.stdin.readline())
    e1 = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    e2 = list(map(int,sys.stdin.readline().split()))
    res = [0] * (n+m)
    idx1 = 0
    idx2 = 0
    for i in range(n+m):
      if idx1 < n and idx2 < m:
        if e1[idx1] < e2[idx2]:
          res[i] = e1[idx1]
          idx1 += 1
        else:
          res[i] = e2[idx2]
          idx2 += 1
      elif idx1 == n:
        res[i] = e2[idx2]
        idx2 += 1
      elif idx2 == m:
        res[i] = e1[idx1]
        idx1 += 1
    print(res)