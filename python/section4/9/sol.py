import sys
for prob in range(1,6):
    sys.stdin = open("section4/9/in"+str(prob)+".txt","rt")
    n = int(input())
    info = list(map(int,input().split()))
    last = 0
    direction = []
    while len(info) > 1:
        if last < info[0] < info[-1] or info[-1] < last < info[0]:
            last = info[0]
            direction.append('L')
            info.pop(0)
        elif last < info[-1] < info[0] or info[0] < last < info[-1]:
            last = info[-1]
            direction.append('R')
            info.pop(-1)
        else:
            break
    if len(info) == 1 and info[0] > last:
        direction.append('L')
        
    print(len(direction))
    for x in direction:
        print(x,end='')
    print()


