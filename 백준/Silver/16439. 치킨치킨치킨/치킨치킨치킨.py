import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
prefer = []

for _ in range(N) :
    prefer.append(list(map(int, input().split())))

result = 0
for a, b, c in combinations(range(M), 3) :
    temp = 0
    for i in range(N) :
        temp += max(prefer[i][a], prefer[i][b], prefer[i][c])
    result = max(result, temp)

print(result)