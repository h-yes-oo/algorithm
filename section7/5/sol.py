import sys
def DFS(level, one, two, three):
  global res
  if level == kind:
    diff = max([one,two,three]) - min([one,two,three])
    if diff < res:
      if one == two or two == three or three == one:
        return
      else:
        res = diff
  else:
    DFS(level+1, one + info[level], two, three)
    DFS(level+1, one, two + info[level], three)
    DFS(level+1, one, two, three+ info[level])

if __name__ == "__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/5/in"+str(prob)+".txt","rt")
    kind = int(sys.stdin.readline())
    info = [0] * kind
    for i in range(kind):
      info[i] = int(sys.stdin.readline())
    res = float('inf')
    DFS(0,0,0,0)
    print(res)