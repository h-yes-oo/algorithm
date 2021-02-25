import sys
for prob in range(1,6):
    sys.stdin = open("section6/4/in"+str(prob)+".txt","rt")

    def DFS(x):
        if x == num:
            total = 0
            total_rev = 0
            for i in range(num):
                if ch[i] == 1:
                    total += elems[i]
                else:
                    total_rev += elems[i]
            if total == total_rev:
                flag[0] = 1
                return
        else:
            ch[x] = 1
            DFS(x+1)
            ch[x] = 0
            DFS(x+1)

    num = int(sys.stdin.readline())
    elems = list(map(int,sys.stdin.readline().strip().split()))
    ch = [0] * (num)
    flag = [0]
    DFS(0)
    if flag[0] > 0:
        print("YES")
    else:
        print("NO")
    
