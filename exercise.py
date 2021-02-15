'''
print("hello world")

a=1
A=2
_b=5
print(a,A,_b)

a, b = 10,20
a,b = b,a
print(a,b)

a=12.1233338888888888888888
b='student'
c='hihi'
d=4
print(type(a))
print(a,b,c, sep='\n')
print(a, end=' ')
print(b)
print(c)

a=input("숫자를 입력하세요: ")
print(a)

a,b = input("두개를 컴마로 입력하세요").split(',')
print(a)
print(b)
a=int(a)
b=int(b)
print(a+b)

c,d = map(int, input("두 개의 숫자를 입력하세요 : ").split())
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c//d) #몫
print(c%d) #나머지
print(c**d) #거듭제곱

x=11
if x<10:
    print("10보다 작은 자연수")
else:
    print("10보다 큰 수")

x=99
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print("D")
else:
    print("F")


a=range(10) #순차적으로 정수 리스트 
print(list(a))
b=range(1,11)
print(list(b))

for i in range(1,10):
    print(i)


for i in range(10,1,-1):
    print(i)

i=1
while i<=10:
    print(i)
    i=i+1

i=10
while i>=1:
    print(i)
    i=i-1

i=3
while True:
    print(i)
    if i==10:
        break
    i+=1

for i in range(1, 11):
    if i%2 == 0:
        continue
    print(i)

n=int(input())
total=0
for i in range(1, n+1):
    total+=i
print(total)

for i in range(1,n+1):
    if i%2 != 0:
        print(i)

n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')


for i in range(5):
    print('i: ', i, sep='', end=' ')
    for j in range(5):
        print('j: ',j,sep='',end=' ')
    print()

msg="It is Time"
print(msg.upper())
print(msg)
print(msg.lower())
tmp=msg.upper()
print(tmp)
print(tmp.find('t')) #해당 문자의 인덱스 번호, 문자가 없는 경우 -1 반환
print(tmp.find("IS"))
print(tmp.count('T'))
print(msg[:4])
print(msg[3:5])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()
for x in msg:
    if x.isalpha():
        if x.isupper():
            print(x, end=' ')
        if x.islower():
            print('*',end=' ')
    else:
        print(' ', end='')
print()

tmp='AZ'
for x in tmp:
    print(ord(x),end=' ') #아스키 넘버를 출력해줌

tmp=65
print(chr(tmp)) #정수에 대응되는 문자를 출력

import random as r
a=[]
b=list()
print(b)

a=[1,2,3,4,5]
print(a)
print(a[0])
b=list(range(1,11))
print(a+b)

a.append(6) #맨 뒤에 추가
print(a)
a.insert(3,7) #인덱스에 값 추가
print(a)
a.pop() #맨 뒤 값 제거
print(a) 
a.pop(3) # 해당 인덱스 제거
print(a)
a.remove(4) #해당 값 제거
print(a)
print(a.index(5)) #해당 값의 인덱스 출력
a=list(range(1,11))
print(a)
print(sum(a))
print(max(a))
print(min(7,5))
print('min of a:',min(a),sep=' ')
print('before shuffle:',a, sep=' ')
r.shuffle(a)
print('after shuffle:',a, sep=' ')
a.sort()
print('after sort:',a,sep=' ')
a.sort(reverse=True)
print('after reverse sort:',a,sep=' ')
a.clear() # 리스트 내부값 모두 지움
print(a)

a=[23,12,36,53,19]
print(a[:3])
print(a[1:4])
print(a)
for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x%2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x) #(인덱스, 값)의 튜플로 출력
b=(1,2,3,4,5) #튜플은 값 변경이 불가하다는 점에서 리스트와 차이 b[0]=7 과 같은 명령은 불가
print(b[0])

for x in enumerate(a):
    print(x[1], end=' ')
print()
for index, value in enumerate(a):
    print(index,'th element of a: ', value, sep='', end='\n')

norm=11
if all(norm>x for x in a):
    print('all elements are smaller than',norm,'!',sep=' ')
else:
    print('some elements are bigger than',norm,'!',sep=' ')

if any(norm>x for x in a):
    print('some elements are smaller than',norm,'!',sep=' ')
else:
    print('all elements are bigger than',norm,'!',sep=' ')


a=[0]*10
print(a)

a=[[0]*3 for _ in range(5)]
print(a)
a[0][1]=1
a[1][2]=2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()

def printSum(a, b):
    print(a+b)

printSum(3,4)
printSum(5,7)

def add(a,b):
    return a+b

print(add(3,4))

def add_and_minus(a,b):
    c=a+b
    d=a-b
    return c,d #파이썬은 두 변수를 함께 반환 가능 이 경우 튜플로 반환됨

print(add_and_minus(5,1))

def isPrime(x):
    for i in range(2,x):
        if(x%i == 0):
            return False
    return True

print(isPrime(13))
print(isPrime(14))
'''

def plus_one(x):
    return x+1
print(plus_one(3))

#lambda function

plus_two=lambda x: x+2
print(plus_two(1))

a=[1,2,3]
print(list(map(plus_one,a)))
print(list(map(lambda x: x+2, a)))