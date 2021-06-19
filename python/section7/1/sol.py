import sys
# import time

def DFS(level, score_sum, time_left):
  global result
  if time_left < 0:
    return
  if level == n :
    if score_sum > result:
      result = score_sum
    return
  if score_sum + sum(score[level : ]) < result:
    return
  else:
      DFS(level+1, score_sum, time_left)
      DFS(level+1, score_sum + score[level], time_left - times[level])

if __name__=="__main__":
  # start_time = time.time()
  for prob in range(1,6):
    sys.stdin = open("section7/1/in"+str(prob)+".txt","rt")
    n, limit = map(int, sys.stdin.readline().split())
    score = [0] * n
    times = [0] * n
    for i in range(n):
      s, t = map(int, sys.stdin.readline().split())
      score[i] = s
      times[i] = t
    result = 0
    DFS(0,0,limit)
    print(result)
  # print("--- %s seconds ---" % (time.time() - start_time))

'''
level : 현재 결정할 문제의 인덱스
'''