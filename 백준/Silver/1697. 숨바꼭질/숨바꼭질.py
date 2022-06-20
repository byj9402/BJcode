from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * (10 ** 5 + 1)

def bfs(start, finish, visited) :
    q = deque([start])
    q.append(start)
    while q :
        x = q.popleft()
        if x == finish :
            return visited[x]
        for i in (x - 1, x + 1, 2 * x) :
            if 0 <= i <= 10 ** 5 and not visited[i] :
                visited[i] = visited[x] + 1
                q.append(i)

print(bfs(N, K, visited))