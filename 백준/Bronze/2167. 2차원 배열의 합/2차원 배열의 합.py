import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [[0] * m for _ in range(n)]

for i in range(0, n) :
    array[i] = list(map(int, input().split()))

#구간 합
sum = [[0] * (m+1) for _ in range(n+1)]
result = 0
for i in range(1, n+1) :
    for j in range(1, m+1) :
        sum[i][j] = array[i-1][j-1] + sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1]

t = int(input())
    
for _ in range(0, t) :
    x1, y1, x2, y2 = map(int, input().split())
    print(sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1])