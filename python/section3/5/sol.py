import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section3/5/in"+str(prob)+".txt","rt")
    n,goal = map(int,sys.stdin.readline().split())
    elem = list(map(int,sys.stdin.readline().split()))
    count = 0
    for i in range(n):
      num = 0
      total = 0
      while total < goal and i+num < n and num<=goal:
        total += elem[i+num]
        if total == goal:
          count +=1 
          break
        num += 1
    print(count)

