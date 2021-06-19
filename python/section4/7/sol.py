import sys
for prob in range(1,6):
    sys.stdin = open("section4/7/in"+str(prob)+".txt","rt")
    l = int(input())
    h = list(map(int,input().split()))
    m = int(input())
    h.sort(reverse=True)
    for _ in range(m):
        h[0] -= 1
        h[-1] += 1
        h.sort(reverse=True)
    print(h[0]-h[-1])
