import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
line = [[0] * 2 for _ in range(N)]
result = []

for i in range(N) :
    for j in range(i) :
        if num[i] > num[j] and line[i][0] < line[j][0] :
            line[i][0] = line[j][0]
    line[i][0] += 1

for i in range(N - 1, -1, -1) :
    for j in range(N - 1, i - 1, -1) :
        if num[i] > num[j] and line[i][1] < line[j][1] :
            line[i][1] = line[j][1]
    line[i][1] += 1

for i in range(N) :
    result.append(line[i][0] + line[i][1] - 1)

print(max(result))