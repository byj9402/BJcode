import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
num = [i for i in range(1, 1 + N)]
result = list(permutations(num, M))

for i in range(len(result)) : print(*result[i])