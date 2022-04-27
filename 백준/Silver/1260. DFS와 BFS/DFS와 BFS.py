import sys
from collections import deque

def dfs(graph, start, visited) :
    v = start
    visited[v] = True
    print(v, end = " ")
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, start, visited) :
    queue = deque([start])
    visited[start] = True
    while queue :
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M) :
    s, f = map(int, sys.stdin.readline().split())
    graph[s].append(f)
    graph[f].append(s)

for i in range(len(graph)) : graph[i].sort()

dfs(graph, V, visit)
print()
visit = [False] * (N+1)
bfs(graph, V, visit)