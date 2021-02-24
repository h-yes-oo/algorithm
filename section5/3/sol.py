import sys
for prob in range(1,6):
    sys.stdin = open("section5/3/in"+str(prob)+".txt","rt")
    info = sys.stdin.readline().strip()
    result = ''
    stack = []
    for x in info:
        if x.isdecimal():
            result += x
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                result += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.append(x)
    while stack:
        result += stack.pop()
    print(result)