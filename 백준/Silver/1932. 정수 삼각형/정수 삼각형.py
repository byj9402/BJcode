import sys
input = sys.stdin.readline

T = []
n = int(input())

# 삼각형 list
for i in range(n) : T.insert(len(T), list(map(int, input().split())))

for i in range(1, n) :
    for j in range(i + 1) :
        if j == 0 : T[i][j] += T[i - 1][j]
        elif i == j : T[i][j] += T[i - 1][j - 1]
        else : T[i][j] += max(T[i - 1][j], T[i - 1][j - 1])

print(max(T[n - 1]))