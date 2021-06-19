import sys
for prob in range(1,6):
    sys.stdin = open("section5/7/in"+str(prob)+".txt","rt")
    norm = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        standard = [char for char in norm]
        classes = sys.stdin.readline().strip()
        for x in classes:
            if x == standard[0]:
                standard.pop(0)
            elif x in standard:
                print('#%d NO' %(i+1))
                break
            if len(standard) == 0:
                print('#%d YES' %(i+1))
                break
        else:
            print('#%d NO' %(i+1))
        

