import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
field = []
rain = []
water = []
for _ in range(N) :
    field.append(list(map(int, input().split())))

cnt = 0
def dfs(map, level, x, y) :
    map[x][y] = 0
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(map) and 0 <= ny < len(map) :
            if map[nx][ny] > level :
                dfs(map, level, nx, ny)

for level in range(0, 101) :
    cnt = 0
    rain = copy.deepcopy(field)
    for i in range(N) :
        for j in range(N) :
            if rain[i][j] > level :
                cnt += 1
                dfs(rain, level, i, j)
    water.append(cnt)

print(max(water))
