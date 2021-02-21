import sys
for i in range(1,6):
    sys.stdin=open("section2/6/in"+str(i)+".txt","rt")
    n=int(input())
    a=list(map(int,input().split()))
    def digit_sum(x):
        total = 0
        while True:
            total += x%10
            x=x//10
            if(x<10):
                break
        total += x
        return total
    
    result=list(map(digit_sum,a))

    max_value = result[0]
    max_index = 0
    for i in range(len(result)):
        if result[i] > max_value:
            max_value = result[i]
            max_index = i
    print(a[max_index])