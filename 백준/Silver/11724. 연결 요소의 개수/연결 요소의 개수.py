import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N+1)

for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, start, visited) :
    visited[start] = True
    for x in graph[start] :
        if not visited[x] :
            dfs(graph, x, visited)
cnt = 0
for i in range(1, N + 1) :
    if not visited[i] :
        cnt += 1
        dfs(graph, i, visited)
    
print(cnt)