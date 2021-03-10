import sys

if __name__=="__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/1/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    check = [0] * (n+1)
    check[1] = 1
    check[2] = 2
    for i in range(3,n+1):
      check[i] = check[i-1]+check[i-2]
    print(check[n])

'''
DFS를 사용하면 시간 초과 발생
점화식을 구하여 풀기 !
F(n) = F(n-1) + F(n-2)
'''