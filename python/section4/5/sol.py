import sys
for prob in range(1,6):
    sys.stdin = open("section4/5/in"+str(prob)+".txt","rt")
    n = int(input())
    time = []
    for _ in range(n):
        start, end = map(int, input().split())
        time.append((start,end))
    time.sort(key = lambda x : (x[1], x[0])) #x[1]을 우선으로 정렬하라  
    cnt = 1
    end_time = time[0][1]
    for start, end in time:
        if start >= end_time:
            cnt += 1
            end_time = end
    print(cnt)

#그리디는 대부분 정렬과 관련이 있다