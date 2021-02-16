import sys
sys.stdin=open("/Users/hyesoo/Desktop/algorithm/2-1.kth_divider/in5.txt", "rt")
n, k=map(int, input().split())

def find_kth_divider(n,k):
    divider = 0
    for i in range(1,n+1):
        if n%i == 0:
            divider += 1
            if(divider == k):
                return(i)
    return(-1)

print(find_kth_divider(n,k))

#강의 답안
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        cnt += 1
    if cnt==k:
        print(i)
        break
else:
    print(-1)
