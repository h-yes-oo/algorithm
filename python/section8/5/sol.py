import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/5/in"+str(prob)+".txt","rt")
    num = int(sys.stdin.readline())
    elem = list(map(int, sys.stdin.readline().split()))
    check = [0] * num
    check[0] = 1
    res = 1
    for i in range(1,num):
      max_line = 1
      for j in range(i-1,-1,-1):
        if elem[i] > elem[j] and check[j] + 1 > max_line:
          max_line = check[j] + 1
      check[i] = max_line
      if max_line > res:
        res = max_line
    print(res)
    