import sys
for prob in range(1,6):
    sys.stdin = open("section4/4/in"+str(prob)+".txt", "rt")
    n,c = map(int, input().split())
    position = []
    for _ in range(n):
        position.append(int(input()))
    position.sort()
    def horse(distance):
        idx = 0
        next_idx = 1
        for _ in range(c-1):
            while position[next_idx]-position[idx] < distance:
                next_idx += 1
                if(n <= next_idx):
                    return False
            idx = next_idx
        else:
            return True
    lower = 0
    upper = max(position) - min(position)
    res = -1
    while lower <= upper:
        mid = (lower + upper) // 2
        if horse(mid):
            res=mid
            lower = mid+1
        else:
            upper = mid-1
    print(res)
