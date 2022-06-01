import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(graph, x, visited, result) :
    visited[x] = True
    for i in graph[x] :
        if not visited[i] :
            result[i] = result[x] + 1
            dfs(graph, i, visited, result)
    return

N = int(input())
x, y = map(int, input().split())
family = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(int(input())) :
    a, b = map(int, input().split())
    family[a].append(b)
    family[b].append(a)

result = [0] * (N + 1)
dfs(family, x, visited, result)

if result[y] == 0 : print(-1)
else : print(result[y])