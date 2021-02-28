import sys
for prob in range(1,6):
    sys.stdin = open("section6/9/in"+str(prob)+".txt","rt")
    n, result = map(int,sys.stdin.readline().strip().split())

    times = [0] * n
    times[0] = 1
    # for i in range(1,n):
    #     for j in range(i,0,-1):
    #         times[j] += times[j-1]

    for i in range(1,n):
        times[i] = times[i-1]*(n-i)//i

    flag = False
    res=[0] * n
    check=[0] * (n+1)
    def DFS(level):
        global flag
        if flag == True:
            return
        if level == n:
            total = 0
            for i in range(n):
                total += res[i]*times[i]
            if total == result:
                flag = True
                #res가 바뀌기 전에 이때 바로 출력해주기 !
                for i in range(n-1):
                    print(res[i],end=' ')
                print(res[-1]) 
                return
        else:
            for i in range(1,n+1):
                if check[i]==0:
                    res[level] = i
                    check[i]=1
                    DFS(level+1)
                    check[i]=0
    DFS(0)

        

    '''
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    [1,5,10,10,5,1]
    [1,6,15,20,15,6,1]
    '''