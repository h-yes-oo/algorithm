import sys
for prob in range(1,6):
    sys.stdin = open("section4/10/in"+str(prob)+".txt","rt")
    n = int(input())
    info = list(map(int,input().split()))
    res = [0] * n
    for i in range(n):
        for j in range(n):
            if info[i]==0 and res[j]==0:
                res[j]=i+1
                break
            elif res[j]==0:
                info[i]-=1
    for k in range(0,len(res)-1):
        print(res[k],end=' ')
    print(res[-1])