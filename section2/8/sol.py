import sys
for problem_num in range(1,6):
    sys.stdin = open("section2/8/in"+str(problem_num)+".txt","rt")
    n = int(input())
    a = list(map(int, input().split()))
    def reverse(x):
        # numbers = []
        # while True:
        #     if(x<10):
        #         numbers.append(x)
        #         break
        #     numbers.append(x%10)
        #     x=x//10
        # result = 0
        # for i in range(len(numbers)):
        #     result += numbers[i] * (10**(len(numbers)-i-1))
        res = 0
        while x>0:
            t = x%10
            res = res*10 + t
            x=x//10
        return res
    
    
    def isPrime(x):
        if x==1:
             return False
        for k in range(2,x):
            if(x%k==0):
                return False
        return True


    for l in range(len(a)):
        res = reverse(a[l])
        if(isPrime(res)):
            print(res, end=' ')
    print()
            