import sys
for prob in range(1,4):
    sys.stdin = open("section6/8/in"+str(prob)+".txt","rt")
    def DFS(level, current):
        global select, count
        if level == select:
            print(current)
            count += 1
            return
        else:
            for x in num_string:
                if x not in current:
                    DFS(level+1, current + ' ' + x)
    num, select = map(int,sys.stdin.readline().strip().split())
    count = 0
    num_string = list(map(str,list(range(1,num+1))))
    for x in num_string:
        DFS(1,x)
    print(count)
