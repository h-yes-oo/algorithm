import sys
for prob in range(1,6):
    sys.stdin = open("section6/7/in"+str(prob)+".txt","rt")

    def DFS(level, remain):
        global res, min_type, max_type
        if remain == 0:
            if level < res:
                res = level
            return
        elif level + (remain // max_type) > res:
            #이미 최소 경우를 넘은 경우
            return
        elif remain - min_type < 0:
            #답이 안나오는 경우
            return
        else:
            for x in types:
                DFS(level+1, remain-x)

    num = int(sys.stdin.readline().strip())

    types = list(map(int,sys.stdin.readline().strip().split()))
    types.sort(reverse=True) #가지를 뻗을때에 큰 동전부터 적용하여 좀더 빠르게 최솟값을 얻을 수 있다
    min_type = types[-1]
    max_type = types[0]

    money = int(sys.stdin.readline().strip())

    res=float('inf')
    DFS(0,money)
    print(res)