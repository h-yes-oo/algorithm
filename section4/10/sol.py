import sys
for prob in range(1,6):
    sys.stdin = open("section4/10/in"+str(prob)+".txt","rt")
    n = int(input())
    info = list(map(int,input().split()))
    res = [0] * (n)
    position = [info[0]]
    res[info[0]] = 1
    for i in range(1,n):
        value = i + 1
        pos = info[i]
        if pos < min(position):
            res[pos] = value
            position.append(pos)
        else:
            smaller = len(list(filter(lambda x : x != 0, res[:pos])))
            for j in range(smaller+pos,n):
                if res[j] == 0 and len(list(filter(lambda x : x == 0, res[:j]))) == pos :
                    res[j] = value
                    position.append(j)
                    break
    for k in range(0,len(res)-1):
        print(res[k],end=' ')
    print(res[-1])

