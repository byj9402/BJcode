import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(graph, x, y, N, M) :
    graph[x][y] = 0
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N :
            if graph[nx][ny] == 1 :
                dfs(graph, nx, ny, N, M)

while (True) :
    field = []
    cnt = 0
    N, M = map(int, input().split())
    if N == 0 and M == 0 : break
    for _ in range(M) : field.append(list(map(int, input().split())))
    for x in range(M) :
        for y in range(N) :
            if field[x][y] == 1 :
                cnt += 1
                dfs(field, x, y, N, M)
    print(cnt)