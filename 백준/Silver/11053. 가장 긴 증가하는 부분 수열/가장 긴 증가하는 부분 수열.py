import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
result = [0] * N

for i in range(N) :
    for j in range(i) :
        if num[i] > num[j] and result[i] < result[j] :
            result[i] = result[j]
    result[i] += 1

print(max(result))