import sys
input = sys.stdin.readline

N = int(input())
P = sorted(list(map(int, input().split())))

sum = 0
for i in range(N) : sum += P[i] * (N - i)

print(sum)