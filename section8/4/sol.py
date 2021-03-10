import sys

if __name__ == "__main__":
  for prob in range(1,6):
    sys.stdin = open("section8/4/in"+str(prob)+".txt","rt")
    num = int(sys.stdin.readline())
    info = list(map(int, sys.stdin.readline().split()))
    final = [0] * num
    final[0] = 1
    res = 1
    for i in range(1,num):
      count = 1
      for j in range(i):
        if info[j] < info[i]:
          tmp = final[j] + 1
          if count < tmp:
            count = tmp
      final[i] = count
      if count > res:
        res = count
    print(res)
        
'''
final - i번째 원소 = 마지막 원소가 info[i] 인 최대 증가 수열의 길이
앞의 인덱스들을 훑으면서 나보다 작은 애 중에 길이가 가장 긴 애한테 1을 증가시킨다
Longest Increasing Subsequence(LIS)
'''
      