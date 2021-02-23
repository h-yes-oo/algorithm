import sys
for prob in range(1,6):
    sys.stdin = open("section2/10/in"+str(prob)+".txt","rt")
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(1,n):
        if(a[i] == 1):
            a[i] += a[i-1]
    print(sum(a))