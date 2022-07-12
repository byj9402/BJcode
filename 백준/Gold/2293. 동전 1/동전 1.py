import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
money = [1] + [0] * k

for i in range(n) : coin.append(int(input()))
for i in coin :
    for j in range(1, k + 1) :
        if j - i >= 0 : money[j] += money[j - i]

print(money[k])