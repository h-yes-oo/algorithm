import sys
for prob in range(1,6):

    def calc_money(a,b,c):
        if a == b == c:
            return 10000 + 1000*a
        elif a == b or a==c:
            return 1000 + 100*a
        elif c == b:
            return 1000 + 100*b
        else:
            return c*100

    sys.stdin = open("section2/9/in"+str(prob)+".txt","rt")
    n = int(input())
    max_value = -1
    for i in range(n):
        tmp = input().split()
        tmp.sort()
        a,b,c = map(int, tmp)
        res = calc_money(a,b,c)
        if res > max_value:
            max_value = res
    print(max_value)
