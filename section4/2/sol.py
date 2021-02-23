import sys
for prob in range(1,6):
    sys.stdin = open("section4/2/in"+str(prob)+".txt","rt")
    k,n = map(int, input().split())
    exists = []
    for _ in range(k):
        exists.append(int(input()))
    upper = sum(exists) // n
    lower = 1
    def num_of_stick(x):
        return sum(list(map(lambda y: y//x, exists)))
    res=0
    while lower<=upper:
        mid = (upper + lower) //2
        if num_of_stick(mid) >= n:
            res=mid
            lower = mid+1
        elif num_of_stick(mid) < n:
            upper = mid-1
    print(res)

'''
    for i in range(upper,0,-k):
        if sum(list(map(lambda x: x//i, exists))) >= n:
            reach = i
            break
    for j in range(reach+k-1, reach-1, -1):
        if sum(list(map(lambda x: x//j, exists))) >= n:
            print(j)
            break
'''

'''
결정 알고리즘 : 답이 특정 범위 안에 있다는 것을 알 때, 범위를 점점 좁혀 나가며 답을 찾는것
반으로 쪼개가며 찾는 것이 가장 빠름 !
'''