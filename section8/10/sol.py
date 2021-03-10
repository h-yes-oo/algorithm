import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/10/in"+str(prob)+".txt","rt")
    kind = int(sys.stdin.readline())
    penny = list(map(int,sys.stdin.readline().split()))
    money = int(sys.stdin.readline())
    dy = [float('inf')] * (money+1)
    dy[0] = 0
    for i in range(kind):
      price = penny[i]
      for j in range(price,money+1):
        tmp = dy[j-price] + 1
        if dy[j] > tmp:
          dy[j] = tmp
    print(dy[money])

    '''
    dy[j] : j원을 거슬러 주는데에 사용된 동전의 최소 개수
    '''