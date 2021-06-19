import sys
def check(str):
    str = str.lower()
    for j in range(len(str)//2):
        if str[j] != str[-1-j]:
            return("NO")
    else:
        return("YES")

for prob in range(1,6):
    sys.stdin = open("section3/1/in"+str(prob)+".txt","rt")
    n = int(input())
    for i in range(n):
        a = input()
        print("#%d %s" %(i+1,check(a)))
    print()


#프린트 형식 print("%d %s" %(a,b)) 에 주의 !