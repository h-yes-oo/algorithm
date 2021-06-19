import sys
for prob in range(1,6):
    sys.stdin = open("section6/6/in"+str(prob)+".txt","rt")
    def DFS(level,current):
        if level == times-1:
            print(current)
            return
        else:
            for j in num_str:
                DFS(level+1, current+' '+j)
    num, times = map(int,sys.stdin.readline().strip().split())
    total_times = num ** times
    num_str = list(map(str,list(range(1,num+1))))
    for i in num_str:
        DFS(0,i)
    print(total_times)