import sys
for prob in range(1,6):
    sys.stdin = open("section4/8/in"+str(prob)+".txt","rt")
    n,m = map(int,input().split())
    info = list(map(int,input().split()))
    info.sort()
    count = 0
    while len(info) > 1:
        if(info[-1]+info[0] <= m):
            info.pop(-1)
            info.pop(0) #길이가 1인 리스트에서는 인덱스 -1과 0이 동일
            count += 1
        else:
            info.pop(-1)
            count += 1
    if len(info) == 1:
        if info[0] <= m :
            count += 1
    print(count)