import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/6/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    bricks = []
    for i in range(n):
      a,b,c = map(int, sys.stdin.readline().split())
      bricks.append((a,b,c))
    bricks.sort(reverse=True)
    check = [0] * n
    check[0] = bricks[0][1]
    res = bricks[0][1]
    for i in range(1,n):
      max_height = 0
      for j in range(i-1,-1,-1):
        if bricks[j][2] > bricks[i][2] and max_height < check[j]:
          max_height = check[j]
      max_height += bricks[i][1]
      check[i] = max_height
      if max_height > res:
        res = max_height
    print(res)