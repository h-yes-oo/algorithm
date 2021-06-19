import sys
for prob in range(1,6):
  sys.stdin = open("section6/4/in"+str(prob)+".txt","rt")
  n = int(sys.stdin.readline().strip())
  info = list(map(int,sys.stdin.readline().strip().split()))
  total = sum(info)
  goal = total // 2
  flag = False
  def DFS(level, current_sum):
    global flag
    if level == n:
      return
    if current_sum == goal:
      flag = True
      return
    else:
      DFS(level+1, current_sum+info[level])
      DFS(level+1, current_sum)
  if total%2 == 0:
    DFS(0,0)
  if flag:
    print("YES")
  else:
    print("NO")

