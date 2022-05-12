import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

house = []
sum = []
for _ in range(int(input())) : house.append(list(map(int, input().strip())))

def dfs(graph, x, y) :
    global count
    count = count + 1
    graph[x][y] = 0
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph) :
            if graph[nx][ny] == 1 :
                dfs(graph, nx, ny)
    return count

for i in range(len(house)) :
    for j in range(len(house)) :
        if house[i][j] == 1 :
            count = 0
            sum.append(dfs(house, i, j))

sum.sort()
print(len(sum))
for i in range(len(sum)) : print(sum[i])