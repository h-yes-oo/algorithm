import time
start_time = time.time()
import sys
for prob in range(1,6):
    sys.stdin = open("section5/9/in"+str(prob)+".txt","rt")
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    str1=[0]*52
    for x in s1:
        #대문자의 아스키 코드는 65~90
        if x.isupper():
            str1[ord(x)-65] += 1
            #ord는 아스키 코드를 반환해주는 함수
        #소문자의 아스키 코드는 97~122
        else:
            str1[ord(x)-71] += 1
    for x in s2:
        if x.isupper():
            str1[ord(x)-65] -= 1
        else:
            str1[ord(x)-71] -= 1
    for x in str1:
        if x != 0:
            print('NO')
            break
    else:
        print('YES')
print("--- %s seconds ---" % (time.time() - start_time))
