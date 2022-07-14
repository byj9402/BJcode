import sys
input = sys.stdin.readline

result = [1, 1, 2] + [0] * 999998

for i in range(3, 1000001) :
    result[i] = result[i - 1] % 1000000009 + result[i - 2] % 1000000009 + result[i - 3] % 1000000009

for i in range(int(input())) :
    n = int(input())
    print(result[n] % 1000000009)