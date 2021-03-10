import sys

if __name__=="__main__":
  step = int(sys.stdin.readline())
  check = [0]*(step+1)
  check[1]=1
  check[2]=2
  for i in range(3,step+1):
    check[i] = check[i-1] + check[i-2]
  print(check[step])
  