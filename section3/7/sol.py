import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section3/7/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    apple = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    middle = n // 2
    total = 0
    for row in range(0,middle):
      for col in range(middle-row,middle+row+1):
        total += apple[row][col]
    total += sum(apple[middle])
    for row in range(middle+1, n):
      idx = n - 1 - row
      for col in range(middle-idx,middle+idx+1):
        total += apple[row][col]
    print(total)



    '''
    2
    123
    012345
    123
    2
    '''