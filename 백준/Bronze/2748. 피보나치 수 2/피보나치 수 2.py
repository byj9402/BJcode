import sys
input = sys.stdin.readline

result = [0, 1]
N = int(input())

if N >= 2 :
    for i in range(2, N+1) :
        tmp = result[i-2] + result[i-1]
        result.append(tmp)

print(result[N])