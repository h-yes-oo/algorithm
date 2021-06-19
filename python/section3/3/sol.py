import sys
for prob in range(1,6):
    sys.stdin = open("section3/3/in"+str(prob)+".txt","rt")
    res = list(range(21))
    for _ in range(10):
        a,b = map(int,input().split())
        size = b+1-a
        for j in range(size//2):
            tmp = res[a+j]
            res[a+j]=res[b-j]
            res[b-j] = tmp
    for j in range(1,21):
        print(res[j],end=' ')
    print()

#list(range(5)) -> [0,1,2,3,4]
#swap in python -> a,b = b,a
