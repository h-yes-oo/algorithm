import sys

def DFS(x_now, y_now):
  global count
  if x_now == end[0] and y_now == end[1]:
    count += 1
    return
  else:
    for i in range(4):
      x = x_now + dx[i]
      y = y_now + dy[i]
      if n>x>=0 and n>y>=0 and check[x][y] == 0 and mount[x][y] > mount[x_now][y_now]:
        check[x][y] = 1
        DFS(x,y)
        check[x][y] = 0


if __name__ == "__main__":
  for prob in range(1,6):
    sys.stdin = open("section7/11/in"+str(prob)+".txt","rt")
    n = int(sys.stdin.readline())
    mount = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    highest = mount[0][0]
    lowest = mount[0][0]
    start = (0,0)
    end = (0,0)
    for i in range(n):
      for j in range(n):
        if mount[i][j] > highest:
          highest = mount[i][j]
          end = (i,j)
        elif mount[i][j] < lowest:
          lowest = mount[i][j]
          start = (i,j)

    check = [[0] * n for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    count = 0

    check[start[0]][start[1]] == 1
    DFS(start[0],start[1])

    print(count)
      