import time
start_time = time.time()
import sys
for prob in range(1,6):
    sys.stdin = open("section6/5/in"+str(prob)+".txt","rt")
    def DFS(level, total, tsum):
        global res, all_dogs
        if total > upper:
            return
        if (total + all_dogs - tsum) < res:
            #남은 강아지들을 다 데려와도 지금까지의 최대값보다 작다면 가지를 더이상 치지 않는다
            return
        if level == num:
            if res < total:
                res = total
        else:
            DFS(level+1, total + dogs[level], tsum + dogs[level])
            DFS(level+1, total, tsum + dogs[level])
    upper, num = map(int,sys.stdin.readline().strip().split())
    dogs = [0] * num
    res = -1
    for i in range(num):
        dogs[i] = int(sys.stdin.readline())
    all_dogs = sum(dogs)
    DFS(0,0,0)
    print(res)
print("--- %s seconds ---" % (time.time() - start_time))