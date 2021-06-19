import sys
for i in range(1,6):
    sys.stdin=open("section2/4/in"+str(i)+".txt", "rt")
    n = int(input())
    a= list(map(int, input().split()))
    '''
    total = 0
    for i in range(n):
        total+= a[i]
    average = round(total/n)
    '''
    average = int(sum(a)/n + 0.5) 
    #round는 round_half_even 방식을 따르므로 이렇게 반올림하는 것이 안전

    a=list(map(lambda x:x-average, a))
    smallest=a[0]
    index = 0
    for i in range(n):
        if abs(a[i]) < abs(smallest):
            index = i
            smallest = a[i]
        elif abs(a[i]) == abs(smallest):
            if(a[i]>smallest):
                index = i
                smallest = a[i]

    print("%d %d" %(average,index+1))

