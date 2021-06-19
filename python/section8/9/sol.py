import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/9/in"+str(prob)+".txt","rt")
    kind, limit = map(int,sys.stdin.readline().split())
    dy = [0] * (limit+1)
    for i in range(kind):
      w, p = map(int,sys.stdin.readline().split())
      for j in range(w,limit+1):
        tmp = dy[j-w] + p
        if dy[j] < tmp:
          dy[j] = tmp
    print(dy[limit])


    '''
    dy[j] : 가방에 j까지 담을 수 있을때에, 가방에 담을 수 있는 보석의 최대 가치
    '''