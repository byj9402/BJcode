import sys
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y) :
    graph[x][y]= 0
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[nx]) :
            if graph[nx][ny] == 1 :
                dfs(graph, nx, ny)

for _ in range(int(input())) :
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]

    for _ in range(K) :
        x, y = map(int, input().split())
        field[x][y] = 1

    cnt = 0
    for i in range(M) :
        for j in range(N) :
            if field[i][j] == 1 :
                cnt += 1
                dfs(field, i, j)
    print(cnt)