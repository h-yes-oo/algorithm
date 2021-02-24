import time
start_time = time.time()
import sys
for prob in range(1,6):
    sys.stdin = open("section5/9/in"+str(prob)+".txt","rt")
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    chars = dict()
    for x in s1:
        chars[x] = chars.get(x, 0) + 1
    for y in s2:
        chars[y] = chars.get(y, 0) - 1
    for key,value in chars.items():
        if value != 0:
            print('NO')
            break
    else:
        print('YES')
print("--- %s seconds ---" % (time.time() - start_time))