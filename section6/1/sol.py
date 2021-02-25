import sys
for prob in range(1,6):
    sys.stdin = open("section6/1/in"+str(prob)+".txt","rt")
    num = int(sys.stdin.readline())
    def cal(num,x):
        if num == x:
            print('1',end='')
        elif num%(2*x) == x:
            cal(num-x,2*x)
            print('1',end='')
        elif num/(2*x) == 1 and num%(2*x) == 0:
            print('10',end='')
        else:
            cal(num,2*x)
            print('0',end='')
    cal(num,1)
    print()


'''
120/2=60...0
120/4=30...0
120/8=15...0
120/16=7...8
112/32=3...16
96/64=1...32
64/128=0...64

120=1111000
'''