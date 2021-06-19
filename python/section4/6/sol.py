import sys
for prob in range(1,6):
    sys.stdin = open("section4/6/in"+str(prob)+".txt","rt")
    n = int(input())
    info = []
    for _ in range(n):
        h, w = map(int,input().split())
        info.append((h,w))
    info.sort(reverse=True) #키 순 정렬
    count = 0
    norm_w = 0 #몸무게로 승부하려면 이것보단 커야함
    for h,w in info:
        if w > norm_w:
            count += 1
            norm_w = w #앞으로 몸무게로 승부하려면 나보다는 커라
    print(count)