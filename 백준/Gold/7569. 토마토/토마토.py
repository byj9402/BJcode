import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = []
queue = deque()

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(H) :
    temp = []
    for j in range(N) :
        temp.append(list(map(int, input().split())))
        for k in range(M) :
            if temp[j][k] == 1 : queue.append([i, j, k])
    tomato.append(temp)

while(queue) :
    x, y, z = queue.popleft()
    for i in range(6) :
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M :
            if tomato[nx][ny][nz] == 0 :
                queue.append([nx, ny ,nz])
                tomato[nx][ny][nz] = tomato[x][y][z] + 1

result = True
day = 0
for box in tomato :
    for line in box :
        for i in line : 
            if i == 0 : result = False
        day = max(day, max(line))
if result : print(day - 1)
else : print(-1)