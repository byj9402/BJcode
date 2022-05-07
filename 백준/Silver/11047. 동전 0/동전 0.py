import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 지폐를 저장하는 list
money = []
# 지폐의 개수를 저장하는 list
result = [0] * N

for _ in range(N) : money.append(int(input()))
for i in range(N - 1, -1, -1) :
    result[i] = K // money[i]
    K %= money[i]

print(sum(result))