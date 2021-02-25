import sys
for prob in range(1,6):
    sys.stdin = open("section6/1/in"+str(prob)+".txt","rt")
    def DFS(x):
        if x==0:
            return
        else:
            DFS(x//2)
            print(x%2,end='')
    if __name__=="__main__":
        num = int(sys.stdin.readline())
        DFS(num)
        print()