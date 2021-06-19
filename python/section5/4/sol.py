import sys
for prob in range(1,6):
    sys.stdin = open("section5/4/in"+str(prob)+".txt","rt")
    info = sys.stdin.readline().strip()
    stack = []
    for x in info:
        if x.isdecimal():
            stack.append(int(x))
        elif x == '+':
            stack.append(stack.pop() + stack.pop())
        elif x == '*':
            stack.append(stack.pop() * stack.pop())
        elif x == '-':
            stack.append( stack.pop(-2) - stack.pop() )
        elif x == '/':
            stack.append( stack.pop(-2) / stack.pop() )
    print(stack[0])