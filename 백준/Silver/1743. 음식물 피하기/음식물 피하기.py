import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M, K = map(int, input().split())
field = [[0] * M for _ in range(N)]
result = []

for _ in range(K) :
    a, b = map(int, input().split())
    field[a - 1][b - 1] = 1

def dfs(field, x, y) :
    global count
    field[x][y] = 0
    count += 1
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M :
            if field[nx][ny] == 1 :
                dfs(field, nx, ny)

for i in range(N) :
    for j in range(M) :
        if field[i][j] == 1 :
            count = 0
            dfs(field, i, j)
            result.append(count)

print(max(result))