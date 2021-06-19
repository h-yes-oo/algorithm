import sys
for prob in range(1,6):
    sys.stdin = open("section6/4/in"+str(prob)+".txt","rt")
    def DFS(level, sum):
        global flag
        if(sum > total/2):
            return
        if(flag == 1):
            return
        if level == num:
            if sum == (total - sum):
                flag=1
                return
        else:
            DFS(level+1,sum + elem[level])
            DFS(level+1, sum)
    flag=0
    num = int(sys.stdin.readline())
    elem = list(map(int,sys.stdin.readline().strip().split()))
    total = sum(elem)
    DFS(0,0)
    if flag == 0:
        print("NO")
    else:
        print("YES")