import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
result = 0

from itertools import combinations
for i in range(1, N+1):
    comb = combinations(num, i)
    for x in comb:
        if sum(x) == S:
            result += 1

print(result)