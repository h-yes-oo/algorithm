import sys
for prob in range(1,6):
    sys.stdin = open("section4/3/in"+str(prob)+".txt","rt")
    n,m = map(int, input().split())
    song = list(map(int,input().split()))
    def contain(capacity):
        total = 0
        gaze = 0
        for i in range(n):
            gaze = gaze + song[i]
            if(gaze > capacity):
                total += 1
                gaze = song[i]
        if(gaze > 0):
            total += 1
        return total

    lower = max(song) #최소 범위에 주의
    upper = sum(song)
    res = 0
    while lower<=upper:
        mid = (lower + upper ) // 2
        if contain(mid) > m:
            lower = mid + 1
        elif contain(mid) <= m:
            res = mid
            upper = mid - 1
    print(res)