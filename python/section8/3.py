import sys

if __name__ == "__main__":
  stone = int(sys.stdin.readline())
  check = [0] * (stone + 1)
  check[1]=2
  check[0]=1
  for i in range(2,stone+1):
    check[i] = check[i-1] + check[i-2]
  print(check[stone])