import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()
money = [1] + [0] * k

for i in coin :
    for j in range(i, k + 1) :
        money[j] += money[j - i]

print(money[k])