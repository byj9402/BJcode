from re import L
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
n, m = min(n, m), max(n, m)
coke = 10000
result = 0

for i in range(t//n + 1, -1, -1) :
    temp = t - i * n
    burger = i + temp // m
    if temp % m == 0 :
        coke = 0
        result = burger
        break
    elif temp % m < coke :
        coke = temp % m
        result = burger

print(result, coke)