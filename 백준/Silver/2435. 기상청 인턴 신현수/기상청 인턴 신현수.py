import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temperature = list(map(int, input().split()))
tempSum = []

for i in range(K, N + 1) : tempSum.append(sum(temperature[i - K:i]))
print(max(tempSum))