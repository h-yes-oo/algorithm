import sys
for prob in range(1,6):
    sys.stdin = open("section5/2/in"+str(prob)+".txt","rt")
    info = sys.stdin.readline().strip()
    res =[]
    before = False
    total = 0
    for x in info:
        if x == '(':
            res.append('(')
            before = True
        elif x == ')':
            if before == True:
                res.pop()
                total += len(res)
            else:
                res.pop()
                total += 1
            before = False
    print(total)