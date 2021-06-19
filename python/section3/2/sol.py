import sys
for prob in range(1,6):
    sys.stdin = open("section3/2/in"+str(prob)+".txt","rt")
    a = input()
    res = 0
    for char in a:
        if char.isdecimal():
            res = res*10 + int(char)
    print(res)
    count = 2
    for i in range(2,res):
        if res%i == 0:
            count += 1
    print(count)
    print()

    #using isdecimal() function