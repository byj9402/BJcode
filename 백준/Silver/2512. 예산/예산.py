import sys
input = sys.stdin.readline

N = int(input())
budget = sorted(list(map(int, input().split())))
total = int(input())
result = 0

for i in range(N) :
    temp = total // (N - i)
    if budget[i] < temp :
        total -= budget[i]
        result = budget[i]
    else :
        result = temp
        break

print(result)