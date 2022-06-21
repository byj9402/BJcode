import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
first = int(input())

temp = []
for i in range(1, N) :
    second = int(input())
    temp.append(second - first)
    first = second

temp.sort()
distance = temp[0]
## 모든 경우의 GCD를 구해야함
for i in range(1, len(temp)) :
    distance = gcd(distance, temp[i])

result = 0
for i in range(len(temp)) :
    result += (temp[i] // distance) - 1

print(result)