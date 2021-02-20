import sys
for i in range(1,6):
    sys.stdin=open("section2/5/in"+str(i)+".txt", "rt")
    n,m= map(int, input().split())

    total = [0] * (n+m+1) #from 2 to n+m

    for u in range(1,n+1):
        for j in range(1,m+1):
            total[u+j]+=1

    max_value = total[2]
    max_index = [2]
    for k in range(2,n+m+1):
        if(total[k] > max_value):
            max_value = total[k]
            max_index = []
            max_index.append(k)
        elif(total[k] == max_value):
            max_value = total[k]
            max_index.append(k)
    for l in max_index:
        print(l,end=' ')
    print()
