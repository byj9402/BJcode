import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
friend = [[] for _ in range(N + 1)]

for _ in range(M) :
    x, y = map(int, input().split())
    friend[x].append(y)
    friend[y].append(x)

def bfs(friend, start, visited) :
    count = [0] * (N + 1)
    visited[start] = [True]
    queue = deque([start])
    while (queue) :
        n = queue.popleft()
        for x in friend[n] :
            if not visited[x] :
                count[x] = count[n] + 1
                queue.append(x)
                visited[x] = True
    return sum(count)

result = []
for i in range(1, N+1) :
    visited = [False] * (N + 1)
    result.append(bfs(friend, i, visited))

print(result.index(min(result)) + 1)