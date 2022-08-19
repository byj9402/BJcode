import sys
from collections import deque
sys.setrecursionlimit = (10 ** 6)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
field = []
for _ in range(N) :
    field.append(list(map(int, input().strip())))
    
def bfs(x, y) :
    queue = deque()
    queue.append((x, y))
    while(queue) :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if field[nx][ny] == 1 :
                    field[nx][ny] = field[x][y] + 1
                    queue.append((nx, ny))
    return

bfs(0, 0)
print(field[-1][-1])
    