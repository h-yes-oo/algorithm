import sys
for prob in range(1,6):
    sys.stdin = open("section6/3/in"+str(prob)+".txt","rt")
    num = int(sys.stdin.readline())
    def DFS(v):
        if v==num+1:
            for i in range(1,num+1):
                if ch[i] == 1:
                    print(i, end=' ')
            print()
        else:
            ch[v]=1
            DFS(v+1)
            ch[v]=0
            DFS(v+1)
    ch=[0]*(num+1)
    DFS(1)
    

'''
111
110
101
100
011
010
001
000 출력하지 않음
'''