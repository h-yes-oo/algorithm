import sys
for problem in range(1,6):
    sys.stdin = open("section2/7/in"+str(problem)+".txt", "rt")
    n = int(input())
    ch = [0] * (n+1) #인덱스 번호를 그 수라고 생각하고 풀기
    cnt = 0
    for i in range(2,n+1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i,n+1, i): #증가하는 스텝을 지정해주는 것이 중요
                ch[j] = 1
    print(cnt, end= ' ')
