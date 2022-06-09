import sys
input = sys.stdin.readline

num = [int(input()) for _ in range(5)]
num.sort()

## 평균
print(sum(num)//5)
## 중앙값
print(num[2])