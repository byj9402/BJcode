import sys

N = int(input())
num = [[]] * N
for i in range(0, N) : num[i] = list(map(int, sys.stdin.readline().split()))

num.sort(key = lambda x : x[1])
num.sort(key = lambda x : x[0])

for i in range(0, N) :
    for j in range(0, 2) : print(num[i][j], end = ' ')
    print()