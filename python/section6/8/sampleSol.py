import sys
for prob in range(1,4):
    sys.stdin = open("section6/8/in"+str(prob)+".txt","rt")
    def DFS(level):
        global count
        if level == select:
            for i in range(level):
                print(res[i], end=' ')
            print()
            count += 1
        else:
            for j in range(1, num+1):
                if ch[j] == 0:
                    ch[j] = 1
                    res[level] = j
                    DFS(level+1)
                    ch[j]=0
    num, select = map(int,sys.stdin.readline().strip().split())
    res = [0] * num
    ch = [0] * (num+1)
    count = 0
    DFS(0)
    print(count)