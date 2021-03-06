import sys

def DFS(level, pay_sum):
  global res
  if pay_sum + sum(pay[level:]) < res:
    return
  if level == n:
    if res < pay_sum:
      res = pay_sum
  else:
    next_level = level + days[level]
    if next_level <= n:
      DFS(next_level, pay_sum + pay[level])
    DFS(level + 1, pay_sum)


if __name__=="__main__":
  for prob in range(1,6):
    #sys.stdin = open("section7/2/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    days = [0] * n
    pay = [0] * n
    for i in range(n):
      d,p = map(int,sys.stdin.readline().split())
      days[i] = d
      pay[i] = p
    res = 0
    DFS(0,0)
    print(res)

'''
level이 날짜가 된다 !!
'''