import sys
input = sys.stdin.readline

result = [1] * 100001

for i in range(2, 10001) :
    result[i] += result[i - 2]

for i in range(3, 10001) :
    result[i] += result[i - 3]

for _ in range(int(input())) :
    n = int(input())
    print(result[n])