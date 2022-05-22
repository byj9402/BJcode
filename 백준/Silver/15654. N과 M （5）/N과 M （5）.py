import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

result = list(permutations(num, M))
for i in range(len(result)) : print(*list(result[i]))