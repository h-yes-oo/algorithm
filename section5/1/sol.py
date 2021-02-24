import sys
for prob in range(1,6):
    sys.stdin = open("section5/1/in"+str(prob)+".txt","rt")
    num, m = map(int,sys.stdin.readline().strip().split())
    num=list(map(int,str(num)))
    stack=[]
    for x in num:
        while stack and m>0 and stack[-1]<x:
            stack.pop()
            m -= 1
        stack.append(x)
    if m>0:
        stack = stack[:-m]
    for i in stack:
        print(i,end='')
    print()
