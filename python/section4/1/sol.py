import sys
for prob in range(1,6):
    sys.stdin = open("section4/1/in"+str(prob)+".txt","rt")
    n,m = map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    start = 0
    end = n-1
    while True:
        mid = (start + end) // 2
        if a[mid] > m:
            end = mid-1
        elif a[mid] < m:
            start = mid+1
        else:
            print(mid+1)
            break